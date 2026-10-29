# ADR 0007: Headless JCA Connectivity, Remote Explorers, Automated SCM (Pre-Commit Boundary), 12-Component Generation & Stdio MCP Server

- **Status**: Accepted
- **Date**: 2026-10-26
- **Target Skill**: `ln_studio_skill`
- **Specification**: [`docs/SPEC_HEADLESS_JCA_CONNECTIVITY_SCM_AND_MCP.md`](../SPEC_HEADLESS_JCA_CONNECTIVITY_SCM_AND_MCP.md)
- **Implementation Plan**: [`docs/PLAN_HEADLESS_JCA_CONNECTIVITY_SCM_AND_MCP.md`](../PLAN_HEADLESS_JCA_CONNECTIVITY_SCM_AND_MCP.md)
- **Prior ADRs**:
  - [`docs/adr/0002-ln-studio-skill-self-contained-toolchain.md`](0002-ln-studio-skill-self-contained-toolchain.md)
  - [`docs/adr/0003-ln-studio-object-modeling-and-static-verification.md`](0003-ln-studio-object-modeling-and-static-verification.md) *(Partially superseded regarding manual Eclipse check-out requirement and Win32 keystroke build default)*
  - [`docs/adr/0006-ln-studio-extension-readonly-and-lnui-workflow.md`](0006-ln-studio-extension-readonly-and-lnui-workflow.md) *(Preserved: Extension Modeler `tx*` components remain Get-Only in Studio)*

---

## 1. Context & Problem Statement

In prior iterations of `ln_studio_skill` (ADR 0002 and ADR 0003), the toolchain operated strictly offline on local workspace directories and relied on:
1. Manual developer interaction inside the Eclipse LN Studio UI to authenticate via `.ionapi`, browse remote servers, create activities, and check out/check in components.
2. Win32 window focus and synthetic keystrokes (`F5` / `Ctrl+B` via `ln_studio_bridge.py`) to trigger compilation inside an open Eclipse workbench, followed by binary `.markers` parsing.
3. Component XML generation for only 6 of the 12 LN Studio component types (`.tbl`, `.ses`, `.dmn`, `.lib`, `.mnu`, `.lbl`), leaving out Reports (`.rpt`/`.rptdsrc`), Messages (`.msg`), Questions (`.qst`/`.que`), Include Functions (`.fnc`/`.fun`), and Additional Files (`.add`).

### Reverse-Engineering Findings (`InforLNStudio_10_8_0_build0640-x86_64`)
Inspection of the installed Infor LN Studio 10.8 (build 0640) plugins established that:
- `com.infor.erpln.jca.connectivity_10.8.12.v0-20250703-1423/lib/JCAAdapter4ERPln-10.8.10.jar` is a **pure Java JCA 1.6 connector with zero Eclipse UI or SWT dependencies**.
- It communicates directly over HTTPS (`ActivationType = http_oauth2`, `User-Agent: JCAWebClient (LNStudio)`) with `<GatewayURL>/<TenantID>/LN/webservice` using OAuth2 Bearer tokens acquired from Infor ION API (`.ionapi`) profiles.
- Every LN Studio Explorer (Software Project Explorer, Activity Explorer, Component Explorer), every SCM operation (`Get`, `CheckOut`, `Put`, `DR_Create`, `CheckIn`, `UndoCheckOut`), and every Server Build operation (`Compile`, `ConvertToRuntime`, `CreateTables`, `executeVSC`) is executed via XML BDE calls over `JcaBdeManager.doBdeCall(...)`.

---

## 2. Settled Architectural Decisions (Rounds 1, 2, and 3)

