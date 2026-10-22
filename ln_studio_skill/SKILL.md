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

---

## Task-to-Entry-Point Table

| Task | CLI Command / Entry Point |
|---|---|
| Inspect workspaces and activities | `python <skill_dir>/tools/ln_component_builder.py workspace --list` / `--activities` |
| Validate authoring schema | `python <skill_dir>/tools/ln_schema_parser.py <schema.yaml>` |
| Generate Table, Label & Domain XML | `python <skill_dir>/tools/ln_component_builder.py table --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Domain XML independently | `python <skill_dir>/tools/ln_component_builder.py domain --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Session XML (Maintain, MMT, Satellites) | `python <skill_dir>/tools/ln_component_builder.py session --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Library XML (DLL, `ess`, `est`) | `python <skill_dir>/tools/ln_component_builder.py library --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate Menu XML & Labels | `python <skill_dir>/tools/ln_component_builder.py menu --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Generate All Components in one pass | `python <skill_dir>/tools/ln_component_builder.py component --spec <schema.yaml> [--output-dir <path>] [--dry-run]` |
| Inject 4GL source into workspace XML | `python <skill_dir>/tools/ln_component_builder.py inject --source <f.dal> --target <f.tbl>` |
| Extract 4GL source from workspace XML | `python <skill_dir>/tools/ln_component_builder.py extract --source <f.tbl> --output <f.dal>` |
| Statically verify 4GL scripts (offline) | `python <skill_dir>/tools/ln_component_builder.py check-script <script_or_xml_file> [--strict] [--json]` |
| Run 4-Layer Activity Validation | `python <skill_dir>/tools/ln_component_builder.py validate [<activity_path>] [--strict] [--fix] [--json]` |
| Synchronize Activity `.admin` SCM Cache | `python <skill_dir>/tools/ln_component_builder.py sync-admin --activity "<act>"` |
| Read Eclipse problem markers (`.markers`) | `python <skill_dir>/tools/ln_component_builder.py diagnose --activity "<act>" [--errors-only]` |
| Trigger Eclipse build bridge (F5 + Ctrl+B) | `python <skill_dir>/tools/ln_component_builder.py build --activity "<act>"` |
| Full Autonomous Pipeline (Gen -> Sync -> Validate -> Build) | `python <skill_dir>/tools/ln_component_builder.py pipeline --spec <schema.yaml> [--output-dir <path>] [--auto-fix] [--skip-build]` |

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

## Toolchain & Reference Layout

```
tools/                          Self-contained automation toolchain:
  ln_component_builder.py         Master CLI orchestrator (14 subcommands)
  ln_schema_parser.py             Declarative authoring schema validator (multi-table & domains)
  generate_ln_table.py            Table, Label & Domain XML generator (Ecore facets & conventions)
  generate_ln_domain.py           Standalone & Spec-based Domain generator (.dmn & enums)
  generate_ln_session.py          Multi-archetype Session generator (Maintain, MMT, Satellites, Commands)
  generate_ln_library.py          Library generator (DLL, ess, est with #context_on/#context_off)
  generate_ln_menu.py             Menu generator (<DR_Menu> XML & .lbl)
  inject_ln_script.py             Bidirectional 4GL synchronizer with Read-Only guardrails
  admin_sync.py                   12-extension SCM .admin cache synchronizer (+ Java helper)
  scm_guardrails.py               OS Read-Only SCM protection module
  check_4gl_script.py             Static 4GL syntax, completion & block balance inspector
  validate_ln_activity.py         Four-layer activity validator & safe --fix engine
  extract_studio_dictionaries.py  LN Studio 10.8 reflection extractor for keywords, sections, hooks
  ln_error_reader.py              Binary .markers problem diagnostics reader
  ln_studio_bridge.py             Windows action bridge (F5 refresh / Ctrl+B build)
  ln_workspace_manager.py         Pinned Studio & workspace environment resolver
  tests/                          Comprehensive unit test suite (86+ tests)
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
