[⬅️ Back to Skill_LN Main Repository](../README.md)

---

# Infor LN Studio Automation Toolset & Assistant Skill (`ln_studio_skill`)

[![Infor LN](https://img.shields.io/badge/ERP-Infor%20LN%2010.8%20Build%200640-0052CC?style=for-the-badge&logo=infor&logoColor=white)](https://www.infor.com)
[![MCP Server](https://img.shields.io/badge/MCP%20Server-Native%20Stdio%20(16%20Tools)-FF6F00?style=for-the-badge&logo=anthropic&logoColor=white)](#native-stdio-mcp-server-ln_studio_mcppy)
[![Headless JCA](https://img.shields.io/badge/Headless%20Engine-JCA%201.6%20Bridge%20(JDK%2011)-4CAF50?style=for-the-badge&logo=openjdk&logoColor=white)](#headless-jca-architecture)
[![Components](https://img.shields.io/badge/Generators-12%2F12%20Studio%20Types-9C27B0?style=for-the-badge)](#12-component-archetype-matrix)
[![SCM Guardrails](https://img.shields.io/badge/SCM%20Guardrails-ADR%200006%20%26%200007-D32F2F?style=for-the-badge)](#strict-human-in-the-loop-commit-gate-adr-0007)
[![Tests](https://img.shields.io/badge/Tests-283%20Passed-brightgreen?style=for-the-badge)](#automated-test-suite)

> **Self-contained, production-grade intelligence, headless JCA connectivity, declarative 12-component modeling, pre-commit SCM engine, and native Model Context Protocol (MCP) server for Infor LN Studio 10.8 (Build 0640, April 2026 tree, Eclipse RCP).**

---

## Table of Contents

- [Overview & Modern Architecture](#overview--modern-architecture)
- [Headless JCA Architecture](#headless-jca-architecture)
- [AI Agent Configuration Matrix (Claude Desktop, Cursor, Antigravity)](#ai-agent-configuration-matrix)
- [5-Stage Lifecycle Matrix (16 MCP Tools & 37 CLI Subcommands)](#5-stage-lifecycle-matrix)
- [12-Component Archetype Matrix & Declarative Modeling](#12-component-archetype-matrix)
- [Enterprise Safety Guardrails & Callouts](#enterprise-safety-guardrails)
  - [Extension Modeler Cloud UI Boundary (ADR 0006)](#extension-modeler-boundary)
  - [Strict Human-in-the-Loop Commit Gate (ADR 0007)](#human-commit-gate)
- [Master CLI Reference (Categorized)](#master-cli-reference)
- [Automated Test Suite](#automated-test-suite)
- [Directory Layout](#directory-layout)

---

## Overview & Modern Architecture

Historically, developing applications and extensions in Infor LN Studio required repetitive manual clicks across heavy Eclipse RCP wizards, modal dialogs, and fragile UI keystrokes. 

`ln_studio_skill` transforms Infor LN Studio into a **headless-capable, automated developer and AI agent ecosystem**:

1. **Headless JCA 1.6 Connectivity & BYOJ (`ln_server_client.py`)**: Direct BDE XML communication over HTTPS via auto-discovered local Eclipse JARs (`JCAAdapter4ERPln-10.8.10.jar` + `lnstudio_commoncore.jar` from `LN_STUDIO_HOME`, zero proprietary JARs tracked in Git) and JDK 11 (~150MB RAM footprint for Python CLI + Headless JVM Daemon).
2. **3-Tier Automated OAuth2 Token Lifecycle (`ln_env_manager.py`)**: Persistent per-workspace token cache at `~/.ln_studio/tokens/<workspace>.json` with a 5-minute safety buffer, silent refresh via `refresh_token` or Service Account (`saak`/`sask`), and interactive browser login (`webbrowser.open`) + `--manual-auth` paste fallback for headless/SSH/WSL environments.
3. **Remote Server Explorers & Workspace Reference Sync (`ln_component_explorer.py`)**: Browse remote Applications, Software Projects, Activities, and Components across all 12 types, or pull Read-Only reference copies (`sync-reference`) into `.reference/<type>/` while automatically indexing `.tbl` and `.dmn` XMLs into `.ln_dd_cache.json`.
4. **Complete 12-Component Ecore Generators & Report Cloning**: Declarative generation for Tables (`.tbl`), Sessions (`.ses`), Domains (`.dmn`), Libraries (`.lib`), Menus (`.mnu`), Labels (`.lbl`), Messages (`.msg`), Questions (`.qst`/`.que`), Include Functions (`.fnc`/`.fun`), and Additional Files (`.add`), plus baseline report/component cloning (`clone-component --source-type report`).
5. **Pre-Commit SCM Engine & Split `deploy-test` (`ln_scm_engine.py`, `ln_build_pipeline.py`)**: Safe `--mode compile-only` (default: `Put -> Compile -> VSC -> CheckIn`) and `--mode schema-crdd` (`Put -> Compile -> CRDD -> CreateTables -> VSC -> CheckIn` with `--dry-run` pre-check and active LN UI session lock warning).
6. **Strict Human-in-the-Loop Commit Gate ([ADR 0007](../docs/adr/0007-headless-jca-connectivity-scm-and-mcp-server.md))**: Hard-blocks `End Activity` / `CloseTask` / `FinalizeActivity` in CLI, MCP, and at the Java protocol level inside `LNStudioJcaBridge.java`.
7. **Native Stdio MCP Server (`ln_studio_mcp.py`)**: Exposes all capabilities via JSON-RPC 2.0 stdio with 16 tools, ready for Claude Desktop, Cursor, Antigravity, and AI Agents.

---

## Headless JCA Architecture

```mermaid
flowchart TD
    subgraph Clients["Dual Entry Points"]
        AGENT["AI Agent\n(Claude Code / Cursor / Antigravity)"]
        DEV["Developer Terminal\n(CLI Commands)"]
    end

    subgraph EntryLayers["Orchestration Layer (Single Testing Seam)"]
        MCP["Native Stdio MCP Server\n(ln_studio_mcp.py - 16 Tools)"]
        CLI["Master Orchestrator CLI\n(ln_component_builder.py - 37 Subcommands)"]
    end

    subgraph CoreEngines["ln_studio_skill Core Engines"]
        ENV["Environment & .ionapi Manager\n(Token Cache, cloudenv.prefs, connectivity.prefs)"]
        EXPLORE["Remote Server Explorers\n(Projects, Activities, 12-Component Explorer)"]
        GEN["12-Component Declarative Generator & Cloner\n(.tbl, .ses, .dmn, .lib, .mnu, .lbl, .rpt, .msg, .qst, .fnc, .add)"]
        SCM["Pre-Commit SCM Engine\n(Get, CheckOut, Uncheckout, Put, CheckIn)"]
        GATE["Human Commit Gate\nHard-Blocks End Activity | prepare-end-activity"]
        VAL["4-Layer Static Activity Validator\n(SCM, XML, Cross-References, 4GL Offline)"]
    end

    subgraph Bridge["Headless Java JCA Daemon (JDK 11)"]
        JCA["LNStudioJcaBridge.java\n(JCAAdapter4ERPln-10.8.10.jar + lnstudio_commoncore.jar)"]
        AUTH["OAuth2 Token Refresher\n(Desktop oob Catcher & Service Accounts)"]
    end

    subgraph Server["Infor LN Server / CloudSuite (HTTPS / XML BDE)"]
        BDE_PROJ["Project & Activity BDEs\n(Application, SoftwareProject_V2, FglStudio)"]
        BDE_EXP["Component Explorer BDEs\n(Group, StudioComponent.GetBrowseList)"]
        BDE_SCM["SCM & Build BDEs\n(DR_*, Compile, ConvertToRuntime, executeVSC)"]
    end

    AGENT --> MCP
    DEV --> CLI

    MCP --> ENV
    MCP --> EXPLORE
    MCP --> GEN
    MCP --> SCM
    MCP --> GATE
    MCP --> VAL

    CLI --> ENV
    CLI --> EXPLORE
    CLI --> GEN
    CLI --> SCM
    CLI --> GATE
    CLI --> VAL

    ENV --> JCA
    EXPLORE --> JCA
    SCM --> JCA
    JCA --> AUTH

    JCA -- "HTTPS / XML BDE" --> BDE_PROJ
    JCA -- "HTTPS / XML BDE" --> BDE_EXP
    JCA -- "HTTPS / XML BDE" --> BDE_SCM

    classDef blue fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px;
    classDef orange fill:#fff3e0,stroke:#fb8c00,stroke-width:2px;
    classDef purple fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px;
    classDef red fill:#ffebee,stroke:#e53935,stroke-width:2px;
    class Clients,EntryLayers blue;
    class CoreEngines,Bridge orange;
    class GATE red;
    class Server purple;
```

---

## AI Agent Configuration Matrix

Connect your AI Coding Agent directly to Infor LN Studio via native Stdio MCP. Choose your environment below and copy the snippet into your client configuration:

### 1. Claude Desktop (`%APPDATA%\Claude\claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "infor-ln-studio": {
      "command": "python",
      "args": [
        "c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/ln_studio_skill/tools/ln_studio_mcp.py"
      ],
      "env": {
        "PYTHONIOENCODING": "utf-8",
        "LN_STUDIO_HOME": "C:/Infor/LNStudio",
        "JAVA_HOME": "C:/Program Files/Eclipse Adoptium/jdk-11.0.22.7-hotspot"
      }
    }
  }
}
```

### 2. Cursor IDE (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "infor-ln-studio": {
      "command": "python",
      "args": [
        "${workspaceFolder}/ln_studio_skill/tools/ln_studio_mcp.py"
      ],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

### 3. Google Antigravity (`antigravity.json`)
```json
{
  "mcpServers": {
    "infor-ln-studio": {
      "command": "python",
      "args": [
        "${workspaceRoot}/ln_studio_skill/tools/ln_studio_mcp.py"
      ]
    }
  }
}
```

### 4. Gemini CLI / Generic Stdio MCP
```bash
# Automated setup for supported clients:
python ln_studio_skill/tools/ln_component_builder.py mcp-setup --target claude-desktop
python ln_studio_skill/tools/ln_component_builder.py mcp-setup --target cursor
```

---

## 5-Stage Lifecycle Matrix

All 16 MCP tools and 37 CLI subcommands are mapped into 5 logical lifecycle phases matching enterprise Infor LN development:

| Stage / Lifecycle | MCP Tool Name | Master CLI Equivalent | Description & Safety Guardrail |
|---|---|---|---|
| **1. Environment & Auth** | `ln_list_environments` | `environments`, `workspace` | List workspaces, tenant IDs, and gateway connectivity |
| | `ln_connect` | `connect --ionapi <file>` | Import `.ionapi`, authenticate OAuth2, and sync preferences |
| **2. Remote Exploration** | `ln_explore_projects` | `project --list` | Browse remote Applications, Software Projects, and VRCs |
| | `ln_explore_activities` | `activity --list` | Query open activities, tasks, and modified components |
| | `ln_explore_components` | `explorer --type <type>` | Query server components across all 12 types with wildcard filters |
| | `ln_create_activity` | `activity --create <id>` | Create remote Activity and bootstrap local workspace metadata |
| | `ln_clean_activity` | `clean-activity` | Recover stuck locks or workareas on server |
| **3. Modeling & Cloning** | `ln_create_component` | `table`, `session`, `domain`, ... | Declaratively generate any of the 12 LN Studio components |
| | `ln_clone_component` | `clone-component` | Clone server component into renamed custom activity component |
| | `ln_get_component` | `get-component` | Fetch server component (in-memory inspect or read-only download) |
| | `ln_sync_reference` | `sync-reference` | Pull read-only server references & auto-index `.ln_dd_cache.json` |
| **4. SCM & Cloud Testing** | `ln_checkout_component`| `checkout-component` | Check out component on server (**Hard-blocks `tx*` extensions**) |
| | `ln_uncheckout_component`| `uncheckout-component` | Revert server lock and restore local read-only copy |
| | `ln_checkin_component` | `checkin-component` | Check in component with comment for live testing in LN UI |
| | `ln_deploy_test` | `deploy-test` | Automated composite deployment (`Put` -> `Compile` -> `CheckIn`) |
| **5. Verification & Gate** | `ln_validate_activity` | `validate`, `diagnose` | 4-layer static verification (`.admin`, XML facets, refs, 4GL) |
| | `ln_prepare_end_activity`| `prepare-end-activity` | Pre-commit readiness verifier and human commit handoff report |
| | `ln_end_activity` | `end-activity` | **Hard-Blocked Safety Gate**: Enforces human review in LN Studio |

---

## 12-Component Archetype Matrix

`ln_studio_skill` supports high-fidelity declarative XML generation matching official Infor LN Studio Build 0640 schemas across all 12 component archetypes:

| Component Type | Extension | Ecore Datatype ID | CLI Generator Flag | CLI Command Example |
|---|---|---|---|---|
| **Table** | `.tbl` | Ecore Model 1-14 | `table` | `python ln_studio_skill/tools/ln_component_builder.py table --spec schema.yaml` |
| **Session** | `.ses` | Type 1-4, MMT | `session` | `python ln_studio_skill/tools/ln_component_builder.py session --spec schema.yaml` |
| **Domain** | `.dmn` | Byte, Long, String, Enum | `domain` | `python ln_studio_skill/tools/ln_component_builder.py domain --spec schema.yaml` |
| **Library** | `.lib` | DLL / Extension | `library` | `python ln_studio_skill/tools/ln_component_builder.py library --spec schema.yaml` |
| **Menu** | `.mnu` | Menu Hierarchy | `menu` | `python ln_studio_skill/tools/ln_component_builder.py menu --spec schema.yaml` |
| **Label** | `.lbl` | Multi-language | `label` | `python ln_studio_skill/tools/ln_component_builder.py label --code txcmg011.lbl --desc "Batch"` |
| **Report** | `.rpt` | Layout & Data Source | `report` / `clone-component` | `python ln_studio_skill/tools/ln_component_builder.py clone-component --source-type report ...` |
| **Message** | `.msg` | Severity Levels | `message` | `python ln_studio_skill/tools/ln_component_builder.py message --code txcmg0001 --desc "Invalid"` |
| **Question** | `.qst` | Yes/No/Cancel | `question` | `python ln_studio_skill/tools/ln_component_builder.py question --code txcmg0002 --desc "Proceed?"` |
| **Function** | `.fnc` | Reusable Include | `function` | `python ln_studio_skill/tools/ln_component_builder.py function --code txcmgfnc01 --desc "Calc"` |
| **Additional File** | `.add` | Text / Binary Asset | `additional` | `python ln_studio_skill/tools/ln_component_builder.py additional --code txcmgcfg --desc "Config"` |
| **MMT Controller** | `.ses` | Type 2 MMT | `session` | `python ln_studio_skill/tools/ln_component_builder.py session --spec mmt_spec.yaml` |

### Consolidated Declarative YAML Specification (`schema.yaml`)

```yaml
version_id: B61O_a_ext
application: PROJ_CUSTOM_01

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
      - name: bild
        domain: tfgld.date
        type: date
      - name: tamt
        domain: tcamnt
        type: amount
      - name: stat
        domain: txcmg.stat
        type: enum
    indices:
      - id: 1
        columns: [btno]
        primary_key: true

sessions:
  - code: txcmg0110m100
    description: Billing Batch Maintenance
    type: mmt_controller
    table: txcmg011
    satellites: [txcmg0510m000]
    form_commands:
      - name: exec.user.0
        function: generate.billing
        label_code: txcmg0110m100.cmd1
        description: Generate Billing
```

<details>
<summary><b>View Specialized MMT Controller & Satellite Schema Details</b></summary>

```yaml
# MMT Satellite Session Definition
sessions:
  - code: txcmg0510m000
    description: Billing Batch Lines
    type: standard_maintenance
    table: txcmg051
    satellite_relationship:
      controller_session: txcmg0110m100
      foreign_keys:
        - parent_column: btno
          child_column: btno
```
</details>

---

## Enterprise Safety Guardrails

> [!IMPORTANT]
> <a id="extension-modeler-boundary"></a>
> ### Extension Modeler Boundary (Cloud UI Workflow)
> In Infor LN CloudSuite, **Extension Modeler objects** (`ttext1500m000`, components named `tx*` in `ess`, `est`, `esb`, `esm`, `esr`) **cannot be checked out or checked in via Eclipse Studio SCM**. Attempting to do so corrupts server-side repository locks.  
> 
> `ln_studio_skill` enforces the **Agent Guide-and-Paste Protocol**:
> 1. Writes to Extension Modeler components are intercepted with `ReadOnlyComponentError`.
> 2. Use `new-extension` to scaffold cohesive 4GL extension scripts locally.
> 3. Use `import-extension` to pull standard extension hooks read-only.
> 4. Use `extension-hooks --copy-to-clipboard` to extract `#context_on` blocks into your clipboard.
> 5. **Paste and compile the code directly into the Infor LN UI Web client (`ttext1500m000`)**.

> [!WARNING]
> <a id="human-commit-gate"></a>
> ### Strict Human-in-the-Loop Commit Gate ([ADR 0007](../docs/adr/0007-headless-jca-connectivity-scm-and-mcp-server.md))
> To protect enterprise environments against accidental or automated delivery closures:
> - Calling `end-activity` in CLI, MCP, or Java bridge raises `PreCommitBoundaryError` and is **hard-blocked**.
> - Automated agents must run `prepare-end-activity` to verify activity readiness, synchronize `.project` and `.admin`, and generate a structured commit handoff report.
> - **A human developer must perform the final review inside Infor LN Studio and click "End Activity"**.

---

## Master CLI Reference

```bash
# -------------------------------------------------------------
# 1. Environment & Workspace Management
# -------------------------------------------------------------
python ln_studio_skill/tools/ln_component_builder.py environments
python ln_studio_skill/tools/ln_component_builder.py connect --ionapi credentials/PRD_ENV.ionapi --workspace PRD_ENV
python ln_studio_skill/tools/ln_component_builder.py workspace --list-workspaces

# -------------------------------------------------------------
# 2. Remote Server Explorers
# -------------------------------------------------------------
python ln_studio_skill/tools/ln_component_builder.py project --list
python ln_studio_skill/tools/ln_component_builder.py activity --list --project PROJ_CUSTOM_01
python ln_studio_skill/tools/ln_component_builder.py activity --create ACT_DEV_001 --project PROJ_CUSTOM_01 --desc "New Feature" --bootstrap
python ln_studio_skill/tools/ln_component_builder.py clean-activity --project PROJ_CUSTOM_01 --activity-id ACT_DEV_001
python ln_studio_skill/tools/ln_component_builder.py explorer --type table --filter "tx*" --project PROJ_CUSTOM_01

# -------------------------------------------------------------
# 3. Declarative Component Modeling & Cloning
# -------------------------------------------------------------
python ln_studio_skill/tools/ln_component_builder.py table --spec schema.yaml --output-dir .
python ln_studio_skill/tools/ln_component_builder.py session --spec schema.yaml --output-dir .
python ln_studio_skill/tools/ln_component_builder.py clone-component --source-type report --source-name tdsls440101000 --target-name txsls440101000 --activity ACT_DEV_001

# -------------------------------------------------------------
# 4. SCM, Reference Sync & Automated deploy-test Pipeline
# -------------------------------------------------------------
python ln_studio_skill/tools/ln_component_builder.py sync-reference --type table --name "tdsls40*" --workspace PRD_ENV
python ln_studio_skill/tools/ln_component_builder.py checkout-component --type table --name txcmg011 --activity ACT_DEV_001 --comment "Modify batch"
python ln_studio_skill/tools/ln_component_builder.py checkin-component --type table --name txcmg011 --activity ACT_DEV_001 --comment "Updated"

# Safe Script-Only Deploy & Test (Default: Put -> Compile -> VSC -> CheckIn):
python ln_studio_skill/tools/ln_component_builder.py deploy-test --type table --name txcmg011 --activity ACT_DEV_001 --mode compile-only --comment "Deploy script"

# Full Schema Reconfiguration (Put -> Compile -> CRDD -> CreateTables -> VSC -> CheckIn):
python ln_studio_skill/tools/ln_component_builder.py deploy-test --type table --name txcmg011 --activity ACT_DEV_001 --mode schema-crdd --dry-run
python ln_studio_skill/tools/ln_component_builder.py deploy-test --type table --name txcmg011 --activity ACT_DEV_001 --mode schema-crdd --comment "Deploy schema"

# -------------------------------------------------------------
# 5. Verification & Pre-Commit Gates
# -------------------------------------------------------------
python ln_studio_skill/tools/ln_component_builder.py validate ACT_DEV_001 --strict --fix
python ln_studio_skill/tools/ln_component_builder.py prepare-end-activity --activity ACT_DEV_001
```

---

## Automated Test Suite

Run the full unit test suite across all tools:

```bash
python -m unittest discover -s ln_studio_skill/tools/tests -p "test_*.py"
```

Validate documentation integrity & links:

```bash
python ln_studio_skill/tools/validate_skill.py --skill-dir ln_studio_skill
```

---

## Directory Layout

```text
ln_studio_skill/
├── SKILL.md                          # AI agent skill definition & instructions
├── README.md                         # Dedicated toolset & MCP documentation
├── references/                       # Distilled LN Studio Application Development Guide
└── tools/
    ├── ln_component_builder.py       # Master CLI orchestrator (37 subcommands)
    ├── ln_studio_mcp.py              # Native Stdio MCP Server (16 tools)
    ├── ln_env_manager.py             # .ionapi & OAuth2 credentials lifecycle manager
    ├── ln_server_client.py           # Headless JCA server client & Java bridge
    ├── ln_project_activity_manager.py# Software Projects & Activity Explorer manager
    ├── ln_component_explorer.py      # 12-component explorer, get, inspect, clone
    ├── ln_scm_engine.py              # Pre-Commit SCM Engine (Check-Out, Put, CheckIn)
    ├── ln_build_pipeline.py          # Remote build, CRDD, CreateTables, deploy-test
    ├── ln_extension_manager.py       # Extension Modeler local project workflow (ADR 0006)
    ├── validate_ln_activity.py       # 4-Layer static activity validator & safe --fix
    ├── check_4gl_script.py           # Offline 4GL script syntax inspector
    ├── scm_guardrails.py             # SCM Read-Only & Extension protection rules
    ├── admin_sync.py                 # 12-extension .admin SCM cache synchronizer
    ├── generate_ln_*.py              # 12-Component declarative Ecore generators
    └── tests/                        # Automated unit tests
```
