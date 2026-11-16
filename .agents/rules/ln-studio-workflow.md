---
trigger: model_decision
description: Infor LN Studio CLI/MCP automation workflows, component XML generation, Eclipse SCM sync/build, and Pre-Fetch-Auth-Gate OAuth2 guardrails. Load when managing LN Studio workspaces, generating components, interacting with Infor LN servers, or running skill-ln / ln_component_builder commands.
---

# Infor LN Studio Automation & Server Auth Guardrails

Workflows and mandatory authentication guardrails for Infor LN Studio 10.8 build 0640 automation (`skill-ln` CLI / MCP server and `.agents/skills/ln_studio_skill/tools/`).

---

## 1. Automation Toolchain Workflows for AI Agents

When implementing features, creating tables, or debugging compilation errors, agents MUST use the unified CLI tools (`skill-ln` or `.agents/skills/ln_studio_skill/tools/ln_component_builder.py`):

### 1.1 Step 1: Component Definition & Generation
Define the table, fields, indices, and session in a YAML schema file (see `.agents/skills/ln_studio_skill/templates/table_schema_sample.yaml`). Generate metadata directly into the target activity:

```bash
python .agents/skills/ln_studio_skill/tools/ln_component_builder.py component --spec schema.yaml --activity "<activity_name>"
```

### 1.2 Step 2: 4GL Code Development & Synchronization
Develop Baan 4GL source in standalone `.dal` or `.cln` files in `scripts/`:
- DAL: `scripts/dal/<table_code>.dal`
- UI: `scripts/ui/<session_code>.cln`

Inject the code into workspace metadata XML:
```bash
python .agents/skills/ln_studio_skill/tools/ln_component_builder.py inject --source scripts/dal/txptc100.dal --target "<activity_path>/tx/table/ptc/txptc100.tbl"
```

### 1.3 Step 3: Eclipse SCM Synchronization
Register new components in the activity `.admin` file:
```bash
python .agents/skills/ln_studio_skill/tools/ln_component_builder.py sync-admin --activity "<activity_name>"
```

### 1.4 Step 4: Closed-Loop Compilation & Diagnostic Fixing
Trigger Eclipse build and inspect line-accurate compiler error markers:
```bash
python .agents/skills/ln_studio_skill/tools/ln_component_builder.py build --activity "<activity_name>"
```

If compilation errors exist, the tool prints exact files, line numbers, and error descriptions. Fix the code in `scripts/`, re-inject, and rebuild until 0 errors are reported.

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
