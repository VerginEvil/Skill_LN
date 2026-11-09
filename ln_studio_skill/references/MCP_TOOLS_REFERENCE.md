# Infor LN Studio MCP Tools Reference (`ln_studio_mcp.py`)

Reference catalog for the zero-dependency Stdio Model Context Protocol (MCP) server bundled with `ln_studio_skill` (25 total tools: 4 consolidated high-efficiency + 21 detailed backward-compatible).

---

## 1. Consolidated High-Efficiency Suite (4 Tools)

Designed for low-context token consumption while providing full project, code intelligence, diff, and compile capabilities:

| Tool Name | Supported Actions / Parameters | Guardrail & Description |
|---|---|---|
| `ln_project_activity` | `action`: `project_info`, `list_activities`, `new_activity`, `open_activity`, `clean_activity`, `move_components`, `clean_components`<br>Parameters: `project`, `activity_name`, `task_desc`, `components` | Remote project and activity lifecycle management with Single-XML TDE Layout bootstrapping. |
| `ln_code_intelligence`| `action`: `search_server`, `call_hierarchy`, `open_declaration`, `generate_report_server`<br>Parameters: `pattern`, `package`, `source_file`, `function_name`, `table_name`, `report_code` | Remote code intelligence via `FglStudio` (search, callers/callees, jump to definition, report generation wizard). |
| `ln_version_diff` | `action`: `list_revisions`, `get_revision`, `diff_component`<br>Parameters: `comp_type`, `comp_name`, `revision`, `activity_name` | Server revision history and structural XML + 4GL script diff against committed server versions. |
| `ln_adhoc_compile` | Parameters: `package_code`, `source_code`, `flags`, `activity_name` | Ad-hoc server compilation via `FglStudio.compileSource` without requiring check-out or commit. |

---

## 2. Detailed Backward-Compatible Suite (21 Tools)

Legacy granular tools supported across all MCP clients:

| Tool Name | Parameters | Safety Guardrail & Purpose |
|---|---|---|
| `ln_list_environments` | `workspace_root` (optional) | **Read-only**: Lists workspaces, cloud configurations, active dev/runtime endpoints. |
| `ln_login` | `workspace`, `ionapi_file`, `status_only`, `register_protocol_only` | **Production**: Multi-channel SSO login, `oob://` protocol capture, and token refresh. |
| `ln_connect` | `ionapi_file`, `workspace`, `manual_auth` | **Idempotent**: Imports `.ionapi` credentials, sets up `cloudenv.prefs` & `connectivity.prefs`. |
| `ln_explore_projects` | `app_code`, `project_name` | **Read-only**: Browses remote Applications and Software Projects via JCA. |
| `ln_explore_activities`| `project_name` | **Read-only**: Lists remote Activities under a Software Project. |
| `ln_explore_components`| `comp_type`, `filter_pattern` | **Read-only**: Browses server components across all 12 types with wildcard filters. |
| `ln_create_activity` | `project_name`, `task_id`, `description`, `user_id` | **Production**: Creates remote Activity and bootstraps local `.project`, `.admin`, `.settings`. |
| `ln_clean_activity` | `project_name`, `task_id` | **Recovery**: Recovers stuck workarea lock on LN Server. |
| `ln_get_component` | `comp_type`, `comp_name`, `activity_name`, `inspect_only`, `export_script` | **Read-only**: Fetches component from server (in-memory or read-only download). |
| `ln_sync_reference` | `comp_type`, `filter_pattern`, `workspace` | **Read-only**: Syncs read-only reference components into `.reference/` and indexes DD cache. |
| `ln_checkout_component`| `comp_type`, `comp_name`, `activity_name` | **ADR 0006 Guardrail**: Checks out component on server. Strictly rejects `tx*` extensions. |
| `ln_uncheckout_component`| `comp_type`, `comp_name`, `activity_name` | **Safe Revert**: Reverts component check-out on server and restores read-only copy. |
| `ln_checkin_component` | `comp_type`, `comp_name`, `activity_name`, `comment` | **Safe Check-In**: Puts component to server and checks in for LN UI Cloud testing. |
| `ln_checkout_activity` | `activity_name`, `project_name` | **Bulk SCM**: Checks out all components within an activity. |
| `ln_checkin_activity` | `activity_name`, `project_name`, `comment` | **Bulk SCM**: Checks in all components within an activity. |
| `ln_create_component` | `comp_type`, `spec_yaml`, `activity_name`, `output_dir` | **Generation**: Generates any of the 12 LN Studio components and registers in `.admin`. |
| `ln_clone_component` | `source_type`, `source_name`, `target_name`, `activity_name` | **Renaming**: Clones standard/custom component into renamed custom activity component. |
| `ln_validate_activity` | `activity_path`, `strict_mode`, `auto_fix` | **Read-only / Safe Fix**: 4-layer activity validation (`.admin`, XML schema, cross-refs, 4GL). |
| `ln_deploy_test` | `comp_type`, `comp_name`, `activity_name`, `mode` | **Cloud Testing**: Composite pipeline: Put -> Compile -> CRDD -> CreateTables -> VSC -> CheckIn. |
| `ln_prepare_end_activity`| `activity_name`, `project_name` | **ADR 0007 Human Gate**: Pre-commit verification gate before handing delivery off to engineer. |
| `ln_end_activity` | `task_id`, `project_name` | **Hard-blocked Pre-Commit Gate**: Raises `PreCommitBoundaryError` (human final delivery only). |

---

## 3. Client Registration Guide (`mcp-setup`)

```bash
# Register in Claude Desktop configuration (~/AppData/Roaming/Claude/claude_desktop_config.json)
python tools/ln_component_builder.py mcp-setup --client claude --apply

# Register in Cursor configuration (.cursor/mcp.json)
python tools/ln_component_builder.py mcp-setup --client cursor --apply

# Register in Antigravity configuration
python tools/ln_component_builder.py mcp-setup --client antigravity --apply

# Output generic JSON configuration to stdout
python tools/ln_component_builder.py mcp-setup --client generic --dry-run
```

---

## 4. MCP Standard Envelope Contract

All MCP tool responses return a uniform dictionary structure:
```json
{
  "status": "success",
  "action": "checkout_component",
  "result": {
    "component": "whwmd4100m000",
    "type": "session",
    "activity": "dev_natt_1107-1 [EXTce01107]"
  },
  "message": "Component checked out successfully."
}
```
In case of error, `status` is `"error"` and `message` contains the human-readable diagnostic.
