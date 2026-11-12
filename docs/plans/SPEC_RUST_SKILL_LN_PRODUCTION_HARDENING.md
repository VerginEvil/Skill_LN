# Specification: Native Rust `skill-ln` Production Hardening & Live CloudSuite Integration (`Phase 6`)

Status: ready-for-agent

- **Feature Directory**: [`.scratch/rust-skill-ln-production-hardening/`](../../.scratch/rust-skill-ln-production-hardening/)
- **Companion Plan**: [`docs/plans/rust-skill-ln-production-hardening-plan.md`](rust-skill-ln-production-hardening-plan.md)
- **Parent Architecture Spec**: [`docs/plans/SPEC_NATIVE_RUST_SKILL_LN.md`](SPEC_NATIVE_RUST_SKILL_LN.md)
- **Architecture Decision Record**: [`docs/adr/0021-native-rust-skill-ln-single-binary-architecture.md`](../adr/0021-native-rust-skill-ln-single-binary-architecture.md)
- **Active Ticket Roster**: [`docs/plans/Tickets.md`](Tickets.md)
- **Target Execution Model**: `flash` (Gemini 3.8 Flash High)

---

## Problem Statement

While Phases 1–5 of ADR 0021 built all 9 internal Rust workspace crates (`ln-eclipse-compat`, `ln-auth`, `ln-jca`, `ln-daemon`, `ln-kb`, `ln-linter`, `ln-model`, `ln-scm`, `ln-verify`) and compiled the unified `skill-ln` binary, a two-axis `/code-review` (`Standards` + `Spec`) combined with live integration testing against **Infor CloudSuite `SCS_TEST` (`SCS_TST`)**, Activity **`dev_natt_v01108-1` (`EXTce01108`)**, and **LN Studio Build 0640** uncovered **7 critical production blockers** that prevent `skill-ln` from replacing the Python toolchain in real-world agent workflows:

1. **Blocker 1 — Unwired Hardcoded Stubs in CLI (`commands.rs`) & MCP (`mcp/tools.rs`) + Legacy Plural Path Regression**:
   - In `rust/bins/skill-ln/src/commands.rs`, 30+ server/SCM/code-intelligence/daemon subcommands (`environments`, `project`, `project-info`, `activity`, `clean-activity`, `move-components`, `clean-components`, `daemon`, `explorer`, `get-component`, `sync-reference`, `clone-component`, `checkout-component`, `uncheckout-component`, `checkin-component`, `checkout-activity`, `checkin-activity`, `prepare-end-activity`, `compile-source`, `search-server`, `call-hierarchy`, `open-declaration`, `related-components`, `revisions`, `diff-component`, `generate-report-server`, `build`) are hardcoded `println!` stubs that never invoke `ln-scm`, `ln-daemon`, or `ln-auth`.
   - `new-activity` and `open-activity` only call `bootstrap_local_activity` with a hardcoded `"B61U_a_ext"` release instead of invoking `ln_scm::activity::create_remote_activity` / `open_remote_activity`.
   - `deploy-test` (lines 543–555) hardcodes `HttpClient::new("http://localhost:8080/jca", "")` and project `"EXTce01107"` instead of resolving the workspace's active `.prefs` endpoint, OAuth2 token, and `.project` metadata.
   - `message`, `question`, `function`, `additional`, and `report` in `commands.rs` (lines 376–421) and `ln_create_component` in `mcp/tools.rs` (lines 702–707) bypass `ln_model::generators::*` and write 1-line XML with attributes (`<DR_Message name='...'/>`) into legacy plural directories (`messages/`, `questions/`, `functions/`, `additional/`, `reports/`), directly violating **ADR 0012** and **ADR 0021** Single-XML TDE zero-attribute layout (`{pkg}/{type}/{mod}/{name}.{ext}`).
   - In `rust/bins/skill-ln/src/mcp/tools.rs`, 23 of the 25 MCP tools ignore their workspace/server execution path and return hardcoded mock JSON (`"project": "EXTce01107"`, `"revision": 2`, etc.).
2. **Blocker 2 — JCA Connection Point vs. Numeric `conid` Mismatch (`HTTP 500 POST request failed` on Live CloudSuite)**:
   - Every function in `ln-scm` (`project.rs`, `activity.rs`, `explorer.rs`, `scm_engine.rs`, `build.rs`, `code_intel.rs`, `revision_diff.rs`) instantiates `JcaBdeManager::new(client, "ProjectServer")` or passes a repository address like `"EXTce01108_dev"` as `conid`.
   - `JcaBdeManager::execute` puts `self.conid` directly into the query string `?method=bdecall&bdename=...&bdemethod=...&conid=ProjectServer`.
   - Live verification against `https://mingle-ionapi.ne1.inforcloudsuite.com/SLNBGS786BCXMXWQ_TST/LN/webservice` proved that the LN JCA servlet requires `conid` to be the **integer connection ID** returned by `?method=connect&company=0` (e.g. `<conid>0</conid>`) or `?method=share&company=0` (e.g. `<conid>1</conid>`). Passing `conid=ProjectServer` causes `HTTP 500 <error><info>null</info><message>POST request failed</message><reason>0</reason></error>`.
