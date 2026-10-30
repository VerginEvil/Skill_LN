---
name: ln_studio_skill
description: "Infor LN Studio Assistant Skill for developing Infor LN applications, generating tables/sessions, synchronizing 4GL source code, and diagnosing compiler errors."
---

# Infor LN Studio Assistant Skill

The **Infor LN Studio Assistant Skill** empowers engineers and AI agents to model and verify applications on
**Infor ERP LN** using **Infor LN Studio 10.8 build 0640 (April 2026 tree)** — an Eclipse RCP,
activity-based development environment with SCM — with high speed, strict safety guardrails, and zero manual UI clicking.

---

## Skill Seam: Studio Engine vs Programmer's Guide

This skill operates under a strict division of responsibilities with [`erp-ln-progguide`](../erp-ln-progguide/SKILL.md):

| Domain | Responsible Skill | Key Responsibilities |
|---|---|---|
| **Studio Toolchain & Object Modeling** | `ln_studio_skill` (This Skill) | Pinned Studio 10.8 path resolution, explicit workspace/activity targeting, 12-extension `.admin` SCM cache synchronization, OS Read-Only guardrails, high-fidelity XML generation (`.tbl`, `.ses`, `.lib`, `.dmn`, `.lbl`, `.mnu`), 4-layer activity validation (`validate` & `--fix`), and offline 4GL syntax/completion inspection (`check-script`). |
| **4GL Coding Recipes & DAL 2 Patterns** | `erp-ln-progguide` | Business logic cookbooks, DAL 2 hook patterns, Extension point design, SQL optimization recipes, and Cloud tenant governor limits. |

---

## SCM & Workspace Operational Rules

1. **Explicit Workspace and Activity Resolution**:
   - Never assume default activities or hardcoded paths. Always specify target workspace via `--workspace <name>` or direct activity folder via `--activity-path <path>` (or pass explicit schema files).
   - Reference workspace: `C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST` (e.g., Activity `dev_natt_1107-1 [EXTce01107]`).
2. **Human-in-the-Loop SCM Guardrails**:
   - Checked-in components have the OS Read-Only attribute set.
   - The toolchain enforces `assert_file_writable` before any write or injection operation. If a file is Read-Only, operations abort with `ReadOnlyComponentError`, instructing the user to check out the component in the Eclipse workbench.
   - The toolchain **never** clears OS Read-Only flags automatically and **never** bypasses Eclipse JCA remote SCM authentication.
3. **12-Extension `.admin` SCM Synchronization**:
   - Manages all 12 LN Studio component extensions: `.tbl`, `.ses`, `.lib`, `.dmn`, `.lbl`, `.mnu`, `.rpt`, `.rptdsrc`, `.msg`, `.que`, `.add`, `.fun`.
   - Prevents accidental deletion of `.mnu` or `.rpt` files during SCM cache synchronization.
4. **Extension Modeler Boundary & Studio Read-Only "Get" Mode (ADR 0006)**:
   - Extension Modeler components (`tx*`, `ess`, `est`, `esb`, `esm`, `esr`) **cannot** be checked out or checked in via LN Studio SCM.
   - Studio SCM enforces: `Failure checking-out the component: Action on "..." is not allowed. Use session ttext1500m000 to process extensions.`
   - In Studio workspaces, extension files are strictly Read-Only / "Get" mode for viewing and debugging.
   - All extension authoring must be performed directly in local project repositories (`extensions/<type>/<component>_ext.4gl`) and deployed via LN UI (`ttext1500m000`).
   - The toolchain intercepts write/inject actions on extension components with `ReadOnlyComponentError`, and `validate` marks them as `[GET_ONLY_EXTENSION]`, suppressing false-positive SCM errors.
5. **Pre-Fetch Server Authentication & User Alert Guardrail (ADR 0010)**:
   - Before executing operations that fetch, download, inspect, check out, or synchronize remote code, scripts, or components from an Infor LN server or activity, the toolchain and AI assistant must verify the environment authentication state and alert the user with target object, server, and activity metadata.
   - Missing or expired tokens trigger automatic multi-channel SSO login (`ln_login` / `ln_auth_helper.py`), alerting the user in chat/terminal.

---

## Task-to-Entry-Point Table

