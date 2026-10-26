[![Infor LN](https://img.shields.io/badge/ERP-Infor%20LN%2010.8-blue.svg)](https://www.infor.com)
[![Agent Skill](https://img.shields.io/badge/AI%20Skill-Claude%20Code%20%7C%20OpenClaw%20%7C%20Cursor%20%7C%20Antigravity-green.svg)](#)
[![Automation](https://img.shields.io/badge/Toolchain-Eclipse%20RCP%20Automation-orange.svg)](#)
[![Author](https://img.shields.io/badge/Author-Natthaphon%20Srikasem-purple.svg)](#credits--maintainer)
[![Tests](https://img.shields.io/badge/Tests-94%20Passed-brightgreen.svg)](#automated-test-suite)

# Skill_LN: Infor ERP LN Developer Skill & Studio Automation Toolchain

A unified, production-grade intelligence, modeling, and static verification system for **Infor ERP LN** and **Infor LN Studio 10.8 build 0640 (April 2026 tree, Eclipse RCP)**.

This repository provides three core pillars:
1. **[Infor LN Studio Automation Toolset & Assistant Skill](#infor-ln-studio-automation-toolset--skill)** (`ln_studio_skill/`, self-contained: knowledge plus executables under `ln_studio_skill/tools/`): A reverse-engineered CLI toolchain and agent skill enabling high-fidelity declarative metadata modeling, bidirectional 4GL source synchronization, OS Read-Only SCM guardrails, 12-extension `.admin` cache synchronization, offline 4GL syntax/completion inspection, 4-layer static activity validation (`validate` & `--fix`), Windows action bridging, and closed-loop compiler diagnostic loops. Studio usage knowledge is distilled from the *Application Development Guide (Cloud and On-premises), September 2025* into `ln_studio_skill/references/studio_guide/` with master index `references/STUDIO_INDEX.md`.
2. **[Baan 4GL Programmer's Guide, Dev Tools, Best Practices & Standalone Audit Engine](#infor-erp-ln-programmers-guide-dev-tools-best-practices--audit-engine)** (`erp-ln-progguide/`): Over 5,000 converted Markdown reference pages covering **2,266 authoritative bshell functions** (Build 0640) with Cloud Multi-Tenant Trust indicators, GenAI APIs, SQL volumes, Extension Modeler, Public Interfaces up to 25082026, 13 chapters of Infor LN Development Tools (2016), a 6-part architectural Best Practices Cookbook suite, official **Studio Script Templates**, and a zero-dependency **Standalone 4GL & DAL Audit Engine** (`scripts/audit_4gl.py`).
3. **[VS Code Extension Production-Ready Assets](#vs-code-extension-assets-package)** (`export/vscode/`): Production-grade TextMate grammar (`tmLanguage.json`), code snippets (`.code-snippets`), language configuration, and hover/completion catalog ready for authoring or packaging VS Code extensions for Baan 4GL and Infor LN development.

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
       [1. Declarative Authoring]                                     [2. Code Sync & Verification]
                     |                                                              |
                     v                                                              v
       +-----------------------------+                               +-----------------------------+
       | ln_component_builder.py     |                               | inject_ln_script.py         |
       | Generates .tbl, .ses, .lib, |                               | Syncs .dal / .cln / .src    |
       | .dmn, .lbl, .mnu from specs |                               | with SCM Read-Only checks   |
       +--------------+--------------+                               +--------------+--------------+
                      |                                                             |
                      +------------------------------+------------------------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | SCM Guardrail & 12-Ext Admin Sync |
                                  | - scm_guardrails.py (Read-Only)   |
                                  | - admin_sync.py (.admin cache)    |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | Four-Layer Static Validator       |
                                  | - validate_ln_activity.py         |
                                  | - check_4gl_script.py (offline)   |
                                  | - Safe --fix missing labels       |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | Standalone 4GL & DAL Audit Engine |
                                  | - erp-ln-progguide/scripts/       |
                                  |   audit_4gl.py (--cloud, --mode)  |
                                  | - Zero dependencies, pure Python  |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | ln_studio_bridge.py (Optional)    |
                                  | Triggers F5 (Refresh) & Ctrl+B    |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | ln_error_reader.py                |
                                  | Directly parses .markers file     |
                                  | -> Returns line-accurate errors   |
                                  +------------------+----------------+
                                                     |
                                                     v
                                  +-----------------------------------+
                                  | Closed-Loop Autonomous Debugging  |
                                  | Agent fixes code until 0 errors   |
                                  +------------------+----------------+
```

---

## Infor LN Studio Automation Toolset & Skill

Located in [`ln_studio_skill/`](ln_studio_skill/) (self-contained: knowledge plus executables).

### Key Capabilities

- **Human-in-the-Loop SCM Guardrails**: Intercepts writes to checked-in Read-Only files with clear diagnostic alerts (`ReadOnlyComponentError`) instructing developers to check out in Eclipse.
- **12-Extension `.admin` Synchronization**: Synchronizes on-disk components across all 12 LN Studio extensions (`.tbl`, `.ses`, `.lib`, `.dmn`, `.lbl`, `.mnu`, `.rpt`, `.rptdsrc`, `.msg`, `.que`, `.add`, `.fun`) without deleting `.mnu` or `.rpt` files.
- **High-Fidelity Object Modeling**: Full support for Ecore native datatypes (Byte=1, Double=2, Long=3, Numeric=5, String=6, Enum=7, Date=9, UTC=14), Workbench column labels (`<pkg><table_code>.<column>`), MMT Controllers with satellites, Form Commands, Libraries (DLL, `ess`, `est` with `#context_on`/`#context_off`), and Menus.
- **LN Studio 10.8 Syntax & Completion Extraction**: Extracted official dictionaries (Keywords, SQL Keywords, Program/Sub/Choice/Report Sections, Variables, Defines, DAL Object/Field Hooks, Templates) directly from Studio JARs.
- **Four-Layer Static Activity Verification (`validate` & `--fix`)**:
  - *Layer 1 (SCM)*: Audits `.admin` tracking & Read-Only states.
  - *Layer 2 (XML)*: Checks XML root tags, Ecore facets, and Session `<FormGroup>` hierarchy trees.
  - *Layer 3 (References)*: Resolves `.lbl` references, Table-Session column bindings, and Index columns.
  - *Layer 4 (4GL)*: Statically verifies section headers, block balance (`select`, `if`, `case`, `for`, `while`, `repeat`, `#context_on`), missing `#include` headers, Cloud Multi-Tenant rules (`--cloud`), and hook signatures.
  - *Safe `--fix`*: Auto-creates missing `.lbl` files and synchronizes `.admin` without touching Read-Only files.

### CLI Tools Summary

| Tool | Purpose | Primary Commands |
|---|---|---|
| [`ln_component_builder.py`](ln_studio_skill/tools/ln_component_builder.py) | **Master Orchestrator CLI** (14 subcommands) | `table`, `session`, `domain`, `library`, `menu`, `component`, `inject`, `extract`, `check-script`, `validate`, `sync-admin`, `diagnose`, `build`, `pipeline` |
| [`validate_ln_activity.py`](ln_studio_skill/tools/validate_ln_activity.py) | **4-Layer Activity Validator & Safe `--fix`** | `python ln_studio_skill/tools/validate_ln_activity.py [<act>] [--strict] [--fix] [--json]` |
| [`check_4gl_script.py`](ln_studio_skill/tools/check_4gl_script.py) | **Static 4GL Script Inspector** (Layer 4) | `python ln_studio_skill/tools/check_4gl_script.py <file> [--owning-xml <xml>] [--cloud] [--strict]` |
| [`scm_guardrails.py`](ln_studio_skill/tools/scm_guardrails.py) | **SCM Read-Only Protection** | Enforces `assert_file_writable` before write/inject |
| [`admin_sync.py`](ln_studio_skill/tools/admin_sync.py) | **12-Extension `.admin` SCM Synchronizer** | `python ln_studio_skill/tools/admin_sync.py --activity <act> --scan-and-update` |
| [`generate_ln_table.py`](ln_studio_skill/tools/generate_ln_table.py) | Table, Label & Domain XML Generator | `python ln_studio_skill/tools/generate_ln_table.py --spec <spec> [--output-dir <dir>]` |
| [`generate_ln_domain.py`](ln_studio_skill/tools/generate_ln_domain.py) | Standalone Domain XML Generator | `python ln_studio_skill/tools/generate_ln_domain.py --spec <spec> [--output-dir <dir>]` |
| [`generate_ln_session.py`](ln_studio_skill/tools/generate_ln_session.py) | Multi-Archetype Session Generator | `python ln_studio_skill/tools/generate_ln_session.py --spec <spec> [--output-dir <dir>]` |
| [`generate_ln_library.py`](ln_studio_skill/tools/generate_ln_library.py) | Library Generator (DLL, `ess`, `est`) | `python ln_studio_skill/tools/generate_ln_library.py --spec <spec> [--output-dir <dir>]` |
| [`generate_ln_menu.py`](ln_studio_skill/tools/generate_ln_menu.py) | Menu Generator (`<DR_Menu>` & `.lbl`) | `python ln_studio_skill/tools/generate_ln_menu.py --spec <spec> [--output-dir <dir>]` |
| [`inject_ln_script.py`](ln_studio_skill/tools/inject_ln_script.py) | 4GL Source Synchronizer (with Guardrails) | `python ln_studio_skill/tools/inject_ln_script.py --inject --source <f.dal> --target <f.tbl>` |
| [`extract_studio_dictionaries.py`](ln_studio_skill/tools/extract_studio_dictionaries.py) | LN Studio 10.8 Reflection Extractor | Generates `studio_syntax_completion.json` & docs |
| [`ln_workspace_manager.py`](ln_studio_skill/tools/ln_workspace_manager.py) | Pinned Studio & Activity Resolver | `python ln_studio_skill/tools/ln_workspace_manager.py --list-workspaces` |
| [`ln_error_reader.py`](ln_studio_skill/tools/ln_error_reader.py) | Eclipse `.markers` Error Parser | `python ln_studio_skill/tools/ln_error_reader.py --activity <act> [--errors-only]` |
| [`ln_studio_bridge.py`](ln_studio_skill/tools/ln_studio_bridge.py) | Windows Action Bridge (F5, Ctrl+B) | `python ln_studio_skill/tools/ln_studio_bridge.py --build-and-check --activity <act>` |

---

## Infor ERP LN Programmer's Guide, Dev Tools, Best Practices & Audit Engine

Located in [`erp-ln-progguide/`](erp-ln-progguide/).

### Key Capabilities

- **5,000+ reference pages** | **2,266 authoritative bshell functions** from Studio Build 0640 | **1,833 public interfaces / process extensions** | **AFS `stpapi.*` primitives**.
- **Enriched Grep-Friendly Function Index** ([`references/FUNCTION_INDEX.md`](erp-ln-progguide/references/FUNCTION_INDEX.md)): Strict single-line physical formatting with Cloud Multi-Tenant indicators:
  ```markdown
  - **Json.getString** | [Cloud: Trusted] [Scope: all] [Inc: <bic_json>] | `string Json.getString( ... )` -> `references/guide/...`
  - **cmf.create** | [Cloud: Untrusted] [Scope: all] [Inc: <bic_cmf>] | `long cmf.create( )` -> `references/guide/...`
  ```
- **Authoritative Functions Database** ([`index/functions_db.json`](erp-ln-progguide/index/functions_db.json)): Complete machine-readable catalog of bshell functions with return types, parameters, cloud trust, and required includes.
- **Standalone 4GL & DAL Audit Engine** ([`scripts/audit_4gl.py`](erp-ln-progguide/scripts/audit_4gl.py)):
  Zero-dependency Python CLI tool auditing 4GL, DAL2, and UEDLL files outside of Eclipse:
  ```bash
  python erp-ln-progguide/scripts/audit_4gl.py <target_path> [--mode dal2|uedll|general] [--cloud] [--format text|json] [--strict]
  ```
  - `SYN001`: Unbalanced block statements (`select/endselect`, `if/endif`, `for/endfor`, `while/endwhile`, `case/endcase`, `{}`)
  - `SYN002`: Section header typos and suggestions based on official Studio dictionary
  - `DAL001`: Rejection of interactive dialogs (`message()`, `ask.enum()`, `box()`) in DAL2 and Table Extensions
  - `DAL002`: Enforcement of DAL field hook signatures (`long i.mode` on `.update`, `long has_changed` on `.check`)
  - `DAL003`: Validation of return types for DAL hooks
  - `DAL004`: Prohibition of direct database mutations (`db.insert`, `db.update`, `db.delete`) in UI scripts
  - `CLD001`: Rejection of untrusted bshell functions in Cloud Multi-Tenant mode (`--cloud`)
  - `CLD002`: Warnings on deprecated bshell functions
  - `INC001`: Verification of required header includes (e.g. `#include <bic_json>`, `#include <bic_cmf>`)
  - `CAV001`: Direct float comparison warning (`== 100.0`)
  - `CAV003`: Nested transaction detection in DAL hooks
- **Official Script Templates** ([`templates/`](erp-ln-progguide/templates/)):
  Extracted directly from Studio `ScriptTemplates/`: `DalTwo.dal`, `UIDatabase.cln`, `UserExitDLL.ue`, `Dal.dal`, `Bol.cln`, `Function.cln`, `Integration.cln`, `Report.cln`, `ThreeGL.cln`.
- **13 Complete Development Tools Chapters** ([`references/DEV_TOOLS_INDEX.md`](erp-ln-progguide/references/DEV_TOOLS_INDEX.md)): Software components, Data Dictionaries (runtime vs application), table reconfiguration (`crdd`), 4GL Engine, SCM, PMC, and reporting.
- **6 Actionable Best Practices Cookbooks** ([`references/best_practices/`](erp-ln-progguide/references/best_practices/)):
  1. [`01_extension_hooks_cookbook.md`](erp-ln-progguide/references/best_practices/01_extension_hooks_cookbook.md): Table/Session lifecycles, `DALHOOKERROR`, CDF logic hooks, Cloud governance.
  2. [`02_dal_architecture_and_business_logic.md`](erp-ln-progguide/references/best_practices/02_dal_architecture_and_business_logic.md): Separation of Concerns (no DB writes in UI scripts!), DAL 1 vs 2, business methods.
  3. [`03_sql_query_optimization_and_transactions.md`](erp-ln-progguide/references/best_practices/03_sql_query_optimization_and_transactions.md): Embedded Baan SQL, index alignment, array fetching, `db.retry.point()`.
  4. [`04_data_model_and_domain_design.md`](erp-ln-progguide/references/best_practices/04_data_model_and_domain_design.md): Domain modeling, referential integrity, safe 2-step `crdd` reconfiguration.
  5. [`05_session_and_mmt_patterns.md`](erp-ln-progguide/references/best_practices/05_session_and_mmt_patterns.md): Session types 1-4, MMT Controller & Satellite synchronization, labels/localization.
  6. [`06_4gl_coding_standards_and_caveats.md`](erp-ln-progguide/references/best_practices/06_4gl_coding_standards_and_caveats.md): Domains vs primitives, buffer collision prevention, float equality caveats (`double.cmp`), and 1-based arrays.

---

## VS Code Extension Assets Package

Located in [`export/vscode/`](export/vscode/). Ready-to-use artifacts for future VS Code extension authoring or language server development:

- **TextMate Grammar** ([`syntaxes/baan4gl.tmLanguage.json`](export/vscode/syntaxes/baan4gl.tmLanguage.json)): Complete syntax highlighting grammar covering 80 keywords, 92 SQL operators, section headers, DAL hooks, pipe comments, and bshell functions.
- **Code Snippets** ([`snippets/baan4gl.code-snippets`](export/vscode/snippets/baan4gl.code-snippets)): 19 rich code snippets for official Studio templates, modern DAL2 hooks (`.update`, `.check`, `.is.applicable`, `before.save.object`), and retry-point transactions.
- **Language Configuration** ([`language-configuration.json`](export/vscode/language-configuration.json)): Comment rules (`|`), bracket pairs, quote auto-closing, and 4GL block folding.
- **Hover & Completion Dataset** ([`completions.json`](export/vscode/completions.json)): 2,491 structured completion proposals covering 2,266 bshell functions, predefined variables, standard defines, and DAL hooks with Markdown parameter hints.
- **Integration Guide** ([`README.md`](export/vscode/README.md)): Step-by-step instructions for wiring into a VS Code extension manifest.

---

## Installation & Skill Configuration

### Installing the Skills into AI Coding Agents

Copy or link the skill folders to your agent's configuration directory:

| Tool | Reference & Audit Skill (`erp-ln-progguide`) | Studio Assistant Skill (`ln_studio_skill`) |
|---|---|---|
| **Claude Code** | `~/.claude/skills/erp-ln-progguide/` | `~/.claude/skills/ln_studio_skill/` |
| **OpenClaw** | `~/.openclaw/skills/erp-ln-progguide/` | `~/.openclaw/skills/ln_studio_skill/` |
| **Cursor** | `.cursor/skills/erp-ln-progguide/` | `.cursor/skills/ln_studio_skill/` |
| **Gemini CLI / Antigravity** | `~/.gemini/skills/erp-ln-progguide/` | `~/.gemini/skills/ln_studio_skill/` |

---

## Automated Test Suite

Run the full unit test suite (94 tests total):
```bash
# 1. Studio Toolchain & Object Modeling Tests (86 tests)
python -m unittest discover -s ln_studio_skill/tools/tests

# 2. Standalone 4GL & DAL Audit Engine Tests (8 tests)
python -m unittest discover -s erp-ln-progguide/tests
```

Validate documentation integrity & links:
```bash
python ln_studio_skill/tools/validate_skill.py --skill-dir erp-ln-progguide
python ln_studio_skill/tools/validate_skill.py --skill-dir ln_studio_skill
```

---

## Credits & Maintainer

**Created and Maintained by:**
- **Natthaphon Srikasem** — Lead Developer & Infor LN Solution Architect

Dedicated to advancing autonomous, high-velocity, and safe enterprise development on Infor ERP LN and Infor LN Studio.
