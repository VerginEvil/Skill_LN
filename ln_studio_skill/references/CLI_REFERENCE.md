# Infor LN Studio CLI Reference (`skill-ln`)

Comprehensive catalog of subcommands provided by the native Rust `skill-ln` binary (`skill-ln.exe`), organized by development lifecycle stage, along with common high-frequency command recipes.

---

## 1. Subcommands by Lifecycle Stage

### 1.1 Environment & Authentication
| Command | Options / Arguments | Description |
|---|---|---|
| `environments` | `[--workspace-root <path>]` | List configured cloud environments and connection endpoints |
| `login` | `[--workspace <ws>] [--ionapi <path>] [--status\|--check-only] [--json] [--register-protocol]` | Multi-channel OAuth2 SSO login, status check, and protocol registration |
| `connect` | `--ionapi <path> [--workspace <ws>] [--manual-auth]` | Import `.ionapi` credentials and synchronize Eclipse preferences |
| `daemon` | `[--status\|--stop\|--restart\|--token <t>]` | Manage persistent background JCA JVM daemon |

### 1.2 Project & Activity Management
| Command | Options / Arguments | Description |
|---|---|---|
| `workspace` | `--list \| --activities` | List workspaces and discover activity folders |
| `project` | `[--app <code>] [--project <p>]` | Browse remote applications and software projects |
| `project-info`| `--project <p>` | Inspect software project metadata and VRC configuration |
| `new-activity` | `--project <p> --task <t> [--desc <d>] [--user <u>]` | Create new activity on LN server and bootstrap local workspace |
| `open-activity`| `--project <p> --task <t> [--no-sync-modified]` | Open and bootstrap an existing activity locally |
| `clean-activity`| `--project <p> --task <act>` | Clean stuck workarea lock on LN server |
| `move-components`| `--source-activity <a> --target-task <ta> --components <t:n,...>` | Move components between development activities |
| `clean-components`| `--activity <a> --components <t:n,...>` | Release locks and remove components from activity |

### 1.3 Explorer, Remote Fetch & SCM
| Command | Options / Arguments | Description |
|---|---|---|
| `explorer` | `--type <t> [--filter <pattern>]` | Browse components across all 12 types with wildcard filters |
| `sync-reference`| `--type <table\|domain\|session\|extension> --name <pattern>` | Sync read-only reference components into `.reference/` and update DD cache |
| `get-component`| `--type <t> --name <n> [--inspect] [--export-script <path>] [--activity <a>]` | Fetch component from server (inspect, read-only download, or script export) |
| `clone-component`| `--source-type <t> --source-name <sn> --target-name <tn> --activity <a>` | Clone standard or custom component into renamed custom activity component |
| `checkout-component`| `--type <t> --name <n> --activity <a>` | Check out component on server and download editable Single-XML (rejects `tx*`) |
| `uncheckout-component`| `--type <t> --name <n> --activity <a>` | Revert component check-out on server and restore read-only copy |
| `checkin-component`| `--type <t> --name <n> --activity <a> [--comment <c>]` | Put component to server and check in for LN UI Cloud testing |

### 1.4 Code Intelligence, Revision History & Diff
| Command | Options / Arguments | Description |
|---|---|---|
| `compile-source`| `--package <pkg> [--source-file <f>\|--code <code>] [--flags <f>]` | Ad-hoc server compilation via `FglStudio` without committing |
| `search-server` | `--pattern <regex> [--package <pkg>]` | Global server regex search across packages via `FglStudio` |
| `call-hierarchy`| `--source-file <f> --function <fn> [--mode callers\|callees]` | Call hierarchy and where-used analysis |
| `open-declaration`| `--comp <c> --type <t> --function <fn>` | Jump to symbol declaration on server |
| `related-components`| `--package <pkg> [--source-file <f>\|--code <code>]` | Discover script-referenced components (tables, libraries, domains) |
| `revisions` | `--type <t> --name <n> [--version <v>]` | Query server revision history and commit logs |
| `diff-component`| `--type <t> --name <n> --activity <a> [--revision <r>]` | Script and structural XML diff against server revisions |
| `generate-report-server`| `--code <r> --table <tbl> [--paper-width 80\|132] [--report-type 1\|2\|3]` | Generate report structure on server via `DR_Report` wizard |

