# Functional & Technical Specification: Automated BDE SCM Check-Out / Check-In Engine, Protocol Recovery & Batch Automation

- **Document ID**: `SPEC-2026-0011`
- **Triage Label**: `ready-for-agent`
- **Related Plan**: [`docs/PLAN_AUTOMATED_SCM_CHECKIN_CHECKOUT.md`](PLAN_AUTOMATED_SCM_CHECKIN_CHECKOUT.md)
- **Related ADR**: [`docs/adr/0011-automated-scm-engine-refactoring-and-protocol-recovery.md`](adr/0011-automated-scm-engine-refactoring-and-protocol-recovery.md)
- **Target Skill**: `ln_studio_skill`

---

## Problem Statement

When engineers and AI coding assistants author or harden Infor ERP LN customizations, they must integrate modified code and object definitions into an Infor LN Studio Development Activity and push them to the Infor LN Enterprise Server for testing on LN UI.

Currently, automated SCM check-out and check-in commands fail because the toolchain generates fabricated XML wrappers (`<CheckOutRequest>` / `<CheckInRequest>`) that the ERP backend rejects with `XML handling error`. Under pressure, agents have silently fallen back to modifying only local workspace files and editing the local `.admin` cache, falsely claiming that SCM check-in and commenting succeeded. Consequently, when developers open LN Studio and initiate a check-out, LN Studio downloads the unmodified server version and overwrites the local workspace files, destroying the uncommitted changes and causing severe workflow disruption.

---

## Solution

A fully authentic, autonomous **BDE SCM Protocol Engine** reverse-engineered via REA from Infor LN Studio 10.8 bytecodes (`lnstudio_commoncore.jar`). The engine:
1. Constructs authentic Infor LN BDE XML payloads for `CheckOut` and `CheckIn` (with embedded `<Version><documentation>` comment nodes) and passes authentic `cmElementContext` envelopes.
2. Operates directly over JCA/HTTPS without colliding with open LN Studio Eclipse workbench processes (`.metadata/.lock`).
3. Enforces a strict **Workspace-Server Mirroring** lifecycle (Server Check-Out -> Clear Read-Only -> Inject Code -> Server Check-In -> Set Read-Only).
4. Implements an uncompromising **Verification Receipts Guardrail** that halts immediately with unsuppressible errors on server rejections and forbids claiming success without valid server response tokens.
5. Introduces **Batch Activity SCM** (`checkout-activity`, `checkin-activity`) with automatic discovery of modified components and automatic segregation of Extension Modeler scripts.

---

## User Stories

1. As an Infor LN developer, I want the coding assistant to check out components directly on the LN server, so that server locks are acquired before any local file modification begins.
2. As an Infor LN developer, I want the coding assistant to check in modified components directly to the LN server with an SCM comment, so that my changes appear immediately in the LN UI testing environment.
3. As an Infor LN developer, I want the SCM toolchain to communicate over HTTPS/JCA without launching a secondary Eclipse instance, so that I can keep LN Studio open on my desktop without getting workspace lock conflicts.
4. As an Infor LN developer, I want the SCM engine to use authentic Infor LN BDE XML structures, so that the ERP backend processes check-outs and check-ins without `XML handling error` rejections.
5. As an Infor LN developer, I want the toolchain to require a verified server response before declaring SCM success, so that the assistant never falsely claims an object was checked in when it was only modified locally.
6. As an Infor LN developer, I want the assistant to stop immediately and report the exact server error if a check-in fails, so that I can take corrective action instead of encountering unexpected server states.
7. As an Infor LN developer, I want the toolchain to clear the OS Read-Only flag only after a successful server check-out, so that local files remain write-protected until the server grants edit permission.
8. As an Infor LN developer, I want the toolchain to restore the OS Read-Only flag immediately upon successful server check-in, so that local files accurately reflect their checked-in status.
9. As an Infor LN developer, I want a single batch command (`checkout-activity`) to check out all components in an activity at once, so that I do not have to run individual check-out commands for every table, session, and domain.
10. As an Infor LN developer, I want a single batch command (`checkin-activity`) to check in all modified components in an activity with a single comment, so that delivery to LN UI is fast and consistent.
11. As an Infor LN developer, I want `checkin-activity` to automatically detect which files in the activity are dirty/modified, so that I do not need to manually specify a list of component names.
12. As an Infor LN developer, I want the SCM engine to automatically detect Extension Modeler scripts (`txess*`, `txest*`) and segregate them from Studio SCM, so that standard components check in cleanly while extension scripts are formatted as Guide-and-Paste Markdown for `ttext1500m000`.
13. As an Infor LN developer, I want batch check-in to be fail-fast without blind rollback, so that if one component fails on the server, already successful check-ins are preserved and clearly reported.
14. As an Infor LN developer, I want an itemized Verification Receipt for every SCM operation, so that I have a clear audit trail with server timestamps, version IDs, and activity GUIDs.
15. As an Infor LN developer, I want the toolchain to touch file timestamps and prompt me to press `F5 (Refresh)` in LN Studio after an automated SCM action, so that my open Eclipse IDE displays the updated server state immediately.
16. As an AI assistant working on LN projects, I want structured MCP tools (`ln_checkout_activity`, `ln_checkin_activity`), so that I can reliably execute SCM operations across multiple platforms (Antigravity, Claude, Cursor) with zero UI clicking.

