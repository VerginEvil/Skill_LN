---
name: ln_studio_skill
description: "Infor LN Studio Assistant Skill for developing Infor LN applications, generating tables/sessions, synchronizing 4GL source code, and diagnosing compiler errors."
---

# Infor LN Studio Assistant Skill

The **Infor LN Studio Assistant Skill** empowers engineers and AI agents to develop applications on
**Infor ERP LN** with **Infor LN Studio 10.8 build 0640 (April 2026 tree)** — an Eclipse RCP,
activity-based development environment with SCM — with high speed and zero manual UI clicking.

Live-workspace scanning is explicitly permitted: reading installation plugins, workspace metadata,
SCM caches (`.admin`), and problem markers (`.markers`) in the example workspace, including real
activity names such as `dev_natt_01103`, `dev_natt_01105`, `dev_natt_01102`.

> Copying this folder installs a working skill: knowledge (`references/`, `templates/`, `SKILL.md`)
> plus executables (`tools/`, `scripts/`). All commands below use `<skill_dir>` for the copied
> skill root (e.g. `~/.claude/skills/ln_studio_skill` or the repo path `ln_studio_skill`).

---

## How to answer questions (token-efficient workflow)

Never read folders blindly. Use this order:

1. **Know what to run** -> check the task-to-entry-point table below.
2. **Free-text "how do I ..." question** (connectivity, clean/recover activity, SCM, problem
   markers, breakpoints, wizards, editors, views) -> run search first, then Read only the hit:
   ```
   python <skill_dir>/scripts/search.py <terms> [--dir studio_guide|all] [--group substr] [--regex PATTERN] [--max 25]
   python <skill_dir>/scripts/search.py --list-groups        # topic folders + page counts
   ```
   Output is `path | title` headers with ranked `line: snippet` hits. Read only promising files.
3. **Known topic name** -> grep `references/STUDIO_INDEX.md` for the chapter/section, or check
   `index/INDEX.tsv` (every page: path TAB title). Then Read only that file.
4. **Code generation / sync / build** -> run the closed-loop recipe (author schema, generate, sync
   SCM cache, build, diagnose, fix, repeat). Links between pages are relative Markdown links.

## Task-to-entry-point table

