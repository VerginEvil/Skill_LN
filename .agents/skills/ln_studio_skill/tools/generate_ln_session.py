#!/usr/bin/env python3
"""
ln_studio_skill/tools/generate_ln_session.py
Infor LN Studio Multi-Archetype Session & Dynamic Form Generator.

Generates production-grade .ses and session .lbl XML files matching Infor LN Studio 10.8
specifications for all archetypes (Overview/Maintain List, Maintain Details, MMT Controller with
Satellites, Satellite, Display, Process, and Print), plus Form Commands (<FormCommand>) and labels.
"""

import os
import sys
import uuid
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Set, Tuple, Union

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_schema_parser import parse_schema_file
from generate_ln_table import (
    compact_tde_xml,
    ensure_label_context_variant,
    generate_label_xml,
    get_current_iso_time,
)
from ln_workspace_manager import resolve_activity, load_config, detect_current_activity
from scm_guardrails import assert_file_writable, ReadOnlyComponentError

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


def strip_session_pkg_for_field_label(
    label_code: Optional[str],
    default_label: str,
    session_pkg: str = "",
) -> str:
    """Strips one leading session package prefix for <FormField><fieldLabel> (preserving tc/unprefixed codes)."""
    if not label_code:
        return default_label
    pkg = (session_pkg or "").lower()
    if pkg and label_code.lower().startswith(pkg):
        return label_code[len(pkg):]
    return label_code


def generate_form_field_xml(
    field_spec: Dict[str, Any],
    table_code: str,
    sequence: int,
    group_id: int = 2,
    session_pkg: str = "",
) -> str:
    """Generates standard <FormField> XML for dynamic form."""
    fname = field_spec["name"]
    full_name = f"{table_code}.{fname}"
    f_lbl = strip_session_pkg_for_field_label(field_spec.get("label_code"), full_name, session_pkg=session_pkg)
    u_id = str(uuid.uuid4())
    is_mand = "true" if field_spec.get("mandatory") else "false"
    f_len = field_spec.get("facets", {}).get("maxLength", "20")
    f_dt = field_spec.get("native_datatype", 6)

    zoom_prog = field_spec.get("zoom_program", "")
    zoom_ret = field_spec.get("zoom_return_field", "")
    zoom_type = "2" if zoom_prog else "1"

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
    session_spec: Dict[str, Any],
    table_spec: Optional[Dict[str, Any]],
    application: str,
    ui_script_code: Optional[str] = None
) -> str:
    """Generates standard <DR_Controller> XML for any session archetype."""
    scode = session_spec["code"]
    sdesc = session_spec.get("description", scode)
    ver = session_spec.get("version_id", "B61O_a_ext")
    w_type = session_spec.get("window_type", 2)
    sub_type = session_spec.get("sub_type", 1)
    tcode = session_spec.get("table", "")
    t_desc = table_spec.get("description", tcode) if table_spec else tcode
    now_iso = get_current_iso_time()

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
        f'<windowType>{w_type}</windowType>',
    ]

    # Controller Table Relationship (if linked to a main table)
    if tcode:
        index_usages = ""
        indices = table_spec.get("indices", [1]) if table_spec else [1]
        for idx_num in range(1, len(indices) + 1):
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

    # Satellites (for MMT Controller)
    for sat_pos, sat_session in enumerate(session_spec.get("satellites", []), start=1):
        sat_code = sat_session if isinstance(sat_session, str) else sat_session.get("code", "")
        sat_desc = sat_session.get("description", sat_code) if isinstance(sat_session, dict) else sat_code
        parts.append(
            f'<ControllerSatelliteRelationship>'
            f'<name>{sat_code}</name>'
            f'<description>{sat_desc}</description>'
            f'<descriptionReference>{sat_code}</descriptionReference>'
            f'<position>{sat_pos}</position>'
            f'<documentation/>'
            f'<versionID>{ver}</versionID>'
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
            f'<toSession>{sat_code}</toSession>'
            f'<initialHidden>false</initialHidden>'
            f'</ControllerSatelliteRelationship>'
        )

    # Form Commands (<FormCommand>)
    for cmd in session_spec.get("form_commands", []):
        c_name = cmd["name"]
        c_desc = cmd.get("description", c_name)
        c_lbl = cmd.get("label_code", f"{scode}.{c_name}")
        c_fn = cmd.get("function", c_name)
        c_pos = cmd.get("position", "1")
        c_seq = cmd.get("sequence", "10")
        parts.append(
            f'<FormCommand>'
            f'<name>{c_name}</name>'
            f'<description>{c_desc}</description>'
            f'<descriptionReference>{c_lbl}</descriptionReference>'
            f'<type>user</type>'
            f'<position>{c_pos}</position>'
            f'<sequence>{c_seq}</sequence>'
            f'<defaultcommand>false</defaultcommand>'
            f'<activationType>function</activationType>'
            f'<activationName>{c_fn}</activationName>'
            f'<parent/>'
            f'<shortcut/>'
            f'<separator>false</separator>'
            f'<showAsButton>true</showAsButton>'
            f'<showOnMenu>true</showOnMenu>'
            f'<initialHidden>false</initialHidden>'
            f'<commandAvailability>1</commandAvailability>'
            f'<multipleExecution>false</multipleExecution>'
            f'<saveBeforeExecution>false</saveBeforeExecution>'
            f'<refreshParent>false</refreshParent>'
            f'<category>1</category>'
            f'</FormCommand>'
        )

    # Standard Commands & UI Methods
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

    # Form & Fields Layout (only if table fields are available)
    fields_list = table_spec.get("fields", []) if table_spec else []
    ses_pkg = scode[:2].lower() if len(scode) >= 2 else ""
    fields_xml = ""
    for seq, f in enumerate(fields_list, start=1):
        fields_xml += generate_form_field_xml(f, tcode, sequence=seq, group_id=2, session_pkg=ses_pkg)

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

    # Embedded UI Script
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


