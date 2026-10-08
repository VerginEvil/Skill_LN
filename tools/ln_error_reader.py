#!/usr/bin/env python3
"""
tools/ln_error_reader.py
Eclipse Problem Marker & Error Diagnostics Reader for Infor LN Studio.

Directly decodes the binary .markers files in Eclipse workspace metadata:
  <workspace>/.metadata/.plugins/org.eclipse.core.resources/.projects/<Activity>/.markers
and extracts compiler errors, warnings, line numbers, and messages.
Also scans <workspace>/.metadata/.log for JCA connection or communication errors.
"""

import os
import sys
import json
import struct
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

_current_dir = Path(__file__).resolve().parent
_repo_root = _current_dir.parent
for p in (str(_repo_root), str(_current_dir)):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from tools.ln_workspace_manager import resolve_activity, load_config, get_workspace_root
except ImportError:
    from ln_workspace_manager import resolve_activity, load_config, get_workspace_root

SEVERITY_MAP = {
    2: "ERROR",
    1: "WARNING",
    0: "INFO"
}


def parse_eclipse_markers_file(markers_file_path: Path) -> List[Dict[str, Any]]:
    """
    Parses Eclipse MarkerReader_3 binary format (.markers) and returns
    list of decoded problem markers.
    """
    if not markers_file_path.exists():
        return []

    with open(markers_file_path, "rb") as f:
        data = f.read()

    pos = 0
    if len(data) < 4:
        return []

    # Version header
    version = struct.unpack_from(">I", data, pos)[0]
    pos += 4

    types_table: List[str] = []
    markers: List[Dict[str, Any]] = []

    def read_utf() -> str:
        nonlocal pos
        if pos + 2 > len(data):
            return ""
        slen = struct.unpack_from(">H", data, pos)[0]
        pos += 2
        sval = data[pos:pos+slen].decode("utf-8", errors="replace")
        pos += slen
        return sval

    while pos < len(data):
        res_path = read_utf()
        if not res_path and pos >= len(data):
            break
        if pos + 4 > len(data):
            break

        marker_count = struct.unpack_from(">I", data, pos)[0]
        pos += 4

        for _ in range(marker_count):
            if pos >= len(data):
                break

            marker_id = struct.unpack_from(">Q", data, pos)[0]
            pos += 8

            type_flag = data[pos]
            pos += 1

            if type_flag == 1:
                type_idx = struct.unpack_from(">I", data, pos)[0]
                pos += 4
                marker_type = types_table[type_idx] if type_idx < len(types_table) else "unknown"
            elif type_flag == 2:
                marker_type = read_utf()
                types_table.append(marker_type)
            else:
                marker_type = "unknown"

            attr_count = struct.unpack_from(">h", data, pos)[0]
            pos += 2
            attrs: Dict[str, Any] = {}

            if attr_count > 0:
                for _ in range(attr_count):
                    key = read_utf()
                    val_type = data[pos]
                    pos += 1
                    if val_type == 1:  # boolean
                        val = bool(data[pos])
                        pos += 1
                    elif val_type == 2:  # int
                        val = struct.unpack_from(">i", data, pos)[0]
                        pos += 4
                    elif val_type == 3:  # string
                        val = read_utf()
                    else:
                        val = None
                    attrs[key] = val

            creation_time = 0
            if pos + 8 <= len(data):
                creation_time = struct.unpack_from(">Q", data, pos)[0]
                pos += 8

            # Clean up resource path relative to activity project root
            clean_res = res_path.strip("/")
            parts = clean_res.split("/", 1)
            rel_file = parts[1] if len(parts) > 1 else clean_res

            sev_code = attrs.get("severity", 1)
            sev_str = SEVERITY_MAP.get(sev_code, "UNKNOWN")

            markers.append({
                "id": marker_id,
                "type": marker_type,
                "file": rel_file,
                "resource_path": res_path,
                "line": attrs.get("lineNumber", 0),
                "severity_code": sev_code,
                "severity": sev_str,
                "message": attrs.get("message", ""),
                "is_script_problem": bool(attrs.get("isScriptProblem", False)),
                "creation_time": creation_time,
                "attributes": attrs
            })

    return markers