| Task | Entry point |
|---|---|
| Set up connectivity and workspace (installation, workspace selection, JCA connectivity) | Guide: `references/studio_guide/ch02_installation_and_configuration.md`; resolver: `python <skill_dir>/tools/ln_workspace_manager.py --list-workspaces` / `--list-activities` |
| Understand Activity lifecycle (open, clean, recover, reassign, end, link run configurations) | Guide: `references/studio_guide/ch03_activity_based_development.md` (`Cleaning an activity`, `Recovering an activity`, `Reassigning an activity`, `Linking run configurations to an activity`); dialogs: `references/studio_guide/ch07_wizards_and_dialogs.md` |
| Decide when SCM applies (project VRC vs application) and which CM actions to use | Guide: `references/studio_guide/ch03_activity_based_development.md` (`Usage of SCM`, `Activating SCM for a project VRC`, `Activating SCM for an application`, `CM actions`) |
| Validate authoring schema | `python <skill_dir>/tools/ln_component_builder.py table --spec <schema> --dry-run` or `python <skill_dir>/tools/ln_schema_parser.py <schema.yaml>` |
| Generate table / domain / label metadata | `python <skill_dir>/tools/ln_component_builder.py table --spec <schema> --activity "<act>" [--dry-run]` |
| Generate session / form metadata | `python <skill_dir>/tools/ln_component_builder.py session --spec <schema> --activity "<act>" [--dry-run]` |
| Generate table + session together | `python <skill_dir>/tools/ln_component_builder.py component --spec <schema> --activity "<act>" [--dry-run]` |
| Inject 4GL source into workspace metadata (repo stays source of truth) | `python <skill_dir>/tools/ln_component_builder.py inject --source <f.dal> --target <f.tbl>` |
| Extract 4GL source back out of workspace metadata | `python <skill_dir>/tools/ln_component_builder.py extract --source <f.tbl> --output <f.dal>` |
| Resynchronize SCM cache after generating files (fix phantom missing components) | `python <skill_dir>/tools/ln_component_builder.py sync-admin --activity "<act>"` (guide background: ch03 SCM usage) |
| Read line-accurate compiler diagnostics | `python <skill_dir>/tools/ln_component_builder.py diagnose --activity "<act>" [--errors-only]` |
| Trigger Eclipse refresh + build, then check diagnostics | `python <skill_dir>/tools/ln_component_builder.py build --activity "<act>"` |
| Run full pipeline (validate, generate, sync, build) | `python <skill_dir>/tools/ln_component_builder.py pipeline --spec <schema> --activity "<act>" [--dry-run] [--skip-build]` |
| Verify components; handle warnings vs errors (what blocks a build) | Guide: `references/studio_guide/ch04_development_procedure.md` (`Verifying software components`, `Handling warnings`, `Identifying problems in your code`); dialogs: ch07 `Verify Software Components` |
| Run and debug sessions (suspend, resume, step, inspect, breakpoints, expressions) | Guide: `references/studio_guide/ch04_development_procedure.md` (`Running and debugging software components`, `Using breakpoints`); views: `references/studio_guide/ch11_views.md` (`Breakpoints view`, `Debug view`, `Variables view`, `Expressions view`) |
| Pick the right wizard or dialog (activity, component, domain, label, function, browse) | Guide: `references/studio_guide/ch07_wizards_and_dialogs.md` (`Create a New Infor LN Software Component wizard`, `Creating a domain/label/session/table`, browse/select dialogs) |
| Edit metadata safely (multipage editors, script editor assistance/navigation/limits) | Guides: `references/studio_guide/ch08_multipage_editors.md` (per-component editors, tabs, DAL handling); `references/studio_guide/ch09_script_editor.md` (markers, code assist, comments, folding, open declaration) |
| Check documented limitations before filing issues | Guide: `references/studio_guide/ch06_studio_limitations.md` (general, Script Editor, CM, build, debugger, Web UI) |
| Navigate workbench (perspectives, views, project server, delivery) | Guides: `references/studio_guide/ch10_perspectives.md`; `references/studio_guide/ch11_views.md` (`Activity Explorer`, `Problems`, `Verify Components`); `references/studio_guide/ch12_project_server.md` (projects, delivery activities, solutions) |
| Search the Studio guide | `python <skill_dir>/scripts/search.py <terms> [--dir studio_guide|all]` |
| Validate the skill (links + index) | `python <skill_dir>/tools/validate_skill.py --skill-dir <skill_dir>` |
| Regenerate the every-page index | `python <skill_dir>/tools/generate_indices.py --skill-dir <skill_dir>` |
| Re-ingest the Studio guide from source text | `python <skill_dir>/tools/convert_txt_studio_guide.py --src <guide.txt> --out-dir <skill_dir>/references/studio_guide --index <skill_dir>/references/STUDIO_INDEX.md` |

---

## Standard Workflows & Recipes

### Recipe 1: Create a New Table and Session from Scratch

1. **Author the Schema YAML:**
   Create a YAML definition following [`templates/table_schema_sample.yaml`](templates/table_schema_sample.yaml):
   ```yaml
   table:
     code: txptc300
     description: Inspection Defect Logs
   fields:
     - name: logn
       domain: tcpono
       mandatory: true
       default: '$__unique'
     - name: item
       domain: tcitcm
       mandatory: true
   indices:
     - id: 1
       columns: [logn]
       primary_key: true
   session:
     code: txptc1300m000
   ```

2. **Generate All XML Metadata:**
   ```bash
   python <skill_dir>/tools/ln_component_builder.py component --spec schema.yaml --activity "dev_natt_01103"
   ```

3. **Sync Eclipse SCM State:**
   ```bash
   python <skill_dir>/tools/ln_component_builder.py sync-admin --activity "dev_natt_01103"
   ```

