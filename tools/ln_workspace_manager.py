#!/usr/bin/env python3
"""
tools/ln_workspace_manager.py
Infor LN Studio Workspace Discovery & Activity Environment Manager.

Scans Eclipse workspaces under workspace_lnstudio, lists activities matching
'<activity> [<project>]', resolves filesystem paths, and manages default settings.
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple

DEFAULT_WORKSPACE_ROOT = r"C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio"
CONFIG_FILE_NAME = ".ln_studio_config.json"
ACTIVITY_PATTERN = re.compile(r"^(.+?)\s+\[([A-Za-z0-9_]+)\]$")


def get_repo_root() -> Path:
    """Returns the root directory of the Skill_LN repository."""
    return Path(__file__).resolve().parent.parent


def get_config_path() -> Path:
    """Returns the path to the workspace configuration JSON."""
    return get_repo_root() / CONFIG_FILE_NAME


def load_config() -> Dict[str, str]:
    """Loads default configuration or returns empty defaults."""
    cfg_path = get_config_path()
    if cfg_path.exists():
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_config(cfg: Dict[str, str]) -> None:
    """Saves configuration to .ln_studio_config.json."""
    cfg_path = get_config_path()
    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


def get_workspace_root(override_root: Optional[str] = None) -> Path:
    """Resolves workspace root from argument, env variable, config, or default."""
    if override_root:
        return Path(override_root).resolve()
    env_root = os.environ.get("LN_WORKSPACE_ROOT")
    if env_root:
        return Path(env_root).resolve()
    cfg = load_config()
    if "workspace_root" in cfg:
        return Path(cfg["workspace_root"]).resolve()
    return Path(DEFAULT_WORKSPACE_ROOT).resolve()


def list_workspaces(root: Optional[Path] = None) -> List[str]:
    """
    Lists all workspace folders under root that contain Eclipse .metadata
    or activity project directories.
    """
    ws_root = root or get_workspace_root()
    if not ws_root.exists() or not ws_root.is_dir():
        return []

    workspaces = []
    # Check if the root itself is a workspace
    if (ws_root / ".metadata").exists():
        workspaces.append(ws_root.name)

    # Check child directories
    for child in ws_root.iterdir():
        if child.is_dir() and child.name not in (".metadata", "RemoteSystemsTempFiles"):
            # A valid workspace either has .metadata or contains activity folders
            has_metadata = (child / ".metadata").exists()
            has_activities = any(ACTIVITY_PATTERN.match(item.name) for item in child.iterdir() if item.is_dir())
            if has_metadata or has_activities:
                workspaces.append(child.name)

    return sorted(list(set(workspaces)))


def parse_activity_dir_name(dir_name: str) -> Optional[Tuple[str, str]]:
    """
    Parses 'activity_name [project_name]' and returns (activity_name, project_name).
    """
    m = ACTIVITY_PATTERN.match(dir_name)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return None


def list_activities(workspace_name: Optional[str] = None, root: Optional[Path] = None) -> List[Dict[str, str]]:
    """
    Lists activities in a given workspace or across all discovered workspaces.
    """
    ws_root = root or get_workspace_root()
    targets = [workspace_name] if workspace_name else list_workspaces(ws_root)

    results = []
    for ws in targets:
        ws_dir = ws_root if (ws == ws_root.name and (ws_root / ".metadata").exists()) else ws_root / ws
        if not ws_dir.exists() or not ws_dir.is_dir():
            continue

        for child in ws_dir.iterdir():
            if child.is_dir():
                parsed = parse_activity_dir_name(child.name)
                if parsed:
                    act_name, proj_name = parsed
                    results.append({
                        "workspace": ws,
                        "activity": act_name,
                        "project": proj_name,
                        "folder_name": child.name,
                        "path": str(child.resolve())
                    })

    return sorted(results, key=lambda x: (x["workspace"], x["activity"]))


def resolve_activity(activity_identifier: str, workspace_name: Optional[str] = None, root: Optional[Path] = None) -> Optional[Dict[str, str]]:
    """
    Resolves an activity directory by activity name, project name, or exact folder name.
    """
    activities = list_activities(workspace_name=workspace_name, root=root)
    # 1. Exact match on folder_name
    for a in activities:
        if a["folder_name"].lower() == activity_identifier.lower():
            return a

    # 2. Exact match on activity name
    for a in activities:
        if a["activity"].lower() == activity_identifier.lower():
            return a

    # 3. Partial / prefix match on activity name
    matches = [a for a in activities if activity_identifier.lower() in a["activity"].lower()]
    if len(matches) == 1:
        return matches[0]

    return None


def main():
    parser = argparse.ArgumentParser(description="Infor LN Studio Workspace & Activity Manager")
    parser.add_argument("--root", help="Custom workspace root directory")
    parser.add_argument("--list-workspaces", action="store_true", help="List all detected Eclipse workspaces")
    parser.add_argument("--list-activities", action="store_true", help="List all activities")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--resolve", help="Resolve directory path for an activity name")
    parser.add_argument("--set-default-workspace", help="Set default workspace in config")
    parser.add_argument("--set-default-activity", help="Set default activity in config")
    parser.add_argument("--status", action="store_true", help="Show current default workspace and activity")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else get_workspace_root()

    if args.set_default_workspace:
        cfg = load_config()
        cfg["default_workspace"] = args.set_default_workspace
        save_config(cfg)
        print(f"[OK] Set default workspace: {args.set_default_workspace}")
        return

    if args.set_default_activity:
        cfg = load_config()
        cfg["default_activity"] = args.set_default_activity
        save_config(cfg)
        print(f"[OK] Set default activity: {args.set_default_activity}")
        return

    if args.status:
        cfg = load_config()
        print("LN Studio Configuration:")
        print(f"  Workspace Root:    {root}")
        print(f"  Default Workspace: {cfg.get('default_workspace', '(not set)')}")
        print(f"  Default Activity:  {cfg.get('default_activity', '(not set)')}")
        return

    if args.list_workspaces:
        wss = list_workspaces(root)
        if args.json:
            print(json.dumps(wss, indent=2))
        else:
            print(f"Discovered {len(wss)} workspaces under '{root}':")
            for w in wss:
                print(f"  - {w}")
        return

    if args.list_activities:
        acts = list_activities(workspace_name=args.workspace, root=root)
        if args.json:
            print(json.dumps(acts, indent=2))
        else:
            print(f"Found {len(acts)} activities:")
            for a in acts:
                print(f"  [{a['workspace']}] {a['folder_name']} -> {a['path']}")
        return

    if args.resolve:
        resolved = resolve_activity(args.resolve, workspace_name=args.workspace, root=root)
        if not resolved:
            print(f"[ERROR] Could not resolve activity: '{args.resolve}'", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(resolved, indent=2))
        else:
            print(f"Resolved Activity:")
            print(f"  Workspace:   {resolved['workspace']}")
            print(f"  Activity:    {resolved['activity']}")
            print(f"  Project:     {resolved['project']}")
            print(f"  Folder:      {resolved['folder_name']}")
            print(f"  Path:        {resolved['path']}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
