#!/usr/bin/env python3
"""
tools/generate_ln_session.py
Infor LN Studio Session & Integrated Dynamic Form Generator.

Generates production-grade .ses and session .lbl XML files matching Infor LN Studio 10.8
specifications, including <DR_Controller>, main table relationship, standard commands,
integrated dynamic forms (<PhysicalFormLayout>), and starter UI script.
"""

import os
import sys
import uuid
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

_current_dir = Path(__file__).resolve().parent
_repo_root = _current_dir.parent
for p in (str(_repo_root), str(_current_dir)):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from tools.ln_schema_parser import parse_schema_file
    from tools.generate_ln_table import generate_label_xml, get_current_iso_time
    from tools.ln_workspace_manager import resolve_activity, load_config
except ImportError:
    from ln_schema_parser import parse_schema_file
    from generate_ln_table import generate_label_xml, get_current_iso_time
    from ln_workspace_manager import resolve_activity, load_config


STANDARD_COMMANDS = [
    ("start.set", False, 1),
    ("first.view", False, 2),
    ("next.view", False, 3),
    ("prev.view", False, 4),
    ("last.view", False, 5),
    ("def.find", True, 6),
    ("find.data", True, 7),
    ("first.set", True, 8),
    ("next.set", True, 9),
    ("display.set", False, 10),
    ("prev.set", True, 11),
    ("rotate.curr", False, 12),
    ("last.set", True, 13),
    ("add.set", True, 14),
    ("update.db", True, 15),
    ("dupl.occur", True, 16),
    ("recover.set", True, 17),
    ("mark.delete", True, 18),
    ("mark.occur", False, 19),
    ("change.order", False, 20),
    ("modify.set", True, 21),
    ("print.data", False, 23),
    ("create.job", False, 24),
    ("change.frm", True, 25),
    ("first.frm", True, 26),
    ("next.frm", True, 27),
    ("prev.frm", True, 28),
    ("last.frm", True, 29),
    ("resize.frm", False, 31),
    ("cust.grid", False, 32),
    ("cmd.options", False, 33),
    ("zoom", False, 34),
    ("interrupt", False, 35),
    ("end.program", True, 36),
    ("abort.program", True, 37),
    ("text.manager", False, 39),
    ("run.job", False, 40),
    ("global.delete", False, 41),
    ("global.copy", False, 42),
    ("save.defaults", False, 43),
    ("get.defaults", False, 44),
    ("start.chart", False, 45),
    ("start.query", True, 46),
    ("select.all", False, 47),
]