| Task | CLI Command / Entry Point |
|---|---|
| Inspect workspaces and activities | `python <skill_dir>/tools/ln_component_builder.py workspace --list` / `--activities` |
| List configured cloud environments | `python <skill_dir>/tools/ln_component_builder.py environments [--workspace-root <path>]` |
| Auto SSO Login & Token Acquisition | `python <skill_dir>/tools/ln_component_builder.py login [--workspace <ws>] [--ionapi <path>] [--register-protocol]` |
| Connect / import .ionapi credentials | `python <skill_dir>/tools/ln_component_builder.py connect --ionapi <path> [--workspace <ws>] [--manual-auth]` |
| Browse remote projects & apps | `python <skill_dir>/tools/ln_component_builder.py project [--app <code>] [--project <p>]` |
| Browse/create remote activities | `python <skill_dir>/tools/ln_component_builder.py activity --project <p> [--create <act>] [--desc <d>]` |
| Clean remote activity lock | `python <skill_dir>/tools/ln_component_builder.py clean-activity --project <p> --task <act>` |
| Browse components across 12 types | `python <skill_dir>/tools/ln_component_builder.py explorer --type <t> [--filter <pattern>]` |
| Sync Read-Only references & DD cache | `python <skill_dir>/tools/ln_component_builder.py sync-reference --type <table\|domain\|session\|extension> --name <pattern>` |
| Get component (inspect or Read-Only) | `python <skill_dir>/tools/ln_component_builder.py get-component --type <t> --name <n> [--inspect] [--reference-only] [--activity <a>]` |
| Clone component into custom (incl. report) | `python <skill_dir>/tools/ln_component_builder.py clone-component --source-type <t> --source-name <sn> --target-name <tn> --activity <a>` |
| Check-out component from server | `python <skill_dir>/tools/ln_component_builder.py checkout-component --type <t> --name <n> --activity <a>` |
| Revert check-out (uncheckout) | `python <skill_dir>/tools/ln_component_builder.py uncheckout-component --type <t> --name <n> --activity <a>` |
| Check-in component to server | `python <skill_dir>/tools/ln_component_builder.py checkin-component --type <t> --name <n> --activity <a> [--comment <c>]` |
| Deploy-Test split pipeline | `python <skill_dir>/tools/ln_component_builder.py deploy-test --type <t> --name <n> --activity <a> [--mode compile-only\|schema-crdd] [--dry-run]` |
| Pre-commit verification (prepare) | `python <skill_dir>/tools/ln_component_builder.py prepare-end-activity --activity <a> [--project <p>]` |
| End activity (hard-blocked gate) | `python <skill_dir>/tools/ln_component_builder.py end-activity --task <act> --project <p>` |
| Register Stdio MCP Server | `python <skill_dir>/tools/ln_component_builder.py mcp-setup [--client claude\|cursor\|antigravity\|generic] [--apply]` |
| Validate authoring schema | `python <skill_dir>/tools/ln_schema_parser.py <schema.yaml>` |
| Generate Table, Label & Domain XML | `python <skill_dir>/tools/ln_component_builder.py table --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Domain XML independently | `python <skill_dir>/tools/ln_component_builder.py domain --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Session XML (Maintain, MMT) | `python <skill_dir>/tools/ln_component_builder.py session --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Library XML (Standard DLL) | `python <skill_dir>/tools/ln_component_builder.py library --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Menu XML & Labels | `python <skill_dir>/tools/ln_component_builder.py menu --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Message (.msg) XML | `python <skill_dir>/tools/ln_component_builder.py message --code <c> [--severity 1-3] [--text <t>] --activity <a>` |
| Generate Question (.qst/.que) XML | `python <skill_dir>/tools/ln_component_builder.py question --code <c> [--domain <d>] [--text <t>] --activity <a>` |
| Generate Include Function (.fnc/.fun) | `python <skill_dir>/tools/ln_component_builder.py function --code <c> [--script-file <f>] --activity <a>` |
| Generate Additional File (.add) | `python <skill_dir>/tools/ln_component_builder.py additional --code <c> [--content-file <f>] --activity <a>` |
| Generate Report (.rpt) XML | `python <skill_dir>/tools/ln_component_builder.py report --code <c> [--paper-width 80\|132] --activity <a>` |
| Generate All Components in one pass | `python <skill_dir>/tools/ln_component_builder.py component --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Scaffold Local Extension 4GL script | `python <skill_dir>/tools/ln_component_builder.py new-extension --type <table\|session> --target <comp> [--output <path>]` |
| Import Extension from Studio 'Get' cache | `python <skill_dir>/tools/ln_component_builder.py import-extension --source <xml_or_4gl> [--output <path>]` |
| Inspect & Export Extension Hooks | `python <skill_dir>/tools/ln_component_builder.py extension-hooks <ext_4gl> [--list] [--hook <name>] [--copy]` |
| Inject 4GL source into workspace XML | `python <skill_dir>/tools/ln_component_builder.py inject --source <f.dal> --target <f.tbl>` |
| Extract 4GL source from workspace XML | `python <skill_dir>/tools/ln_component_builder.py extract --source <f.tbl> --output <f.dal>` |
| Statically verify 4GL scripts (offline) | `python <skill_dir>/tools/ln_component_builder.py check-script <script_or_xml_file> [--strict] [--json]` |
| Run 4-Layer Activity Validation | `python <skill_dir>/tools/ln_component_builder.py validate [<activity_path>] [--strict] [--fix] [--json]` |
| Synchronize Activity `.admin` SCM Cache | `python <skill_dir>/tools/ln_component_builder.py sync-admin --activity "<act>"` |
| Read Eclipse problem markers (`.markers`) | `python <skill_dir>/tools/ln_component_builder.py diagnose --activity "<act>" [--errors-only]` |
| Trigger JCA remote compile or UI build | `python <skill_dir>/tools/ln_component_builder.py build --activity "<act>" [--ui-bridge]` |
| Full Autonomous Pipeline (Gen -> Sync -> Validate -> Build) | `python <skill_dir>/tools/ln_component_builder.py pipeline --spec <schema.yaml> [--output-dir <path>] [--auto-fix] [--skip-build]` |

