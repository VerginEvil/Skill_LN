#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_menu.py
Infor LN Studio Menu XML Generator.

Generates production-grade .mnu and associated label .lbl XML files matching
Infor LN Studio 10.8 specifications with ordered <MenuChoice> elements linking
to sessions or sub-menus, enforcing SCM Read-Only protection.
"""

import os
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Union

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_schema_parser import parse_schema_file
from generate_ln_table import generate_label_xml, get_current_iso_time
from ln_workspace_manager import resolve_activity, detect_current_activity
from scm_guardrails import assert_file_writable, ReadOnlyComponentError


def generate_menu_xml(
    menu_spec: Dict[str, Any],
    application: str
) -> str:
    """Generates standard <DR_Menu> .mnu XML."""
    code = menu_spec["code"]
    desc = menu_spec.get("description", code)
    ver = menu_spec.get("version_id", "B61O_a_ext")
    now_iso = get_current_iso_time()

    choices_xml = ""
    for ch in menu_spec.get("choices", []):
        ch_pos = ch.get("position", 10)
        ch_type = ch.get("type_code", 1 if ch.get("type") == "session" else 2)
        ch_target = ch.get("target", "")
        ch_desc = ch.get("description", ch_target)
        choices_xml += (
            f'<MenuChoice>'
            f'<descriptionReference/>'
            f'<description>{ch_desc}</description>'
            f'<initialHidden>false</initialHidden>'
            f'<filterFunction/><filterLibrary/>'
            f'<isActive>true</isActive>'
            f'<processInfo/>'
            f'<menuFieldName>{ch_target}</menuFieldName>'
            f'<menuFieldType>{ch_type}</menuFieldType>'
            f'<descriptionIsLinked>true</descriptionIsLinked>'
            f'<position>{ch_pos}</position>'
            f'</MenuChoice>'
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        f'<DR_Menu>'
        f'<description>{desc}</description>'
        f'<versionID>{ver}</versionID>'
        f'<type>menu</type>'
        f'<name>{code}</name>'
        f'<Version>'
        f'<ObjectID/><classID/><checkInLabel/><documentation/>'
        f'<isExpired>no</isExpired>'
        f'<isCheckedOutParallel>no</isCheckedOutParallel>'
        f'<isCheckedOut>no</isCheckedOut>'
        f'<modificationDateTime>{now_iso}</modificationDateTime>'
        f'<modifiedBy/>'
        f'<creationDateTime>{now_iso}</creationDateTime>'
        f'<createdBy>agent</createdBy>'
        f'</Version>'
        f'<descriptionReference>{code}</descriptionReference>'
        f'{choices_xml}'
        f'<Attachment><type>relnotes</type><name>{code}</name></Attachment>'
        f'<Attachment><type>techdoc</type><name>{code}</name></Attachment>'
        f'<documentation/>'
        f'<application>{application}</application>'
        f'</DR_Menu>'
    )
    return xml


def generate_menus(
    schema_file: Union[str, Path, Dict[str, Any]],
    menu_code: Optional[str] = None,
    activity_name: Optional[str] = None,
    output_dir: Optional[str] = None,
    workspace_name: Optional[str] = None,
    activity_path: Optional[str] = None,
    dry_run: bool = False
) -> List[Dict[str, str]]:
    """
    Generates .mnu and label .lbl files for declared menus in schema.
    """
    if isinstance(schema_file, dict):
        schema = schema_file
    else:
        schema = parse_schema_file(schema_file)

    ver = schema.get("version_id", "B61O_a_ext")
    app_code = schema.get("application", "")

    # Target directory resolution
    target_root: Path
    if output_dir:
        target_root = Path(output_dir).resolve()
        if not app_code:
            app_code = "EXTce01105"
    elif activity_path or activity_name:
        resolved = resolve_activity(activity_name, workspace_name=workspace_name, activity_path=activity_path)
        if not resolved:
            raise ValueError(f"Could not resolve activity: '{activity_path or activity_name}'")
        target_root = Path(resolved["path"])
        if not app_code:
            app_code = resolved["project"]
    else:
        detected = detect_current_activity()
        if detected:
            target_root = Path(detected["path"])
            if not app_code:
                app_code = detected["project"]
        elif dry_run:
            target_root = Path.cwd() / "output"
            if not app_code:
                app_code = "EXTce01105"
        else:
            raise ValueError("Explicit --activity, --activity-path, or --output-dir required to generate menus.")

    menus_to_gen = schema.get("menus", [])
    if menu_code:
        menus_to_gen = [m for m in menus_to_gen if m["code"].lower() == menu_code.lower()]
        if not menus_to_gen:
            raise ValueError(f"Menu '{menu_code}' not found in schema.")

    generated = []
    for mnu in menus_to_gen:
        code = mnu["code"]
        pkg = code[:2]
        mod = mnu.get("module", code[2:5] if len(code) >= 5 else "gen")
        desc = mnu.get("description", code)

        mnu_dir = target_root / pkg / "menu" / mod
        mnu_path = mnu_dir / f"{code}.mnu"
        xml_content = generate_menu_xml(mnu, application=app_code)
        generated.append({
            "type": "menu",
            "name": code,
            "path": str(mnu_path),
            "content": xml_content
        })

        lbl_dir = target_root / pkg / "label"
        lbl_path = lbl_dir / f"{code}.lbl"
        lbl_xml = generate_label_xml(code, desc, ver, app_code)
        generated.append({
            "type": "label",
            "name": code,
            "path": str(lbl_path),
            "content": lbl_xml
        })

    if not dry_run:
        for item in generated:
            p = Path(item["path"])
            assert_file_writable(p, target_root)

        for item in generated:
            p = Path(item["path"])
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(item["content"])

    return generated


def main():
    parser = argparse.ArgumentParser(description="Generate Infor LN Menu XML (.mnu) from Schema")
    parser.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    parser.add_argument("--code", help="Specific menu code to generate")
    parser.add_argument("--activity", help="Target activity folder name or activity code")
    parser.add_argument("--activity-path", help="Direct activity directory path")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--output-dir", help="Direct target directory path (overrides activity)")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files to disk")

    args = parser.parse_args()

    try:
        files = generate_menus(
            schema_file=args.spec,
            menu_code=args.code,
            activity_name=args.activity,
            activity_path=args.activity_path,
            workspace_name=args.workspace,
            output_dir=args.output_dir,
            dry_run=args.dry_run
        )
        mode_str = "[DRY-RUN] Would generate" if args.dry_run else "[SUCCESS] Generated"
        print(f"{mode_str} {len(files)} menu file(s):")
        for f in files:
            print(f"  ({f['type'].upper():<6}) {f['name']:<20} -> {f['path']}")
    except ReadOnlyComponentError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Menu generation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
