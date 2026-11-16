use std::path::{Path, PathBuf};
use serde_json::{json, Value};

use ln_jca::client::{ConnectOptions, HttpClient};
use ln_model::path_resolver::split_component_name;
use ln_scm::activity::{
    bootstrap_local_activity, clean_activity_components, clean_remote_activity,
    create_remote_activity, find_component_file, list_remote_activities,
    move_activity_components, open_remote_activity, ComponentRef, CreateActivityOptions,
};
use ln_scm::build::{deploy_test, prepare_end_activity};
use ln_scm::code_intel::{
    compile_source_adhoc, get_call_hierarchy, get_related_script_components, open_declaration,
    search_server_pattern,
};
use ln_scm::context::{ActivityDotProject, WorkspaceContext};
use ln_scm::explorer::{browse_components, clone_component, get_component, inspect_component, sync_reference};
use ln_scm::project::{get_software_project_details, list_software_projects};
use ln_scm::revision_diff::{
    diff_component, generate_report_on_server, get_component_revision, list_component_revisions,
};
use ln_scm::scm_engine::{
    checkin_activity, checkin_component, checkout_activity, checkout_component,
    is_extension_component, uncheckout_component,
};

use crate::commands::{
    create_single_xml_component, resolve_activity_path, write_generated_tde_file,
};
use crate::mcp::envelope::{format_mcp_response, make_envelope};

