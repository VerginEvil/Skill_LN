# ADR 0012: 100% Eclipse LN Studio 10.8 Parity via REA Bytecode Ground Truth, Persistent JCA Daemon, and Exact Metadata Serialization

- **Status**: Accepted
- **Date**: 2026-10-30
- **Target Skill**: `ln_studio_skill`
- **Specification**: [`.scratch/rea-100-percent-ln-studio-parity/spec.md`](../../.scratch/rea-100-percent-ln-studio-parity/spec.md)
- **Prior ADRs**:
  - [`docs/adr/0006-ln-studio-extension-readonly-and-lnui-workflow.md`](0006-ln-studio-extension-readonly-and-lnui-workflow.md) *(Preserved: Native Extension Modeler `ess`, `est`, `esb`, `esm`, `esr` components are blocked from Studio SCM and routed to LN UI `ttext1500m000`, whereas custom `tx*` 4GL components use full Studio SCM)*
  - [`docs/adr/0007-headless-jca-connectivity-scm-and-mcp-server.md`](0007-headless-jca-connectivity-scm-and-mcp-server.md) *(Refined with 5-mode `JcaBdeManager` execution, Persistent Daemon, and authentic XML payloads)*
  - [`docs/adr/0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md`](0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md) *(Preserved: BYOJ, split `deploy-test` modes, protocol-level `EndActivity` hard-block)*
  - [`docs/adr/0011-automated-scm-engine-refactoring-and-protocol-recovery.md`](0011-automated-scm-engine-refactoring-and-protocol-recovery.md) *(Extended from SCM CheckOut/CheckIn to 100% of Build, Explorer, Project/Activity, `.admin`, `properties.index`, and `FglStudio` operations)*

---

## 1. Context & Problem Statement

To make `ln_studio_skill` operate as a 100% functional headless replacement for the Eclipse-based **Infor LN Studio 10.8 (build 0640)** without opening the Eclipse GUI—while remaining 100% compatible when a developer later opens Eclipse LN Studio to inspect or click `End Activity`—a comprehensive **REA (Reverse Engineer Anything)** bytecode decompilation was conducted across:
- `com.infor.ln.studio.common.connectivity_10.8.0.0640.jar` (`lnstudio_connectivity.jar`)
- `com.infor.ln.studio.common.core_10.8.0.0640.jar` (`lnstudio_commoncore.jar` + `owtemplates/*.xml`)
- `com.infor.ln.studio.apps.core_10.8.0.0640.jar` (`fourglstudio_core.jar`)
- `com.infor.ln.studio.apps.proxy_10.8.0.0640.jar` (`fourglstudio_proxy.jar`)
- `org.eclipse.core.resources_3.22.100.v20250206-1238.jar`

### Root Causes Identified by REA Bytecode Inspection

1. **Process-per-Call JVM Spawning vs. Single Persistent Bshell Connection**:
   - `HeadlessJavaJcaTransport.do_bde_call()` spawned a new `java LNStudioJcaBridge` process for every single BDE call and immediately closed the connection (`conn.close()`).
   - Every JCA connection spawns a server-side `bshell` process. Opening/closing connections across `CheckOut -> Put -> Compile -> CRDD -> VSC -> CheckIn` wastes licenses, drops session state, and risks database row lock collisions.

2. **5-Mode `BdeManager` Execution Mismatch (`Template.java`)**:
   - `LNStudioJcaBridge.java` only invoked `bdeMgr.executeMethod(reqElement, methodName)`.
   - In reality, `com.infor.ln.studio.common.connectivity.core.Template` dispatches across **5 distinct `BdeManager` modes**:
     - Mode `0` (`LIST`) & Mode `4` (`BROWSELIST`): `bdeMgr.executeList(bdeName, methodName, bdeSelection, bdeFilter, maxNoOfObjects)`
     - Mode `1` (`SHOW`): `bdeMgr.executeShow(reqElement, methodName, bdeSelection, bdeFilter)`
     - Mode `2` (`BDE`): `bdeMgr.executeMethod(reqElement, methodName)`
     - Mode `3` (`SPECIALLIST`): `bdeMgr.executeSpecialList(bdeName, methodName, bdeSelection, reqElement)`
   - Furthermore, operations like `GetBrowseList`, `ConvertToRuntime`, and `CreateTables` require `bdeMgr.setSpecificControlAttributeMetaData("{method}:{attr}:{in|out}")` and `bdeMgr.setSpecificControlAttribute(attr, value)`.