def generate_form_field_xml(
    field_spec: Dict[str, Any],
    table_code: str,
    sequence: int,
    group_id: int = 2
) -> str:
    """Generates standard <FormField> XML for dynamic form."""
    fname = field_spec["name"]
    full_name = f"{table_code}.{fname}"
    f_lbl = field_spec.get("label_code", full_name)
    u_id = str(uuid.uuid4())
    is_mand = "true" if field_spec.get("mandatory") else "false"
    f_len = field_spec.get("facets", {}).get("maxLength", "20")
    f_dt = field_spec.get("native_datatype", 6)

    zoom_prog = field_spec.get("zoom_program", "")
    zoom_ret = field_spec.get("zoom_return_field", "")
    zoom_type = "2" if zoom_prog else "1"

    # Display format for numeric
    disp_format = "ZZZZZ9" if f_dt == 3 else ""
    format_linked = "true" if disp_format else "true"

    xml = (
        f'<FormField>'
        f'<uuid>{u_id}</uuid>'
        f'<textDirection>10</textDirection>'
        f'<fieldAlignment>5</fieldAlignment>'
        f'<indexZoomSession>0</indexZoomSession>'
        f'<iconName/>'
        f'<additionalProperties2>0</additionalProperties2>'
        f'<additionalProperties1>1</additionalProperties1>'
        f'<autoEnableDisable>false</autoEnableDisable>'
        f'<behindEnumConstant>0</behindEnumConstant>'
        f'<hyperlink>false</hyperlink>'
        f'<searchDescription/>'
        f'<constantValueForYes>0</constantValueForYes>'
        f'<viewField>false</viewField>'
        f'<displayHeight>1</displayHeight>'
        f'<columnID>1</columnID>'
        f'<endXPosition>50</endXPosition>'
        f'<parentField>0</parentField>'
        f'<labelHeightOverview>1</labelHeightOverview>'
        f'<labelLengthOverview>999</labelLengthOverview>'
        f'<labelHeightDetail>1</labelHeightDetail>'
        f'<labelLengthDetail>{len(field_spec.get("description", fname))}</labelLengthDetail>'
        f'<labelPosition>1</labelPosition>'
        f'<dependentOnParentField>false</dependentOnParentField>'
        f'<xPositionLabel>1</xPositionLabel>'
        f'<followUpField>0</followUpField>'
        f'<labelAlignment>2</labelAlignment>'
        f'<windowsControl>0</windowsControl>'
        f'<fieldBelowGrid>false</fieldBelowGrid>'
        f'<overviewSession>true</overviewSession>'
        f'<detailsSession>true</detailsSession>'
        f'<childFieldsBehind>false</childFieldsBehind>'
        f'<followUp>false</followUp>'
        f'<nextField>0</nextField>'
        f'<groupID>{group_id}</groupID>'
        f'<synchronizedField>false</synchronizedField>'
        f'<defaultValue/>'
        f'<inputReferenceExpression>1</inputReferenceExpression>'
        f'<fieldLabel>{f_lbl}</fieldLabel>'
        f'<languageUnitExpression/>'
        f'<mandatoryInput>{is_mand}</mandatoryInput>'
        f'<sequenceMode>{sequence * 10}</sequenceMode>'
        f'<fieldLength>{f_len}</fieldLength>'
        f'<echoField>true</echoField>'
        f'<message/>'
        f'<defaultExpression>false</defaultExpression>'
        f'<zoomReturnField>{zoom_ret}</zoomReturnField>'
        f'<zoomProgram>{zoom_prog}</zoomProgram>'
        f'<zoomType>{zoom_type}</zoomType>'
        f'<startPositionString>1</startPositionString>'
        f'<linkInputDigitsBefore>true</linkInputDigitsBefore>'
        f'<inputDigitsBefore>{f_len}</inputDigitsBefore>'
        f'<linkDisplayDigitsBefore>true</linkDisplayDigitsBefore>'
        f'<displayDigitsBefore>{f_len}</displayDigitsBefore>'
        f'<minimumInputLength>0</minimumInputLength>'
        f'<displayFormatLinked>{format_linked}</displayFormatLinked>'
        f'<displayFormat>{disp_format}</displayFormat>'
        f'<fieldType>2</fieldType>'
        f'<domain/>'
        f'<element>1</element>'
        f'<fieldName>{full_name}</fieldName>'
        f'<rowScreenPosition>1</rowScreenPosition>'
        f'<columnScreenPosition>44</columnScreenPosition>'
        f'<sequenceNumber>{sequence}</sequenceNumber>'
        f'</FormField>'
    )
    return xml