### Decision 1: Dual-Interface Architecture (CLI + Stdio MCP Server)
`ln_studio_skill` will expose all capabilities through two synchronized interfaces sharing the same core Python + Headless Java engine:
1. **CLI Subcommands (`ln_component_builder.py`)**: Fast batch and pipeline execution for developers and scripts (`connect`, `project`, `activity`, `explorer`, `get`, `checkout`, `uncheckout`, `checkin`, `deploy-test`, `clone-component`, `prepare-end-activity`, `mcp-setup`).
2. **Stdio MCP Server (`ln_studio_mcp.py`)**: Native Model Context Protocol server registering structured tools (`ln_connect`, `ln_list_environments`, `ln_explore_projects`, `ln_explore_activities`, `ln_create_activity`, `ln_explore_components`, `ln_get_component`, `ln_checkout_component`, `ln_uncheckout_component`, `ln_create_component`, `ln_clone_component`, `ln_deploy_test`, `ln_prepare_end_activity`) for AI coding agents.

### Decision 2: Direct Headless Java JCA Bridge & Session Daemon
Instead of launching the heavy Eclipse OSGi/RCP workbench, server operations run through a standalone Java bridge (`LNStudioJcaBridge.java`) executed by Studio's bundled JDK (`D:\LN Studio\jdk-11.0.16.1\bin\java.exe`) with `JCAAdapter4ERPln-10.8.10.jar`, its `lib/*` dependencies, and `lnstudio_commoncore.jar` on the classpath. An optional background session daemon (`conid` + session cookies + shared `<Project>_dev`/`<Project>_rt` connections) avoids re-authenticating on every CLI/MCP call.

### Decision 3: `.ionapi` OAuth2 Management & 100% Eclipse Workspace Metadata Sync
1. **Environment & `.ionapi` Import**: Parses customer `.ionapi` files (`ti`, `cn`, `dt`, `ci`, `cs`, `iu`, `pu`, `oa`, `ot`, `or`, `saak`, `sask`) and synchronizes both:
   - Global Studio Cloud Environments (`configuration/.settings/com.infor.erpln.jca.connectivity.cloudenv.prefs`)
   - Per-Workspace JCA Connection Points (`<Workspace>/.metadata/.plugins/org.eclipse.core.runtime/.settings/com.infor.erpln.jca.connectivity.prefs` for `ProjectServer`, `<Project>_dev`, `<Project>_rt`)
2. **Hybrid OAuth2 Token Acquisition**:
   - **Desktop `.ionapi` (`dt="11"`)**: First-time login opens a lightweight browser/redirect catcher for `oob://localhost/lnstudio?code=...`, exchanges the authorization code at `<pu>token.oauth2`, and caches `access_token` + `refresh_token` in a gitignored local store (`.ln_studio_tokens.json`). Subsequent calls silently auto-refresh via `grant_type=refresh_token`.
   - **Service Account `.ionapi` (`saak`/`sask`)**: Acquires tokens 100% headlessly via `grant_type=password`.

### Decision 4: Revised SCM Guardrail Boundary (Automate Up to Check-In; Hard-Block Commit / End Activity)
Superseding ADR 0003's restriction on automated Check-Out/Check-In:
1. **Permitted & Automated via JCA**:
   - **Get (`DR_*.Get`)**: Pull any standard (`tc`, `td`, `wh`, `tf`) or custom (`tx`) component from the server in Read-Only mode (either saved into the Activity folder with `.admin` sync, or returned in `--inspect` memory/scratch mode without cluttering the activity).
   - **Create / Open Activity (`SoftwareProject_V2.Change` / `Show`)**: Create or open activities on the server and initialize `<taskId> [<projectName>]` locally with `.project`, `.admin`, and Eclipse `properties.index`.
   - **Check-Out (`DR_*.CheckOut`) & Undo Check-Out (`DR_*.UndoCheckOut`)**: Lock components into the active Activity on the server, write the XML locally, clear OS Read-Only, and update `.admin`.
   - **Put / Create / Check-In (`DR_*.Put`, `DR_Create`, `CheckIn`)**: Upload modified or newly created components to the Activity VRC (`ext`) on the server with check-in comments so developers can immediately test in LN UI Cloud.
2. **Strictly Hard-Blocked (Human-in-the-Loop Final Gate)**:
   - **`CloseTask (<End/> / <Deliver/>)` and `FinalizeActivity` (Commit / End Activity) are strictly prohibited and never executed by CLI or MCP.**
   - Instead, `prepare-end-activity` runs pre-flight checks (`DR_Solution.ValidateDevelopmentActivity` + `ExecuteVSC`), verifies 100% Eclipse workspace metadata sync, and outputs a structured commit summary for the developer to review before manually ending/committing the Activity in LN Studio.
   - **ADR 0006 Preserved**: Extension Modeler components (`tx*` in `ess`, `est`, `esr`, `esb`, `esm`) remain strictly **Get-Only** in Studio and cannot be checked out.

