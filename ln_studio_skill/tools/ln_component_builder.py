#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_component_builder.py
Unified Component Builder & Pipeline Orchestrator for Infor LN Studio.

Master CLI entrypoint that unifies:
  - Declarative schema validation (ln_schema_parser)
  - Table, domain, and label generation (generate_ln_table, generate_ln_domain)
  - Session and dynamic form generation (generate_ln_session)
  - Library generation (generate_ln_library)
  - Menu generation (generate_ln_menu)
  - Bidirectional 4GL source synchronization (inject_ln_script)
  - Eclipse SCM cache synchronization (admin_sync)
  - 4-layer activity validation (validate_ln_activity)
  - Static 4GL script checking (check_4gl_script)
  - Windows action bridge & build triggering (ln_studio_bridge)
  - Eclipse Problem Marker diagnostics (ln_error_reader)
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import Optional, List, Dict, Any

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_workspace_manager import (
    list_workspaces, list_activities, resolve_activity, load_config, save_config, get_workspace_root, detect_current_activity
)
from ln_schema_parser import parse_schema_file, SchemaValidationError
from generate_ln_table import generate_all_components
from generate_ln_session import generate_session
from generate_ln_domain import generate_domains
from generate_ln_library import generate_libraries
from generate_ln_menu import generate_menus
from inject_ln_script import inject_file, extract_file, sync_all_activity_scripts
from admin_sync import scan_and_sync_activity, list_admin_components
from ln_error_reader import read_activity_diagnostics
from ln_studio_bridge import trigger_build_and_diagnose
from check_4gl_script import check_file as check_4gl_file
from validate_ln_activity import ActivityValidator, validate_activity
from ln_extension_manager import (
    new_extension, import_extension, list_hooks, get_hook, copy_to_clipboard
)
from ln_env_manager import (
    parse_ionapi, sync_cloudenv_prefs, sync_connectivity_prefs,
    list_configured_environments, OAuth2TokenManager, IonapiConfig
)
from ln_server_client import (
    LNStudioServerClient, HeadlessJavaJcaTransport, MockJcaTransport
)
from ln_project_activity_manager import (
    list_applications, list_software_projects, get_software_project_details,
    list_remote_activities, create_remote_activity, clean_remote_activity,
    bootstrap_local_activity
)
from ln_component_explorer import (
    browse_components, inspect_component, get_component, clone_component,
    BDE_TYPE_MAP
)
from ln_scm_engine import (
    checkout_component, uncheckout_component, put_component, checkin_component,
    end_activity_gate, PreCommitBoundaryError
)
from ln_build_pipeline import (
    parse_compile_diagnostics, compile_component, convert_to_runtime,
    create_tables, execute_vsc, deploy_test, prepare_end_activity
)
from generate_ln_message import generate_messages
from generate_ln_question import generate_questions
from generate_ln_function import generate_functions
from generate_ln_additional import generate_additionals
from generate_ln_report import generate_reports
from ln_studio_mcp import register_mcp_config, get_default_mcp_config_path


def cmd_workspace(args):
    """Handles 'workspace' subcommand."""
    if args.list:
        wss = list_workspaces()
        print(f"Available Workspaces ({len(wss)}):")
        for w in wss:
            print(f"  - {w}")
    elif args.activities:
        acts = list_activities(workspace_name=args.workspace)
        print(f"Activities ({len(acts)}):")
        for a in acts:
            print(f"  [{a['workspace']}] {a['folder_name']}")
    elif args.set_default:
        cfg = load_config()
        cfg["default_activity"] = args.set_default
        save_config(cfg)
        print(f"[OK] Set default activity: '{args.set_default}'")
    else:
        cfg = load_config()
        print("Workspace Status:")
        print(f"  Root:             {get_workspace_root()}")
        print(f"  Default Activity: {cfg.get('default_activity', '(not set)')}")


def cmd_environments(args):
    """Handles 'environments' subcommand."""
    ws_root = Path(args.workspace_root).resolve() if getattr(args, "workspace_root", None) else None
    envs = list_configured_environments(workspace_root=ws_root)
    if getattr(args, "json", False):
        print(json.dumps(envs, indent=2))
        return

    print(f"Configured Customer Workspaces ({len(envs)}):")
    fmt = "{:<12} {:<12} {:<24} {:<18} {:<18}"
    print(fmt.format("Workspace", "CloudEnv", "TenantID", "Dev Point", "RT Point"))
    print("-" * 88)
    for name, info in envs.items():
        print(fmt.format(
            name,
            info.get("cloud_env") or "-",
            info.get("tenant_id") or "-",
            info.get("dev_point") or "-",
            info.get("rt_point") or "-"
        ))


def cmd_connect(args):
    """Handles 'connect' subcommand."""
    ionapi_path = Path(args.ionapi).resolve()
    config = parse_ionapi(ionapi_path)
    env_name = args.env_name or ionapi_path.stem

    from ln_workspace_manager import get_studio_installation_path, get_workspace_root
    studio_path = get_studio_installation_path()
    cloudenv_prefs = studio_path / "configuration" / ".settings" / "com.infor.erpln.jca.connectivity.cloudenv.prefs"
    sync_cloudenv_prefs(cloudenv_prefs, env_name, config)
    print(f"[OK] Synchronized global cloudenv.prefs for '{env_name}' ({config.tenant_id})")

    # If target workspace specified or found, sync workspace connectivity.prefs
    ws_root = get_workspace_root()
    if ws_root and (args.workspace or (ws_root / env_name).exists()):
        ws_name = args.workspace or env_name
        ws_path = ws_root / ws_name
        conn_prefs = ws_path / ".metadata" / ".plugins" / "org.eclipse.core.runtime" / ".settings" / "com.infor.erpln.jca.connectivity.prefs"
        sync_connectivity_prefs(conn_prefs, env_name, config, project_name=args.project)
        print(f"[OK] Synchronized workspace connectivity.prefs in '{ws_path}'")

    token_mgr = OAuth2TokenManager()
    token = None
    try:
        token = token_mgr.get_access_token(env_name, config)
        print(f"[OK] OAuth2 Access Token acquired successfully (length: {len(token)})")
    except Exception as e:
        print(f"[WARN] Could not acquire token automatically: {e}")

    if getattr(args, "ping", False):
        if not token:
            print("[ERROR] Cannot ping: No valid access token available.", file=sys.stderr)
            sys.exit(1)
        transport = HeadlessJavaJcaTransport(
            gateway_url=config.gateway_url,
            tenant_id=config.tenant_id,
            access_token=token,
            studio_path=studio_path,
        )
        client = LNStudioServerClient(transport=transport)
        if client.ping():
            print(f"[SUCCESS] JCA ping succeeded for '{env_name}' on Infor LN Server!")
        else:
            print(f"[ERROR] JCA ping failed for '{env_name}'.", file=sys.stderr)
            sys.exit(1)


