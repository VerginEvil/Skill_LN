#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_report.py
Infor LN Studio Report Component Generator.

Generates production-grade .rpt (and .rptdsrc) XML files matching Infor LN Studio 10.8 <DR_Report> specifications.
Supports input fields, sort modes, physical layouts (header, detail, footer),
specials (date, page, time, company, user, label), and 4GL report scripts.
Registers components in .admin and enforces SCM protection.
"""

import os
import sys
import base64
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
from ln_schema_parser import DATA_TYPE_MAP, STANDARD_DOMAINS


# Base64 encoded empty 80-column layout text grid
DEFAULT_80COL_GRID_BASE64 = (
    "AQgBjDoBEwGMWwEZAYwsAR4BjF0BSwGMOgJLAYs6/yAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg"
    "ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg"
    "ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg"
    "ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA="
)


def _resolve_native_datatype(domain: str) -> int:
    """Infers nativeDatatype from domain or defaults to 6 (String)."""
    if domain in STANDARD_DOMAINS:
        return STANDARD_DOMAINS[domain]["nativeDatatype"]
    if "date" in domain:
        return 9
    if "utc" in domain:
        return 14
    if "long" in domain or "pono" in domain or "btno" in domain:
        return 3
    if "amnt" in domain or "wght" in domain or "leng" in domain:
        return 5
    if "bool" in domain or "yesno" in domain:
        return 7
    return 6


def generate_report_xml(spec: Dict[str, Any], application: str) -> str:
    """Generates standard <DR_Report> XML matching Infor LN Studio 10.8."""
    code = spec["code"]
    desc = spec.get("description", code)
    ver = spec.get("version_id", "B61O_a_ext")
    paper_width = int(spec.get("paper_width", 80))
    script = spec.get("script", "")

    lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        '<DR_Report xmlns="http://www.infor.com/businessline/application/dr" version="1.0">',
        f'  <description>{desc}</description>',
        f'  <versionID>{ver}</versionID>',
        '  <type>report</type>',
        f'  <name>{code}</name>',
        '  <Version>',
        '    <ObjectID/><classID/><checkInLabel/><documentation/>',
        '    <isExpired>no</isExpired>',
        '    <isCheckedOutParallel>no</isCheckedOutParallel>',
        '    <isCheckedOut>no</isCheckedOut>',
        '  </Version>',
        f'  <descriptionReference>{code}</descriptionReference>',
        '  <SSRSDesignPresent>false</SSRSDesignPresent>',
    ]

    # Input Fields
    input_fields = spec.get("input_fields", [])
    if not input_fields:
        # Default starter field
        input_fields = [{"fieldname": "dummy", "domain": "tcmcs.long"}]

    for idx, f in enumerate(input_fields, start=1):
        fname = f.get("fieldname") or f.get("name") or f"field_{idx}"
        dom = f.get("domain", "tcdsca")
        native_dt = f.get("nativeDatatype") or _resolve_native_datatype(dom)
        is_tbl = "yes" if f.get("is_table_field", False) else "no"
        sort_seq = f.get("sort_sequence", 99)
        sort_mode = f.get("sort_mode", 1)  # 1 = asc, 2 = desc, 4 = none
        label_ref = f.get("label", "")

        lines.extend([
            '  <InputField>',
            f'    <label>{label_ref}</label>',
            f'    <nativeDatatype>{native_dt}</nativeDatatype>',
            f'    <isTableField>{is_tbl}</isTableField>',
            f'    <sortSequence>{sort_seq}</sortSequence>',
            f'    <sortMode>{sort_mode}</sortMode>',
            f'    <domain>{dom}</domain>',
            '    <depth>0</depth>',
            f'    <fieldname>{fname}</fieldname>',
            '  </InputField>',
        ])

    # Layouts
    layouts = spec.get("layouts", [])
    if not layouts:
        # Default header and detail layouts
        layouts = [
            {"type": 2, "rows": 2, "columns": paper_width, "specials": [{"type": 8, "label": "tcgen.h.date", "row": 1, "col": 1, "len": 10}, {"type": 8, "label": "tcgen.page", "row": 1, "col": 65, "len": 10}]},
            {"type": 4, "rows": 2, "columns": paper_width, "output_fields": [{"print_expression": input_fields[0]["fieldname"], "domain": input_fields[0].get("domain", "tcdsca"), "row": 1, "col": 1, "len": 30}]},
        ]

    for seq, lay in enumerate(layouts, start=1):
        l_type = lay.get("type", 4)  # 2 = page_header, 4 = detail, 6 = footer
        rows = lay.get("rows", 2)
        cols = lay.get("columns", paper_width)
        out_expr = lay.get("output_expression", "1")

        lines.extend([
            '  <Layout>',
            '    <PhysicalReportLayout>',
            '      <ReportLayoutText>',
            f'        <content>{DEFAULT_80COL_GRID_BASE64}</content>',
            '        <position>1</position>',
            '      </ReportLayoutText>',
        ])

        # Output fields in layout
        for of_pos, of in enumerate(lay.get("output_fields", []), start=1):
            expr = of.get("print_expression") or of.get("expression") or ""
            dom = of.get("domain", "tcdsca")
            row = of.get("row", 1)
            col = of.get("col", 1)
            plen = of.get("len", 30)

            lines.extend([
                '      <ReportOutputField>',
                '        <barCode>0</barCode><font>0</font><maximumTextLines>0</maximumTextLines><minimumTextLines>0</minimumTextLines>',
                '        <underlined>false</underlined><reverse>false</reverse><bold>false</bold><color>8</color>',
                '        <aggregateFunction>0</aggregateFunction><aggregateExpression/><printCondition>1</printCondition>',
                '        <suppressIdenticalValues>false</suppressIdenticalValues><alignment>0</alignment>',
                f'        <printLength>{plen}</printLength><linkWithDomain>true</linkWithDomain>',
                f'        <domain>{dom}</domain><printExpression>{expr}</printExpression>',
                f'        <rowPosition>{row}</rowPosition><columnPosition>{col}</columnPosition>',
                f'        <position>{of_pos}</position>',
                '      </ReportOutputField>',
            ])

        # Specials in layout
        for sp_pos, sp in enumerate(lay.get("specials", []), start=1):
            sp_type = sp.get("type", 8)  # 8 = label, 3 = date, 6 = page, etc.
            sp_lbl = sp.get("label", "")
            row = sp.get("row", 1)
            col = sp.get("col", 1)
            slen = sp.get("len", 10)

            lines.extend([
                '      <ReportSpecial>',
                '        <fillPrintEffect>false</fillPrintEffect><alignment>0</alignment><domainAdjustment>false</domainAdjustment><height>1</height>',
                f'        <label>{sp_lbl}</label>',
                '        <underlined>false</underlined><reverse>false</reverse><bold>true</bold><color>8</color>',
                f'        <length>{slen}</length><rowPosition>{row}</rowPosition><columnPosition>{col}</columnPosition>',
                f'        <specialType>{sp_type}</specialType><position>{sp_pos}</position>',
                '      </ReportSpecial>',
            ])

        lines.extend([
            '    </PhysicalReportLayout>',
            '    <positioningColumns>1</positioningColumns>',
            '    <extraNeed>0</extraNeed><newPage>false</newPage><lineFont>2</lineFont>',
            f'    <rows>{rows}</rows><columns>{cols}</columns>',
            f'    <outputExpression>{out_expr}</outputExpression>',
            f'    <sequence>{seq}</sequence>',
            '    <inputField/>',
            f'    <layoutType>{l_type}</layoutType>',
            '  </Layout>',
        ])

    # Page Setup
    lines.extend([
        '  <PageSetup>',
        '    <repeatExpression>1</repeatExpression><nrColumns>0</nrColumns>',
        '    <Font><fixedFont>false</fixedFont><defaultFont>1</defaultFont></Font>',
        f'    <Paper><height>-1</height><width>{paper_width}</width></Paper>',
        '    <Margins><footMargin>-1</footMargin><leftMargin>5</leftMargin><bottomMargin>2</bottomMargin><topMargin>2</topMargin></Margins>',
        '  </PageSetup>',
    ])

    # Script tag if present
    if script:
        lines.extend([
            '  <Source>',
            f'    <expression><![CDATA[{script}]]></expression>',
            '    <sourceType>6</sourceType>',
            f'    <sourceName>{code}</sourceName>',
            '  </Source>',
        ])

    lines.extend([
        f'  <application>{application}</application>',
        '</DR_Report>',
    ])

    return "\n".join(lines) + "\n"


def generate_reports(
    specs: List[Dict[str, Any]],
    activity_dir: Path,
    application: str,
    dry_run: bool = False,
) -> List[Dict[str, Any]]:
    """Generates report XML files in activity_dir/reports/."""
    out_dir = activity_dir / "reports"
    created = []

    for spec in specs:
        code = spec["code"]
        target_path = out_dir / f"{code}.rpt"

        if not dry_run:
            assert_file_writable(target_path, activity_path=activity_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            xml_content = generate_report_xml(spec, application)
            target_path.write_text(xml_content, encoding="utf-8")
            rel_path = target_path.relative_to(activity_dir).as_posix()
            try:
                add_component(activity_dir, rel_path)
            except Exception:
                pass

        created.append({
            "type": "report",
            "name": code,
            "path": str(target_path),
        })

    return created


def main():
    parser = argparse.ArgumentParser(description="Generate Infor LN Report (.rpt) XML component")
    parser.add_argument("--code", required=True, help="Report code (e.g. txcmg04010100)")
    parser.add_argument("--desc", help="Description")
    parser.add_argument("--paper-width", type=int, choices=[80, 132], default=80, help="Paper width (80 or 132)")
    parser.add_argument("--script-file", help="Path to 4GL report script file")
    parser.add_argument("--activity", help="Target activity folder")
    parser.add_argument("--project", default="EXTce01107", help="Software Project name")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    act_info = resolve_activity(activity_name=args.activity)
    act_dir = Path(act_info["path"])

    script_text = ""
    if args.script_file:
        p = Path(args.script_file).resolve()
        if p.exists():
            script_text = p.read_text(encoding="utf-8")

    spec = {
        "code": args.code,
        "description": args.desc or args.code,
        "paper_width": args.paper_width,
        "script": script_text,
    }
    files = generate_reports([spec], act_dir, args.project, dry_run=args.dry_run)
    print(f"[SUCCESS] Created report: {files[0]['path']}")


if __name__ == "__main__":
    main()