---

## Extension Modeler Boundary & Agent "Guide-and-Paste" Protocol

In Infor ERP LN 10.8+, **Extension Modeler (`ttext1500m000`)** in LN UI (Web) is the authoritative environment for creating, editing, and compiling last-mile extensions.

### The System Constraint:
Attempting to check out or edit an extension component in Infor LN Studio fails with:
```text
Failure checking-out the component
Action on "txesswmd4300m0" is not allowed.
Use session ttext1500m000 to process extensions.
```
In Studio, extensions exist solely as Read-Only "Get" cache for viewing and debugging.

### Mandatory Agent Protocol (Guide-and-Paste):
When an AI agent or engineer is asked to author or modify an Infor LN Extension:
1. **Local Authoring**: Scaffold or edit the extension `.4gl` file inside the local project repository (under `extensions/<type>/<component>_ext.4gl`) with standard `#context_on "<hook_name>"` ... `#context_off` blocks.
2. **Offline Verification**: Run `check_4gl_script.py` to ensure 0 syntax errors, balanced blocks, valid hook signatures (`void` for command before/after hooks without return values), declarations include placement (`EXT001`), hook scope separation (`EXT002`), and full Cloud Governance compliance (no interactive dialogs or transaction controls in Table extensions; session extensions may coordinate transactions for secondary DAL tables).
3. **Interactive Step-by-Step Delivery**: In chat, output structured Markdown instructing the developer:
   - Target Session: `ttext1500m000` (Extension Modeler)
   - Component Selection: e.g. Table Extension for `whwmd400`
   - For each hook: Clean, copy-pasteable code block (stripped of `#context_on` wrappers)
4. **Studio Warning**: Explicitly warn the user **never** to check out or edit the component in LN Studio.

---

## Four-Layer Activity Validation (`validate` & `--fix`)

The `validate` subcommand executes a comprehensive 4-layer audit across an activity:

1. **Layer 1: SCM & Activity State**:
   - Audits all files across the 12 managed extensions against `.admin` SCM registration.
   - Flags untracked disk files or registered files missing on disk.
   - Checks Read-Only vs check-out consistency.
2. **Layer 2: XML Structure & Ecore Compliance**:
   - Verifies root tags (`<DR_Table>`, `<DR_Session>`, `<DR_Controller>`, `<DR_Module>`, `<DR_Domain>`, `<DR_Label>`, `<DR_Menu>`).
   - Validates `nativeDatatype` codes (`1`=Byte, `2`=Double, `3`=Long, `5`=Numeric, `6`=String, `7`=Enum, `9`=Date, `14`=UTC).
   - Validates Session `<FormGroup>` hierarchy trees (detects orphan parents, broken children, and cyclic pointer loops).
