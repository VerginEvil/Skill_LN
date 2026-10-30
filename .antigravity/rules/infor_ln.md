# Infor LN & Baan 4GL Architecture Rules and Coding Guidelines

This document defines the authoritative architecture rules, coding standards, and CLI automation protocols for any engineer or AI coding assistant developing on Infor LN Studio 10.8 build 0640 (April 2026 tree) and Infor Enterprise Server.

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

When implementing features, creating tables, or debugging compilation errors, agents MUST use the unified CLI tools in `ln_studio_skill/tools/`:

### 3.1 Step 1: Component Definition & Generation
Define the table, fields, indices, and session in a YAML schema file (see `ln_studio_skill/templates/table_schema_sample.yaml`). Generate metadata directly into the target activity:

```bash
python ln_studio_skill/tools/ln_component_builder.py component --spec schema.yaml --activity "<activity_name>"
```

### 3.2 Step 2: 4GL Code Development & Synchronization
Develop Baan 4GL source in standalone `.dal` or `.cln` files in `scripts/`:
- DAL: `scripts/dal/<table_code>.dal`
- UI: `scripts/ui/<session_code>.cln`

Inject the code into workspace metadata XML:
```bash
python ln_studio_skill/tools/ln_component_builder.py inject --source scripts/dal/txptc100.dal --target "<activity_path>/tx/table/ptc/txptc100.tbl"
```

### 3.3 Step 3: Eclipse SCM Synchronization
Register new components in the activity `.admin` file:
```bash
python ln_studio_skill/tools/ln_component_builder.py sync-admin --activity "<activity_name>"
```

### 3.4 Step 4: Closed-Loop Compilation & Diagnostic Fixing
Trigger Eclipse build and inspect line-accurate compiler error markers:
```bash
python ln_studio_skill/tools/ln_component_builder.py build --activity "<activity_name>"
```

If compilation errors exist, the tool prints exact files, line numbers, and error descriptions. Fix the code in `scripts/`, re-inject, and rebuild until 0 errors are reported.

---

## 4. Pre-Fetch Authentication Verification & User Alert Guardrail (ADR 0010)

Before executing any operation that fetches, downloads, inspects, extracts, checks out, or synchronizes remote code, scripts, or components from an Infor LN server or activity (e.g. `get-component`, `sync-reference`, `checkout-component`, `extract`, `explorer`, `ln_get_component`, `ln_checkout_component`):

### 4.1 Mandatory User Notification
The AI Assistant and CLI tools MUST explicitly notify the user beforehand:
- **Target Object & Type**: e.g. Library `txibddllitem01`, Table `whwmd400`, Session `txcmg0110m100`.
- **Target Workspace & Cloud Environment**: e.g. `SCS_TST`.
- **Target Software Project & Activity**: e.g. Project `EXTce01107`, Activity `dev_natt_1107-1`.
- **Operation Mode**: In-Memory Inspection, Read-Only Fetch, or Check-Out.

### 4.2 Mandatory Authentication Pre-Flight Check & Auto-Authenticate
1. **Token Status Check**: Verify cached OAuth2 token in `~/.ln_studio/tokens/<env>.json`.
2. **Auto-Refresh**: If token is expired or within the 300s safety buffer, automatically perform silent refresh using `refresh_token`.
3. **Auto-Authenticate / Alert**: If token is missing or refresh fails:
   - Alert the user immediately that authentication is required.
   - Launch or guide the user through the self-contained multi-channel SSO login (`ln_login` / `ln_auth_helper.py` via Windows `oob://` protocol handler or clipboard detection).
4. **Resilience**: Never fail silently or crash unexpectedly without alerting the user of the authentication and connection status.

---

## 5. Extension Modeler (`ttext1500m000`) Compiler Rules & Static Guardrails (ADR 0013)

Infor ERP LN Cloud Extension Modeler (`ttext1500m000`) generates 4GL code from discrete hook blocks wrapped in `#context_on "<hook>"` ... `#context_off`. To eliminate Baan C compiler errors (`bic6.2`), developers and AI assistants MUST enforce the following guardrails:

### 5.1 Declarations Context & Header Placement (`EXT001`)
- The Extension Modeler code generator **only** routes code enclosed in `#context_on "declarations"` ... `#context_off` into the declarations segment of the compiled script.
- Any `#include` header (such as `<bic_dam>`, `<bic_dal2>`, `<bic_sessionext>`, `<bic_tableext>`, `<bic_text>`) placed outside `#context_on "declarations"` is ignored by the code generator, resulting in compiler failures (`Unresolved reference to function 'dal.*'`).
- Whenever `dal.*` operations (`dal.change.object`, `dal.set.field`, `dal.save.object`, etc.) are invoked in extension scripts, `#include <bic_dam>` (or `<bic_dal2>`) MUST be present inside `#context_on "declarations"`.

### 5.2 Form Command Hook Prototypes & Void Return Constraints (`DAL002`, `DAL003`)
- **Form Command Hooks**:
  - Visibility / Enablement hooks (`.is.visible`, `.is.enabled`): Prototype MUST return `boolean` (`return(true)` / `return(false)`).
  - Command execution hooks (`.before.command`, `.after.command`): Standard prototype is `void` (or `long`).
- **Void Function Return Constraint**: In Baan 4GL, returning any expression with a value (e.g. `return(true)` or `return(0)`) from a `void` function triggers a fatal compiler error: `Return value for void function not allowed`. Always use bare `return` (or `return()`) without an argument.
- **Command Interception**: To cancel standard command execution inside a `function.<cmd>.before.command()` hook, call `choice.again()` and issue `return;`.

### 5.3 Cross-Component Hook Scope Separation (`EXT002`)
- **Table Extensions (`.est`, `^[a-z]{5}\d{3}$`)**:
  - Supported: Table DAL hooks (`before.save.object`, `after.save.object`, `before.destroy.object`, `method.is.allowed`, field hooks).
  - Prohibited: Form Command hooks (`function.<cmd>.before.command`, `function.<cmd>.is.enabled`, etc.).
- **Session Extensions (`.ess`, `m\d{3}$`)**:
  - Supported: Form Command hooks, session UI hooks, custom helper functions.
  - Prohibited: Table DAL lifecycle hooks (`before.save.object`, `after.save.object`, etc.).

### 5.4 Session Extension Archetype & Transaction Boundaries
- Session Extensions (`whinh4131m000.cln`, `ess`) are classified under the `general` archetype (UI program scripts).
- When a Session Extension coordinates business operations across secondary tables via DAL 2 (`dal.change.object()`), it is fully permitted to initiate and manage its own transaction boundaries (`db.retry.point()`, `commit.transaction()`, `abort.transaction()`). The auditor MUST NOT flag `DAL005` on Session Extensions.


