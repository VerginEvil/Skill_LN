#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_table.py
Infor LN Studio Table, Label, and Domain XML Generator.

Generates production-grade .tbl, .lbl, and .dmn XML files matching Infor LN Studio 10.8
specifications from validated schemas, enforcing SCM Read-Only protection and workbench conventions.
"""

import os
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_schema_parser import parse_schema_file
from ln_workspace_manager import resolve_activity, load_config, detect_current_activity
from scm_guardrails import assert_file_writable, ReadOnlyComponentError


def get_current_iso_time() -> str:
    """Returns current UTC ISO-8601 timestamp."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def generate_label_xml(
    name: str,
    description: str,
    version_id: str,
    application: str,
    length: Optional[int] = None,
    created_time: Optional[str] = None
) -> str:
    """Generates standard <DR_Label> XML."""
    c_time = created_time or "1970-01-01T00:00:00Z"
    lbl_len = length if length is not None else max(len(description), 1)
    keyword = description[:14].upper().strip()

    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        f'<DR_Label>'
        f'<description>{description}</description>'
        f'<versionID>{version_id}</versionID>'
        f'<type>label</type>'
        f'<name>{name}</name>'
        f'<Version>'
        f'<ObjectID/><classID/><checkInLabel/><documentation/>'
        f'<isExpired>no</isExpired>'
        f'<isCheckedOutParallel>no</isCheckedOutParallel>'
        f'<isCheckedOut>no</isCheckedOut>'
        f'<modificationDateTime>{c_time}</modificationDateTime>'
        f'<modifiedBy/>'
        f'<creationDateTime>{c_time}</creationDateTime>'
        f'<createdBy/>'
        f'</Version>'
        f'<Attachment><type>techdoc</type><name>{name}</name></Attachment>'
        f'<LabelVariant>'
        f'<keyword>{keyword}</keyword>'
        f'<isActive>1</isActive>'
        f'<description>{description}</description>'
        f'<height>1</height>'
        f'<length>{lbl_len}</length>'
        f'<context>3</context>'
        f'<language>2</language>'
        f'</LabelVariant>'
        f'<application>{application}</application>'
        f'</DR_Label>'
    )
    return xml


def generate_domain_xml(
    domain_spec: Dict[str, Any],
    version_id: str,
    application: str
) -> str:
    """Generates standard <DR_Domain> XML for all native datatypes."""
    name = domain_spec["name"]
    desc = domain_spec["description"]
    c_time = "1970-01-01T00:00:00Z"
    native_dt = domain_spec.get("native_datatype", 7)
    disp_len = domain_spec.get("display_length", 20)
    ver = domain_spec.get("version_id", version_id)
    app = domain_spec.get("application", application)

    enums_xml = ""
    for enum_item in domain_spec.get("enums", []):
        e_name = enum_item["name"]
        e_desc = enum_item["description"]
        e_pos = enum_item["position"]
        e_ref = enum_item.get("label_code", f"{name}{e_pos:03d}")
        enums_xml += (
            f'<Enumeration>'
            f'<descriptionReference>{e_ref}</descriptionReference>'
            f'<description>{e_desc}</description>'
            f'<name>{e_name}</name>'
            f'<position>{e_pos}</position>'
            f'</Enumeration>'
        )

    facets = domain_spec.get("facets", {})
    facets_xml = ""
    if native_dt == 7:  # Enum
        tot_digits = facets.get("totalDigits", str(disp_len))
        facets_xml = f'<Facet><value>{tot_digits}</value><type>totalDigits</type></Facet>'
    elif native_dt in (3, 5):  # Integer or Amount
        tot_digits = facets.get("totalDigits", facets.get("maxLength", str(disp_len)))
        facets_xml = f'<Facet><value>{tot_digits}</value><type>totalDigits</type></Facet>'
        if native_dt == 5:
            facets_xml += '<Facet><value>2</value><type>fractionDigits</type></Facet>'
    else:  # String, Date, etc.
        max_len = facets.get("maxLength", str(disp_len))
        min_len = facets.get("minLength", "1")
        facets_xml = f'<Facet><value>{max_len}</value><type>maxLength</type></Facet><Facet><value>{min_len}</value><type>minLength</type></Facet>'

    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        f'<DR_Domain>'
        f'<description>{desc}</description>'
        f'<versionID>{ver}</versionID>'
        f'<type>domain</type>'
        f'<name>{name}</name>'
        f'<Version>'
        f'<ObjectID/><classID/><checkInLabel/><documentation/>'
        f'<isExpired>no</isExpired>'
        f'<isCheckedOutParallel>no</isCheckedOutParallel>'
        f'<isCheckedOut>no</isCheckedOut>'
        f'<modificationDateTime>{c_time}</modificationDateTime>'
        f'<modifiedBy/>'
        f'<creationDateTime>{c_time}</creationDateTime>'
        f'<createdBy/>'
        f'</Version>'
        f'<documentation/>'
        f'<Attachment><type>relnotes</type><name>{name}</name></Attachment>'
        f'<Attachment><type>techdoc</type><name>{name}</name></Attachment>'
        f'{enums_xml}'
        f'<rangeMessage/><range/><displayFormat/>'
        f'<roundingMethod>4</roundingMethod>'
        f'<divideFactor>0</divideFactor>'
        f'<displayLength>{disp_len}</displayLength>'
        f'<internalFormat/>'
        f'<conversion>4</conversion>'
        f'<alignment>5</alignment>'
        f'<application>{app}</application>'
        f'<datatype>'
        f'{facets_xml}'
        f'<nativeDatatype>{native_dt}</nativeDatatype>'
        f'</datatype>'
        f'</DR_Domain>'
    )
    return xml


