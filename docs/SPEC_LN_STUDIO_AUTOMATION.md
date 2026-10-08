# Specification: Infor LN Studio Automation & Assistant Skill

## Problem Statement

Developing software for **Infor ERP LN** using **Infor LN Studio** (an Eclipse Rich Client Platform / RCP application) involves substantial manual, repetitive, and error-prone procedures:

1. **Tedious GUI Metadata Creation:** Creating database tables, domains, labels, and sessions requires navigating dozens of nested dialogs and wizards in Eclipse. Developers must manually configure hundreds of fields, check-boxes, and references.
2. **Impeded Source Version Control:** Source code for Data Access Layer (DAL 2) scripts and UI scripts is embedded directly inside XML metadata files (`.tbl` and `.ses` files within `<expression>` tags). This prevents standard Git workflows, code reviews, and effective AI-assisted coding because 4GL code cannot be natively edited or diffed as plain text.
3. **Broken Feedback Loops for AI Agents:** When an AI coding assistant generates 4GL code or table definitions, it cannot easily trigger LN Studio's compilation process or inspect compile errors, because compilation is performed remotely on the Infor Enterprise Server via JCA/Bshell. Agents lack an automated mechanism to refresh the workspace, trigger builds, and capture line-accurate compiler errors from Eclipse.
4. **Violation of Architectural Boundaries:** Without explicit, automated guidelines, code often blurs the line between UI logic and business logic. Business rules leak into UI scripts instead of being centralized in DAL 2 hooks (`<field>.is.valid`, `before.save.object`), breaking integration interfaces (BDE/BOD) and causing regressions.

---

## Solution

Build an integrated **Infor LN Studio Automation Toolset & AI Assistant Skill** consisting of four cohesive pillars:

1. **Declarative Component Builder (`tools/ln_component_builder.py`):**
   A Python CLI tool that ingests human- and AI-friendly JSON/YAML schema definitions (specifying tables, columns, domains, labels, and indices) and generates fully formed, schema-compliant LN Studio XML files (`.tbl`, `.ses`, `.dmn`, `.lbl`) directly into the target Activity folder in the workspace.
2. **Bidirectional Script Synchronizer (`tools/inject_ln_script.py`):**
   A script injector and extractor that bridges standalone plain-text 4GL files (`.dal`, `.cln`, `.src`) in the repository with the embedded `<expression>` XML blocks in `.tbl`, `.ses`, and `.lib` files in the Eclipse workspace.
3. **Workspace Action & Diagnostic Bridge (`tools/ln_studio_bridge.py` & `tools/ln_error_reader.py`):**
   - A lightweight automation bridge to focus the Infor LN Studio window and issue workspace actions: **F5** (Refresh), **Ctrl+Shift+S** (Save All), and **Ctrl+B** (Build All).
   - A direct parser for Eclipse `.markers` files in `.metadata/.plugins/org.eclipse.core.resources/.projects/<Activity>/` to extract line-accurate compiler and VSC error messages into structured JSON without fragile screen scraping or OCR.
4. **Infor LN Project Rules & Skill (`ln_studio_skill/` & `.antigravity/rules/infor_ln.md`):**
   A codified skill and rule system that enforces DAL 2 / UI Script separation, standard maintenance comment headers (`|#activity.sn` / `|#activity.en`), schema templating, and closed-loop "Code -> Inject -> Build -> Diagnose -> Fix" agent workflows.

---

## User Stories