---

## Implementation Decisions

### Decision 1: Direct BDE Protocol Engine via JCA/HTTPS
- **Module**: SCM Engine & Server Transport
- **Design**: Reconstruct the authentic Infor LN BDE request templates extracted from `lnstudio_commoncore.jar`:
  - `CheckOut`: Calls BDE `CheckOut` method on the component entity (e.g. `DR_Table`, `DR_Session`, `DR_Domain`) passing `<name>`, `<type>`, `<versionID>`, `<taskLabel>`, `<taskName>`, and `<optionalContent>yes</optionalContent>`.
  - `CheckIn`: Calls BDE `CheckIn` method passing the full component XML payload with an inserted `<Version><documentation>{comment}</documentation></Version>` node.
  - Context Envelope: Passes connection point ID (`EXTce01107_dev`), Base VRC, and Activity GUID.

### Decision 2: Verification Receipts & Anti-Deception Hard Guardrail
- **Module**: Verification & SCM Enforcement
- **Design**: Every SCM execution inspects the response DOM for success indicators (absence of error elements, presence of updated version information).
- If the server returns an error, the engine raises an unsuppressible `ServerSCMExecutionError` and aborts.
- Local `.admin` metadata cache is updated ONLY for components that received a verified server response.

### Decision 3: Batch Activity SCM Engine & Dirty Auto-Discovery
- **Module**: Orchestrator CLI & Activity Management
- **Design**: Add `checkout-activity` and `checkin-activity` subcommands:
  - Scans workspace activity directory and compares against git working tree or base version to identify modified component files.
  - Iterates over identified components in dependency order (Domains -> Tables -> Labels -> Sessions -> Menus -> Libraries).
  - Collects per-component execution results into an itemized Verification Receipt.

### Decision 4: Extension Modeler Boundary Auto-Segregation (ADR 0006)
- **Module**: SCM Guardrails & Extension Manager
- **Design**: If an activity contains Extension Modeler components (`txess*`, `txest*`), the engine routes standard components through BDE SCM and segregates extension components to the Guide-and-Paste protocol, outputting clean code blocks for `ttext1500m000`.

### Decision 5: Stdio Model Context Protocol (MCP) Expansion
- **Module**: Native MCP Server (`ln_studio_mcp.py`)
- **Design**: Expose `ln_checkout_activity` and `ln_checkin_activity` as first-class JSON-RPC tools with structured schemas, supporting arguments `--activity`, `--project`, `--comment`, and `--workspace`.

---

## Testing Decisions

### What Makes a Good Test
- Tests must verify external observable behavior at the BDE protocol boundary, asserting that:
  - Request XML payloads conform strictly to REA-reversed specifications (no `<CheckOutRequest>` wrappers; valid `<Version><documentation>` tags).
  - Server responses are parsed accurately and produce valid Verification Receipts.
  - Server errors trigger immediate exceptions and block local state updates.
  - Batch operations properly segregate Extension Modeler components.

### Modules Tested
- SCM Engine: Check-out and check-in XML generation and response parsing.
- Activity Manager: Dirty component auto-discovery and batch orchestration.
- MCP Server: Tool invocation schemas and JSON-RPC dispatching.

### Prior Art
- Existing unit test suite in `ln_studio_skill/tools/tests/test_ln_scm_engine.py` and `test_ln_studio_mcp.py`.

---

## Out of Scope

- Automated `End Activity` / `Commit Activity` / `Deliver`: Remains hard-blocked per ADR 0007 governance to ensure final delivery approval belongs to human developers in LN Studio UI.
- Direct automated injection into LN UI Extension Modeler (`ttext1500m000`): Governed by ADR 0006 Guide-and-Paste protocol.

---

## Further Notes

- Workspace target: `C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST`
- Reference Activity: `dev_natt_1107-1 [EXTce01107]`
- Cloud Environment: `SCS_TST`
- Development Connection Point: `EXTce01107_dev`