def get_server_client(workspace_name: Optional[str] = None, mock: bool = False) -> Tuple[LNStudioServerClient, Dict[str, Any]]:
    """Helper to resolve workspace connectivity and instantiate LNStudioServerClient."""
    if mock:
        transport = MockJcaTransport()
        transport.register_response(
            "Application", "List",
            "<Applications><Application><name>LN</name><title>Infor LN</title></Application></Applications>"
        )
        transport.register_response(
            "SoftwareProject", "List",
            "<SoftwareProjects><SoftwareProject><name>EXTce01107</name><description>Customer Project</description><status>active</status></SoftwareProject></SoftwareProjects>"
        )
        transport.register_response(
            "SoftwareProject_V2", "Show",
            "<SoftwareProject_V2><name>EXTce01107</name><Tasks><Task><taskId>task_01</taskId><uuid>uuid-1</uuid><description>Test</description><status>open</status></Task></Tasks></SoftwareProject_V2>"
        )
        transport.register_response(
            "SoftwareProject_V2", "Change",
            "<SoftwareProject_V2><Tasks action=\"create\"><Task><taskId>new_task</taskId><uuid>uuid-new</uuid><status>created</status></Task></Tasks></SoftwareProject_V2>"
        )
        transport.register_response("FglStudio", "CleanActivity", "<FglStudio><CleanActivityResponse><status>success</status></CleanActivityResponse></FglStudio>")
        transport.register_response(
            "StudioComponent", "GetBrowseList",
            "<StudioComponent><Component><name>tcibd001</name><type>table</type><package>tc</package><module>ibd</module><description>General Item Data</description></Component></StudioComponent>"
        )
        transport.register_response(
            "DR_Table", "Get",
            "<DR_Table name=\"tcibd001\" package=\"tc\" module=\"ibd\"><description>Item Data</description><Fields><Field name=\"item\" domain=\"tcitem\" label=\"tcibd001.item\"/></Fields></DR_Table>"
        )
        transport.register_response("DR_Table", "DR_Create", "<DR_Table><status>created</status></DR_Table>")
        transport.register_response("DR_Table", "CheckOut", "<DR_Table name=\"tdsls400\" package=\"td\" module=\"sls\"><desc>Sales Order</desc></DR_Table>")
        transport.register_response("DR_Table", "UndoCheckOut", "<DR_Table><status>uncheck_out_success</status></DR_Table>")
        transport.register_response("DR_Table", "CheckIn", "<DR_Table><status>checked_in</status></DR_Table>")
        transport.register_response("DR_Table", "Compile", "<CompileResponse><status>success</status></CompileResponse>")
        transport.register_response("DR_Table", "ConvertToRuntime", "<ConvertToRuntimeResponse>OK</ConvertToRuntimeResponse>")
        transport.register_response("DR_Table", "CreateTables", "<CreateTablesResponse>OK</CreateTablesResponse>")
        transport.register_response("DR_Table", "executeVSC", "<executeVSCResponse><status>pass</status></executeVSCResponse>")
        transport.register_response("DR_Solution", "ValidateDevelopmentActivity", "<ValidateResponse><status>valid</status></ValidateResponse>")
        return LNStudioServerClient(transport=transport), {"workspace": "mock", "cloud_env": "mock", "tenant_id": "mock"}

    from ln_workspace_manager import get_workspace_root
    ws_root = get_workspace_root()
    envs = list_configured_environments(ws_root)
    ws = workspace_name
    if not ws:
        cfg = load_config()
        ws = cfg.get("default_workspace") or (list(envs.keys())[0] if envs else None)

    if not ws or ws not in envs:
        raise ValueError(f"Could not resolve workspace '{ws}'. Available: {list(envs.keys())}")

    env_info = envs[ws]
    cloud_env = env_info["cloud_env"] or ws
    tenant_id = env_info["tenant_id"]

    from ln_workspace_manager import get_studio_installation_path
    studio_path = get_studio_installation_path()
    cloudenv_prefs = studio_path / "configuration" / ".settings" / "com.infor.erpln.jca.connectivity.cloudenv.prefs"

    from ln_env_manager import _read_prefs_file
    props = _read_prefs_file(cloudenv_prefs)
    count = int(props.get("EnvironmentsCount", "0"))
    cfg_found = None
    for i in range(count):
        if props.get(f"EnvironmentName{i}") == cloud_env:
            cfg_found = IonapiConfig(
                tenant_id=props.get(f"TenantID{i}", tenant_id),
                client_name="LNStudio",
                device_type="11",
                client_id=props.get(f"ClientID{i}", ""),
                client_secret=props.get(f"ClientSecret{i}", ""),
                gateway_url=props.get(f"GatewayURL{i}", ""),
                auth_url=props.get(f"AuthorizationCodeURL{i}", ""),
                token_url=props.get(f"RequestTokenURL{i}", ""),
                revoke_url=props.get(f"RevokeTokenURL{i}", ""),
            )
            break

    if not cfg_found:
        raise RuntimeError(f"CloudEnvironment '{cloud_env}' not found in cloudenv.prefs. Run 'connect' first.")

    token_mgr = OAuth2TokenManager()
    token = token_mgr.get_access_token(cloud_env, cfg_found)

    transport = HeadlessJavaJcaTransport(
        gateway_url=cfg_found.gateway_url,
        tenant_id=cfg_found.tenant_id,
        access_token=token,
        studio_path=studio_path,
        workspace_path=env_info.get("workspace_path"),
    )
    return LNStudioServerClient(transport=transport), env_info


def cmd_project(args):
    """Handles 'project' subcommand."""
    client, _ = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if args.project:
        details = get_software_project_details(client, args.project)
        if getattr(args, "json", False):
            print(json.dumps(details, indent=2))
        else:
            print(f"Software Project: {details['name']}")
            print(f"  Description:  {details['description']}")
            print(f"  Base VRC:     {details['baseVRC']}")
            print(f"  WorkSet VRC:  {details['workSetVRC']}")
            print(f"  Packages:     {', '.join(details['packages'])}")
    else:
        apps = list_applications(client)
        projs = list_software_projects(client)
        if getattr(args, "json", False):
            print(json.dumps({"applications": apps, "projects": projs}, indent=2))
        else:
            print(f"Applications ({len(apps)}):")
            for a in apps:
                print(f"  - {a['name']:<15} {a['description']}")
            print(f"\nSoftware Projects ({len(projs)}):")
            for p in projs:
                print(f"  - {p['name']:<15} [{p['status']}] {p['description']}")


def cmd_activity(args):
    """Handles 'activity' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    project_name = args.project or env_info.get("dev_point", "").replace("_dev", "")
    if not project_name:
        raise ValueError("Must specify --project (e.g. EXTce01107)")

    if getattr(args, "create", None):
        task_id = args.create
        desc = getattr(args, "desc", None) or f"Activity {task_id}"
        res = create_remote_activity(client, project_name, task_id, desc)
        if getattr(args, "bootstrap", False):
            from ln_workspace_manager import get_workspace_root
            ws_root = get_workspace_root()
            ws_path = ws_root / (args.workspace or env_info["workspace"])
            act_path = bootstrap_local_activity(
                workspace_path=ws_path,
                task_id=task_id,
                project_name=project_name,
                activity_uuid=res.get("uuid", ""),
                dev_connection=env_info.get("dev_point", f"{project_name}_dev"),
            )
            res["local_path"] = str(act_path)
            print(f"[SUCCESS] Bootstrapped activity folder: {act_path}")

        if getattr(args, "json", False):
            print(json.dumps(res, indent=2))
        else:
            print(f"[OK] Activity created on server: {task_id} (UUID: {res.get('uuid')})")
    else:
        acts = list_remote_activities(client, project_name)
        if getattr(args, "json", False):
            print(json.dumps({"project": project_name, "activities": acts}, indent=2))
        else:
            print(f"Remote Activities in Project '{project_name}' ({len(acts)}):")
            fmt = "  {:<20} {:<10} {:<12} {:<36} {}"
            print(fmt.format("Task ID", "Status", "Owner", "UUID", "Description"))
            print("  " + "-" * 88)
            for a in acts:
                print(fmt.format(a["task_id"], a["status"], a["owner"], a["uuid"], a["description"]))


def cmd_clean_activity(args):
    """Handles 'clean-activity' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    project_name = args.project or env_info.get("dev_point", "").replace("_dev", "")
    ok = clean_remote_activity(client, project_name, args.task)
    if ok:
        print(f"[SUCCESS] Activity '{args.task}' in project '{project_name}' cleaned on server.")
    else:
        print(f"[ERROR] Failed to clean activity '{args.task}'.", file=sys.stderr)
        sys.exit(1)


