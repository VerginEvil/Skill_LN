[![Infor LN](https://img.shields.io/badge/ERP-Infor%20LN%2010.8-blue.svg)](https://www.infor.com)
[![Agent Skill](https://img.shields.io/badge/AI%20Skill-Claude%20Code%20%7C%20OpenClaw%20%7C%20Cursor%20%7C%20Antigravity-green.svg)](#)
[![Automation](https://img.shields.io/badge/Toolchain-Eclipse%20RCP%20Automation-orange.svg)](#)

# Skill_LN: Infor ERP LN Developer Skill & Studio Automation Toolchain

A unified, production-grade intelligence and automation system for **Infor ERP LN** and **Infor LN Studio 10.8 build 0640 (April 2026 tree, Eclipse RCP)**.

This repository provides two core pillars:
1. **[Infor LN Studio Automation Toolset & Assistant Skill](#infor-ln-studio-automation-toolset--skill)** (`ln_studio_skill/`, self-contained: knowledge plus executables under `ln_studio_skill/tools/`): A reverse-engineered CLI toolchain and agent skill enabling declarative metadata generation, bidirectional 4GL source synchronization, Windows action bridging, and closed-loop compiler diagnostic loops. Studio usage knowledge is distilled from the *Application Development Guide (Cloud and On-premises), September 2025* into `ln_studio_skill/references/studio_guide/` with master index `references/STUDIO_INDEX.md`.
2. **[Baan 4GL Programmer's Guide, Dev Tools & Best Practices Skill](#infor-erp-ln-programmers-guide-skill)** (`erp-ln-progguide/`): Over 5,000 converted Markdown reference pages covering 2,425 Baan 4GL functions, GenAI APIs, SQL volumes, Extension Modeler, Public Interfaces up to 25082026, 13 chapters of Infor LN Development Tools (2016), and a 5-part architectural Best Practices Cookbook suite.

---

## Architecture Overview

```
                                  +-----------------------------------+
                                  |        User / AI Agent            |
                                  +-----------------+-----------------+
                                                    |
                     +------------------------------+-------------------------------+
                     |                                                              |
                     v                                                              v
       [1. Declarative Authoring]                                     [2. Code Sync & Automation]
                     |                                                              |
                     v                                                              v
       +-----------------------------+                               +-----------------------------+
       | ln_studio_skill/tools/ln_component_builder  |                               | ln_studio_skill/tools/inject_ln_script.py   |
       | Generates .tbl, .ses, .dmn, |                               | Syncs .dal / .cln / .src    |
       | .lbl from YAML/JSON specs   |                               | with embedded XML tags      |
       +--------------+--------------+                               +--------------+--------------+
                      |                                                             |
                      +------------------------------+------------------------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | LN Studio Activity Directory      |
                                  | (workspace/<WS>/<Act> [<Proj>])   |
                                  | - tx/table/.../*.tbl              |
                                  | - tx/session/.../*.ses            |
                                  | - .admin & .project               |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | ln_studio_skill/tools/ln_studio_bridge.py         |
                                  | Triggers F5 (Refresh) & Ctrl+B    |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | Infor LN Studio (Eclipse RCP)     |
                                  | - IncrementalProjectBuilderBIC    |
                                  | - JCA Adapter -> LN Server (bic)  |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | ln_studio_skill/tools/ln_error_reader.py          |
                                  | Directly parses .markers file     |
                                  | -> Returns line-accurate errors   |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | Closed-Loop Autonomous Debugging  |
                                  | Agent fixes code until 0 errors   |
                                  +-----------------------------------+
```

---

## Infor LN Studio Automation Toolset & Skill

Located in [`ln_studio_skill/`](ln_studio_skill/) (self-contained: knowledge plus executables).

### CLI Tools Summary

| Tool | Purpose | Primary Commands |
|---|---|---|
| [`ln_studio_skill/tools/ln_component_builder.py`](ln_studio_skill/tools/ln_component_builder.py) | **Master Orchestrator CLI** | `table`, `session`, `component`, `inject`, `extract`, `sync-admin`, `build`, `pipeline` |
| [`ln_studio_skill/tools/ln_workspace_manager.py`](ln_studio_skill/tools/ln_workspace_manager.py) | Workspace & Activity Resolver | `python ln_studio_skill/tools/ln_workspace_manager.py --list-workspaces`<br>`python ln_studio_skill/tools/ln_workspace_manager.py --list-activities` |
| [`ln_studio_skill/tools/ln_schema_parser.py`](ln_studio_skill/tools/ln_schema_parser.py) | Declarative Schema Validator | `python ln_studio_skill/tools/ln_schema_parser.py <schema.yaml>` |
| [`ln_studio_skill/tools/generate_ln_table.py`](ln_studio_skill/tools/generate_ln_table.py) | Table/Label/Domain XML Generator | `python ln_studio_skill/tools/generate_ln_table.py --spec <spec> --activity <act>` |
| [`ln_studio_skill/tools/generate_ln_session.py`](ln_studio_skill/tools/generate_ln_session.py) | Session & Form XML Generator | `python ln_studio_skill/tools/generate_ln_session.py --spec <spec> --activity <act>` |
| [`ln_studio_skill/tools/inject_ln_script.py`](ln_studio_skill/tools/inject_ln_script.py) | 4GL Source Code Synchronizer | `python ln_studio_skill/tools/inject_ln_script.py --inject --source <f.dal> --target <f.tbl>`<br>`python ln_studio_skill/tools/inject_ln_script.py --extract --source <f.tbl> --output <f.dal>` |
| [`ln_studio_skill/tools/admin_sync.py`](ln_studio_skill/tools/admin_sync.py) | Activity SCM `.admin` Synchronizer | `python ln_studio_skill/tools/admin_sync.py --activity <act> --scan-and-update`<br>`python ln_studio_skill/tools/admin_sync.py --activity <act> --status` |
| [`ln_studio_skill/tools/ln_error_reader.py`](ln_studio_skill/tools/ln_error_reader.py) | Eclipse `.markers` Error Parser | `python ln_studio_skill/tools/ln_error_reader.py --activity <act> [--errors-only]` |
| [`ln_studio_skill/tools/ln_studio_bridge.py`](ln_studio_skill/tools/ln_studio_bridge.py) | Windows Action Bridge (F5, Ctrl+B) | `python ln_studio_skill/tools/ln_studio_bridge.py --build-and-check --activity <act>` |

### Quick Start: Generate Table & Session from Schema

1. Define your table and session in YAML (e.g. [`ln_studio_skill/templates/table_schema_sample.yaml`](ln_studio_skill/templates/table_schema_sample.yaml)):
```yaml
table:
  code: txptc200
  description: Inspection Criteria Configuration
fields:
  - name: seqn
    domain: tcpono
    mandatory: true
    default: '$__unique'
  - name: cmnf
    domain: tcmcs.cmnf
    mandatory: true
indices:
  - id: 1
    columns: [seqn]
    primary_key: true
session:
  code: txptc1200m000
```

2. Run the end-to-end pipeline in one command:
```bash
python ln_studio_skill/tools/ln_component_builder.py pipeline --spec ln_studio_skill/templates/table_schema_sample.yaml --activity "dev_natt_01103"
```

3. If errors are flagged during compilation, read line-accurate problem markers:
```bash
python ln_studio_skill/tools/ln_component_builder.py diagnose --activity "dev_natt_01103" --errors-only
```

---

## Infor ERP LN Programmer's Guide, Dev Tools & Best Practices Skill

Located in [`erp-ln-progguide/`](erp-ln-progguide/).

- **5,000+ reference pages** | **2,425 Baan 4GL functions** | **1,833 public interfaces / process extensions** | **AFS `stpapi.*` primitives**
- **13 Complete Development Tools Chapters** ([`references/DEV_TOOLS_INDEX.md`](erp-ln-progguide/references/DEV_TOOLS_INDEX.md)): Software components, Data Dictionaries (runtime vs application), table reconfiguration (`crdd`), 4GL Engine, SCM, PMC, and reporting.
- **5 Actionable Best Practices Cookbooks** ([`references/best_practices/`](erp-ln-progguide/references/best_practices/)):
  1. [`01_extension_hooks_cookbook.md`](erp-ln-progguide/references/best_practices/01_extension_hooks_cookbook.md): Table/Session lifecycles, `DALHOOKERROR`, CDF logic hooks, Cloud governance.
  2. [`02_dal_architecture_and_business_logic.md`](erp-ln-progguide/references/best_practices/02_dal_architecture_and_business_logic.md): Separation of Concerns (no DB writes in UI scripts!), DAL 1 vs 2, business methods.
  3. [`03_sql_query_optimization_and_transactions.md`](erp-ln-progguide/references/best_practices/03_sql_query_optimization_and_transactions.md): Embedded Baan SQL, index alignment, array fetching, `db.retry.point()`.
  4. [`04_data_model_and_domain_design.md`](erp-ln-progguide/references/best_practices/04_data_model_and_domain_design.md): Domain modeling, referential integrity, safe 2-step `crdd` reconfiguration.
  5. [`05_session_and_mmt_patterns.md`](erp-ln-progguide/references/best_practices/05_session_and_mmt_patterns.md): Session types 1-4, MMT Controller & Satellite synchronization, labels/localization.
- Full-text search with `python erp-ln-progguide/scripts/search.py <query>`.

### Fast Reference Search
```bash
# Search 4GL functions
python erp-ln-progguide/scripts/search.py genai.processing.start
python erp-ln-progguide/scripts/search.py subquery --dir sql
python erp-ln-progguide/scripts/search.py "Address.Create" --dir public_interfaces

# Search Best Practices Cookbooks & Dev Tools
python erp-ln-progguide/scripts/search.py "DALHOOKERROR" --dir best_practices
python erp-ln-progguide/scripts/search.py "query.extend.where" --dir best_practices
python erp-ln-progguide/scripts/search.py "crdd" --dir dev_tools
python erp-ln-progguide/scripts/search.py "MMT Controller" --dir best_practices
```

---

## Installation & Skill Configuration

### Installing the Skills into AI Coding Agents

Copy or link the skill folders to your agent's configuration directory:

| Tool | Reference Skill (`erp-ln-progguide`) | Studio Assistant Skill (`ln_studio_skill`) |
|---|---|---|
| **Claude Code** | `~/.claude/skills/erp-ln-progguide/` | `~/.claude/skills/ln_studio_skill/` |
| **OpenClaw** | `~/.openclaw/skills/erp-ln-progguide/` | `~/.openclaw/skills/ln_studio_skill/` |
| **Cursor** | `.cursor/skills/erp-ln-progguide/` | `.cursor/skills/ln_studio_skill/` |
| **Gemini CLI / Antigravity** | `~/.gemini/skills/erp-ln-progguide/` | `~/.gemini/skills/ln_studio_skill/` |

Architecture and coding rules are codified in [`.antigravity/rules/infor_ln.md`](.antigravity/rules/infor_ln.md).

---

## Automated Test Suite

Run the full unit test suite:
```bash
python -m unittest discover -s ln_studio_skill/tools/tests
```
All 69 unit tests validate schema constraints, XML generation, script injection/extraction round-trips, binary marker parsing, and admin synchronization.
