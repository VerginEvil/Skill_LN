#!/usr/bin/env python3
"""
ln_studio_skill/tools/admin_sync.py
Eclipse Activity SCM (.admin) Synchronizer for Infor LN Studio.

Maintains the Java-serialized .admin file in each Activity folder, registering
newly created LN Studio components across all 12 managed extensions with proper SCM status
flags (isCreated=true, m_isDirty=true, m_isVSCHappy=false).
"""

import os
import sys
import shutil
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_workspace_manager import resolve_activity, load_config
from scm_guardrails import is_extension_component

JAVA_BIN_CANDIDATES = [
    r"C:\Program Files\Java\jdk-25.0.2\bin\java.exe",
    r"C:\Program Files\Java\latest\bin\java.exe",
    shutil.which("java") or "java"
]

# 12 Managed LN Studio Component Extensions (plus aliases .que and .fun)
MANAGED_EXTENSIONS = {
    ".tbl", ".ses", ".lib", ".dmn", ".lbl",
    ".mnu", ".rpt", ".rptdsrc", ".msg", ".qst", ".que",
    ".add", ".fnc", ".fun"
}
EXCLUDED_EXTENSIONS = {
    ".src", ".4gl", ".dal", ".clnsrc"
}
MODULE_SCOPED_TYPES = {
    "table", "session", "library", "function", "report", "menu", "additional", "businessobject"
}
PACKAGE_SCOPED_TYPES = {
    "domain", "label", "message", "question", "chart"
}
TYPE_EXTENSION_MAP = {
    "table": ".tbl",
    "session": ".ses",
    "library": ".lib",
    "function": ".fnc",
    "report": ".rpt",
    "menu": ".mnu",
    "domain": ".dmn",
    "label": ".lbl",
    "message": ".msg",
    "question": ".qst",
    "additional": ".add",
    "businessobject": ".bus",
    "chart": ".cha",
}


def normalize_admin_path(path_str: str) -> str:
    """Normalizes relative paths to project-relative paths without leading slash or :<activity>/ prefix."""
    p = str(path_str).replace("\\", "/").strip()
    while p.startswith("/"):
        p = p[1:]
    if p.startswith(":"):
        slash = p.find("/")
        p = p[slash + 1 :] if slash != -1 else p[1:]
    while p.startswith("/"):
        p = p[1:]
    return p


def get_tde_component_rel_path(
    package: str,
    comp_type: str,
    module: str = "",
    name: str = "",
    ext: Optional[str] = None,
) -> str:
    """
    Computes Native Single-XML TDE project-relative path:
    - Module-scoped types: {pkg}/{type}/{mod}/{name}.{ext}
    - Package-scoped types: {pkg}/{type}/{name}.{ext}
    """
    pkg = package.lower()
    ctype = comp_type.lower()
    if not ext:
        ext = TYPE_EXTENSION_MAP.get(ctype, f".{ctype[:3]}")
    if not ext.startswith("."):
        ext = f".{ext}"

    if ctype in MODULE_SCOPED_TYPES:
        mod = (module or (name[len(pkg):len(pkg)+3] if len(name) >= len(pkg)+3 else "")).lower()
        if mod:
            return f"{pkg}/{ctype}/{mod}/{name}{ext}"
        return f"{pkg}/{ctype}/{name}{ext}"
    else:
        return f"{pkg}/{ctype}/{name}{ext}"


def find_component_file(
    activity_path: Path,
    package: str,
    comp_type: str,
    module: str = "",
    name: str = "",
    ext: Optional[str] = None,
) -> Optional[Path]:
    """Finds a component file on disk, checking TDE path first then legacy plural subfolders."""
    tde_rel = get_tde_component_rel_path(package, comp_type, module, name, ext)
    tde_path = activity_path / tde_rel
    if tde_path.exists():
        return tde_path

    if not ext:
        ext = TYPE_EXTENSION_MAP.get(comp_type.lower(), f".{comp_type.lower()[:3]}")
    if not ext.startswith("."):
        ext = f".{ext}"

    plural = f"{comp_type.lower()}s"
    candidates = [
        activity_path / plural / f"{name}{ext}",
        activity_path / plural / module.lower() / f"{name}{ext}",
        activity_path / comp_type.lower() / f"{name}{ext}",
    ]
    for c in candidates:
        if c.exists():
            return c

    target_filename = f"{name}{ext}".lower()
    for f in activity_path.rglob(f"*{ext}"):
        if f.is_file() and f.name.lower() == target_filename:
            return f

    return None


def get_java_executable() -> str:
    """Returns path to working java executable."""
    for cand in JAVA_BIN_CANDIDATES:
        if cand and (os.path.isfile(cand) or cand == "java"):
            return cand
    return "java"


