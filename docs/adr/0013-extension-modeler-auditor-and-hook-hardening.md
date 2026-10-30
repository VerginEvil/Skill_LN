# ADR 0013: Extension Modeler (`ttext1500m000`) Auditor Hardening, Context Include Boundaries (`EXT001`), and Cross-Type Hook Scope Enforcement (`EXT002`)

- **Status**: Accepted
- **Date**: 2026-10-30
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`
- **Prior ADRs**:
  - [`docs/adr/0006-ln-studio-extension-readonly-and-lnui-workflow.md`](0006-ln-studio-extension-readonly-and-lnui-workflow.md) *(Extension Modeler Boundary & #context_on Syntax)*
  - [`docs/adr/0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md`](0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md) *(Semantic/AST 4GL Auditor & Rule System)*

---

## 1. Context & Problem Statement

Production usage of Infor ERP LN Cloud / Extension Modeler (`ttext1500m000`) revealed four critical compilation and validation defects:

1. **`Return value for void function ... not allowed` in Form Command Hooks**:
   Infor LN Extension Modeler defines `function.<command>.before.command` with a standard **`void`** prototype. In Baan 4GL, returning an expression (`return(true)`) in a void function is a fatal compiler error (`Return value for void function '<func_name>' not allowed`). The auditor previously misclassified `.before.command` as requiring a `boolean` return under `DAL002`, and the project scaffolding template generated invalid `return(true)` code.
2. **`Unresolved reference to function 'dal.*'` due to `#include` outside `#context_on "declarations"`**:
   Extension Modeler's code generator only feeds source inside `#context_on "declarations"` ... `#context_off` into the compiled declarations segment. Placing `#include <bic_dam>` or `#include <bic_dal2>` outside this block strips function prototypes during compilation, causing unresolved reference failures for `dal.change.object()`, `dal.set.field()`, and `dal.save.object()`.
3. **False-Positive `DAL005` Transaction Control Errors on Session Extensions**:
   When a Session Extension (`whinh4131m000.cln`, `ess`) interacts with DAL 2 to update related tables, including `<bic_dal2>` previously caused `detect_archetype()` to classify the file as `"dal2"`. This triggered `DAL005` ("Transaction control 'db.retry.point()' is prohibited in DAL/Table Extension hooks"), preventing session extensions from executing necessary transaction boundaries.
4. **Scope Mismatch across Table and Session Extensions**:
   Table Extensions (`est`) mistakenly allowed Form Command hooks, and Session Extensions (`ess`) allowed Table DAL hooks, causing silent deployment errors or invalid runtime hook registrations.

---

## 2. Settled Architectural Decisions

### Decision 1: Form Command Hook Prototypes & Void Return Value Verification (`DAL002` & `DAL003`)
1. **Accurate Command Hook Return Types (`DAL002`)**:
   - `function.<command>.is.visible`: MUST return `boolean`.
   - `function.<command>.is.enabled`: MUST return `boolean`.
   - `function.<command>.before.command`: MUST return `void` or `long` (or unannotated void).
   - `function.<command>.after.command`: MUST return `void` or `long` (or unannotated void).
2. **Void Return Value Prevention (`DAL003`)**:
   - In any function or hook declared with a `void` return type (or defaulting to void), executing `return(expression)` with a non-empty expression is flagged as an `ERROR` (`DAL003`). Only bare `return` or `return()` without an expression is permitted.

### Decision 2: Session Extension Archetype Classification (`general` mode)
1. **Explicit Session Extension Detection**:
   - Files matching session patterns (`[a-z]{5}\d{3}[ms]\d{3}` or `m\d{3}` in filename, path containing `session` or `ess`, `#include <bic_sessionext>` or `<bic_interface>`, or containing Form Command hooks) are classified as `"general"` mode.
   - Including `<bic_dal2>` or `<bic_dam>` in a Session Extension does NOT switch the script to `"dal2"` mode. Session extensions are fully permitted to manage outer transactions (`db.retry.point()`, `commit.transaction()`) when coordinating DAL operations on other tables.

### Decision 3: Rule `EXT001` (Extension Modeler Declarations Include Boundary)
1. **`#include` Placement Inside Declarations Context**:
   - In extension scripts, all `#include` directives must reside inside `#context_on "declarations"` ... `#context_off`. Direct `#include` statements outside this block are flagged with `EXT001 [ERROR]`.
2. **DAL Include Requirement for Extension Modeler**:
   - Any extension script invoking `dal.change.object`, `dal.set.field`, `dal.save.object`, `dal.new.object`, or `dal.destroy.object` MUST have `#include <bic_dam>` or `#include <bic_dal2>` declared inside `#context_on "declarations"`. Missing includes are flagged with `EXT001 [ERROR]`.

### Decision 4: Rule `EXT002` (Extension Hook Scope Enforcement)
1. **Table Extension Hook Restrictions**:
   - Table Extensions (`whinh431.cln`, `est`) only support Table DAL hooks. Declaring Form Command hooks (`function.*.command`, `function.*.is.enabled`, `function.*.is.visible`) triggers `EXT002 [ERROR]`.
2. **Session Extension Hook Restrictions**:
   - Session Extensions (`whinh4131m000.cln`, `ess`) only support Form Command hooks and UI logic. Declaring Table DAL hooks (`before.save.object`, `after.save.object`, `method.is.allowed`, `is.valid`, etc.) triggers `EXT002 [ERROR]`.

### Decision 5: Scaffolding Template & Toolchain Alignment
1. **Corrected Scaffolding Template**:
   - `session_extension_template.4gl` is updated to define `function extern void function.custom.action.before.command()` with no return statement and clear `choice.again()` cancellation documentation.
2. **Synchronized Static Checkers**:
   - Both `erp-ln-progguide/scripts/audit_4gl.py` and `ln_studio_skill/tools/check_4gl_script.py` enforce identical `DAL002`, `DAL003`, `EXT001`, and `EXT002` diagnostics.
