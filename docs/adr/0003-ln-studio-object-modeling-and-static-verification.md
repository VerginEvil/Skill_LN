# ADR 0003: LN Studio Object Modeling, SCM Guardrails & Static Verification Engine

- **Status**: Accepted
- **Date**: 2026-10-22
- **Spec**: [`docs/SPEC_LN_STUDIO_OBJECT_AND_VALIDATION.md`](../SPEC_LN_STUDIO_OBJECT_AND_VALIDATION.md)
- **Work Roster**: [`Tickets.md`](../../Tickets.md) (Tickets 01 through 06)
- **Prior ADRs**:
  - [`docs/adr/0001-plan-skill-update-and-coding-best-practices.md`](0001-plan-skill-update-and-coding-best-practices.md)
  - [`docs/adr/0002-ln-studio-skill-self-contained-toolchain.md`](0002-ln-studio-skill-self-contained-toolchain.md)

---

## Context & Motivation

Following the self-contained toolchain reorganization in ADR 0002, practical usage against real-world enterprise workspaces (such as `SCS_TST\dev_natt_1107-1 [EXTce01107]`) exposed critical gaps:
1. **Accidental SCM Overwriting**: Checked-in components have the OS Read-Only flag set. Generating or injecting code blindly caused `PermissionError` or corrupted working copies.
2. **Incomplete SCM Tracking**: `admin_sync.py` only monitored `.tbl` and `.ses`, deleting `.mnu` and `.rpt` during synchronization.
3. **Data Dictionary Fidelity Gaps**: Native datatypes were misaligned with LN Studio's Ecore metamodel (`Date`, `Numeric/Amount`, and `Enum`), and column label naming did not match the Workbench convention `<package><table_code>.<column>` (e.g. `txtxcmg010.user`).
4. **Missing Component Archetypes**: Only single-occurrence tables and list sessions were supported; Multi-Main-Table (MMT) Controllers, Satellite sessions, Form Commands, Libraries (DLL, `ess`, `est`), and Menus were absent.
5. **Lack of Offline Static Verification**: Developers and AI agents had to trigger slow Windows UI builds (F5 + Ctrl+B) to detect simple typos in section headers, unbalanced blocks, or broken cross-references.

---

## Decisions Recorded

### 1. Clean Skill Seam Alignment
- **`ln_studio_skill`** owns the Eclipse RCP workspace toolchain: explicit workspace and activity path resolution, Human-in-the-loop SCM Read-Only guardrails, 12-extension `.admin` cache synchronization, high-fidelity XML generation, 4-layer static activity validation (`validate` & `--fix`), and offline 4GL syntax/completion inspection (`check-script`).
- **`erp-ln-progguide`** owns 4GL programming guides, DAL 2 business logic patterns, SQL optimization recipes, and Cloud tenant governor limits. 4GL coding tutorials are not duplicated in `ln_studio_skill`.

### 2. Human-in-the-Loop SCM & Read-Only Guardrails
- Checked-in components on disk have the OS Read-Only attribute set.
- All generators and script synchronizers call `assert_file_writable` before modifying or injecting files. If a file is Read-Only, execution aborts with `ReadOnlyComponentError`, instructing the developer to check out the component in the Eclipse workbench.
- The toolchain **never** automatically unsets the OS Read-Only flag and **never** attempts unauthorized remote SCM checkouts outside Eclipse JCA.

### 3. Expanded 12-Extension `.admin` Synchronization
- `MANAGED_EXTENSIONS` expanded to all 12 LN Studio component extensions:
  `.tbl`, `.ses`, `.lib`, `.dmn`, `.lbl`, `.mnu`, `.rpt`, `.rptdsrc`, `.msg`, `.que`, `.add`, `.fun`.
- `admin_sync.py` and `AdminSyncHelper` register all on-disk components and only remove obsolete entries matching these 12 extensions.

