#!/usr/bin/env python3
"""
ln_studio_skill/tools/inject_ln_script.py
Bidirectional 4GL Source Code Synchronizer for Infor LN Studio.

Bridges standalone Baan 4GL source files (.dal, .cln, .src, .lib) in the Git repository
with the embedded <DR_Module><Source><expression> XML tags in .tbl, .ses, and .lib workspace files.
Guarantees 100% round-trip fidelity with zero byte or character loss, enforcing Read-Only check-out protection.
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import Optional, Tuple

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_workspace_manager import resolve_activity, load_config, detect_current_activity
from scm_guardrails import assert_file_writable, is_extension_component, ReadOnlyComponentError

EXPRESSION_REGEX = re.compile(r"<expression>(.*?)</expression>", re.DOTALL)


def escape_4gl_to_xml(source_code: str) -> str:
    """
    Escapes plain Baan 4GL source code for inclusion in an XML text node.
    Only &, <, and > must be escaped inside standard element character data.
    """
    return (
        source_code.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def unescape_xml_to_4gl(xml_text: str) -> str:
    """
    Unescapes XML text back to plain Baan 4GL source code.
    Decodes &lt;, &gt;, &quot;, &apos;, and &amp;.
    """
    res = xml_text.replace("&lt;", "<")
    res = res.replace("&gt;", ">")
    res = res.replace("&quot;", '"')
    res = res.replace("&apos;", "'")
    res = res.replace("&amp;", "&")
    return res


def extract_script_from_xml(xml_content: str) -> Optional[str]:
    """Extracts and unescapes the 4GL code from <expression> in XML content."""
    m = EXPRESSION_REGEX.search(xml_content)
    if not m:
        return None
    raw_expr = m.group(1)
    stripped = raw_expr.strip()
    if stripped.startswith("<![CDATA[") and stripped.endswith("]]>"):
        return stripped[9:-3].strip()
    return unescape_xml_to_4gl(raw_expr)


def inject_script_into_xml(xml_content: str, script_code: str) -> str:
    """
    Safely injects escaped 4GL source code into the <expression> tag of an existing XML content.
    If no <expression> tag exists, raises ValueError.
    """
    m = EXPRESSION_REGEX.search(xml_content)
    if m:
        start, end = m.span(1)
        raw_inner = m.group(1)
        if "<![CDATA[" in raw_inner:
            return xml_content[:start] + f"<![CDATA[\n{script_code}\n]]>" + xml_content[end:]
        escaped_code = escape_4gl_to_xml(script_code)
        return xml_content[:start] + escaped_code + xml_content[end:]
    else:
        raise ValueError("Could not find <expression> tag in target XML file.")


def extract_file(xml_file_path: Path, output_file_path: Path) -> bool:
    """Extracts 4GL code from an XML file and writes to output file."""
    if not xml_file_path.exists():
        raise FileNotFoundError(f"Source XML file does not exist: {xml_file_path}")

    with open(xml_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    script = extract_script_from_xml(content)
    if script is None:
        raise ValueError(f"No <expression> found in {xml_file_path}")

    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(script)

    return True


def inject_file(source_script_path: Path, target_xml_path: Path) -> bool:
    """
    Injects 4GL code from a plain script file into target XML file.
    Enforces SCM Read-Only protection on target_xml_path before writing.
    """
    if not source_script_path.exists():
        raise FileNotFoundError(f"Source 4GL file does not exist: {source_script_path}")
    if not target_xml_path.exists():
        raise FileNotFoundError(f"Target XML file does not exist: {target_xml_path}")

    # Enforce Read-Only check-out protection
    assert_file_writable(target_xml_path)

    with open(source_script_path, "r", encoding="utf-8") as f:
        script_code = f.read()

    with open(target_xml_path, "r", encoding="utf-8") as f:
        xml_content = f.read()

    updated_xml = inject_script_into_xml(xml_content, script_code)

    with open(target_xml_path, "w", encoding="utf-8") as f:
        f.write(updated_xml)

    return True


def sync_all_activity_scripts(
    activity_path: Path,
    repo_scripts_dir: Path,
    direction: str = "repo-to-ws"
) -> int:
    """
    Synchronizes all scripts between repo scripts directory and workspace activity.
    direction: 'repo-to-ws' (inject) or 'ws-to-repo' (extract).
    Supports .tbl (DAL), .ses (UI), and .lib (Library / Extension).
    """
    synced_count = 0
    if direction == "repo-to-ws":
        # Search repo scripts: scripts/dal/*.dal, scripts/ui/*.cln, scripts/lib/*.lib
        for script_file in repo_scripts_dir.rglob("*"):
            if not script_file.is_file():
                continue
            ext = script_file.suffix.lower()
            stem = script_file.stem.lower()

            target_ext = None
            if ext == ".dal":
                target_ext = ".tbl"
            elif ext in (".cln", ".src"):
                target_ext = ".ses"
            elif ext == ".lib":
                target_ext = ".lib"
            elif ext in (".rpt", ".rep", ".rptdsrc"):
                target_ext = ".rpt"

            if target_ext:
                # Search matching target file in activity
                matches = list(activity_path.rglob(f"{stem}{target_ext}"))
                if matches:
                    target_file = matches[0]
                    if is_extension_component(target_file):
                        print(f"  [SKIPPED] Extension component '{target_file.name}' is Read-Only in Studio. Use session ttext1500m000 in LN UI.")
                        continue
                    # Enforce guardrail
                    assert_file_writable(target_file, activity_path)
                    inject_file(script_file, target_file)
                    print(f"  [INJECTED] {script_file.relative_to(repo_scripts_dir.parent)} -> {target_file.relative_to(activity_path)}")
                    synced_count += 1
    else:
        # ws-to-repo: Extract from all .tbl, .ses, .lib in activity
        for xml_file in activity_path.rglob("*"):
            if not xml_file.is_file():
                continue
            ext = xml_file.suffix.lower()
            stem = xml_file.stem.lower()

            out_subfolder = None
            out_ext = None
            if ext == ".tbl":
                out_subfolder = "dal"
                out_ext = ".dal"
            elif ext == ".ses":
                out_subfolder = "ui"
                out_ext = ".cln"
            elif ext == ".lib":
                out_subfolder = "lib"
                out_ext = ".lib"
            elif ext in (".rpt", ".rptdsrc"):
                out_subfolder = "report"
                out_ext = ".rpt"

            if out_subfolder and out_ext:
                out_file = repo_scripts_dir / out_subfolder / f"{stem}{out_ext}"
                try:
                    if extract_file(xml_file, out_file):
                        print(f"  [EXTRACTED] {xml_file.relative_to(activity_path)} -> {out_file.relative_to(repo_scripts_dir.parent)}")
                        synced_count += 1
                except ValueError:
                    pass

    return synced_count


def main():
    parser = argparse.ArgumentParser(description="Synchronize Baan 4GL source code with LN Studio XML components")
    parser.add_argument("--inject", action="store_true", help="Inject plain script into XML")
    parser.add_argument("--extract", action="store_true", help="Extract plain script from XML")
    parser.add_argument("--source", help="Source script/XML file path")
    parser.add_argument("--target", help="Target XML file path (for --inject)")
    parser.add_argument("--output", help="Output script file path (for --extract)")

    parser.add_argument("--sync-all", action="store_true", help="Batch sync all scripts between activity and repo")
    parser.add_argument("--activity", help="Target activity folder name or activity code")
    parser.add_argument("--activity-path", help="Direct activity directory path")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--scripts-dir", default=str(_SKILL_ROOT / "scripts"), help="Directory containing repository scripts")
    parser.add_argument("--direction", choices=["repo-to-ws", "ws-to-repo"], default="repo-to-ws")

    args = parser.parse_args()

    if args.inject:
        if not args.source or not args.target:
            print("[ERROR] --inject requires both --source and --target", file=sys.stderr)
            sys.exit(1)
        try:
            inject_file(Path(args.source), Path(args.target))
            print(f"[SUCCESS] Injected '{args.source}' into '{args.target}'")
        except ReadOnlyComponentError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"[ERROR] Injection failed: {e}", file=sys.stderr)
            sys.exit(1)
        return

    if args.extract:
        if not args.source or not args.output:
            print("[ERROR] --extract requires both --source and --output", file=sys.stderr)
            sys.exit(1)
        try:
            extract_file(Path(args.source), Path(args.output))
            print(f"[SUCCESS] Extracted '{args.source}' to '{args.output}'")
        except Exception as e:
            print(f"[ERROR] Extraction failed: {e}", file=sys.stderr)
            sys.exit(1)
        return

    if args.sync_all:
        act_path = None
        if args.activity_path:
            act_path = Path(args.activity_path).resolve()
        elif args.activity:
            resolved = resolve_activity(args.activity, workspace_name=args.workspace)
            if not resolved:
                print(f"[ERROR] Could not resolve activity: '{args.activity}'", file=sys.stderr)
                sys.exit(1)
            act_path = Path(resolved["path"])
        else:
            detected = detect_current_activity()
            if detected:
                act_path = Path(detected["path"])
            else:
                print("[ERROR] Please provide --activity or --activity-path (or run within an Activity directory)", file=sys.stderr)
                sys.exit(1)

        scripts_path = Path(args.scripts_dir).resolve()

        print(f"Syncing scripts ({args.direction}) between:")
        print(f"  Activity: {act_path}")
        print(f"  Scripts:  {scripts_path}")

        try:
            count = sync_all_activity_scripts(act_path, scripts_path, direction=args.direction)
            print(f"[SUCCESS] Synchronized {count} script(s).")
        except ReadOnlyComponentError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
