#!/usr/bin/env python3
"""
tools/admin_sync.py
Eclipse Activity SCM (.admin) Synchronizer for Infor LN Studio.

Maintains the Java-serialized .admin file in each Activity folder, registering
newly created .tbl, .ses, .lib, .dmn, and .lbl components with proper SCM status
flags (isCreated=true, m_isDirty=true, m_isVSCHappy=false).
"""

import os
import sys
import shutil
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

_current_dir = Path(__file__).resolve().parent
_repo_root = _current_dir.parent
for p in (str(_repo_root), str(_current_dir)):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from tools.ln_workspace_manager import resolve_activity, load_config
except ImportError:
    from ln_workspace_manager import resolve_activity, load_config

JAVA_BIN_CANDIDATES = [
    r"C:\Program Files\Java\jdk-25.0.2\bin\java.exe",
    r"C:\Program Files\Java\latest\bin\java.exe",
    shutil.which("java") or "java"
]


def get_java_executable() -> str:
    """Returns path to working java executable."""
    for cand in JAVA_BIN_CANDIDATES:
        if cand and (os.path.isfile(cand) or cand == "java"):
            return cand
    return "java"


def get_admin_helper_classpath() -> str:
    """Returns classpath string including tools/lib and lnstudio_commoncore.jar."""
    lib_dir = _current_dir / "lib"
    jar_path = lib_dir / "lnstudio_commoncore.jar"
    return f"{lib_dir};{jar_path}"


def ensure_helper_compiled() -> None:
    """Ensures AdminSyncHelper.class is compiled; compiles it on demand if missing."""
    lib_dir = _current_dir / "lib"
    class_file = lib_dir / "tools" / "lib" / "AdminSyncHelper.class"
    java_file = lib_dir / "AdminSyncHelper.java"
    if not class_file.exists() and java_file.exists():
        java_exe = get_java_executable()
        javac_cand = java_exe.replace("java.exe", "javac.exe")
        javac_exe = javac_cand if os.path.isfile(javac_cand) else (shutil.which("javac") or "javac")
        jar_path = lib_dir / "lnstudio_commoncore.jar"
        cmd = [javac_exe, "-d", str(lib_dir), str(java_file)]
        subprocess.run(cmd, capture_output=True, text=True, check=False)


def run_helper(admin_file: Path, cmd: str, args: Optional[List[str]] = None) -> subprocess.CompletedProcess:
    """Invokes Java AdminSyncHelper CLI."""
    ensure_helper_compiled()
    java_exe = get_java_executable()
    cp = get_admin_helper_classpath()
    full_cmd = [java_exe, "-cp", cp, "tools.lib.AdminSyncHelper", str(admin_file), cmd]
    if args:
        full_cmd.extend(args)

    return subprocess.run(full_cmd, capture_output=True, text=True, check=False)


def list_admin_components(activity_path: Path) -> List[Dict[str, Any]]:
    """Lists components registered in activity's .admin file."""
    admin_file = activity_path / ".admin"
    if not admin_file.exists():
        return []

    res = run_helper(admin_file, "list")
    if res.returncode != 0:
        raise RuntimeError(f"Failed to read .admin file: {res.stderr}")

    components = []
    for line in res.stdout.strip().splitlines():
        if line.startswith("ENTRY\t"):
            parts = line.split("\t")
            if len(parts) >= 6:
                components.append({
                    "path": parts[1],
                    "isCreated": parts[2].lower() == "true",
                    "isCheckedOut": parts[3].lower() == "true",
                    "isDirty": parts[4].lower() == "true",
                    "isVSCHappy": parts[5].lower() == "true",
                })
    return components


def add_component(activity_path: Path, rel_path: str) -> bool:
    """Registers a component in the activity's .admin file."""
    admin_file = activity_path / ".admin"
    act_folder = activity_path.name
    res = run_helper(admin_file, "add", [rel_path, act_folder])
    if res.returncode != 0:
        raise RuntimeError(f"Failed to add component to .admin: {res.stderr}")
    return True