pub fn list_registered_tools() -> Vec<Value> {
    vec![
        json!({
            "name": "ln_list_environments",
            "description": "Lists configured Infor LN customer workspaces, cloud environments, and connection status.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "workspace_root": {"type": "string", "description": "Optional custom workspace root directory"}
                }
            }
        }),
        json!({
            "name": "ln_login",
            "description": "Authenticates with Infor CloudSuite SSO, registers Windows oob protocol, captures authorization code via multi-channel auto-detect, and saves active tokens.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "workspace": {"type": "string", "description": "Target customer workspace or CloudEnvironment name (e.g. SCS_TST)"},
                    "ionapi_file": {"type": "string", "description": "Optional path to .ionapi credential file"},
                    "register_protocol_only": {"type": "boolean", "description": "Only register Windows oob:// protocol handler without logging in"},
                    "check_only": {"type": "boolean", "description": "Check current token validity and status without initiating browser login"}
                }
            }
        }),
        json!({
            "name": "ln_connect",
            "description": "Imports .ionapi credentials and synchronizes Eclipse global and workspace connectivity preferences.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "ionapi_file": {"type": "string", "description": "Path to .ionapi credential file"},
                    "workspace": {"type": "string", "description": "Optional workspace name to sync"}
                },
                "required": ["ionapi_file"]
            }
        }),
        json!({
            "name": "ln_explore_projects",
            "description": "Explores remote Infor LN Applications and Software Projects via Headless JCA.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "application": {"type": "string", "description": "Optional application code (e.g. tc)"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                }
            }
        }),
        json!({
            "name": "ln_explore_activities",
            "description": "Explores remote Activities under a specific Infor LN Software Project.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "project": {"type": "string", "description": "Software Project name (e.g. EXTce01107)"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["project"]
            }
        }),
        json!({
            "name": "ln_explore_components",
            "description": "Browses components on server across all 12 types (table, session, domain, library, etc.).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "description": "Component type (table, session, domain, library, menu, etc.)"},
                    "filter": {"type": "string", "description": "Optional component name filter wildcard (e.g. tx*)"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["type"]
            }
        }),
        json!({
            "name": "ln_create_activity",
            "description": "Creates a remote Activity under a Software Project and bootstraps local activity folder structure.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "project": {"type": "string", "description": "Software Project name (e.g. EXTce01107)"},
                    "activity_id": {"type": "string", "description": "Activity task identifier (e.g. task_001)"},
                    "description": {"type": "string", "description": "Activity description"},
                    "workspace": {"type": "string", "description": "Target workspace folder"},
                    "bootstrap_local": {"type": "boolean", "description": "Whether to scaffold local .project, .admin, etc."},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["project", "activity_id"]
            }
        }),
        json!({
            "name": "ln_clean_activity",
            "description": "Recovers stuck locks or workareas on LN server for a specific Activity.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "project": {"type": "string", "description": "Software Project name"},
                    "activity_id": {"type": "string", "description": "Activity task identifier"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["project", "activity_id"]
            }
        }),
        json!({
            "name": "ln_get_component",
            "description": "Fetches a component from server (inspects in-memory, downloads Read-Only into local activity, or syncs to .reference/<type>/ and updates .ln_dd_cache.json).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "description": "Component type (table, session, domain, extension, etc.)"},
                    "name": {"type": "string", "description": "Component name or pattern (e.g. tcibd001, txsli001)"},
                    "activity": {"type": "string", "description": "Target local activity folder or path"},
                    "inspect_only": {"type": "boolean", "description": "If true, inspect in memory without writing"},
                    "reference_only": {"type": "boolean", "description": "If true, save Read-Only into .reference/<type>/ and update .ln_dd_cache.json"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["type", "name"]
            }
        }),
        json!({
            "name": "ln_sync_reference",
            "description": "Downloads standard/custom tables, domains, sessions, or read-only extensions into .reference/<type>/ and indexes .tbl/.dmn schemas into .ln_dd_cache.json.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": ["table", "domain", "session", "extension", "library", "report", "menu"],
                        "description": "Reference component type (extensions are strictly Read-Only Get per ADR 0006)"
                    },
                    "name": {"type": "string", "description": "Component name or wildcard pattern (e.g. tcibd001, tcibd*, txsli001)"},
                    "workspace_dir": {"type": "string", "description": "Local workspace/project root directory"},
                    "dd_cache_path": {"type": "string", "description": "Optional path to .ln_dd_cache.json"},
                    "workspace": {"type": "string", "description": "LN Studio workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["type", "name"]
            }
        }),
        json!({
            "name": "ln_checkout_component",
            "description": "Locks component on server into activity and downloads editable XML. Hard-blocks Extension Modeler tx* objects.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "description": "Component type"},
                    "name": {"type": "string", "description": "Component name"},
                    "activity": {"type": "string", "description": "Target activity directory"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "comment": {"type": "string", "description": "Check-out comment"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["type", "name", "activity"]
            }
        }),
        json!({
            "name": "ln_uncheckout_component",
            "description": "Reverts component lock on server and restores local read-only copy.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "description": "Component type"},
                    "name": {"type": "string", "description": "Component name"},
                    "activity": {"type": "string", "description": "Target activity directory"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["type", "name", "activity"]
            }
        }),
        json!({
            "name": "ln_checkin_component",
            "description": "Puts component and checks in with comment to update server and enable LN UI Cloud testing.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "description": "Component type"},
                    "name": {"type": "string", "description": "Component name"},
                    "activity": {"type": "string", "description": "Target activity directory"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "comment": {"type": "string", "description": "Check-in comment"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["type", "name", "activity"]
            }
        }),
        json!({
            "name": "ln_checkout_activity",
            "description": "Batch Check-Out for all components in an activity ordered by architectural dependency. Halts immediately on first failure without blind rollback.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "activity": {"type": "string", "description": "Target activity directory or name"},
                    "project": {"type": "string", "description": "Software Project name (e.g. EXTce01107)"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["activity"]
            }
        }),
        json!({
            "name": "ln_checkin_activity",
            "description": "Batch Check-In for all modified components in an activity with a single comment. Automatically segregates Extension Modeler components (ADR 0006). Halts immediately on first failure without blind rollback.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "activity": {"type": "string", "description": "Target activity directory or name"},
                    "project": {"type": "string", "description": "Software Project name (e.g. EXTce01107)"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "comment": {"type": "string", "description": "Check-in comment"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["activity", "comment"]
            }
        }),
        json!({
            "name": "ln_create_component",
            "description": "Creates one of the 12 Infor LN Studio components and registers it in .admin SCM.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "Component type (table, session, domain, library, menu, message, question, function, additional, report)"
                    },
                    "code": {"type": "string", "description": "Component code (e.g. txcmg0001)"},
                    "description": {"type": "string", "description": "Component description"},
                    "activity": {"type": "string", "description": "Target activity folder or path"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "spec": {"type": "object", "description": "Optional type-specific schema attributes"},
                    "dry_run": {"type": "boolean", "description": "Preview without writing to disk"}
                },
                "required": ["type", "code", "activity"]
            }
        }),
        json!({
            "name": "ln_clone_component",
            "description": "Clones a standard or custom component into a renamed custom component in target activity.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "source_type": {"type": "string", "description": "Source component type"},
                    "source_name": {"type": "string", "description": "Source component name"},
                    "target_name": {"type": "string", "description": "Target cloned component name (must start with custom package)"},
                    "activity": {"type": "string", "description": "Target activity directory"},
                    "target_desc": {"type": "string", "description": "Target description"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["source_type", "source_name", "target_name", "activity"]
            }
        }),
        json!({
            "name": "ln_validate_activity",
            "description": "Performs 4-layer validation across activity components (.admin, XML structure, cross-references, 4GL scripts).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "activity": {"type": "string", "description": "Activity directory or name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "strict": {"type": "boolean", "description": "Treat warnings as errors"}
                },
                "required": ["activity"]
            }
        }),
        json!({
            "name": "ln_deploy_test",
            "description": "Runs split test deployment pipeline on server: compile-only (default safe mode: Put -> Compile -> VSC -> CheckIn) or schema-crdd (adds CRDD & CreateTables with lock warning).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "description": "Component type"},
                    "name": {"type": "string", "description": "Component name"},
                    "activity": {"type": "string", "description": "Target activity directory"},
                    "mode": {
                        "type": "string",
                        "enum": ["compile-only", "schema-crdd"],
                        "description": "Deployment mode: compile-only (default safe mode) or schema-crdd"
                    },
                    "dry_run": {"type": "boolean", "description": "Pre-check planned steps and table lock risks without executing"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "comment": {"type": "string", "description": "Check-in comment"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["type", "name", "activity"]
            }
        }),
        json!({
            "name": "ln_prepare_end_activity",
            "description": "Pre-commit readiness verifier. Validates all activity components, clean working tree, and generates handoff report.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "activity": {"type": "string", "description": "Target activity directory"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["activity"]
            }
        }),
        json!({
            "name": "ln_end_activity",
            "description": "Hard-blocked pre-commit boundary gate. Infor LN Studio human review is required before activity finalization.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "activity": {"type": "string", "description": "Activity directory"},
                    "project": {"type": "string", "description": "Software Project name"}
                }
            }
        }),
        json!({
            "name": "ln_project_activity",
            "description": "Consolidated tool for Software Projects and Activities (project_info, list_activities, new_activity, open_activity, clean_activity, move_components, clean_components).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["project_info", "list_activities", "new_activity", "open_activity", "clean_activity", "move_components", "clean_components"],
                        "description": "Sub-action to perform"
                    },
                    "project": {"type": "string", "description": "Software Project name (e.g. EXTce01107)"},
                    "task": {"type": "string", "description": "Activity task ID (e.g. task_01)"},
                    "description": {"type": "string", "description": "Activity description"},
                    "assigned_to": {"type": "string", "description": "Assignee username"},
                    "no_open": {"type": "boolean", "description": "Skip local bootstrap after creating activity"},
                    "sync_modified": {"type": "boolean", "description": "Query and download modified components when opening activity (default true)"},
                    "components": {"type": "array", "items": {"type": "object"}, "description": "Component list for move/clean: [{'type':'table','name':'txibd001'}]"},
                    "source_activity": {"type": "string", "description": "Source activity directory for move_components"},
                    "target_activity": {"type": "string", "description": "Target activity directory for move_components"},
                    "activity": {"type": "string", "description": "Target activity folder or name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["action"]
            }
        }),
        json!({
            "name": "ln_code_intelligence",
            "description": "Consolidated tool for FglStudio code intelligence, remote compilation, related-component discovery, and server report generation (search_server, call_hierarchy, open_declaration, compile_source, related_components, generate_report_server).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["search_server", "call_hierarchy", "open_declaration", "compile_source", "related_components", "generate_report_server"],
                        "description": "Sub-action to perform"
                    },
                    "pattern": {"type": "string", "description": "Search pattern or regex"},
                    "package_code": {"type": "string", "description": "Package code (e.g. tx, td)"},
                    "source_code": {"type": "string", "description": "Optional 4GL script source code for compile_source"},
                    "flags": {"type": "string", "description": "Optional compiler flags for compile_source"},
                    "source_file": {"type": "string", "description": "Source file name"},
                    "function_name": {"type": "string", "description": "Function name"},
                    "call_mode": {"type": "string", "enum": ["callers", "callees"], "description": "Call hierarchy mode: callers (where-used) or callees"},
                    "comp_code": {"type": "string", "description": "Component code"},
                    "comp_type": {"type": "string", "description": "Component type"},
                    "context": {"type": "string", "description": "Optional context for declaration lookup"},
                    "report_name": {"type": "string", "description": "Report component code"},
                    "table_name": {"type": "string", "description": "Primary table code for report"},
                    "version_id": {"type": "string", "description": "Version ID (default 1)"},
                    "report_size": {"type": "string", "enum": ["80", "132"], "description": "Paper width (80 or 132)"},
                    "report_type": {"type": "string", "enum": ["1", "2", "3"], "description": "Report type (1, 2, or 3)"},
                    "used_index": {"type": "string", "description": "Used table index"},
                    "input_fields": {"type": "array", "items": {"type": "string"}, "description": "List of report input field names"},
                    "activity": {"type": "string", "description": "Target activity folder"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["action"]
            }
        }),
        json!({
            "name": "ln_version_diff",
            "description": "Consolidated tool for server revision history and structural diff (list_revisions, get_revision, diff_component).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["list_revisions", "get_revision", "diff_component"],
                        "description": "Sub-action to perform"
                    },
                    "comp_type": {"type": "string", "description": "Component type (table, session, library, report, etc.)"},
                    "comp_name": {"type": "string", "description": "Component name (e.g. txibd001)"},
                    "version_id": {"type": "string", "description": "Version ID (default 1)"},
                    "rev_number": {"type": "integer", "description": "Revision number for get_revision or diff_component"},
                    "activity": {"type": "string", "description": "Activity directory for diff_component"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["action", "comp_type", "comp_name"]
            }
        }),
        json!({
            "name": "ln_adhoc_compile",
            "description": "Ad-Hoc Server Compile via FglStudio.compileSource in SHOW mode (compiles 4GL code snippet directly on server bic6.2 without modifying workspace files or SCM state).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "package_code": {"type": "string", "description": "Package code (e.g. tx, tc, td)"},
                    "source_code": {"type": "string", "description": "4GL source code snippet to compile"},
                    "flags": {"type": "string", "description": "Optional bic6.2 compiler flags"},
                    "activity": {"type": "string", "description": "Target activity folder"},
                    "project": {"type": "string", "description": "Software Project name"},
                    "workspace": {"type": "string", "description": "Workspace name"},
                    "mock": {"type": "boolean", "description": "Use mock transport for testing"}
                },
                "required": ["package_code", "source_code"]
            }
        })
    ]
}