3. **Fabricated Build, Explorer & Project XML Payloads**:
   - `ln_build_pipeline.py` sent invented `<CompileRequest>`, `<ConvertToRuntimeRequest>`, `<CreateTablesRequest>`, and `<executeVSCRequest>` wrappers and parsed non-existent `<CompileResponseError>` tags.
   - Bytecode truth:
     - `Compile` (`executeShow` on `DR_*`): `<{bdeName}><name>{compName}</name><isCheckedOut>{yes|no}</isCheckedOut></{bdeName}>`, returning `<compileResult><error line="..." source="..."/><warning line="..." source="..." level="..."/><summary .../><bicCommand>...</bicCommand></compileResult>`.
     - `ConvertToRuntime` (`executeBde` on `DR_*` with control attribute `ConvertToRuntime:executionMethod:in=synchronous`): `<{bdeName}><name>{compName}</name><type>{itemType}</type></{bdeName}>`.
     - `CreateTables` (`executeBde` on `DR_Table` with control attribute `CreateTables:executionMethod:in=synchronous`): `<DR_Table><name>{tableName}</name><type>table</type></DR_Table>`.
     - `ExecuteVSC` (`executeShow` on BDE `"VSC"`): `<VSC><componentName>{compName}</componentName><componentType>{itemType}</componentType></VSC>`, returning `<vscResult verificationCode="..."><warning .../></vscResult>`.
     - `CmGet` (`executeBde` on `StudioComponent` or `DR_*`): `<{bdeName}><name>{name}</name><type>{type}</type><includeCustomerFields>yes</includeCustomerFields><optionalContent>yes</optionalContent></{bdeName}>`.
     - `CmCreate` (`DR_Create`): sends the **raw component root XML element** (`<DR_Table>...</DR_Table>`) directly without any `<DR_CreateRequest>` wrapper.
     - `<ActivityID>` ControlArea requires `<activityUUID>{labelUUID}</activityUUID>` (the task's `Label` property from `SoftwareProject_V2`), NOT `taskName` or `taskUUID` (which is the PMC Solution code).

4. **Eclipse Overwrite & Phantom Deletion Root Causes (`.admin` `m_path`, Single-XML Layout & Binary `properties.index`)**:
   - **`AdminSyncHelper.java` `m_path` Bug**: Set `m_path = ":" + actFolder + "/" + relPath`. When Eclipse starts up, `Administration.removeObsoleteComponents()` walks `IProject.findMember(segment)` using `comp.getPath()`. Because `m_path` included `:actFolder/`, Eclipse failed to locate the resource and **silently deleted the entry from `.admin`**! Both the `HashMap` key and `m_path` MUST be the exact project-relative path without leading slash (e.g., `"tx/table/cmg/txcmg011.tbl"`).
   - **Exact Single-XML Workspace Layout (`TDEResource`)**: Eclipse stores components as a **single XML file** on disk (with 4GL/DAL scripts embedded inside `<DR_Module><Source><expression><![CDATA[...]]></expression></Source></DR_Module>` for `.ses`/`.tbl` or `<Source><expression><![CDATA[...]]></expression></Source>` for `.lib`/`.fnc`/`.rpt`):
     - Module-scoped (`session`, `report`, `table`, `library`, `function`, `menu`, `additional`, `businessobject`): `{pkg}/{type}/{mod}/{name}.{ext}`
     - Package-scoped (`domain`, `label`, `message`, `question`, `chart`): `{pkg}/{type}/{name}.{ext}` (no `{mod}` subfolder!)
   - **Binary `properties.index` (`PropertyBucket`)**: `ln_project_activity_manager.py` wrote a plain-text `.settings/properties.index` inside the activity folder. Eclipse actually reads a **big-endian binary `DataOutputStream` `PropertyBucket`** at `<workspace>/.metadata/.plugins/org.eclipse.core.resources/.projects/<ProjectFolderName>/.indexes/properties.index` containing `ProjectProperties` (`qualifier=""`: `ProjectName`, `ApplicationRelease`, `TaskName`, `Label`, `TaskVersionID`, `TaskContext`, `DevelopmentEnvironment`, etc.).

---

## 2. Settled Architectural Decisions

### Decision 1: Persistent `LNStudioJcaBridge` Daemon with Single Connection Pool & Sequential FIFO Queue
1. Upgrade `LNStudioJcaBridge.java` to run as a per-workspace **Persistent Background Daemon** listening on `127.0.0.1:<ephemeral_port>` (registered in `~/.ln_studio/daemon_<workspace_hash>.json`).
2. Maintain a **Single Persistent JCA Connection** (`Pool Size = 1` per connection point: `ProjectServer`, `<Project>_dev`, `<devEnv>_admin`) backed by a thread-safe **Sequential FIFO Command Queue** so `CheckOut -> Put -> Compile -> CRDD -> VSC -> CheckIn` execute strictly in sequence on the same `bshell` without database lock contention.
3. Support **Dynamic OAuth2 Token Hot-Swap** (updating the active `OAuth2Callback` token in-memory when `ln_env_manager.py` refreshes tokens) and a 30-minute idle auto-shutdown timer.
4. Support all **5 `BdeManager` Execution Modes** (`LIST`, `SHOW`, `BDE`, `SPECIALLIST`, `BROWSELIST`), `BdeSelection`, `BdeFilter`, and `ControllingAttributes` (`setSpecificControlAttributeMetaData` / `setSpecificControlAttribute`).

### Decision 2: Complete Software Project Version & Activity Lifecycle (`project-info`, `new-activity`, `open-activity`)
1. **Software Project Version & Metadata (`project-info` / `ShowSoftwareProjectV2`)**:
   - Invoke `SoftwareProject_V2.Show` via `executeShow` (`<SoftwareProject_V2><projectName>{projectName}</projectName></SoftwareProject_V2>`).
   - Extract and return `projectVersionID` (Base VRC), `developmentEnvironment`, `developmentRepositoryAddress` (`<project>_dev`), `runtimeRepositoryAddress` (`<project>_rt`), `integrationWithPMC`, and all `<Task>` entries with `taskName`, `labelUUID`, `taskVersionID`, `taskStatus`, `typeOfTask`, and `assignedTo`.
2. **Create New Activity (`new-activity` / `CreateSoftwareTaskV2.xml`)**:
   - Invoke `SoftwareProject_V2.Change` (`<SoftwareProject_V2 actionType="unchanged"><projectName>...</projectName><Task actionType="create">...</Task></SoftwareProject_V2>`).
   - Capture the server-generated `<labelUUID>` from the response and automatically chain into `open-activity`.
3. **Open Existing Activity (`open-activity` / `ActivityUtil.open` + Optional Sync)**:
   - Execute `ShowSoftwareTaskV2` (`SoftwareProject_V2.Show` with `BdeFilter("Task.taskName" == taskName)`) to pull exact `labelUUID`, `taskVersionID`, and `projectVersionID` (Base VRC).
   - Execute `MaintainSoftwareTask` (`ChangeSoftwareTaskStatus.xml`: `SoftwareProject.Change` setting `<taskStatus>opened</taskStatus>` with `<taskVersionID>`).
   - Create local Eclipse project `<taskName> [<projectName>]` with `.project`, `.admin`, and the authentic binary `<workspace>/.metadata/.plugins/org.eclipse.core.resources/.projects/<taskName> [<projectName>]/.indexes/properties.index`.
   - Query `CMLabel.GetModifiedComponents` (`<CMLabel><timeStampSince>0</timeStampSince><type></type></CMLabel>`) on `<devEnv>_admin` and optionally download all active components in the activity via `CmGet` (`--sync-modified`, enabled by default for headless workflows).

### Decision 3: Authentic Build, SCM & Pre-Put Integrity Guardrails
1. Replace all XML payloads and response parsers in `ln_build_pipeline.py`, `ln_component_explorer.py`, and `ln_scm_engine.py` with the exact REA-verified templates (`Compile`, `ConvertToRuntime`, `CreateTables`, `VSC.executeVSC`, `CmGet`, `CmPut`, `CmCreate`, `CmCheckIn`, `CmCheckOut`, `CmUnCheckOut`, `StudioComponent.GetBrowseList`).
2. **Pre-Put Script Merge & Non-Empty Source Guardrail**:
   - Components reside on disk in **100% Native Eclipse Single-XML TDE Layout** (`{pkg}/{type}/{mod}/{name}.{ext}` for module-scoped types; `{pkg}/{type}/{name}.{ext}` for `domain`, `label`, `message`, `question`).
   - Before `Put` or `CheckIn`, if a developer or AI edited a standalone `.4gl`/`.dal` file, automatically merge it into `<DR_Module><Source><expression><![CDATA[...]]></expression></Source></DR_Module>` (for `.ses`/`.tbl`) or `<Source><expression><![CDATA[...]]></expression></Source>` (for `.lib`/`.fnc`/`.rpt`).
   - Verify that `<expression>` is non-empty (if the component previously contained code) before transmitting `Put` or `CheckIn`, preventing accidental blank-script overwrites.
3. **Strict End-Activity Hard-Block Preserved**:
   - `FglStudio.CloseTask` (`<End/>` / `<Deliver/>`) remains physically blocked in both Python and `LNStudioJcaBridge.java`.
   - `prepare-end-activity` uses the authentic `DR_Solution.ValidateDevelopmentActivity` template with `<CMLabel>` and `VSC.executeVSC`.

### Decision 4: Exact `.admin` (`m_path`) & Binary `properties.index` Synchronization + Live Eclipse Detection
1. Fix `AdminSyncHelper.java` so both the `HashMap` key and `AdministrationComponent.m_path` store the exact project-relative path without leading slash or project prefix (e.g., `"tx/table/cmg/txcmg011.tbl"`), and never register `.src`/`.4gl`/`.dal` files in `.admin`.
2. Implement exact state transitions matching `CMStudio.java`:
   - `Get`: `isCreated=false, isCheckedout=false, isEvercheckedIn=false, m_isDirty=false`
   - `DR_Create`: `isCreated=true, isCheckedout=true, isEvercheckedIn=false, m_isDirty=true, m_isVSCHappy=false`
   - `CheckOut`: `isCreated=false, isCheckedout=true, isEvercheckedIn=false, m_isDirty=false`
   - `Put`: `m_isDirty=false` (while `isCheckedout=true`)
   - `CheckIn`: `isCreated=false, isCheckedout=false, isEvercheckedIn=true, m_isDirty=false`
3. Implement a binary `PropertyBucket` reader/writer in Java/Python to read and write `<workspace>/.metadata/.plugins/org.eclipse.core.resources/.projects/<ProjectFolder>/.indexes/properties.index` using big-endian `DataOutputStream` (`version=1`, `QNAME=2`/`INDEX=1` qualifier table, and all `ProjectProperties` keys).
4. Detect active Eclipse instances via `<workspace>/.metadata/.lock` and trigger non-intrusive workspace refresh when Eclipse is open.

### Decision 5: 100% Eclipse LN Studio Feature Parity via `FglStudio`, `DR_Report`, and Consolidated MCP Tools
Add the missing Eclipse LN Studio capabilities discovered via REA into `ln_studio_skill` (both CLI subcommands and consolidated MCP tools):
1. **Ad-Hoc Server Compile (`compile-source` / `FglStudio.compileSource`)**: Compile 4GL code directly against server `bic6.2` in-memory without checking out or overwriting workspace files.
2. **Global Server Search (`search-server` / `FglStudio.Searchpattern`)**: Regex/pattern search across server packages.
3. **Call Hierarchy / Where-Used & Open Declaration (`call-hierarchy`, `open-declaration` / `fglstudio.GetCallHierarchyData`, `FglStudio.OpenDeclarationFunction`)**: Inspect callers, callees, and symbol declarations across the server repository.
4. **Revision History & Structural Diff (`revisions`, `diff-component` / `FglStudio.GetRevisions`, `StudioComponent.GetRevision`)**: List component revisions and diff Local Workarea vs. Activity VRC vs. Base VRC.
5. **Server-Side Report Wizard (`generate-report-server` / `DR_Report.Generate`)**: Invoke the ERP server's native report generator for a table/index, plus activity maintenance (`move-components` via `FglStudio.MoveComponent`, `clean-components` via `FglStudio.CleanComponents`).
6. **Consolidated MCP Tool Surface (`ln_studio_mcp.py`)**: Keep existing core tools intact while grouping new capabilities into consolidated multi-action tools (`ln_project_activity`, `ln_code_intelligence`, `ln_version_diff`, `ln_adhoc_compile`) so AI agents have 100% of Eclipse LN Studio's power with minimal token overhead.