### 4. High-Fidelity Object Modeling
- **Ecore Native Datatypes & Facets**: Aligned with LN Studio's Ecore model: `1` (Byte), `2` (Double/Float), `3` (Long/Integer), `5` (Numeric/Amount), `6` (String/Multibyte), `7` (Enumeration/Boolean), `9` (Date), `14` (UTC DateTime).
- **Column Labels**: Follows the Workbench convention `<package><table_code>.<column>` (e.g. `txtxcmg010.user`).
- **Multi-Archetype Sessions**: `<DR_Controller>` generator supports `maintain_list`, `maintain_details`, `mmt_controller` (with `<ControllerSatelliteRelationship>`), `satellite`, `display`, `process`, and `print`, plus `<FormCommand>` declarations.
- **Libraries**: `<DR_Module>` generator supports General DLL (`<pkg>/library/<mod>/`, `sourceType=6`), Session Extension (`<pkg>/library/ess/`, `sourceType=8`), and Table Extension (`<pkg>/library/est/`, `sourceType=6` with official `#context_on` / `#context_off` hook blocks).
- **Menus**: `<DR_Menu>` generator creates menu XML with `<MenuChoice>` entries and matching `.lbl` files.

### 5. Deterministic Studio Dictionary Extraction
- Extractor `extract_studio_dictionaries.py` reflectively extracts official constants from pinned Studio 10.8 JARs (`lnstudio_commonui.jar`, `lnstudio_commoncore.jar`, `com.infor.ln.studio.common.ui_*.jar`):
  - `KEYWORDS` (80 keywords)
  - `SQL_KEYWORDS` (92 SQL keywords)
  - `PROGRAM_SECTIONS` (9 program section headers)
  - `SUB_SECTIONS` (43 subsections)
  - `CHOICE_SECTIONS` (60 choice sections)
  - `REPORT_SECTIONS` (9 report sections)
  - `PREDEFINED_VARIABLES` (176 variables)
  - `STANDARD_DEFINES` (49 defines)
  - `DAL_OBJECT_HOOKS` (15 hooks)
  - `DAL_FIELD_HOOK_SUFFIXES` (10 hooks with return types, arguments, and default bodies)
  - `TEMPLATES` (12 code templates)
- Materialized in `ln_studio_skill/references/studio_syntax_completion.json` and `STUDIO_SYNTAX_COMPLETION.md`.

### 6. Four-Layer Activity Validation (`validate` & `check-script`)
- **Layer 1 (SCM & Activity State)**: Compares disk files against `.admin` entries across all 12 extensions, reports untracked files or missing disk files, and audits Read-Only consistency.
- **Layer 2 (XML Structure & Ecore Compliance)**: Verifies root tags, native datatypes, facets, and Session `<FormGroup>` hierarchy tree integrity (detects orphan parents, broken children, and cyclic pointer loops).
- **Layer 3 (Cross-Object References)**: Verifies that `<descriptionReference>` and `<fieldLabel>` tags resolve to local `.lbl` files (or standard LN packages), Session form fields match Table columns, and Table index columns exist.
- **Layer 4 (Static 4GL Script & Symbol Verification)**: Runs `check_4gl_script.py` across embedded `<expression>` blocks, flags unrecognized/misspelled section headers, checks block balance (`select`/`endselect`, `if`/`endif`, `on case`/`endcase`, `for`/`endfor`, `while`/`endwhile`, `repeat`/`until`, `#context_on`/`#context_off`, `{`/`}`), and cross-checks DAL property hooks against Table columns.
- **Safe `--fix` Mode**: Auto-generates missing `.lbl` files and synchronizes `.admin` registration while strictly preserving Read-Only files.

### 7. Unified CLI Orchestrator
- `ln_component_builder.py` provides 14 unified subcommands: `workspace`, `table`, `session`, `domain`, `library`, `menu`, `component`, `inject`, `extract`, `check-script`, `validate`, `sync-admin`, `diagnose`, `build`, and `pipeline`.

---

## Validation & Verification

- **Unit Test Suite**: 86 total tests passing with 0 failures (`python -m unittest discover -s ln_studio_skill/tools/tests`).
- **Live Reference Workspace Verification**: Validated against `C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST\dev_natt_1107-1 [EXTce01107]`:
  - 85 component files scanned.
  - Successfully identified 14 untracked components in `.admin` (e.g. `txcmg.clor01.lbl` through `txcmg.clor07.lbl`, `txessacr2520m0.lib`).
  - Successfully identified 3 missing label references (`txprocess`, `txselect`, `txgld011.ttyp`).
  - 100% clean pass on Layer 4 static 4GL inspection across all 13 production scripts.
