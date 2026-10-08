#!/usr/bin/env python3
"""
tools/generate_ln_table.py
Infor LN Studio Table and Metadata XML Generator.

Generates production-grade .tbl, .lbl, and .dmn XML files matching Infor LN Studio 10.8
specifications from validated YAML/JSON schemas, and writes them into the target Activity folder.
"""

import os
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

# Ensure both repo root and tools folder are in sys.path
_current_dir = Path(__file__).resolve().parent
_repo_root = _current_dir.parent
for p in (str(_repo_root), str(_current_dir)):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from tools.ln_schema_parser import parse_schema_file
    from tools.ln_workspace_manager import resolve_activity, load_config
except ImportError:
    from ln_schema_parser import parse_schema_file
    from ln_workspace_manager import resolve_activity, load_config


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
    """Generates standard <DR_Domain> XML for enums or custom domains."""
    name = domain_spec["name"]
    desc = domain_spec["description"]
    c_time = "1970-01-01T00:00:00Z"
    native_dt = domain_spec.get("native_datatype", 7)

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

    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        f'<DR_Domain>'
        f'<description>{desc}</description>'
        f'<versionID>{version_id}</versionID>'
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
        f'<displayLength>20</displayLength>'
        f'<internalFormat/>'
        f'<conversion>4</conversion>'
        f'<alignment>5</alignment>'
        f'<application>{application}</application>'
        f'<datatype>'
        f'<Facet><value>20</value><type>totalDigits</type></Facet>'
        f'<nativeDatatype>{native_dt}</nativeDatatype>'
        f'</datatype>'
        f'</DR_Domain>'
    )
    return xml


def generate_table_xml(
    schema: Dict[str, Any],
    application: str,
    dal_code: Optional[str] = None
) -> str:
    """Generates standard Infor LN Studio 10.8 <DR_Table> XML."""
    tbl = schema["table"]
    name = tbl["code"]
    desc = tbl["description"]
    version_id = tbl["version_id"]
    now_iso = get_current_iso_time()

    # 1. Header & Version
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

    # 2. Attachments for table and fields
    parts.append(f'<Attachment><type>relnotes</type><name>{name}</name></Attachment>')
    parts.append(f'<Attachment><type>techdoc</type><name>{name}</name></Attachment>')
    for f in schema["fields"]:
        fname = f["name"]
        parts.append(f'<Attachment><type>relnotes</type><name>{name}.{fname}</name></Attachment>')
        parts.append(f'<Attachment><type>techdoc</type><name>{name}.{fname}</name></Attachment>')

    # 3. Indices
    for ind in schema["indices"]:
        idx_id = ind["id"]
        idx_desc = ind["description"]
        idx_label = ind["label_code"]
        is_pk = "true" if ind["primary_key"] else "false"
        is_unq = "true" if ind["unique"] else "false"
        is_act = "true" if ind["active"] else "false"

        idx_cols_xml = ""
        for col in ind["columns"]:
            s_order = col.get("sorting_order", col.get("sortingOrder", "asc"))
            idx_cols_xml += (
                f'<IndexColumn>'
                f'<sortingOrder>{s_order}</sortingOrder>'
                f'<column>{col["column"]}</column>'
                f'<position>{col["position"]}</position>'
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

    # 4. Table Relationships (Foreign Keys)
    for ref in schema["references"]:
        to_tbl = ref["to_table"]
        del_rule = ref["delete_rule"]
        upd_rule = ref["update_rule"]
        mult = ref["multiplicity"]
        rel_name = ref["name"]

        cols_xml = ""
        for cm in ref["columns"]:
            cols_xml += f'<TableRelationshipColumn><to>{cm["to"]}</to><from>{cm["from"]}</from></TableRelationshipColumn>'

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

    # 5. Columns
    for col in schema["fields"]:
        c_name = col["name"]
        c_desc = col["description"]
        c_label = col["label_code"]
        c_pos = col["position"]
        c_null = "true" if col["nullable"] else "false"
        c_mand = "true" if col["mandatory"] else "false"
        c_act = "true" if col["active"] else "false"
        c_dt_code = col["native_datatype"]
        c_domain = col["domain"]

        def_val_tag = f'<defaultValue>{col["default_value"]}</defaultValue>' if col["default_value"] else ""

        facets_xml = ""
        for f_type, f_val in col["facets"].items():
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

    # 6. Documentation
    parts.append('<documentation/>')

    # 7. Embedded DAL (<DR_Module>)
    # If no DAL code supplied, create a standard DAL2 starter skeleton
    if not dal_code:
        pkg = tbl["package"]
        tname = tbl["code"]
        dal_code = (
            f"|*******************************************************************************\n"
            f"|* {tname}  {version_id}\n"
            f"|* {desc}\n"
            f"|* Script Type: DAL\n"
            f"|*******************************************************************************\n\n"
            f"#include <bic_dal2>\n\n"
            f"table t{tname}\n\n"
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
            f"}}\n\n"
            f"function extern long before.save.object(long i.mode)\n"
            f"{{\n"
            f"\treturn(0)\n"
            f"}}\n\n"
            f"function extern long after.save.object(long i.mode)\n"
            f"{{\n"
            f"\treturn(0)\n"
            f"}}\n"
        )

    # XML Escape DAL code
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
        f'<sourceType>12</sourceType>'
        f'<sourceDescription>{desc}</sourceDescription>'
        f'<sourceName>{name}</sourceName>'
        f'</Source>'
        f'<documentation/>'
        f'<Attachment><type>relnotes</type><name>{name}</name></Attachment>'
        f'<Attachment><type>techdoc</type><name>{name}</name></Attachment>'
        f'<additionalConstraints>2522</additionalConstraints>'
        f'<additionalInstructions/>'
        f'<keyword>||</keyword>'
        f'<application>{application}</application>'
        f'</DR_Module>'
    )

    # 8. Closing Table Tag
    parts.append(f'<application>{application}</application>')
    parts.append('</DR_Table>')

    return "".join(parts)


