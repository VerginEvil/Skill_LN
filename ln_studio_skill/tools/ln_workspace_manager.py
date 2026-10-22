#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_workspace_manager.py
Infor LN Studio Workspace Discovery & Activity Environment Manager.

Scans Eclipse workspaces, lists activities matching '<activity> [<project>]',
resolves filesystem paths, and defaults only to the pinned LN Studio installation.
Enforces explicit workspace / activity resolution without hardcoded fallback assumptions.
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple

PINNED_STUDIO_PATH = r"D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64"
CONFIG_FILE_NAME = ".ln_studio_config.json"
ACTIVITY_PATTERN = re.compile(r"^(.+?)\s+\[([A-Za-z0-9_]+)\]$")


def get_skill_root() -> Path:
    """Returns the skill root (ln_studio_skill/) regardless of checkout path."""
    return Path(__file__).resolve().parent.parent


def get_repo_root() -> Path:
    """Returns the root directory of the Skill_LN repository."""
    return get_skill_root().parent


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


def get_studio_installation_path(override_path: Optional[str] = None) -> Path:
    """
    Returns the pinned Infor LN Studio installation path.
    Honors explicit override or LN_STUDIO_PATH environment variable if set.
    """
    if override_path:
        return Path(override_path).resolve()
    env_studio = os.environ.get("LN_STUDIO_PATH")
    if env_studio:
        return Path(env_studio).resolve()
    return Path(PINNED_STUDIO_PATH).resolve()


def get_workspace_root(override_root: Optional[str] = None) -> Optional[Path]:
    """
    Resolves workspace root from argument, env variable, config, or discovery root.
    Returns None if no root could be resolved.
    """
    if override_root:
        return Path(override_root).resolve()
    env_root = os.environ.get("LN_WORKSPACE_ROOT")
    if env_root:
        return Path(env_root).resolve()
    cfg = load_config()
    if "workspace_root" in cfg:
        return Path(cfg["workspace_root"]).resolve()

    # Known standard location if it exists on host
    standard_loc = Path(r"C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio")
    if standard_loc.exists() and standard_loc.is_dir():
        return standard_loc

    return None


def list_workspaces(root: Optional[Path] = None) -> List[str]:
    """
    Lists all workspace folders under root that contain Eclipse .metadata
    or activity project directories.
    """
    ws_root = root or get_workspace_root()
    if not ws_root or not ws_root.exists() or not ws_root.is_dir():
        return []

    workspaces = []
    # Check if the root itself is a workspace
    if (ws_root / ".metadata").exists():
        workspaces.append(ws_root.name)

    # Check child directories
    for child in ws_root.iterdir():
        if child.is_dir() and child.name not in (".metadata", "RemoteSystemsTempFiles"):
            has_metadata = (child / ".metadata").exists()
            try:
                has_activities = any(ACTIVITY_PATTERN.match(item.name) for item in child.iterdir() if item.is_dir())
            except Exception:
                has_activities = False
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


def detect_current_activity() -> Optional[Dict[str, str]]:
    """
    Detects if current working directory (or any of its parents) is an Activity folder.
    """
    curr = Path.cwd().resolve()
    while curr and curr != curr.parent:
        if (curr / ".project").exists() or (curr / ".admin").exists():
            parsed = parse_activity_dir_name(curr.name)
            act_name = parsed[0] if parsed else curr.name
            proj_name = parsed[1] if parsed else ""
            return {
                "workspace": curr.parent.name,
                "activity": act_name,
                "project": proj_name,
                "folder_name": curr.name,
                "path": str(curr)
            }
        curr = curr.parent
    return None


def list_activities(workspace_name: Optional[str] = None, root: Optional[Path] = None) -> List[Dict[str, str]]:
    """
    Lists activities in a given workspace or across all discovered workspaces under root.
    """
    ws_root = root or get_workspace_root()
    if not ws_root or not ws_root.exists():
        return []

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


