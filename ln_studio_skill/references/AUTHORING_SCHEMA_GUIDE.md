# Infor LN Studio Declarative Authoring Schema Guide

Specification and guide for generating Infor LN Studio components declaratively from YAML schemas using `tools/ln_component_builder.py` and `tools/ln_schema_parser.py`.

---

## 1. Multi-Component Schema Specification

A declarative `schema.yaml` file defines domains, tables, sessions, libraries, and menus in a unified, versioned document:

```yaml
version_id: B61O_a_ext
application: EXTce01107

domains:
  - name: txcmg.remk
    package: tx
    datatype: string
    length: 100
    description: Billing Remarks
  - name: txcmg.stat
    package: tx
    datatype: enum
    description: Batch Status
    constants:
      - { value: 1, name: open, label: Open }
      - { value: 2, name: approved, label: Approved }
      - { value: 3, name: closed, label: Closed }

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
      - name: stat
        domain: txcmg.stat
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

## 2. Component Generation Commands

Generate individual components or the entire specification in a single command:

```bash
# Validate authoring schema syntax
python tools/ln_schema_parser.py schema.yaml

# Generate Table, Labels, and Domains
python tools/ln_component_builder.py table --spec schema.yaml --output-dir ./components

# Generate Domain XML independently
python tools/ln_component_builder.py domain --spec schema.yaml --output-dir ./components

# Generate Session XML (Maintain, MMT Controller, or Satellite)
python tools/ln_component_builder.py session --spec schema.yaml --output-dir ./components

# Generate Library XML (Standard DLL)
python tools/ln_component_builder.py library --spec schema.yaml --output-dir ./components

# Generate Menu XML & Labels
python tools/ln_component_builder.py menu --spec schema.yaml --output-dir ./components

# Generate ALL components declared in schema
python tools/ln_component_builder.py component --spec schema.yaml --output-dir ./components

# Full autonomous generation pipeline (generate -> sync-admin -> validate --fix -> build)
python tools/ln_component_builder.py pipeline --spec schema.yaml --output-dir ./components --auto-fix
```

---

## 3. Single-XML TDE Layout Architecture

All generated components adhere strictly to authentic Eclipse Infor LN Studio Single-XML TDE layout rules:

1. **Self-Contained Single XML**: Each component is an authentic XML file (`.tbl`, `.ses`, `.lib`, `.dmn`, `.lbl`, `.mnu`, `.rpt`, `.msg`, `.qst`, `.fnc`, `.add`).
2. **Directory Placement**:
   - Module-scoped components (`.tbl`, `.ses`, `.lib`, `.rpt`, `.fnc`, `.add`): `{package}/{component_type}/{module}/{name}.{ext}`
   - Global components (`domain`, `label`, `message`, `question`, `menu`): `{package}/{component_type}/{name}.{ext}`
3. **Embedded Script Logic**: 4GL source logic (DAL scripts, UI scripts, library source) is stored inside `<expression>` tags within the XML file.
4. **Automated Label Synchronization**: Custom field labels and session titles reference `.lbl` components. Missing `.lbl` files are automatically generated when running `validate --fix`.