def get_admin_helper_classpath() -> str:
    """Returns classpath string including ln_studio_skill/tools/lib and dynamically resolved lnstudio_commoncore.jar (BYOJ)."""
    lib_dir = _TOOLS_DIR / "lib"
    sep = ";" if sys.platform == "win32" else ":"
    try:
        from ln_server_client import resolve_ln_studio_jars
        jar_info = resolve_ln_studio_jars()
        commoncore = jar_info.get("commoncore_jar")
        if commoncore:
            return f"{lib_dir}{sep}{commoncore}"
    except Exception:
        pass
    jar_path = lib_dir / "lnstudio_commoncore.jar"
    return f"{lib_dir}{sep}{jar_path}"


def ensure_helper_compiled() -> None:
    """Ensures AdminSyncHelper.class is compiled; compiles it on demand if missing."""
    lib_dir = _TOOLS_DIR / "lib"
    class_file = lib_dir / "tools" / "lib" / "AdminSyncHelper.class"
    java_file = lib_dir / "AdminSyncHelper.java"
    if not class_file.exists() or java_file.stat().st_mtime > class_file.stat().st_mtime:
        java_exe = get_java_executable()
        javac_cand = java_exe.replace("java.exe", "javac.exe")
        javac_exe = javac_cand if os.path.isfile(javac_cand) else (shutil.which("javac") or "javac")
        cp = get_admin_helper_classpath()
        cmd = [javac_exe, "--release", "11", "-cp", cp, "-d", str(lib_dir), str(java_file)]
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
    """Lists components registered in activity's .admin file with all 7 AdministrationComponent fields."""
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
            if len(parts) >= 8:
                norm_p = normalize_admin_path(parts[1])
                components.append({
                    "path": norm_p,
                    "isCreated": parts[2].lower() == "true",
                    "isCheckedOut": parts[3].lower() == "true",
                    "isEverCheckedIn": parts[4].lower() == "true",
                    "isExpired": parts[5].lower() == "true",
                    "isDirty": parts[6].lower() == "true",
                    "isVSCHappy": parts[7].lower() == "true",
                    "m_path": normalize_admin_path(parts[8]) if len(parts) > 8 else norm_p,
                })
            elif len(parts) >= 6:
                norm_p = normalize_admin_path(parts[1])
                components.append({
                    "path": norm_p,
                    "isCreated": parts[2].lower() == "true",
                    "isCheckedOut": parts[3].lower() == "true",
                    "isEverCheckedIn": False,
                    "isExpired": False,
                    "isDirty": parts[4].lower() == "true",
                    "isVSCHappy": parts[5].lower() == "true",
                    "m_path": norm_p,
                })
    return components


def add_component(activity_path: Path, rel_path: str) -> bool:
    """Registers a component in the activity's .admin file with exact project-relative path."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "add", [norm_path])
    if res.returncode != 0:
        raise RuntimeError(f"Failed to add component to .admin: {res.stderr}")
    return True


def remove_component(activity_path: Path, rel_path: str) -> bool:
    """Removes a component from the activity's .admin file."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "remove", [norm_path])
    if res.returncode != 0:
        raise RuntimeError(f"Failed to remove component from .admin: {res.stderr}")
    return True


def admin_after_get(activity_path: Path, rel_path: str) -> bool:
    """CMStudio state transition after Get (isCreated=false, isCheckedout=false, m_isDirty=false)."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "after_get", [norm_path])
    return res.returncode == 0


def admin_after_create(activity_path: Path, rel_path: str) -> bool:
    """CMStudio state transition after DR_Create (isCreated=true, isCheckedout=true, m_isDirty=true)."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "after_create", [norm_path])
    return res.returncode == 0


def admin_after_checkout(activity_path: Path, rel_path: str) -> bool:
    """CMStudio state transition after CheckOut (isCreated=false, isCheckedout=true, m_isDirty=false)."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "after_checkout", [norm_path])
    return res.returncode == 0


def admin_after_put(activity_path: Path, rel_path: str) -> bool:
    """CMStudio state transition after Put (m_isDirty=false, retaining isCheckedout=true)."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "after_put", [norm_path])
    return res.returncode == 0


def admin_after_checkin(activity_path: Path, rel_path: str) -> bool:
    """CMStudio state transition after CheckIn (isCreated=false, isCheckedout=false, isEvercheckedIn=true)."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "after_checkin", [norm_path])
    return res.returncode == 0


def admin_after_uncheckout(activity_path: Path, rel_path: str) -> bool:
    """CMStudio state transition after UndoCheckOut (removes uncommitted new component or resets flags)."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "after_uncheckout", [norm_path])
    return res.returncode == 0


