# Task Tickets: 100% Native Rust Single-Binary Architecture (`skill-ln` — ADR 0021)

- **Active Specification**: [`docs/plans/SPEC_NATIVE_RUST_SKILL_LN.md`](SPEC_NATIVE_RUST_SKILL_LN.md) ([`.scratch/native-rust-skill-ln/spec.md`](../../.scratch/native-rust-skill-ln/spec.md))
- **Active Implementation Plan**: [`docs/plans/native-rust-skill-ln-plan.md`](native-rust-skill-ln-plan.md)
- **Architecture Decision Record**: [`docs/adr/0021-native-rust-skill-ln-single-binary-architecture.md`](../adr/0021-native-rust-skill-ln-single-binary-architecture.md)
- **Wayfinder Map**: [`.scratch/native-rust-skill-ln/map.md`](../../.scratch/native-rust-skill-ln/map.md)
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`

---

## Active Batch Dependency Graph (`Batch: Native Rust Single-Binary Toolchain skill-ln — ADR 0021`)

```mermaid
flowchart TD
    T01["01: Cargo Workspace & ln-eclipse-compat\n(.admin 0xACED0005, properties.index, .markers)"]
    T02["02: ln-auth 3-Tier OAuth2 Lifecycle\n(.ionapi, prefs, Loopback OOB, Pre-Fetch-Auth-Gate)"]
    T03["03: ln-jca Clean-Room HTTP/1.1 Wire Client\n(5-Mode BdeManager, 250-Pagination, Hard-Block)"]
    T04["04: [CHECKPOINT 1] ln-daemon Single-Leader\n(Sequential FIFO Queue, Token Hot-Swap & Phase 1 Gate)"]

    T05["05: ln-kb Zero-Copy Knowledge Base\n(rkyv 2,266 Functions, Syntax Dict, fn/doc-search)"]
    T06["06: ln-linter Part 1: Lexer, AST & 15 Core Rules\n(SYN, INC, ARR002, SQL008, STR001, CLD, DAL001-005)"]
    T07["07: [CHECKPOINT 2] ln-linter Part 2: Call Graph, DD & EXT\n(CAV003, TBL001-003, DMN001-003, EXT001-003 & Phase 2 Gate)"]

    T08["08: TDE Bytecode Schema Extractor\n(tde_schema_0640.json 129 Classes + 39 owtemplates)"]
    T09["09: ln-model Part 1: 12-Component XML Generators\n(Single-XML TDE Layout & Multi-Component YAML)"]
    T10["10: [CHECKPOINT 3] ln-model Part 2: Lossless DOM Surgery\n(Unknown Node Inspector, 4-Layer Validate & Phase 3 Gate)"]

    T11["11: ln-scm Part 1: Project/Activity & Explorer\n(project-info, new/open-activity, GetBrowseList, sync-reference)"]
    T12["12: ln-scm Part 2: Pre-Commit SCM & Build Pipeline\n(CheckOut/Put/CheckIn, deploy-test, EXT Guide-and-Paste)"]
    T13["13: [CHECKPOINT 4] ln-scm Part 3: FglStudio Code Intel\n(compile-source, search, call-hierarchy, diff & Phase 4 Gate)"]

    T14["14: ln-verify Crash Fixtures, Auto-Fallback & Build Differ\n(LN_FALLBACK_MODE & verify-studio-build 0xCAFEBABE)"]
    T15["15: [CHECKPOINT 5] Unified skill-ln Binary\n(60 CLI Cmds + 25 MCP Stdio Tools + CI & Final Gate)"]

    T01 --> T02
    T01 --> T03
    T02 --> T03
    T01 --> T04
    T02 --> T04
    T03 --> T04

    T01 --> T05
    T05 --> T06
    T06 --> T07

    T01 --> T08
    T08 --> T09
    T07 --> T10
    T09 --> T10

    T04 --> T11
    T10 --> T11
    T11 --> T12
    T12 --> T13

    T08 --> T14
    T13 --> T14
    T14 --> T15