def remove_component(activity_path: Path, rel_path: str) -> bool:
    """Removes a component from the activity's .admin file."""
    admin_file = activity_path / ".admin"
    res = run_helper(admin_file, "remove", [rel_path])
    if res.returncode != 0:
        raise RuntimeError(f"Failed to remove component from .admin: {res.stderr}")
    return True


def scan_and_sync_activity(activity_path: Path) -> Dict[str, Any]:
    """
    Scans activity folder on disk, compares against .admin entries,
    registers untracked files, and cleans up missing ones.
    """
    admin_file = activity_path / ".admin"
    registered = {c["path"]: c for c in list_admin_components(activity_path)}

    # Scan files on disk
    managed_exts = {".tbl", ".ses", ".lib", ".dmn", ".lbl"}
    disk_files = set()

    for p in activity_path.rglob("*"):
        if p.is_file() and p.suffix.lower() in managed_exts:
            rel = p.relative_to(activity_path).as_posix()
            disk_files.add(rel)

    to_add = sorted(list(disk_files - set(registered.keys())))
    to_remove = sorted(list(set(registered.keys()) - disk_files))

    added = []
    removed = []

    for item in to_add:
        add_component(activity_path, item)
        added.append(item)

    for item in to_remove:
        remove_component(activity_path, item)
        removed.append(item)

    return {
        "activity": activity_path.name,
        "total_disk_components": len(disk_files),
        "total_registered": len(registered) + len(added) - len(removed),
        "added": added,
        "removed": removed
    }


def main():
    parser = argparse.ArgumentParser(description="Synchronize Infor LN Studio Activity .admin File")
    parser.add_argument("--activity", help="Activity name or folder name")
    parser.add_argument("--path", help="Direct activity directory path")
    parser.add_argument("--status", action="store_true", help="Display registered components in .admin")
    parser.add_argument("--scan-and-update", action="store_true", help="Scan disk files and synchronize .admin")
    parser.add_argument("--add", help="Add specific relative path to .admin")
    parser.add_argument("--remove", help="Remove specific relative path from .admin")

    args = parser.parse_args()

    act_path: Optional[Path] = None
    if args.path:
        act_path = Path(args.path).resolve()
    elif args.activity:
        resolved = resolve_activity(args.activity)
        if not resolved:
            print(f"[ERROR] Could not resolve activity: '{args.activity}'", file=sys.stderr)
            sys.exit(1)
        act_path = Path(resolved["path"])
    else:
        cfg = load_config()
        def_act = cfg.get("default_activity")
        if def_act:
            resolved = resolve_activity(def_act)
            if resolved:
                act_path = Path(resolved["path"])

    if not act_path:
        print("[ERROR] Please provide --activity or --path", file=sys.stderr)
        sys.exit(1)

    if args.status:
        comps = list_admin_components(act_path)
        print(f"Activity: {act_path.name}")
        print(f"Registered Components in .admin ({len(comps)}):")
        for c in comps:
            flags = []
            if c["isCreated"]: flags.append("Created")
            if c["isCheckedOut"]: flags.append("CheckedOut")
            if c["isDirty"]: flags.append("Dirty")
            flags_str = ",".join(flags) if flags else "Synced"
            print(f"  [{flags_str:<12}] {c['path']}")
        return

    if args.scan_and_update:
        print(f"Scanning and updating .admin for '{act_path.name}'...")
        res = scan_and_sync_activity(act_path)
        print(f"[SUCCESS] Scanned {res['total_disk_components']} components.")
        if res["added"]:
            print(f"  Added {len(res['added'])} component(s):")
            for a in res["added"]:
                print(f"    + {a}")
        if res["removed"]:
            print(f"  Removed {len(res['removed'])} obsolete component(s):")
            for r in res["removed"]:
                print(f"    - {r}")
        if not res["added"] and not res["removed"]:
            print("  All components are already in sync.")
        return

    if args.add:
        add_component(act_path, args.add)
        print(f"[SUCCESS] Added '{args.add}' to .admin")
        return

    if args.remove:
        remove_component(act_path, args.remove)
        print(f"[SUCCESS] Removed '{args.remove}' from .admin")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