def cmd_explorer(args):
    """Handles 'explorer' subcommand."""
    client, _ = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    comps = browse_components(
        client=client,
        package=getattr(args, "package", "") or "",
        comp_type=getattr(args, "type", "") or "",
        name_filter=getattr(args, "filter", "") or "",
    )
    if getattr(args, "json", False):
        print(json.dumps({"components": comps}, indent=2))
    else:
        print(f"Remote Server Components ({len(comps)}):")
        fmt = "  {:<20} {:<12} {:<8} {:<8} {}"
        print(fmt.format("Component", "Type", "Package", "Module", "Description"))
        print("  " + "-" * 80)
        for c in comps:
            print(fmt.format(c["name"], c["type"], c["package"], c["module"], c["description"]))


def cmd_get_component(args):
    """Handles 'get-component' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if getattr(args, "inspect", False):
        summary = inspect_component(client=client, comp_type=args.type, comp_name=args.name)
        if getattr(args, "json", False):
            print(json.dumps(summary, indent=2))
        else:
            print(f"Component Inspection: {summary['name']} ({summary['type'].upper()})")
            print(f"  Package:     {summary['package']}")
            print(f"  Module:      {summary['module']}")
            print(f"  Description: {summary['description']}")
            if summary.get("fields"):
                print(f"  Fields ({len(summary['fields'])}):")
                for f in summary["fields"]:
                    print(f"    - {f['name']:<15} domain={f['domain']} label={f['label']}")
            if summary.get("script"):
                print(f"\n  Embedded Script Preview:\n" + "\n".join("    " + line for line in summary["script"].splitlines()[:20]))
    else:
        act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
        act_dir = Path(act_info["path"])
        is_ro = not getattr(args, "writable", False)
        saved_file = get_component(
            client=client,
            comp_type=args.type,
            comp_name=args.name,
            activity_dir=act_dir,
            read_only=is_ro,
        )
        ro_str = " (Read-Only)" if is_ro else ""
        print(f"[SUCCESS] Downloaded {args.type} '{args.name}'{ro_str} -> {saved_file}")


def cmd_clone_component(args):
    """Handles 'clone-component' subcommand."""
    client, _ = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
    act_dir = Path(act_info["path"])
    reg = not getattr(args, "no_server_register", False)
    cloned_file = clone_component(
        client=client,
        comp_type=args.type,
        source_name=args.source,
        target_name=args.target,
        activity_dir=act_dir,
        register_on_server=reg,
    )
    reg_str = " and registered on server" if reg else ""
    print(f"[SUCCESS] Cloned '{args.source}' -> '{args.target}'{reg_str} -> {cloned_file}")


def cmd_checkout_component(args):
    """Handles 'checkout-component' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if args.activity and (Path(args.activity).is_dir() or "/" in args.activity or "\\" in args.activity):
        act_dir = Path(args.activity).resolve()
    else:
        act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
        act_dir = Path(act_info["path"])

    project_name = getattr(args, "project", None) or env_info.get("dev_point", "").replace("_dev", "")
    if not project_name:
        m = re.search(r"\[([A-Za-z0-9_]+)\]$", act_dir.name)
        if m:
            project_name = m.group(1)

    checked_out = checkout_component(
        client=client,
        comp_type=args.type,
        comp_name=args.name,
        activity_dir=act_dir,
        project_name=project_name or "EXTce01107",
    )
    print(f"[SUCCESS] Checked out {args.type} '{args.name}' into '{checked_out}'")


def cmd_uncheckout_component(args):
    """Handles 'uncheckout-component' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if args.activity and (Path(args.activity).is_dir() or "/" in args.activity or "\\" in args.activity):
        act_dir = Path(args.activity).resolve()
    else:
        act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
        act_dir = Path(act_info["path"])

    project_name = getattr(args, "project", None) or env_info.get("dev_point", "").replace("_dev", "")
    if not project_name:
        m = re.search(r"\[([A-Za-z0-9_]+)\]$", act_dir.name)
        if m:
            project_name = m.group(1)

    uncheckout_component(
        client=client,
        comp_type=args.type,
        comp_name=args.name,
        activity_dir=act_dir,
        project_name=project_name or "EXTce01107",
    )
    print(f"[SUCCESS] Reverted check-out for {args.type} '{args.name}'")


def cmd_checkin_component(args):
    """Handles 'checkin-component' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if args.activity and (Path(args.activity).is_dir() or "/" in args.activity or "\\" in args.activity):
        act_dir = Path(args.activity).resolve()
    else:
        act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
        act_dir = Path(act_info["path"])

    project_name = getattr(args, "project", None) or env_info.get("dev_point", "").replace("_dev", "")
    if not project_name:
        m = re.search(r"\[([A-Za-z0-9_]+)\]$", act_dir.name)
        if m:
            project_name = m.group(1)

    comment = getattr(args, "comment", None) or "Automated check-in for LN UI Cloud testing"
    checkin_component(
        client=client,
        comp_type=args.type,
        comp_name=args.name,
        activity_dir=act_dir,
        project_name=project_name or "EXTce01107",
        comment=comment,
    )
    print(f"[SUCCESS] Checked in {args.type} '{args.name}' (comment: '{comment}')")


def cmd_end_activity(args):
    """Handles 'end-activity' subcommand (hard-blocked by ADR 0007)."""
    end_activity_gate(
        project_name=getattr(args, "project", "") or "EXTce01107",
        task_id=getattr(args, "task", "") or "activity",
    )


def cmd_table(args):
    """Handles 'table' subcommand."""
    print(f"[INFO] Generating table components from '{args.spec}'...")
    files = generate_all_components(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} {len(files)} component files:")
    for f in files:
        print(f"  ({f['type'].upper():<6}) {f['name']:<20} -> {f['path']}")


def cmd_session(args):
    """Handles 'session' subcommand."""
    print(f"[INFO] Generating session components...")
    files = generate_session(
        schema_file=args.spec,
        table_code=args.table,
        session_code=args.code,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} {len(files)} session files:")
    for f in files:
        print(f"  ({f['type'].upper():<7}) {f['name']:<20} -> {f['path']}")


def cmd_domain(args):
    """Handles 'domain' subcommand."""
    print(f"[INFO] Generating domain components from '{args.spec}'...")
    files = generate_domains(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} {len(files)} domain files:")
    for f in files:
        print(f"  ({f['type'].upper():<6}) {f['name']:<20} -> {f['path']}")


def cmd_library(args):
    """Handles 'library' subcommand."""
    print(f"[INFO] Generating library components from spec '{args.spec}'...")
    files = generate_libraries(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} {len(files)} library files:")
    for f in files:
        print(f"  ({f['type'].upper():<7}) {f['name']:<20} -> {f['path']}")


def cmd_menu(args):
    """Handles 'menu' subcommand."""
    print(f"[INFO] Generating menu components from spec '{args.spec}'...")
    files = generate_menus(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} {len(files)} menu files:")
    for f in files:
        print(f"  ({f['type'].upper():<6}) {f['name']:<20} -> {f['path']}")


def cmd_component(args):
    """Generates table, session, and associated components in one pass."""
    cmd_table(args)
    cmd_session(args)


def cmd_message(args):
    """Handles 'message' subcommand."""
    act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
    act_dir = Path(act_info["path"])
    spec = {
        "code": args.code,
        "description": args.desc or args.code,
        "severity": getattr(args, "severity", "3") or "3",
        "text": getattr(args, "text", None) or args.desc or args.code,
    }
    files = generate_messages([spec], act_dir, getattr(args, "project", "EXTce01107") or "EXTce01107", dry_run=args.dry_run)
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} message: {files[0]['path']}")


def cmd_question(args):
    """Handles 'question' subcommand."""
    act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
    act_dir = Path(act_info["path"])
    spec = {
        "code": args.code,
        "description": args.desc or args.code,
        "severity": getattr(args, "severity", "2") or "2",
        "domain": getattr(args, "domain", "tcyesno") or "tcyesno",
        "default_answer": getattr(args, "default_answer", "yes") or "yes",
        "text": getattr(args, "text", None) or args.desc or args.code,
    }
    legacy = getattr(args, "legacy_alias", False)
    files = generate_questions([spec], act_dir, getattr(args, "project", "EXTce01107") or "EXTce01107", legacy_alias=legacy, dry_run=args.dry_run)
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} question: {files[0]['path']}")