fn is_mock(arguments: &Value) -> bool {
    arguments.get("mock").and_then(|v| v.as_bool()).unwrap_or(false)
}

fn mcp_ok(name: &str, data: Value, msg: &str) -> Value {
    format_mcp_response(make_envelope(name, data, msg, "success"), false)
}

fn mcp_err(name: &str, msg: &str) -> Value {
    format_mcp_response(make_envelope(name, Value::Null, msg, "error"), true)
}

fn arg_str<'a>(arguments: &'a Value, key: &str) -> Option<&'a str> {
    arguments
        .get(key)
        .and_then(|v| v.as_str())
        .map(str::trim)
        .filter(|s| !s.is_empty())
}

fn parse_mcp_component_refs(val: Option<&Value>) -> Vec<ComponentRef> {
    let Some(v) = val else {
        return Vec::new();
    };
    if let Some(arr) = v.as_array() {
        return arr
            .iter()
            .filter_map(|item| {
                let ctype = item.get("type").and_then(|x| x.as_str())?;
                let cname = item.get("name").and_then(|x| x.as_str())?;
                Some(ComponentRef {
                    comp_type: ctype.trim().to_lowercase(),
                    name: cname.trim().to_string(),
                })
            })
            .collect();
    }
    if let Some(raw) = v.as_str() {
        return raw
            .split(',')
            .map(str::trim)
            .filter(|s| !s.is_empty())
            .map(|item| {
                if let Some((ct, nm)) = item.split_once(':') {
                    ComponentRef {
                        comp_type: ct.trim().to_lowercase(),
                        name: nm.trim().to_string(),
                    }
                } else {
                    ComponentRef {
                        comp_type: "table".to_string(),
                        name: item.to_string(),
                    }
                }
            })
            .collect();
    }
    Vec::new()
}

async fn mcp_resolve_ctx_and_client(
    arguments: &Value,
) -> Result<(WorkspaceContext, HttpClient), String> {
    let ws_str = arg_str(arguments, "workspace").or_else(|| arg_str(arguments, "workspace_dir"));
    let act_str = arg_str(arguments, "activity").or_else(|| arg_str(arguments, "source_activity"));
    let ep_str = arg_str(arguments, "endpoint");
    let tok_str = arg_str(arguments, "access_token");

    let ws_opt = ws_str.map(Path::new);
    let act_opt = act_str.map(Path::new);

    let mut ctx = match WorkspaceContext::discover(ws_opt, act_opt) {
        Ok(c) => c,
        Err(e) => {
            if let Some(ep) = ep_str {
                let ws_dir = ws_opt
                    .map(Path::to_path_buf)
                    .or_else(|| act_opt.and_then(|p| p.parent().map(Path::to_path_buf)))
                    .unwrap_or_else(|| PathBuf::from("."));
                WorkspaceContext {
                    workspace_dir: ws_dir,
                    env_name: ws_str.unwrap_or("MCP").to_string(),
                    endpoint_url: ep.to_string(),
                    company: "0".to_string(),
                    default_activity_dir: act_opt.map(Path::to_path_buf),
                }
            } else {
                return Err(e.to_string());
            }
        }
    };

    if let Some(ep) = ep_str {
        ctx.endpoint_url = ep.to_string();
    }

    let client = if let Some(tok) = tok_str {
        let c = HttpClient::new(&ctx.endpoint_url, tok);
        c.set_default_company(&ctx.company);
        c
    } else {
        ctx.build_authenticated_client()
            .await
            .map_err(|e| e.to_string())?
    };

    Ok((ctx, client))
}

