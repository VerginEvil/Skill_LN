#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_studio_mcp.py
Native Stdio Model Context Protocol (MCP) Server for Infor LN Studio.

Exposes the full Infor LN Studio Headless JCA engine, Explorers, 12-Component Generators,
Pre-Commit SCM Engine, and Build/Pre-Commit Pipeline as standard MCP tools.
Implements JSON-RPC 2.0 over stdio with zero third-party dependencies.

Enforces ADR 0006 (ReadOnlyComponentError for Extension Modeler tx* objects)
and ADR 0007 (PreCommitBoundaryError hard-blocking End Activity delivery).
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_workspace_manager import (
    list_workspaces, list_activities, resolve_activity, load_config, get_workspace_root
)
from ln_env_manager import (
    list_configured_environments, parse_ionapi, sync_cloudenv_prefs, sync_connectivity_prefs
)
from ln_server_client import (
    LNStudioServerClient, HeadlessJavaJcaTransport, MockJcaTransport
)
from ln_project_activity_manager import (
    list_applications, list_software_projects, get_software_project_details,
    list_remote_activities, create_remote_activity, open_remote_activity,
    clean_remote_activity, bootstrap_local_activity
)
from ln_code_intelligence import (
    compile_source_adhoc, search_server_pattern, get_call_hierarchy,
    open_declaration, get_related_script_components
)
from ln_revision_diff import (
    list_component_revisions, get_component_revision, diff_component,
    generate_report_on_server, move_activity_components, clean_activity_components
)
from ln_component_explorer import (
    browse_components, inspect_component, get_component, clone_component, sync_reference
)
from ln_scm_engine import (
    checkout_component, uncheckout_component, put_component, checkin_component,
    checkout_activity, checkin_activity, end_activity_gate, PreCommitBoundaryError,
    ReadOnlyComponentError, ServerSCMExecutionError
)
from ln_build_pipeline import (
    deploy_test, prepare_end_activity, compile_component, convert_to_runtime,
    create_tables, execute_vsc
)
from generate_ln_table import generate_all_components
from generate_ln_session import generate_session
from generate_ln_domain import generate_domains
from generate_ln_library import generate_libraries
from generate_ln_menu import generate_menus
from generate_ln_message import generate_messages
from generate_ln_question import generate_questions
from generate_ln_function import generate_functions
from generate_ln_additional import generate_additionals
from generate_ln_report import generate_reports
from validate_ln_activity import validate_activity


# Setup logger to write to stderr (stdio stdout is reserved exclusively for JSON-RPC)
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="[ln-studio-mcp] %(levelname)s: %(message)s"
)
logger = logging.getLogger("ln_studio_mcp")


TOOLS_REGISTRY: List[Dict[str, Any]] = [
    {
        "name": "ln_list_environments",
        "description": "Lists configured Infor LN customer workspaces, cloud environments, and connection status.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace_root": {"type": "string", "description": "Optional custom workspace root directory"}
            }
        }
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
        "name": "ln_end_activity",
        "description": "Hard-blocked pre-commit boundary gate. Infor LN Studio human review is required before activity finalization.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "activity": {"type": "string", "description": "Activity directory"},
                "project": {"type": "string", "description": "Software Project name"}
            }
        }
    },
    {
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
    },
    {
        "name": "ln_code_intelligence",
        "description": "Consolidated tool for FglStudio code intelligence and server report generation (search_server, call_hierarchy, open_declaration, generate_report_server).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["search_server", "call_hierarchy", "open_declaration", "generate_report_server"],
                    "description": "Sub-action to perform"
                },
                "pattern": {"type": "string", "description": "Search pattern or regex"},
                "package_code": {"type": "string", "description": "Package code (e.g. tx, td)"},
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
    },
    {
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
    },
    {
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
    }
]


def list_registered_tools() -> List[Dict[str, Any]]:
    """Returns list of registered MCP tools."""
    return TOOLS_REGISTRY