3. **Blocker 3 — Java Serialization (`0xACED0005`) Handle Assignment Order Bug in `ln-eclipse-compat/src/admin.rs`**:
   - Running `skill-ln validate` on the real Eclipse `.admin` file inside `C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST\dev_natt_v01108-1 [EXTce01108]\.admin` fails with:
     `Failed to parse .admin: Malformed Java serialization stream: Handle 0x007e0003 is not a ClassDescriptor`
   - Root cause: `admin.rs` assigns `newHandle` (`0x007E0000 + idx`) in the wrong order during both `serialize()` and `deserialize()`:
     - Per the JVM Object Serialization Stream Protocol (`java.io.ObjectInputStream`), `TC_OBJECT (0x73)` reads `classDesc` **first** (which assigns `newHandle` to the `ClassDesc`, and then assigns handles to any `TC_STRING` field type descriptors inside `classDescInfo`, before assigning `newHandle` to the `Object` instance itself).
     - `admin.rs` pushed `HandleValue::Object` *before* calling `read_class_desc()`, and pushed `HandleValue::ClassDesc` *after* reading field descriptor strings (`"Ljava/lang/String;"`), inverting handles `0x007E0000`/`0x007E0001` and shifting `ClassDesc(AdministrationComponent)` from `0x007E0003` to `0x007E0005`.
4. **Blocker 4 — Windows Main Thread Stack Overflow (`1 MB`) in Debug Builds**:
   - Running `target/debug/skill-ln.exe` on Windows crashes immediately on every command with `thread 'main' has overflowed its stack` (`exit code 1` / `0xC00000FD`).
   - Root cause: Windows default main thread stack is `1 MB`. The unoptimized 60-variant `Commands` enum plus the unboxed `async fn execute_command` state machine in `rust/bins/skill-ln/src/commands.rs` exceeds `1 MB` in debug builds. `cargo test` missed this because Rust's test harness spawns worker threads with larger stacks and `test_cli.rs` called `execute_command()` in-process rather than spawning `CARGO_BIN_EXE_skill-ln`.
5. **Blocker 5 — Real Server `.tbl` XML Parsing False Positives in `ln-model/src/validator.rs`**:
   - Running `skill-ln validate` on real server tables `txcmg011.tbl` and `txcmg012.tbl` in `dev_natt_v01108-1 [EXTce01108]` produces 20+ false-positive errors (`IndexColumn '1' does not match any defined Column in table 'txcmg011'`, `Session FormField 'txcmg012.btno' does not match any column in controller table 'txcmg012'`).
   - Root cause: `validator.rs` uses naive regexes (`<Column>([\s\S]*?)</Column>` + first `<name>`) instead of DOM traversal:
     1. In real LN Studio `<Column>` XML (`<Column>...<datatype>...<name>tfgld.btno</name></datatype><type>simple</type><name>btno</name></Column>`), `<datatype><name>` appears *before* the column's direct `<name>btno</name>` child.
     2. In real LN Studio `<Index>` XML (`<Index>...<IndexColumn><sortingOrder>asc</sortingOrder><column>btno</column><position>1</position></IndexColumn>...<name>1</name></Index>`), `validator.rs` searches `<Index>` for `<name>` (getting index number `"1"`) instead of reading `<IndexColumn><column>` (or `<IndexColumn><name>`).
6. **Blocker 6 — Real Workspace False Positives in `ln-linter` (`audit-4gl` on `txesssli2620m0.lib`)**:
   - Running `skill-ln audit-4gl` on `dev_natt_v01108-1 [EXTce01108]` produces 21 false-positive violations on real server-generated files (`txesssli2620m0.lib`):
     1. `audit_path` reads Single-XML `.lib` files as raw text without extracting `<expression>` CDATA/escaped text and unescaping XML entities (`&lt;`, `&gt;`, `&amp;`, `&quot;`, `&apos;`), causing `<?xml ...>` on line 1 to trigger `EXT003` and `#include &lt;bic_dam&gt;` to fail `INC001` detection. Furthermore, directory scanning in `audit_path` skips `.tbl`, `.ses`, `.rpt`, and `.fnc` Single-XML files that contain embedded 4GL `<expression>` blocks.
     2. `EXT003` in `auditor.rs` (lines 816–826) falsely requires all `ext.get.*` functions to have `void` return type, rejecting the 4 standard LN Extension Modeler framework functions `function extern long ext.get.form.fields()`, `ext.get.session.indices()`, `ext.get.command.extensions()`, and `ext.get.report.extensions()`.
     3. `DAL003` in `auditor.rs` (lines 1049–1068) matches `return` inside dotted function names like `function extern void function.ext.gen.return.man.sales.before.command()` because `.` is not treated as an identifier character before `return`.
7. **Blocker 7 — Skill Entrypoints (`SKILL.md` & `references/`) Still Point to Python Scripts**:
   - `ln_studio_skill/SKILL.md`, `erp-ln-progguide/SKILL.md`, and their `references/` files still instruct agents to run `python tools/ln_component_builder.py` and `python scripts/audit_4gl.py` instead of `skill-ln`.

---

## Solution

Harden and wire the entire `skill-ln` Rust workspace to achieve **true, verified 100% production readiness** across local binary codecs, XML validators, 4GL static analysis, live JCA HTTP/1.1 session management, the Single-Leader daemon, all 60 CLI subcommands, all 25 MCP Stdio tools, and both agent `SKILL.md` entrypoints:

1. **Fix Windows Stack Size & Process-Level Binary Execution (`rust/.cargo/config.toml` & `bins/skill-ln`)**:
   - Configure `rustflags = ["-C", "link-arg=/STACK:8388608"]` (`8 MB` stack) for `x86_64-pc-windows-msvc` and `Box::pin` large async subcommand futures so `target/debug/skill-ln.exe` and `target/release/skill-ln.exe` never overflow the main thread stack.
   - Enforce process-level execution tests (`std::process::Command::new(env!("CARGO_BIN_EXE_skill-ln"))`) in `test_cli.rs` and `scripts/run_checks.py`.
2. **Fix JVM `0xACED0005` Handle Table Order in `ln-eclipse-compat/src/admin.rs`**:
   - Align `serialize()` and `deserialize()` with `java.io.ObjectInputStream` / `ObjectOutputStream` handle assignment rules, supporting both `TC_REFERENCE` and `TC_STRING` on `m_path` (`field 7`) and verifying byte-for-byte / structural round-trip parity against the real Eclipse `.admin` file from `dev_natt_v01108-1 [EXTce01108]`.
3. **Fix DOM-Based `.tbl` Validation in `ln-model/src/validator.rs` & Real-World XML/4GL Auditing in `ln-linter/src/auditor.rs`**:
   - Replace regex-based `<Column>` and `<Index>` extraction in `validator.rs` with `roxmltree::Document` direct-child inspection (`<Column>` direct child `<name>`, and `<IndexColumn>` child `<column>` or `<name>`).
   - In `ln-linter/src/auditor.rs`:
     - Extract and XML-unescape `<expression>` payloads from Single-XML component files (`.lib`, `.tbl`, `.ses`, `.rpt`, `.fnc`) while preserving line numbers or logical block context, and include `.tbl`, `.ses`, `.rpt`, `.fnc` in directory walks (matching `erp-ln-progguide/scripts/audit_4gl.py`).
     - Whitelist `long` return type on `ext.get.form.fields`, `ext.get.session.indices`, `ext.get.command.extensions`, and `ext.get.report.extensions` in `EXT003`.
     - Treat `.` as a valid Baan 4GL identifier character before `return` in `DAL003` and skip `function` declaration headers so dotted identifiers like `function.ext.gen.return.*` never trigger false positives.
4. **Fix JCA `conid` Resolution & Workspace Endpoint Discovery in `ln-jca`, `ln-auth`, and `ln-scm`**:
   - Enhance `HttpClient` in `ln-jca` with thread-safe logical connection-point resolution (`"ProjectServer"` $\rightarrow$ primary integer `conid` from `connect()`, and activity/reference repository addresses like `"EXTce01108_dev"` / `"EXT_admin"` $\rightarrow$ multiplexed integer `conid` from `share()`, with automatic lazy `connect()` / `share()` when not yet established).
   - Add a unified **Workspace & Activity Context Resolver** in `ln-scm` (or `bins/skill-ln`) that automatically resolves:
     - Active Eclipse workspace directory (`--workspace`, `LN_WORKSPACE`, `~/.ln_studio/config.json`, or `./workspace_lnstudio/<env>`),
     - Cloud environment & JCA endpoint URL from `.metadata/.plugins/org.eclipse.core.runtime/.settings/com.infor.ln.studio.integration.connectivity.prefs` + `com.infor.ln.studio.Global.cloudenv.prefs`,
     - OAuth2 Bearer token via `ln_auth::prefetch_gate` (`~/.ln_studio/tokens/<env>.json`, auto-refreshing via `refresh_token` or `.ionapi` ROPC/client credentials if needed),
     - Active activity directory and `.project` metadata (`ProjectName`, `TaskName`, `Label`, `ApplicationRelease`, `DevelopmentTimeRepositoryAddress`, `RunTimeRepositoryAddress`).
5. **Wire All 60 CLI Subcommands (`commands.rs`) & All 25 MCP Stdio Tools (`mcp/tools.rs`)**:
   - Replace every stub in `commands.rs` with real calls into `ln-scm`, `ln-daemon`, `ln-model`, `ln-auth`, `ln-eclipse-compat`, `ln-linter`, `ln-kb`, and `ln-verify`.
   - Fix `message`, `question`, `function`, `additional`, `report` in `commands.rs` and `ln_create_component` in `mcp/tools.rs` to call `ln_model::generators::*` and `resolve_component_path` (`{pkg}/{type}/{mod}/{name}.{ext}` or `{pkg}/{type}/{name}.{ext}`).
   - Wire all 25 MCP tools in `mcp/tools.rs` to execute real crate operations when invoked normally while honoring an explicit `"mock": true` flag (or mock HTTP transport) for hermetic offline unit tests.
6. **Update Skill Entrypoints (`ln_studio_skill/SKILL.md` & `erp-ln-progguide/SKILL.md`) & Unified Checks**:
   - Update both `SKILL.md` files (staying strictly `<= 80` lines per ADR 0018) and `references/` to invoke `skill-ln`.
   - Expand `scripts/run_checks.py` to verify process-level `skill-ln` CLI execution and zero false positives on real workspace fixtures.

---

## User Stories