def cmd_function(args):
    """Handles 'function' subcommand."""
    act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
    act_dir = Path(act_info["path"])
    script_text = None
    if getattr(args, "script_file", None):
        p = Path(args.script_file).resolve()
        if p.exists():
            script_text = p.read_text(encoding="utf-8")
    spec = {
        "code": args.code,
        "description": args.desc or args.code,
    }
    if script_text:
        spec["script"] = script_text
    legacy = getattr(args, "legacy_alias", False)
    files = generate_functions([spec], act_dir, getattr(args, "project", "EXTce01107") or "EXTce01107", legacy_alias=legacy, dry_run=args.dry_run)
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} function: {files[0]['path']}")


def cmd_additional(args):
    """Handles 'additional' subcommand."""
    act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
    act_dir = Path(act_info["path"])
    content = ""
    if getattr(args, "content_file", None):
        p = Path(args.content_file).resolve()
        if p.exists():
            content = p.read_text(encoding="utf-8")
    spec = {
        "code": args.code,
        "description": args.desc or args.code,
        "content": content,
        "keyword1": getattr(args, "keyword1", "") or "",
        "keyword2": getattr(args, "keyword2", "") or "",
        "keyword3": getattr(args, "keyword3", "") or "",
    }
    files = generate_additionals([spec], act_dir, getattr(args, "project", "EXTce01107") or "EXTce01107", dry_run=args.dry_run)
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} additional file: {files[0]['path']}")


def cmd_report(args):
    """Handles 'report' subcommand."""
    act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
    act_dir = Path(act_info["path"])
    script_text = ""
    if getattr(args, "script_file", None):
        p = Path(args.script_file).resolve()
        if p.exists():
            script_text = p.read_text(encoding="utf-8")
    spec = {
        "code": args.code,
        "description": args.desc or args.code,
        "paper_width": getattr(args, "paper_width", 80) or 80,
        "script": script_text,
    }
    files = generate_reports([spec], act_dir, getattr(args, "project", "EXTce01107") or "EXTce01107", dry_run=args.dry_run)
    status_str = "[DRY-RUN] Planned" if args.dry_run else "[SUCCESS] Created"
    print(f"{status_str} report: {files[0]['path']}")


def cmd_mcp_setup(args):
    """Handles 'mcp-setup' subcommand."""
    client = getattr(args, "client", "generic") or "generic"
    cfg_path = Path(args.config_file).resolve() if getattr(args, "config_file", None) else None
    dry_run = getattr(args, "dry_run", False) or not getattr(args, "apply", False)

    res = register_mcp_config(client=client, config_path=cfg_path, dry_run=dry_run)
    status_str = "[DRY-RUN] Planned" if dry_run else "[SUCCESS] Applied"
    print(f"{status_str} MCP registration for '{client}':")
    print(f"  Target File: {res['config_path']}")
    print(f"  Configuration:\n{json.dumps(res['config'], indent=2)}")


def cmd_inject(args):
    """Injects 4GL code into workspace XML."""
    inject_file(Path(args.source), Path(args.target))
    print(f"[SUCCESS] Injected '{args.source}' -> '{args.target}'")


def cmd_extract(args):
    """Extracts 4GL code from workspace XML."""
    extract_file(Path(args.source), Path(args.output))
    print(f"[SUCCESS] Extracted '{args.source}' -> '{args.output}'")


def cmd_sync_admin(args):
    """Synchronizes activity's .admin SCM cache."""
    act_ident = args.activity or load_config().get("default_activity")
    if not act_ident:
        print("[ERROR] No activity specified. Use --activity <name>", file=sys.stderr)
        sys.exit(1)

    resolved = resolve_activity(act_ident)
    if not resolved:
        print(f"[ERROR] Could not resolve activity: '{act_ident}'", file=sys.stderr)
        sys.exit(1)

    act_path = Path(resolved["path"])
    res = scan_and_sync_activity(act_path)
    print(f"[SUCCESS] Synchronized .admin for '{act_path.name}':")
    print(f"  Disk Components: {res['total_disk_components']}")
    print(f"  Added:           {len(res['added'])}")
    print(f"  Removed:         {len(res['removed'])}")


