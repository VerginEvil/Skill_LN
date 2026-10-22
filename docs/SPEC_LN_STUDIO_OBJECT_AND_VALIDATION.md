# Specification: LN Studio Object Modeling, SCM Guardrails & Static Verification Engine

- **Status**: `ready-for-agent`

## Problem Statement

Engineers and AI coding agents developing Infor ERP LN applications in Infor LN Studio (Eclipse RCP Workbench with Activity-based development and SCM) face several structural gaps in the current Studio assistant skill:

1. **Blurred Boundary with the Programmer's Guide Skill**: The Studio skill still duplicates 4GL coding instructions instead of focusing on its unique responsibility — creating and validating LN Studio XML objects, enforcing Eclipse Workspace and SCM Cache (`.admin`) rules, and bridging local Activity metadata with the Workbench.
2. **Incomplete Object Coverage & XML Drift**: Real LN Studio Activities contain diverse software components — Tables, Domains (enumerated, string, numeric, date, amount), Labels, Multi-Main Table (MMT) Controllers, Satellites, Overview/Detail Sessions with Form Commands, Libraries (general DLLs, Session Extensions, Table Extensions), Menus, and Reports. However, the existing generator only produces basic tables, enum domains, and a single list-window session type, and suffers from XML fidelity bugs (such as generating `txt<table_code>.<column>` instead of `tx<table_code>.<column>` for column label references and misassigning `nativeDatatype` codes for Date and Amount fields).
3. **Destructive SCM Cache Synchronization & Missing Read-Only Protection**: Checked-in components inside an Activity are marked Read-Only on disk until explicitly checked out in the LN Studio Workbench. The current tools do not verify Read-Only or check-out state before overwriting files, risking silent corruption of un-checked-out objects. Worse, the SCM Cache (`.admin`) synchronizer only recognizes five file extensions and deletes valid Menu, Report, Report Data Source, Message, Question, and Function entries from `.admin` during a scan.
4. **Lack of Pre-Compile Object & Cross-Reference Validation**: There is no offline validator to verify XML structure, `<FormGroup>` tree integrity, `<application>` and `<versionID>` alignment, or cross-object references (missing Labels, mismatched Table columns in Session forms, invalid index/relationship columns) before triggering a remote JCA/Bshell build.
5. **Untapped LN Studio Syntax Highlighting & Code Completion Metadata**: The local LN Studio installation contains official 3GL/4GL lexer/parser libraries, syntax highlighting token tables, code completion dictionaries (program sections, subsections, choice sections, SQL keywords, predefined variables, standard defines, DAL object hooks), and script templates, none of which are currently leveraged to statically verify 4GL scripts and their bindings to XML objects before compilation.
6. **Hardcoded Workspace Coupling**: The workspace manager currently assumes a fixed default workspace root and default activity instead of pinning only the LN Studio installation while requiring the caller to explicitly specify the target Workspace or Activity path per invocation.

## Solution

Transform the LN Studio assistant skill into a dedicated **Object Modeling, SCM Guardrail & Static Verification Engine** that complements (rather than duplicates) the 4GL programmer's-guide skill:

