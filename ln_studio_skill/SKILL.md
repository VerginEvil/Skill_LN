---
name: ln_studio_skill
description: "Infor LN Studio Assistant Skill for developing Infor LN applications, generating tables/sessions, synchronizing 4GL source code, and diagnosing compiler errors."
---

# Infor LN Studio Assistant Skill

The **Infor LN Studio Assistant Skill** empowers engineers and AI agents to develop applications on **Infor ERP LN** and **Infor LN Studio 10.8 (Eclipse RCP)** with high speed and zero manual UI clicking.

---

## Capabilities & Toolset

All CLI tools reside in `tools/` and can be invoked either directly or through the master orchestrator `tools/ln_component_builder.py`:

| Tool | Purpose | Primary Commands |
|------|---------|------------------|
| [`ln_component_builder.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/ln_component_builder.py) | Master pipeline CLI | `table`, `session`, `component`, `inject`, `extract`, `build`, `pipeline` |
| [`ln_schema_parser.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/ln_schema_parser.py) | Schema validator | `python tools/ln_schema_parser.py <schema.yaml>` |
| [`generate_ln_table.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/generate_ln_table.py) | Table/Label/Domain XML generator | `python tools/generate_ln_table.py --spec <spec> --activity <act>` |
| [`generate_ln_session.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/generate_ln_session.py) | Session & Form XML generator | `python tools/generate_ln_session.py --spec <spec> --activity <act>` |
| [`inject_ln_script.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/inject_ln_script.py) | 4GL bidirectional synchronizer | `python tools/inject_ln_script.py --inject --source <f.dal> --target <f.tbl>` |
| [`admin_sync.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/admin_sync.py) | Eclipse SCM `.admin` cache sync | `python tools/admin_sync.py --activity <act> --scan-and-update` |
| [`ln_error_reader.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/ln_error_reader.py) | Binary `.markers` diagnostics reader | `python tools/ln_error_reader.py --activity <act> [--errors-only]` |
| [`ln_studio_bridge.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/ln_studio_bridge.py) | Windows action bridge (F5 / Ctrl+B) | `python tools/ln_studio_bridge.py --build-and-check --activity <act>` |
| [`ln_workspace_manager.py`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/tools/ln_workspace_manager.py) | Activity environment resolver | `python tools/ln_workspace_manager.py --list-activities` |

---

## Standard Workflows & Recipes

### Recipe 1: Create a New Table and Session from Scratch

1. **Author the Schema YAML:**
   Create a YAML definition following [`ln_studio_skill/templates/table_schema_sample.yaml`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/ln_studio_skill/templates/table_schema_sample.yaml):
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
   python tools/ln_component_builder.py component --spec schema.yaml --activity "dev_natt_01103"
   ```

3. **Sync Eclipse SCM State:**
   ```bash
   python tools/ln_component_builder.py sync-admin --activity "dev_natt_01103"
   ```

4. **Compile & Verify:**
   ```bash
   python tools/ln_component_builder.py build --activity "dev_natt_01103"
   ```

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
   python tools/ln_component_builder.py inject --source scripts/dal/txptc300.dal --target "path/to/txptc300.tbl"
   ```

3. **Trigger Compilation & Inspect Output:**
   ```bash
   python tools/ln_component_builder.py build --activity "dev_natt_01103"
   ```

---

### Recipe 3: Closed-Loop Autonomous Debugging

When an AI agent modifies code and receives compiler errors:
```bash
python tools/ln_error_reader.py --activity "dev_natt_01103" --errors-only
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

---

## References & Guides

- [COMPONENT_XML_SCHEMA.md](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/ln_studio_skill/references/COMPONENT_XML_SCHEMA.md): Complete XML schema reference for `.tbl`, `.ses`, `.dmn`, and `.lbl`.
- [DAL2_HOOKS_GUIDE.md](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/ln_studio_skill/references/DAL2_HOOKS_GUIDE.md): Catalog of DAL 2 Object Hooks, Property Hooks, and Business Methods.
- [UI_SCRIPT_GUIDE.md](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/ln_studio_skill/references/UI_SCRIPT_GUIDE.md): Guide for UI Script sections, form commands, and zoom filters.
