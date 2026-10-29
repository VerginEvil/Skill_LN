# ADR 0010: Pre-Fetch Server Authentication Verification Guardrail and User Notification Protocol

- **Status**: Accepted
- **Date**: 2026-10-29
- **Target Skills**: `ln_studio_skill`
- **Prior ADRs**:
  - [`docs/adr/0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md`](0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md)
  - [`docs/adr/0009-infor-cloudsuite-oauth2-login-and-oob-protocol-resolution.md`](0009-infor-cloudsuite-oauth2-login-and-oob-protocol-resolution.md)

---

## 1. Context & Problem Statement

When AI assistants and CLI tools pull, inspect, download, check out, or synchronize code or object definitions from Infor LN Cloud servers or Activity workareas:
1. **Unnotified Operations**: Users had no advance visibility into which object was being accessed, from which server, or into which workspace activity.
2. **Abrupt Unauthenticated Failures**: If an OAuth2 token had expired or was missing, operations failed abruptly with low-level network or permission errors instead of performing a pre-flight authentication verification or prompting/launching authentication.
3. **Activity Lock & Target Ambiguity**: Missing activity context or wrong workspace selection resulted in confusing error messages from bshell or JCA.

---

## 2. Settled Architectural Decisions

### Decision 1: Mandatory Pre-Fetch User Alert
Before executing any retrieval operation (`get-component`, `sync-reference`, `checkout-component`, `clone-component`, `explorer`, `ln_get_component`, `ln_checkout_component`), the assistant or toolchain MUST notify the user with clear target metadata:
- **Target Object & Type**: Name and component type (e.g. `txibddllitem01` [library/DLL], `tcibd001` [table]).
- **Workspace & Cloud Environment**: Target workspace name and mapped Infor CloudSuite tenant.
- **Activity / WorkSet**: Target Development Activity folder (e.g. `dev_natt_1107-1 [EXTce01107]`).
- **Operation Mode**: In-Memory Inspection, Read-Only Fetch, or Check-Out.

Example Banner:
```text
[PRE-FETCH ALERT] Accessing Infor LN Server / Activity:
  Target:     library 'txibddllitem01' | Activity: dev_natt_1107-1
  Workspace:  SCS_TST (CloudEnv: SCS_TST)
```

### Decision 2: Pre-Flight Authentication Verification & Auto-Authenticate (`ensure_authenticated_token`)
All server client resolution routines (`get_server_client`, `_resolve_client` in MCP) route through `OAuth2TokenManager.ensure_authenticated_token`:
1. **Token Health Inspection**: Checks `check_token_status(env_name)` against cached tokens in `~/.ln_studio/tokens/<env>.json`.
2. **Silent Refresh**: If the token is near expiry (within 300s safety buffer) or expired, automatically invokes `refresh_access_token` and notifies the user (`[AUTH STATUS] Token successfully refreshed`).
3. **Auto-Authenticate Flow**: If no token exists or silent refresh fails:
   - Emits an alert: `[AUTH ALERT] Authentication required for '<env>'. Initiating SSO login flow...`.
   - Launches `execute_login` with the registered Windows `oob://` protocol handler and clipboard auto-detect.
   - Updates token cache and proceeds with the requested operation seamlessly.
4. **Resilience & Non-Crashing Guarantee**: If auto-login is disabled, provides an actionable `PermissionError` explaining how to log in via CLI or browser instead of crashing unexpectedly.
