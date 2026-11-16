---
trigger: model_decision
description: Infor ERP LN, Baan 4GL, DAL 2, UI script, SQL, and Extension Modeler (ttext1500m000, EXT001-EXT003) coding architecture rules and guardrails. Load whenever writing, modifying, debugging, or reviewing Baan 4GL, .dal, .cln, .4gl, or Extension Modeler scripts.
---

# Infor LN & Baan 4GL Architecture Rules and Coding Guidelines

Authoritative architecture rules and coding standards for Infor LN Studio 10.8 build 0640 (April 2026 tree) and Infor Enterprise Server.

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

## 3. Extension Modeler (`ttext1500m000`) Compiler Rules & Static Guardrails (ADR 0013, ADR 0020)

Infor ERP LN Cloud Extension Modeler (`ttext1500m000`) generates 4GL code from discrete hook blocks wrapped in `#context_on "<hook>"` ... `#context_off`. To eliminate Baan C compiler errors (`bic6.2`), developers and AI assistants MUST enforce the following guardrails:

### 3.1 Declarations Context & Header Placement (`EXT001`)
- The Extension Modeler code generator **only** routes custom code enclosed in `#context_on "declarations"` ... `#context_off` into the declarations segment of the compiled script.
- Standard generated `#include` headers (such as `<bic_dam>`, `<bic_dal2>`, `<bic_tableext>`, `<bic_text>`, `<bic_interface>`) generated under `| Additional generated declarations` are recognized as standard framework boilerplate and must remain untouched in place.
- Any **custom** `#include` header (such as custom DLLs `otxslidll...`) placed outside `#context_on "declarations"` is ignored by the code generator and triggers `EXT001 [ERROR]`.
- Whenever `dal.*` operations (`dal.change.object`, `dal.set.field`, `dal.save.object`, etc.) are invoked in extension scripts, `#include <bic_dam>` (or `<bic_dal2>`) MUST be present either in standard generated declarations or inside `#context_on "declarations"`.

### 3.2 Form Command Hook Prototypes & Void Return Constraints (`DAL002`, `DAL003`)
- **Form Command Hooks:**
  - Visibility / Enablement hooks (`.is.visible`, `.is.enabled`): Prototype MUST return `boolean` (`return(true)` / `return(false)`).
  - Command execution hooks (`.before.command`, `.after.command`): Standard prototype is `void` (or `long`).
- **Void Function Return Constraint:** In Baan 4GL, returning any expression with a value (e.g. `return(true)` or `return(0)`) from a `void` function triggers a fatal compiler error: `Return value for void function not allowed`. Always use bare `return` (or `return()`) without an argument.
- **Command Interception:** To cancel standard command execution inside a `function.<cmd>.before.command()` hook, call `choice.again()` and issue `return;`.

### 3.3 Cross-Component Hook Scope Separation (`EXT002`)
- **Table Extensions (`.est`, `^[a-z]{5}\d{3}$`):**
  - Supported: Table DAL hooks (`before.save.object`, `after.save.object`, `before.destroy.object`, `method.is.allowed`, field hooks).
  - Prohibited: Form Command hooks (`function.<cmd>.before.command`, `function.<cmd>.is.enabled`, etc.).
- **Session Extensions (`.ess`, `m\d{3}$`):**
  - Supported: Form Command hooks, session UI hooks, custom helper functions.
  - Prohibited: Table DAL lifecycle hooks (`before.save.object`, `after.save.object`, etc.).

### 3.4 Session Extension Archetype & Transaction Boundaries
- Session Extensions (`whinh4131m000.cln`, `ess`) are classified under the `general` archetype (UI program scripts).
- When a Session Extension coordinates business operations across secondary tables via DAL 2 (`dal.change.object()`), it is fully permitted to initiate and manage its own transaction boundaries (`db.retry.point()`, `commit.transaction()`, `abort.transaction()`). The auditor MUST NOT flag `DAL005` on Session Extensions.

### 3.5 Non-Context Standard Code Read-Only Boundary & Anti-Tamper (`EXT003` - ADR 0020)
- **Automatic Extension Detection:** Any 4GL script containing `#context_on` or `#context_off` directives is automatically recognized as an Extension Modeler script.
- **Strict Non-Context Read-Only Boundary:** All code outside `#context_on` ... `#context_off` blocks is strictly **Read-Only / Immutable**. AI assistants MUST NEVER modify, delete, reformat, or insert code outside context blocks. This includes:
  - Header comments and SCM metadata comments.
  - The `| Additional generated declarations` section and standard `table` declarations.
  - Standard generated framework functions: `get.extension.point.version()`, `ext.is.cdfs.of.ref.tables.selected()`, `ext.get.form.fields()`, `ext.get.session.indices()`, `ext.get.command.extensions()`, and `ext.get.report.extensions()`.
- **Strict No-Relocation Policy:** AI assistants MUST NEVER move existing code across `#context` boundaries. Do not move declarations from `| Additional generated declarations` into `#context_on "declarations"`. New custom declarations must be added inside `#context_on "declarations"`, leaving standard declarations untouched.
- **Dual-Mode Delivery:** When presenting changes:
  1. Maintain the full-fidelity cohesive `.4gl` file in the project with all standard boilerplate preserved.
  2. Output clean, individual hook code blocks in chat (stripped of `#context` tags) for 1-click pasting into LN UI (`ttext1500m000`).