def scan_workspace_log_for_errors(workspace_root: Path, max_lines: int = 50) -> List[str]:
    """Scans <workspace>/.metadata/.log for recent JCA/Bshell errors."""
    log_file = workspace_root / ".metadata" / ".log"
    if not log_file.exists():
        return []

    errors = []
    try:
        with open(log_file, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
            for line in lines[-max_lines:]:
                if "!MESSAGE" in line and ("error" in line.lower() or "exception" in line.lower() or "failed" in line.lower()):
                    errors.append(line.strip())
    except Exception:
        pass
    return errors


def read_activity_diagnostics(
    activity_name: Optional[str] = None,
    errors_only: bool = False
) -> Dict[str, Any]:
    """
    Finds activity project, resolves its .markers file, decodes problem markers,
    and returns diagnostic summary.
    """
    act_ident = activity_name
    if not act_ident:
        cfg = load_config()
        act_ident = cfg.get("default_activity")
    if not act_ident:
        raise ValueError("No activity specified and no default activity configured.")

    resolved = resolve_activity(act_ident)
    if not resolved:
        raise ValueError(f"Could not resolve activity: '{act_ident}'")

    ws_root = get_workspace_root()
    ws_name = resolved["workspace"]
    folder_name = resolved["folder_name"]

    # Locate .markers file
    project_markers_path = (
        ws_root / ws_name / ".metadata" / ".plugins" / "org.eclipse.core.resources" / ".projects" / folder_name / ".markers"
    )

    markers = parse_eclipse_markers_file(project_markers_path)

    # Filter by problem type if applicable
    problem_markers = [m for m in markers if "problem" in m["type"].lower()]
    if not problem_markers:
        problem_markers = markers

    if errors_only:
        problem_markers = [m for m in problem_markers if m["severity"] == "ERROR"]

    # Sort: Errors first, then by file and line
    problem_markers.sort(key=lambda x: (0 if x["severity"] == "ERROR" else 1, x["file"], x["line"]))

    error_count = sum(1 for m in problem_markers if m["severity"] == "ERROR")
    warning_count = sum(1 for m in problem_markers if m["severity"] == "WARNING")

    # Scan log file
    ws_log_errors = scan_workspace_log_for_errors(ws_root / ws_name)

    return {
        "activity": resolved["activity"],
        "project": resolved["project"],
        "folder": folder_name,
        "workspace": ws_name,
        "markers_file": str(project_markers_path),
        "total_problems": len(problem_markers),
        "errors_count": error_count,
        "warnings_count": warning_count,
        "markers": problem_markers,
        "log_errors": ws_log_errors
    }


def main():
    parser = argparse.ArgumentParser(description="Infor LN Studio Problem Marker & Diagnostics Reader")
    parser.add_argument("--activity", help="Activity name or folder name")
    parser.add_argument("--markers-file", help="Direct path to .markers binary file")
    parser.add_argument("--errors-only", action="store_true", help="Only report ERROR severity (ignore warnings)")
    parser.add_argument("--json", action="store_true", help="Output in structured JSON format")

    args = parser.parse_args()

    try:
        if args.markers_file:
            mf = Path(args.markers_file)
            raw_markers = parse_eclipse_markers_file(mf)
            if args.errors_only:
                raw_markers = [m for m in raw_markers if m["severity"] == "ERROR"]
            if args.json:
                print(json.dumps(raw_markers, indent=2))
            else:
                print(f"Decoded {len(raw_markers)} markers from {mf}:")
                for m in raw_markers:
                    print(f"  [{m['severity']}] {m['file']}:{m['line']} -> {m['message']}")
            sys.exit(1 if any(m["severity"] == "ERROR" for m in raw_markers) else 0)

        diag = read_activity_diagnostics(activity_name=args.activity, errors_only=args.errors_only)

        if args.json:
            print(json.dumps(diag, indent=2))
        else:
            print(f"=== Eclipse Diagnostics: {diag['folder']} ({diag['workspace']}) ===")
            print(f"Errors: {diag['errors_count']} | Warnings: {diag['warnings_count']}")
            print("-" * 65)

            if not diag["markers"]:
                print("[CLEAN] No problem markers found.")
            else:
                for m in diag["markers"]:
                    sev = m["severity"]
                    sev_label = f"[{sev}]" if sev == "ERROR" else f"({sev})"
                    print(f"  {sev_label:<9} {m['file']}:{m['line']}")
                    print(f"            {m['message']}")

            if diag["log_errors"]:
                print("\nWorkspace Log Errors:")
                for le in diag["log_errors"][-3:]:
                    print(f"  [LOG] {le}")

        sys.exit(1 if diag["errors_count"] > 0 else 0)

    except Exception as e:
        print(f"[ERROR] Diagnostics reader failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
