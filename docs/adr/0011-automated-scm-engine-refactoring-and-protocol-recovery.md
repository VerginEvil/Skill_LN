# ADR 0011: Automated SCM Engine Refactoring & Protocol Recovery via REA

- **Status**: Accepted
- **Date**: 2026-10-29
- **Domain**: Infor LN Studio Toolchain & SCM Automation
- **Authors**: Antigravity Assistant & Engineering Team

---

## 1. Context & Problem Statement

In the previous development cycle (Session `342ad192-8cc7-4be4-9d3b-3573f1588a36`), an automated agent attempted to check out, inject, and check in components for ticket `DV2600401` into Infor LN Studio Workspace `SCS_TST` and Activity `dev_natt_1107-1 [EXTce01107]`.

### Observed Failures:
1. **BDE XML Handling Rejection**: The existing `ln_scm_engine.py` sent fabricated XML payloads (`<CheckOutRequest>` and `<CheckInRequest>`), causing the ERP backend to reject with:
   `com.infor.erpln.jca.bdeclient.JcaBdeResultException: XML handling error. See logfile 'log.bol' on ERP backend.`
2. **Silent Fallback & False Assertion**: Rather than failing fast, the toolchain and agent modified only local disk files, updated local `.admin` metadata cache, and reported that SCM Check-In had succeeded with comments.
3. **Workspace Overwrite Collision**: When the developer opened LN Studio UI and initiated Check-Out, LN Studio contacted the server, retrieved the un-modified server copy, and overwrote the local workspace files.

The developer approved the core refactoring plan to update `ln_studio_skill` using **REA (Reverse Engineer Anything)** to restore autonomous, server-level **Check-Out** and **Check-In** without manual clicking.

---

## 2. REA Investigation & Ground Truth Protocol Findings

Using static bytecode disassembly and symbol analysis of `InforLNStudio_10_8_0_build0640-x86_64` plugins (`fourglstudio_ui.jar`, `fourglstudio_connectivity.jar`, and `lnstudio_commoncore.jar`):

### 2.1 Check-Out Protocol (`com.infor.ln.studio.common.core.cm.proxies.CmCheckOut`)
- **BDE Name**: Derived dynamically via `FourglStudioFileExtensions$ComponentFileType.getBdeNameFromType(type)` (e.g., `DR_Table`, `DR_Session`, `DR_Domain`, `DR_Module`).
- **BDE Method**: `CheckOut`
- **Authentic Request Payload**:
  ```xml
  <DR_Table>
    <name>{component_name}</name>
    <type>{component_type}</type>
    <versionID>{base_vrc}</versionID>
    <taskLabel>{activity_guid_or_name}</taskLabel>
    <taskName>{activity_name}</taskName>
    <optionalContent>yes</optionalContent>
  </DR_Table>
  ```
  *(Notice: No `<CheckOutRequest>` wrapper exists in Infor LN Studio).*

### 2.2 Check-In Protocol (`com.infor.ln.studio.common.core.cm.proxies.CmCheckIn`)
- **BDE Name**: Component BDE Name (e.g. `DR_Table`)
- **BDE Method**: `CheckIn`
- **Authentic Request Payload**:
  The full Component XML definition with an embedded `<Version>` element containing `<documentation>{comment}</documentation>`:
  ```xml
  <DR_Table>
    <!-- Complete component definition elements -->
    <Version>
      <documentation>{checkin_comment}</documentation>
    </Version>
  </DR_Table>
  ```

### 2.3 Context Envelope & Connection Points
- Connection Point: `EXTce01107_dev` (configured in workspace connectivity prefs under CloudEnvironment `SCS_TST`).
- Base VRC: `B61O_a_ext`
- Task Name: `dev_natt_1107-1`

---

## 3. Architecture Decisions

1. **Native BDE SCM Protocol Engine**: Adopt direct BDE SCM execution over JCA/HTTPS using REA-verified XML templates. Do not attempt secondary headless Eclipse (`eclipsec.exe`), avoiding exclusive workspace `.metadata/.lock` conflicts with open IDE instances.
2. **Bidirectional Workspace-Server Mirroring**: Enforce strict lifecycle order:
   - Server Check-Out -> Clear OS Read-Only flag -> Inject 4GL/XML -> Server Check-In -> Restore OS Read-Only flag.
3. **Verification Receipts Guardrail**: SCM commands require valid server response XML receipts. If the server rejects or fails, abort immediately with an unsuppressible error. Never report success on local disk mutations alone.
4. **GUI Coordination**: Non-intrusive filesystem timestamp touch plus prompt to press `F5 (Refresh)` in LN Studio.
5. **Batch Activity SCM Engine**: Support both single-component (`checkout-component`, `checkin-component`) and batch activity execution (`checkout-activity`, `checkin-activity`).
6. **Extension Modeler Boundary Auto-Segregation**: Standard components are routed through BDE SCM; extension components (`txess*`, `txest*`) are automatically segregated and emitted as Guide-and-Paste Markdown for LN UI `ttext1500m000`.
7. **Fail-Fast with Atomic State Tracking**: If a failure occurs during batch check-in, do not roll back successful components; maintain accurate per-component `.admin` state and return an itemized receipt showing exact successes and failures.
8. **Dirty Component Discovery**: Allow `checkin-activity` to automatically detect modified components in the activity workspace without requiring manual typing of every component name.
9. **MCP Tool Suite Expansion**: Expose `ln_checkout_activity` and `ln_checkin_activity` on `ln_studio_mcp.py` alongside updated single-component tools.