### 1.5 Component Generation & Pipeline
| Command | Options / Arguments | Description |
|---|---|---|
| `table` | `--spec <schema.yaml> [--output-dir <p>] [--dry-run]` | Generate Table, Label & Domain XML from schema |
| `domain` | `--spec <schema.yaml> [--output-dir <p>] [--dry-run]` | Generate Domain XML independently |
| `session` | `--spec <schema.yaml> [--output-dir <p>] [--dry-run]` | Generate Session XML (Maintain, MMT Controller, Satellite) |
| `library` | `--spec <schema.yaml> [--output-dir <p>] [--dry-run]` | Generate Library XML (Standard DLL) |
| `menu` | `--spec <schema.yaml> [--output-dir <p>] [--dry-run]` | Generate Menu XML and Labels |
| `message` | `--code <c> [--severity 1-3] [--text <t>] --activity <a>` | Generate Message (`.msg`) XML |
| `question` | `--code <c> [--domain <d>] [--text <t>] --activity <a>` | Generate Question (`.qst`/`.que`) XML |
| `function` | `--code <c> [--script-file <f>] --activity <a>` | Generate Include Function (`.fnc`/`.fun`) XML |
| `additional` | `--code <c> [--content-file <f>] --activity <a>` | Generate Additional File (`.add`) XML |
| `report` | `--code <c> [--paper-width 80\|132] --activity <a>` | Generate Report (`.rpt`) XML |
| `component` | `--spec <schema.yaml> [--output-dir <p>] [--dry-run]` | Generate all components declared in schema in one pass |
| `pipeline` | `--spec <schema.yaml> [--output-dir <p>] [--auto-fix] [--skip-build]` | Full autonomous pipeline (Gen -> Sync -> Validate -> Build) |

### 1.6 Extension Modeler Helpers (Guide-and-Paste)
| Command | Options / Arguments | Description |
|---|---|---|
| `new-extension` | `--type <table\|session> --target <comp> [--output <path>]` | Scaffold local extension `.4gl` script with `#context_on` blocks |
| `import-extension`| `--source <xml_or_4gl> [--output <path>]` | Import extension script from Studio 'Get' cache into local file |
| `extension-hooks` | `<ext_4gl> [--list] [--hook <name>] [--copy]` | Inspect and extract clean hook blocks for pasting into LN UI |

### 1.7 Validation, Diagnostics, Build & Pre-Commit SCM
| Command | Options / Arguments | Description |
|---|---|---|
| `check-script` | `<script_or_xml_file> [--strict] [--json]` | Offline static 4GL syntax, block balance, and hook check |
| `validate` | `[<activity_path>] [--strict] [--fix] [--json]` | 4-layer activity validation (`.admin`, XML, cross-ref, 4GL) |
| `sync-admin` | `--activity "<act>"` | Synchronize 12-extension SCM `.admin` registration cache |
| `diagnose` | `--activity "<act>" [--errors-only]` | Decode Eclipse binary problem markers (`.markers`) |
| `build` | `--activity "<act>" [--ui-bridge]` | Trigger JCA remote compile or workbench UI build |
| `deploy-test` | `--type <t> --name <n> --activity <a> [--mode compile-only\|schema-crdd]` | Push local component changes to server Activity VRC for testing |
| `prepare-end-activity`| `--activity <a> [--project <p>]` | Pre-commit verification gate before human handoff |
| `end-activity` | `--task <act> --project <p>` | Hard-blocked pre-commit delivery gate (raises error) |
| `inject` | `--source <f.dal> --target <f.tbl>` | Inject 4GL script into Single-XML `<expression>` |
| `extract` | `--source <f.tbl> --output <f.dal>` | Extract 4GL script from Single-XML `<expression>` |
| `mcp-stdio` | _(no arguments)_ | Run native JSON-RPC 2.0 Stdio MCP server (25 tools) |
| `mcp-setup` | `[--client claude\|cursor\|antigravity\|generic] [--apply]` | Register Stdio MCP Server (`skill-ln mcp-stdio`) in client configuration |
| `verify-studio-build` | `--studio-home <path>` | Verify Studio Build 0640 plugin JARs vs pure-Rust crate coverage |
| `audit-4gl` | `<file> [--mode dal2\|uedll\|general] [--cloud] [--json]` | Run offline 4GL/DAL/Extension static code audit |
| `fn-search` | `<term> [--cloud-only]` | Search bshell API function index |
| `doc-search` | `<query> [--limit N]` | Full-text search across ERP LN documentation |

---

## 2. High-Frequency Practical Recipes

### 2.1 Check Token Status & Trigger Silent Refresh
```bash
# Non-interactive check with silent refresh (no browser opened)
skill-ln login --workspace SCS_TST --status

# Output status as JSON
skill-ln login --workspace SCS_TST --status --json
```

### 2.2 Fetch Extension Component & Export 4GL Script
```bash
# By session code (maps to txesssli2620m0.lib and exports scripts/cisli2620m000.cln)
skill-ln get-component --type extension --name cisli2620m000 --export-script ./scripts

# By table code (maps to txestcisli220.lib and exports scripts/cisli220.cln)
skill-ln get-component --type extension --name cisli220 --export-script ./scripts
```

### 2.3 Persistent JCA Daemon Control
```bash
skill-ln daemon --status
skill-ln daemon --restart
skill-ln daemon --stop
```

### 2.4 Activity Validation with Non-Destructive Auto-Fix
```bash
# Validates .admin, XML schema, label references, and 4GL expressions; auto-generates missing labels
skill-ln validate "C:\workspace\SCS_TST\dev_act [EXT01]" --fix
```