1. **Clean Skill Seam & Delegation**: Focus the Studio skill on LN Studio XML object lifecycle, SCM/Activity rules, and static/compiler verification, while delegating 4GL language syntax, DAL 2 business logic patterns, Extension Hook recipes, and Baan SQL optimization to the programmer's-guide skill.
2. **Expanded Domain Model & High-Fidelity XML Generators**: Extend the declarative authoring schema and component builder CLI to generate and update Tables, Domains (all native datatypes), Labels (with accurate LN Studio naming conventions), Sessions (Maintain List/Overview, Maintain Details, MMT Controller with Satellites, Satellite, Display, Process/Print, and Form Commands), Libraries (General DLL, Session Extension, Table Extension with `#context_on`/`#context_off` blocks), and Menus, while preserving backward compatibility with existing single-table schemas.
3. **Human-in-the-Loop SCM & Read-Only Guardrails**: Enforce strict Read-Only check-out protection across all write and injection operations (failing fast with clear instructions to check out the component in Eclipse first), and expand the `.admin` SCM Cache synchronizer to preserve and register all LN Studio component types (including Menus, Reports, Report Data Sources, Messages, Questions, Functions, and Additional Files).
4. **Pinned Studio Installation & Explicit Workspace Resolution**: Configure the pinned LN Studio installation path as the sole default path in the workspace resolver, removing hardcoded default workspace assumptions so callers explicitly supply (or run within) the target Workspace or Activity path.
5. **Four-Layer Object, Cross-Reference & 4GL Syntax/Completion Validator**: Extract the official Syntax Highlighting, Code Completion, and Ecore validation metadata from the pinned LN Studio installation and combine it with the 3GL/4GL scanner/parser to provide a single `validate` (and `check-script`) workflow covering:
   - Layer 1: SCM Cache (`.admin`), Read-Only check-out state, and Activity `<application>` / `<versionID>` consistency.
   - Layer 2: XML schema fidelity, `nativeDatatype` and `Facet` compliance, and Session `<FormGroup>` hierarchy integrity.
   - Layer 3: Cross-object reference integrity across Tables, Sessions, Domains, Labels, Libraries, and Menus.
   - Layer 4: Static 4GL syntax and code-completion validation (valid sections, subsections, choice sections, SQL keywords, balanced control/context blocks, and object-to-script hook/field/command alignment), plus an optional safe `--fix` mode to synthesize missing Labels and synchronize `.admin`.

## User Stories

