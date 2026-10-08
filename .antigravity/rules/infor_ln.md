# Infor LN & Baan 4GL Architecture Rules and Coding Guidelines

This document defines the authoritative architecture rules, coding standards, and CLI automation protocols for any engineer or AI coding assistant developing on Infor LN Studio 10.8 and Infor Enterprise Server.

---

## 1. Architectural Layer Separation

### 1.1 Data Access Layer 2 (DAL 2 - `#include <bic_dal2>`)
All business logic, data integrity constraints, validations, and lifecycle operations MUST reside in DAL 2 scripts embedded in table definitions (`.tbl`).

- **Object Hooks:**
  - `before.open.object.set()`: Restrict access or set filter criteria for reading objects.
  - `method.is.allowed(long i.method)`: Control whether `DAL_NEW`, `DAL_UPDATE`, or `DAL_DESTROY` is permitted.
  - `before.save.object(long i.mode)`: Validate cross-field consistency and business constraints before write (`DAL_NEW` or `DAL_UPDATE`). Return `0` on success or `DALHOOKERROR` on failure.
  - `after.save.object(long i.mode)`: Synchronize dependent records or audit logs after successful database write.
  - `before.destroy.object()` / `after.destroy.object()`: Cascade checks and cleanup upon deletion.
- **Field / Property Hooks:**
  - `<table_field>.make.valid(long i.mode)`: Calculate default values or auto-sequence numbers.
  - `<table_field>.is.valid(long i.mode)`: Validate individual field values.
  - `<table_field>.is.mandatory(long i.mode)`: Conditionally require fields based on record state.
  - `<table_field>.is.readonly(long i.mode)`: Conditionally disable editing of specific fields.
  - `<table_field>.update(long i.mode)`: Handle side-effects when a field value changes.
- **Cardinal Rule:**
  Never execute `commit.transaction()` or `abort.transaction()` within DAL 2 hooks. Transactions are managed entirely by the DAL transaction framework.

### 1.2 UI Script (`bic_dam` - `#include <bic_dam>`)
UI scripts embedded in sessions (`.ses`) must strictly contain presentation and user interaction logic.

- **Permitted in UI Scripts:**
  - Form navigation and layout hooks (`before.program:`, `before.display:`, `after.form.read:`).
  - Zoom filters and parameters (`before.zoom:`, `selection.filter:`, `query.extend.where.in.zoom(...)`).
  - Standard choice intercepts (`choice.update.db:`, `choice.end.program:`).
  - Form commands and toolbar button handlers.
- **Strictly Prohibited in UI Scripts:**
  - Direct database DML (`db.insert()`, `db.update()`, `db.delete()`). All persistence must occur through the DAL.
  - Validations that protect business data integrity (these must live in DAL 2 so BOD/BDE integrations are protected).

---

## 2. Infor LN Coding Standards & Conventions

### 2.1 Maintenance Comments (SPS Compliance)
Whenever modifying an existing script or adding new logic to an activity, all modified or inserted blocks MUST be wrapped with maintenance comments identifying the activity:

```baan
|#<activity_name>.sn
txptc100.seqn = tem.seqn + 1
|#<activity_name>.en
```

- `.sn`: Start-New / Start-Modification
- `.en`: End-New / End-Modification
- `.so` / `.eo`: Start-Old / End-Old (commenting out obsolete code)

### 2.2 Error Messaging
- Use `dal.set.error.message("@<label_code>")` or formatted messages:
  ```baan
  dal.set.error.message("@txptc100.seqn.invalid")
  return(DALHOOKERROR)
  ```
- Use `show.dal.messages()` only when explicitly required to force user presentation.

### 2.3 Control Flow & Code Hygiene
- **No `goto` statements.** Use structured loops (`while`, `repeat`, `for`) or functions.
- **Explicit return codes:** All hook functions must explicitly return an integer (`return(0)` or `return(DALHOOKERROR)`) or boolean (`return(true)` / `return(false)`).
- **Check Query Results:** Always provide `selectdo` and `selectempty` branches for SQL queries:
  ```baan
  select  txptc100.*
  from    txptc100
  where   txptc100._index1 = {:i.seqn}
  as set with 1 rows
  selectdo
      | Record found
  selectempty
      | Record not found
  endselect
  ```

---

## 3. Automation Toolchain Workflows for AI Agents

When implementing features, creating tables, or debugging compilation errors, agents MUST use the unified CLI tools in `tools/`:

### 3.1 Step 1: Component Definition & Generation
Define the table, fields, indices, and session in a YAML schema file (see `ln_studio_skill/templates/table_schema_sample.yaml`). Generate metadata directly into the target activity:

```bash
python tools/ln_component_builder.py component --spec schema.yaml --activity "<activity_name>"
```

### 3.2 Step 2: 4GL Code Development & Synchronization
Develop Baan 4GL source in standalone `.dal` or `.cln` files in `scripts/`:
- DAL: `scripts/dal/<table_code>.dal`
- UI: `scripts/ui/<session_code>.cln`

Inject the code into workspace metadata XML:
```bash
python tools/ln_component_builder.py inject --source scripts/dal/txptc100.dal --target "<activity_path>/tx/table/ptc/txptc100.tbl"
```

### 3.3 Step 3: Eclipse SCM Synchronization
Register new components in the activity `.admin` file:
```bash
python tools/ln_component_builder.py sync-admin --activity "<activity_name>"
```

### 3.4 Step 4: Closed-Loop Compilation & Diagnostic Fixing
Trigger Eclipse build and inspect line-accurate compiler error markers:
```bash
python tools/ln_component_builder.py build --activity "<activity_name>"
```

If compilation errors exist, the tool prints exact files, line numbers, and error descriptions. Fix the code in `scripts/`, re-inject, and rebuild until 0 errors are reported.