def _probe_server_labels(
    pkg: str,
    probe_labels_fn=None,
    workspace_name: Optional[str] = None,
) -> Tuple[Dict[str, bool], Set[str]]:
    """Probes package and 'tc' labels via callback or StudioComponent.GetBrowseList(includeProjectLock='yes')."""
    pkg_labels: Dict[str, bool] = {}
    tc_labels: Set[str] = set()

    if probe_labels_fn is None and workspace_name:
        try:
            from ln_component_builder import get_server_client
            from ln_component_explorer import browse_components
            client, _ = get_server_client(workspace_name=workspace_name, notify=False, auto_auth=False)

            def _default_probe(p: str):
                rows = browse_components(client, package=p, comp_type="label", name_filter="%")
                out = []
                for r in rows:
                    locked = bool(r.get("locked") or r.get("lockActivity") or r.get("projectLock"))
                    out.append({"name": r.get("name", ""), "locked": locked, "lockActivity": r.get("lockActivity", "")})
                return out

            probe_labels_fn = _default_probe
        except Exception:
            probe_labels_fn = None

    if probe_labels_fn is not None:
        for row in probe_labels_fn(pkg) or []:
            if isinstance(row, dict):
                n = (row.get("name") or "").lower()
                if n:
                    pkg_labels[n] = bool(row.get("locked") or row.get("lockActivity"))
            elif isinstance(row, str) and row:
                pkg_labels[row.lower()] = False
        if pkg != "tc":
            for row in probe_labels_fn("tc") or []:
                n = (row.get("name") if isinstance(row, dict) else str(row)).lower()
                if n:
                    tc_labels.add(n)

    return pkg_labels, tc_labels