3. **Layer 3: Cross-Object Reference Integrity**:
   - Verifies that `<descriptionReference>` and `<fieldLabel>` tags resolve to local `.lbl` files (or standard LN packages).
   - Verifies that Session `<FormField>` and `<ControllerTableRelationship>` elements match actual Table columns.
   - Verifies that Table `<IndexColumn>` entries match declared `<Column>` elements.
   - Verifies Menu choice target components.
4. **Layer 4: Static 4GL Script & Symbol Verification**:
   - Inspects embedded `<expression>` blocks in `.tbl`, `.ses`, and `.lib` files.
   - Flags unrecognized or misspelled section headers (`before.program:`, `field.*:`, `choice.*:`, `main.table.io:`).
   - Verifies structural block balance (`select`/`endselect`, `if`/`endif`, `on case`/`endcase`, `for`/`endfor`, `while`/`endwhile`, `repeat`/`until`, `#context_on`/`#context_off`, `{`/`}`).
   - Cross-checks DAL property hooks against table columns and UI choices against session form commands.

### Safe `--fix` Mode:
Running `validate --fix` performs non-destructive automatic repairs:
- Auto-generates missing `.lbl` files for custom labels declared in tables, sessions, domains, or menus.
- Synchronizes `.admin` registration across all 12 managed extensions.
- Strictly preserves Read-Only files without modification.

---

## Native Stdio Model Context Protocol (MCP) Server (`ln_studio_mcp.py`)

The skill exposes a zero-dependency Stdio MCP server (`ln_studio_mcp.py`) implementing JSON-RPC 2.0. It exposes 17 structured tools for AI coding assistants (Claude Desktop, Cursor, Antigravity):

| MCP Tool | Capability | Guardrail / Policy |
|---|---|---|
| `ln_list_environments` | Lists customer workspaces, cloud configs, active dev/runtime endpoints | Read-only |
| `ln_login` | Multi-channel SSO login, Windows oob protocol capture & token acquisition | Production |
| `ln_connect` | Imports `.ionapi` credentials, syncs `cloudenv.prefs` & `connectivity.prefs` | Idempotent |
| `ln_explore_projects` | Lists remote Applications and Software Projects | Read-only Headless JCA |
| `ln_explore_activities` | Lists remote Activities under a Software Project | Read-only Headless JCA |
| `ln_explore_components` | Browses server components across all 12 types with wildcard filters | Read-only Headless JCA |
| `ln_create_activity` | Creates remote Activity and bootstraps local `.project`, `.admin`, `.settings` | Production |
| `ln_clean_activity` | Recovers stuck workarea locks on LN Server | Recovery |
| `ln_get_component` | Fetches component from server (inspects in-memory or downloads Read-Only) | Preserves Read-Only |
| `ln_checkout_component` | Checks out component into activity on server and downloads editable XML | **ADR 0006 Guardrail**: Rejects `tx*` extension check-outs |
| `ln_uncheckout_component`| Reverts component check-out on server and restores local Read-Only copy | Safe Revert |
| `ln_checkin_component` | Puts component to server and checks in with comment for LN UI testing | Safe Check-In |
| `ln_create_component` | Generates any of the 12 LN Studio components and registers in `.admin` | 12 Components |
| `ln_clone_component` | Clones standard or custom component into renamed custom activity component | Prefix Renaming |
| `ln_validate_activity` | Runs 4-layer validation across activity (.admin, XML, cross-ref, 4GL) | Read-only Audit |
| `ln_deploy_test` | Composite pipeline: Put -> Compile -> CRDD -> CreateTables -> VSC -> CheckIn | Cloud Testing |
| `ln_prepare_end_activity`| Pre-commit verification before handing delivery off to human review | **ADR 0007 Human Gate** |
| `ln_end_activity` | **Hard-blocked pre-commit delivery gate**: Raises `PreCommitBoundaryError` | Human LN Studio Hand-off |

### Client Registration (`mcp-setup`):
```bash
# Register in Claude Desktop configuration
python <skill_dir>/tools/ln_component_builder.py mcp-setup --client claude --apply

# Register in Cursor configuration (.cursor/mcp.json)
python <skill_dir>/tools/ln_component_builder.py mcp-setup --client cursor --apply

# Preview generic JSON configuration
python <skill_dir>/tools/ln_component_builder.py mcp-setup --client generic --dry-run
```

---

## Self-Contained OAuth2 Login & 'oob://' Protocol Resolution (ADR 0009)