def _resolve_client(
    workspace_name: Optional[str] = None,
    mock: bool = False,
    target_object: Optional[str] = None,
    target_type: Optional[str] = None,
    target_activity: Optional[str] = None,
    notify: bool = False,
) -> LNStudioServerClient:
    """Builds an LNStudioServerClient with either mock or live JCA transport, enforcing pre-fetch verification."""
    from ln_component_builder import get_server_client
    client, _ = get_server_client(
        workspace_name=workspace_name,
        mock=mock,
        target_object=target_object,
        target_type=target_type,
        target_activity=target_activity,
        notify=notify,
    )
    return client


def _make_envelope(
    action: str,
    result: Any = None,
    message: str = "",
    status: str = "success"
) -> Dict[str, Any]:
    """
    Builds a normalized MCP response envelope adhering to ADR 0014:
    {
      "status": "success" | "error",
      "action": "<action>",
      "result": <data_or_wrapped_dict>,
      "message": "<message>"
    }
    """
    if isinstance(result, Path):
        result = str(result)
    elif isinstance(result, bool):
        result = {"success": result}

    env: Dict[str, Any] = {
        "status": status,
        "action": action,
        "result": result,
        "message": message or ("Success" if status == "success" else "Error"),
    }
    return env


def _format_mcp_response(env: Dict[str, Any], is_error: bool = False) -> Dict[str, Any]:
    """Helper to format canonical MCP JSON response."""
    return {
        "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
        "isError": is_error,
    }


