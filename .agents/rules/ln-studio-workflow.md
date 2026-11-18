---
trigger: model_decision
description: Infor LN Studio CLI/MCP automation workflows, component XML generation, Eclipse SCM sync/build, and Pre-Fetch-Auth-Gate OAuth2 guardrails. Load when managing LN Studio workspaces, generating components, interacting with Infor LN servers, or running skill-ln / ln_component_builder commands.
---

# Infor LN Studio Automation & Server Auth Guardrails

Workflows and mandatory authentication guardrails for Infor LN Studio 10.8 build 0640 automation (`skill-ln` CLI / MCP server and `.agents/skills/ln_studio_skill/tools/`).

---

## 1. Automation Toolchain Workflows for AI Agents

Use the native Rust binary `skill-ln` (primary) or Python equivalent (`.agents/skills/ln_studio_skill/tools/ln_component_builder.py`):

### 1.1 Component Definition & Generation
Define tables, fields, indices, and sessions in `schema.yaml` (see `.agents/skills/ln_studio_skill/templates/table_schema_sample.yaml`):
```bash
skill-ln component --spec schema.yaml --activity "<activity_path>"
```

### 1.2 4GL Code Development & Injection
Develop Baan 4GL source in standalone `.dal` / `.cln` files and inject into Single-Line TDE XML:
```bash
skill-ln inject --source scripts/dal/txptc100.dal --target "<activity_path>/tx/table/ptc/txptc100.tbl"
```

### 1.3 SCM Sync, Validation & Pre-Commit Handoff
```bash
skill-ln sync-admin --activity "<activity_path>"
skill-ln validate "<activity_path>" --fix --online
skill-ln deploy-test --type table --name txptc100 --activity "<activity_path>" --mode compile-only --comment "Test"
skill-ln prepare-end-activity --activity "<activity_path>"
```
After partial or full `End Activity` in Studio UI, refresh server-committed VRCs without overwriting local `CheckedOut`/`Dirty` edits:
```bash
skill-ln sync-activity --activity "<activity_path>"
```

### 1.4 Cross-Runtime Parity & Reuse Reviewer Standard
- Whenever adding or changing behavior in `ln_studio_skill/tools/*.py` or `rust/crates/*`, verify CLI and Stdio MCP parity across both runtimes (subcommand flags, JSON fields, and `MCP_TOOLS_REFERENCE.md` schema).
- Reuse existing shared helpers (e.g., `ensure_label_context_variant`, `compact_tde_xml`, `map_tde_extension_to_type`) rather than duplicating mapping or XML surgery code.

---

## 2. Pre-Fetch Authentication Verification & User Alert Guardrail (`Pre-Fetch-Auth-Gate` - ADR 0010)

Before executing any operation that fetches, downloads, inspects, extracts, checks out, or synchronizes remote code, scripts, or components from an Infor LN server or activity (e.g. `get-component`, `sync-reference`, `checkout-component`, `extract`, `explorer`, `ln_get_component`, `ln_checkout_component`):

### 2.1 Mandatory User Notification
The AI Assistant and CLI tools MUST explicitly notify the user beforehand:
- **Target Object & Type**: e.g. Library `txibddllitem01`, Table `whwmd400`, Session `txcmg0110m100`.
- **Target Workspace & Cloud Environment**: e.g. `PRD_ENV`.
- **Target Software Project & Activity**: e.g. Project `EXTce01107`, Activity `dev_natt_1107-1`.
- **Operation Mode**: In-Memory Inspection, Read-Only Fetch, or Check-Out.

### 2.2 Mandatory Authentication Pre-Flight Check & Auto-Authenticate
1. **Token Status Check**: Verify cached OAuth2 token in `~/.ln_studio/tokens/<env>.json`.
2. **Auto-Refresh**: If token is expired or within the 300s safety buffer, automatically perform silent refresh using `refresh_token`.
3. **Auto-Authenticate / Alert**: If token is missing or refresh fails:
   - Alert the user immediately that authentication is required.
   - Launch or guide the user through the self-contained multi-channel SSO login (`ln_login` / `ln_auth_helper.py` via Windows `oob://` protocol handler or clipboard detection).
4. **Resilience**: Never fail silently or crash unexpectedly without alerting the user of the authentication and connection status.