4. **Compile & Verify:**
   ```bash
   python <skill_dir>/tools/ln_component_builder.py build --activity "dev_natt_01103"
   ```

Background: workspace/activity setup is in
[`references/studio_guide/ch02_installation_and_configuration.md`](references/studio_guide/ch02_installation_and_configuration.md)
and the Activity/SCM lifecycle in
[`references/studio_guide/ch03_activity_based_development.md`](references/studio_guide/ch03_activity_based_development.md).

---

### Recipe 2: Implement Business Rules in DAL 2

1. **Write Clean 4GL in Git Repository:**
   Save your DAL logic in `scripts/dal/<table_code>.dal`:
   ```baan
   #include <bic_dal2>
   table ttxptc300

   function extern long before.save.object(long i.mode)
   {
   |#dev_natt_01103.sn
       if isspace(txptc300.item) then
           dal.set.error.message("@item.is.mandatory")
           return(DALHOOKERROR)
       endif
       return(0)
   |#dev_natt_01103.en
   }
   ```

2. **Inject into Workspace XML:**
   ```bash
   python <skill_dir>/tools/ln_component_builder.py inject --source scripts/dal/txptc300.dal --target "path/to/txptc300.tbl"
   ```

3. **Trigger Compilation & Inspect Output:**
   ```bash
   python <skill_dir>/tools/ln_component_builder.py build --activity "dev_natt_01103"
   ```

Background: verification and warning handling are in
[`references/studio_guide/ch04_development_procedure.md`](references/studio_guide/ch04_development_procedure.md);
editor behavior (multipage Session/Table editors, script assist) is in
[`references/studio_guide/ch08_multipage_editors.md`](references/studio_guide/ch08_multipage_editors.md) and
[`references/studio_guide/ch09_script_editor.md`](references/studio_guide/ch09_script_editor.md).

---

### Recipe 3: Closed-Loop Autonomous Debugging

When an AI agent modifies code and receives compiler errors:
```bash
python <skill_dir>/tools/ln_component_builder.py diagnose --activity "dev_natt_01103" --errors-only
```
Output:
```
=== Eclipse Diagnostics: dev_natt_01103 [EXTce01103] ===
Errors: 1 | Warnings: 0
  [ERROR]   tx/table/ptc/txptc300.tbl:42
            Variable 'tcitcm' not declared
```
1. The agent inspects line 42 of the source file.
2. The agent corrects the syntax in `scripts/dal/txptc300.dal`.
3. The agent re-injects and re-builds.
4. The loop repeats until 0 errors are returned.

Background: `Identifying problems in your code` and the run/debug flow
(`Using breakpoints`, suspend/resume/step/inspect/expressions) are in
[`references/studio_guide/ch04_development_procedure.md`](references/studio_guide/ch04_development_procedure.md);
the Problems/Breakpoints/Debug views are in
[`references/studio_guide/ch11_views.md`](references/studio_guide/ch11_views.md).

---

## Layout

```
tools/                          Self-contained automation toolchain (.refs resolve from skill root):
  ln_component_builder.py         Master pipeline CLI (table|session|component|inject|extract|sync-admin|diagnose|build|pipeline)
  ln_schema_parser.py             Declarative authoring schema validator
  generate_ln_table.py            Table/Label/Domain XML generator
  generate_ln_session.py          Session & Form XML generator
  inject_ln_script.py             4GL bidirectional synchronizer
  admin_sync.py                   Eclipse SCM `.admin` cache synchronizer (+ lib/ Java helper)
  ln_error_reader.py              Binary `.markers` diagnostics reader
  ln_studio_bridge.py             Windows action bridge (F5 / Ctrl+B)
  ln_workspace_manager.py         Activity environment resolver (live-workspace scanning permitted)
  convert_txt_studio_guide.py     Studio guide ingester (stdlib only, deterministic)
  convert_chm.py / convert_pdf_interfaces.py / convert_txt_dev_tools.py   Shared converters
  generate_indices.py             Every-page index generator (also targets erp-ln-progguide)
  validate_skill.py               Skill validator (zero broken links / orphan entries)
  update_pipeline.py              Shared update pipeline
  lib/AdminSyncHelper.java + lnstudio_commoncore.jar   Java helper + binary library
  tests/ (+ fixtures/)            Relocated unit suite (regression)
scripts/search.py               Full-text search (stdlib only; --dir studio_guide|all; --group; --list-groups)
references/studio_guide/        12 ingested Application Guide chapters (full: ch01-ch04,ch07-ch09; summary: ch05,ch06,ch10-ch12)
references/STUDIO_INDEX.md      Master studio index (chapters -> sections, depth, Phase 2 boundary)
references/COMPONENT_XML_SCHEMA.md  Complete XML schema reference for `.tbl`, `.ses`, `.dmn`, `.lbl`
references/DAL2_HOOKS_GUIDE.md  Catalog of DAL 2 Object Hooks, Property Hooks, and Business Methods
references/UI_SCRIPT_GUIDE.md   Guide for UI Script sections, form commands, and zoom filters
templates/                      Authoring samples (table_schema_sample.yaml, dal2_template.dal, ui_script_template.cln)
index/INDEX.tsv                 Every page: path TAB title
```