### Decision 5: End-to-End `deploy-test` Pipeline & Headless Default for `build`
Because saving/checking in on an Activity VRC (`ext`) is the standard mechanism for testing customizations on LN UI Cloud:
- Introduce a composite `deploy-test` operation (and make Headless JCA Build the default for `build` and `pipeline`, relegating `ln_studio_bridge.py` Win32 keystrokes to `--ui-bridge` fallback).
- Execution sequence:
  1. Inject 4GL script into component XML (if standalone `.dal`/`.cln`/`.4gl` provided).
  2. `DR_*.DR_Create` (if new) or `DR_*.Put` (if existing checked-out) to upload XML to the server Activity workarea.
  3. `DR_*.Compile` — parses `<CompileResponseError>` and `<CompileResponseWarning>` directly from XML response with exact line/column numbers.
  4. `DR_*.ConvertToRuntime` (`crdd`) and `DR_Table.CreateTables` when Table/Domain/Session/Menu definitions change.
  5. `DR_*.executeVSC` — runs Verification of Source Code.
  6. `DR_*.CheckIn` (with comment) and updates local `.admin` + Read-Only state as requested.

### Decision 6: Full 12-Component Generation (`Create New Component`) & Server Cloning (`clone-component`)
1. Expand generators and `ln_schema_parser.py` to support all 12 LN Studio component types:
   - Existing 6: Table (`.tbl`), Domain (`.dmn`), Label (`.lbl`), Session (`.ses`), Library (`.lib`), Menu (`.mnu`).
   - New 6: Report (`.rpt` & `.rptdsrc` via `<DR_Report>`), Message (`.msg` via `<DR_Message>`), Question (`.qst` canonical / `.que` alias via `<DR_Question>`), Include Function (`.fnc` canonical / `.fun` alias via `<DR_Module><type>function</type>`), and Additional File (`.add` via `<DR_AdditionalFile>`).
2. Add `clone-component` to fetch an existing standard or custom component from the server via `Get`, rename its Package/Module/Component code and label references (e.g., into `tx...`), and register it into the active Activity via `DR_Create`.

---

## 3. Architecture Comparison

| Capability | Prior Architecture (ADR 0002 / 0003) | New Architecture (ADR 0007) |
|---|---|---|
| **Server Connectivity** | Offline only (manual setup in Eclipse) | Headless JCA 1.6 HTTP/OAuth2 Bridge + `.ionapi` Import & Auto-Refresh |
| **Project / Activity / Component Explorers** | None (local filesystem inspection only) | Live Server BDE Explorers (`SoftwareProject_V2`, `Group`, `StudioComponent`) |
| **SCM Get / Check-Out / Check-In** | Blocked (required manual clicking in Eclipse) | Automated via JCA (`Get`, `CheckOut`, `Put`, `DR_Create`, `CheckIn`, `UndoCheckOut`) |
| **Commit / End Activity** | Manual in Eclipse | **Hard-Blocked** in CLI/MCP; `prepare-end-activity` validates & hands off to human |
| **Compilation & CRDD** | Win32 keystrokes (`F5`/`Ctrl+B`) + `.markers` binary | Direct Server `Compile` XML response + `ConvertToRuntime` + `CreateTables` + `VSC` |
| **Component Generators** | 6 of 12 types (`.tbl`, `.ses`, `.dmn`, `.lib`, `.mnu`, `.lbl`) | All 12 types (adds `.rpt`/`.rptdsrc`, `.msg`, `.qst`/`.que`, `.fnc`/`.fun`, `.add`) + Server `clone-component` |
| **Agent Integration** | CLI calls only | Dual Interface: CLI (`ln_component_builder.py`) + Native Stdio MCP Server (`ln_studio_mcp.py`) |
