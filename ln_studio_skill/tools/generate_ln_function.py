#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_function.py
Infor LN Studio Include Function Component Generator.

Generates production-grade .fnc (and legacy .fun) XML files matching Infor LN Studio 10.8 <DR_Module><type>function</type> specifications.
Registers components in .admin and enforces SCM protection.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional, Union

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_workspace_manager import resolve_activity, detect_current_activity
from scm_guardrails import assert_file_writable, ReadOnlyComponentError
from admin_sync import add_component


def generate_function_xml(spec: Dict[str, Any], application: str) -> str:
    """Generates standard <DR_Module> .fnc XML for an Include Function."""
    code = spec["code"]
    desc = spec.get("description", code)
    ver = spec.get("version_id", "B61O_a_ext")
    script = spec.get("script", f"| Function: {code}\nfunction extern void {code}_init()\n{{\n}}\n")

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        '<DR_Module xmlns="http://www.infor.com/businessline/application/dr" version="1.0">',
        f'  <description>{desc}</description>',
        f'  <versionID>{ver}</versionID>',
        '  <type>function</type>',
        f'  <name>{code}</name>',
        '  <Source>',
        f'    <expression><![CDATA[{script}]]></expression>',
        '    <sourceType>6</sourceType>',
        f'    <sourceName>{code}</sourceName>',
        '  </Source>',
        f'  <application>{application}</application>',
        '</DR_Module>',
    ]
    return "\n".join(xml_lines) + "\n"


def generate_functions(
    specs: List[Dict[str, Any]],
    activity_dir: Path,
    application: str,
    legacy_alias: bool = False,
    dry_run: bool = False,
) -> List[Dict[str, Any]]:
    """Generates function XML files in activity_dir/functions/."""
    out_dir = activity_dir / "functions"
    ext = ".fun" if legacy_alias else ".fnc"
    created = []

    for spec in specs:
        code = spec["code"]
        target_path = out_dir / f"{code}{ext}"

        if not dry_run:
            assert_file_writable(target_path, activity_path=activity_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            xml_content = generate_function_xml(spec, application)
            target_path.write_text(xml_content, encoding="utf-8")
            rel_path = target_path.relative_to(activity_dir).as_posix()
            try:
                add_component(activity_dir, rel_path)
            except Exception:
                pass

        created.append({
            "type": "function",
            "name": code,
            "path": str(target_path),
        })

    return created


def main():
    parser = argparse.ArgumentParser(description="Generate Infor LN Include Function (.fnc) XML component")
    parser.add_argument("--code", required=True, help="Function code (e.g. txcmgf001)")
    parser.add_argument("--desc", help="Description")
    parser.add_argument("--script-file", help="Path to plain .4gl/.src file containing function source")
    parser.add_argument("--legacy-alias", action="store_true", help="Generate with .fun extension instead of .fnc")
    parser.add_argument("--activity", help="Target activity folder")
    parser.add_argument("--project", default="EXTce01107", help="Software Project name")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    act_info = resolve_activity(activity_name=args.activity)
    act_dir = Path(act_info["path"])

    script_text = None
    if args.script_file:
        p = Path(args.script_file).resolve()
        if p.exists():
            script_text = p.read_text(encoding="utf-8")

    spec = {
        "code": args.code,
        "description": args.desc or args.code,
    }
    if script_text:
        spec["script"] = script_text

    files = generate_functions([spec], act_dir, args.project, legacy_alias=args.legacy_alias, dry_run=args.dry_run)
    print(f"[SUCCESS] Created function: {files[0]['path']}")


if __name__ == "__main__":
    main()