1. **As an AI coding agent on Windows**, I want both `target/debug/skill-ln.exe` and `target/release/skill-ln.exe` to execute any CLI subcommand in a child process without overflowing the `1 MB` default Windows main thread stack.
2. **As an LN developer**, I want `skill-ln validate` and `skill-ln sync-admin` to read, validate, and round-trip real Eclipse `.admin` files (`0xACED0005` Java serialization stream with `HashMap<String, AdministrationComponent>`) produced by LN Studio Build 0640 without throwing `Handle 0x007e0003 is not a ClassDescriptor`.
3. **As an LN developer**, I want `skill-ln validate --activity-dir <dir>` to accurately parse real server-downloaded `.tbl` files (`<Column>` with nested `<datatype><name>` and `<IndexColumn>` with `<column>`) so valid tables (`txcmg011.tbl`, `txcmg012.tbl`) and sessions (`txcmg0512m000.ses`) pass validation with 0 false positives.
4. **As an LN 4GL auditor**, I want `skill-ln audit-4gl <activity_dir>` to extract and XML-unescape `<expression>` blocks from Single-XML `.lib`, `.tbl`, `.ses`, `.rpt`, and `.fnc` files, recognize `#include <bic_dam>` inside XML-escaped expressions, permit `long` return types on standard `ext.get.{form.fields,session.indices,command.extensions,report.extensions}` hooks, and ignore `.return.` substrings inside dotted function names, achieving 0 false positives on `dev_natt_v01108-1 [EXTce01108]`.
5. **As an LN developer working against live CloudSuite (`SCS_TST`)**, I want `ln-jca` and `ln-scm` to resolve logical connection point names (`"ProjectServer"`, `"EXTce01108_dev"`, `"EXT_admin"`) to the numeric `<conid>` (`0`, `1`, ...) returned by `?method=connect` and `?method=share`, so all live BDE calls succeed with `HTTP 200` instead of failing with `HTTP 500 POST request failed`.
6. **As an LN developer**, I want all 12 component creation CLI commands (`table`, `session`, `domain`, `library`, `menu`, `component`, `message`, `question`, `function`, `additional`, `report`) and MCP `ln_create_component` to use `ln_model::generators::*` and write zero-attribute Single-XML TDE files to their canonical Build 0640 paths (`{pkg}/{type}/{mod}/{name}.{ext}` or `{pkg}/{type}/{name}.{ext}`), never into legacy plural folders (`messages/`, `questions/`, `functions/`, `additional/`, `reports/`).
7. **As an LN developer**, I want all 60 CLI subcommands in `skill-ln` to execute real workspace, authentication, daemon, SCM, explorer, build, `deploy-test`, and `FglStudio` code-intelligence logic against my configured CloudSuite environment rather than printing placeholder stub strings.
8. **As an AI agent using MCP (`skill-ln mcp-stdio`)**, I want all 25 MCP tools to execute real operations against the workspace and live/daemon JCA session (while still supporting hermetic test mode), returning accurate data inside the standard MCP Tool Envelope (`{"status": "success"|"error", "action": ..., "result": ..., "message": ...}`).
9. **As an AI agent loading `ln_studio_skill` or `erp-ln-progguide`**, I want `SKILL.md` (`<= 80` lines) and `references/` to document `skill-ln` commands and MCP tools so I invoke the fast native Rust binary automatically.

---

## Implementation Decisions

### 1. Windows Main Thread Stack Size & Boxed Async Dispatch (`Blocker 4`)

- **Cargo Linker Configuration (`rust/.cargo/config.toml`)**:
  - Add `[target.x86_64-pc-windows-msvc]` with `rustflags = ["-C", "link-arg=/STACK:8388608"]` (`8 MB` main thread stack, matching Linux/macOS defaults).
- **Runtime Thread Guard & Future Boxing (`rust/bins/skill-ln/src/main.rs` & `commands.rs`)**:
  - In `rust/bins/skill-ln/src/main.rs`, run the CLI parse + Tokio runtime inside a dedicated thread spawned via `std::thread::Builder::new().name("skill-ln-main".into()).stack_size(8 * 1024 * 1024)` so even if invoked in an environment that overrides linker flags, `skill-ln` is guaranteed an `8 MB` stack.
  - Box large async subcommand handlers (`Box::pin(...)`) inside `execute_command` so the outer state machine stays compact.

### 2. Exact JVM `0xACED0005` Object Serialization Protocol in `ln-eclipse-compat/src/admin.rs` (`Blocker 3`)

- **JVM Handle Table Rules (`baseWireHandle = 0x007E0000`)**:
  Per the official Java Object Serialization Specification (Section 6.4):
  1. When writing/reading `TC_OBJECT (0x73)`:
     - **Step A**: Read/write `classDesc` (`TC_CLASSDESC 0x72` or `TC_REFERENCE 0x71`).
     - **Step B**: If `classDesc` is a new `TC_CLASSDESC (0x72)`:
       1. Read/write `className` (UTF-16/modified-UTF-8 length-prefixed raw string — does **not** allocate a handle).
       2. Read/write `serialVersionUID` (`i64`) and `classDescFlags` (`u8`).
       3. **Allocate `newHandle` for the `ClassDesc` immediately** (before reading field descriptors!).
       4. Read/write `fields` count (`u16`). For each field: read/write `typecode` (`u8`) and `fieldName` (raw UTF). If `typecode` is `'L'` or `'['`, read/write `className1` as a string object (`TC_STRING 0x74` or `TC_REFERENCE 0x71`), where `TC_STRING` **allocates a `newHandle`**.
       5. Read/write `classAnnotation` (`TC_ENDBLOCKDATA 0x78`) and `superClassDesc` (`TC_NULL 0x70`).
     - **Step C**: **Allocate `newHandle` for the `Object` instance itself** immediately after `classDesc` completes and before `classdata[]` is read/written.
     - **Step D**: Read/write `classdata[]` (fields and/or custom `writeObject` block data). Every `TC_STRING (0x74)` inside `classdata[]` allocates a `newHandle`; every `TC_REFERENCE (0x71)` looks up an existing handle in `handles[handle - 0x007E0000]`.