pub async fn execute_tool(name: &str, arguments: &Value) -> Value {
    match name {
        "ln_list_environments" => {
            let mut envs = Vec::new();
            if let Some(docs) = dirs::document_dir() {
                let ws_base = docs.join("workspace_lnstudio");
                if let Ok(entries) = std::fs::read_dir(ws_base) {
                    for e in entries.flatten() {
                        let p = e.path();
                        if p.is_dir() && p.join(".metadata").exists() {
                            if let Some(nm) = p.file_name().and_then(|s| s.to_str()) {
                                if !envs.contains(&nm.to_string()) {
                                    envs.push(nm.to_string());
                                }
                            }
                        }
                    }
                }
            }
            if let Some(home) = dirs::home_dir() {
                let ln_dir = home.join(".ln_studio").join("tokens");
                if let Ok(entries) = std::fs::read_dir(ln_dir) {
                    for e in entries.flatten() {
                        let p = e.path();
                        if p.extension().map_or(false, |ext| ext == "json") {
                            if let Some(stem) = p.file_stem().and_then(|s| s.to_str()) {
                                if !envs.contains(&stem.to_string()) {
                                    envs.push(stem.to_string());
                                }
                            }
                        }
                    }
                }
            }
            if envs.is_empty() {
                envs.push("SCS_TST".to_string());
            }
            mcp_ok(
                name,
                json!({ "workspaces": envs }),
                &format!("Found {} workspaces", envs.len()),
            )
        }

        "ln_login" => {
            if arguments.get("register_protocol_only").and_then(|v| v.as_bool()).unwrap_or(false) {
                #[cfg(target_os = "windows")]
                let ok = std::process::Command::new("reg")
                    .args(["add", r"HKCU\Software\Classes\oob", "/ve", "/d", "URL:oob Protocol", "/f"])
                    .status()
                    .map_or(false, |s| s.success());
                #[cfg(not(target_os = "windows"))]
                let ok = true;

                return if ok {
                    mcp_ok(name, json!({ "protocol_registered": true }), "Protocol registered")
                } else {
                    mcp_err(name, "Registration failed")
                };
            }

            let ws = arg_str(arguments, "workspace").unwrap_or("SCS_TST");
            let home = dirs::home_dir().unwrap_or_else(|| PathBuf::from("."));
            let tok_dir = home.join(".ln_studio").join("tokens");
            let tok_mgr = ln_auth::OAuth2TokenManager::new(Some(tok_dir.clone()));

            if arguments.get("check_only").and_then(|v| v.as_bool()).unwrap_or(false) {
                let st = tok_mgr.check_token_status(ws);
                let is_valid = matches!(st, ln_auth::TokenStatus::Valid { .. });
                let exp = match st {
                    ln_auth::TokenStatus::Valid { expires_in, .. }
                    | ln_auth::TokenStatus::NeedsRefresh { expires_in, .. }
                    | ln_auth::TokenStatus::Expired { expires_in } => expires_in,
                    ln_auth::TokenStatus::Missing => 0.0,
                };
                let st_name = match st {
                    ln_auth::TokenStatus::Valid { .. } => "valid",
                    ln_auth::TokenStatus::NeedsRefresh { .. } => "needs_refresh",
                    ln_auth::TokenStatus::Expired { .. } => "expired",
                    ln_auth::TokenStatus::Missing => "missing",
                };
                return mcp_ok(
                    name,
                    json!({ "status": st_name, "valid": is_valid, "expires_in": exp }),
                    "Workspace auth status",
                );
            }

            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "workspace": ws, "authenticated": true, "token_type": "Bearer" }),
                    "Authentication complete",
                );
            }

            if let Some(ionapi) = arg_str(arguments, "ionapi_file") {
                let cfg = match ln_auth::IonapiConfig::load_from_path(Path::new(ionapi)) {
                    Ok(c) => c,
                    Err(e) => return mcp_err(name, &format!("Failed to read .ionapi: {e}")),
                };
                if let Some(cached) = tok_mgr.load_token(ws) {
                    if let Some(rt) = cached.refresh_token {
                        if let Ok(new_tok) = tok_mgr.refresh_access_token(&cfg, &rt).await {
                            let _ = tok_mgr.save_token(ws, new_tok);
                            return mcp_ok(
                                name,
                                json!({ "workspace": ws, "authenticated": true, "status": "refreshed" }),
                                "Refreshed OAuth2 token",
                            );
                        }
                    }
                }
                if cfg.saak.is_some() && cfg.sask.is_some() {
                    match tok_mgr.acquire_service_account_token(&cfg).await {
                        Ok(tok) => {
                            let _ = tok_mgr.save_token(ws, tok);
                            return mcp_ok(
                                name,
                                json!({ "workspace": ws, "authenticated": true, "status": "authenticated" }),
                                "Acquired service account OAuth2 token",
                            );
                        }
                        Err(e) => return mcp_err(name, &format!("Service account token error: {e}")),
                    }
                }
                let auth_url = tok_mgr.build_authorization_url(&cfg, None, None);
                return mcp_err(name, &ln_auth::format_auth_alert_banner(ws, Some(&auth_url)));
            }

            let rep = ln_auth::check_auth_status(ws, Some(tok_dir), None);
            if rep.access_token.is_some() {
                mcp_ok(
                    name,
                    json!({ "workspace": ws, "authenticated": true, "status": rep.status, "expires_in": rep.expires_in }),
                    "Authentication valid",
                )
            } else {
                mcp_err(name, &rep.alert_banner.unwrap_or_else(|| format!("Authentication required for '{}'", ws)))
            }
        }

        "ln_connect" => {
            let ws = arg_str(arguments, "workspace").unwrap_or("SCS_TST");
            let ionapi = arg_str(arguments, "ionapi_file").unwrap_or("");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "workspace": ws, "ionapi_file": ionapi, "connected": true }),
                    "Preferences synchronized",
                );
            }

            if !ionapi.is_empty() {
                let path = Path::new(ionapi);
                if !path.exists() {
                    return mcp_err(name, &format!(".ionapi file not found: {ionapi}"));
                }
                let cfg = match ln_auth::IonapiConfig::load_from_path(path) {
                    Ok(c) => c,
                    Err(e) => return mcp_err(name, &format!("Invalid .ionapi: {e}")),
                };
                let home = dirs::home_dir().unwrap_or_else(|| PathBuf::from("."));
                let prefs_path = home.join(".ln_studio").join("com.infor.erpln.jca.connectivity.cloudenv.prefs");
                if let Err(e) = ln_auth::sync_cloudenv_prefs(&prefs_path, ws, &cfg) {
                    return mcp_err(name, &format!("Failed to sync global prefs: {e}"));
                }
                if let Ok(ctx) = WorkspaceContext::discover(Some(Path::new(ws)), None) {
                    let conn_prefs = ctx.workspace_dir.join(".metadata/.plugins/org.eclipse.core.runtime/.settings/com.infor.erpln.jca.connectivity.prefs");
                    if conn_prefs.exists() {
                        let _ = ln_auth::sync_connectivity_prefs(&conn_prefs, ws, &cfg, None);
                    }
                }
            }

            match mcp_resolve_ctx_and_client(arguments).await {
                Ok((ctx, client)) => {
                    let conn_res = client
                        .connect(&ConnectOptions {
                            company: Some(ctx.company.clone()),
                            ..Default::default()
                        })
                        .await;
                    let _ = client.disconnect_all().await;
                    match conn_res {
                        Ok(r) => mcp_ok(
                            name,
                            json!({
                                "workspace": ws,
                                "endpoint": ctx.endpoint_url,
                                "ionapi_file": ionapi,
                                "conid": r.conid,
                                "connected": true
                            }),
                            "Connected to JCA endpoint",
                        ),
                        Err(e) => mcp_err(name, &format!("JCA connect failed: {e}")),
                    }
                }
                Err(e) => {
                    if !ionapi.is_empty() {
                        mcp_ok(
                            name,
                            json!({ "workspace": ws, "ionapi_file": ionapi, "connected": true }),
                            "Preferences synchronized",
                        )
                    } else {
                        mcp_err(name, &format!("Workspace discovery failed: {e}"))
                    }
                }
            }
        }

        "ln_explore_projects" => {
            if is_mock(arguments) {
                let projects = vec![
                    json!({ "name": "EXTce01107", "description": "Custom Extensions Project" }),
                    json!({ "name": "tcibd010", "description": "Standard Components Project" }),
                ];
                return mcp_ok(name, json!({ "projects": projects }), "Found 2 projects");
            }
            let (_ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let res = list_software_projects(&client).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(projs) => {
                    let app_filter = arg_str(arguments, "application");
                    let filtered: Vec<_> = projs
                        .into_iter()
                        .filter(|p| app_filter.map_or(true, |a| p.name.to_lowercase().contains(&a.to_lowercase())))
                        .collect();
                    let count = filtered.len();
                    mcp_ok(
                        name,
                        json!({ "projects": filtered }),
                        &format!("Found {} projects", count),
                    )
                }
                Err(e) => mcp_err(name, &format!("SoftwareProject.List failed: {e}")),
            }
        }

        "ln_explore_activities" => {
            let proj = arg_str(arguments, "project").unwrap_or("");
            if is_mock(arguments) {
                let acts = vec![json!({ "activity_id": "task_mcp_01", "project": proj, "status": "open" })];
                return mcp_ok(name, json!({ "activities": acts }), "Found 1 activity");
            }
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (_, proj_name, _) = resolve_activity_path(&ctx, None, Some(proj).filter(|s| !s.is_empty()));
            let res = list_remote_activities(&client, &proj_name).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(acts) => {
                    let count = acts.len();
                    mcp_ok(
                        name,
                        json!({ "project": proj_name, "activities": acts }),
                        &format!("Found {} activities", count),
                    )
                }
                Err(e) => mcp_err(name, &format!("Activity.List failed: {e}")),
            }
        }

        "ln_explore_components" => {
            let ctype = arg_str(arguments, "type").unwrap_or("table");
            if is_mock(arguments) {
                let comps = vec![json!({ "name": "txcmg010", "type": ctype, "package": "tx" })];
                return mcp_ok(name, json!({ "components": comps }), "Found 1 component");
            }
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (_, proj_name, dev_cp) = resolve_activity_path(&ctx, arg_str(arguments, "activity"), arg_str(arguments, "project"));
            let filt = arg_str(arguments, "filter").unwrap_or("");
            let pkg: String = filt.chars().take(2).take_while(|c| c.is_ascii_alphabetic()).collect();
            let res = browse_components(&client, &pkg, ctype, filt, &dev_cp).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(comps) => {
                    let count = comps.len();
                    mcp_ok(
                        name,
                        json!({ "project": proj_name, "components": comps }),
                        &format!("Found {} components", count),
                    )
                }
                Err(e) => mcp_err(name, &format!("Component browse failed: {e}")),
            }
        }

        "ln_create_activity" => {
            let proj = arg_str(arguments, "project").unwrap_or("");
            let act_id = arg_str(arguments, "activity_id").unwrap_or("");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "project": proj, "activity_id": act_id, "created": true }),
                    "Activity created",
                );
            }
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let bootstrap = arguments.get("bootstrap_local").and_then(|v| v.as_bool()).unwrap_or(true);
            let opts = CreateActivityOptions {
                description: arg_str(arguments, "description").unwrap_or(act_id),
                assigned_to: arg_str(arguments, "assigned_to").unwrap_or(""),
                auto_open: bootstrap,
                workspace_path: if bootstrap { Some(&ctx.workspace_dir) } else { None },
                ..Default::default()
            };
            let res = create_remote_activity(&client, proj, act_id, opts).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(created) => mcp_ok(name, json!(created), "Activity created"),
                Err(e) => mcp_err(name, &format!("Activity.Create failed: {e}")),
            }
        }

        "ln_clean_activity" => {
            let proj = arg_str(arguments, "project").unwrap_or("");
            let act_id = arg_str(arguments, "activity_id").unwrap_or("");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "project": proj, "activity_id": act_id, "cleaned": true }),
                    "Activity cleaned",
                );
            }
            let (_ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let res = clean_remote_activity(&client, proj, act_id, None, false).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(ok) => mcp_ok(
                    name,
                    json!({ "project": proj, "activity_id": act_id, "cleaned": ok }),
                    "Activity cleaned",
                ),
                Err(e) => mcp_err(name, &format!("clean_remote_activity failed: {e}")),
            }
        }

        "ln_get_component" => {
            let ctype = arg_str(arguments, "type").unwrap_or("");
            let cname = arg_str(arguments, "name").unwrap_or("");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "type": ctype, "name": cname, "fetched": true }),
                    "Component fetched",
                );
            }
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, arg_str(arguments, "activity"), arg_str(arguments, "project"));
            let dd_cache = ctx.workspace_dir.join(".ln_dd_cache.json");
            let inspect_only = arguments.get("inspect_only").and_then(|v| v.as_bool()).unwrap_or(false);
            let reference_only = arguments.get("reference_only").and_then(|v| v.as_bool()).unwrap_or(false);

            let res = if inspect_only {
                inspect_component(&client, ctype, cname, &dev_cp, Some(&dd_cache), None, None)
                    .await
                    .map(|info| json!({ "mode": "inspect", "project": proj_name, "component": info }))
            } else if reference_only {
                sync_reference(&client, ctype, cname, &ctx.workspace_dir, Some(&dd_cache), &dev_cp)
                    .await
                    .map(|sr| json!({ "mode": "reference", "sync": sr }))
            } else {
                let dir = act_opt.unwrap_or_else(|| ctx.workspace_dir.clone());
                let meta = ActivityDotProject::from_activity_dir(&dir).ok();
                let label_uuid = meta.as_ref().map(|m| m.label.as_str()).filter(|s| !s.is_empty());
                let base_vrc = meta.as_ref().map(|m| m.application_release.as_str()).filter(|s| !s.is_empty());
                get_component(&client, ctype, cname, &dir, true, &dev_cp, Some(&dd_cache), label_uuid, base_vrc, None)
                    .await
                    .map(|saved| json!({ "mode": "get", "type": ctype, "name": cname, "saved_path": saved }))
            };
            let _ = client.disconnect_all().await;
            match res {
                Ok(data) => mcp_ok(name, data, "Component fetched"),
                Err(e) => mcp_err(name, &format!("ln_get_component failed: {e}")),
            }
        }

        "ln_sync_reference" => {
            let ctype = arg_str(arguments, "type").unwrap_or("");
            let cname = arg_str(arguments, "name").unwrap_or("");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "type": ctype, "name": cname, "synced": true }),
                    "Reference component synchronized",
                );
            }
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (_, _, dev_cp) = resolve_activity_path(&ctx, None, arg_str(arguments, "project"));
            let ws_root = arg_str(arguments, "workspace_dir")
                .map(PathBuf::from)
                .unwrap_or_else(|| ctx.workspace_dir.clone());
            let dd_cache = arg_str(arguments, "dd_cache_path").map(PathBuf::from);
            let res = sync_reference(&client, ctype, cname, &ws_root, dd_cache.as_deref(), &dev_cp).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(sr) => mcp_ok(name, json!(sr), "Reference component synchronized"),
                Err(e) => mcp_err(name, &format!("ln_sync_reference failed: {e}")),
            }
        }

        "ln_checkout_component" => {
            let ctype = arg_str(arguments, "type").unwrap_or("");
            let cname = arg_str(arguments, "name").unwrap_or("");
            if ctype.eq_ignore_ascii_case("extension") || is_extension_component(cname) {
                return mcp_err(
                    name,
                    "ReadOnlyComponentError: Extension Modeler component is Read-Only Get per ADR 0006. SCM Check-Out is blocked.",
                );
            }
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({
                        "checked_out": true,
                        "receipt": format!("CheckOut receipt for {}:{}", ctype, cname)
                    }),
                    "Component checked out successfully",
                );
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
            let dir = act_opt.unwrap_or_else(|| PathBuf::from(act_str));
            let res = checkout_component(&client, ctype, cname, &dir, &proj_name, None, Some(&dev_cp)).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(co) => mcp_ok(
                    name,
                    json!({ "checked_out": true, "path": co.path, "receipt": co.receipt }),
                    "Component checked out successfully",
                ),
                Err(e) => mcp_err(name, &format!("checkout_component failed: {e}")),
            }
        }

        "ln_uncheckout_component" => {
            let ctype = arg_str(arguments, "type").unwrap_or("");
            let cname = arg_str(arguments, "name").unwrap_or("");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "uncheckout": true, "type": ctype, "name": cname }),
                    "Component check-out reverted",
                );
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
            let dir = act_opt.unwrap_or_else(|| PathBuf::from(act_str));
            let res = uncheckout_component(&client, ctype, cname, &dir, &proj_name, None, Some(&dev_cp)).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(receipt) => mcp_ok(name, json!({ "uncheckout": true, "receipt": receipt }), "Component check-out reverted"),
                Err(e) => mcp_err(name, &format!("uncheckout_component failed: {e}")),
            }
        }

        "ln_checkin_component" => {
            let ctype = arg_str(arguments, "type").unwrap_or("");
            let cname = arg_str(arguments, "name").unwrap_or("");
            let comment = arg_str(arguments, "comment").unwrap_or("Checked in by skill-ln");
            if ctype.eq_ignore_ascii_case("extension") || is_extension_component(cname) {
                return mcp_err(
                    name,
                    "ReadOnlyComponentError: Extension Modeler component is Read-Only Get per ADR 0006. SCM Check-In is blocked.",
                );
            }
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({
                        "checkin": true,
                        "receipt": format!("CheckIn receipt for {}:{} comment: {}", ctype, cname, comment)
                    }),
                    "Component checked in successfully",
                );
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
            let dir = act_opt.unwrap_or_else(|| PathBuf::from(act_str));
            let res = checkin_component(&client, ctype, cname, &dir, &proj_name, comment, None, Some(&dev_cp)).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(receipt) => mcp_ok(name, json!({ "checkin": true, "receipt": receipt }), "Component checked in successfully"),
                Err(e) => mcp_err(name, &format!("checkin_component failed: {e}")),
            }
        }

        "ln_checkout_activity" => {
            if is_mock(arguments) {
                return mcp_ok(name, json!({ "checked_out_count": 1 }), "Activity components checked out");
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
            let dir = act_opt.unwrap_or_else(|| PathBuf::from(act_str));
            let res = checkout_activity(&client, &dir, &proj_name, None, Some(&dev_cp), None).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(batch) => mcp_ok(name, json!(batch), "Activity components checked out"),
                Err(e) => mcp_err(name, &format!("checkout_activity failed: {e}")),
            }
        }

        "ln_checkin_activity" => {
            if is_mock(arguments) {
                return mcp_ok(name, json!({ "checkin_count": 1 }), "Activity components checked in");
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let comment = arg_str(arguments, "comment").unwrap_or("Batch check-in via skill-ln");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
            let dir = act_opt.unwrap_or_else(|| PathBuf::from(act_str));
            let res = checkin_activity(&client, &dir, &proj_name, comment, None, Some(&dev_cp), None).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(batch) => mcp_ok(name, json!(batch), "Activity components checked in"),
                Err(e) => mcp_err(name, &format!("checkin_activity failed: {e}")),
            }
        }

        "ln_create_component" => {
            let ctype = arg_str(arguments, "type").unwrap_or("");
            let code = arg_str(arguments, "code").unwrap_or("");
            let desc = arg_str(arguments, "description").unwrap_or(code);
            let act = arg_str(arguments, "activity").unwrap_or(".");
            let dry_run = arguments.get("dry_run").and_then(|v| v.as_bool()).unwrap_or(false);
            let act_path = PathBuf::from(act);

            match create_single_xml_component(&act_path, ctype, code, desc, arguments.get("spec"), dry_run) {
                Ok((full, rel, xml)) => mcp_ok(
                    name,
                    json!({
                        "type": ctype,
                        "code": code,
                        "relative_path": rel,
                        "file": full.to_string_lossy(),
                        "dry_run": dry_run,
                        "bytes": xml.len()
                    }),
                    &format!("Component {}:{} created ({})", ctype, code, rel),
                ),
                Err(e) => mcp_err(name, &format!("ln_create_component failed: {e}")),
            }
        }

        "ln_clone_component" => {
            let st = arg_str(arguments, "source_type").unwrap_or("");
            let sn = arg_str(arguments, "source_name").unwrap_or("");
            let tn = arg_str(arguments, "target_name").unwrap_or("");
            if st.eq_ignore_ascii_case("extension") || is_extension_component(sn) {
                return mcp_err(name, "Extension Modeler components cannot be cloned (ADR 0006).");
            }
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "source_type": st, "source_name": sn, "target_name": tn, "cloned": true }),
                    "Component cloned successfully",
                );
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let act_path = PathBuf::from(act_str);
            if let Ok((ctx, client)) = mcp_resolve_ctx_and_client(arguments).await {
                let (act_opt, _, dev_cp) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
                let dir = act_opt.unwrap_or(act_path);
                let label_uuid = ActivityDotProject::from_activity_dir(&dir)
                    .ok()
                    .map(|m| m.label)
                    .filter(|s| !s.is_empty());
                let res = clone_component(&client, st, sn, tn, &dir, true, &dev_cp, label_uuid.as_deref()).await;
                let _ = client.disconnect_all().await;
                match res {
                    Ok(saved) => mcp_ok(
                        name,
                        json!({ "source_type": st, "source_name": sn, "target_name": tn, "saved_path": saved, "cloned": true }),
                        "Component cloned successfully",
                    ),
                    Err(e) => mcp_err(name, &format!("clone_component failed: {e}")),
                }
            } else {
                let Some(src_file) = find_component_file(&act_path, sn, st) else {
                    return mcp_err(name, &format!("Local source component {}:{} not found and no JCA endpoint available", st, sn));
                };
                let raw_xml = match std::fs::read_to_string(&src_file) {
                    Ok(s) => s,
                    Err(e) => return mcp_err(name, &format!("Failed reading source: {e}")),
                };
                let (src_pkg, src_mod, _) = split_component_name(sn);
                let (dst_pkg, dst_mod, _) = split_component_name(tn);
                let cloned = ln_model::clone_component_xml(
                    &raw_xml,
                    sn,
                    tn,
                    &src_pkg,
                    &dst_pkg,
                    if src_mod.is_empty() { None } else { Some(src_mod.as_str()) },
                    if dst_mod.is_empty() { None } else { Some(dst_mod.as_str()) },
                );
                let ext = src_file.extension().and_then(|s| s.to_str()).map(|s| format!(".{s}")).unwrap_or_else(|| ".tbl".into());
                match write_generated_tde_file(&act_path, st, tn, &ext, &cloned) {
                    Ok(saved) => mcp_ok(
                        name,
                        json!({ "source_type": st, "source_name": sn, "target_name": tn, "saved_path": saved, "cloned": true }),
                        "Component cloned locally",
                    ),
                    Err(e) => mcp_err(name, &format!("Failed saving cloned component: {e}")),
                }
            }
        }

        "ln_validate_activity" => {
            let act = arg_str(arguments, "activity").unwrap_or(".");
            let strict = arguments.get("strict").and_then(|v| v.as_bool()).unwrap_or(false);
            let act_path = Path::new(act);
            if !act_path.exists() {
                return mcp_err(name, &format!("Activity path does not exist: {act}"));
            }
            let report = ln_model::validate_activity(act_path, strict, false);
            let err_count = report
                .diagnostics
                .iter()
                .filter(|d| d.severity == ln_model::validator::ValidationSeverity::Error)
                .count();
            let warn_count = report
                .diagnostics
                .iter()
                .filter(|d| d.severity == ln_model::validator::ValidationSeverity::Warning)
                .count();
            mcp_ok(
                name,
                json!({
                    "activity": act,
                    "valid": err_count == 0,
                    "errors": err_count,
                    "warnings": warn_count,
                    "files_scanned": report.files_scanned,
                    "diagnostics": report.diagnostics,
                    "repaired_items": report.repaired_items,
                }),
                if err_count == 0 { "Activity validation passed" } else { "Activity validation failed" },
            )
        }

        "ln_deploy_test" => {
            let ctype = arg_str(arguments, "type").unwrap_or("");
            let cname = arg_str(arguments, "name").unwrap_or("");
            let mode = arg_str(arguments, "mode").unwrap_or("compile-only");
            let dry_run = arguments.get("dry_run").and_then(|v| v.as_bool()).unwrap_or(false);
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "deployed": true, "type": ctype, "name": cname, "mode": mode, "dry_run": dry_run }),
                    "Deployment pipeline completed",
                );
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let comment = arg_str(arguments, "comment").unwrap_or("Deploy test via skill-ln MCP");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
            let dir = act_opt.unwrap_or_else(|| PathBuf::from(act_str));
            let res = deploy_test(&client, ctype, cname, &dir, &proj_name, comment, mode, dry_run).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(dep) => mcp_ok(name, json!(dep), "Deployment pipeline completed"),
                Err(e) => mcp_err(name, &format!("deploy_test failed: {e}")),
            }
        }

        "ln_prepare_end_activity" => {
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "ready": true, "pending_changes": 0 }),
                    "Activity ready for end-activity handoff",
                );
            }
            let act_str = arg_str(arguments, "activity").unwrap_or(".");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, Some(act_str), arg_str(arguments, "project"));
            let dir = act_opt.unwrap_or_else(|| PathBuf::from(act_str));
            let res = prepare_end_activity(&client, &dir, &proj_name).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(prep) => mcp_ok(name, json!(prep), "Activity ready for end-activity handoff"),
                Err(e) => mcp_err(name, &format!("prepare_end_activity failed: {e}")),
            }
        }

        "ln_end_activity" => {
            // ADR 0007 / ADR 0020: Physically hard-blocked pre-commit boundary gate
            mcp_err(
                name,
                "PreCommitBoundaryError: Direct end-activity is physically hard-blocked per ADR 0007. Delivery must be finalized in Infor LN Studio UI.",
            )
        }

        "ln_project_activity" => {
            let action = arg_str(arguments, "action").unwrap_or("project_info");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "action": action, "success": true }),
                    &format!("Project activity action '{}' completed", action),
                );
            }
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let act_arg = arg_str(arguments, "activity").or_else(|| arg_str(arguments, "source_activity"));
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, act_arg, arg_str(arguments, "project"));
            let task = arg_str(arguments, "task").unwrap_or("");

            let res: Result<Value, String> = match action {
                "project_info" => get_software_project_details(&client, &proj_name, None)
                    .await
                    .map(|p| json!({ "action": action, "project": p }))
                    .map_err(|e| e.to_string()),
                "list_activities" => list_remote_activities(&client, &proj_name)
                    .await
                    .map(|a| json!({ "action": action, "project": proj_name, "activities": a }))
                    .map_err(|e| e.to_string()),
                "new_activity" => {
                    let no_open = arguments.get("no_open").and_then(|v| v.as_bool()).unwrap_or(false);
                    let opts = CreateActivityOptions {
                        description: arg_str(arguments, "description").unwrap_or(task),
                        assigned_to: arg_str(arguments, "assigned_to").unwrap_or(""),
                        auto_open: !no_open,
                        workspace_path: if no_open { None } else { Some(&ctx.workspace_dir) },
                        ..Default::default()
                    };
                    create_remote_activity(&client, &proj_name, task, opts)
                        .await
                        .map(|c| json!({ "action": action, "activity": c }))
                        .map_err(|e| e.to_string())
                }
                "open_activity" => {
                    let ws_root = ctx.workspace_dir.clone();
                    let sync_mod = arguments.get("sync_modified").and_then(|v| v.as_bool()).unwrap_or(true);
                    match open_remote_activity(&client, &proj_name, task, Some(&ws_root), sync_mod).await {
                        Ok(res) => Ok(json!({ "action": action, "result": res })),
                        Err(err) => match bootstrap_local_activity(&ws_root, task, &proj_name, "", &dev_cp) {
                            Ok(p) => Ok(json!({ "action": action, "workspace_path": p, "note": err.to_string() })),
                            Err(io_err) => Err(io_err.to_string()),
                        },
                    }
                }
                "clean_activity" => clean_remote_activity(&client, &proj_name, task, None, false)
                    .await
                    .map(|ok| json!({ "action": action, "cleaned": ok }))
                    .map_err(|e| e.to_string()),
                "move_components" => {
                    let refs = parse_mcp_component_refs(arguments.get("components"));
                    let src_dir = act_opt.unwrap_or_else(|| ctx.workspace_dir.clone());
                    let target_task = arg_str(arguments, "target_activity").unwrap_or(task);
                    let meta = ActivityDotProject::from_activity_dir(&src_dir).ok();
                    let base_vrc = meta.as_ref().map(|m| m.application_release.clone()).unwrap_or_else(|| "B61O_a_ext".to_string());
                    match ln_scm::activity::get_remote_activity_details(&client, &proj_name, target_task).await {
                        Ok(Some(td)) => move_activity_components(&client, &refs, &src_dir, target_task, &td.label_uuid, &base_vrc, &dev_cp, None)
                            .await
                            .map(|mv| json!({ "action": action, "result": mv }))
                            .map_err(|e| e.to_string()),
                        Ok(None) => Err(format!("Target activity '{}' not found", target_task)),
                        Err(e) => Err(e.to_string()),
                    }
                }
                "clean_components" => {
                    let refs = parse_mcp_component_refs(arguments.get("components"));
                    let dir = act_opt.unwrap_or_else(|| ctx.workspace_dir.clone());
                    clean_activity_components(&client, &refs, &dir)
                        .await
                        .map(|r| json!({ "action": action, "result": r }))
                        .map_err(|e| e.to_string())
                }
                other => Err(format!("Unsupported action '{}'", other)),
            };

            let _ = client.disconnect_all().await;
            match res {
                Ok(data) => mcp_ok(name, data, &format!("Project activity action '{}' completed", action)),
                Err(e) => mcp_err(name, &e),
            }
        }

        "ln_code_intelligence" => {
            let action = arg_str(arguments, "action").unwrap_or("search_server");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "action": action, "results": [] }),
                    &format!("Code intelligence action '{}' completed", action),
                );
            }
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, arg_str(arguments, "activity"), arg_str(arguments, "project"));
            let res: Result<Value, String> = match action {
                "compile_source" => {
                    let pkg = arg_str(arguments, "package_code").unwrap_or("tx");
                    let src = arg_str(arguments, "source_code").unwrap_or("");
                    let flags = arg_str(arguments, "flags").unwrap_or("");
                    compile_source_adhoc(&client, pkg, src, flags, &proj_name, act_opt.as_deref())
                        .await
                        .map(|r| json!({ "action": action, "result": r }))
                        .map_err(|e| e.to_string())
                }
                "search_server" => {
                    let pat = arg_str(arguments, "pattern").unwrap_or("");
                    let pkg = arg_str(arguments, "package_code").unwrap_or("");
                    search_server_pattern(&client, pat, pkg, &proj_name, act_opt.as_deref())
                        .await
                        .map(|r| json!({ "action": action, "result": r }))
                        .map_err(|e| e.to_string())
                }
                "related_components" => {
                    let pkg = arg_str(arguments, "package_code").unwrap_or("tx");
                    let src = arg_str(arguments, "source_code").unwrap_or("");
                    get_related_script_components(&client, pkg, src, &proj_name, act_opt.as_deref())
                        .await
                        .map(|r| json!({ "action": action, "result": r }))
                        .map_err(|e| e.to_string())
                }
                "call_hierarchy" => {
                    let sf = arg_str(arguments, "source_file").unwrap_or("");
                    let fn_name = arg_str(arguments, "function_name").unwrap_or("");
                    let cm = arg_str(arguments, "call_mode").unwrap_or("callers");
                    get_call_hierarchy(&client, sf, fn_name, cm, &proj_name, act_opt.as_deref())
                        .await
                        .map(|r| json!({ "action": action, "result": r }))
                        .map_err(|e| e.to_string())
                }
                "open_declaration" => {
                    let cc = arg_str(arguments, "comp_code").unwrap_or("");
                    let ct = arg_str(arguments, "comp_type").unwrap_or("library");
                    let fn_name = arg_str(arguments, "function_name").unwrap_or("");
                    let ctxt = arg_str(arguments, "context").unwrap_or("script");
                    open_declaration(&client, cc, ct, fn_name, ctxt, &proj_name, act_opt.as_deref())
                        .await
                        .map(|r| json!({ "action": action, "result": r }))
                        .map_err(|e| e.to_string())
                }
                "generate_report_server" => {
                    let rn = arg_str(arguments, "report_name").unwrap_or("");
                    let tn = arg_str(arguments, "table_name").unwrap_or("");
                    let vid = arg_str(arguments, "version_id").unwrap_or("1");
                    let rs = arg_str(arguments, "report_size").unwrap_or("132");
                    let rt = arg_str(arguments, "report_type").unwrap_or("1");
                    let ui = arg_str(arguments, "used_index").unwrap_or("1");
                    let input_fields: Option<Vec<String>> = arguments
                        .get("input_fields")
                        .and_then(|v| v.as_array())
                        .map(|arr| arr.iter().filter_map(|x| x.as_str().map(str::to_string)).collect());
                    generate_report_on_server(
                        &client,
                        rn,
                        tn,
                        vid,
                        rn,
                        rs,
                        rt,
                        ui,
                        input_fields.as_deref(),
                        false,
                        &proj_name,
                        act_opt.as_deref(),
                    )
                    .await
                    .map(|r| json!({ "action": action, "result": r }))
                    .map_err(|e| e.to_string())
                }
                other => Err(format!("Unsupported code_intelligence action '{}'", other)),
            };
            let _ = client.disconnect_all().await;
            match res {
                Ok(data) => mcp_ok(name, data, &format!("Code intelligence action '{}' completed", action)),
                Err(e) => mcp_err(name, &e),
            }
        }

        "ln_version_diff" => {
            let action = arg_str(arguments, "action").unwrap_or("list_revisions");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "action": action, "diff": "" }),
                    &format!("Version diff action '{}' completed", action),
                );
            }
            let ct = arg_str(arguments, "comp_type").unwrap_or("");
            let cn = arg_str(arguments, "comp_name").unwrap_or("");
            let vid = arg_str(arguments, "version_id").unwrap_or("B61O_a_ext");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, arg_str(arguments, "activity"), arg_str(arguments, "project"));
            let res: Result<Value, String> = match action {
                "list_revisions" => list_component_revisions(&client, ct, cn, vid, &proj_name, act_opt.as_deref())
                    .await
                    .map(|r| json!({ "action": action, "result": r }))
                    .map_err(|e| e.to_string()),
                "get_revision" => {
                    let rev = arguments.get("rev_number").and_then(|v| v.as_u64()).unwrap_or(1) as usize;
                    get_component_revision(&client, ct, cn, vid, rev, &proj_name, act_opt.as_deref())
                        .await
                        .map(|xml| json!({ "action": action, "revision": rev, "xml": xml }))
                        .map_err(|e| e.to_string())
                }
                "diff_component" => {
                    let dir = act_opt.unwrap_or_else(|| ctx.workspace_dir.clone());
                    let rev = arguments.get("rev_number").and_then(|v| v.as_u64()).map(|n| n as usize);
                    diff_component(&client, ct, cn, &dir, Some(vid), rev, &proj_name)
                        .await
                        .map(|d| json!({ "action": action, "diff": d }))
                        .map_err(|e| e.to_string())
                }
                other => Err(format!("Unsupported version_diff action '{}'", other)),
            };
            let _ = client.disconnect_all().await;
            match res {
                Ok(data) => mcp_ok(name, data, &format!("Version diff action '{}' completed", action)),
                Err(e) => mcp_err(name, &e),
            }
        }

        "ln_adhoc_compile" => {
            let pkg = arg_str(arguments, "package_code").unwrap_or("tx");
            if is_mock(arguments) {
                return mcp_ok(
                    name,
                    json!({ "package": pkg, "compiled": true, "errors": 0 }),
                    "Ad-hoc compilation succeeded with 0 errors",
                );
            }
            let src = arg_str(arguments, "source_code").unwrap_or("");
            let flags = arg_str(arguments, "flags").unwrap_or("");
            let (ctx, client) = match mcp_resolve_ctx_and_client(arguments).await {
                Ok(v) => v,
                Err(e) => return mcp_err(name, &e),
            };
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, arg_str(arguments, "activity"), arg_str(arguments, "project"));
            let res = compile_source_adhoc(&client, pkg, src, flags, &proj_name, act_opt.as_deref()).await;
            let _ = client.disconnect_all().await;
            match res {
                Ok(c) => mcp_ok(name, json!(c), "Ad-hoc compilation completed"),
                Err(e) => mcp_err(name, &format!("compile_source_adhoc failed: {e}")),
            }
        }

        _ => mcp_err(name, &format!("Tool not found: '{}'", name)),
    }
}
