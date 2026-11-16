#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_domain.py
Infor LN Studio Standalone Domain XML Generator.

Generates production-grade .dmn and associated constant .lbl XML files
for all LN Studio native datatypes (Enum, String, Integer, Amount, Date, UTC).
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

from ln_schema_parser import parse_schema_file
from ln_workspace_manager import resolve_activity, detect_current_activity
from scm_guardrails import assert_file_writable, ReadOnlyComponentError
from generate_ln_table import generate_domain_xml, generate_label_xml


def generate_domains(
    schema_file: Union[str, Path, Dict[str, Any]],
    domain_name: Optional[str] = None,
    activity_name: Optional[str] = None,
    output_dir: Optional[str] = None,
    workspace_name: Optional[str] = None,
    activity_path: Optional[str] = None,
    dry_run: bool = False
) -> List[Dict[str, str]]:
    """
    Generates .dmn and constant .lbl files for declared domains.
    """
    if isinstance(schema_file, dict):
        schema = schema_file
    else:
        schema = parse_schema_file(schema_file)

    ver = schema.get("version_id", "B61O_a_ext")
    app_code = schema.get("application", "")

    # Resolve target directory
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
            raise ValueError("Explicit --activity, --activity-path, or --output-dir required to generate domains.")

    domains_to_generate = schema.get("domains", [])
    if domain_name:
        domains_to_generate = [d for d in domains_to_generate if d["name"].lower() == domain_name.lower()]
        if not domains_to_generate:
            raise ValueError(f"Domain '{domain_name}' not found in schema.")

    generated_files = []
    for dmn in domains_to_generate:
        d_name = dmn["name"]
        pkg = dmn.get("package") or (d_name[:2] if len(d_name) >= 2 else "tx")
        dmn_dir = target_root / pkg / "domain"
        d_path = dmn_dir / f"{d_name}.dmn"
        generated_files.append({
            "type": "domain",
            "name": d_name,
            "path": str(d_path),
            "content": generate_domain_xml(dmn, ver, app_code)
        })

        lbl_dir = target_root / pkg / "label"
        for en in dmn.get("enums", []):
            en_lbl = en["label_code"]
            en_path = lbl_dir / f"{en_lbl}.lbl"
            generated_files.append({
                "type": "label",
                "name": en_lbl,
                "path": str(en_path),
                "content": generate_label_xml(en_lbl, en["description"], ver, app_code)
            })

    if not dry_run:
        for item in generated_files:
            p = Path(item["path"])
            assert_file_writable(p, target_root)

        for item in generated_files:
            p = Path(item["path"])
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(item["content"])

    return generated_files


def main():
    parser = argparse.ArgumentParser(description="Generate Infor LN Domain and Label XML from Schema")
    parser.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    parser.add_argument("--name", help="Specific domain name to generate")
    parser.add_argument("--activity", help="Target activity folder name or activity code")
    parser.add_argument("--activity-path", help="Direct activity directory path")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--output-dir", help="Direct target directory path (overrides activity)")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files to disk")

    args = parser.parse_args()

    try:
        files = generate_domains(
            schema_file=args.spec,
            domain_name=args.name,
            activity_name=args.activity,
            activity_path=args.activity_path,
            workspace_name=args.workspace,
            output_dir=args.output_dir,
            dry_run=args.dry_run
        )
        mode_str = "[DRY-RUN] Would generate" if args.dry_run else "[SUCCESS] Generated"
        print(f"{mode_str} {len(files)} domain file(s):")
        for f in files:
            print(f"  ({f['type'].upper():<6}) {f['name']:<20} -> {f['path']}")
    except ReadOnlyComponentError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Domain generation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