1. As an LN developer, I want the Studio skill and the programmer's-guide skill to have a clear division of responsibility, so that the Studio skill handles XML objects, SCM state, and verification while the programmer's-guide skill handles 4GL coding patterns without conflicting guidance.
2. As an LN developer, I want the workspace resolver to default only to the pinned LN Studio installation path and require an explicit Workspace or Activity path at runtime, so that commands never accidentally read or write the wrong Workspace.
3. As an LN developer, I want any tool that modifies or injects into an existing Activity file to check the operating system Read-Only attribute and SCM check-out status first, so that un-checked-out components are never overwritten on disk.
4. As an LN developer, I want a clear actionable error message when a target file is Read-Only, so that I know which component to check out in the LN Studio Workbench before re-running the tool.
5. As an LN developer, I want the SCM Cache (`.admin`) synchronizer to recognize all LN Studio component file extensions (Tables, Sessions, Libraries, Domains, Labels, Menus, Reports, Report Data Sources, Messages, Questions, Functions, and Additional Files), so that syncing `.admin` never strips Menus or Reports from my Activity.
6. As an LN developer, I want column description references in generated Tables to follow the exact LN Studio convention (`tx<table_code>.<column>`), so that generated Tables match Workbench-authored Tables and link cleanly to their Label files.
7. As an LN developer, I want Table and Domain generation to support the full set of LN Studio `nativeDatatype` codes (including Byte, Float/Double, Long/Integer, Amount/Numeric, String, Enumeration, Date, and UTC DateTime) with accurate Facets, alignments, and conversions, so that financial, date, and text fields open without error in Multipage Editors.
8. As an LN developer, I want to define and generate standalone or bundled Domains (enumerated, string, numeric, date, and amount), so that custom fields do not fall back to generic string facets.
9. As an LN developer, I want to generate Maintain List (Overview), Maintain Details, Display, and Process/Print Sessions from a declarative specification, so that all standard session archetypes can be scaffolded without manual wizard clicking.
10. As an LN developer, I want to generate Multi-Main Table (MMT) Controller Sessions and linked Satellite Sessions from a declarative specification, so that complex header/line interfaces are wired correctly in XML.
11. As an LN developer, I want to declare custom Form Commands (`<UserCommand>`) on a Session and have both the Session XML and its associated Label generated automatically, so that toolbar actions and session extensions bind without manual form editing.
12. As an LN developer, I want to generate General DLL Libraries, Session Extension Libraries (`ess`), and Table Extension Libraries (`est`) with LN Studio `#context_on` / `#context_off` hook markers and official script templates, so that new libraries and extensions compile cleanly.
13. As an LN developer, I want to generate Menu components (`<DR_Menu>`) with ordered `<MenuChoice>` entries linking to Sessions or sub-Menus, so that new sessions can be attached to application navigation declaratively.
14. As an LN developer, I want existing single-table YAML specifications to continue working without modification, so that backward compatibility with prior automation recipes is preserved.
15. As an LN developer, I want a single `validate` command that audits an Activity (or individual component) in read-only mode by default, so that I can inspect all SCM, XML, cross-reference, and 4GL script issues safely before compiling.
16. As an LN developer, I want the validator to detect untracked component files on disk that are missing from `.admin` as well as orphaned `.admin` entries whose files no longer exist, so that Eclipse SCM state stays healthy.
17. As an LN developer, I want the validator to verify that every XML component in an Activity carries the `<application>` project code and `<versionID>` VRC of that Activity, so that copy-pasted components from other activities are caught immediately.
18. As an LN developer, I want the validator to check XML tag structure, required `<Attachment>` elements, column/index positions, and `<FormGroup>` parent/child/sibling tree pointers in Sessions, so that malformed XML never crashes LN Studio Multipage Editors.
19. As an LN developer, I want the validator to check cross-object references across the Activity — verifying that every `<descriptionReference>`, `<fieldLabel>`, and enumeration constant points to an existing Label, every Session `<FormField>` maps to a valid Table column or declared script variable, and every `<IndexColumn>` or `<TableRelationshipColumn>` maps to a defined Table column — so that missing references are caught before build time.
20. As an LN developer, I want the skill to extract and index LN Studio's built-in Syntax Highlighting and Code Completion dictionaries (`KEYWORDS`, `PROGRAM_SECTIONS`, `SUB_SECTIONS`, `CHOICE_SECTIONS`, `REPORT_SECTIONS`, `SQL_KEYWORDS`, `PREDEFINED_VARIABLES`, `STANDARD_DEFINES`, `DAL_OBJECT_HOOKS`, and `ScriptTemplates`), so that both the static checker and AI agents validate against the exact vocabulary of LN Studio 10.8 build 0640.
21. As an LN developer, I want a static 4GL script inspector (invoked standalone via `check-script` or as part of `validate`) that uses LN Studio's 3GL/4GL scanner/parser and completion dictionaries to flag misspelled section headers, invalid choice/subsection names, and unclosed blocks (`select`/`endselect`, `if`/`endif`, `case`/`endcase`, `for`/`endfor`, `while`/`endwhile`, `#context_on`/`#context_off`), so that syntax mistakes are caught offline in milliseconds.
22. As an LN developer, I want the static inspector to cross-check 4GL scripts against their owning XML Objects — verifying that `field.<name>:` sections in UI scripts match `<FormField>` entries or script variables, `choice.<name>:` sections match enabled `<StandardCommand>` or `<UserCommand>` entries, DAL/Table Extension property hooks (`<table.column>.check`, `<table.column>.is.valid`, `<table.column>.update`, etc.) match actual `<Column>` names in `.tbl`, and Session Extension command hooks (`function.<cmd>.is.enabled`, `function.<cmd>.after.command`) follow valid hook conventions — so that object-to-code mismatches are eliminated.
23. As an LN developer, I want an optional `--fix` mode on `validate` that performs safe, non-destructive repairs — automatically generating missing `.lbl` files for declared references and synchronizing `.admin` for untracked disk files while never touching Read-Only files — so that routine metadata bookkeeping is automated safely.
24. As an AI agent, I want updated XML schema references covering Tables, Sessions (Overview, Details, MMT Controller, Satellite), Domains, Labels, Libraries (DLL, `ess`, `est`), Menus, and Reports/Report Data Sources, so that I can inspect or author any LN Studio component accurately.
25. As an AI agent, I want the Studio skill definition and agent rules to reflect the explicit `--workspace` / `--activity-path` requirement, Read-Only check-out workflow, new object generators, and pre-build `validate` step, so that I follow a reliable closed-loop workflow on every task.
26. As a repository maintainer, I want all new reference guides and syntax/completion catalogs indexed in the skill's full-text search and every-page index, and verified by the skill validator with zero broken links, so that discovery remains fast and token-efficient.
27. As a skill consumer, I want the updated skill synchronized to both the repository skill folder and the active agent configuration skill directory, so that improvements take effect immediately in live sessions.