1. As an LN developer, I want to define a new table and its fields in a clear YAML/JSON specification, so that I can generate complete LN Studio table metadata without manually clicking through Eclipse wizards.
2. As an LN developer, I want primary and secondary indices to be generated automatically from the schema specification, so that table indexing is consistent and primary keys are correctly defined.
3. As an LN developer, I want table relationships (foreign keys) and referential integrity rules (cascade, restricted, noAction) to be auto-populated in the table metadata, so that database integrity is enforced by the ERP.
4. As an LN developer, I want multi-language labels (`.lbl`) to be generated automatically alongside table and column definitions, so that UI descriptions and reports display proper localized text.
5. As an LN developer, I want domain definitions (`.dmn`) with enumerations and facets to be generated automatically, so that field types and validation boundaries match standard LN conventions.
6. As an LN developer, I want to write DAL 2 scripts in standalone `.dal` files in my Git repository, so that I have standard syntax highlighting, clean Git diffs, and modular code management.
7. As an LN developer, I want to inject my standalone `.dal` code into the corresponding `.tbl` metadata file inside the active workspace activity, so that LN Studio can compile and upload it to the Infor Enterprise Server.
8. As an LN developer, I want to extract existing DAL and UI scripts from `.tbl` and `.ses` workspace files into standalone repository files, so that I can refactor and version-control legacy components easily.
9. As an LN developer, I want to generate maintain and display sessions (`.ses`) with integrated dynamic forms, so that overview grids and detail views are available immediately upon Eclipse refresh.
10. As an LN developer, I want session form commands and toolbar action sets to be configured via the schema, so that business methods and standard actions are accessible without manual GUI layouting.
11. As an autonomous AI agent, I want a CLI command to trigger an Eclipse workspace refresh and build, so that changes written to disk are synced and compiled on the LN server automatically.
12. As an autonomous AI agent, I want to programmatically parse Eclipse compiler problem markers (`.markers`), so that I receive exact file paths, line numbers, and error descriptions without fragile UI OCR or screen scraping.
13. As an autonomous AI agent, I want a closed-loop correction loop ("write -> inject -> build -> parse error -> fix"), so that I can autonomously resolve 4GL syntax and DAL logic errors until compilation succeeds.
14. As an LN developer, I want the `.admin` SCM cache in the workspace activity to stay synchronized when new files are created, so that Eclipse does not show broken or dirty status indicators.
15. As a project lead, I want strict architecture rules in `.antigravity/rules/infor_ln.md` mandating that all business logic resides in DAL 2 and UI scripts contain only presentation logic, so that code quality and ERP maintainability are preserved.
16. As an LN developer, I want automatic insertion of activity maintenance comments (`|#activity.sn` / `|#activity.en`), so that code modifications comply with Infor LN Software Programming Standards (SPS).
17. As an LN developer, I want to list all open activities and projects across multiple Eclipse workspaces, so that I can easily select the target activity without navigating directory trees manually.
18. As an LN developer, I want the tool to validate field names (max 8 characters), table names (`<package><module><number>`), and domain types before generating XML, so that schema compilation never fails on naming convention checks.

---

## Implementation Decisions

### 1. Canonical Schema Specification (JSON / YAML)
- Component definitions will be authored in declarative YAML (with JSON as interchangeable alternative).
- The schema will define:
  - `table`: table code (e.g. `txptc100`), module (e.g. `ptc`), description, and version ID (e.g. `B61O_a_ext`).
  - `fields`: list of columns, each specifying `name` (max 8 chars), `domain`, `description`, `mandatory` (boolean), `default_value` (e.g. `$__unique` for sequence, constant, or empty), and `position`.
  - `indices`: list of indices, each specifying `id` (1 = primary key), `unique` (boolean), `description`, and `columns` with sort orders (`asc`/`desc`).
  - `references`: foreign key relations specifying `to_table`, column mappings (`from` -> `to`), `delete_rule`, and `update_rule`.
  - `session`: optional block to generate an integrated session (`.ses`) linked to the table.

### 2. XML Metadata Engine (`tools/ln_component_builder.py`)
- The generator produces standard Infor LN Studio XML structures:
  - Table: `<DR_Table>` XML root, `<Column>` elements, `<Index>` elements, `<TableRelationship>` elements, and `<application>` tag matching the activity's project name.
  - Session: `<DR_Controller>` XML root with `<ControllerTableRelationship>`, `<StandardCommand>` entries, and integrated `<Form><PhysicalFormLayout>` containing `<FormGroup>` and `<FormField>`.
  - Domain: `<DR_Domain>` with `<datatype><nativeDatatype>` mapping (3 = Long/Integer, 6 = String, 7 = Enum, etc.) and `<Enumeration>` entries.
  - Label: `<DR_Label>` with `<LabelVariant>` containing English (`language=2`) descriptions, calculated length/height, and uppercase keywords.

### 3. Bi-directional 4GL Code Sync Engine (`tools/inject_ln_script.py`)
- Clean separation between Git storage and Eclipse workspace storage:
  - In Git/repo: Standalone `.dal` (DAL 2), `.cln` (UI Script), and `.lib` (Libraries) containing pure Baan 4GL source code.
  - In Workspace: Injected inside `<DR_Module><Source><expression>...</expression></Source></DR_Module>` of `.tbl`, `.ses`, or `.lib` files.
- The tool handles XML entity conversion:
  - Inbound (Inject): escapes `&` -> `&amp;`, `<` -> `&lt;`, `>` -> `&gt;`.
  - Outbound (Extract): decodes XML entities into standard 4GL source.
- Preserves headers, metadata, and existing table/session properties without altering other XML elements.