Infor CloudSuite PingFederate OAuth2 for LN Studio Desktop Clients (`dt=11`) enforces two strict constraints:
1. **Password Grant Blocked**: Direct `grant_type=password` is disallowed by Infor SSO policy (`Unsupported grant type password. Expected one of authorization_code`).
2. **Custom 'oob://' URI Scheme**: Authorization codes are redirected to `oob://localhost/lnstudio?code=<CODE>&state=<UUID>`. Standard web browsers (Chrome, Edge) do not recognize `oob://`, aborting with `net::ERR_ABORTED` or `ERR_UNKNOWN_URL_SCHEME` and appearing as a broken or blank page.
3. **Federation Hub Sensitivity**: Requesting unconfigured scopes (e.g. `scope=openid`) causes Infor OS Federation Hub to abort with *"InforOS Federation Hub service has encountered an error"*.

### Zero-Click Multi-Channel Solution (`ln_auth_helper.py`):
Running `python <skill_dir>/tools/ln_component_builder.py login --workspace <ws>` solves this end-to-end:
* **Channel 1 (Windows Registry Protocol Handler)**: Auto-registers `HKCU\Software\Classes\oob` to launch `capture_oob.py`. When the user clicks "Allow" in their browser, Chrome/Edge forwards the redirect directly to the helper, which extracts the code, closes the loop, and displays a clean confirmation tab.
* **Channel 2 (Real-Time Clipboard Auto-Detection)**: A 64-bit safe `ctypes.windll.user32` thread monitors clipboard changes. If the user copies the address bar URL or code, it is instantly captured within 0.4s without pressing Enter.
* **Channel 3 (Interactive Fallback)**: Terminal prompt accepts pasted URLs or raw codes.
* **PingFederate Fix**: Automatically generates a cryptographically secure UUID `state` parameter and suppresses empty/unconfigured scopes, eliminating Federation Hub errors.

---

## Pre-Fetch Server Authentication & User Alert Guardrail (ADR 0010)

Before executing any remote operation to pull code, scripts, or object definitions (e.g. `get-component`, `sync-reference`, `checkout-component`, `extract`, `explorer`, `ln_get_component`):

### 1. Mandatory Pre-Fetch User Alert
The toolchain emits an explicit user-facing notification banner in stdout and structured MCP responses:
```text
[PRE-FETCH ALERT] Accessing Infor LN Server / Activity:
  Target:     <component_type> '<object_name>' | Activity: <activity_name>
  Workspace:  <workspace_name> (CloudEnv: <cloud_env>)
```

### 2. Pre-Flight Authentication Verification & Auto-Authenticate
- `OAuth2TokenManager.check_token_status` inspects cached token validity (with a 300s safety buffer).
- If near expiry, automatically performs a silent refresh using `refresh_token`.
- If missing or un-refreshable, automatically initiates the multi-channel SSO login flow (`execute_login`), alerting the user to authorize via browser, and capturing the authorization code via the registered Windows `oob://` protocol handler or clipboard detection.
- Connects and verifies JCA server/activity reachability before retrieving components.

---

## Toolchain & Reference Layout

