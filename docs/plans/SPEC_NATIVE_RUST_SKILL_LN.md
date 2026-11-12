# Functional & Technical Specification: 100% Native Rust Single-Binary Architecture (`skill-ln`)

- **Document ID**: `SPEC-2026-0021`
- **Status / Triage Label**: `ready-for-agent`
- **Related Master Plan**: [`docs/plans/native-rust-skill-ln-plan.md`](native-rust-skill-ln-plan.md)
- **Related ADR**: [`docs/adr/0021-native-rust-skill-ln-single-binary-architecture.md`](../adr/0021-native-rust-skill-ln-single-binary-architecture.md)
- **Prior ADRs Respected**: ADR 0006, ADR 0007, ADR 0008, ADR 0012, ADR 0014, ADR 0017, ADR 0018, ADR 0019, ADR 0020
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`

---

## Problem Statement

Engineers and AI coding agents developing, auditing, and deploying Infor ERP LN 10.8 (`build 0640`) components through `erp-ln-progguide` and `ln_studio_skill` currently rely on a hybrid Python 3 + JDK 11+ + proprietary Eclipse JAR (`BYOJ`) runtime stack. While ADR 0012 achieved functional parity with the Eclipse LN Studio workbench, four operational problems remain:

1. **Heavyweight Runtime Dependencies (`JDK 11+` & `BYOJ` Eclipse JARs)**:
   - Every workspace requires a local JDK installation (`java.exe`, `javac.exe`) and access to proprietary Infor Eclipse plugin JARs (`JCAAdapter4ERPln-10.8.10.jar`, `lnstudio_commoncore.jar`) to serialize `.admin` files and execute JCA calls.
   - Running headless automation on clean CI agents, lightweight containers, or developer laptops without Eclipse LN Studio installed is impossible under the current `BYOJ` constraint.
2. **Startup Latency & Memory Overhead**:
   - Python CLI invocations incur `150–400 ms` interpreter + JSON dictionary load times (`functions_db.json` with 2,266 bshell functions), while the Java JCA daemon consumes `80–150 MB` of JVM heap.
   - Single-threaded Python static analysis (`audit_4gl.py` across 25 rules) scales linearly when scanning large multi-component activities.
3. **Multi-Entrypoint Fragmentation across Dual Skills**:
   - AI agents must invoke separate Python scripts across two directories (`erp-ln-progguide/scripts/search.py`, `erp-ln-progguide/scripts/audit_4gl.py`, `ln_studio_skill/tools/ln_component_builder.py`, `ln_studio_skill/tools/ln_studio_mcp.py`), managing Python virtual environments and `sys.path` wiring.
4. **Silent Omission & Version-Upgrade Fragility in Reverse-Engineered Protocols**:
   - Re-implementing complex enterprise XML models (12 component types across 129 TDE classes) and BDE server protocols risks silent data loss if an unmapped XML tag is stripped during serialization, or runtime crashes when Infor LN servers return undocumented error payloads or upgrade beyond Build 0640.

---

## Solution

Replace the Python + Java + Eclipse JAR runtime stack with a **100% Native Rust Single-Binary Toolchain (`skill-ln.exe` / `skill-ln`)** built from a modular Cargo Workspace (`rust/`) and backed by a **4-Layer Anti-Omission & Upgrade Verification System**:

1. **Zero-JAR, Zero-JDK Standalone Runtime (`ln-jca`, `ln-auth`, `ln-eclipse-compat`)**:
   - Implement the exact Infor LN `http_oauth2` wire protocol (`com.infor.erpln.protocol.HttpClient` + `JcaBdeManager` across all 5 execution modes) directly in Rust over `reqwest` (`rustls-tls-native-certs`).
   - Implement pure-Rust binary codecs for Eclipse's `<activity>/.admin` (`0xACED0005` Java `ObjectOutputStream` of `HashMap<String, AdministrationComponent>` with `serialVersionUID = 2L`), `<workspace>/.metadata/.../properties.index` (`PropertyBucket` v1), and `.markers` (`MarkerReader_3` v3).
2. **Unified Single-Leader Native Daemon (`ln-daemon`)**:
   - Route both CLI subcommands and `skill-ln mcp-stdio` through a single per-workspace background Rust daemon (`skill-ln daemon`, `< 15 MB` RAM) guarded by an OS file lock (`~/.ln_studio/daemon_<workspace_hash>.lock`).
   - Hold a single persistent HTTP/JCA session (`Pool Size = 1` `bshell` on `ProjectServer` with `GET ?method=share` multiplexed `conid`s for `<Project>_dev` and `<devEnv>_admin`), executing all BDE and `.admin` mutations through a thread-safe **Sequential FIFO Command Queue**.
3. **129-Class Bytecode Schema + Dual-Mode Lossless XML Engine (`ln-model`)**:
   - Mathematically extract all 129 TDE classes (`com.infor.ln.studio.common.core.model.tde.*`), `.model.additional.*`, 39 `owtemplates/*.xml`, and 9 `ScriptTemplates/` from Build 0640 bytecode into a version-controlled `rust/schemas/tde_schema_0640.json` so `cargo build` requires zero Infor JARs.
   - Use **Struct Generation** for new components (`create-*`) and **Lossless DOM Surgery** (in-place XML patching via `roxmltree` / `quick-xml`) for server-fetched components (`get`, `clone-component`, `inject`, `put`) so unknown vendor tags are never stripped.
4. **Zero-Copy Embedded Knowledge Base (`ln-kb`) & 25-Rule Parallel Linter (`ln-linter`)**:
   - Embed `functions_db.json` (2,266 functions), `studio_syntax_completion.json`, and documentation search indices into `skill-ln` using `rkyv` zero-copy archives (`0 ms` startup parse time).
   - Port all 25 static 4GL/DAL2/Extension rules (`ARR002`, `CAV001`, `CAV003`, `CLD001`–`002`, `DAL001`–`005`, `DBG001`, `DMN001`–`003`, `EXT001`–`003`, `INC001`, `SQL008`, `STR001`, `SYN001`–`002`, `TBL001`–`003`) to multi-threaded Rust (`rayon`).
5. **4-Layer Anti-Omission & Upgrade Safety Net (`ln-verify`)**:
   - (1) **Shadow / Differential Test Harness** against the Python/Java Golden Reference Oracle, (2) **Unknown Node Inspector** logging unmapped XML elements to `~/.ln_studio/unmapped_packets.log`, (3) **Sanitized Crash Fixture Recorder & Auto-Fallback** (`LN_FALLBACK_MODE=auto|strict|off`), and (4) **Built-in JVM Bytecode & Template Differ** (`skill-ln verify-studio-build`).

---

## User Stories

1. As an AI coding agent or LN engineer, I want a single native executable (`skill-ln.exe` / `skill-ln`) that starts in under 5 milliseconds with zero Python, JDK, or Eclipse JAR runtime requirements, so that every CLI command and MCP tool call executes instantaneously on any machine with only an `.ionapi` file.
2. As an LN developer working alongside the Eclipse LN Studio GUI, I want `skill-ln` to read and write `<activity>/.admin` using the exact Java Object Serialization (`0xACED0005`) binary format of `HashMap<String, AdministrationComponent>` (`serialVersionUID = 2L`), so that Eclipse LN Studio never purges my components during `Administration.removeObsoleteComponents()` and allows me to click `End Activity` in the GUI at any time.
3. As an LN developer, I want `skill-ln` to read and write the big-endian binary Eclipse `PropertyBucket` (`properties.index` v1) and decode binary `.markers` (`MarkerReader_3` v3) in pure Rust, so that project properties (`Label` / `labelUUID`, `ApplicationRelease`, `TaskVersionID`) and compiler markers stay 100% synchronized with Eclipse without spawning a JVM.
4. As an LN developer, I want `skill-ln` to detect active Eclipse instances via non-blocking OS file locking on `<workspace>/.metadata/.lock`, so that headless operations warn or coordinate cleanly when the Eclipse workbench is open.
5. As an LN developer in an enterprise Windows environment, I want `skill-ln` to use the OS native certificate store (`rustls-tls-native-certs`) and respect `HTTPS_PROXY` / `NO_PROXY` environment variables, so that corporate SSL inspection proxies and internal enterprise Root CAs work out of the box without certificate errors.
6. As an LN developer, I want `skill-ln` to implement the 3-Tier OAuth2 token lifecycle (cached token with 5-minute buffer $\rightarrow$ silent refresh via `refresh_token` or Service Account `saak`/`sask` $\rightarrow$ interactive browser loopback listener on `oob://localhost/lnstudio` or manual code paste) using the exact `~/.ln_studio/tokens/<workspace>.json` format, so that tokens are shared seamlessly between Rust and legacy Python tools.
7. As an LN developer, I want `skill-ln` to enforce the `Pre-Fetch-Auth-Gate` before any remote server interaction, verifying token validity and emitting a clear authentication notification banner when interactive login is required.
8. As an LN developer running both `skill-ln mcp-stdio` in my IDE and `skill-ln <subcommand>` in my terminal, I want both modes to connect to a **Single-Leader Native Daemon** (`skill-ln daemon`) per workspace locked via `~/.ln_studio/daemon_<workspace_hash>.lock`, so that only one `bshell` connection pool (`Pool Size = 1`) is opened on the Infor LN server and `.admin` writes never race.
9. As an LN developer, I want the **Single-Leader Native Daemon** to process all BDE calls through a **Sequential FIFO Command Queue**, automatically send `GET ?method=ping` keepalives at half the server `<timeout>` interval, support dynamic in-memory OAuth2 Bearer token hot-swap, and shut down after 30 minutes of idle time.
10. As an LN developer, I want the Rust JCA client to execute `GET ?method=connect` on `ProjectServer` and multiplex `<Project>_dev` and `<devEnv>_admin` (`protocol=bw`) over the same HTTP session and cookies via `GET ?method=share[&company=...]`, so that all repository endpoints share a single authenticated session just like Eclipse `HttpSessionLayer`.
11. As an LN developer, I want the Rust JCA client to support all **5 `BdeManager` Execution Modes** (`LIST=0`, `SHOW=1`, `BDE=2`, `SPECIALLIST=3`, `BROWSELIST=4`), `BdeSelection`, `BdeFilter`, `ControllingAttributes` (`{method};{attr};{in|out};false`), and automatic pagination (`<iteratorFetchSize>250</iteratorFetchSize>` + `<iteratorID>N</iteratorID>` loops), so that large component lists and synchronous server actions (`ConvertToRuntime`, `CreateTables`) execute identically to `JCAAdapter4ERPln`.
12. As an LN developer, I want the Rust JCA client to inspect the `X-Infor-BDEException` HTTP response header and HTTP `401`/`404`/`500` `<error>` XML payloads, converting server failures into structured `BdeExecutionError` diagnostics containing `<Result>` and `<InformationArea>` messages.
13. As an LN governance lead, I want `skill-ln` to physically hard-block `EndActivity`, `CloseTask`, `FinalizeActivity`, `DeliverActivity`, `<End/>`, and `<Deliver/>` at the lowest JCA transport boundary (`Pre-Commit-Boundary`), so that no CLI command or AI MCP call can ever close or deliver an activity on the server.
14. As an AI coding agent querying Baan 4GL / bshell documentation, I want `skill-ln fn-search <query>` and `skill-ln doc-search <query>` backed by a compile-time `rkyv` zero-copy database of all 2,266 bshell functions (`functions_db.json`), `studio_syntax_completion.json`, and cookbook indices, so that `Search-Before-Read` lookups complete in under 1 millisecond.
15. As an Infor LN developer writing 4GL, DAL 2, or Extension code, I want `skill-ln audit-4gl` (and `check-script`) to execute all **25 static lint rules** (`ARR002`, `CAV001`, `CAV003`, `CLD001`–`002`, `DAL001`–`005`, `DBG001`, `DMN001`–`003`, `EXT001`–`003`, `INC001`, `SQL008`, `STR001`, `SYN001`–`002`, `TBL001`–`003`) in parallel across files using `rayon`, producing identical rule IDs, line numbers, and severities to `audit_4gl.py`.
16. As an Infor LN developer, I want `skill-ln audit-4gl` to build an intra-file function call graph to detect direct and transitive nested transactions (`CAV003`) and validate table/field/domain/enum references (`TBL001`–`003`, `DMN001`–`003`) against `.ln_dd_cache.json` (with `--auto-fetch-dd` support).
17. As an Infor LN developer authoring Extension Modeler (`ttext1500m000`) scripts, I want `skill-ln` to enforce the **Non-Context Standard Code Boundary & Anti-Tamper (`EXT003`)**, **Declarations Include Boundary (`EXT001`)**, and **Hook Scope Enforcement (`EXT002`)** rules, ensuring code outside `#context_on` ... `#context_off` is treated as strictly immutable.
18. As a Rust contributor building `skill-ln` in CI, I want a bytecode schema extractor (`scripts/extract_tde_schema.py`) that extracts all 129 TDE classes from `lnstudio_commoncore.jar`, `.model.additional.*` from `fourglstudio_core.jar`, 39 `owtemplates/*.xml`, and 9 `ScriptTemplates/` into `rust/schemas/tde_schema_0640.json`, so that `cargo build` and `cargo test` require zero proprietary JARs.
19. As an LN developer scaffolding new components, I want `skill-ln` to generate valid Single-XML TDE files across all 12 component types (`.tbl`, `.ses`, `.dmn`, `.lib`, `.mnu`, `.lbl`, `.rpt`, `.msg`, `.qst`, `.fnc`, `.add`, `.bus`/`.cha`) from CLI flags or declarative multi-component YAML specs, placing module-scoped types at `{pkg}/{type}/{mod}/{name}.{ext}` and package-scoped types at `{pkg}/{type}/{name}.{ext}`.
20. As an LN developer modifying or cloning existing server components (`get-component`, `clone-component`, `inject`, `put`), I want `skill-ln` to use **Lossless DOM Surgery** (patching only target XML nodes such as `<expression><![CDATA[...]]></expression>` while preserving all untouched server elements and ordering byte-for-byte), so that server metadata is never lost on round-trip.
21. As an LN developer, I want `skill-ln` to automatically merge modified standalone `.4gl`/`.dal` script files into `<DR_Module><Source><expression>` (for `.ses`/`.tbl`) or `<Source><expression>` (for `.lib`/`.fnc`/`.rpt`) before `Put` or `CheckIn`, and abort if a non-empty script would be overwritten with an empty string.
22. As an LN developer, I want the **Unknown Node Inspector** in `ln-model` and `ln-jca` to compare every server XML response and component file against `tde_schema_0640.json` and log any unrecognized XML element or attribute to `~/.ln_studio/unmapped_packets.log` without failing the operation.
23. As an LN developer, I want `skill-ln validate` (with optional `--fix`) to execute the **Four-Layer Activity Validator**: (1) `.admin` registration and OS Read-Only SCM Guardrail across 12 extensions, (2) XML root/child structure and Ecore native integer datatypes (`1`=Byte, `2`=Double, `3`=Long, `5`=Numeric, `6`=String, `7`=Enum, `9`=Date, `14`=UTC), (3) cross-object references (`.lbl`, `.tbl`, `.mnu`), and (4) 25-rule static 4GL checks on `<expression>` blocks.
24. As an LN developer, I want `skill-ln` to support the full Software Project & Activity lifecycle (`project-info`, `new-activity`, `open-activity` with automatic `CMLabel.GetModifiedComponents` + `CmGet` download, `clean-activity`, `move-components`, `clean-components`) using authentic `SoftwareProject_V2` and `FglStudio` BDE payloads.
25. As an LN developer, I want `skill-ln` to enforce the `Read-Only-SCM-Guardrail` on local files and support the full Pre-Commit SCM lifecycle (`checkout-component`, `uncheckout-component`, `checkin-component`, `checkout-activity`, `checkin-activity`) while strictly blocking SCM check-out/check-in on Extension Modeler components (`ess`, `est`, `esb`, `esm`, `esr`) with `[GET_ONLY_EXTENSION]`.
26. As an LN developer, I want `skill-ln deploy-test` to support split execution modes (`--mode compile-only` running `Put/DR_Create -> Compile -> executeVSC -> CheckIn`, and `--mode schema-crdd` adding synchronous `ConvertToRuntime` and `CreateTables` with lock warnings), returning line-accurate `bic6.2` compiler diagnostics and VSC results.
27. As an LN developer, I want `skill-ln prepare-end-activity` to execute `DR_Solution.ValidateDevelopmentActivity` (with `<CMLabel>`) and `VSC.executeVSC` on the server, verify 100% local `.admin` and `properties.index` synchronization, and output a human handoff summary before manual `End Activity` in Eclipse.
28. As an LN developer, I want `skill-ln` to provide the complete `FglStudio` & `DR_Report` server intelligence suite: Ad-Hoc Server Compile (`compile-source`), Global Server Search (`search-server`), Call Hierarchy / Where-Used (`call-hierarchy`), Open Declaration (`open-declaration`), Related Components (`related-components`), Revision History (`revisions`), Structural Diff (`diff-component`), and Server Report Wizard (`generate-report-server`).
29. As an AI coding agent connecting over Model Context Protocol (`skill-ln mcp-stdio`), I want all **25 MCP Tools** (22 standalone tools + 3 consolidated multi-action tools: `ln_project_activity`, `ln_code_intelligence`, `ln_version_diff`, plus new knowledge lookup actions) returning the standardized **MCP Tool Envelope** (`{"status": "success" | "error", "action": str, "result": any, "message": str}`).
30. As an LN developer operating during the transition period, I want `skill-ln` to support `LN_FALLBACK_MODE=auto|strict|off`: whenever an unexpected BDE error or XML parse failure occurs, `skill-ln` saves a token-redacted **Sanitized Crash Fixture** to `~/.ln_studio/unmapped_packets/<timestamp>_<bde>_<method>.json` and (in `auto` mode) falls back to the legacy Python/Java runner for that single command.
31. As a platform maintainer upgrading to a future Infor LN Studio build after Build 0640, I want `skill-ln verify-studio-build --studio-home <path>` to inspect the new installation's `.jar` files, JVM `.class` (`0xCAFEBABE`) field tables/`serialVersionUID`s, and `owtemplates/*.xml` directly in Rust, reporting any schema or protocol diffs against Build 0640 in under 1 second.
32. As a maintainer running `python scripts/run_checks.py`, I want the Unified Checks Gateway to run `cargo test --workspace`, execute the **Shadow / Differential Test Harness** comparing Python/Java vs. Rust outputs 1:1, and package `skill-ln` in the release pipeline.

---

## Implementation Decisions

### 1. Cargo Workspace Topology (`rust/`)
The Rust implementation resides in `rust/` at the repository root and is structured as a multi-crate Cargo Workspace compiling into a single binary `skill-ln` (`skill-ln.exe` on Windows):
- `rust/Cargo.toml`: Workspace manifest with shared dependencies (`tokio`, `reqwest`, `roxmltree`, `quick-xml`, `serde`, `serde_json`, `rkyv`, `rayon`, `logos`, `clap`, `byteorder`, `sha2`).
- `rust/crates/ln-eclipse-compat`: Pure-Rust binary codecs for `.admin` (`0xACED0005`), `properties.index` (`PropertyBucket` v1), `.markers` (`MarkerReader_3` v3), `.project` XML, and `<workspace>/.metadata/.lock` OS lock detection.
- `rust/crates/ln-auth`: `.ionapi`, `cloudenv.prefs`, and `connectivity.prefs` parsers, 3-Tier OAuth2 token lifecycle (`~/.ln_studio/tokens/<workspace>.json`), loopback OOB HTTP listener (`oob://localhost/lnstudio`), and `Pre-Fetch-Auth-Gate`.
- `rust/crates/ln-jca`: Clean-room `HttpClient` (`connect`, `share`, `bdecall`, `ping`, `disconnect`, `dllcall`, `file_download`, `file_upload`), 5-Mode `JcaBdeManager` (`LIST`, `SHOW`, `BDE`, `SPECIALLIST`, `BROWSELIST`), `BdeSelection`, `BdeFilter`, `ControllingAttributes`, `BdeElementIterator` (`iteratorFetchSize=250`), `X-Infor-BDEException` handler, and protocol-level `EndActivity`/`CloseTask` hard-block.
- `rust/crates/ln-daemon`: Per-workspace **Single-Leader Native Daemon** (`~/.ln_studio/daemon_<workspace_hash>.lock` and `.json`) listening on `127.0.0.1:<ephemeral_port>` with a **Sequential FIFO Command Queue**, `Pool Size = 1` persistent `bshell` connection, keepalive timer, dynamic token hot-swap, and 30-minute idle timeout.
- `rust/crates/ln-kb`: Compile-time `rkyv` zero-copy knowledge base embedding `functions_db.json` (2,266 functions), `studio_syntax_completion.json`, and documentation search indices for `fn-search` and `doc-search`.
- `rust/crates/ln-linter`: Baan 4GL / DAL2 / Extension lexer, AST parser, intra-file call graph builder, `.ln_dd_cache.json` schema validator, `rayon` parallel file runner, and all **25 lint rules**.
- `rust/crates/ln-model`: `tde_schema_0640.json` schema loader, 12-component XML generators, multi-component YAML compiler, **Lossless DOM Surgery** engine (`inject`, `extract`, `clone-component`, `Pre-Put Script Merge`), **Unknown Node Inspector** (`~/.ln_studio/unmapped_packets.log`), and **Four-Layer Activity Validator** (`validate --fix`).
- `rust/crates/ln-scm`: Software Project & Activity lifecycle (`SoftwareProject_V2`), Component Explorer (`StudioComponent.GetBrowseList`, `CmGet`, `sync-reference`, `CmCreate`), Pre-Commit SCM state machine (`CmCheckOut`, `CmUnCheckOut`, `CmPut`, `CmCheckIn`), Build Pipeline (`Compile`, `ConvertToRuntime`, `CreateTables`, `VSC.executeVSC`, `deploy-test`, `prepare-end-activity`), Extension Modeler workflow (`new-extension`, `import-extension`, `extension-hooks`), and `FglStudio` / `DR_Report` code intelligence & revision diff.
- `rust/crates/ln-verify`: **Sanitized Crash Fixture** writer, `LN_FALLBACK_MODE=auto|strict|off` legacy Python/Java bridge delegator, and zero-dependency JVM `.class` (`0xCAFEBABE`) & `owtemplates` build differ (`verify-studio-build`).
- `rust/bins/skill-ln`: Unified CLI (`clap`, 56 Studio subcommands + `fn-search`, `doc-search`, `audit-4gl`, `verify-studio-build`) and `skill-ln mcp-stdio` (25 JSON-RPC 2.0 MCP tools over stdio).

---

### 2. Exact Wire & Binary Protocol Contracts

#### A. JCA HTTP/1.1 & BDE Envelope Contract (`ln-jca`)
- **Endpoint**: `{gateway_url}/{tenant}/LN/webservice`
- **Headers**:
  - `Authorization: Bearer <access_token>`
  - `User-Agent: JCAWebClient (LNStudio)`
  - `Accept: application/xml`
  - `Cookie: <k1>=<v1>; <k2>=<v2>` (captured from `Set-Cookie` on `?method=connect`)
- **Operations**:
  - `GET ?method=connect[&environment=<bse>][&company=<company>][&command=<cmd>][&clientHost=<host>][&clientIp=<ip>]` $\rightarrow$ `<ConnectResponse><company>...</company><lnuser>...</lnuser><timeout>300</timeout><conid>1</conid><version>1</version></ConnectResponse>`
  - `GET ?method=share[&company=<company>]` $\rightarrow$ `<ConnectResponse><conid>2</conid>...</ConnectResponse>` (multiplexes `<Project>_dev` and `<devEnv>_admin` over `ProjectServer` session)
  - `POST ?method=bdecall&bdename=<bdeName>&bdemethod=<bdeMethod>&conid=<conid>` (`Content-Type: application/xml;charset=utf-8`) $\rightarrow$ checks response header `X-Infor-BDEException` (`0` = success, `!= 0` = BDE exception)
  - `GET ?method=ping` (keepalive every `(timeout * 1000) / 2` ms)
  - `GET ?method=disconnect[&conid=<conid>]`
- **5 Execution Modes**:
  1. `LIST` (`0`) & `BROWSELIST` (`4`): `<{methodName}Request><ControlArea>[Selection][Filter][ActivityID][maxNumberOfObjects]<iteratorFetchSize>250</iteratorFetchSize>[ControllingAttributes]</ControlArea></{methodName}Request>`. Loops with `<iteratorID>N</iteratorID>` while response `<ControlArea>` contains `<iteratorID> >= 0`, merging all `<DataArea>` children.
  2. `SPECIALLIST` (`3`): Same `iteratorFetchSize=250` pagination loop as `LIST`, but includes `<DataArea><{bdeName}>...</{bdeName}></DataArea>` on the initial call.
  3. `SHOW` (`1`): Single request with `<ControlArea>` + `<DataArea><{bdeName}>...</{bdeName}></DataArea>`; returns first child element of `<DataArea>`.
  4. `BDE` (`2`): Single request with `<ControlArea>` + `<DataArea><{bdeName}>...</{bdeName}></DataArea>` (or empty payload if `request_xml` is empty).
- **Protocol-Level Hard-Block (`Pre-Commit-Boundary`)**:
  - Physically reject any call where `bde_name` or `method_name` (case-insensitive) matches `endactivity`, `closetask`, `finalizeactivity`, `deliveractivity`, `commitactivity`, `completeactivity`, or where `request_xml` contains `<endactivity`, `<closetask`, `<finalizeactivity`, `<deliveractivity`, `<end/>`, `<end>`, `<deliver/>`, or `<deliver>`.

#### B. `.admin` Java Object Serialization (`0xACED0005`) Contract (`ln-eclipse-compat`)
- Stream magic `0xACED`, version `0x0005`.
- Outer object: `java.util.HashMap` (`serialVersionUID = 362498820763181265L` / `0x0507DAC1C31660D1`, flags `0x03`, `F loadFactor = 0.75f`, `I threshold`, `TC_BLOCKDATA` 8 bytes `[i32 buckets, i32 size]`, followed by `size` entries of `(TC_STRING key, TC_OBJECT AdministrationComponent)`, terminated by `TC_ENDBLOCKDATA` `0x78`).
- Value class: `com.infor.ln.studio.common.core.cm.administration.AdministrationComponent` (`serialVersionUID = 2L` / `0x0000000000000002`, flags `0x02` `SC_SERIALIZABLE`, superclass `null`).
- **7 Fields in Exact JVM Serialization Order**:
  1. `Z` `isCheckedout` (`u8`: `0x00` or `0x01`)
  2. `Z` `isCreated` (`u8`)
  3. `Z` `isEvercheckedIn` (`u8`)
  4. `Z` `isExpired` (`u8`)
  5. `Z` `m_isDirty` (`u8`)
  6. `Z` `m_isVSCHappy` (`u8`)
  7. `L` `m_path` (`Ljava/lang/String;` — exact normalized project-relative path e.g. `tx/table/cmg/txcmg011.tbl`, never starting with `/` or `:<activity>/`)
- **State Machine Transitions (`CMStudio`)**:
  - `after_get`: `isCreated=false, isCheckedout=false, isEvercheckedIn=false, isExpired=false, m_isDirty=false, m_isVSCHappy=true`
  - `after_create`: `isCreated=true, isCheckedout=true, isEvercheckedIn=false, isExpired=false, m_isDirty=true, m_isVSCHappy=false`
  - `after_checkout`: `isCreated=false, isCheckedout=true, isEvercheckedIn=false, isExpired=false, m_isDirty=false, m_isVSCHappy=true`
  - `after_put`: `isCheckedout=true, m_isDirty=false` (preserving `isCreated`, `isEvercheckedIn`, `isExpired`, `m_isVSCHappy`)
  - `after_checkin`: `isCreated=false, isCheckedout=false, isEvercheckedIn=true, isExpired=false, m_isDirty=false, m_isVSCHappy=true`
  - `after_uncheckout`: if `isCreated && !isEvercheckedIn`, remove entry from map; otherwise set `isCreated=false, isCheckedout=false, m_isDirty=false, m_isVSCHappy=true`.

#### C. `properties.index` (`PropertyBucket` v1) & `.markers` (`MarkerReader_3` v3) Contracts
- **`properties.index`**: Big-endian `u8 version = 1`, `u32 entry_count`, per entry: `UTF path` (`u16` len + bytes; `""` for root), `u16 prop_count`, per property: `u8 qualifier_tag` (`2` = `QNAME` followed by `UTF qualifier` added to 0-based file table; `1` = `INDEX` followed by `i32` table index), `UTF local_name`, `UTF value`.
- **`.markers`**: Big-endian `u32 version = 3`, loop until EOF: `UTF resource_path`, `u32 markers_len`, per marker: `u64 id`, `u8 type_flag` (`1` = `INDEX u32`, `2` = `QNAME UTF`), `i16 attr_count`, per attribute: `UTF key`, `u8 val_type` (`1` = `u8 bool`, `2` = `i32`, `3` = `UTF`), `u64 creation_time`.

#### D. Complete 25 Static Linter Rules (`ln-linter`)
`ln-linter` must implement and verify 100% parity on all 25 rule IDs:
1. `SYN001` (`ERROR`): Block balancing (`select`/`endselect`, `if`/`endif`, `while`/`endwhile`, `for`/`endfor`, `repeat`/`until`, `case`/`endcase`, `function`/`endfunction`, `#context_on`/`#context_off`) and `void` function return value rejection (`Return value for void function not allowed`).
2. `SYN002` (`ERROR`): Lexical syntax errors, unterminated string literals, malformed preprocessor directives.
3. `INC001` (`WARNING`): `#include` validation against standard `<bic_*>` headers and missing includes.
4. `ARR002` (`WARNING`): Prohibits 1D domain string array declarations (`domain <str_dmn> var(n)`); enforces 2D syntax `string arr(len, n)`.
5. `SQL008` (`ERROR`): Prohibits array subscripts or parenthesized expressions inside SQL host bind variables (`:ident(...)`), preventing SQLState `42I03` Error `302`.
6. `STR001` (`WARNING`/`ERROR`): Prohibits assigning un-sliced `logname$` to 16-char user fields (`tfgld.user`); requires `strip$(shiftl$(logname$))(1; 16)`.
7. `CAV001` (`WARNING`): Prohibits direct floating-point equality (`==` / `<>` on `double` fields/variables); requires `double.cmp()`.
8. `CAV003` (`WARNING`/`ERROR`): Intra-file function call graph analysis detecting direct or transitive nested transactions (`db.retry.point()`, `commit.transaction()`, `abort.transaction()` inside an active transaction or DAL hook).
9. `CLD001` (`ERROR`): CloudSuite Multi-Tenant prohibited OS/host calls (`run.prog`, `shell`, `app_start`, untrusted functions where `Trusted="no"` in `functions_db.json`).
10. `CLD002` (`WARNING`): CloudSuite Multi-Tenant high-risk / deprecated calls.
11. `DAL001` (`ERROR`): Prohibits interactive UI calls (`message()`, `ask.enum()`, `box()`, `input.string()`) inside DAL scripts.
12. `DAL002` (`ERROR`): Enforces DAL2 hook naming conventions, parameter prototypes, and return types (`0` vs `DALHOOKERROR`).
13. `DAL003` (`ERROR`): Prohibits direct `db.insert`/`db.update`/`db.delete` on the owning table inside its own DAL; enforces `dal.new.object()` / `dal.change.object()` / `dal.destroy.object()`.
14. `DAL004` (`ERROR`): Enforces mandatory `dal.set.error.message()` before returning `DALHOOKERROR` in DAL hooks.
15. `DAL005` (`ERROR`): Prohibits manual transaction control (`db.retry.point()`, `commit.transaction()`, `abort.transaction()`) inside DAL object/property hooks.
16. `DBG001` (`WARNING`/`ERROR`): Flags interactive `message()` popups in headless/batch/DLL contexts.
17. `DMN001` (`ERROR`): Validates `domain <name>` declarations against `.ln_dd_cache.json`.
18. `DMN002` (`ERROR`): Enforces datatype/domain assignment compatibility (including `Julian Day (Date 4)` vs `UTC Epoch Timestamp` mismatch prevention per ADR 0017).
19. `DMN003` (`WARNING`/`ERROR`): Detects cross-domain enum constant comparisons/assignments (`Enum Value Space Collision`).
20. `EXT001` (`ERROR`): Enforces Extension Modeler `#include` placement (permits standard generated includes under `| Additional generated declarations`; flags custom includes outside `#context_on "declarations"`).
21. `EXT002` (`ERROR`): Enforces Extension Hook Scope separation (Table Extensions `est` only allow DAL hooks; Session Extensions `ess` only allow UI/Form Command hooks, and `.before.command`/`.after.command` must be `void`).
22. `EXT003` (`ERROR`): Enforces **Non-Context Standard Code Boundary & Anti-Tamper** (ADR 0020) — flags any mutation/deletion of standard generated framework functions (`get.extension.point.version`, `ext.get.*`), malformed `#context_on`/`#context_off` pairs, or custom functions placed outside `#context_on` blocks.
23. `TBL001` (`ERROR`): Verifies every `<table>.<field>` referenced in 4GL or Baan SQL (excluding the main table) has a `table t<table>` declaration in `declaration:`.
24. `TBL002` (`ERROR`): Validates `<table>.<field>` existence against `.ln_dd_cache.json`.
25. `TBL003` (`ERROR`): Enforces table index usage in `SELECT` queries and flags `Mandatory: Yes` on line-number columns (`line`, `lino`, `seqn`) where `0` is a valid natural value.

#### E. Complete CLI Surface (60 Subcommands) & MCP Surface (25 Tools)
- **CLI Subcommands (`skill-ln <subcommand>`)**:
  - All 56 existing `ln_component_builder.py` subcommands (`workspace`, `environments`, `login`, `connect`, `project`, `project-info`, `activity`, `new-activity`, `open-activity`, `clean-activity`, `daemon`, `explorer`, `get-component`, `sync-reference`, `clone-component`, `checkout-component`, `uncheckout-component`, `checkin-component`, `checkout-activity`, `checkin-activity`, `end-activity`, `prepare-end-activity`, `compile-source`, `search-server`, `call-hierarchy`, `open-declaration`, `related-components`, `revisions`, `diff-component`, `generate-report-server`, `move-components`, `clean-components`, `table`, `session`, `domain`, `library`, `menu`, `component`, `message`, `question`, `function`, `additional`, `report`, `inject`, `extract`, `check-script`, `validate`, `sync-admin`, `diagnose`, `build`, `pipeline`, `new-extension`, `import-extension`, `extension-hooks`, `deploy-test`, `mcp-setup`)
  - Plus 4 unified native subcommands:
    57. `mcp-stdio` (starts the native JSON-RPC 2.0 Stdio MCP server)
    58. `audit-4gl` (runs the 25-rule `rayon` parallel 4GL/DAL/Extension linter)
    59. `fn-search` / `doc-search` (sub-millisecond `rkyv` knowledge base lookup)
    60. `verify-studio-build` (zero-dependency JVM `.class` & XML template differ for new LN Studio builds)
- **MCP Tools (`skill-ln mcp-stdio`)**:
  - All 25 MCP tools from `ln_studio_mcp.py` (`ln_list_environments`, `ln_login`, `ln_connect`, `ln_explore_projects`, `ln_explore_activities`, `ln_explore_components`, `ln_create_activity`, `ln_clean_activity`, `ln_get_component`, `ln_sync_reference`, `ln_checkout_component`, `ln_uncheckout_component`, `ln_checkin_component`, `ln_checkout_activity`, `ln_checkin_activity`, `ln_create_component`, `ln_clone_component`, `ln_validate_activity`, `ln_deploy_test`, `ln_prepare_end_activity`, `ln_end_activity`, `ln_adhoc_compile`, `ln_project_activity`, `ln_code_intelligence`, `ln_version_diff`) returning the exact **MCP Tool Envelope** (`{"status": "success" | "error", "action": str, "result": any, "message": str}`).

---

## Testing Decisions

### Primary High-Level Testing Seams
To minimize seam proliferation while guaranteeing 100% behavioral parity, verification centers on **three high-level seams**:
1. **Seam 1: Differential Parity Harness (`scripts/run_checks.py` & `cargo test --workspace`)**:
   - Executes identical inputs against the legacy Python/Java Golden Reference Oracle and the new Rust crates (`ln-eclipse-compat`, `ln-model`, `ln-linter`, `ln-kb`), asserting byte-for-byte equality on `.admin` (`0xACED0005`), `properties.index`, and `.markers`, canonical XML equality on all 12 component types, and 100% identical `(rule_id, line, severity)` diagnostic sets across all 25 linter rules.
2. **Seam 2: Local Loopback Mock BDE Server (`ln-jca` & `ln-daemon` Integration Seam)**:
   - A lightweight local HTTP/1.1 mock server in Rust simulating `{gateway_url}/{tenant}/LN/webservice` (`?method=connect`, `?method=share`, `?method=bdecall`, `?method=ping`, `?method=disconnect`, `X-Infor-BDEException` headers, and multi-page `<iteratorID>` responses) to test the full `skill-ln` CLI and `mcp-stdio` JSON-RPC pipeline hermetically without network dependencies.
3. **Seam 3: Live CloudSuite Verification Seam (`SCS_TEST`, Activity `dev_natt_v01108-1`)**:
   - End-to-end smoke verification against the live `SCS_TEST` tenant using externalized `.ionapi` credentials (never committed to Git), validating OAuth2 token refresh, `project-info`, `open-activity`, `get-component`, `compile-source`, and Eclipse LN Studio workspace coexistence.

### Prior Art in Codebase
- `ln_studio_skill/tools/tests/test_properties_index.py` (binary `PropertyBucket` round-trip tests)
- `ln_studio_skill/tools/tests/test_env_and_jca_bridge.py` (5-mode BDE dispatch and daemon tests)
- `ln_studio_skill/tools/tests/test_mcp_tool_execution.py` (hermetic MCP envelope tests)
- `erp-ln-progguide/tests/test_audit_4gl.py` (25-rule static 4GL auditor test corpus)

---

## Out of Scope

1. **Automated Activity Closure / Delivery (`EndActivity` / `CloseTask` / `<End/>` / `<Deliver/>`)**: Remains physically hard-blocked per ADR 0007 / ADR 0021; final activity closure is always performed by a human engineer in LN Studio after running `prepare-end-activity`.
2. **SCM Check-Out / Check-In of Extension Modeler Components (`ess`, `est`, `esb`, `esm`, `esr`)**: Physically prohibited by Infor LN Studio (`ttext1500m000`); remains governed by ADR 0006 and ADR 0020 (`[GET_ONLY_EXTENSION]` + `Guide-and-Paste`).
3. **Graphical Desktop Form/Report Canvas Rendering**: Visual drag-and-drop SWT editors remain inside Eclipse RCP; `skill-ln` handles all headless XML modeling, scripting, validation, compilation, and SCM operations.
4. **Committing Live Credentials or `.ionapi` Secrets to Git**: All live testing against `SCS_TEST` must read `.ionapi` and credentials from gitignored paths or environment variables.

---

## Further Notes

- **Execution Model for Subagents**: All implementation tickets in `.scratch/native-rust-skill-ln/issues/` are designed to be executed sequentially or along the unblocked dependency frontier by **Gemini 3.8 Flash (`flash`)**. Every ticket contains explicit acceptance criteria, exact binary/XML field specifications, and a mandatory verification command (`cargo test` + `python scripts/run_checks.py`).