def cmd_check_script(args):
    """Statically verifies 4GL scripts against LN Studio completion and syntax rules."""
    target = Path(args.path)
    if not target.exists():
        print(f"[ERROR] Target path does not exist: {target}", file=sys.stderr)
        sys.exit(1)

    files_to_check: List[Path] = []
    if target.is_dir():
        for ext in ("*.tbl", "*.ses", "*.lib", "*.dal", "*.cln", "*.4gl", "*.bic"):
            files_to_check.extend(target.rglob(ext))
    else:
        files_to_check.append(target)

    owning_xml = Path(args.owning_xml) if args.owning_xml else None
    all_diagnostics = []
    for f in sorted(files_to_check):
        diags = check_4gl_file(f, owning_xml=owning_xml)
        all_diagnostics.extend(diags)

    errors = [d for d in all_diagnostics if d.severity == "ERROR"]
    warnings = [d for d in all_diagnostics if d.severity == "WARNING"]

    if args.json:
        out = {
            "total_files": len(files_to_check),
            "errors_count": len(errors),
            "warnings_count": len(warnings),
            "diagnostics": [
                {
                    "file": d.file_path,
                    "line": d.line,
                    "col": d.col,
                    "severity": d.severity,
                    "message": d.message,
                }
                for d in all_diagnostics
            ]
        }
        print(json.dumps(out, indent=2))
    else:
        print(f"Checked {len(files_to_check)} component(s):")
        for d in all_diagnostics:
            print(f"  {d}")
        print(f"\nSummary: {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (args.strict and warnings):
        sys.exit(1)


def cmd_validate(args):
    """Runs 4-layer validation across activity."""
    act_path = Path(args.path) if args.path else None
    if not act_path:
        act_info = detect_current_activity()
        if act_info and act_info.get("activity_path"):
            act_path = Path(act_info["activity_path"])
        else:
            print("[ERROR] No activity path provided and none detected in workspace.", file=sys.stderr)
            sys.exit(1)

    if not act_path.exists():
        print(f"[ERROR] Activity path does not exist: {act_path}", file=sys.stderr)
        sys.exit(1)

    validator = ActivityValidator(act_path, strict=args.strict, fix=args.fix)
    report = validator.run()

    if args.json:
        out = {
            "activity_path": str(report.target_path),
            "files_scanned": report.files_scanned,
            "errors_count": len(report.errors),
            "warnings_count": len(report.warnings),
            "repaired_items": report.repaired_items,
            "diagnostics": [
                {
                    "file": d.file_path,
                    "line": d.line,
                    "col": d.col,
                    "severity": d.severity,
                    "message": d.message,
                }
                for d in report.diagnostics
            ]
        }
        print(json.dumps(out, indent=2))
    else:
        print(f"Validated Activity: {report.target_path}")
        print(f"Scanned {report.files_scanned} component file(s):")
        for d in report.diagnostics:
            print(f"  {d}")

        if report.repaired_items:
            print("\nSafe Repairs Applied:")
            for rep in report.repaired_items:
                print(f"  [REPAIRED] {rep}")

        print(f"\nSummary: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")

    if report.errors or (args.strict and report.warnings):
        sys.exit(1)


def cmd_diagnose(args):
    """Reads Eclipse problem markers."""
    diag = read_activity_diagnostics(activity_name=args.activity, errors_only=args.errors_only)
    print(f"=== Eclipse Diagnostics: {diag['folder']} ({diag['workspace']}) ===")
    print(f"Errors: {diag['errors_count']} | Warnings: {diag['warnings_count']}")
    print("-" * 65)

    if not diag["markers"]:
        print("[CLEAN] 0 problems recorded in .markers.")
    else:
        for m in diag["markers"]:
            sev = m["severity"]
            sev_label = f"[{sev}]" if sev == "ERROR" else f"({sev})"
            print(f"  {sev_label:<9} {m['file']}:{m['line']}")
            print(f"            {m['message']}")

    sys.exit(1 if diag["errors_count"] > 0 else 0)


def cmd_build(args):
    """Triggers build: defaults to Headless JCA Server Build; keeps Win32 keystrokes as --ui-bridge fallback."""
    if getattr(args, "ui_bridge", False):
        code = trigger_build_and_diagnose(
            activity_name=args.activity,
            settle_seconds=getattr(args, "settle", 3.0),
            errors_only=getattr(args, "errors_only", False)
        )
        sys.exit(code)

    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if args.activity and (Path(args.activity).is_dir() or "/" in args.activity or "\\" in args.activity):
        act_dir = Path(args.activity).resolve()
    else:
        act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
        act_dir = Path(act_info["path"])

    project_name = getattr(args, "project", None) or env_info.get("dev_point", "").replace("_dev", "")
    if not project_name:
        m = re.search(r"\[([A-Za-z0-9_]+)\]$", act_dir.name)
        if m:
            project_name = m.group(1)

    print(f"[INFO] Headless JCA Server Build for activity '{act_dir.name}' (Project: {project_name})...")
    from admin_sync import list_admin_components
    comps = list_admin_components(act_dir)

    all_errors = []
    all_warnings = []
    for c in comps:
        p = Path(c["path"])
        ext = p.suffix.lower()
        comp_type = None
        for t, info in BDE_TYPE_MAP.items():
            if info["ext"] == ext:
                comp_type = t
                break
        if not comp_type:
            continue

        comp_name = p.stem
        put_component(client, comp_type, comp_name, act_dir, project_name or "EXTce01107")
        cres = compile_component(client, comp_type, comp_name, project_name or "EXTce01107")
        all_errors.extend(cres["errors"])
        all_warnings.extend(cres["warnings"])

        if comp_type in ("table", "domain", "session", "menu"):
            convert_to_runtime(client, comp_type, comp_name, project_name or "EXTce01107")
        if comp_type == "table":
            create_tables(client, comp_name, project_name or "EXTce01107")

    print(f"[RESULT] Build completed: {len(all_errors)} errors, {len(all_warnings)} warnings.")
    for err in all_errors:
        print(f"  [ERROR] line {err['line']}, col {err['column']}: {err['message']} ({err['code']})")
    for warn in all_warnings:
        print(f"  (WARN)  line {warn['line']}, col {warn['column']}: {warn['message']} ({warn['code']})")

    sys.exit(1 if len(all_errors) > 0 else 0)


def cmd_deploy_test(args):
    """Handles 'deploy-test' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if args.activity and (Path(args.activity).is_dir() or "/" in args.activity or "\\" in args.activity):
        act_dir = Path(args.activity).resolve()
    else:
        act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
        act_dir = Path(act_info["path"])

    project_name = getattr(args, "project", None) or env_info.get("dev_point", "").replace("_dev", "")
    if not project_name:
        m = re.search(r"\[([A-Za-z0-9_]+)\]$", act_dir.name)
        if m:
            project_name = m.group(1)

    comment = getattr(args, "comment", None) or "Automated deploy-test for LN UI Cloud testing"
    res = deploy_test(
        client=client,
        comp_type=args.type,
        comp_name=args.name,
        activity_dir=act_dir,
        project_name=project_name or "EXTce01107",
        comment=comment,
    )
    if getattr(args, "json", False):
        print(json.dumps(res, indent=2))
    else:
        status_str = "[SUCCESS]" if res["success"] else "[FAILED]"
        print(f"{status_str} deploy-test for {args.type} '{args.name}': {res.get('message')}")
        if res.get("errors"):
            for e in res["errors"]:
                print(f"  [ERROR] Line {e['line']}: {e['message']}")


def cmd_prepare_end_activity(args):
    """Handles 'prepare-end-activity' subcommand."""
    client, env_info = get_server_client(workspace_name=args.workspace, mock=getattr(args, "mock", False))
    if args.activity and (Path(args.activity).is_dir() or "/" in args.activity or "\\" in args.activity):
        act_dir = Path(args.activity).resolve()
    else:
        act_info = resolve_activity(activity_name=args.activity, workspace_name=args.workspace)
        act_dir = Path(act_info["path"])

    project_name = getattr(args, "project", None) or env_info.get("dev_point", "").replace("_dev", "")
    if not project_name:
        m = re.search(r"\[([A-Za-z0-9_]+)\]$", act_dir.name)
        if m:
            project_name = m.group(1)

    res = prepare_end_activity(
        client=client,
        activity_dir=act_dir,
        project_name=project_name or "EXTce01107",
    )
    if getattr(args, "json", False):
        print(json.dumps(res, indent=2))
    else:
        print(res["commit_summary"])
        print(f"\n[NEXT STEP] {res['human_action_required']}")


def cmd_pipeline(args):
    """
    Executes full autonomous pipeline:
    1. Parse schema and generate all declared components (tables, domains, sessions, libraries, menus)
    2. Synchronize .admin SCM cache
    3. Run 4-layer validation
    4. Optional build trigger & diagnostics
    """
    print("=================================================================")
    print("        INFOR LN STUDIO AUTOMATION PIPELINE                     ")
    print("=================================================================")

    # Step 1: Generate Components
    print("\n[STEP 1/4] Generating declared components (Tables, Domains, Sessions, Libraries, Menus)...")
    tbl_files = generate_all_components(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    ses_files = generate_session(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    lib_files = generate_libraries(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    mnu_files = generate_menus(
        schema_file=args.spec,
        activity_name=args.activity,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    total_files = len(tbl_files) + len(ses_files) + len(lib_files) + len(mnu_files)
    print(f"[OK] Generated {total_files} component files.")

    if args.dry_run:
        print("\n[DRY-RUN] Pipeline completed in preview mode.")
        return

    # Step 2: Sync Admin
    print("\n[STEP 2/4] Synchronizing Eclipse Activity SCM (.admin)...")
    act_ident = args.activity or load_config().get("default_activity")
    act_path = None
    if act_ident:
        resolved = resolve_activity(act_ident)
        if resolved:
            act_path = Path(resolved["path"])
            res = scan_and_sync_activity(act_path)
            print(f"[OK] Synchronized .admin (Added: {len(res['added'])}, Total: {res['total_registered']})")
        else:
            print(f"[WARN] Could not resolve activity '{act_ident}', skipped .admin sync.")
    elif args.output_dir:
        act_path = Path(args.output_dir)
        try:
            res = scan_and_sync_activity(act_path)
            print(f"[OK] Synchronized .admin (Added: {len(res['added'])}, Total: {res['total_registered']})")
        except Exception as e:
            print(f"[INFO] .admin sync skipped: {e}")

    # Step 3: Validate
    if act_path and act_path.exists():
        print("\n[STEP 3/4] Running 4-Layer Activity Validation...")
        validator = ActivityValidator(act_path, strict=False, fix=args.auto_fix)
        report = validator.run()
        print(f"Scanned {report.files_scanned} files -> {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
        if report.errors:
            print("[WARN] Validation detected errors in generated activity:")
            for e in report.errors[:5]:
                print(f"  {e}")
            if not args.skip_build:
                print("[ERROR] Aborting build due to validation errors.")
                sys.exit(1)
    else:
        print("\n[STEP 3/4] Validation skipped (no activity directory target).")

    # Step 4: Build & Diagnose
    if not args.skip_build:
        print("\n[STEP 4/4] Triggering Eclipse Build Bridge...")
        code = trigger_build_and_diagnose(
            activity_name=args.activity,
            settle_seconds=args.settle,
            errors_only=args.errors_only
        )
        print("\nPipeline Complete!")
        sys.exit(code)
    else:
        print("\n[STEP 4/4] Skipped build (--skip-build).")
        print("\nPipeline Complete!")


def cmd_new_extension(args):
    """Handles 'new-extension' subcommand."""
    print(f"[INFO] Scaffolding {args.type} extension for '{args.target}'...")
    try:
        out_p = new_extension(
            ext_type=args.type,
            target=args.target,
            output_path=args.output,
            author=args.author if hasattr(args, "author") and args.author else "Developer"
        )
        print(f"[SUCCESS] Created extension file: {out_p}")
        print(f"Target Session: Infor LN UI -> ttext1500m000 (Extension Modeler)")
        print(f"Note: Author and verify locally. Do NOT check out in LN Studio.")
    except Exception as e:
        print(f"[ERROR] Failed to scaffold extension: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_import_extension(args):
    """Handles 'import-extension' subcommand."""
    print(f"[INFO] Importing extension from '{args.source}'...")
    try:
        out_p = import_extension(
            source=args.source,
            output_path=args.output,
            ext_type=args.type if hasattr(args, "type") else None
        )
        print(f"[SUCCESS] Imported and normalized extension: {out_p}")
        print(f"Ready for offline verification with 'check-script'.")
    except Exception as e:
        print(f"[ERROR] Import failed: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_extension_hooks(args):
    """Handles 'extension-hooks' subcommand."""
    file_p = Path(args.path).resolve()
    if not file_p.exists():
        print(f"[ERROR] Extension file not found: {file_p}", file=sys.stderr)
        sys.exit(1)

    if args.hook:
        hook_block = get_hook(file_p, args.hook)
        if not hook_block:
            print(f"[ERROR] Hook '{args.hook}' not found in {file_p.name}", file=sys.stderr)
            avail = [h["name"] for h in list_hooks(file_p)]
            if avail:
                print(f"Available hooks: {', '.join(avail)}")
            sys.exit(1)

        clean_code = hook_block.clean_code
        if args.copy:
            copied = copy_to_clipboard(clean_code)
            if copied:
                print(f"[SUCCESS] Copied hook '{hook_block.name}' ({hook_block.code_lines_count} lines) to system clipboard!")
                print(f"Target: Infor LN UI -> Session ttext1500m000 -> Hook '{hook_block.name}'")
            else:
                print(f"[WARNING] Could not copy to clipboard automatically. Outputting code below:")
                print(clean_code)
        else:
            print(f"--- Hook: {hook_block.name} ({file_p.name}, lines {hook_block.start_line}-{hook_block.end_line}) ---")
            print(clean_code)
    else:
        # Default / --list behavior
        hooks = list_hooks(file_p)
        print(f"Extension Hooks in {file_p.name} ({len(hooks)} hook(s)):")
        for idx, h in enumerate(hooks, start=1):
            print(f"  {idx:2d}. {h['name']:<35} (Lines {h['start_line']:3d} - {h['end_line']:3d}, {h['code_lines']} code lines)")
        print("\nUse --hook <name> to view clean code, or --hook <name> --copy to copy to clipboard for LN UI.")


def main():
    parser = argparse.ArgumentParser(
        description="Infor LN Studio Automation Toolset & Assistant CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # workspace
    sp_ws = subparsers.add_parser("workspace", help="Inspect workspaces and activities")
    sp_ws.add_argument("--list", action="store_true", help="List all workspaces")
    sp_ws.add_argument("--activities", action="store_true", help="List activities")
    sp_ws.add_argument("--workspace", help="Filter by workspace name")
    sp_ws.add_argument("--set-default", help="Set default activity")

    # table
    sp_tbl = subparsers.add_parser("table", help="Generate table, labels, and domains from schema")
    sp_tbl.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    sp_tbl.add_argument("--activity", help="Target activity name")
    sp_tbl.add_argument("--output-dir", help="Target directory (overrides activity)")
    sp_tbl.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # session
    sp_ses = subparsers.add_parser("session", help="Generate session and dynamic form from schema or table")
    sp_ses.add_argument("--spec", help="Path to schema YAML/JSON file")
    sp_ses.add_argument("--table", help="Table code")
    sp_ses.add_argument("--code", help="Session code override")
    sp_ses.add_argument("--activity", help="Target activity name")
    sp_ses.add_argument("--output-dir", help="Target directory (overrides activity)")
    sp_ses.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # domain
    sp_dmn = subparsers.add_parser("domain", help="Generate domain components from schema")
    sp_dmn.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    sp_dmn.add_argument("--activity", help="Target activity name")
    sp_dmn.add_argument("--output-dir", help="Target directory")
    sp_dmn.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # library
    sp_lib = subparsers.add_parser("library", help="Generate library (DLL, session/table extension)")
    sp_lib.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    sp_lib.add_argument("--activity", help="Target activity name")
    sp_lib.add_argument("--output-dir", help="Target directory")
    sp_lib.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # menu
    sp_mnu = subparsers.add_parser("menu", help="Generate menu components")
    sp_mnu.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    sp_mnu.add_argument("--activity", help="Target activity name")
    sp_mnu.add_argument("--output-dir", help="Target directory")
    sp_mnu.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # component
    sp_comp = subparsers.add_parser("component", help="Generate both table and session from schema")
    sp_comp.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    sp_comp.add_argument("--table", help="Table code")
    sp_comp.add_argument("--code", help="Session code override")
    sp_comp.add_argument("--activity", help="Target activity name")
    sp_comp.add_argument("--output-dir", help="Target directory")
    sp_comp.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # inject
    sp_inj = subparsers.add_parser("inject", help="Inject 4GL script into workspace XML")
    sp_inj.add_argument("--source", required=True, help="Path to .dal / .cln source script")
    sp_inj.add_argument("--target", required=True, help="Path to target .tbl / .ses XML file")

    # extract
    sp_ext = subparsers.add_parser("extract", help="Extract 4GL script from workspace XML")
    sp_ext.add_argument("--source", required=True, help="Path to source .tbl / .ses XML file")
    sp_ext.add_argument("--output", required=True, help="Path to output .dal / .cln script file")

    # check-script
    sp_chk = subparsers.add_parser("check-script", help="Statically verify 4GL script syntax and structure")
    sp_chk.add_argument("path", help="Path to 4GL script or XML component file/directory")
    sp_chk.add_argument("--owning-xml", help="Owning XML component file for symbol verification")
    sp_chk.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    sp_chk.add_argument("--json", action="store_true", help="Output results in JSON format")

    # validate
    sp_val = subparsers.add_parser("validate", help="Run 4-layer validation across activity")
    sp_val.add_argument("path", nargs="?", help="Path to activity folder")
    sp_val.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    sp_val.add_argument("--fix", action="store_true", help="Perform safe non-destructive repairs (missing labels, admin sync)")
    sp_val.add_argument("--json", action="store_true", help="Output results in JSON format")

    # sync-admin
    sp_adm = subparsers.add_parser("sync-admin", help="Synchronize activity .admin SCM cache")
    sp_adm.add_argument("--activity", help="Target activity name")

    # diagnose
    sp_diag = subparsers.add_parser("diagnose", help="Read Eclipse problem markers (.markers)")
    sp_diag.add_argument("--activity", help="Activity name")
    sp_diag.add_argument("--errors-only", action="store_true", help="Only report errors")

    # build
    sp_bld = subparsers.add_parser("build", help="Execute Headless JCA Server Build (or Win32 Ctrl+B with --ui-bridge)")
    sp_bld.add_argument("--activity", help="Activity name or folder path")
    sp_bld.add_argument("--project", help="Software Project name")
    sp_bld.add_argument("--workspace", help="Target workspace folder name")
    sp_bld.add_argument("--ui-bridge", action="store_true", help="Fallback to Win32 F5 + Ctrl+B keystrokes")
    sp_bld.add_argument("--settle", type=float, default=3.0, help="Settle wait in seconds (for --ui-bridge)")
    sp_bld.add_argument("--errors-only", action="store_true", help="Only report errors")
    sp_bld.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # pipeline
    sp_pip = subparsers.add_parser("pipeline", help="Run full pipeline: Schema -> XML -> Admin Sync -> Validate -> Build")
    sp_pip.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    sp_pip.add_argument("--activity", help="Target activity name")
    sp_pip.add_argument("--output-dir", help="Target output directory")
    sp_pip.add_argument("--auto-fix", action="store_true", help="Auto-fix missing labels and admin sync during validation")
    sp_pip.add_argument("--skip-build", action="store_true", help="Skip Eclipse build trigger")
    sp_pip.add_argument("--settle", type=float, default=3.0, help="Build settle wait in seconds")
    sp_pip.add_argument("--errors-only", action="store_true", help="Only report errors")
    sp_pip.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # new-extension
    sp_next = subparsers.add_parser("new-extension", help="Scaffold a local project extension 4GL file")
    sp_next.add_argument("--type", required=True, choices=["table", "session"], help="Extension type: 'table' or 'session'")
    sp_next.add_argument("--target", required=True, help="Target component code (e.g. whwmd400)")
    sp_next.add_argument("--output", help="Output path (default: extensions/<type>/<target>_ext.4gl)")
    sp_next.add_argument("--author", default="Developer", help="Author metadata")

    # import-extension
    sp_impext = subparsers.add_parser("import-extension", help="Import an extension from Studio activity 'Get' cache into local project")
    sp_impext.add_argument("--source", required=True, help="Path to .lib or .4gl extension in Studio workspace")
    sp_impext.add_argument("--output", help="Output path in local project")
    sp_impext.add_argument("--type", choices=["table", "session"], help="Override extension type")

    # extension-hooks
    sp_exthooks = subparsers.add_parser("extension-hooks", help="Inspect and extract hooks from local extension 4GL file")
    sp_exthooks.add_argument("path", help="Path to extension .4gl file")
    sp_exthooks.add_argument("--list", action="store_true", help="List all hook blocks")
    sp_exthooks.add_argument("--hook", help="Extract specific hook block stripped of wrappers")
    sp_exthooks.add_argument("--copy", action="store_true", help="Copy clean hook code directly to system clipboard for LN UI")

    # environments
    sp_envs = subparsers.add_parser("environments", help="List configured customer workspaces and cloud environments")
    sp_envs.add_argument("--workspace-root", help="Custom workspace discovery root directory")
    sp_envs.add_argument("--json", action="store_true", help="Output results in JSON format")

    # connect
    sp_conn = subparsers.add_parser("connect", help="Import .ionapi credentials and synchronize Eclipse preferences")
    sp_conn.add_argument("--ionapi", required=True, help="Path to .ionapi credentials file")
    sp_conn.add_argument("--env-name", help="Custom CloudEnvironment name (defaults to .ionapi filename)")
    sp_conn.add_argument("--workspace", help="Target workspace folder name under workspace root")
    sp_conn.add_argument("--project", help="Software project name for shared dev/rt connection points (e.g. EXTce01107)")
    sp_conn.add_argument("--ping", action="store_true", help="Execute live JCA ping to verify server connectivity")

    # project
    sp_proj = subparsers.add_parser("project", help="Browse remote Applications and Software Projects")
    sp_proj.add_argument("--project", help="Inspect specific Software Project (e.g. EXTce01107)")
    sp_proj.add_argument("--workspace", help="Target workspace folder name")
    sp_proj.add_argument("--json", action="store_true", help="Output results in JSON format")
    sp_proj.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # activity
    sp_act = subparsers.add_parser("activity", help="Browse, create, or bootstrap Activities under a Software Project")
    sp_act.add_argument("--project", help="Software Project name (e.g. EXTce01107)")
    sp_act.add_argument("--workspace", help="Target workspace folder name")
    sp_act.add_argument("--create", help="Create new activity with specified Task ID")
    sp_act.add_argument("--desc", help="Description for new activity")
    sp_act.add_argument("--bootstrap", action="store_true", help="Bootstrap local activity folder with .project/.admin/properties.index")
    sp_act.add_argument("--json", action="store_true", help="Output results in JSON format")
    sp_act.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # clean-activity
    sp_clnact = subparsers.add_parser("clean-activity", help="Clean/recover stuck activity workarea locks on server")
    sp_clnact.add_argument("--task", required=True, help="Task ID of activity to clean")
    sp_clnact.add_argument("--project", help="Software Project name")
    sp_clnact.add_argument("--workspace", help="Target workspace folder name")
    sp_clnact.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # explorer
    sp_expl = subparsers.add_parser("explorer", help="Browse server components across all 12 types")
    sp_expl.add_argument("--package", help="Filter by package (e.g. tc, td, wh, tx)")
    sp_expl.add_argument("--type", help="Filter by component type (table, session, library, report, etc.)")
    sp_expl.add_argument("--filter", help="Name wildcard or prefix filter")
    sp_expl.add_argument("--workspace", help="Target workspace folder name")
    sp_expl.add_argument("--json", action="store_true", help="Output results in JSON format")
    sp_expl.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # get-component
    sp_get = subparsers.add_parser("get-component", help="Fetch component from server (inspect in-memory or download Read-Only)")
    sp_get.add_argument("--type", required=True, help="Component type (table, session, library, report, etc.)")
    sp_get.add_argument("--name", required=True, help="Component name (e.g. tcibd001, whwmd4300m000)")
    sp_get.add_argument("--inspect", action="store_true", help="Inspect in-memory without creating local files")
    sp_get.add_argument("--activity", help="Target activity name (defaults to active activity)")
    sp_get.add_argument("--workspace", help="Target workspace folder name")
    sp_get.add_argument("--writable", action="store_true", help="Clear OS Read-Only attribute on downloaded file")
    sp_get.add_argument("--json", action="store_true", help="Output inspection results in JSON format")
    sp_get.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # clone-component
    sp_clone = subparsers.add_parser("clone-component", help="Clone standard or custom component into renamed custom activity component")
    sp_clone.add_argument("--type", required=True, help="Component type (table, session, library, report, etc.)")
    sp_clone.add_argument("--source", required=True, help="Source component code (e.g. tcibd001)")
    sp_clone.add_argument("--target", required=True, help="Target component code (e.g. txibd001)")
    sp_clone.add_argument("--activity", help="Target activity name")
    sp_clone.add_argument("--workspace", help="Target workspace folder name")
    sp_clone.add_argument("--no-server-register", action="store_true", help="Skip DR_Create registration on server")
    sp_clone.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # checkout-component
    sp_chkout = subparsers.add_parser("checkout-component", help="Lock component into activity on server and download editable XML")
    sp_chkout.add_argument("--type", required=True, help="Component type (table, session, library, report, etc.)")
    sp_chkout.add_argument("--name", required=True, help="Component name (e.g. tdsls400)")
    sp_chkout.add_argument("--activity", help="Target activity name or directory path")
    sp_chkout.add_argument("--project", help="Software Project name (e.g. EXTce01107)")
    sp_chkout.add_argument("--workspace", help="Target workspace folder name")
    sp_chkout.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # uncheckout-component
    sp_unchk = subparsers.add_parser("uncheckout-component", help="Revert component lock on server and restore local Read-Only")
    sp_unchk.add_argument("--type", required=True, help="Component type (table, session, library, report, etc.)")
    sp_unchk.add_argument("--name", required=True, help="Component name (e.g. tdsls400)")
    sp_unchk.add_argument("--activity", help="Target activity name or directory path")
    sp_unchk.add_argument("--project", help="Software Project name")
    sp_unchk.add_argument("--workspace", help="Target workspace folder name")
    sp_unchk.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # checkin-component
    sp_chkin = subparsers.add_parser("checkin-component", help="Upload and check in component with comment for LN UI testing")
    sp_chkin.add_argument("--type", required=True, help="Component type (table, session, library, report, etc.)")
    sp_chkin.add_argument("--name", required=True, help="Component name (e.g. tdsls400)")
    sp_chkin.add_argument("--comment", default="Automated check-in for LN UI Cloud testing", help="Check-in comment")
    sp_chkin.add_argument("--activity", help="Target activity name or directory path")
    sp_chkin.add_argument("--project", help="Software Project name")
    sp_chkin.add_argument("--workspace", help="Target workspace folder name")
    sp_chkin.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # end-activity (hard-blocked)
    sp_endact = subparsers.add_parser("end-activity", help="Hard-blocked: Human review gate before activity delivery")
    sp_endact.add_argument("--task", help="Task ID of activity")
    sp_endact.add_argument("--project", help="Software Project name")

    # deploy-test
    sp_deptest = subparsers.add_parser("deploy-test", help="Composite test deployment: Put -> Compile -> CRDD -> Tables -> VSC -> CheckIn")
    sp_deptest.add_argument("--type", required=True, help="Component type (table, session, library, report, etc.)")
    sp_deptest.add_argument("--name", required=True, help="Component name (e.g. txibd001)")
    sp_deptest.add_argument("--activity", help="Target activity name or directory path")
    sp_deptest.add_argument("--project", help="Software Project name")
    sp_deptest.add_argument("--workspace", help="Target workspace folder name")
    sp_deptest.add_argument("--comment", default="Automated deploy-test for LN UI Cloud testing", help="Check-in comment")
    sp_deptest.add_argument("--json", action="store_true", help="Output results in JSON format")
    sp_deptest.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # prepare-end-activity
    sp_prepend = subparsers.add_parser("prepare-end-activity", help="Pre-commit readiness verifier and human commit handoff")
    sp_prepend.add_argument("--activity", help="Target activity name or directory path")
    sp_prepend.add_argument("--project", help="Software Project name")
    sp_prepend.add_argument("--workspace", help="Target workspace folder name")
    sp_prepend.add_argument("--json", action="store_true", help="Output results in JSON format")
    sp_prepend.add_argument("--mock", action="store_true", help="Run with mock transport for testing")

    # message
    sp_msg = subparsers.add_parser("message", help="Generate Infor LN Message (.msg) component")
    sp_msg.add_argument("--code", required=True, help="Message code (e.g. txcmg0001)")
    sp_msg.add_argument("--desc", help="Description")
    sp_msg.add_argument("--severity", choices=["1", "2", "3"], default="3", help="1=Info, 2=Warning, 3=Error")
    sp_msg.add_argument("--text", help="Message text")
    sp_msg.add_argument("--activity", help="Target activity folder")
    sp_msg.add_argument("--workspace", help="Target workspace folder name")
    sp_msg.add_argument("--project", default="EXTce01107", help="Software Project name")
    sp_msg.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # question
    sp_qst = subparsers.add_parser("question", help="Generate Infor LN Question (.qst) component")
    sp_qst.add_argument("--code", required=True, help="Question code (e.g. txcmg0002)")
    sp_qst.add_argument("--desc", help="Description")
    sp_qst.add_argument("--severity", choices=["1", "2", "3"], default="2", help="1=Info, 2=Warning, 3=Error")
    sp_qst.add_argument("--domain", default="tcyesno", help="Answer domain")
    sp_qst.add_argument("--default-answer", default="yes", help="Default answer (yes/no)")
    sp_qst.add_argument("--text", help="Question text")
    sp_qst.add_argument("--legacy-alias", action="store_true", help="Generate with .que extension instead of .qst")
    sp_qst.add_argument("--activity", help="Target activity folder")
    sp_qst.add_argument("--workspace", help="Target workspace folder name")
    sp_qst.add_argument("--project", default="EXTce01107", help="Software Project name")
    sp_qst.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # function
    sp_fnc = subparsers.add_parser("function", help="Generate Infor LN Include Function (.fnc) component")
    sp_fnc.add_argument("--code", required=True, help="Function code (e.g. txcmgf001)")
    sp_fnc.add_argument("--desc", help="Description")
    sp_fnc.add_argument("--script-file", help="Path to plain .4gl/.src file containing function source")
    sp_fnc.add_argument("--legacy-alias", action="store_true", help="Generate with .fun extension instead of .fnc")
    sp_fnc.add_argument("--activity", help="Target activity folder")
    sp_fnc.add_argument("--workspace", help="Target workspace folder name")
    sp_fnc.add_argument("--project", default="EXTce01107", help="Software Project name")
    sp_fnc.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # additional
    sp_add = subparsers.add_parser("additional", help="Generate Infor LN Additional File (.add) component")
    sp_add.add_argument("--code", required=True, help="Additional file code (e.g. txcmgcfg)")
    sp_add.add_argument("--desc", help="Description")
    sp_add.add_argument("--content-file", help="Path to payload file (JSON, XML, text, etc.)")
    sp_add.add_argument("--keyword1", help="Keyword 1")
    sp_add.add_argument("--keyword2", help="Keyword 2")
    sp_add.add_argument("--keyword3", help="Keyword 3")
    sp_add.add_argument("--activity", help="Target activity folder")
    sp_add.add_argument("--workspace", help="Target workspace folder name")
    sp_add.add_argument("--project", default="EXTce01107", help="Software Project name")
    sp_add.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # report
    sp_rpt = subparsers.add_parser("report", help="Generate Infor LN Report (.rpt) component")
    sp_rpt.add_argument("--code", required=True, help="Report code (e.g. txcmg04010100)")
    sp_rpt.add_argument("--desc", help="Description")
    sp_rpt.add_argument("--paper-width", type=int, choices=[80, 132], default=80, help="Paper width (80 or 132)")
    sp_rpt.add_argument("--script-file", help="Path to 4GL report script file")
    sp_rpt.add_argument("--activity", help="Target activity folder")
    sp_rpt.add_argument("--workspace", help="Target workspace folder name")
    sp_rpt.add_argument("--project", default="EXTce01107", help="Software Project name")
    sp_rpt.add_argument("--dry-run", action="store_true", help="Preview without writing")

    # mcp-setup
    sp_mcpset = subparsers.add_parser("mcp-setup", help="Register Stdio MCP Server (ln_studio_mcp.py) in AI agent configuration")
    sp_mcpset.add_argument("--client", choices=["claude", "cursor", "antigravity", "generic"], default="generic", help="Target AI coding agent client")
    sp_mcpset.add_argument("--config-file", help="Explicit path to MCP configuration file")
    sp_mcpset.add_argument("--apply", action="store_true", help="Write configuration changes to target file")
    sp_mcpset.add_argument("--dry-run", action="store_true", help="Preview configuration without writing")

    args = parser.parse_args()

    commands = {
        "workspace": cmd_workspace,
        "environments": cmd_environments,
        "connect": cmd_connect,
        "project": cmd_project,
        "activity": cmd_activity,
        "clean-activity": cmd_clean_activity,
        "explorer": cmd_explorer,
        "get-component": cmd_get_component,
        "clone-component": cmd_clone_component,
        "checkout-component": cmd_checkout_component,
        "uncheckout-component": cmd_uncheckout_component,
        "checkin-component": cmd_checkin_component,
        "end-activity": cmd_end_activity,
        "deploy-test": cmd_deploy_test,
        "prepare-end-activity": cmd_prepare_end_activity,
        "table": cmd_table,
        "session": cmd_session,
        "domain": cmd_domain,
        "library": cmd_library,
        "menu": cmd_menu,
        "component": cmd_component,
        "message": cmd_message,
        "question": cmd_question,
        "function": cmd_function,
        "additional": cmd_additional,
        "report": cmd_report,

        "inject": cmd_inject,
        "extract": cmd_extract,
        "check-script": cmd_check_script,
        "validate": cmd_validate,
        "sync-admin": cmd_sync_admin,
        "diagnose": cmd_diagnose,
        "build": cmd_build,
        "pipeline": cmd_pipeline,
        "new-extension": cmd_new_extension,
        "import-extension": cmd_import_extension,
        "extension-hooks": cmd_extension_hooks,
        "mcp-setup": cmd_mcp_setup,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