## Studio guide navigation

| Task | Start at |
|---|---|
| Studio guide master index (all chapters + sections) | `references/STUDIO_INDEX.md` |
| Every page (jump from a known topic name) | `index/INDEX.tsv` |
| Installation, workspace, connectivity (full) | `references/studio_guide/ch02_installation_and_configuration.md` |
| Activity lifecycle + SCM: project VRC vs application, CM actions, clean/recover/reassign (full) | `references/studio_guide/ch03_activity_based_development.md` |
| Development procedure: verify, warnings vs errors, run/debug, breakpoints (full) | `references/studio_guide/ch04_development_procedure.md` |
| Wizards and dialogs: activity, component creation, domain/label/function, browse actions (full) | `references/studio_guide/ch07_wizards_and_dialogs.md` |
| Multipage editors per component (full) | `references/studio_guide/ch08_multipage_editors.md` |
| Script editor: assist, navigation, limitations (full) | `references/studio_guide/ch09_script_editor.md` |
| InContext modeling (summary) | `references/studio_guide/ch05_incontext_modeling.md` |
| Studio/debugger/Web UI limitations (summary) | `references/studio_guide/ch06_studio_limitations.md` |
| Perspectives (summary) | `references/studio_guide/ch10_perspectives.md` |
| Views incl. Activity Explorer, Problems, Verify Components (summary) | `references/studio_guide/ch11_views.md` |
| Project Server: projects, delivery, solutions (summary) | `references/studio_guide/ch12_project_server.md` |
| Studio overview and workbench orientation (full) | `references/studio_guide/ch01_studio_overview.md` |

Search first:
```bash
python <skill_dir>/scripts/search.py connectivity --dir studio_guide
python <skill_dir>/scripts/search.py "clean" "activity" --dir studio_guide
python <skill_dir>/scripts/search.py SCM --dir studio_guide
python <skill_dir>/scripts/search.py problem --dir studio_guide
python <skill_dir>/scripts/search.py breakpoints --dir studio_guide
```

Phase 2 boundary: the *Integration Development Guide* (business interfaces, BOD modeling, hook
reference, event publishing) is out of scope here and must not duplicate the extensibility
reference in `erp-ln-progguide`.

---

## References & Guides

- [`references/COMPONENT_XML_SCHEMA.md`](references/COMPONENT_XML_SCHEMA.md): Complete XML schema reference for `.tbl`, `.ses`, `.dmn`, and `.lbl`.
- [`references/DAL2_HOOKS_GUIDE.md`](references/DAL2_HOOKS_GUIDE.md): Catalog of DAL 2 Object Hooks, Property Hooks, and Business Methods.
- [`references/UI_SCRIPT_GUIDE.md`](references/UI_SCRIPT_GUIDE.md): Guide for UI Script sections, form commands, and zoom filters.
- [`references/STUDIO_INDEX.md`](references/STUDIO_INDEX.md): Master index of the 12 ingested Studio guide chapters.

