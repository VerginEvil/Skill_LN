# Implementation Plan: Infor LN Studio Automation & Assistant Skill

This plan details the phased execution roadmap for building the **Infor LN Studio Assistant Skill and Automation CLI Tools** based on the reverse-engineered architecture of Infor LN Studio 10.8 and Eclipse RCP.

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

## Phase 1: Exploration, Reverse Engineering & Specification (DONE)

- [x] **Task 1.1: Workspace Structure Discovery**
  - Identified workspace root: `C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio`.
  - Discovered multi-workspace hierarchy: `Team_TST`, `ZAP_TST`, `DNT_TRN`, `RDT_TST`, etc.
  - Documented Eclipse Project naming convention: `<activity_name> [<software_project_name>]`.
- [x] **Task 1.2: Component Metadata & XML Reverse Engineering**
  - Analyzed `.tbl` (`<DR_Table>` schema, `<Column>`, `<Index>`, `<TableRelationship>`, embedded `<DR_Module>` DAL).
  - Analyzed `.ses` (`<DR_Controller>` schema, main table binding, integrated `<Form>`, embedded `<DR_Module>` UI Script).
  - Analyzed `.dmn` (`<DR_Domain>`), `.lbl` (`<DR_Label>`), `.lib` (`<DR_Module>`).
  - Analyzed `.admin` (Java Serialized `HashMap<String, AdministrationComponent>`).
  - Analyzed `.project` (`com.infor.ln.studio.apps.core.bic` builder & `fourglStudio` nature).
- [x] **Task 1.3: Plugin & Headless Capability Assessment**
  - Inspected `D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64\plugins`.
  - Identified server-side compilation via JCA / Bshell adapter.
  - Discovered `.markers` binary persistence in `.metadata/.../.markers` containing exact file, line, and compiler errors.
- [x] **Task 1.4: Formal Specification**
  - Generated [SPEC_LN_STUDIO_AUTOMATION.md](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/docs/SPEC_LN_STUDIO_AUTOMATION.md).

---

## Phase 2: Metadata & Code Generation CLI Tools

### Milestone Deliverables: `tools/ln_component_builder.py` and `tools/inject_ln_script.py`

- [ ] **Task 2.1: YAML/JSON Schema Parser & Validator (`tools/ln_schema_parser.py`)**
  - Support input in YAML or JSON format.
  - Validate naming conventions:
    - Table code: 2-char package + 3-char module + 3-digit number (e.g. `txptc100`).
    - Field names: max 8 characters, lowercase alphanumeric.
    - Domain references: validate data types and map to `nativeDatatype` codes (3=Long, 6=String, 7=Enum, etc.).
    - Index rules: index 1 must be primary key.
  - Auto-generate label codes and descriptions for table, fields, and indices.

- [ ] **Task 2.2: Table Metadata Generator (`tools/generate_ln_table.py` / `ln_component_builder.py`)**
  - Generate schema-compliant `.tbl` XML matching LN Studio 10.8 `<DR_Table>` format.
  - Generate corresponding `.lbl` files in `<package>/label/` for all table and field descriptions.
  - Generate custom `.dmn` files in `<package>/domain/` if custom enums or domains are specified in schema.
  - Create directory paths automatically in the target Activity folder.

- [ ] **Task 2.3: Session & Dynamic Form Generator (`tools/generate_ln_session.py`)**
  - Generate schema-compliant `.ses` XML matching `<DR_Controller>`.
  - Auto-generate `<PhysicalFormLayout>` with standard `<FormGroup>` and `<FormField>` entries.
  - Populate `<StandardCommand>` entries (Find, First, Next, Prev, Last, Add, Modify, Delete, etc.).
  - Set up `<ControllerTableRelationship>` linking to the main table.

- [ ] **Task 2.4: 4GL Script Injector & Extractor (`tools/inject_ln_script.py`)**
  - `--inject`:
    - Read plain 4GL file (`.dal` for DAL, `.cln`/`.src` for UI script, `.lib` for library).
    - Convert to XML entities (`<` -> `&lt;`, `>` -> `&gt;`, `&` -> `&amp;`).
    - Locate `<expression>` within the target `.tbl`, `.ses`, or `.lib` file and update it cleanly.
  - `--extract`:
    - Read `.tbl`, `.ses`, or `.lib` file.
    - Extract contents of `<expression>` tag.
    - Decode XML entities and write to standalone `.dal`, `.cln`, or `.lib` file.

- [ ] **Task 2.5: Activity `.admin` SCM Synchronizer (`tools/admin_sync.py`)**
  - Helper to register newly generated component files into the activity's `.admin` file.
  - Set `isCheckedout=false`, `isCreated=true`, `m_isDirty=true`, `m_isVSCHappy=false`.
  - Prevent Eclipse from showing missing/unmanaged component status.

---

## Phase 3: Action Bridge & Closed-Loop Diagnostic Loop

### Milestone Deliverables: `tools/ln_studio_bridge.py` and `tools/ln_error_reader.py`

