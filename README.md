[![Infor LN](https://img.shields.io/badge/ERP-Infor%20LN%2010.8-blue.svg)](https://www.infor.com)
[![Agent Skill](https://img.shields.io/badge/AI%20Skill-Claude%20Code%20%7C%20OpenClaw%20%7C%20Cursor%20%7C%20Antigravity-green.svg)](#)
[![Automation](https://img.shields.io/badge/Toolchain-Eclipse%20RCP%20Automation-orange.svg)](#)

# Skill_LN: Infor ERP LN Developer Skill & Studio Automation Toolchain

A unified, production-grade intelligence and automation system for **Infor ERP LN** and **Infor LN Studio 10.8 (Eclipse RCP)**.

This repository provides two core pillars:
1. **[Infor LN Studio Automation Toolset & Assistant Skill](#infor-ln-studio-automation-toolset--skill)** (`ln_studio_skill/` & `tools/`): A reverse-engineered CLI toolchain and agent skill enabling declarative metadata generation, bidirectional 4GL source synchronization, Windows action bridging, and closed-loop compiler diagnostic loops.
2. **[Baan 4GL Programmer's Guide & Public Interfaces Skill](#infor-erp-ln-programmers-guide-skill)** (`erp-ln-progguide/`): Over 5,000 converted Markdown reference pages covering 2,425 Baan 4GL functions, GenAI APIs, SQL volumes, Extension Modeler, and Public Interfaces up to release 25082026.

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
       | tools/ln_component_builder  |                               | tools/inject_ln_script.py   |
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
                                  | tools/ln_studio_bridge.py         |
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
                                  | tools/ln_error_reader.py          |
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

Located in [`ln_studio_skill/`](ln_studio_skill/) and [`tools/`](tools/).

### CLI Tools Summary

| Tool | Purpose | Primary Commands |
|---|---|---|
| [`tools/ln_component_builder.py`](tools/ln_component_builder.py) | **Master Orchestrator CLI** | `table`, `session`, `component`, `inject`, `extract`, `sync-admin`, `build`, `pipeline` |
| [`tools/ln_workspace_manager.py`](tools/ln_workspace_manager.py) | Workspace & Activity Resolver | `python tools/ln_workspace_manager.py --list-workspaces`<br>`python tools/ln_workspace_manager.py --list-activities` |
| [`tools/ln_schema_parser.py`](tools/ln_schema_parser.py) | Declarative Schema Validator | `python tools/ln_schema_parser.py <schema.yaml>` |
| [`tools/generate_ln_table.py`](tools/generate_ln_table.py) | Table/Label/Domain XML Generator | `python tools/generate_ln_table.py --spec <spec> --activity <act>` |
| [`tools/generate_ln_session.py`](tools/generate_ln_session.py) | Session & Form XML Generator | `python tools/generate_ln_session.py --spec <spec> --activity <act>` |
| [`tools/inject_ln_script.py`](tools/inject_ln_script.py) | 4GL Source Code Synchronizer | `python tools/inject_ln_script.py --inject --source <f.dal> --target <f.tbl>`<br>`python tools/inject_ln_script.py --extract --source <f.tbl> --output <f.dal>` |
| [`tools/admin_sync.py`](tools/admin_sync.py) | Activity SCM `.admin` Synchronizer | `python tools/admin_sync.py --activity <act> --scan-and-update`<br>`python tools/admin_sync.py --activity <act> --status` |
| [`tools/ln_error_reader.py`](tools/ln_error_reader.py) | Eclipse `.markers` Error Parser | `python tools/ln_error_reader.py --activity <act> [--errors-only]` |
| [`tools/ln_studio_bridge.py`](tools/ln_studio_bridge.py) | Windows Action Bridge (F5, Ctrl+B) | `python tools/ln_studio_bridge.py --build-and-check --activity <act>` |

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
python tools/ln_component_builder.py pipeline --spec ln_studio_skill/templates/table_schema_sample.yaml --activity "dev_natt_01103"
```

3. If errors are flagged during compilation, read line-accurate problem markers:
```bash
python tools/ln_component_builder.py diagnose --activity "dev_natt_01103" --errors-only
```

---

## Infor ERP LN Programmer's Guide Skill

Located in [`erp-ln-progguide/`](erp-ln-progguide/).

- **2,970 + 155 + 162 + 2,361 + 76 pages** | **2,425 function references** | **1,833 public interfaces / process extensions** | **AFS `stpapi.*` primitives**
- Full-text search with `python erp-ln-progguide/scripts/search.py <query>`.

### Fast Reference Search
```bash
# Search 4GL functions
python erp-ln-progguide/scripts/search.py genai.processing.start
python erp-ln-progguide/scripts/search.py subquery --dir sql
python erp-ln-progguide/scripts/search.py "Address.Create" --dir public_interfaces
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
python -m unittest discover tools/tests/
```
All 69 unit tests validate schema constraints, XML generation, script injection/extraction round-trips, binary marker parsing, and admin synchronization.