## Implementation Decisions

### 1. Skill Seam & Responsibility Boundary
- The Studio skill owns the **LN Studio Object, Workspace/SCM, and Verification domain**: Eclipse Workspace/Activity resolution, Human-in-the-loop SCM and Read-Only guardrails, `.admin` cache synchronization, declarative XML generation/editing, offline 4GL syntax/completion and cross-object validation, and Eclipse `.markers` compiler diagnostics.
- The programmer's-guide skill remains the single authoritative source for **4GL language semantics, DAL 2 architecture, Extension Hook lifecycles, and Embedded Baan SQL rules**. Duplicated 4GL tutorials inside the Studio skill are replaced with concise cross-check rules and direct task links into the programmer's-guide skill.

### 2. Pinned Studio Path & Explicit Workspace Resolution
- The workspace resolver stores the pinned LN Studio installation path as its built-in default so the toolchain can always locate LN Studio plugin JARs (`lnstudio_commoncore.jar`, `lnstudio_commonui.jar`, `fourglstudio_core.jar`, `threegl_scanner.jar`, `threegl_parser.jar`, `mocca_runtime.jar`).
- Hardcoded default workspace roots and persistent `default_activity` fallbacks are removed from the execution path. Every workspace-targeted CLI command requires an explicit `--workspace` or `--activity` / `--activity-path` argument (or auto-detects only when the current working directory is already inside a valid Activity or Workspace directory), failing fast with a clear usage error when omitted.

### 3. Human-in-the-Loop SCM & Read-Only Protection
- Before any generator or script synchronizer overwrites an existing file on disk, a centralized guardrail checks whether the file has the OS Read-Only attribute set (`IsReadOnly`) or is marked checked-in (`isCheckedOut=false` and `isCreated=false`) in `.admin`.
- If a file is Read-Only, the tool aborts the write immediately with a non-zero exit code and outputs a clear human-in-the-loop instruction naming the locked file and telling the developer to perform **Check-out** in LN Studio (Eclipse) before retrying. Tools never clear the Read-Only attribute on existing checked-in files.
- The `.admin` SCM Cache synchronizer expands its managed component set to cover all LN Studio component extensions: `.tbl`, `.ses`, `.lib`, `.dmn`, `.lbl`, `.mnu`, `.rpt`, `.rptdsrc`, `.msg`, `.que`, `.add`, and `.fun`. Existing `.admin` entries for any of these extensions are preserved during `sync-admin`.

