# ADR 0008: Semantic/AST 4GL Auditor, 3-Tier OAuth2 Lifecycle, Auto-DD Cache (`sync-reference`), and BYOJ Production Hardening

- **Status**: Accepted
- **Date**: 2026-10-28
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`
- **Prior ADRs**:
  - [`docs/adr/0006-ln-studio-extension-readonly-and-lnui-workflow.md`](0006-ln-studio-extension-readonly-and-lnui-workflow.md) *(Strictly enforced: Extension Modeler `tx*`/`.eso`/`.eto`/`.ere` components remain Get-Only in Studio)*
  - [`docs/adr/0007-headless-jca-connectivity-scm-and-mcp-server.md`](0007-headless-jca-connectivity-scm-and-mcp-server.md) *(Refined regarding 3-tier OAuth2 persistence, BYOJ JAR resolution, split `deploy-test` modes, and Java-level `EndActivity` blocking)*

---

## 1. Context & Problem Statement

Real-world CloudSuite LN Studio (`10.8.0_build0640`) development with AI agents exposed four critical production bottlenecks:
1. **False-Positive Passes in `audit_4gl.py`**: Surface-level regex and line-by-line block checks allowed 4GL/DAL code to pass offline verification while failing immediately on `bic6.2` compilation in LN Studio due to missing `table t<name>` declarations (`TBL001`), hallucinated table columns or domain names (`TBL002`, `DMN001`), preprocessor `#define` macros breaking block counters (`SYN001`), or helper functions hiding nested `commit.transaction()` calls (`CAV003`).
2. **Repetitive Manual OAuth2 Token Configuration & Missing Server Reference Cache**: Developers needed seamless 3-tier OAuth2 token persistence (`~/.ln_studio/tokens/<workspace>.json`) with a 5-minute expiry safety buffer, silent refresh, and interactive browser/loopback or manual paste fallback (`oob://localhost/lnstudio`), plus a clean `.reference/<type>/` workspace cache (`sync-reference`) that automatically indexes real Ecore `.tbl` (`<Column>/<datatype>/<name>`) and `.dmn` (`<Enumeration>`) XML schemas into `.ln_dd_cache.json` without polluting Activity `.admin` files.
3. **Proprietary JAR Distribution & CRDD Lock Risks**: Bundling Infor JARs (`lnstudio_commoncore.jar`, `JCAAdapter4ERPln*.jar`) in Git violates Bring-Your-Own-JARs (BYOJ) licensing compliance. Additionally, running `ConvertToRuntime` (`CRDD`) and `CreateTables` by default on every `deploy-test` invocation risks bshell/table lock hangs when active LN UI sessions hold locks on target tables.
4. **Protocol-Level `EndActivity` Assurance & Report Generation Realism**: While Python CLI/MCP blocked `EndActivity`, `LNStudioJcaBridge.java` previously accepted arbitrary XML payloads without inspecting BDE method names. Furthermore, from-scratch declarative YAML layout generation for complex `.rpt` reports proved inferior to cloning an existing server report (`clone-component --type report`) and patching specific fields/labels.

---

## 2. Settled Architectural Decisions

### Decision 1: Semantic, Schema & Recursive-Descent AST Validation in `audit_4gl.py`
1. **`TBL001` (Table Declaration Enforcement)**:
   - Parse `declaration:` (and top-level declarations) for `table\s+t([a-z]{5}\d{3})`.
   - Scan tokenized 4GL statements and embedded SQL (`select ... from ... where ...`) for `([a-z]{5}\d{3})\.([a-z0-9_]+)` references.
   - Exempt the component's main table passed via `--main-table <table>` or inferred automatically from the script filename (`txsli001.dal`) or XML wrapper (`<DR_Table><name>`, `<mainTable>`). Flag `ERROR` (`TBL001`) for any undeclared referenced table.
2. **`TBL002` & `DMN001` (Data Dictionary Schema Cache Verification)**:
   - Load `.ln_dd_cache.json` from the workspace/repository root (or `--dd-cache <path>`), supplemented by local `.tbl`/`.dmn` XML files found in the workspace.
   - Validate `<table>.<field>` (`TBL002`, ignoring bshell pseudo-fields `_index1`..`_index9`, `_compnr`, `record_len`) and `domain <domain_name>` (`DMN001`) against `.ln_dd_cache.json`.
   - Support `--auto-fetch-dd`: when a referenced table or domain is absent from `.ln_dd_cache.json`, automatically invoke the read-only server getter (`ComponentExplorer.sync_reference` / `get_component`) to pull the `.tbl` or `.dmn` XML, update `.ln_dd_cache.json`, and complete validation.