### 4. Direct Problem Marker Reader (`tools/ln_error_reader.py`)
- Rather than relying on UI screen scraping or OCR of the Eclipse "Problems" view:
  - The tool directly parses the binary `.markers` file located at:
    `workspace/.metadata/.plugins/org.eclipse.core.resources/.projects/<Activity_Project>/.markers`
  - It extracts:
    - Resource path (e.g. `tx/library/inh/txinh4201api.lib` or `tx/table/ptc/txptc100.tbl`)
    - Severity (`Error`, `Warning`, `Info`)
    - Line number
    - Problem description (e.g. syntax error, type mismatch, uncompiled references)
  - Also monitors `<workspace>/.metadata/.log` for JCA connection or server-side communication failures.
  - Outputs structured JSON for automated consumption by the AI agent.

### 5. Automation Action Bridge (`tools/ln_studio_bridge.py`)
- Automates interactions with the active Infor LN Studio Eclipse window:
  - Identifies the window by title pattern (`Infor LN Studio` or activity title).
  - Sends Windows input keys:
    - `F5`: Refresh active resource/project (reloads disk changes into Eclipse).
    - `Ctrl+Shift+S`: Save All open dirty editors.
    - `Ctrl+B`: Build All (triggers `IncrementalProjectBuilderBIC` to compile via JCA to Enterprise Server).
  - Implements a retry and settle delay (default 2-3 seconds) to allow the background build job to complete before reading `.markers`.

### 6. Workspace Activity Management & `.admin` Cache
- Activity directory discovery: Automatically resolves `<activity> [<project>]` directory paths under the selected workspace (e.g. `Team_TST`, `ZAP_TST`).
- Helper utility ensures that when new component files are added on disk, the `.admin` file (Java Serialized `HashMap<String, AdministrationComponent>`) is updated with initial created/checked-out state so Eclipse does not flag the resource as untracked.

### 7. Strict Layering Architecture Rules (`.antigravity/rules/infor_ln.md`)
- **DAL 2 Rule:** All business rules, integrity checks, auto-number generation, and field dependencies must reside in DAL 2 hooks:
  - `before.save.object(long mode)`
  - `after.save.object(long mode)`
  - `<field>.make.valid(long mode)`
  - `<field>.is.valid(long mode)`
  - `<field>.is.mandatory(long mode)`
  - `method.is.allowed(long method)`
- **UI Script Rule:** UI Scripts must strictly contain presentation logic:
  - `main.table.io:`
  - `choice.<command>:`
  - `field.<field_name>:` (e.g. `before.zoom:`, `selection.filter:`)
  - No database updates or direct table queries that bypass DAL.
- **Maintenance Comments:** Enforces mandatory `|#<activity>.sn` (Start-New) and `|#<activity>.en` (End-New) comment tagging on all code modifications.

---

## Testing Decisions

1. **Schema Parser & Generator Tests:**
   - Ingest a sample YAML schema for a new table and verify that the generated `.tbl` XML matches the exact element ordering, namespaces, and facet structures of production references (`txptc100.tbl` and `txwmd401.tbl`).
2. **Round-Trip Code Synchronization Tests:**
   - Extract DAL code from `txptc100.tbl` to a temporary `.dal` file.
   - Re-inject it back into a copy of `txptc100.tbl`.
   - Verify zero semantic or formatting drift between the original XML expression and the re-injected expression.
3. **Marker Parser Verification:**
   - Execute `ln_error_reader.py` against existing `.markers` files in `workspace_lnstudio/Team_TST/.metadata/...` and confirm that known errors and warnings are correctly decoded into structured JSON with accurate line numbers.
4. **End-to-End Dry-Run Simulation:**
   - Validate full flow on a mock activity directory: Generate Table -> Inject DAL -> Verify `.admin` and `.project` integrity -> Mock trigger build -> Read diagnostic report.

---

## Out of Scope

1. **Replacing Eclipse IDE:** The goal is not to replace Eclipse RCP or write a custom JCA server daemon, but to automate and bridge with the existing Infor LN Studio installation.
2. **Low-Level Binary JCA Protocol Emulation:** We do not intercept or emulate raw JCA socket communications between Eclipse and Enterprise Server; compilation remains orchestrated by Eclipse's native `IncrementalProjectBuilderBIC`.
3. **Modifying Standard Package VRCs:** Direct editing of standard Infor base tables (e.g. standard `whinh200` without extension VRC) is prohibited; all tooling operates within customer extension VRCs (e.g. `B61O_a_ext`).

---

## Further Notes

- **Working Directory Structure:**
  - Tools directory: `tools/`
  - Skill directory: `ln_studio_skill/`
  - Rules directory: `.antigravity/rules/`
- **Compatibility:**
  - Infor LN Studio 10.8.x (Eclipse 4.35 / Java 25 / JRE 11)
  - Infor Enterprise Server 10.5+ / 10.8+