### 4. Expanded Declarative Domain Model & XML Generators
- The declarative authoring schema is modeled as a normalized domain structure that supports both **multi-component specifications** and **legacy single-table specifications** (backward-compatible).
- Prototype schema shape encoding the expanded domain model:
  ```yaml
  version_id: B61O_a_ext
  application: EXTce01107

  domains:
    - name: txcmg.clor
      description: Collector Name
      type: enum          # enum | string | long | integer | double | amount | date | utc | bool
      length: 8
      enums:
        - { name: z0, description: Z0, position: 1, label_code: txcmg.clor001 }

  tables:                 # (also accepts legacy top-level 'table', 'fields', 'indices', 'references')
    - code: txcmg010
      description: Select Invoice for Billing Batches
      fields:
        - { name: user, domain: tfgld.user, type: string, length: 16, mandatory: true, description: User }
        - { name: docd, domain: tfgld.date, type: date, mandatory: true, description: Document Date }
        - { name: amnt, domain: tfgld.amnt, type: amount, length: 19, description: Amount }
      indices:
        - { id: 1, columns: [user], primary_key: true, unique: true }
      references: []

  sessions:               # (also accepts legacy top-level 'session')
    - code: txcmg0110m100
      description: Billing Batch MMT Controller
      type: mmt_controller  # maintain_list | maintain_details | mmt_controller | satellite | display | process | print
      table: txcmg011
      satellites: [txcmg0510m000, txcmg0512m000]
      form_commands:
        - { name: exec.user.0, function: generate.billing, label_code: txcmg0110m100.cmd1, description: Generate Billing }

  libraries:
    - code: txibddllitem01
      module: ibd
      type: dll             # dll | session_extension | table_extension
      target: ""            # target session/table code when type is session_extension (ess) or table_extension (est)
      description: Dll Gen Item Code

  menus:
    - code: txgld0000m001
      module: gld
      description: Enhancements
      choices:
        - { position: 10, type: session, target: txcmg9000m000, description: Withholding Tax Parameter }
  ```
- **Data Dictionary & XML Fidelity Fixes**:
  - Column `<descriptionReference>` defaults to `tx<table_code>.<column>` (e.g., `txtxcmg010.user`) when the package is `tx`, or `<package><table_code>.<column>`, matching Workbench behavior.
  - Native datatype mapping aligns with LN Studio's Ecore model: `1` (Byte), `2` (Double/Float), `3` (Long/Integer), `5` (Numeric/Amount), `6` (String/Multibyte), `7` (Enumeration/Boolean), `9` (Date), `14` (UTC DateTime).
  - Session generator supports session window/sub-type combinations for `maintain_list`, `maintain_details`, `mmt_controller` (including `<Satellite>` elements), `satellite`, `display`, and `process`/`print`, plus `<UserCommand>` form command declarations.
  - Library generator creates `<DR_Module>` `.lib` files under `<pkg>/library/<mod>/` for general DLLs, `<pkg>/library/ess/` (`sourceType=8`) for Session Extensions, and `<pkg>/library/est/` for Table Extensions, seeding `#context_on` / `#context_off` hook sections from LN Studio's script templates.
  - Menu generator creates `<DR_Menu>` `.mnu` files under `<pkg>/menu/<mod>/` with `<MenuChoice>` elements (`menuFieldType` `1` for session, `2` for menu, etc.) and corresponding `.lbl` files.
- The master orchestrator CLI adds dedicated subcommands (`domain`, `library`, `menu`, `validate`, `check-script`) alongside existing subcommands (`workspace`, `table`, `session`, `component`, `inject`, `extract`, `sync-admin`, `diagnose`, `build`, `pipeline`).

### 5. LN Studio Syntax Highlighting & Code Completion Extractor & Static 4GL Inspector
- A dedicated extractor/helper reads the pinned LN Studio installation JARs (`lnstudio_commonui.jar`, `lnstudio_commoncore.jar`, `fourglstudio_core.jar`, `threegl_scanner.jar`, `threegl_parser.jar`) to materialize a canonical JSON/Markdown dictionary of LN Studio's Script Editor intelligence:
  - `KEYWORDS`, `PROGRAM_SECTIONS`, `SUB_SECTIONS`, `CHOICE_SECTIONS`, `REPORT_SECTIONS`, `SQL_KEYWORDS`, `PREDEFINED_VARIABLES`, `STANDARD_DEFINES`, `OTHER`, `DAL_OBJECT_HOOKS`, and `ScriptTemplates`.