def generate_all_components(
    schema_file: str,
    activity_name: Optional[str] = None,
    output_dir: Optional[str] = None,
    dry_run: bool = False
) -> List[Dict[str, str]]:
    """
    Parses schema, determines target paths, and generates table, labels, and domains.
    Returns list of generated file dictionaries: [{"type": "...", "path": "...", "name": "..."}].
    """
    schema = parse_schema_file(schema_file)
    tbl = schema["table"]
    pkg = tbl["package"]
    mod = tbl["module"]
    tcode = tbl["code"]
    desc = tbl["description"]
    ver = tbl["version_id"]

    target_root: Path
    app_code: str = tbl.get("application", "")

    if output_dir:
        target_root = Path(output_dir).resolve()
        if not app_code:
            app_code = "EXTce01105"
    elif activity_name:
        resolved = resolve_activity(activity_name)
        if not resolved:
            raise ValueError(f"Could not resolve activity: '{activity_name}'")
        target_root = Path(resolved["path"])
        app_code = resolved["project"]
    else:
        cfg = load_config()
        def_act = cfg.get("default_activity")
        if def_act:
            resolved = resolve_activity(def_act)
            if resolved:
                target_root = Path(resolved["path"])
                app_code = resolved["project"]
            else:
                target_root = Path.cwd() / "output"
                app_code = "EXTce01105"
        else:
            target_root = Path.cwd() / "output"
            app_code = "EXTce01105"

    generated_files = []

    # 1. Generate Table XML
    tbl_dir = target_root / pkg / "table" / mod
    tbl_path = tbl_dir / f"{tcode}.tbl"
    tbl_xml = generate_table_xml(schema, application=app_code)
    generated_files.append({
        "type": "table",
        "name": tcode,
        "path": str(tbl_path),
        "content": tbl_xml
    })

    # 2. Generate Label XMLs
    lbl_dir = target_root / pkg / "label"

    # Table description label
    lbl_tbl_path = lbl_dir / f"{tcode}.lbl"
    generated_files.append({
        "type": "label",
        "name": tcode,
        "path": str(lbl_tbl_path),
        "content": generate_label_xml(tcode, desc, ver, app_code)
    })

    # Field description labels
    for f in schema["fields"]:
        f_lbl_code = f["label_code"]
        f_lbl_path = lbl_dir / f"{f_lbl_code}.lbl"
        generated_files.append({
            "type": "label",
            "name": f_lbl_code,
            "path": str(f_lbl_path),
            "content": generate_label_xml(f_lbl_code, f["description"], ver, app_code)
        })

    # Index description labels
    for ind in schema["indices"]:
        i_lbl_code = ind["label_code"]
        i_lbl_path = lbl_dir / f"{i_lbl_code}.lbl"
        generated_files.append({
            "type": "label",
            "name": i_lbl_code,
            "path": str(i_lbl_path),
            "content": generate_label_xml(i_lbl_code, ind["description"], ver, app_code)
        })

    # 3. Generate Custom Domains
    dmn_dir = target_root / pkg / "domain"
    for dmn in schema.get("domains", []):
        d_name = dmn["name"]
        d_path = dmn_dir / f"{d_name}.dmn"
        generated_files.append({
            "type": "domain",
            "name": d_name,
            "path": str(d_path),
            "content": generate_domain_xml(dmn, ver, app_code)
        })

        # Labels for enum constants
        for en in dmn.get("enums", []):
            en_lbl = en["label_code"]
            en_path = lbl_dir / f"{en_lbl}.lbl"
            generated_files.append({
                "type": "label",
                "name": en_lbl,
                "path": str(en_path),
                "content": generate_label_xml(en_lbl, en["description"], ver, app_code)
            })

    # Write files if not dry-run
    if not dry_run:
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
    parser.add_argument("--output-dir", help="Direct target directory path (overrides activity)")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files to disk")

    args = parser.parse_args()

    try:
        files = generate_all_components(
            schema_file=args.spec,
            activity_name=args.activity,
            output_dir=args.output_dir,
            dry_run=args.dry_run
        )
        mode_str = "[DRY-RUN] Would generate" if args.dry_run else "[SUCCESS] Generated"
        print(f"{mode_str} {len(files)} component files:")
        for f in files:
            print(f"  ({f['type'].upper():<6}) {f['name']:<20} -> {f['path']}")
    except Exception as e:
        print(f"[ERROR] Generation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
