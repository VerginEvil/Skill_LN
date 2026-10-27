#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_additional.py
Infor LN Studio Additional File Component Generator.

Generates production-grade .add XML files matching Infor LN Studio 10.8 <DR_AdditionalFile> specifications.
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


def generate_additional_xml(spec: Dict[str, Any], application: str) -> str:
    """Generates standard <DR_AdditionalFile> .add XML."""
    code = spec["code"]
    desc = spec.get("description", code)
    ver = spec.get("version_id", "B61O_a_ext")
    content = spec.get("content", "")
    kw1 = spec.get("keyword1", "")
    kw2 = spec.get("keyword2", "")
    kw3 = spec.get("keyword3", "")

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        '<DR_AdditionalFile xmlns="http://www.infor.com/businessline/application/dr" version="1.0">',
        f'  <description>{desc}</description>',
        f'  <versionID>{ver}</versionID>',
        '  <type>additional</type>',
        f'  <name>{code}</name>',
        '  <isEditable>true</isEditable>',
        f'  <keyword1>{kw1}</keyword1>',
        f'  <keyword2>{kw2}</keyword2>',
        f'  <keyword3>{kw3}</keyword3>',
        '  <includeContent>true</includeContent>',
        '  <FileContent>',
        f'    <content><![CDATA[{content}]]></content>',
        '  </FileContent>',
        f'  <application>{application}</application>',
        '</DR_AdditionalFile>',
    ]
    return "\n".join(xml_lines) + "\n"


def generate_additionals(
    specs: List[Dict[str, Any]],
    activity_dir: Path,
    application: str,
    dry_run: bool = False,
) -> List[Dict[str, Any]]:
    """Generates additional file XML in activity_dir/additional_files/."""
    out_dir = activity_dir / "additional_files"
    created = []

    for spec in specs:
        code = spec["code"]
        target_path = out_dir / f"{code}.add"

        if not dry_run:
            assert_file_writable(target_path, activity_path=activity_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            xml_content = generate_additional_xml(spec, application)
            target_path.write_text(xml_content, encoding="utf-8")
            rel_path = target_path.relative_to(activity_dir).as_posix()
            try:
                add_component(activity_dir, rel_path)
            except Exception:
                pass

        created.append({
            "type": "additional",
            "name": code,
            "path": str(target_path),
        })

    return created


def main():
    parser = argparse.ArgumentParser(description="Generate Infor LN Additional File (.add) XML component")
    parser.add_argument("--code", required=True, help="Additional file code (e.g. txcmgcfg)")
    parser.add_argument("--desc", help="Description")
    parser.add_argument("--content-file", help="Path to payload file (JSON, XML, text, etc.)")
    parser.add_argument("--keyword1", help="Keyword 1")
    parser.add_argument("--keyword2", help="Keyword 2")
    parser.add_argument("--keyword3", help="Keyword 3")
    parser.add_argument("--activity", help="Target activity folder")
    parser.add_argument("--project", default="EXTce01107", help="Software Project name")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    act_info = resolve_activity(activity_name=args.activity)
    act_dir = Path(act_info["path"])

    content = ""
    if args.content_file:
        p = Path(args.content_file).resolve()
        if p.exists():
            content = p.read_text(encoding="utf-8")

    spec = {
        "code": args.code,
        "description": args.desc or args.code,
        "content": content,
        "keyword1": args.keyword1 or "",
        "keyword2": args.keyword2 or "",
        "keyword3": args.keyword3 or "",
    }
    files = generate_additionals([spec], act_dir, args.project, dry_run=args.dry_run)
    print(f"[SUCCESS] Created additional file: {files[0]['path']}")


if __name__ == "__main__":
    main()