def generate_session_xml(
    schema: Dict[str, Any],
    application: str,
    ui_script_code: Optional[str] = None
) -> str:
    """Generates standard <DR_Controller> XML for session."""
    tbl = schema["table"]
    tcode = tbl["code"]
    t_desc = tbl["description"]
    ver = tbl["version_id"]

    ses = schema.get("session") or {}
    scode = ses.get("code") or f"{tcode[:2]}{tcode[2:5]}1100m000"
    sdesc = ses.get("description", t_desc)
    now_iso = get_current_iso_time()

    # 1. Controller Header
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        '<DR_Controller>',
        f'<description>{sdesc}</description>',
        f'<versionID>{ver}</versionID>',
        '<type>session</type>',
        f'<name>{scode}</name>',
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
        f'<descriptionReference>{scode}</descriptionReference>',
    ]

    # 2. Controller Table Relationship
    index_usages = ""
    for idx_num in range(1, len(schema.get("indices", [1])) + 1):
        index_usages += (
            f'<IndexUsage>'
            f'<nrGroupFields>0</nrGroupFields>'
            f'<sequence>0</sequence>'
            f'<active>false</active>'
            f'<position>{idx_num}</position>'
            f'</IndexUsage>'
        )

    parts.append(
        f'<ControllerTableRelationship>'
        f'<showView>false</showView>'
        f'<dynIndexSwitching>1</dynIndexSwitching>'
        f'{index_usages}'
        f'<toTable>{tcode}</toTable>'
        f'<position>1</position>'
        f'<descriptionReference>{tcode}</descriptionReference>'
        f'<description>{t_desc}</description>'
        f'<name>{tcode}</name>'
        f'</ControllerTableRelationship>'
    )

    # 3. UI Methods & Standard Commands
    parts.append('<UIMethod><status>allowed</status><description>Webtop Enabled</description><name>webtop</name></UIMethod>')
    parts.append('<UIMethod><status>notchecked</status><description>Workflow Enabled</description><name>workflow</name></UIMethod>')

    for cmd_name, is_act, pos in STANDARD_COMMANDS:
        act_str = "true" if is_act else "false"
        parts.append(
            f'<StandardCommand>'
            f'<active>{act_str}</active>'
            f'<defaultcommand>false</defaultcommand>'
            f'<startcommand>false</startcommand>'
            f'<position>{pos}</position>'
            f'<description/>'
            f'<name>{cmd_name}</name>'
            f'</StandardCommand>'
        )

    parts.append('<defaultStartCommand>false</defaultStartCommand>')

    # 4. Integrated Dynamic Form (<Form>)
    fields_xml = ""
    for seq, f in enumerate(schema.get("fields", []), start=1):
        fields_xml += generate_form_field_xml(f, tcode, sequence=seq, group_id=2)

    form_groups_xml = (
        '<FormGroup>'
        '<selectionGroup>false</selectionGroup><parentTable/><miscellaneous>0</miscellaneous>'
        '<nextToOtherGroup>false</nextToOtherGroup><checkBoxesOnly>false</checkBoxesOnly>'
        '<formFormat>13</formFormat><subGroupOnNewPage>false</subGroupOnNewPage>'
        '<nrSubGroups>1</nrSubGroups><firstChildGroup>2</firstChildGroup><virtualGroup>true</virtualGroup>'
        '<groupAlignment>1</groupAlignment><firstField>0</firstField><nextGroup>0</nextGroup>'
        '<previousGroup>0</previousGroup><parentGroup>0</parentGroup><overviewSession>true</overviewSession>'
        '<detailsSession>true</detailsSession><showGroupBox>false</showGroupBox><groupHeader/>'
        '<level>0</level><repeating>false</repeating><groupID>1</groupID>'
        '</FormGroup>'
        '<FormGroup>'
        '<selectionGroup>false</selectionGroup><parentTable/><miscellaneous>0</miscellaneous>'
        '<nextToOtherGroup>false</nextToOtherGroup><checkBoxesOnly>false</checkBoxesOnly>'
        '<formFormat>13</formFormat><subGroupOnNewPage>false</subGroupOnNewPage>'
        '<nrSubGroups>1</nrSubGroups><firstChildGroup>0</firstChildGroup><virtualGroup>false</virtualGroup>'
        '<groupAlignment>-2</groupAlignment><firstField>10</firstField><nextGroup>3</nextGroup>'
        '<previousGroup>0</previousGroup><parentGroup>1</parentGroup><overviewSession>true</overviewSession>'
        '<detailsSession>true</detailsSession><showGroupBox>false</showGroupBox><groupHeader/>'
        '<level>1</level><repeating>true</repeating><groupID>2</groupID>'
        '</FormGroup>'
        '<FormGroup>'
        '<selectionGroup>false</selectionGroup><parentTable/><miscellaneous>0</miscellaneous>'
        '<nextToOtherGroup>false</nextToOtherGroup><checkBoxesOnly>false</checkBoxesOnly>'
        '<formFormat>13</formFormat><subGroupOnNewPage>false</subGroupOnNewPage>'
        '<nrSubGroups>1</nrSubGroups><firstChildGroup>0</firstChildGroup><virtualGroup>false</virtualGroup>'
        '<groupAlignment>-3</groupAlignment><firstField>20</firstField><nextGroup>0</nextGroup>'
        '<previousGroup>2</previousGroup><parentGroup>1</parentGroup><overviewSession>true</overviewSession>'
        '<detailsSession>true</detailsSession><showGroupBox>false</showGroupBox><groupHeader/>'
        '<level>1</level><repeating>false</repeating><groupID>3</groupID>'
        '</FormGroup>'
    )

    form_xml = (
        f'<Form>'
        f'<PhysicalFormLayout>'
        f'{fields_xml}'
        f'{form_groups_xml}'
        f'</PhysicalFormLayout>'
        f'<description>{sdesc}</description>'
        f'<name>{scode}d</name>'
        f'<horizontal>true</horizontal>'
        f'<custProhibited>false</custProhibited>'
        f'<additionalConstraints>1</additionalConstraints>'
        f'<documentation/>'
        f'<application>{application}</application>'
        f'</Form>'
    )
    parts.append(form_xml)

    # 5. Embedded UI Script (<DR_Module>)
    if not ui_script_code:
        ui_script_code = (
            f"|*******************************************************************************\n"
            f"|* {scode}  {ver}\n"
            f"|* {sdesc}\n"
            f"|* Script Type: 123\n"
            f"|*******************************************************************************\n\n"
            f"#include <bic_dam>\n\n"
            f"declaration:\n\n"
            f"\ttable\tt{tcode} |* {t_desc}\n\n"
            f"main.table.io:\n"
            f"before.write:\n\n"
            f"before.rewrite:\n\n"
            f"choice.update.db:\n"
            f"before.choice:\n"
            f"\tcheck.all.input()\n"
        )

    escaped_ui = (
        ui_script_code.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    parts.append(
        f'<DR_Module>'
        f'<description>{sdesc}</description>'
        f'<versionID>{ver}</versionID>'
        f'<type>library</type>'
        f'<name>{scode}</name>'
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
        f'<sourceVersionID>{ver}</sourceVersionID>'
        f'<sourceObjectID>1</sourceObjectID>'
        f'<expression>{escaped_ui}</expression>'
        f'<expressionLanguageType>Baan4C</expressionLanguageType>'
        f'<sourceType>1</sourceType>'
        f'<sourceDescription>{sdesc}</sourceDescription>'
        f'<sourceName>{scode}</sourceName>'
        f'</Source>'
        f'<documentation/>'
        f'<Attachment><type>relnotes</type><name>{scode}</name></Attachment>'
        f'<Attachment><type>techdoc</type><name>{scode}</name></Attachment>'
        f'<additionalConstraints>1</additionalConstraints>'
        f'<additionalInstructions/>'
        f'<keyword>||</keyword>'
        f'<application>{application}</application>'
        f'</DR_Module>'
    )

    parts.append('</DR_Controller>')
    return "".join(parts)


def generate_session(
    schema_file: Optional[str] = None,
    table_code: Optional[str] = None,
    session_code: Optional[str] = None,
    activity_name: Optional[str] = None,
    output_dir: Optional[str] = None,
    dry_run: bool = False
) -> List[Dict[str, str]]:
    """
    Generates session .ses and label .lbl files.
    """
    if schema_file:
        schema = parse_schema_file(schema_file)
    elif table_code:
        # Minimal synthesized schema from table code
        tcode = table_code.lower()
        schema = {
            "table": {
                "code": tcode,
                "package": tcode[:2],
                "module": tcode[2:5],
                "description": f"Table {tcode}",
                "version_id": "B61O_a_ext"
            },
            "fields": [
                {"name": "seqn", "description": "Sequence", "position": 1, "native_datatype": 3, "mandatory": True}
            ],
            "indices": [{"id": 1, "description": "Index 1", "primary_key": True, "columns": ["seqn"]}]
        }
    else:
        raise ValueError("Must provide either --spec or --table.")

    tbl = schema["table"]
    pkg = tbl["package"]
    mod = tbl["module"]
    tcode = tbl["code"]
    ver = tbl["version_id"]

    ses_spec = schema.get("session") or {}
    scode = session_code.lower() if session_code else (ses_spec.get("code") or f"{tcode[:2]}{tcode[2:5]}1100m000").lower()
    sdesc = ses_spec.get("description", tbl["description"])

    target_root: Path
    app_code = tbl.get("application", "")

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

    generated = []

    # 1. Session XML
    ses_dir = target_root / pkg / "session" / mod
    ses_path = ses_dir / f"{scode}.ses"
    ses_xml = generate_session_xml(schema, application=app_code)
    generated.append({
        "type": "session",
        "name": scode,
        "path": str(ses_path),
        "content": ses_xml
    })

    # 2. Session Label XML
    lbl_dir = target_root / pkg / "label"
    lbl_path = lbl_dir / f"{scode}.lbl"
    lbl_xml = generate_label_xml(scode, sdesc, ver, app_code)
    generated.append({
        "type": "label",
        "name": scode,
        "path": str(lbl_path),
        "content": lbl_xml
    })

    if not dry_run:
        for item in generated:
            p = Path(item["path"])
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(item["content"])

    return generated


def main():
    parser = argparse.ArgumentParser(description="Generate Infor LN Session and Form XML")
    parser.add_argument("--spec", help="Path to schema YAML/JSON file")
    parser.add_argument("--table", help="Table code (if generating from table)")
    parser.add_argument("--session", help="Session code override (e.g. txptc1100m000)")
    parser.add_argument("--activity", help="Target activity folder name or activity code")
    parser.add_argument("--output-dir", help="Direct target directory path (overrides activity)")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files to disk")

    args = parser.parse_args()

    try:
        files = generate_session(
            schema_file=args.spec,
            table_code=args.table,
            session_code=args.session,
            activity_name=args.activity,
            output_dir=args.output_dir,
            dry_run=args.dry_run
        )
        mode_str = "[DRY-RUN] Would generate" if args.dry_run else "[SUCCESS] Generated"
        print(f"{mode_str} {len(files)} session files:")
        for f in files:
            print(f"  ({f['type'].upper():<7}) {f['name']:<20} -> {f['path']}")
    except Exception as e:
        print(f"[ERROR] Session generation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