3. **Pure-Python Recursive Descent AST & Call Graph (`SYN001` & `CAV003`)**:
   - Replace line-by-line regex matching with a zero-dependency tokenizer and AST parser that strips comments (`|`), string literals, `dllusage`/`functionusage` documentation blocks, and preprocessor `#define` directives before parsing nested control/SQL blocks (`select`/`selectdo`/`selectempty`/`selecteos`/`endselect`, `if`/`endif`, `for`/`endfor`, `while`/`endwhile`, `repeat`/`until`, `on case`/`endcase`).
   - Build an intra-file function **Call Graph** to detect transitive nested transactions (`CAV003`): calling any helper function that directly or transitively invokes `db.retry.point()`, `commit.transaction()`, or `abort.transaction()` inside an active transaction block.

### Decision 2: 3-Tier Automated OAuth2 Lifecycle & `sync-reference` Auto-DD Indexer
1. **3-Tier Token Lifecycle (`ln_env_manager.py`)**:
   - **Tier 1 (Cached Active Token)**: Read from `~/.ln_studio/tokens/<workspace>.json` (or custom `cache_dir` override). If `access_token` is valid with at least a **300-second (5-minute) safety buffer** before `expires_at`, return immediately.
   - **Tier 2 (Silent Refresh)**: When expired or within buffer, HTTP POST to the `.ionapi` token endpoint (`ot`) using cached `refresh_token` (`grant_type=refresh_token`) or Service Account credentials (`saak`/`sask` via `grant_type=password`), and atomically update the token cache.
   - **Tier 3 (Interactive Browser & Manual Paste Fallback)**: Launch `webbrowser.open` to the `.ionapi` authorization URL (`oa`). Spin up a local loopback HTTP listener when `redirect_uri` is `http://localhost:<port>`; when `redirect_uri` is `oob://localhost/lnstudio` (standard Desktop `.ionapi` per `OAuth2CallbackImpl.class`) or `--manual-auth` is passed, prompt the developer to paste the redirected `oob://localhost/lnstudio?code=...` URL or raw `code`, exchange it for tokens, and persist them.
2. **Workspace Reference Sync (`sync-reference`) & Real Ecore DD Indexer**:
   - Provide CLI subcommand `sync-reference --type <table|domain|session|extension> --name <pattern>` and MCP tool `ln_sync_reference`.
   - Store fetched XML files strictly in `<workspace_root>/.reference/<type>/` with OS Read-Only permissions and **zero modifications to any Activity `.admin` file**.
   - Enforce the **Extension Modeler Rule (ADR 0006)**: extensions (`tx*`, `.eso`, `.eto`, `.ere`, `ess`, `est`, `esb`, `esm`, `esr`) can ONLY be fetched read-only via `Get` / `sync-reference` for context and offline snippet validation; all authoring/deployment occurs via manual Copy-Paste in LN UI Cloud (`ttext1500m000`).
   - Parse both real LN Studio Ecore XML (`<DR_Table>/<Column>/<datatype>/<name>`, `<Index>/<IndexColumn>`, `<DR_Domain>/<Enumeration>`) and legacy `<Field>` XML into `.ln_dd_cache.json` automatically on every `get` or `sync-reference`.

### Decision 3: BYOJ Compliance, Split `deploy-test` Modes & Protocol-Level `EndActivity` Removal
1. **BYOJ (Bring Your Own JARs) Compliance**:
   - Untrack `ln_studio_skill/tools/lib/lnstudio_commoncore.jar` from Git and ignore `ln_studio_skill/tools/lib/*.jar` in `.gitignore`.
   - Implement `resolve_ln_studio_jars()` in `ln_server_client.py` and `admin_sync.py` to auto-discover `JCAAdapter4ERPln*.jar` (and its `com.infor.erpln.jca.connectivity_*/lib/*.jar` dependencies) and `com.infor.ln.studio.common.core_*.jar` from `LN_STUDIO_HOME`, `LN_STUDIO_PATH`, environment variables, or standard Eclipse LN Studio directories.
2. **Split `deploy-test` Operational Modes**:
   - `--mode compile-only` (**default safe mode**): Executes `Put -> Compile -> VSC -> CheckIn` without invoking `ConvertToRuntime` or `CreateTables`.
   - `--mode schema-crdd`: Executes full `Put -> Compile -> CRDD -> CreateTables -> VSC -> CheckIn`, enforcing a `--dry-run` pre-check and explicit active-session table lock warning (`--confirm-no-locks`).
3. **Protocol-Level Removal of `EndActivity` in `LNStudioJcaBridge.java`**:
   - Hard-reject any BDE method or XML request containing `EndActivity`, `CloseTask`, `FinalizeActivity`, or `<Deliver` inside `LNStudioJcaBridge.java` before `doBdeCall` can execute.
4. **Documentation & Report Realism**:
   - Document realistic memory footprint (`~150MB RAM (Python CLI + Headless JVM Daemon)`) in `README.md`.
   - Deprecate from-scratch YAML layout generation for complex `.rpt` reports in favor of `clone-component --type report`.
