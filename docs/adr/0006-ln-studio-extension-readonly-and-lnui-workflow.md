# ADR 0006: Infor LN Extension Modeler Boundary: LN Studio Read-Only "Get" Mode and Local Project Hook Workflow

- **Status**: Accepted
- **Date**: 2026-10-26
- **Target Skills**: `ln_studio_skill` and `erp-ln-progguide`
- **Specification**: [`docs/SPEC_LN_STUDIO_EXTENSION_READONLY_AND_LNUI_WORKFLOW.md`](../SPEC_LN_STUDIO_EXTENSION_READONLY_AND_LNUI_WORKFLOW.md)
- **Implementation Plan**: [`docs/PLAN_LN_STUDIO_EXTENSION_READONLY_AND_LNUI_WORKFLOW.md`](../PLAN_LN_STUDIO_EXTENSION_READONLY_AND_LNUI_WORKFLOW.md)
- **Prior ADRs**:
  - [`docs/adr/0001-plan-skill-update-and-coding-best-practices.md`](0001-plan-skill-update-and-coding-best-practices.md)
  - [`docs/adr/0002-ln-studio-skill-self-contained-toolchain.md`](0002-ln-studio-skill-self-contained-toolchain.md)
  - [`docs/adr/0003-ln-studio-object-modeling-and-static-verification.md`](0003-ln-studio-object-modeling-and-static-verification.md)
  - [`docs/adr/0004-4gl-coding-standards-and-caveats.md`](0004-4gl-coding-standards-and-caveats.md)
  - [`docs/adr/0005-progguide-studio-dictionaries-and-audit-engine.md`](0005-progguide-studio-dictionaries-and-audit-engine.md)

---

## 1. Context & Problem Statement

In Infor ERP LN 10.8+, the **Extension Modeler (`ttext1500m000`)** in LN UI (Web UI) is the authoritative environment for creating, editing, and compiling last-mile extensions (Table Extensions `est`, Session Extensions `ess`, Report Extensions `esr`, BOD Extensions `esb`, Menu Extensions `esm`).

### Verified Runtime Behavior:
Attempting to check out an extension component (e.g. `txesswmd4300m0` for session extension of `whwmd4300m000`) in Infor LN Studio fails with the authoritative SCM message:
```text
Failure checking-out the component
Action on "txesswmd4300m0" is not allowed.
Use session ttext1500m000 to process extensions.
```

### Critical Flaws in Prior Approach:
1. **Misguided Workspace Modifications**: Prior versions of `ln_studio_skill` allowed generating and injecting `.lib` XML files for `session_extension` and `table_extension` into the LN Studio activity workspace.
2. **Futile SCM Check-Out**: Extensions cannot be checked out or checked in via LN Studio SCM. In Studio, extension objects are strictly available via "Get" for read-only viewing and debugging.
3. **Dead-End Edits**: Any attempt by an AI agent or engineer to edit or inject 4GL scripts into `.lib` files in the LN Studio workspace is ineffective because LN Studio does not compile or sync them back to the server's Extension Modeler tables.

---

## 2. Settled Decisions (Rounds 1, 2, and 3)

### Decision 1: Strict Seam & Read-Only Policy for Extensions in LN Studio
Extension Modeler objects (`tx*`, `ess`, `est`, `esr`, `esb`, `esm`) in the LN Studio workspace are strictly **Read-Only / Get-Only**. Agents and developers must never attempt to check out, inject, or edit `.lib` files in the Studio workspace. Workspace access is reserved solely for viewing code pulled from the server or attaching the Eclipse 4GL debugger.

### Decision 2: Deprecate Workspace Extension Generation in Favor of Local Project Authoring
Deprecate generating `.lib` XML files for extensions inside the LN Studio activity workspace. Extension source code must be authored and maintained directly within the local project repository (under Git version control). Standard DLL libraries (`--type dll` in `<pkg>/library/<mod>/`) remain supported in Studio workspace.

### Decision 3: Unified Local Extension File Format (`#context_on` Syntax)
Store extension code in the local project as a single, cohesive `.4gl` file per extended component (e.g., `extensions/<type>/<component>_ext.4gl`). Delimit individual lifecycle hooks using Infor LN's native `#context_on "<hook_name>"` ... `#context_off` block directives, ensuring readability and 1-to-1 parity with server-generated scripts.