```
tools/                          Self-contained automation toolchain:
  ln_component_builder.py         Master CLI orchestrator (37 subcommands)
  ln_studio_mcp.py                Native JSON-RPC 2.0 Stdio MCP Server (17 tools)
  ln_env_manager.py               .ionapi parser, token refresh & Eclipse prefs synchronizer
  ln_server_client.py             JCA WebClient transport & BDE call executor
  ln_project_activity_manager.py  Software Project & Activity explorer + local bootstrapper
  ln_component_explorer.py        12-type component explorer, inspector, and cloner
  ln_scm_engine.py                Pre-commit SCM engine (Check-Out, Uncheckout, Put, Check-In)
  ln_build_pipeline.py            Remote compile, CRDD, CreateTables, VSC & deploy-test
  ln_schema_parser.py             Declarative authoring schema validator (multi-table & domains)
  generate_ln_table.py            Table, Label & Domain XML generator (Ecore facets & conventions)
  generate_ln_domain.py           Standalone & Spec-based Domain generator (.dmn & enums)
  generate_ln_session.py          Multi-archetype Session generator (Maintain, MMT, Satellites)
  generate_ln_library.py          Library generator (Standard DLL; redirects extensions to new-extension)
  generate_ln_menu.py             Menu generator (<DR_Menu> XML & .lbl)
  generate_ln_message.py          Message generator (<DR_Message> XML & .msg)
  generate_ln_question.py         Question generator (<DR_Question> XML & .qst/.que)
  generate_ln_function.py         Include Function generator (<DR_Module> XML & .fnc/.fun)
  generate_ln_additional.py       Additional File generator (<DR_AdditionalFile> XML & .add)
  generate_ln_report.py           Report generator (<DR_Report> XML & .rpt/.rptdsrc)
  ln_extension_manager.py         Extension scaffolding, 'Get' import, and hook clipboard extractor
  inject_ln_script.py             Bidirectional 4GL synchronizer with Read-Only guardrails
  admin_sync.py                   12-extension SCM .admin cache synchronizer (+ Java helper)
  scm_guardrails.py               OS Read-Only SCM protection & extension interception module
  check_4gl_script.py             Static 4GL syntax, completion, block balance & extension hook inspector
  validate_ln_activity.py         Four-layer activity validator & safe --fix engine ([GET_ONLY_EXTENSION])
  extract_studio_dictionaries.py  LN Studio 10.8 reflection extractor for keywords, sections, hooks
  ln_error_reader.py              Binary .markers problem diagnostics reader
  ln_studio_bridge.py             Windows action bridge (F5 refresh / Ctrl+B build)
  ln_workspace_manager.py         Pinned Studio & workspace environment resolver
  tests/                          Comprehensive unit test suite (154+ tests across 15 test suites)
templates/
  table_extension_template.4gl    Starter template for Table Extensions (#context_on hooks)
  session_extension_template.4gl  Starter template for Session Extensions (command hooks)
scripts/search.py               Full-text search across documentation guides
references/
  COMPONENT_XML_SCHEMA.md         Complete Ecore XML schema guide for all 12 component types
  STUDIO_SYNTAX_COMPLETION.md     Extracted Studio 10.8 Keywords, Sections, DAL Hooks & Templates
  studio_syntax_completion.json   Machine-readable syntax and completion dictionary catalog
  DAL2_HOOKS_GUIDE.md             DAL 2 Object & Property hook reference
  UI_SCRIPT_GUIDE.md              UI Session 4GL script reference
  STUDIO_INDEX.md                 Master index of the 12 ingested Studio guide chapters
```

---

## Authoring Schema Example (Multi-Component)

```yaml
version_id: B61O_a_ext
application: EXTce01107

domains:
  - name: txcmg.remk
    package: tx
    datatype: string
    length: 100
    description: Billing Remarks

tables:
  - code: txcmg011
    description: Billing Batch Header
    package: tx
    module: cmg
    fields:
      - name: btno
        domain: tcmcs.long
        type: long
        mandatory: true
      - name: remk
        domain: txcmg.remk
        type: string
        length: 100
      - name: stdd
        domain: tcyesno
        type: enum
    indices:
      - id: 1
        columns: [btno]
        primary_key: true

sessions:
  - code: txcmg0110m100
    description: Billing Batch MMT Controller
    type: mmt_controller
    table: txcmg011
    satellites: [txcmg0510m000, txcmg0512m000]
    form_commands:
      - { name: exec.user.0, function: generate.billing, label_code: txcmg0110m100.cmd1, description: Generate Billing }

libraries:
  - code: txibddllitem01
    module: ibd
    type: dll
    description: Item General DLL

menus:
  - code: txgld0000m001
    module: gld
    description: Enhancements Menu
    choices:
      - { position: 10, type: session, target: txcmg0110m100, description: Billing Batch }
```

---

## Related Best Practices & References (`erp-ln-progguide`)

| Task | Start at |
|---|---|
| Extension hook lifecycles, CDF recipes, cloud limits | [01_extension_hooks_cookbook.md](../erp-ln-progguide/references/best_practices/01_extension_hooks_cookbook.md) |
| DAL 1 vs DAL 2, SoC rules, business methods | [02_dal_architecture_and_business_logic.md](../erp-ln-progguide/references/best_practices/02_dal_architecture_and_business_logic.md) |
| Baan SQL optimization & transaction boundaries | [03_sql_query_optimization_and_transactions.md](../erp-ln-progguide/references/best_practices/03_sql_query_optimization_and_transactions.md) |
| Domain design, tables & `crdd` reconfiguration | [04_data_model_and_domain_design.md](../erp-ln-progguide/references/best_practices/04_data_model_and_domain_design.md) |
| Session types 1-4 & MMT Controller/Satellite | [05_session_and_mmt_patterns.md](../erp-ln-progguide/references/best_practices/05_session_and_mmt_patterns.md) |