- The static 4GL inspector (`check-script` and Layer 4 of `validate`) uses the extracted dictionaries together with the 3GL/4GL scanner/parser to inspect standalone scripts (`.dal`, `.cln`, `.lib`) and embedded `<expression>` blocks inside `.tbl`, `.ses`, and `.lib` files:
  - Validates program section headers (e.g., `declaration:`, `before.program:`, `main.table.io:`, `field.<name>:`, `choice.<name>:`) and subsection headers (`before.input:`, `check.input:`, `when.field.changes:`, `before.choice:`, `on.choice:`, `after.choice:`) against the official completion tables, flagging unknown or misspelled sections.
  - Verifies block balance for `select`/`endselect`, `if`/`endif`, `case`/`endcase`, `for`/`endfor`, `while`/`endwhile`, `repeat`/`until`, and `#context_on`/`#context_off`.
  - Cross-checks script symbols against the owning XML Object:
    - UI Script `field.<name>:` sections must reference a `<FormField><fieldName>` in the `.ses` or an identifier declared in the script.
    - UI Script `choice.<name>:` sections must match an active `<StandardCommand>` or `<UserCommand>` in the `.ses` (or standard choice section).
    - DAL 2 and Table Extension property hooks (`<table.column>.is.valid`, `<table.column>.make.valid`, `<table.column>.is.mandatory`, `<table.column>.is.readonly`, `<table.column>.update`, `<table.column>.check`) must match a defined `<Column>` in the corresponding `.tbl` (or a `cdf_` field).
    - Session Extension command hooks (`function.<cmd>.is.enabled`, `function.<cmd>.before.command`, `function.<cmd>.after.command`) are checked for valid hook suffixes.

### 6. Four-Layer Object & Workspace Validator (`validate` & `--fix`)
- The `validate` subcommand runs a deterministic 4-layer audit across an Activity (or specific component path):
  1. **Layer 1 (SCM & Activity State)**: Compares all component files on disk (across all 12 LN Studio component extensions) against `.admin` entries, flags untracked files or missing disk files, reports Read-Only vs checked-out consistency, and verifies `<application>` and `<versionID>` against the Activity's project and VRC.
  2. **Layer 2 (XML Structure & Data Dictionary Rules)**: Verifies root tag and required child elements per component type (`.tbl`, `.ses`, `.dmn`, `.lbl`, `.lib`, `.mnu`, `.rpt`, `.rptdsrc`), validates column/field naming rules, checks `nativeDatatype` and `Facet` combinations, and verifies Session `<FormGroup>` tree integrity (no orphan `parentGroup`, broken `firstChildGroup`, or cyclic `nextGroup`/`previousGroup` pointers).
  3. **Layer 3 (Cross-Object Reference Integrity)**: Verifies that `<descriptionReference>`, `<fieldLabel>`, and `<Enumeration><descriptionReference>` tags resolve to `.lbl` files in the Activity (or known standard package labels), `.ses` `<ControllerTableRelationship><toTable>` and `<FormField><fieldName>` match `.tbl` columns (when the table is in the Activity), `.tbl` `<IndexColumn>` and `<TableRelationshipColumn><from>` match defined `<Column><name>` entries, and `.mnu` choices reference valid component names.
  4. **Layer 4 (4GL Syntax, Code Completion & Object-Script Cross-Check)**: Runs the static 4GL inspector on every embedded `<expression>` in `.tbl`, `.ses`, and `.lib` files within the Activity.
- By default, `validate` is strictly **read-only** and exits with `0` when zero errors are found or `1` when one or more `[ERROR]` items are detected (`[WARNING]` items are reported without failing the exit code unless `--strict` is passed).
- When `--fix` is passed, the validator performs only **safe, non-destructive repairs**:
  1. Generates any missing `.lbl` files in `<pkg>/label/` for custom `<descriptionReference>` / `<fieldLabel>` entries declared in the Activity's `.tbl`, `.ses`, `.dmn`, or `.mnu` files.
  2. Runs `.admin` SCM synchronization across all 12 LN Studio component extensions so newly created files on disk are registered in `.admin`.
  3. Never modifies or unlocks Read-Only files.

