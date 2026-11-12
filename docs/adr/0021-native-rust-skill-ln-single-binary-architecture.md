# ADR 0021: 100% Native Rust Single-Binary Architecture (`skill-ln`), Zero-JAR/Zero-JDK Runtime, and 4-Layer Anti-Omission Verification

- **Status**: Accepted
- **Date**: 2026-11-12
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`
- **Specification & Master Plan**: [`docs/plans/native-rust-skill-ln-plan.md`](../plans/native-rust-skill-ln-plan.md)
- **Prior ADRs**:
  - [`docs/adr/0007-headless-jca-connectivity-scm-and-mcp-server.md`](0007-headless-jca-connectivity-scm-and-mcp-server.md) *(Preserved: Pre-Commit SCM Boundary — hard-blocking `EndActivity` / `CloseTask` / `Deliver`)*
  - [`docs/adr/0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md`](0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md) *(Superseded on runtime BYOJ requirement: `skill-ln` runs 100% standalone without Infor JARs or JDK at runtime)*
  - [`docs/adr/0012-rea-100-percent-ln-studio-parity-and-daemon-architecture.md`](0012-rea-100-percent-ln-studio-parity-and-daemon-architecture.md) *(Evolved from `LNStudioJcaBridge.java` JVM daemon to Native Rust Single-Leader Daemon and byte-exact `.admin` / `properties.index` / `.markers` codecs)*
  - [`docs/adr/0020-extension-modeler-non-context-std-boundary-and-anti-tamper-guardrails.md`](0020-extension-modeler-non-context-std-boundary-and-anti-tamper-guardrails.md) *(Preserved: `EXT001`–`EXT003` Non-Context Read-Only & Anti-Tamper rules)*

---

## 1. Context & Problem Statement

While ADR 0012 achieved 100% functional parity with Eclipse Infor LN Studio 10.8 (build 0640) using Python 3 orchestrating a background JVM daemon (`LNStudioJcaBridge.java` and `AdminSyncHelper.java` against proprietary Infor JARs), three structural bottlenecks remained:
1. **Runtime Dependency on JDK 11+ & Eclipse LN Studio JARs**: Running the toolchain required locating `JCAAdapter4ERPln-10.8.10.jar`, `lnstudio_commoncore.jar`, and a local JDK (`java`/`javac`), adding hundreds of megabytes of JVM memory overhead and startup latency.
2. **Multi-Language Runtime Fragmentation**: AI agents invoked separate Python scripts (`ln_component_builder.py`, `ln_studio_mcp.py`, `audit_4gl.py`, `search.py`) that spawned JVM subprocesses or parsed large JSON dictionaries (`functions_db.json`) on every invocation.
3. **Regression & Schema Drift Risk during Reverse Engineering**: Porting a complex enterprise IDE protocol and 12 component metamodels requires deterministic safeguards against unmapped XML tags, server error edge cases, and future Infor LN Studio build updates.

### Ground-Truth Bytecode Findings (REA Disassembly of Build 0640)

A full bytecode disassembly of `JCAAdapter4ERPln-10.8.10.jar` and `lnstudio_commoncore.jar` established three foundational facts that make a 100% clean-room Native Rust implementation feasible with zero proprietary JAR dependencies at runtime:

1. **Plain HTTP/1.1 + UTF-8 XML Wire Protocol (`com.infor.erpln.protocol.HttpClient` & `JcaBdeManager`)**:
   - `http_oauth2` (method `11`) uses standard HTTPS `GET` and `POST` against `{gateway_url}/{tenant}/LN/webservice` with `Authorization: Bearer <token>`, `User-Agent: JCAWebClient (LNStudio)`, `Accept: application/xml`, and session `Cookie` headers captured from `?method=connect`.
   - There is **no custom binary framing or proprietary encryption** on the wire:
     - `GET ?method=connect[&environment=...][&company=...]` $\rightarrow$ returns `<ConnectResponse><conid>...</conid><timeout>300</timeout><version>1</version></ConnectResponse>`.
     - `GET ?method=share[&company=...]` $\rightarrow$ multiplexes `protocol=bw` aliases (`<Project>_dev`, `<devEnv>_admin`) over the existing `ProjectServer` HTTP session and cookies, returning a dedicated `<conid>`.
     - `POST ?method=bdecall&bdename=<bdeName>&bdemethod=<bdeMethod>&conid=<conid>` $\rightarrow$ transmits `<{methodName}Request><ControlArea>...</ControlArea><DataArea>...</DataArea></{methodName}Request>` and checks response header `X-Infor-BDEException` (`0` = OK, `!= 0` = BDE exception).
     - `GET ?method=ping` and `GET ?method=disconnect[&conid=<conid>]`.
   - `LIST` (`0`), `BROWSELIST` (`4`), and `SPECIALLIST` (`3`) auto-paginate using `<iteratorFetchSize>250</iteratorFetchSize>` and loop on response `<ControlArea><iteratorID>N</iteratorID></ControlArea>`.

2. **Fixed Java Object Serialization Layout of `.admin` (`0xACED0005`)**:
   - `<activity>/.admin` is a standard `java.io.ObjectOutputStream` stream containing `java.util.HashMap<String, AdministrationComponent>` (`serialVersionUID = 362498820763181265L`).
   - `com.infor.ln.studio.common.core.cm.administration.AdministrationComponent` has `serialVersionUID = 2L` (`0x0000000000000002`), implements `java.io.Serializable` without custom `writeObject`, and serializes **7 exact fields in canonical JVM order**:
     1. `Z` `isCheckedout` (`u8` boolean)
     2. `Z` `isCreated` (`u8` boolean)
     3. `Z` `isEvercheckedIn` (`u8` boolean)
     4. `Z` `isExpired` (`u8` boolean)
     5. `Z` `m_isDirty` (`u8` boolean)
     6. `Z` `m_isVSCHappy` (`u8` boolean)
     7. `L` `m_path` (`Ljava/lang/String;`, exact project-relative path without leading slash)

3. **Pure 1-to-1 Reflection TDE Component Models (`com.infor.ln.studio.common.core.model.tde.*`)**:
   - Infor LN Studio does not ship `.ecore` files for the 12 component types; instead, `TDEParentNode` and `TDEProperties` serialize and deserialize XML via 1-to-1 Java reflection over the `public` fields of **129 classes** (`32` in `.model.tde.*`, `97` in `.model.tde.concrete.*`, plus `DR_Solution` and `.model.additional.*`).
   - There are **zero XML attributes** in TDE component XMLs; every valid XML element name is literally `field.getName()`, `_cdata` maps to `<![CDATA[...]]>`, and `List<T>` generic signatures are preserved in the `.class` `Signature` attribute—allowing 100% mathematical extraction of the entire 12-component schema into `tde_schema_0640.json`.

---

## 2. Settled Architectural Decisions (`Q1`–`Q17`)

### Decision 1: Multi-Crate Cargo Workspace Compiling to a Single Binary (`skill-ln` / `skill-ln.exe`)
- Organize the Rust codebase under `rust/` as a modular **Cargo Workspace** (`ln-jca`, `ln-auth`, `ln-model`, `ln-eclipse-compat`, `ln-scm`, `ln-linter`, `ln-kb`, `ln-Verify`, and binary crate `skill-ln`) that compiles into a single self-contained native binary (`skill-ln.exe` on Windows, `skill-ln` on Linux/macOS) with `< 5 ms` cold startup and `~10–15 MB` RSS memory footprint.
- Unify **both** `erp-ln-progguide` (`fn-search`, `doc-search`, `audit-4gl` with all 25 rules) and `ln_studio_skill` (all 56 CLI subcommands and 25 MCP stdio tools) inside `skill-ln`.

### Decision 2: 100% Eclipse LN Studio Binary Compatibility without Java (`ln-eclipse-compat`)
- Maintain 100% bidirectional compatibility with Eclipse LN Studio GUI on the same workspace folder so engineers can open Eclipse at any time to inspect components or click `End Activity`:
  - Implement a dedicated zero-JVM **`.admin` Java Serialization (`0xACED0005`) Reader/Writer** in Rust supporting `HashMap<String, AdministrationComponent>` (`serialVersionUID = 2L`).
  - Implement native big-endian binary codecs for Eclipse **`properties.index`** (`PropertyBucket` version `1`) and **`.markers`** (`MarkerReader_3` version `3`).

### Decision 3: Unified Single-Leader Native Daemon per Workspace (`skill-ln daemon`)
- Prevent server-side `bshell` proliferation and local `.admin` race conditions between concurrent CLI invocations and `skill-ln mcp-stdio`:
  - Both CLI commands and `skill-ln mcp-stdio` route stateful JCA and `.admin` operations through a single per-workspace **Single-Leader Daemon** (`skill-ln daemon`), coordinated via an OS file lock at `~/.ln_studio/daemon_<workspace_hash>.lock` and local IPC (`127.0.0.1:<port>` recorded in `daemon_<workspace_hash>.json`).
  - The daemon holds a single persistent HTTP/JCA session (`Pool Size = 1` `bshell` on `ProjectServer` with `method=share` multiplexed `conid`s for `<Project>_dev` and `<devEnv>_admin`), executes commands strictly through a **Sequential FIFO Queue**, performs automatic keepalive pings (`timeout / 2`), supports in-memory OAuth2 token hot-swap, and auto-terminates after 30 minutes of inactivity.

### Decision 4: Dual-Mode XML Engine (`roxmltree` + `quick-xml`) & Lossless DOM Surgery (`ln-model`)
- Extract the complete 129-class TDE field hierarchy from `lnstudio_commoncore.jar` once into a version-controlled **`rust/schemas/tde_schema_0640.json`** so `cargo build` requires zero proprietary JARs.
- Operate in two distinct XML modes:
  1. **New Component Creation (`create-*`)**: Emit deterministic, field-order-exact XML from strongly typed Rust structs generated from `tde_schema_0640.json`.
  2. **Server Component Mutation (`get`, `clone-component`, `inject`, `put`)**: Use **Lossless DOM Surgery (In-place XML Patching)** so only modified nodes (such as `<expression><![CDATA[...]]></expression>`) are updated while 100% of existing server tags, ordering, and vendor metadata remain untouched byte-for-byte.

### Decision 5: Zero-Copy Embedded Knowledge Base (`rkyv`) & 25-Rule Parallel Linter (`ln-linter`, `ln-kb`)
- Pre-compile `functions_db.json` (2,266 bshell functions), `studio_syntax_completion.json`, and documentation indices into zero-copy `rkyv` binary archives embedded via `include_bytes!` in `build.rs`, eliminating startup JSON parsing (`0 ms` deserialization).
- Port all **25 static analysis rules** (`ARR002`, `CAV001`, `CAV003`, `CLD001`–`002`, `DAL001`–`005`, `DBG001`, `DMN001`–`003`, `EXT001`–`003`, `INC001`, `SQL008`, `STR001`, `SYN001`–`002`, `TBL001`–`003`) into `ln-linter` with `rayon` multi-threaded workspace auditing and `.ln_dd_cache.json` integration.

### Decision 6: 100% Zero-JAR Standalone Runtime & Enterprise TLS (`ln-jca`, `ln-auth`)
- `skill-ln` runs **100% standalone without `LN_STUDIO_HOME`, Eclipse, or JDK** on any machine given only an `.ionapi` profile and workspace folder.
- Configure `reqwest` with **`rustls-tls-native-certs`** and system proxy awareness (`HTTPS_PROXY`, `NO_PROXY`) to trust Windows Enterprise Root CAs out of the box.
- Preserve 100% JSON schema compatibility for `~/.ln_studio/tokens/<workspace>.json` across the 3-Tier OAuth2 lifecycle so Python and Rust tools share active tokens seamlessly.

### Decision 7: 4-Layer Anti-Omission & Build-Upgrade Protection System
1. **Shadow / Differential Test Harness**: Retain the existing Python + Java toolchain as a Golden Reference Oracle during the 5-phase strangler migration, running 1:1 canonical XML diffs and mock BDE server comparisons in `scripts/run_checks.py`.
2. **Unknown Node Inspector (`unmapped_packets.log`)**: Every BDE response and server component XML parsed by `roxmltree` is checked against `tde_schema_0640.json` and known BDE response schemas; any unrecognized element or attribute is automatically logged with context to `~/.ln_studio/unmapped_packets.log`.
3. **Sanitized Crash Fixtures & Graceful Fallback (`LN_FALLBACK_MODE=auto|strict|off`)**: On any unexpected BDE exception or parse failure, `skill-ln` redacts bearer tokens, writes a reproducible test fixture to `~/.ln_studio/unmapped_packets/<timestamp>_<bde>_<method>.json`, and (when `LN_FALLBACK_MODE=auto`) transparently delegates that single command to the legacy Python/Java bridge.
4. **Built-in JVM Bytecode & Template Differ (`skill-ln verify-studio-build`)**: Embed a zero-dependency `.jar`/`.class` (`0xCAFEBABE`) and `owtemplates/*.xml` inspector inside `skill-ln` that diffs any future Infor LN Studio build against the embedded Build 0640 baseline manifest in `< 1 second` without external `jadx` dependencies.

---

## 3. Architecture Comparison

| Dimension | Legacy Python + Java Bridge (ADR 0012) | Native Rust `skill-ln` (ADR 0021) |
|---|---|---|
| **Runtime Dependencies** | Python 3 + JDK 11+ + Infor Eclipse JARs (`BYOJ`) | **Zero (`skill-ln.exe` single native binary)** |
| **Cold Startup / RAM** | `~150–400 ms` Python + `~80–150 MB` JVM daemon | **`< 5 ms` CLI / `~8–15 MB` Native Rust daemon** |
| **JCA Transport (`http_oauth2`)** | Wraps `JCAAdapter4ERPln-10.8.10.jar` in JVM | **Clean-room Rust (`reqwest` + `rustls-tls-native-certs`)** |
| **`.admin` & `properties.index`** | Spawns `java AdminSyncHelper` (`ObjectOutputStream`) | **Native Rust `0xACED0005` & `PropertyBucket` binary codecs** |
| **12-Component XML Handling** | Python `ElementTree` templates | **129-class Bytecode Schema + Lossless DOM Surgery** |
| **4GL Static Linter (25 Rules)** | Single-threaded Python (`audit_4gl.py`) | **Multi-threaded Rust (`rayon`) + `rkyv` zero-copy DB (`50–100x` faster)** |
| **Unmapped Tag / Upgrade Safety** | Manual REA investigation | **Auto Unknown-Node Logger + Crash Fixture + `verify-studio-build`** |