- **Resulting Handle Sequence on Real `.admin` Files**:
  - `0x007E0000`: `ClassDesc("java.util.HashMap")`
  - `0x007E0001`: `Object(HashMap)`
  - `0x007E0002`: `String(entry_0_key)` (e.g. `"/dev_natt_v01108-1 [EXTce01108]/tx/bl/cmg/cmg011.tbl"`)
  - `0x007E0003`: `ClassDesc("com.infor.ln.studio.common.core.cm.administration.AdministrationComponent")`
  - `0x007E0004`: `String("Ljava/lang/String;")` (field descriptor of `m_path`)
  - `0x007E0005`: `Object(AdministrationComponent #0)`
  - Field 7 `m_path` of `AdministrationComponent #0`: if serialized via `TC_REFERENCE`, references `0x007E0002`; if serialized via `TC_STRING`, allocates `0x007E0006`.
  - Subsequent entries (`i >= 1`): `key` is `TC_STRING` (allocates handle $H_k$), `AdministrationComponent` uses `TC_REFERENCE(0x007E0003)` for its `ClassDesc`, allocates handle $H_{obj}$ for the `Object` instance, and its `m_path` either uses `TC_REFERENCE(H_k)` (when `m_path == key`, which is what Java `ObjectOutputStream` writes because Eclipse passes the same `String` reference to both `map.put(path, comp)` and `comp.setPath(path)`) or `TC_STRING` (when `m_path != key`).
- **Implementation Requirement**:
  - Both `AdminReader` and `AdminWriter` in `rust/crates/ln-eclipse-compat/src/admin.rs` MUST follow Steps A–D identically.
  - When `AdminWriter` writes an entry where `comp.path == key`, it MUST emit `TC_REFERENCE` pointing to that entry's key handle (matching Java `ObjectOutputStream` identity semantics); when `comp.path != key`, it emits `TC_STRING` and allocates a handle.
  - `AdminReader` MUST accept both `TC_REFERENCE` and `TC_STRING` (or `TC_NULL`) for `m_path` and any string object in the stream.

### 3. DOM-Based Table/Session XML Validation in `ln-model/src/validator.rs` (`Blocker 5`)

- Replace the regex-based table column and index extraction in `rust/crates/ln-model/src/validator.rs` (lines 300–345) with `roxmltree::Document::parse(&content)`:
  1. **Table Column Extraction (`<Column>`)**:
     - For every `<Column>` descendant element in a `.tbl` document, find its **direct child** `<name>` element (`col_node.children().find(|c| c.is_element() && c.has_tag_name("name"))`). Do **not** match `<name>` inside `<datatype><DatatypeReference><name>` or `<label><LabelReference><name>`.
  2. **Table Index Column Extraction (`<Index>` / `<IndexColumn>`)**:
     - For every `<Index>` descendant element, iterate its `<IndexColumn>` (or `<indexColumns>`) child elements.
     - Inside each `<IndexColumn>`, extract the referenced column name from `<column>` first (`idx_col.children().find(|c| c.is_element() && c.has_tag_name("column"))`), falling back to direct child `<name>` only if `<column>` is absent (to support both real server `<IndexColumn><column>btno</column></IndexColumn>` and synthetic templates).
  3. **Session FormField & Controller Table Validation (`.ses`)**:
     - When validating `.ses` `<FormField>` references against a table in `table_columns`, only validate `<FormField>` elements whose field name is qualified as `<table_name>.<col_name>` (where `<table_name>` exists in `table_columns` of the local activity) or unqualified columns when the controller table itself is present in `table_columns`. If a session references a standard base table not present in the local activity's `.tbl` files, check `.ln_dd_cache.json` if present, and do not emit a false error if the table is external.

### 4. Real-World Single-XML & Extension Modeler Auditing in `ln-linter/src/auditor.rs` (`Blocker 6`)

- **Single-XML `<expression>` Extraction & XML Entity Unescaping**:
  - In `rust/crates/ln-linter/src/auditor.rs`, add a helper `extract_4gl_from_xml_if_needed(filename: &str, raw_content: &str) -> String` (matching `erp-ln-progguide/scripts/audit_4gl.py`):
    - If `raw_content.trim_start().starts_with("<?xml")` or `filename` ends with `.lib`, `.tbl`, `.ses`, `.rpt`, or `.fnc` and contains `<expression>`:
      - Extract all `<expression>...</expression>` blocks (using `roxmltree::Document::parse` or regex + full XML entity unescaping of `&lt;` $\rightarrow$ `<`, `&gt;` $\rightarrow$ `>`, `&amp;` $\rightarrow$ `&`, `&quot;` $\rightarrow$ `"`, `&apos;` $\rightarrow$ `'`, `&#13;` / `&#10;` / `\r\n` $\rightarrow$ `\n`).
      - Join multiple `<expression>` blocks with `\n` (or preserve line offsets where possible).
      - If a Single-XML file (e.g. a pure data `.tbl` or `.ses` with no `<expression>` tag) contains no `<expression>`, `audit_file` returns an empty violation list immediately (`vec![]`).
  - Update `audit_path` directory traversal extensions to include `[".cln", ".dal", ".dalsrc", ".lib", ".ue", ".3gl", ".4gl", ".spt", ".tbl", ".ses", ".rpt", ".fnc"]`.