## Testing Decisions

### 1. What Makes a Good Test
- Tests assert **external behavior only**: CLI exit codes, human-readable/JSON stdout and stderr reports, generated XML file existence and well-formedness, preservation of Read-Only files, `.admin` registration state, and search/validator pass rates. Tests never assert on private helper functions or internal implementation state.

### 2. Testing Seams (Highest Possible Seam)
- **Primary Seam — Master Orchestrator CLI (`ln_component_builder.py`)**:
  - Almost all new functionality (explicit workspace/activity resolution, Read-Only protection, multi-object generation for `.tbl`/`.dmn`/`.lbl`/`.ses`/`.lib`/`.mnu`, expanded `.admin` synchronization, 4-layer `validate` with `--fix`, and `check-script` via LN Studio's syntax/completion engine) is tested through the top-level orchestrator CLI subcommands (`table`, `session`, `domain`, `library`, `menu`, `component`, `inject`, `sync-admin`, `validate`, `check-script`, `pipeline`).
- **Secondary Seam — Skill Validator & Search CLI (`validate_skill.py` & `search.py`)**:
  - Verifies that all updated reference documentation, XML schema guides, and extracted syntax/completion catalogs have zero broken links, complete `INDEX.tsv` coverage, and ranked search hits.

### 3. Modules Under Test
- **Workspace & SCM Guardrail Module**: Explicit `--workspace` / `--activity-path` enforcement, Read-Only write/inject blocking, and 12-extension `.admin` synchronization against fixture activities and live `SCS_TST` activity `dev_natt_1107-1 [EXTce01107]`.
- **Declarative Schema & XML Generators**: Generation and validation of Tables (`tx<table_code>.<column>` labels, Date/Amount/Enum datatypes), Domains, Labels, Sessions (Overview, Details, MMT Controller + Satellites, Form Commands), Libraries (DLL, `ess`, `est`), and Menus, plus backward compatibility with legacy single-table schemas.
- **4-Layer Object Validator & 4GL Syntax/Completion Inspector**: Detection of untracked `.admin` files, `<application>`/`<versionID>` mismatches, broken `<FormGroup>` pointers, missing `.lbl` / column cross-references, invalid 4GL section/choice/hook names, unclosed `select`/`if`/`#context_on` blocks, and safe `--fix` repair behavior.
- **Skill Integrity & Documentation**: Zero broken links or orphan pages via `validate_skill.py`, and ranked hits via `search.py`.

### 4. Prior Art
- Extends the existing unit test suite in `ln_studio_skill/tools/tests/` (`unittest` standard library runner), reusing temporary workspace/activity fixtures, round-trip XML assertions, and the skill validator (`validate_skill.py`).

## Out of Scope

- Replacing or duplicating the 4GL coding cookbooks in `erp-ln-progguide` (DAL 2 business logic design, SQL optimization tutorials, and extension architecture remain in `erp-ln-progguide`).
- Full server-side Bshell bytecode compilation offline (type-checking against remote standard tables not present in the local Workspace still relies on the Eclipse JCA build bridge and `.markers` diagnostics).
- Bypassing JCA security to perform remote SCM Check-in or Check-out outside the LN Studio Eclipse Workbench (Check-in/Check-out remains strictly Human-in-the-loop).
- Ingesting the Integration Development Guide (BOD/BDE modeling) — remains tracked separately as Phase 2 per ADR 0002.

## Further Notes

- **Pinned Studio Installation**: `D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64` (Infor LN Studio 10.8 build 0640).
- **Live Verification Reference Workspace**: `C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST` (Activity `dev_natt_1107-1 [EXTce01107]`), passed explicitly at runtime via `--workspace` or `--activity-path` rather than hardcoded as a default.
- **Installed Skill Synchronization**: Upon completion, the self-contained `ln_studio_skill/` folder in the repository is synchronized to the active agent skill directory (`C:\Users\nutdo\.gemini\config\skills\ln_studio_skill`).
