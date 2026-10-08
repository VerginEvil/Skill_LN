#!/usr/bin/env python3
"""
tools/ln_component_builder.py
Unified Component Builder & Pipeline Orchestrator for Infor LN Studio.

Master CLI entrypoint that unifies:
  - Declarative schema validation (ln_schema_parser)
  - Table, domain, and label generation (generate_ln_table)
  - Session and dynamic form generation (generate_ln_session)
  - Bidirectional 4GL source synchronization (inject_ln_script)
  - Eclipse SCM cache synchronization (admin_sync)
  - Windows action bridge & build triggering (ln_studio_bridge)
  - Eclipse Problem Marker diagnostics (ln_error_reader)
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional, List, Dict, Any

_current_dir = Path(__file__).resolve().parent
_repo_root = _current_dir.parent
for p in (str(_repo_root), str(_current_dir)):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from tools.ln_workspace_manager import (
        list_workspaces, list_activities, resolve_activity, load_config, save_config, get_workspace_root
    )
    from tools.ln_schema_parser import parse_schema_file, SchemaValidationError
    from tools.generate_ln_table import generate_all_components
    from tools.generate_ln_session import generate_session
    from tools.inject_ln_script import inject_file, extract_file, sync_all_activity_scripts
    from tools.admin_sync import scan_and_sync_activity, list_admin_components
    from tools.ln_error_reader import read_activity_diagnostics
    from tools.ln_studio_bridge import trigger_build_and_diagnose
except ImportError:
    from ln_workspace_manager import (
        list_workspaces, list_activities, resolve_activity, load_config, save_config, get_workspace_root
    )
    from ln_schema_parser import parse_schema_file, SchemaValidationError
    from generate_ln_table import generate_all_components
    from generate_ln_session import generate_session
    from inject_ln_script import inject_file, extract_file, sync_all_activity_scripts
    from admin_sync import scan_and_sync_activity, list_admin_components
    from ln_error_reader import read_activity_diagnostics
    from ln_studio_bridge import trigger_build_and_diagnose


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


def cmd_component(args):
    """Generates both table and session in one pass."""
    cmd_table(args)
    cmd_session(args)


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
    """Triggers Eclipse refresh + build and reports diagnostics."""
    code = trigger_build_and_diagnose(
        activity_name=args.activity,
        settle_seconds=args.settle,
        errors_only=args.errors_only
    )
    sys.exit(code)


def cmd_pipeline(args):
    """
    Executes full autonomous pipeline:
    1. Validate schema
    2. Generate table & session XML
    3. Sync .admin
    4. Optional build trigger & diagnostics
    """
    print("=================================================================")
    print("        INFOR LN STUDIO AUTOMATION PIPELINE                     ")
    print("=================================================================")

    # Step 1 & 2: Generate Components
    print("\n[STEP 1/4] Generating Table, Domain, Label, and Session XML...")
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
    print(f"[OK] Generated {len(tbl_files) + len(ses_files)} component files.")

    if args.dry_run:
        print("\n[DRY-RUN] Pipeline completed in preview mode.")
        return

    # Step 3: Sync Admin
    print("\n[STEP 2/4] Synchronizing Eclipse Activity SCM (.admin)...")
    act_ident = args.activity or load_config().get("default_activity")
    if act_ident:
        resolved = resolve_activity(act_ident)
        if resolved:
            act_path = Path(resolved["path"])
            res = scan_and_sync_activity(act_path)
            print(f"[OK] Synchronized .admin (Added: {len(res['added'])}, Total: {res['total_registered']})")
        else:
            print(f"[WARN] Could not resolve activity '{act_ident}', skipped .admin sync.")
    else:
        print("[INFO] No activity target specified, skipped .admin sync.")

    # Step 4: Build & Diagnose
    if not args.skip_build:
        print("\n[STEP 3/4] Triggering Eclipse Build Bridge...")
        code = trigger_build_and_diagnose(
            activity_name=args.activity,
            settle_seconds=args.settle,
            errors_only=args.errors_only
        )
        print("\n[STEP 4/4] Pipeline Complete!")
        sys.exit(code)
    else:
        print("\n[STEP 3/4] Skipped build (--skip-build).")
        print("\n[STEP 4/4] Pipeline Complete!")


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

    # sync-admin
    sp_adm = subparsers.add_parser("sync-admin", help="Synchronize activity .admin SCM cache")
    sp_adm.add_argument("--activity", help="Target activity name")

    # diagnose
    sp_diag = subparsers.add_parser("diagnose", help="Read Eclipse problem markers (.markers)")
    sp_diag.add_argument("--activity", help="Activity name")
    sp_diag.add_argument("--errors-only", action="store_true", help="Only report errors")

    # build
    sp_bld = subparsers.add_parser("build", help="Trigger Eclipse F5 + Ctrl+B and check diagnostics")
    sp_bld.add_argument("--activity", help="Activity name")
    sp_bld.add_argument("--settle", type=float, default=3.0, help="Settle wait in seconds")
    sp_bld.add_argument("--errors-only", action="store_true", help="Only report errors")

    # pipeline
    sp_pip = subparsers.add_parser("pipeline", help="Run full pipeline: Schema -> XML -> Admin Sync -> Build")
    sp_pip.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    sp_pip.add_argument("--activity", help="Target activity name")
    sp_pip.add_argument("--output-dir", help="Target output directory")
    sp_pip.add_argument("--skip-build", action="store_true", help="Skip Eclipse build trigger")
    sp_pip.add_argument("--settle", type=float, default=3.0, help="Build settle wait in seconds")
    sp_pip.add_argument("--errors-only", action="store_true", help="Only report errors")
    sp_pip.add_argument("--dry-run", action="store_true", help="Preview without writing")

    args = parser.parse_args()

    commands = {
        "workspace": cmd_workspace,
        "table": cmd_table,
        "session": cmd_session,
        "component": cmd_component,
        "inject": cmd_inject,
        "extract": cmd_extract,
        "sync-admin": cmd_sync_admin,
        "diagnose": cmd_diagnose,
        "build": cmd_build,
        "pipeline": cmd_pipeline,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