- **`EXT003` Standard Framework Function Return Types**:
  - In `auditor.rs` (around line 816), update the `ext.get.*` signature check so that:
    - The 4 standard generated Extension Modeler entrypoints (`ext.get.form.fields`, `ext.get.session.indices`, `ext.get.command.extensions`, `ext.get.report.extensions`) are allowed to return `long` (or `void` / `domain ttxmlnode`).
    - Only custom or helper functions outside `#context_on` ... `#context_off` with invalid non-standard signatures or executable code outside hooks trigger `EXT003`.
- **`DAL003` Dotted Identifier Boundary Fix**:
  - In `auditor.rs` (around lines 1049–1068):
    - Skip `DAL003` return-value checks on lines that are `function` declarations (`re_func.is_match(s_clean)`).
    - Before matching `return(...)` or `return <expr>`, verify the character immediately preceding `return` in `s_clean` is **not** an ASCII alphanumeric, `_`, or `.` (`!prev_char.is_ascii_alphanumeric() && prev_char != '_' && prev_char != '.'`). In Baan 4GL, `.` is part of identifiers (`function.ext.gen.return.man.sales.before.command`, `ret.return.val`), so `.return` is never a `return` keyword.

### 5. JCA `conid` Session Multiplexer & Workspace Discovery in `ln-jca` and `ln-scm` (`Blocker 2`)