```

---

## Active Ticket Roster (15 Tracer-Bullet Vertical Slices)

- **Local Issues Directory**: [`.scratch/native-rust-skill-ln/issues/`](../../.scratch/native-rust-skill-ln/issues/)

| ID | Phase | Title | Blocked by | What It Delivers | Status | Ticket File |
|---|---|---|---|---|---|---|
| **01** | Phase 1 | Cargo Workspace Scaffold & `ln-eclipse-compat` Binary Codecs | *None (can start immediately)* | Initializes `rust/` Cargo Workspace and pure-Rust `.admin` (`0xACED0005` `AdministrationComponent` `serialVersionUID=2L`), `properties.index` (`PropertyBucket` v1), `.markers` (`MarkerReader_3` v3), and `.metadata/.lock` detector with 1:1 Java/Python differential parity tests | `resolved` | [`01-cargo-workspace-and-eclipse-binary-codecs.md`](../../.scratch/native-rust-skill-ln/issues/01-cargo-workspace-and-eclipse-binary-codecs.md) |
| **02** | Phase 1 | `ln-auth` 3-Tier OAuth2 Lifecycle, `.ionapi` & `Pre-Fetch-Auth-Gate` | **01** | Implements `.ionapi` & Eclipse `.prefs` parsers, 3-Tier OAuth2 token lifecycle (`~/.ln_studio/tokens/<workspace>.json`), local loopback OOB listener (`oob://localhost/lnstudio`), and `Pre-Fetch-Auth-Gate` | `resolved` | [`02-oauth2-lifecycle-and-ionapi-auth.md`](../../.scratch/native-rust-skill-ln/issues/02-oauth2-lifecycle-and-ionapi-auth.md) |
| **03** | Phase 1 | `ln-jca` Clean-Room JCA HTTP/1.1 Wire Client & 5-Mode `JcaBdeManager` | **01, 02** | Implements `HttpClient` (`connect`, `share`, `bdecall`, `ping`, `disconnect`), all 5 `BdeManager` modes (`LIST`, `SHOW`, `BDE`, `SPECIALLIST`, `BROWSELIST`), 250-item `<iteratorID>` pagination, `ControllingAttributes`, `rustls-tls-native-certs`, and `EndActivity`/`CloseTask` hard-block | `resolved` | [`03-jca-http-wire-protocol-and-5-mode-bdemanager.md`](../../.scratch/native-rust-skill-ln/issues/03-jca-http-wire-protocol-and-5-mode-bdemanager.md) |
| **04** | Phase 1 | **[CHECKPOINT 1]** `ln-daemon` Single-Leader Native Daemon & Phase 1 Gate | **01, 02, 03** | Implements per-workspace Single-Leader daemon (`daemon_<workspace_hash>.lock`), Sequential FIFO Command Queue (`Pool Size = 1` `bshell`), token hot-swap, keepalive timer, and clears Phase 1 Gate | `resolved` | [`04-checkpoint-1-single-leader-daemon-and-phase-1-gate.md`](../../.scratch/native-rust-skill-ln/issues/04-checkpoint-1-single-leader-daemon-and-phase-1-gate.md) |
| **05** | Phase 2 | `ln-kb` Zero-Copy Embedded Knowledge Base (`rkyv`) & Search | **01** | Embeds `functions_db.json` (2,266 bshell functions), `studio_syntax_completion.json`, and doc index at compile time (`0 ms` startup parse) and delivers `< 1 ms` `fn-search` and `doc-search` | `resolved` | [`05-zero-copy-knowledge-base-and-search.md`](../../.scratch/native-rust-skill-ln/issues/05-zero-copy-knowledge-base-and-search.md) |
| **06** | Phase 2 | `ln-linter` Part 1: Baan 4GL Lexer, AST & 15 Core Syntax/Cloud/DAL Rules | **05** | Implements 4GL lexer, AST block parser, and 15 rules (`SYN001`–`002`, `INC001`, `ARR002`, `SQL008`, `STR001`, `CAV001`, `DBG001`, `CLD001`–`002`, `DAL001`–`005`) with differential parity tests against `audit_4gl.py` | `resolved` | [`06-4gl-lexer-ast-parser-and-core-syntax-dal-rules.md`](../../.scratch/native-rust-skill-ln/issues/06-4gl-lexer-ast-parser-and-core-syntax-dal-rules.md) |
| **07** | Phase 2 | **[CHECKPOINT 2]** `ln-linter` Part 2: Call Graph, DD Cache, `EXT001`–`003` & Phase 2 Gate | **06** | Completes all 25 lint rules (`CAV003`, `TBL001`–`003`, `DMN001`–`003`, `EXT001`–`003`), `.ln_dd_cache.json` integration, `rayon` parallel auditing, and clears Phase 2 100% Parity Gate against `audit_4gl.py` | `resolved` | [`07-checkpoint-2-call-graph-dd-cache-ext-rules-and-phase-2-gate.md`](../../.scratch/native-rust-skill-ln/issues/07-checkpoint-2-call-graph-dd-cache-ext-rules-and-phase-2-gate.md) |
| **08** | Phase 3 | Bytecode-to-JSON TDE Schema Extractor (`tde_schema_0640.json`) | **01** | Extracts all 129 `model.tde.*` classes, `.model.additional.*`, 39 `owtemplates/*.xml`, and 9 `ScriptTemplates/` from Build 0640 JARs into `rust/schemas/tde_schema_0640.json` and `build_0640_manifest.json` | `resolved` | [`08-tde-bytecode-schema-extractor-and-owtemplates-bundle.md`](../../.scratch/native-rust-skill-ln/issues/08-tde-bytecode-schema-extractor-and-owtemplates-bundle.md) |
| **09** | Phase 3 | `ln-model` Part 1: 12-Component XML Generators & Declarative YAML | **08** | Implements XML generators for all 12 component types (`.tbl`, `.ses`, `.dmn`, `.lib`, `.mnu`, `.lbl`, `.rpt`, `.msg`, `.qst`, `.fnc`, `.add`, `.bus`/`.cha`), multi-component YAML compiler, and Single-XML TDE path resolver | `resolved` | [`09-12-component-xml-generators-and-declarative-yaml.md`](../../.scratch/native-rust-skill-ln/issues/09-12-component-xml-generators-and-declarative-yaml.md) |
| **10** | Phase 3 | **[CHECKPOINT 3]** `ln-model` Part 2: Lossless DOM Surgery, Unknown Node Inspector & Phase 3 Gate | **07, 09** | Implements Lossless DOM Surgery (`inject`, `extract`, `clone-component`, `Pre-Put Script Merge`), Unknown Node Inspector (`unmapped_packets.log`), 4-Layer `validate --fix`, and clears Phase 3 Gate | `resolved` | [`10-checkpoint-3-lossless-dom-surgery-unknown-node-inspector-and-phase-3-gate.md`](../../.scratch/native-rust-skill-ln/issues/10-checkpoint-3-lossless-dom-surgery-unknown-node-inspector-and-phase-3-gate.md) |
| **11** | Phase 4 | `ln-scm` Part 1: Software Project/Activity Lifecycle & Component Explorer | **04, 10** | Implements `project-info`, `new-activity`, `open-activity` (with `CMLabel.GetModifiedComponents` + `CmGet`), `clean-activity`, `move/clean-components`, `GetBrowseList`, `sync-reference` (`.ln_dd_cache.json`), and `DR_Create` | `resolved` | [`11-software-project-activity-lifecycle-and-component-explorer.md`](../../.scratch/native-rust-skill-ln/issues/11-software-project-activity-lifecycle-and-component-explorer.md) |
| **12** | Phase 4 | `ln-scm` Part 2: Pre-Commit SCM Engine, Split `deploy-test` & Extension Modeler | **11** | Implements `CheckOut`, `UnCheckOut`, `Put`, `CheckIn`, `[GET_ONLY_EXTENSION]` guard, Extension `Guide-and-Paste` workflow, `Compile`, `CRDD`, `CreateTables`, `VSC.executeVSC`, split `deploy-test`, and `prepare-end-activity` | `resolved` | [`12-precommit-scm-engine-and-build-pipeline.md`](../../.scratch/native-rust-skill-ln/issues/12-precommit-scm-engine-and-build-pipeline.md) |
| **13** | Phase 4 | **[CHECKPOINT 4]** `ln-scm` Part 3: `FglStudio` Code Intelligence, Revision Diff & Phase 4 Gate | **12** | Implements `compile-source`, `search-server`, `call-hierarchy`, `open-declaration`, `related-components`, `revisions`, `diff-component`, `generate-report-server`, and clears Phase 4 Gate | `resolved` | [`13-checkpoint-4-fglstudio-code-intelligence-revision-diff-and-phase-4-gate.md`](../../.scratch/native-rust-skill-ln/issues/13-checkpoint-4-fglstudio-code-intelligence-revision-diff-and-phase-4-gate.md) |
| **14** | Phase 5 | `ln-verify` Crash Fixtures, Auto-Fallback (`LN_FALLBACK_MODE`) & `verify-studio-build` | **08, 13** | Implements token-redacted Crash Fixture recorder (`unmapped_packets/`), `LN_FALLBACK_MODE=auto\|strict\|off` fallback bridge, and pure-Rust `0xCAFEBABE` classfile & `owtemplates` build differ | `resolved` | [`14-auto-fallback-crash-fixtures-and-verify-studio-build.md`](../../.scratch/native-rust-skill-ln/issues/14-auto-fallback-crash-fixtures-and-verify-studio-build.md) |
| **15** | Phase 5 | **[CHECKPOINT 5]** Unified `skill-ln` Binary (60 CLI Cmds + 25 MCP Tools) & Final Gate | **14** | Wires all 60 CLI subcommands and 25 Stdio MCP tools into `bins/skill-ln`, integrates `cargo test` into `scripts/run_checks.py`, and clears Final Checkpoint 5 Gate (including live `SCS_TEST` verification) | `resolved` | [`15-checkpoint-5-unified-cli-mcp-server-and-final-cutover-gate.md`](../../.scratch/native-rust-skill-ln/issues/15-checkpoint-5-unified-cli-mcp-server-and-final-cutover-gate.md) |