def generate_session(
    schema_file: Optional[Union[str, Path, Dict[str, Any]]] = None,
    table_code: Optional[str] = None,
    session_code: Optional[str] = None,
    activity_name: Optional[str] = None,
    workspace_name: Optional[str] = None,
    activity_path: Optional[str] = None,
    output_dir: Optional[str] = None,
    dry_run: bool = False,
    probe_labels_fn=None,
    online: bool = False,
) -> List[Dict[str, str]]:
    """
    Generates session .ses and label .lbl files for declared sessions.
    Validates SCM Read-Only protection before writing to disk.
    """
    if isinstance(schema_file, dict):
        schema = schema_file
    elif schema_file:
        schema = parse_schema_file(schema_file)
    elif table_code:
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
            "indices": [{"id": 1, "description": "Index 1", "primary_key": True, "columns": ["seqn"]}],
            "sessions": []
        }
    else:
        raise ValueError("Must provide either --spec or --table.")

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
            raise ValueError("Explicit --activity, --activity-path, or --output-dir required to generate sessions.")

    # Collect sessions to generate
    sessions_to_gen = schema.get("sessions", [])
    if not sessions_to_gen and schema.get("session"):
        sessions_to_gen = [schema["session"]]

    # If session_code was explicitly requested and not in schema
    if session_code and not sessions_to_gen:
        scode = session_code.lower()
        sessions_to_gen = [{
            "code": scode,
            "description": f"Session {scode}",
            "type": "maintain_list",
            "window_type": 2,
            "sub_type": 1,
            "table": schema.get("table", {}).get("code", ""),
            "satellites": [],
            "form_commands": []
        }]

    # Build table lookup for fields/descriptions
    tables_map = {t["code"]: t for t in schema.get("tables", [])}
    if "table" in schema and schema["table"]:
        tables_map[schema["table"]["code"]] = schema["table"]

    generated = []
    for ses in sessions_to_gen:
        scode = (session_code.lower() if session_code else ses["code"]).lower()
        sdesc = ses.get("description", scode)
        pkg = scode[:2]
        mod = scode[2:5]
        tcode = ses.get("table", "")
        tbl_info = tables_map.get(tcode)

        ses_dir = target_root / pkg / "session" / mod
        ses_path = ses_dir / f"{scode}.ses"
        ses_xml = generate_session_xml(ses, tbl_info, application=app_code)
        generated.append({
            "type": "session",
            "name": scode,
            "path": str(ses_path),
            "content": ses_xml
        })

        # Session description label (context 2 = Session/Table description)
        lbl_dir = target_root / pkg / "label"
        lbl_path = lbl_dir / f"{scode}.lbl"
        lbl_xml = generate_label_xml(scode, sdesc, ver, app_code, context=2)
        generated.append({
            "type": "label",
            "name": scode,
            "path": str(lbl_path),
            "content": lbl_xml
        })

        # Form Commands labels (context 10 = Form Commands)
        for cmd in ses.get("form_commands", []):
            cmd_lbl = cmd.get("label_code", f"{scode}.{cmd['name']}")
            cmd_desc = cmd.get("description", cmd['name'])
            c_lbl_path = lbl_dir / f"{cmd_lbl}.lbl"
            if c_lbl_path.exists():
                existing_txt = c_lbl_path.read_text(encoding="utf-8", errors="replace")
                if "<context>10</context>" not in existing_txt:
                    if not dry_run:
                        assert_file_writable(c_lbl_path, target_root)
                    updated_lbl, _ = ensure_label_context_variant(existing_txt, context=10, description=cmd_desc)
                    lbl_content = updated_lbl
                else:
                    continue
            else:
                lbl_content = generate_label_xml(cmd_lbl, cmd_desc, ver, app_code, context=10)
            generated.append({
                "type": "label",
                "name": cmd_lbl,
                "path": str(c_lbl_path),
                "content": lbl_content
            })

        # Probe server labels and handle cross-package field labels (e.g. wh.* in tx)
        fields_to_check = (tbl_info.get("fields", []) if tbl_info else []) or ses.get("fields", [])
        server_pkg_labels, server_tc_labels = _probe_server_labels(
            pkg,
            probe_labels_fn=probe_labels_fn,
            workspace_name=workspace_name if online else None,
        )
        ref_lbl_dir = target_root.parent / ".reference" / "label"
        seen_field_lbls = {item["name"].lower() for item in generated if item["type"] == "label"}
        for fld in fields_to_check:
            raw_lbl = (fld.get("label_code") or "").strip()
            if not raw_lbl:
                continue
            raw_lower = raw_lbl.lower()
            # Inherited tc labels stay in tc unless explicitly cloned/prefixed with pkg
            if (raw_lower in server_tc_labels or (raw_lower.startswith("tc") and not raw_lower.startswith(pkg))) and pkg != "tc":
                continue

            full_lbl = raw_lower if raw_lower.startswith(pkg) else f"{pkg}{raw_lower}"
            is_cross_pkg = (not raw_lower.startswith(pkg)) and ("." in raw_lower)

            if full_lbl in server_pkg_labels:
                if server_pkg_labels[full_lbl]:
                    print(f"[WARN] Label '{full_lbl}' is locked in another activity; skipping local generation.", file=sys.stderr)
                continue

            should_create = is_cross_pkg or (probe_labels_fn is not None or online)
            if not should_create:
                continue
            if full_lbl in seen_field_lbls:
                continue
            f_lbl_path = lbl_dir / f"{full_lbl}.lbl"
            if f_lbl_path.exists() or (ref_lbl_dir / f"{full_lbl}.lbl").exists():
                continue

            f_desc = fld.get("description") or fld.get("name") or full_lbl
            generated.append({
                "type": "label",
                "name": full_lbl,
                "path": str(f_lbl_path),
                "content": generate_label_xml(full_lbl, f_desc, ver, app_code, context=1),
            })
            seen_field_lbls.add(full_lbl)

    # Write files if not dry-run, enforcing Read-Only check first
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
    parser = argparse.ArgumentParser(description="Generate Infor LN Session and Form XML")
    parser.add_argument("--spec", help="Path to schema YAML/JSON file")
    parser.add_argument("--table", help="Table code (if generating from table)")
    parser.add_argument("--session", "--code", dest="session", help="Session code override (e.g. txptc1100m000)")
    parser.add_argument("--activity", help="Target activity folder name or activity code")
    parser.add_argument("--activity-path", help="Direct activity directory path")
    parser.add_argument("--workspace", help="Filter by workspace name")
    parser.add_argument("--output-dir", help="Direct target directory path (overrides activity)")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files to disk")

    args = parser.parse_args()

    try:
        files = generate_session(
            schema_file=args.spec,
            table_code=args.table,
            session_code=args.session,
            activity_name=args.activity,
            activity_path=args.activity_path,
            workspace_name=args.workspace,
            output_dir=args.output_dir,
            dry_run=args.dry_run
        )
        mode_str = "[DRY-RUN] Would generate" if args.dry_run else "[SUCCESS] Generated"
        print(f"{mode_str} {len(files)} session files:")
        for f in files:
            print(f"  ({f['type'].upper():<7}) {f['name']:<20} -> {f['path']}")
    except ReadOnlyComponentError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Session generation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