- **`HttpClient` Logical Connection Point $\rightarrow$ Numeric `conid` Resolution (`rust/crates/ln-jca/src/http_client.rs`)**:
  - Add an internal connection registry to `HttpClient`:
    ```rust
    pub struct ConnectionRegistry {
        pub primary_conid: Option<String>,
        pub named_conids: HashMap<String, String>,
    }
    ```
    wrapped in `Arc<tokio::sync::Mutex<ConnectionRegistry>>` (or `std::sync::Mutex`).
  - When `client.connect(company)` succeeds and parses `<conid>N</conid>`, store `primary_conid = Some(N.clone())` and map `"ProjectServer"` $\rightarrow$ `N`.
  - When `client.share(company)` succeeds and parses `<conid>M</conid>`, return `M`. Add a helper `client.resolve_conid(logical_or_numeric: &str, company: u32) -> Result<String, JcaError>`:
    - If `logical_or_numeric` is already all digits (e.g. `"0"`, `"1"`), return it as-is.
    - If `logical_or_numeric` is `"ProjectServer"` or `""`:
      - If `primary_conid` is `Some(id)`, return `id`.
      - Otherwise, automatically call `self.connect(company).await?`, cache `primary_conid`, and return it.
    - For any other logical connection point name (e.g., `"EXTce01108_dev"`, `"EXTce01108_rt"`, `"EXT_admin"`):
      - If present in `named_conids`, return the cached numeric `conid`.
      - Ensure `primary_conid` is connected first (`connect(company)` if `None`), then call `self.share(company).await?` (falling back to `primary_conid` if the mock server doesn't implement `share` separately or returns the primary id), store `named_conids.insert(name, shared_id.clone())`, and return `shared_id`.
  - In `JcaBdeManager::execute` (`rust/crates/ln-jca/src/bde_manager.rs`), resolve `let resolved_conid = self.client.resolve_conid(&self.conid, self.client.default_company()).await?;` before calling `self.client.bde_call(&self.bde_name, method, &resolved_conid, &full_xml).await`.
  - This guarantees that every existing `JcaBdeManager::new(client, "ProjectServer")` and `JcaBdeManager::new(client, &act_info.dev_repo_address)` across `ln-scm` transparently sends the valid numeric `conid` (`0`, `1`, ...) over the wire on live CloudSuite while remaining 100% compatible with existing unit tests!
- **Workspace & Activity Context Resolver (`rust/crates/ln-scm/src/context.rs`)**:
  - Create a reusable module `ln_scm::context::WorkspaceContext` that resolves:
    1. **Workspace Path**: From explicit `--workspace` arg $\rightarrow$ `LN_WORKSPACE` env var $\rightarrow$ `~/.ln_studio/config.json` (`active_workspace`) $\rightarrow$ auto-detecting `C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST` (or current directory if it contains `.metadata`).
    2. **Cloud Environment & Endpoint (`connectivity.prefs` + `cloudenv.prefs`)**:
       - Parse `<workspace>/.metadata/.plugins/org.eclipse.core.runtime/.settings/com.infor.ln.studio.integration.connectivity.prefs` and `com.infor.ln.studio.Global.cloudenv.prefs` via `ln_auth::prefs_parser`.
       - Resolve `env_name` (e.g. `SCS_TST`), `endpoint_url` (e.g. `https://mingle-ionapi.ne1.inforcloudsuite.com/SLNBGS786BCXMXWQ_TST/LN/webservice`), and `company` (default `0`).
    3. **Authenticated `HttpClient` via `Pre-Fetch-Auth-Gate`**:
       - Look up `~/.ln_studio/tokens/<env_name>.json` (and fallback to `~/.ln_studio/tokens/<workspace_folder_name>.json`).
       - Run `ln_auth::prefetch_gate::ensure_valid_token` so expired/near-expiry tokens (`<= 300s`) are automatically refreshed before any JCA network call.
    4. **Active Activity Context (`.project`)**:
       - Parse `<activity_dir>/.project` (or discover the matching activity folder `<task> [<project>]` inside the workspace) to obtain `ProjectName`, `TaskName`, `Label` (`labelUUID`), `ApplicationRelease`, `DevelopmentEnvironment`, `DevelopmentTimeRepositoryAddress`, and `RunTimeRepositoryAddress`.

### 6. Full Wiring of All 60 CLI Subcommands (`commands.rs`) & All 25 MCP Tools (`mcp/tools.rs`) (`Blocker 1`)

- **Component Generator Fix (`commands.rs` & `mcp/tools.rs`)**:
  - In `commands.rs`:
    - `Commands::Message` $\rightarrow$ call `ln_model::generators::msg::generate_message_xml(&package, &code, &text)` and write to `resolve_component_path(&out_dir, "Message", &package, None, &code)` (`{pkg}/emess/{code}.msg`).
    - `Commands::Question` $\rightarrow$ call `ln_model::generators::qst::generate_question_xml(...)` and write to `resolve_component_path(&out_dir, "Question", &package, None, &code)` (`{pkg}/equest/{code}.qst`).
    - `Commands::Function` $\rightarrow$ call `ln_model::generators::fnc::generate_function_xml(...)` and write to `resolve_component_path(&out_dir, "Function", &package, Some(&module), &name)` (`{pkg}/efunc/{mod}/{name}.fnc`).
    - `Commands::Additional` $\rightarrow$ call `ln_model::generators::add::generate_additional_xml(...)` and write to `resolve_component_path(&out_dir, "AdditionalFile", &package, None, &name)` (`{pkg}/eaddfile/{name}.add`).
    - `Commands::Report` $\rightarrow$ call `ln_model::generators::rpt::generate_report_xml(...)` and write to `resolve_component_path(&out_dir, "Report", &package, Some(&module), &name)` (`{pkg}/erep/{mod}/{name}.rpt`).
  - In `mcp/tools.rs`:
    - `ln_create_component` $\rightarrow$ dispatch all 12 component types (`table`, `session`, `domain`, `library`, `menu`, `label`, `message`, `question`, `function`, `additional`, `report`, `bod`) through `ln_model::generators::*` and `resolve_component_path`.
- **CLI Server/SCM/Code-Intel Subcommand Wiring (`commands.rs`)**:
  - Wire every remaining stub subcommand in `rust/bins/skill-ln/src/commands.rs` to the real crate implementation using `WorkspaceContext` (supporting an optional `--endpoint` / `LN_JCA_MOCK_URL` override for offline mock-server tests, and graceful offline diagnostics if no workspace/endpoint is configured):
    - `Environments`: scan parent workspace folder and `~/.ln_studio/tokens/*.json` + `.metadata` connectivity prefs to list all configured environments and token statuses.
    - `Login`: support `--check-only`, `--ionapi <path>`, `--username`/`--password` (ROPC against `.ionapi` token URL), or interactive OOB loopback via `ln_auth`.
    - `Connect`: resolve `WorkspaceContext`, run `Pre-Fetch-Auth-Gate`, connect (`?method=connect`), ping (`?method=ping`), disconnect cleanly, and print connection ID & latency.
    - `Daemon`: implement `--status`, `--start`, `--stop`, `--ping` via `ln_daemon::DaemonManager`.
    - `Project` & `ProjectInfo`: call `ln_scm::project::list_projects` / `get_project_info`.
    - `Activity`, `NewActivity`, `OpenActivity`, `CleanActivity`, `MoveComponents`, `CleanComponents`: call `ln_scm::activity::{get_project_activities, create_remote_activity, open_remote_activity, clean_activity, move_components, clean_components}` (falling back to `bootstrap_local_activity` only when `--offline` or no remote endpoint is configured).
    - `Explorer`, `GetComponent`, `SyncReference`, `CloneComponent`: call `ln_scm::explorer::{browse_components, get_component, sync_reference_dd_cache}` and `ln_model::surgery::clone_component`.
    - `CheckoutComponent`, `UncheckoutComponent`, `CheckinComponent`, `CheckoutActivity`, `CheckinActivity`, `PrepareEndActivity`: call `ln_scm::scm_engine::ScmEngine` and `ln_scm::build::prepare_end_activity`.
    - `CompileSource`, `SearchServer`, `CallHierarchy`, `OpenDeclaration`, `RelatedComponents`, `Revisions`, `DiffComponent`, `GenerateReportServer`: call `ln_scm::code_intel::CodeIntelEngine` and `ln_scm::revision_diff::RevisionDiffEngine`.
    - `Build` & `DeployTest`: call `ln_scm::build::BuildEngine` using resolved `WorkspaceContext` (not hardcoded `localhost:8080` or `EXTce01107`).
- **MCP 25 Tools Wiring (`rust/bins/skill-ln/src/mcp/tools.rs`)**:
  - Update `execute_tool(name, args)` so that:
    - When `args` does NOT set `"mock": true` and a real `workspace` / `activity_dir` / `endpoint` is provided (or configured in `~/.ln_studio/config.json`), each tool executes the real async operation in `ln-auth`, `ln-scm`, `ln-model`, `ln-linter`, or `ln-daemon`.
    - When running in hermetic unit tests without a live JCA endpoint (e.g. `test_mcp_server.rs` passing synthetic IDs like `"EXTce01107"` with no `workspace` or with `"mock": true`), `execute_tool` either routes against the test's mock JCA server or returns deterministic test fixtures so offline tests remain 100% hermetic and fast.

### 7. Skill Entrypoints & Documentation Cutover (`Blocker 7`)

- Update `ln_studio_skill/SKILL.md` (`<= 80` lines) and `erp-ln-progguide/SKILL.md` (`<= 80` lines) to reference `skill-ln` (and `skill-ln mcp-stdio`) as the primary execution binary while noting `LN_FALLBACK_MODE=auto` compatibility.
- Update `ln_studio_skill/references/CLI_REFERENCE.md` and `ln_studio_skill/references/MCP_TOOLS_REFERENCE.md` to show `skill-ln <subcommand>` and `skill-ln mcp-stdio`.

---

## Testing Decisions

A good test in this repository proves behavior at a **real system boundary** rather than asserting that a stub function returns a hardcoded string:

1. **Seam 1 — Process-Level Binary Execution Gate (`test_cli_process.rs` & `scripts/run_checks.py`)**:
   - Every CLI test suite MUST include process-level execution via `std::process::Command::new(env!("CARGO_BIN_EXE_skill-ln"))` in both debug and release modes to guarantee the Windows main thread stack (`8 MB`) never overflows and stdout/stderr/exit codes match the CLI contract.
2. **Seam 2 — Real Eclipse Binary & Real Server XML Corpus Gate**:
   - `ln-eclipse-compat` tests MUST parse and round-trip real JVM-generated `.admin` byte streams (where `ClassDesc` handles precede `Object` handles and `m_path` uses `TC_REFERENCE` or `TC_STRING`), plus verify against the real `.admin` file in `dev_natt_v01108-1 [EXTce01108]`.
   - `ln-model` validator tests MUST include real server `.tbl` structures (`<Column>` with `<datatype><DatatypeReference><name>...</name></DatatypeReference></datatype>` before `<name>col</name>`, and `<Index><IndexColumn><column>col</column></IndexColumn><name>1</name></Index>`) and verify 0 false-positive errors on `txcmg011.tbl`, `txcmg012.tbl`, and `txcmg0512m000.ses`.
   - `ln-linter` auditor tests MUST include real Single-XML `.lib` files (`<?xml ...><Library>...<script>...<expression>...#include &lt;bic_dam&gt;...function extern long ext.get.form.fields()...function extern void function.ext.gen.return.man.sales.before.command()...</expression>`) and verify 0 false-positive errors on `txesssli2620m0.lib`.
3. **Seam 3 — Stateful Mock JCA Server (`conid` Multiplexing) + Live `SCS_TST` (`dev_natt_v01108-1`) Verification Gate**:
   - Update the hermetic mock JCA HTTP server in `ln-scm` and `bins/skill-ln` integration tests so `?method=bdecall` **rejects** non-numeric `conid` values (returning `HTTP 500 POST request failed` if `conid=ProjectServer` is sent, just like the real Infor CloudSuite JCA servlet!). This makes it impossible for any future change to regress `conid` resolution.
   - Run end-to-end live smoke verification against `SCS_TST` (`EXTce01108`, Activity `dev_natt_v01108-1`) using `skill-ln.exe` (`connect`, `project-info`, `activity`, `explorer`, `validate`, `diagnose`, `audit-4gl`, `verify-studio-build`, and `mcp-stdio` tool calls).

---

## Out of Scope

- Unlocking `EndActivity`, `CloseTask`, `FinalizeActivity`, `<End/>`, or `<Deliver/>` (physically hard-blocked per ADR 0007).
- Allowing SCM check-out/check-in of Extension Modeler components (`ess`, `est`, `esb`, `esm`, `esr` remain `[GET_ONLY_EXTENSION]` per ADR 0006).
- Deleting the legacy Python scripts (`ln_studio_skill/tools/` and `erp-ln-progguide/scripts/`), which are intentionally preserved for `LN_FALLBACK_MODE=auto` differential fallback and test suites.

---

## Further Notes (Strict Rules for Gemini 3.8 Flash Execution)

1. **Zero Stub Rule**: Do NOT replace a `println!` stub with another stub or mock return when a real function in `ln-scm`, `ln-model`, `ln-daemon`, `ln-auth`, or `ln-eclipse-compat` exists. Every CLI command and MCP tool must wire through to the real crate implementation.
2. **Cargo Target Directory**: `rust/.cargo/config.toml` sets `target-dir = "C:/Temp/skill_ln_target"`. Built binaries reside at `C:\Temp\skill_ln_target\debug\skill-ln.exe` and `C:\Temp\skill_ln_target\release\skill-ln.exe`.
3. **PowerShell Path Escaping for `[EXTce01108]`**: In PowerShell (`pwsh`), folder names containing `[` and `]` like `dev_natt_v01108-1 [EXTce01108]` are treated as wildcard character classes unless you pass `-LiteralPath` (or quote them passed directly to `skill-ln.exe`).
4. **Test Runner Rule**: Always run `python scripts/run_checks.py` and `cargo test --workspace --manifest-path rust/Cargo.toml` (never invoke `pytest`).
5. **Credential Security Rule**: Never hardcode or commit `.ionapi` secrets, OAuth2 Bearer tokens, or user passwords into any file under `rust/`, `docs/`, `.scratch/`, or `scripts/`. Always load tokens from `~/.ln_studio/tokens/SCS_TST.json` or environment variables during live verification.