- [ ] **Task 3.1: Eclipse Problem Marker Reader (`tools/ln_error_reader.py`)**
  - Parse binary `.markers` files in:
    `workspace/.metadata/.plugins/org.eclipse.core.resources/.projects/<Activity_Project>/.markers`
  - Extract all records with type `com.infor.ln.studio.common.core.problem`.
  - Output structured JSON and colored terminal output:
    ```json
    [
      {
        "file": "tx/table/ptc/txptc100.tbl",
        "resource": "txptc100",
        "line": 42,
        "severity": "ERROR",
        "message": "Variable 'tdipu045' not declared"
      }
    ]
    ```
  - Parse `<workspace>/.metadata/.log` for server connection drops or JCA ping errors.

- [ ] **Task 3.2: Workspace Action Bridge (`tools/ln_studio_bridge.py`)**
  - Locate running Infor LN Studio window by title regex (`.*Infor LN Studio.*` or Eclipse process).
  - Issue Windows keyboard shortcuts:
    - `F5` / Refresh: prompts Eclipse to scan files modified on disk.
    - `Ctrl+Shift+S`: Save all dirty editors.
    - `Ctrl+B`: Build All (triggers BIC incremental builder).
  - Support CLI commands:
    ```bash
    python tools/ln_studio_bridge.py --refresh
    python tools/ln_studio_bridge.py --build
    python tools/ln_studio_bridge.py --build-and-check --activity "dev_natt_01103 [EXTce01103]"
    ```
  - Wait for build settle delay (2-3 seconds) and automatically invoke `ln_error_reader.py`.

- [ ] **Task 3.3: Closed-Loop Agent Orchestration Workflow**
  - Script command `python tools/ln_workflow.py --compile-check`:
    1. Injects updated script into workspace XML.
    2. Sends Refresh (`F5`) and Build (`Ctrl+B`) to Eclipse.
    3. Reads `.markers`.
    4. Returns exit code 0 if clean, or exit code 1 with exact error lines and messages for the agent to fix.

---

## Phase 4: Skill Packaging & Coding Standards Rules

### Milestone Deliverables: `.antigravity/rules/infor_ln.md` and `ln_studio_skill/`

- [ ] **Task 4.1: Project Rule Document (`.antigravity/rules/infor_ln.md`)**
  - Codify strict layer separation:
    - **DAL 2 (`bic_dal2`):** All business logic, mandatory checks, validations, auto-sequence numbering, and references.
    - **UI Script (`bic_dam`):** Form commands, zoom filters, user interaction only. No database DML.
  - Mandatory Maintenance Comments:
    - When modifying existing code, always insert `|#<activity>.sn` (Start-New) and `|#<activity>.en` (End-New).
  - Code hygiene rules:
    - No `goto`.
    - Handle return codes for all DAL functions (`return(DALHOOKERROR)` / `return(0)`).
    - Always check query results (`selectdo` / `selectempty`).
    - No transaction commits/retries inside DAL hooks.

- [ ] **Task 4.2: Infor LN Studio Assistant Skill (`ln_studio_skill/SKILL.md`)**
  - Create the agent skill manifest.
  - Document available CLI tools, parameters, and invocation sequences.
  - Define standard multi-step recipes:
    - Recipe 1: "Create a new Table & Session from scratch".
    - Recipe 2: "Add new fields to an existing table".
    - Recipe 3: "Implement business rules in DAL 2".
    - Recipe 4: "Debug compile errors iteratively".

- [ ] **Task 4.3: Reference Documentation & Schema Templates**
  - Create `ln_studio_skill/references/COMPONENT_XML_SCHEMA.md`: full tag reference for `.tbl`, `.ses`, `.dmn`, `.lbl`.
  - Create `ln_studio_skill/references/DAL2_HOOKS_GUIDE.md`: complete hook catalog (`before.save.object`, `<field>.make.valid`, `<field>.is.valid`, `<field>.is.mandatory`, etc.).
  - Create `ln_studio_skill/references/UI_SCRIPT_GUIDE.md`: form events, commands, zoom hooks.
  - Create templates:
    - `ln_studio_skill/templates/table_schema_sample.yaml`
    - `ln_studio_skill/templates/dal2_template.dal`
    - `ln_studio_skill/templates/ui_script_template.cln`

---

## Phase 5: Verification & Quality Assurance

- [ ] **Task 5.1: Unit Test Suite (`tools/tests/test_ln_tools.py`)**
  - Test YAML parsing against schema constraints.
  - Test XML generation against reference XMLs (`txptc100.tbl`, `txwmd401.tbl`).
  - Test round-trip injection and extraction of DAL and UI scripts with XML entities.
  - Test `.markers` binary parser against real sample files from `workspace_lnstudio`.
- [ ] **Task 5.2: End-to-End Simulation**
  - Run component builder on sample YAML schema in a test activity.
  - Verify generated `.tbl`, `.ses`, `.lbl`, `.dmn` files match LN Studio specifications.
  - Trigger mock compile and verify error reader output.