def execute_tool(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes an MCP tool by name with arguments.
    Returns MCP content result: {"content": [{"type": "text", "text": "..."}], "isError": bool}
    """
    try:
        if name == "ln_list_environments":
            root = Path(arguments.get("workspace_root")) if arguments.get("workspace_root") else None
            envs = list_configured_environments(workspace_root=root)
            env = _make_envelope(name, {"workspaces": envs}, f"Found {len(envs)} workspaces")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_login":
            from ln_auth_helper import register_oob_protocol, execute_login
            from ln_env_manager import check_workspace_auth
            if arguments.get("register_protocol_only"):
                ok = register_oob_protocol()
                env = _make_envelope(name, {"protocol_registered": ok}, "Protocol registered" if ok else "Registration failed", status="success" if ok else "error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}
            ws = arguments.get("workspace")
            if arguments.get("check_only"):
                st = check_workspace_auth(workspace_name=ws)
                env = _make_envelope(name, st, "Workspace auth status")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            from ln_component_builder import resolve_ionapi_config
            env_name, cfg = resolve_ionapi_config(workspace_name=ws, ionapi_file=arguments.get("ionapi_file"))
            tok = execute_login(env_name=env_name, config=cfg, workspace_name=ws)
            env = _make_envelope(name, {
                "workspace": env_name,
                "token_type": tok.get("token_type"),
                "expires_in": tok.get("expires_in")
            }, "Login successful")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_connect":
            ionapi_path = Path(arguments["ionapi_file"])
            cfg = parse_ionapi(ionapi_path)
            cloud_res = sync_cloudenv_prefs(cfg)
            ws_res = False
            if arguments.get("workspace"):
                ws_res = sync_connectivity_prefs(cfg, workspace_name=arguments["workspace"])
            env = _make_envelope(name, {
                "imported": True,
                "description": cfg.description,
                "token_url": cfg.token_url,
                "cloudenv_prefs_updated": cloud_res,
                "connectivity_prefs_updated": ws_res
            }, "Connected and preferences updated")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_explore_projects":
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            projs = list_software_projects(client)
            env = _make_envelope(name, {"projects": projs}, f"Found {len(projs)} projects")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_explore_activities":
            project = arguments["project"]
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            acts = list_remote_activities(client, project_name=project)
            env = _make_envelope(name, {"project": project, "activities": acts}, f"Found {len(acts)} activities")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_explore_components":
            comp_type = arguments["type"]
            flt = arguments.get("filter", "*")
            project = arguments.get("project", "")
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            comps = browse_components(client, component_type=comp_type, name_filter=flt, project=project)
            env = _make_envelope(name, {"type": comp_type, "components": comps}, f"Found {len(comps)} components")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_create_activity":
            project = arguments["project"]
            act_id = arguments.get("task_id") or arguments.get("activity_id") or arguments.get("task", "")
            desc = arguments.get("description", act_id)
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            created_act = create_remote_activity(client, project_name=project, task_id=act_id, description=desc)
            local_path = None
            if arguments.get("bootstrap_local", True):
                ws_root = get_workspace_root()
                ws_name = arguments.get("workspace", "Team")
                target_dir = ws_root / ws_name / f"{act_id} [{project}]"
                bootstrap_local_activity(target_dir, project_name=project)
                local_path = str(target_dir)
            env = _make_envelope(name, {
                "success": True,
                "activity": created_act,
                "local_path": local_path
            }, f"Activity {act_id} created")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_clean_activity":
            project = arguments["project"]
            act_id = arguments.get("task_id") or arguments.get("activity_id") or arguments.get("task", "")
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            cleaned = clean_remote_activity(client, project_name=project, task_id=act_id)
            env = _make_envelope(name, {"cleaned": bool(cleaned)}, f"Activity {act_id} cleaned")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_get_component":
            comp_type = arguments["type"]
            name_val = arguments["name"]
            inspect_only = arguments.get("inspect_only", False)
            reference_only = arguments.get("reference_only", False) or comp_type.lower() == "extension"
            mock = arguments.get("mock", False)
            act_arg = arguments.get("activity")
            client = _resolve_client(
                workspace_name=arguments.get("workspace"),
                mock=mock,
                target_object=name_val,
                target_type=comp_type,
                target_activity=act_arg,
            )

            if inspect_only:
                res = inspect_component(client, comp_type=comp_type, comp_name=name_val)
            elif reference_only:
                ws_dir = Path(arguments.get("activity") or get_workspace_root() or Path.cwd())
                res = sync_reference(client, comp_type=comp_type, name_pattern=name_val, workspace_dir=ws_dir)
            else:
                act_path = Path(act_arg) if act_arg else Path(get_workspace_root())
                saved = get_component(client, comp_type=comp_type, comp_name=name_val, activity_dir=act_path)
                res = {"saved_path": str(saved), "read_only": True}
            env = _make_envelope(name, res, f"Fetched component {name_val}")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_sync_reference":
            comp_type = arguments["type"]
            name_val = arguments["name"]
            ws_dir = Path(arguments.get("workspace_dir") or get_workspace_root() or Path.cwd())
            dd_cache = Path(arguments["dd_cache_path"]) if arguments.get("dd_cache_path") else None
            mock = arguments.get("mock", False)
            client = _resolve_client(
                workspace_name=arguments.get("workspace"),
                mock=mock,
                target_object=name_val,
                target_type=comp_type,
            )
            res = sync_reference(
                client=client,
                comp_type=comp_type,
                name_pattern=name_val,
                workspace_dir=ws_dir,
                dd_cache_path=dd_cache,
            )
            env = _make_envelope(name, res, f"Reference {name_val} synced")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_checkout_component":
            comp_type = arguments["type"]
            name_val = arguments["name"]
            act_arg = arguments["activity"]
            proj = arguments.get("project", "EXTce01107")
            mock = arguments.get("mock", False)
            if Path(act_arg).is_dir() or "/" in str(act_arg) or "\\" in str(act_arg):
                act_dir = Path(act_arg).resolve()
            else:
                act_info = resolve_activity(activity_name=act_arg, workspace_name=arguments.get("workspace"))
                act_dir = Path(act_info["path"])
            client = _resolve_client(
                workspace_name=arguments.get("workspace"),
                mock=mock,
                target_object=name_val,
                target_type=comp_type,
                target_activity=str(act_dir),
            )
            res_path = checkout_component(client, comp_type, name_val, act_dir, proj)
            receipt_data = res_path.receipt.to_dict() if hasattr(res_path, "receipt") and res_path.receipt else None
            env = _make_envelope(name, {"checked_out": True, "path": str(res_path), "receipt": receipt_data}, f"Checked out {name_val}")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_uncheckout_component":
            comp_type = arguments["type"]
            name_val = arguments["name"]
            act_arg = arguments["activity"]
            proj = arguments.get("project", "EXTce01107")
            mock = arguments.get("mock", False)
            if Path(act_arg).is_dir() or "/" in str(act_arg) or "\\" in str(act_arg):
                act_dir = Path(act_arg).resolve()
            else:
                act_info = resolve_activity(activity_name=act_arg, workspace_name=arguments.get("workspace"))
                act_dir = Path(act_info["path"])
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            ok = uncheckout_component(client, comp_type, name_val, act_dir, proj)
            env = _make_envelope(name, {"uncheckout": bool(ok)}, f"Uncheckout {name_val}")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_checkin_component":
            comp_type = arguments["type"]
            name_val = arguments["name"]
            act_arg = arguments["activity"]
            proj = arguments.get("project", "EXTce01107")
            comment = arguments.get("comment", f"Check-in {name_val}")
            mock = arguments.get("mock", False)
            if Path(act_arg).is_dir() or "/" in str(act_arg) or "\\" in str(act_arg):
                act_dir = Path(act_arg).resolve()
            else:
                act_info = resolve_activity(activity_name=act_arg, workspace_name=arguments.get("workspace"))
                act_dir = Path(act_info["path"])
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            receipt = checkin_component(client, comp_type, name_val, act_dir, proj, comment=comment)
            receipt_data = receipt.to_dict() if hasattr(receipt, "to_dict") else receipt
            env = _make_envelope(name, {"checkin": True, "receipt": receipt_data}, f"Checked in {name_val}")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_checkout_activity":
            act_arg = arguments["activity"]
            proj = arguments.get("project", "EXTce01107")
            mock = arguments.get("mock", False)
            client = _resolve_client(
                workspace_name=arguments.get("workspace"),
                mock=mock,
                target_object="activity",
                target_type="activity",
                target_activity=str(act_arg),
            )
            if Path(act_arg).is_dir() or "/" in str(act_arg) or "\\" in str(act_arg):
                act_dir = Path(act_arg).resolve()
            else:
                act_info = resolve_activity(activity_name=act_arg, workspace_name=arguments.get("workspace"))
                act_dir = Path(act_info["path"])
            res = checkout_activity(client, act_dir, proj)
            env = _make_envelope(name, res, "Activity checked out")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_checkin_activity":
            act_arg = arguments["activity"]
            proj = arguments.get("project", "EXTce01107")
            comment = arguments.get("comment", "Automated activity check-in")
            mock = arguments.get("mock", False)
            client = _resolve_client(
                workspace_name=arguments.get("workspace"),
                mock=mock,
                target_object="activity",
                target_type="activity",
                target_activity=str(act_arg),
            )
            if Path(act_arg).is_dir() or "/" in str(act_arg) or "\\" in str(act_arg):
                act_dir = Path(act_arg).resolve()
            else:
                act_info = resolve_activity(activity_name=act_arg, workspace_name=arguments.get("workspace"))
                act_dir = Path(act_info["path"])
            res = checkin_activity(client, act_dir, proj, comment=comment)
            env = _make_envelope(name, res, "Activity checked in")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_create_component":
            ctype = arguments["type"].lower()
            code = arguments["code"]
            desc = arguments.get("description", code)
            act_dir = Path(arguments["activity"])
            proj = arguments.get("project", "EXTce01107")
            dry = arguments.get("dry_run", False)
            spec_extra = arguments.get("spec", {})

            created_files = []
            if ctype == "message":
                spec = {"code": code, "description": desc, "severity": spec_extra.get("severity", "3"), "text": spec_extra.get("text", desc)}
                created_files = generate_messages([spec], act_dir, proj, dry_run=dry)
            elif ctype == "question":
                spec = {"code": code, "description": desc, "severity": spec_extra.get("severity", "2"), "domain": spec_extra.get("domain", "tcyesno"), "default_answer": spec_extra.get("default_answer", "yes"), "text": spec_extra.get("text", desc)}
                created_files = generate_questions([spec], act_dir, proj, dry_run=dry)
            elif ctype == "function":
                spec = {"code": code, "description": desc, "script": spec_extra.get("script", "")}
                created_files = generate_functions([spec], act_dir, proj, dry_run=dry)
            elif ctype == "additional":
                spec = {"code": code, "description": desc, "content": spec_extra.get("content", ""), "keyword1": spec_extra.get("keyword1", ""), "keyword2": spec_extra.get("keyword2", ""), "keyword3": spec_extra.get("keyword3", "")}
                created_files = generate_additionals([spec], act_dir, proj, dry_run=dry)
            elif ctype == "report":
                spec = {"code": code, "description": desc, "paper_width": spec_extra.get("paper_width", 80), "script": spec_extra.get("script", "")}
                created_files = generate_reports([spec], act_dir, proj, dry_run=dry)
            elif ctype == "domain":
                spec = {"name": code, "description": desc, "type": spec_extra.get("data_type", "String"), "length": spec_extra.get("length", 30)}
                created_files = generate_domains(spec, activity_name=str(act_dir), dry_run=dry)
            else:
                env = _make_envelope(name, None, f"Component type '{ctype}' generation via MCP must use schema parser or specific generator.", status="error")
                return {
                    "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                    "isError": True
                }

            env = _make_envelope(name, {"created_files": [str(p) for p in created_files]}, f"Created {len(created_files)} files")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_clone_component":
            stype = arguments.get("comp_type") or arguments.get("source_type", "")
            sname = arguments["source_name"]
            tname = arguments["target_name"]
            act_dir = Path(arguments["activity"])
            tdesc = arguments.get("target_desc", tname)
            proj = arguments.get("project", "EXTce01107")
            mock = arguments.get("mock", False)
            register = arguments.get("register_on_server", True)
            cp = arguments.get("connection_point", "ProjectServer")
            act_uuid = arguments.get("activity_uuid")
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            cloned = clone_component(
                client=client,
                comp_type=stype,
                source_name=sname,
                target_name=tname,
                activity_dir=act_dir,
                register_on_server=register,
                connection_point=cp,
                activity_uuid=act_uuid,
            )
            env = _make_envelope(name, {"cloned_path": str(cloned)}, f"Cloned {sname} to {tname}")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_validate_activity":
            act_dir = Path(arguments["activity"])
            strict = arguments.get("strict", False)
            report = validate_activity(act_dir, strict=strict)
            is_valid = len(report.errors) == 0
            summary = {
                "files_scanned": report.files_scanned,
                "errors_count": len(report.errors),
                "warnings_count": len(report.warnings),
                "errors": [str(e) for e in report.errors],
                "warnings": [str(w) for w in report.warnings],
                "valid": is_valid
            }
            env = _make_envelope(name, summary, "Activity valid" if is_valid else "Activity validation failed", status="success" if is_valid else "error")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": not is_valid
            }

        elif name == "ln_deploy_test":
            comp_type = arguments["type"]
            name_val = arguments["name"]
            act_dir = Path(arguments["activity"])
            proj = arguments.get("project", "EXTce01107")
            comment = arguments.get("comment", f"deploy-test for {name_val}")
            mode = arguments.get("mode", "compile-only")
            dry_run = arguments.get("dry_run", False)
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            res = deploy_test(
                client,
                comp_type,
                name_val,
                act_dir,
                proj,
                comment=comment,
                mode=mode,
                dry_run=dry_run,
            )
            ok = bool(res.get("success", False))
            env = _make_envelope(name, res, "Deploy test completed" if ok else "Deploy test failed", status="success" if ok else "error")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": not ok
            }

        elif name == "ln_prepare_end_activity":
            act_dir = Path(arguments["activity"])
            proj = arguments.get("project", "EXTce01107")
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            res = prepare_end_activity(client, activity_dir=act_dir, project_name=proj)
            ok = bool(res.get("ready_for_human_review", False))
            env = _make_envelope(name, res, "Ready for human review" if ok else "Not ready for review", status="success" if ok else "error")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": not ok
            }

        elif name == "ln_end_activity":
            # ADR 0007 Pre-commit boundary gate
            proj = arguments.get("project", "EXTce01107")
            task = arguments.get("activity", "task_01")
            end_activity_gate(project_name=proj, task_id=task)
            env = _make_envelope(name, {"completed": True}, "End activity completed")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": False
            }

        elif name == "ln_project_activity":
            action = arguments["action"]
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            if action == "project_info":
                details = get_software_project_details(client, arguments["project"])
                env = _make_envelope("project_info", details, f"Project info for {arguments['project']}")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            elif action == "list_activities":
                acts = list_remote_activities(client, project_name=arguments["project"])
                env = _make_envelope("list_activities", {"activities": acts}, f"Activities for {arguments['project']}")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            elif action == "new_activity":
                task_id = arguments.get("task_id") or arguments.get("task", "")
                auto_open = not arguments.get("no_open", False) if "no_open" in arguments else arguments.get("auto_open", False)
                ws_path = arguments.get("workspace_path") or arguments.get("workspace")
                res = create_remote_activity(
                    client=client,
                    project_name=arguments["project"],
                    task_id=task_id,
                    description=arguments.get("description", ""),
                    assigned_to=arguments.get("assigned_to", ""),
                    auto_open=auto_open,
                    workspace_path=ws_path,
                )
                ok = bool(res.get("created") or res.get("status") == "success" or res.get("task_id"))
                env = _make_envelope("new_activity", res, f"Activity {task_id} created" if ok else "Failed to create activity", status="success" if ok else "error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}
            elif action == "open_activity":
                task_id = arguments.get("task_id") or arguments.get("task", "")
                ws_path = arguments.get("workspace_path") or arguments.get("workspace")
                res = open_remote_activity(
                    client=client,
                    project_name=arguments["project"],
                    task_name=task_id,
                    sync_modified=arguments.get("sync_modified", True),
                    workspace_path=ws_path,
                )
                ok = bool(res.get("opened") or res.get("status") == "opened" or res.get("status") == "success")
                env = _make_envelope("open_activity", res, f"Activity {task_id} opened" if ok else "Failed to open activity", status="success" if ok else "error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}
            elif action == "clean_activity":
                task_id = arguments.get("task_id") or arguments.get("task", "")
                cleaned = clean_remote_activity(
                    client=client,
                    project_name=arguments["project"],
                    task_id=task_id,
                )
                env = _make_envelope("clean_activity", {"cleaned": bool(cleaned)}, f"Activity {task_id} cleaned")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not bool(cleaned)}
            elif action == "move_components":
                src_dir = Path(arguments["source_activity"]).resolve()
                tgt_dir = Path(arguments["target_activity"]).resolve() if arguments.get("target_activity") else None
                comps = arguments.get("components", [])
                if isinstance(comps, str):
                    comps = [{"type": item.split(":")[0], "name": item.split(":")[1]} for item in comps.split(",") if ":" in item]
                res = move_activity_components(
                    client=client,
                    components=comps,
                    source_activity_dir=src_dir,
                    target_task_name=arguments.get("task", ""),
                    target_task_uuid=arguments.get("task_uuid", arguments.get("task", "")),
                    target_base_vrc=arguments.get("base_vrc", "1"),
                    target_context=arguments.get("context", "ProjectServer"),
                    target_activity_dir=tgt_dir,
                )
                ok = bool(res.get("success", False))
                env = _make_envelope("move_components", res, "Moved components" if ok else "Failed to move components", status="success" if ok else "error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}
            elif action == "clean_components":
                act_dir = Path(arguments["activity"]).resolve()
                comps = arguments.get("components", [])
                if isinstance(comps, str):
                    comps = [{"type": item.split(":")[0], "name": item.split(":")[1]} for item in comps.split(",") if ":" in item]
                res = clean_activity_components(client=client, components=comps, activity_dir=act_dir)
                ok = bool(res.get("success", False))
                env = _make_envelope("clean_components", res, "Cleaned components" if ok else "Failed to clean components", status="success" if ok else "error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}
            else:
                env = _make_envelope(action, None, f"Unknown action: '{action}'", status="error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": True}

        elif name == "ln_code_intelligence":
            action = arguments["action"]
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            act_dir = Path(arguments["activity"]).resolve() if arguments.get("activity") else None
            if action == "search_server":
                res = search_server_pattern(
                    client=client,
                    pattern=arguments["pattern"],
                    package_code=arguments.get("package_code", ""),
                    project_name=arguments.get("project", ""),
                    activity_dir=act_dir,
                )
                env = _make_envelope("search_server", res, "Server search completed")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            elif action == "call_hierarchy":
                res = get_call_hierarchy(
                    client=client,
                    source_file_name=arguments["source_file"],
                    function_name=arguments["function_name"],
                    call_mode=arguments.get("call_mode", "callers"),
                    project_name=arguments.get("project", ""),
                    activity_dir=act_dir,
                )
                env = _make_envelope("call_hierarchy", res, "Call hierarchy retrieved")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            elif action == "open_declaration":
                res = open_declaration(
                    client=client,
                    comp_code=arguments["comp_code"],
                    comp_type=arguments["comp_type"],
                    function_name=arguments["function_name"],
                    context=arguments.get("context", ""),
                    project_name=arguments.get("project", ""),
                    activity_dir=act_dir,
                )
                ok = bool(res.get("found", False))
                env = _make_envelope("open_declaration", res, "Declaration found" if ok else "Declaration not found", status="success" if ok else "error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}
            elif action == "generate_report_server":
                res = generate_report_on_server(
                    client=client,
                    report_name=arguments["report_name"],
                    table_name=arguments["table_name"],
                    version_id=arguments.get("version_id", "1"),
                    report_size=arguments.get("report_size", "80"),
                    report_type=arguments.get("report_type", "1"),
                    used_index=arguments.get("used_index", "1"),
                    input_fields=arguments.get("input_fields"),
                    activity_dir=act_dir,
                    project_name=arguments.get("project", ""),
                )
                ok = bool(res.get("success", False))
                env = _make_envelope("generate_report_server", res, "Server report generated" if ok else "Report generation failed", status="success" if ok else "error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}
            else:
                env = _make_envelope(action, None, f"Unknown action: '{action}'", status="error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": True}

        elif name == "ln_version_diff":
            action = arguments["action"]
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            act_dir = Path(arguments["activity"]).resolve() if arguments.get("activity") else None
            if action == "list_revisions":
                res = list_component_revisions(
                    client=client,
                    comp_type=arguments["comp_type"],
                    comp_name=arguments["comp_name"],
                    version_id=arguments.get("version_id", "1"),
                    project_name=arguments.get("project", ""),
                    activity_dir=act_dir,
                )
                env = _make_envelope("list_revisions", res, "Component revisions listed")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            elif action == "get_revision":
                rev_num = int(arguments.get("rev_number", 1))
                res_xml = get_component_revision(
                    client=client,
                    comp_type=arguments["comp_type"],
                    comp_name=arguments["comp_name"],
                    version_id=arguments.get("version_id", "1"),
                    rev_number=rev_num,
                    project_name=arguments.get("project", ""),
                    activity_dir=act_dir,
                )
                env = _make_envelope("get_revision", {"xml": res_xml}, "Revision XML fetched")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            elif action == "diff_component":
                if not act_dir:
                    env = _make_envelope("diff_component", None, "activity is required for diff_component", status="error")
                    return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": True}
                rev_num = int(arguments["rev_number"]) if arguments.get("rev_number") is not None else None
                res = diff_component(
                    client=client,
                    comp_type=arguments["comp_type"],
                    comp_name=arguments["comp_name"],
                    activity_dir=act_dir,
                    target_version_id=arguments.get("version_id"),
                    target_rev_number=rev_num,
                    project_name=arguments.get("project", ""),
                )
                env = _make_envelope("diff_component", res, "Component diffed")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": False}
            else:
                env = _make_envelope(action, None, f"Unknown action: '{action}'", status="error")
                return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": True}

        elif name == "ln_adhoc_compile":
            mock = arguments.get("mock", False)
            client = _resolve_client(workspace_name=arguments.get("workspace"), mock=mock)
            act_dir = Path(arguments["activity"]).resolve() if arguments.get("activity") else None
            res = compile_source_adhoc(
                client=client,
                package_code=arguments["package_code"],
                source_code=arguments["source_code"],
                flags=arguments.get("flags", ""),
                project_name=arguments.get("project", ""),
                activity_dir=act_dir,
            )
            ok = bool(res.get("success", False))
            env = _make_envelope(name, res, "Adhoc compile succeeded" if ok else "Adhoc compile failed", status="success" if ok else "error")
            return {"content": [{"type": "text", "text": json.dumps(env, indent=2)}], "isError": not ok}

        else:
            env = _make_envelope(name, None, f"Unknown tool: '{name}'", status="error")
            return {
                "content": [{"type": "text", "text": json.dumps(env, indent=2)}],
                "isError": True
            }

    except PreCommitBoundaryError as pe:
        env = _make_envelope(name, None, f"PreCommitBoundaryError: {str(pe)}", status="error")
        return _format_mcp_response(env, is_error=True)
    except ServerSCMExecutionError as se:
        env = _make_envelope(name, None, f"ServerSCMExecutionError: {str(se)}", status="error")
        return _format_mcp_response(env, is_error=True)
    except ReadOnlyComponentError as re:
        env = _make_envelope(name, None, f"ReadOnlyComponentError: {str(re)}", status="error")
        return _format_mcp_response(env, is_error=True)
    except Exception as e:
        logger.exception(f"Error executing tool {name}")
        env = _make_envelope(name, None, f"{type(e).__name__}: {str(e)}", status="error")
        return _format_mcp_response(env, is_error=True)


def handle_jsonrpc_request(request: Dict[str, Any], server_state: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    """
    Handles a single JSON-RPC 2.0 MCP request and returns the response dictionary.
    Returns None for notifications (no id).
    """
    msg_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if not method:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32600, "message": "Invalid Request: missing method"}
        }

    # Notification handling
    if msg_id is None and method.startswith("notifications/"):
        return None

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": params.get("protocolVersion", "2024-11-05"),
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "infor-ln-studio-mcp",
                    "version": "1.0.1"
                }
            }
        }

    elif method == "ping":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {}
        }

    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": list_registered_tools()
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})
        if not tool_name:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32602, "message": "Missing tool name in tools/call"}
            }
        call_res = execute_tool(tool_name, tool_args)
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": call_res
        }

    else:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32601, "message": f"Method not found: '{method}'"}
        }


def generate_mcp_config(client: str = "generic") -> Dict[str, Any]:
    """Generates MCP configuration dictionary for registering ln_studio_mcp."""
    server_script = str((_TOOLS_DIR / "ln_studio_mcp.py").resolve())
    return {
        "mcpServers": {
            "infor-ln-studio": {
                "command": sys.executable,
                "args": [server_script]
            }
        }
    }


def get_default_mcp_config_path(client: str) -> Optional[Path]:
    """Returns default config file path for known AI coding agent clients."""
    home = Path.home()
    if client == "claude":
        appdata = os.environ.get("APPDATA")
        if appdata:
            return Path(appdata) / "Claude" / "claude_desktop_config.json"
        return home / ".config" / "Claude" / "claude_desktop_config.json"
    elif client == "cursor":
        return Path.cwd() / ".cursor" / "mcp.json"
    elif client == "antigravity":
        return home / ".gemini" / "antigravity" / "mcp" / "ln_studio.json"
    return None


def register_mcp_config(client: str = "generic", config_path: Optional[Path] = None, dry_run: bool = False) -> Dict[str, Any]:
    """Inspects, merges, and writes MCP configuration for the specified client."""
    target_path = config_path or get_default_mcp_config_path(client)
    cfg = generate_mcp_config(client=client)

    if target_path and target_path.exists():
        try:
            existing = json.loads(target_path.read_text(encoding="utf-8"))
            if "mcpServers" not in existing:
                existing["mcpServers"] = {}
            existing["mcpServers"]["infor-ln-studio"] = cfg["mcpServers"]["infor-ln-studio"]
            cfg = existing
        except Exception:
            pass

    if not dry_run and target_path:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")

    return {
        "client": client,
        "config_path": str(target_path) if target_path else "stdout",
        "dry_run": dry_run,
        "applied": not dry_run and target_path is not None,
        "config": cfg
    }


def run_stdio_server():
    """Runs the Stdio MCP server loop reading newline-delimited JSON-RPC from stdin."""
    logger.info("Infor LN Studio MCP Server running on stdio...")
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            line_str = line.strip()
            if not line_str:
                continue

            # Support Content-Length header framing if client sends it
            if line_str.lower().startswith("content-length:"):
                length = int(line_str.split(":", 1)[1].strip())
                # Read empty line separating header from body
                sys.stdin.readline()
                body = sys.stdin.read(length)
                req = json.loads(body)
            else:
                req = json.loads(line_str)

            resp = handle_jsonrpc_request(req)
            if resp is not None:
                out_str = json.dumps(resp)
                sys.stdout.write(out_str + "\n")
                sys.stdout.flush()

        except (KeyboardInterrupt, EOFError):
            break
        except Exception as e:
            logger.exception("Error in MCP stdio loop")
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {str(e)}"}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


def main():
    run_stdio_server()


if __name__ == "__main__":
    main()