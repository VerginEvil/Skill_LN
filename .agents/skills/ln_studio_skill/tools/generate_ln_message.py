#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_message.py
Infor LN Studio Message Component Generator.

Generates production-grade .msg XML files matching Infor LN Studio 10.8 <DR_Message> specifications.
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


def generate_message_xml(spec: Dict[str, Any], application: str) -> str:
    """Generates standard <DR_Message> .msg XML."""
    code = spec["code"]
    desc = spec.get("description", code)
    severity = str(spec.get("severity", "3"))  # 1 = Info, 2 = Warning, 3 = Error
    text = spec.get("text", desc)
    ver = spec.get("version_id", "B61O_a_ext")

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        '<DR_Message xmlns="http://www.infor.com/businessline/application/dr" version="1.0">',
        f'  <description>{desc}</description>',
        f'  <versionID>{ver}</versionID>',
        '  <type>message</type>',
        f'  <name>{code}</name>',
        f'  <severity>{severity}</severity>',
        '  <hasHelp>false</hasHelp>',
        '  <MessageTranslation>',
        '    <language>2</language>',
        f'    <text>{text}</text>',
        '  </MessageTranslation>',
        f'  <application>{application}</application>',
        '</DR_Message>',
    ]
    return "\n".join(xml_lines) + "\n"


def generate_messages(
    specs: List[Dict[str, Any]],
    activity_dir: Path,
    application: str,
    dry_run: bool = False,
) -> List[Dict[str, Any]]:
    """Generates message XML files in activity_dir/messages/."""
    out_dir = activity_dir / "messages"
    created = []

    for spec in specs:
        code = spec["code"]
        target_path = out_dir / f"{code}.msg"

        if not dry_run:
            assert_file_writable(target_path, activity_path=activity_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            xml_content = generate_message_xml(spec, application)
            target_path.write_text(xml_content, encoding="utf-8")
            rel_path = target_path.relative_to(activity_dir).as_posix()
            try:
                add_component(activity_dir, rel_path)
            except Exception:
                pass

        created.append({
            "type": "message",
            "name": code,
            "path": str(target_path),
        })

    return created


def main():
    parser = argparse.ArgumentParser(description="Generate Infor LN Message (.msg) XML component")
    parser.add_argument("--code", required=True, help="Message code (e.g. txcmg0001)")
    parser.add_argument("--desc", help="Description")
    parser.add_argument("--severity", choices=["1", "2", "3"], default="3", help="1=Info, 2=Warning, 3=Error")
    parser.add_argument("--text", help="Message text")
    parser.add_argument("--activity", help="Target activity folder")
    parser.add_argument("--project", default="EXTce01107", help="Software Project name")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    act_info = resolve_activity(activity_name=args.activity)
    act_dir = Path(act_info["path"])

    spec = {
        "code": args.code,
        "description": args.desc or args.code,
        "severity": args.severity,
        "text": args.text or args.desc or args.code,
    }
    files = generate_messages([spec], act_dir, args.project, dry_run=args.dry_run)
    print(f"[SUCCESS] Created message: {files[0]['path']}")


if __name__ == "__main__":
    main()