### Decision 4: Hook-Level Partitioning for LN UI (`ttext1500m000`) Delivery
Because LN UI `ttext1500m000` requires entering code hook-by-hook in dedicated modal windows, the toolchain and agents must present extension code partitioned into clean, individual hook blocks (e.g., `declarations`, `functions`, `before.save.object`, `is.valid`), stripped of `#context_on` wrappers, with clear target directions.

### Decision 5: Offline Static Verification for Project Extensions
Enhance `check_4gl_script.py` and `audit_4gl.py` to validate local extension files against syntax, balanced blocks, hook signatures, and Cloud Governance rules (e.g. no interactive `message()` in table extensions, no nested transaction commits) before deploying to LN UI.

### Decision 6: One-Way Import Bridge from LN Studio "Get" (`import-extension`)
Provide an `import-extension` tool that reads an extension component pulled down into an LN Studio activity workspace via "Get", parses its `#context_on` blocks, and generates a clean, maintainable `.4gl` file in the local project repository.

### Decision 7: Authoritative SCM Guardrail Interception
Update `scm_guardrails.py` and `inject_ln_script.py` to intercept any write action on `tx*` components, raising the exact Infor LN Studio error:
```text
Failure checking-out the component: Action on "<component>" is not allowed. Use session ttext1500m000 to process extensions.
```
Configure `validate_ln_activity.py` to mark `tx*` components as `[GET_ONLY_EXTENSION]` so they never trigger false-positive SCM checkout errors.

### Decision 8: Hook Inspection & Clipboard CLI (`extension-hooks`)
Provide a CLI command (`python tools/ln_component_builder.py extension-hooks <file.4gl> [--hook <name>] [--copy]`) to inspect all hooks declared in an extension file, display clean hook code, and optionally copy a specific hook directly to the OS clipboard.

### Decision 9: Project Extension Scaffolding CLI (`new-extension`)
Introduce CLI command (`python tools/ln_component_builder.py new-extension --type <table|session> --target <name> [--output <path>]`) backed by official templates (`templates/table_extension_template.4gl`, `templates/session_extension_template.4gl`) to bootstrap ready-to-code local extension files.

### Decision 10: Agent "Guide-and-Paste" Protocol
Document the mandatory agent behavioral protocol in `SKILL.md`: when asked to write or modify an extension, agents must:
1. Write or edit the 4GL file in the local project repository.
2. Run offline validation (`check_4gl_script.py`).
3. Provide step-by-step guidance in chat specifying the exact navigation in LN UI (`ttext1500m000` -> Component -> Hook Name) and provide clean code blocks for 1-click copy-pasting.
4. Warn the user never to check out or edit this component in LN Studio.

### Decision 11: Clean Guardrail in `generate_ln_library.py`
Refuse `--type session_extension` and `--type table_extension` when targeting a Studio workspace directory, directing users to `new-extension`, while keeping `--type dll` intact for standard 3GL/DLL components.

---

## 3. Architecture Comparison

| Dimension | Legacy / Erroneous Approach | New Authoritative Approach (ADR 0006) |
|---|---|---|
| **Extension Coding Location** | LN Studio Workspace XML (`.lib` inside activity) | Local Project Repository (`extensions/.../*.4gl`) |
| **LN Studio Role** | Erroneously treated as editable/injectable | Strictly Read-Only / "Get" for viewing & debugging |
| **SCM Behavior in Studio** | Attempted check-out (crashed with `Action not allowed`) | Guarded by `scm_guardrails.py`; skips SCM verification in `validate` |
| **Server Deployment** | Attempted Studio build (ignored by Extension Modeler) | Manual 1-click Copy-Paste into LN UI (`ttext1500m000`) |
| **Code Partitioning** | Monolithic XML `<expression>` string | Structured `#context_on` blocks & Hook-by-Hook CLI output |
| **Verification Gate** | None or only workspace-wide validator | Offline `check_4gl_script.py` validating hooks & Cloud Governance |
| **Scaffolding Tool** | `generate_ln_library.py` (created workspace XML) | `new-extension` CLI (creates local project 4GL with templates) |