---

## Coding Standards & Architectural Guardrails

When generating or reviewing Infor LN code via this Studio toolchain, AI agents and developers **must strictly adhere** to these rules (authoritative details live in `erp-ln-progguide` best practices):

1. **Cardinal Rule — Separation of Concerns (SoC)**:
   - **Never perform database modifications (`db.insert`, `db.update`, `db.delete`, `db.write`) or business validations directly in 4GL UI session scripts.**
   - UI scripts manage form presentation and flow only. All validations, defaults, and table mutations belong in DAL 2 or Table Extensions.
2. **DAL & Extension Hook Error Conventions**:
   - Signal failures with `dal.set.error.message("@<msg_code>")` and `return(DALHOOKERROR)` (or `false` for boolean hooks).
   - Maintain the safe `table.super()` signature pattern with `get.long.arg(1)` for optional `mode` handling.
   - **Never invoke interactive dialogs (`message()`, `ask.enum()`) inside DAL scripts or Table Extension hooks.**
   - **Never call `commit.transaction()` / `abort.transaction()` inside DAL 2 hooks.**
3. **Embedded Baan SQL & Transactions**:
   - `WHERE` clauses must use equality predicates on the **leading fields** of a defined index; never wrap indexed columns in functions.
   - Use `as set with 1 rows` for single-record lookups and `as prepared set` when mutating inside the loop; join parent/child in one statement (no N+1).
   - Bound writes between `db.retry.point()` and `commit.transaction()` / `abort.transaction()`; minimize `for update` lock windows and lock parent before child.
4. **Cloud Governance & Table Reconfiguration**:
   - Respect Cloud governor limits: max execution time `5,000 ms`, max file output `5 MB`; never call untrusted functions (`run.prog()`) or touch files outside sandboxed tenant storage.
   - Follow the two-step `crdd` procedure (Convert to Runtime -> Reconfigure Tables) with exclusive table access.

## Related Best Practices & References (`erp-ln-progguide`)

| Task | Start at |
|---|---|
| Extension hook lifecycles, CDF recipes, cloud limits | [01_extension_hooks_cookbook.md](../erp-ln-progguide/references/best_practices/01_extension_hooks_cookbook.md) |
| DAL 1 vs DAL 2, SoC rules, business methods | [02_dal_architecture_and_business_logic.md](../erp-ln-progguide/references/best_practices/02_dal_architecture_and_business_logic.md) |
| Baan SQL optimization & transaction boundaries | [03_sql_query_optimization_and_transactions.md](../erp-ln-progguide/references/best_practices/03_sql_query_optimization_and_transactions.md) |
| Domain design, tables & `crdd` reconfiguration | [04_data_model_and_domain_design.md](../erp-ln-progguide/references/best_practices/04_data_model_and_domain_design.md) |
| Session types 1-4 & MMT Controller/Satellite | [05_session_and_mmt_patterns.md](../erp-ln-progguide/references/best_practices/05_session_and_mmt_patterns.md) |
| Software components & DAL engine overview | [ch02_overview_of_software_components.md](../erp-ln-progguide/references/dev_tools/ch02_overview_of_software_components.md) |
| Data Dictionaries (Runtime vs Application) | [ch03_data_dictionaries.md](../erp-ln-progguide/references/dev_tools/ch03_data_dictionaries.md) |
| Development procedures (tables, sessions, MMT) | [ch05_software_development_procedures.md](../erp-ln-progguide/references/dev_tools/ch05_software_development_procedures.md) |
| Development Tools master chapter index | [DEV_TOOLS_INDEX.md](../erp-ln-progguide/references/DEV_TOOLS_INDEX.md) |
| Version & Release Management (VRC, SCM) | [ch07_version_and_release_management.md](../erp-ln-progguide/references/dev_tools/ch07_version_and_release_management.md) |
| PMC Maintenance (solutions, patches, FPs) | [ch08_ln_software_maintenance.md](../erp-ln-progguide/references/dev_tools/ch08_ln_software_maintenance.md) |