def admin_set_vsc_happy(activity_path: Path, rel_path: str, is_vsc_happy: bool = True) -> bool:
    """Updates m_isVSCHappy in activity's .admin file."""
    admin_file = activity_path / ".admin"
    norm_path = normalize_admin_path(rel_path)
    res = run_helper(admin_file, "set-vsc", [norm_path, str(is_vsc_happy).lower()])
    return res.returncode == 0


def repair_admin_file(activity_path: Path) -> bool:
    """Repairs an existing .admin file by removing :<activity>/ prefixes and pruning standalone script files."""
    admin_file = activity_path / ".admin"
    if not admin_file.exists():
        return True
    res = run_helper(admin_file, "repair")
    return res.returncode == 0


def init_admin_file(admin_path: Path, initial_data: Optional[Dict[str, Any]] = None) -> None:
    """Initializes an empty .admin file or writes initial component map."""
    admin_path.parent.mkdir(parents=True, exist_ok=True)
    res = run_helper(admin_path, "init")
    if res.returncode != 0:
        # Fallback binary write of empty Java HashMap if java not reachable
        EMPTY_JAVA_HASHMAP = b'\xac\xed\x00\x05sr\x00\x11java.util.HashMap\x05\x07\xda\xc1\xc3\x16`\xd1\x03\x00\x02F\x00\nloadFactorI\x00\tthresholdxp?@\x00\x00\x00\x00\x00\x00w\x08\x00\x00\x00\x10\x00\x00\x00\x00x'
        admin_path.write_bytes(EMPTY_JAVA_HASHMAP)


def set_component_status(
    activity_path: Path,
    rel_path: str,
    is_created: bool = False,
    is_checked_out: bool = True,
    is_dirty: bool = True,
) -> bool:
    """Updates component SCM status flags in activity's .admin file."""
    admin_file = activity_path / ".admin"
    res = run_helper(
        admin_file,
        "set-status",
        [rel_path, str(is_created).lower(), str(is_checked_out).lower(), str(is_dirty).lower()],
    )
    if res.returncode != 0:
        raise RuntimeError(f"Failed to update status in .admin: {res.stderr}")
    return True


write_admin_file = init_admin_file


def scan_and_sync_activity(activity_path: Path) -> Dict[str, Any]:
    """
    Scans activity folder on disk, compares against .admin entries across all
    12 LN Studio component extensions, registers untracked files, and removes
    obsolete entries only when they match managed extensions.
    """
    repair_admin_file(activity_path)
    admin_file = activity_path / ".admin"
    registered = {c["path"]: c for c in list_admin_components(activity_path)}

    # Scan files on disk across all 12 managed extensions (excluding standalone scripts)
    disk_files = set()

    for p in activity_path.rglob("*"):
        if p.is_file() and p.suffix.lower() in MANAGED_EXTENSIONS and p.suffix.lower() not in EXCLUDED_EXTENSIONS:
            # Skip read-only Extension Modeler components
            if is_extension_component(p):
                continue
            rel = normalize_admin_path(p.relative_to(activity_path).as_posix())
            disk_files.add(rel)

    to_add = sorted(list(disk_files - set(registered.keys())))
    to_remove = sorted([
        k for k in (set(registered.keys()) - disk_files)
        if Path(k).suffix.lower() in MANAGED_EXTENSIONS
    ])

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
    parser.add_argument("--path", "--activity-path", dest="path", help="Direct activity directory path")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--status", action="store_true", help="Display registered components in .admin")
    parser.add_argument("--scan-and-update", action="store_true", help="Scan disk files and synchronize .admin")
    parser.add_argument("--repair", action="store_true", help="Repair .admin: remove :<activity>/ prefixes and prune standalone scripts")
    parser.add_argument("--add", help="Add specific relative path to .admin")
    parser.add_argument("--remove", help="Remove specific relative path from .admin")

    args = parser.parse_args()

    act_path: Optional[Path] = None
    if args.path:
        act_path = Path(args.path).resolve()
    elif args.activity:
        resolved = resolve_activity(args.activity, workspace_name=args.workspace)
        if not resolved:
            print(f"[ERROR] Could not resolve activity: '{args.activity}'", file=sys.stderr)
            sys.exit(1)
        act_path = Path(resolved["path"])
    else:
        # Attempt auto-detection from current working directory
        from ln_workspace_manager import detect_current_activity
        detected = detect_current_activity()
        if detected:
            act_path = Path(detected["path"])
        else:
            print("[ERROR] Please provide --activity or --activity-path (or run within an Activity directory)", file=sys.stderr)
            sys.exit(1)

    if not act_path.exists():
        print(f"[ERROR] Activity directory does not exist: {act_path}", file=sys.stderr)
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

    if args.repair:
        repair_admin_file(act_path)
        print(f"[SUCCESS] Repaired .admin for '{act_path.name}'.")
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