def resolve_activity(
    activity_identifier: Optional[str] = None,
    workspace_name: Optional[str] = None,
    root: Optional[Path] = None,
    activity_path: Optional[str] = None
) -> Optional[Dict[str, str]]:
    """
    Resolves an activity directory by path, activity name, project name, or exact folder name.
    Requires explicit workspace or path unless running inside an Activity folder.
    """
    # 1. Direct explicit activity path
    if activity_path:
        p = Path(activity_path).resolve()
        if p.exists() and p.is_dir():
            parsed = parse_activity_dir_name(p.name)
            act_name = parsed[0] if parsed else p.name
            proj_name = parsed[1] if parsed else ""
            return {
                "workspace": p.parent.name,
                "activity": act_name,
                "project": proj_name,
                "folder_name": p.name,
                "path": str(p)
            }
        return None

    # 2. Activity identifier passed as a filesystem path
    if activity_identifier:
        candidate_path = Path(activity_identifier)
        if candidate_path.exists() and candidate_path.is_dir():
            cand_p = candidate_path.resolve()
            parsed = parse_activity_dir_name(cand_p.name)
            act_name = parsed[0] if parsed else cand_p.name
            proj_name = parsed[1] if parsed else ""
            return {
                "workspace": cand_p.parent.name,
                "activity": act_name,
                "project": proj_name,
                "folder_name": cand_p.name,
                "path": str(cand_p)
            }

    # 3. If no identifier given, attempt cwd auto-detection
    if not activity_identifier:
        return detect_current_activity()

    # 4. Search activities within workspace or root
    activities = list_activities(workspace_name=workspace_name, root=root)

    # Exact match on folder_name
    for a in activities:
        if a["folder_name"].lower() == activity_identifier.lower():
            return a

    # Exact match on activity name
    matches_exact = [a for a in activities if a["activity"].lower() == activity_identifier.lower()]
    if len(matches_exact) == 1:
        return matches_exact[0]
    elif len(matches_exact) > 1:
        # Multiple matches across workspaces; if current dir matches one, return it
        cwd_act = detect_current_activity()
        if cwd_act and any(m["path"] == cwd_act["path"] for m in matches_exact):
            return cwd_act
        # Return first if matching workspace_name, or require disambiguation
        if workspace_name:
            for m in matches_exact:
                if m["workspace"].lower() == workspace_name.lower():
                    return m
        return matches_exact[0]

    # Partial / substring match on activity name
    matches = [a for a in activities if activity_identifier.lower() in a["activity"].lower()]
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1 and workspace_name:
        for m in matches:
            if m["workspace"].lower() == workspace_name.lower():
                return m

    return None


def main():
    parser = argparse.ArgumentParser(description="Infor LN Studio Workspace & Activity Manager")
    parser.add_argument("--root", help="Custom workspace root directory")
    parser.add_argument("--list-workspaces", action="store_true", help="List all detected Eclipse workspaces")
    parser.add_argument("--list-activities", action="store_true", help="List all activities")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--resolve", help="Resolve directory path for an activity name")
    parser.add_argument("--activity-path", help="Direct activity directory path")
    parser.add_argument("--studio-path", action="store_true", help="Display pinned LN Studio installation path")
    parser.add_argument("--set-default-workspace", help="Set default workspace in config")
    parser.add_argument("--set-default-activity", help="Set default activity in config")
    parser.add_argument("--status", action="store_true", help="Show workspace status and pinned studio path")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else get_workspace_root()

    if args.studio_path:
        print(f"Pinned LN Studio Path: {get_studio_installation_path()}")
        return

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
        detected = detect_current_activity()
        print("LN Studio Configuration:")
        print(f"  Pinned Studio Path: {get_studio_installation_path()}")
        print(f"  Workspace Root:     {root or '(none)'}")
        print(f"  Current Activity:   {detected['folder_name'] if detected else '(none)'}")
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

    if args.resolve or args.activity_path:
        target = args.resolve or args.activity_path
        resolved = resolve_activity(target, workspace_name=args.workspace, root=root, activity_path=args.activity_path)
        if not resolved:
            print(f"[ERROR] Could not resolve activity: '{target}'", file=sys.stderr)
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