def generate_table_xml(
    table_spec: Dict[str, Any],
    application: str,
    dal_code: Optional[str] = None
) -> str:
    """Generates standard Infor LN Studio 10.8 <DR_Table> XML."""
    name = table_spec["code"]
    desc = table_spec["description"]
    version_id = table_spec["version_id"]
    pkg = table_spec["package"]
    now_iso = get_current_iso_time()

    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        '<DR_Table>',
        f'<description>{desc}</description>',
        f'<versionID>{version_id}</versionID>',
        '<type>table</type>',
        f'<name>{name}</name>',
        '<Version>',
        '<ObjectID/><classID/><checkInLabel/><documentation/>',
        '<isExpired>no</isExpired>',
        '<isCheckedOutParallel>no</isCheckedOutParallel>',
        '<isCheckedOut>no</isCheckedOut>',
        f'<modificationDateTime>{now_iso}</modificationDateTime>',
        '<modifiedBy>agent</modifiedBy>',
        f'<creationDateTime>{now_iso}</creationDateTime>',
        '<createdBy>agent</createdBy>',
        '</Version>',
        f'<descriptionReference>{name}</descriptionReference>',
    ]

    # Attachments
    parts.append(f'<Attachment><type>relnotes</type><name>{name}</name></Attachment>')
    parts.append(f'<Attachment><type>techdoc</type><name>{name}</name></Attachment>')
    for f in table_spec["fields"]:
        fname = f["name"]
        parts.append(f'<Attachment><type>relnotes</type><name>{name}.{fname}</name></Attachment>')
        parts.append(f'<Attachment><type>techdoc</type><name>{name}.{fname}</name></Attachment>')

    # Indices
    for ind in table_spec.get("indices", []):
        idx_id = ind["id"]
        idx_desc = ind["description"]
        idx_label = ind["label_code"]
        is_pk = "true" if ind.get("primary_key") else "false"
        is_unq = "true" if ind.get("unique") else "false"
        is_act = "true" if ind.get("active", True) else "false"

        idx_cols_xml = ""
        for c_pos, col in enumerate(ind["columns"], start=1):
            c_name = col if isinstance(col, str) else col.get("column", "")
            s_order = "asc" if isinstance(col, str) else col.get("sorting_order", "asc")
            idx_cols_xml += (
                f'<IndexColumn>'
                f'<sortingOrder>{s_order}</sortingOrder>'
                f'<column>{c_name}</column>'
                f'<position>{c_pos}</position>'
                f'</IndexColumn>'
            )

        parts.append(
            f'<Index>'
            f'<descriptionReference>{idx_label}</descriptionReference>'
            f'<description>{idx_desc}</description>'
            f'{idx_cols_xml}'
            f'<isActive>{is_act}</isActive>'
            f'<isPrimaryKey>{is_pk}</isPrimaryKey>'
            f'<isUnique>{is_unq}</isUnique>'
            f'<name>{idx_id}</name>'
            f'</Index>'
        )

    # Table Relationships
    for ref in table_spec.get("references", []):
        to_tbl = ref.get("reference_table", ref.get("to_table", ""))
        del_rule = ref.get("delete_rule", "not_delete_restricted")
        upd_rule = ref.get("update_rule", "restrict")
        mult = ref.get("multiplicity", "one_to_many")
        rel_name = ref.get("name", f"ref_{to_tbl}")

        cols_xml = ""
        from_cols = ref.get("from_columns", [])
        to_cols = ref.get("to_columns", [])
        for f_col, t_col in zip(from_cols, to_cols):
            cols_xml += f'<TableRelationshipColumn><to>{t_col}</to><from>{f_col}</from></TableRelationshipColumn>'

        parts.append(
            f'<TableRelationship>'
            f'<companyField/>'
            f'<toTable>{to_tbl}</toTable>'
            f'{cols_xml}'
            f'<deleteRule>{del_rule}</deleteRule>'
            f'<updateRule>{upd_rule}</updateRule>'
            f'<referentialIntegrityCheck>true</referentialIntegrityCheck>'
            f'<multiplicity>{mult}</multiplicity>'
            f'<type>association</type>'
            f'<name>{rel_name}</name>'
            f'</TableRelationship>'
        )

    # Columns
    for col in table_spec["fields"]:
        c_name = col["name"]
        c_desc = col["description"]
        c_label = col["label_code"]
        c_pos = col["position"]
        c_null = "true" if col.get("nullable") else "false"
        c_mand = "true" if col.get("mandatory") else "false"
        c_act = "true" if col.get("active", True) else "false"
        c_dt_code = col["native_datatype"]
        c_domain = col["domain"]

        def_val_tag = f'<defaultValue>{col["default_value"]}</defaultValue>' if col.get("default_value") else ""

        facets_xml = ""
        for f_type, f_val in col.get("facets", {}).items():
            facets_xml += f'<Facet><value>{f_val}</value><type>{f_type}</type></Facet>'

        parts.append(
            f'<Column>'
            f'<descriptionReference>{c_label}</descriptionReference>'
            f'<description>{c_desc}</description>'
            f'<additionalInstructions>columnDepth:0</additionalInstructions>'
            f'<isNullable>{c_null}</isNullable>'
            f'<isActive>{c_act}</isActive>'
            f'<isMandatory>{c_mand}</isMandatory>'
            f'{def_val_tag}'
            f'<position>{c_pos}</position>'
            f'<datatype>'
            f'{facets_xml}'
            f'<nativeDatatype>{c_dt_code}</nativeDatatype>'
            f'<name>{c_domain}</name>'
            f'</datatype>'
            f'<type>simple</type>'
            f'<name>{c_name}</name>'
            f'</Column>'
        )

    # Documentation & Application
    parts.append('<documentation/>')

    # Embedded DAL
    if not dal_code:
        dal_code = (
            f"|*******************************************************************************\n"
            f"|* {name}  {version_id}\n"
            f"|* {desc}\n"
            f"|* Script Type: DAL\n"
            f"|*******************************************************************************\n\n"
            f"#include <bic_dal2>\n\n"
            f"table t{name}\n\n"
            f"function extern boolean method.is.allowed(long i.method)\n"
            f"{{\n"
            f"\ton case i.method\n"
            f"\tcase DAL_NEW:\n"
            f"\t\tbreak\n"
            f"\tcase DAL_UPDATE:\n"
            f"\t\tbreak\n"
            f"\tcase DAL_DESTROY:\n"
            f"\t\tbreak\n"
            f"\tendcase\n"
            f"\treturn(true)\n"
            f"}}\n"
        )

    escaped_dal = (
        dal_code.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    parts.append(
        f'<DR_Module>'
        f'<description>{desc}</description>'
        f'<versionID>{version_id}</versionID>'
        f'<type>library</type>'
        f'<name>{name}</name>'
        f'<Version>'
        f'<ObjectID/><classID/><checkInLabel/><documentation/>'
        f'<isExpired>no</isExpired>'
        f'<isCheckedOutParallel>no</isCheckedOutParallel>'
        f'<isCheckedOut>no</isCheckedOut>'
        f'<modificationDateTime>{now_iso}</modificationDateTime>'
        f'<modifiedBy>agent</modifiedBy>'
        f'<creationDateTime>{now_iso}</creationDateTime>'
        f'<createdBy>agent</createdBy>'
        f'</Version>'
        f'<Source>'
        f'<sourceVersion>'
        f'<ObjectID/><classID/><checkInLabel/><documentation/>'
        f'<isExpired>no</isExpired>'
        f'<isCheckedOutParallel>no</isCheckedOutParallel>'
        f'<isCheckedOut>no</isCheckedOut>'
        f'<modificationDateTime>{now_iso}</modificationDateTime>'
        f'<modifiedBy>agent</modifiedBy>'
        f'<creationDateTime>{now_iso}</creationDateTime>'
        f'<createdBy>agent</createdBy>'
        f'</sourceVersion>'
        f'<sourceVersionID>{version_id}</sourceVersionID>'
        f'<sourceObjectID>1</sourceObjectID>'
        f'<expression>{escaped_dal}</expression>'
        f'<expressionLanguageType>Baan4C</expressionLanguageType>'
        f'<sourceType>2</sourceType>'
        f'<sourceDescription>{desc}</sourceDescription>'
        f'<sourceName>{name}</sourceName>'
        f'</Source>'
        f'<documentation/>'
        f'<Attachment><type>techdoc</type><name>{name}</name></Attachment>'
        f'<application>{application}</application>'
        f'</DR_Module>'
    )

    parts.append(f'<application>{application}</application>')
    parts.append('</DR_Table>')

    return "".join(parts)


def generate_all_components(
    schema_file: Union[str, Path, Dict[str, Any]],
    activity_name: Optional[str] = None,
    output_dir: Optional[str] = None,
    workspace_name: Optional[str] = None,
    activity_path: Optional[str] = None,
    dry_run: bool = False
) -> List[Dict[str, str]]:
    """
    Generates all table, domain, and label components declared in schema.
    Validates SCM Read-Only protection before writing to disk.
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
            raise ValueError("Explicit --activity, --activity-path, or --output-dir required to generate components.")

    generated_files = []
    tables = schema.get("tables", [])
    if not tables and "table" in schema and schema["table"]:
        tables = [schema["table"]]

    # 1. Generate Tables and their Labels
    for tbl in tables:
        tcode = tbl["code"]
        pkg = tbl["package"]
        mod = tbl["module"]
        desc = tbl["description"]
        tbl_ver = tbl.get("version_id", ver)
        tbl_app = tbl.get("application", app_code)

        tbl_dir = target_root / pkg / "table" / mod
        tbl_path = tbl_dir / f"{tcode}.tbl"
        tbl_xml = generate_table_xml(tbl, application=tbl_app)
        generated_files.append({
            "type": "table",
            "name": tcode,
            "path": str(tbl_path),
            "content": tbl_xml
        })

        lbl_dir = target_root / pkg / "label"

        # Table description label
        lbl_tbl_path = lbl_dir / f"{tcode}.lbl"
        generated_files.append({
            "type": "label",
            "name": tcode,
            "path": str(lbl_tbl_path),
            "content": generate_label_xml(tcode, desc, tbl_ver, tbl_app)
        })

        # Field description labels (convention: <pkg><table_code>.<column>)
        for f in tbl["fields"]:
            f_lbl_code = f["label_code"]
            f_lbl_path = lbl_dir / f"{f_lbl_code}.lbl"
            generated_files.append({
                "type": "label",
                "name": f_lbl_code,
                "path": str(f_lbl_path),
                "content": generate_label_xml(f_lbl_code, f["description"], tbl_ver, tbl_app)
            })

        # Index description labels
        for ind in tbl.get("indices", []):
            i_lbl_code = ind["label_code"]
            i_lbl_path = lbl_dir / f"{i_lbl_code}.lbl"
            generated_files.append({
                "type": "label",
                "name": i_lbl_code,
                "path": str(i_lbl_path),
                "content": generate_label_xml(i_lbl_code, ind["description"], tbl_ver, tbl_app)
            })

    # 2. Generate Domains
    for dmn in schema.get("domains", []):
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

        # Labels for enum constants
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

    # Write files if not dry-run, enforcing Read-Only check first
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
    parser = argparse.ArgumentParser(description="Generate Infor LN Table, Labels, and Domains from Schema")
    parser.add_argument("--spec", required=True, help="Path to schema YAML/JSON file")
    parser.add_argument("--activity", help="Target activity folder name or activity code")
    parser.add_argument("--activity-path", help="Direct activity directory path")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--output-dir", help="Direct target directory path (overrides activity)")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files to disk")

    args = parser.parse_args()

    try:
        files = generate_all_components(
            schema_file=args.spec,
            activity_name=args.activity,
            activity_path=args.activity_path,
            workspace_name=args.workspace,
            output_dir=args.output_dir,
            dry_run=args.dry_run
        )
        mode_str = "[DRY-RUN] Would generate" if args.dry_run else "[SUCCESS] Generated"
        print(f"{mode_str} {len(files)} component files:")
        for f in files:
            print(f"  ({f['type'].upper():<6}) {f['name']:<20} -> {f['path']}")
    except ReadOnlyComponentError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Generation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
