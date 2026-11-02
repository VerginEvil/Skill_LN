#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_revision_diff.py
Server-side Revision History, Structural Diff, Server Report Wizard,
and Activity Component Maintenance for Infor LN Studio.

Implements:
- FglStudio.GetRevisions & StudioComponent.GetRevision
- diff_component (Unified 4GL script diff + Structural XML diff)
- DR_Report.Generate (Server Report Wizard)
- FglStudio.MoveComponent (Activity Component Relocation)
- FglStudio.CleanComponents (Activity Component Cleanup)
"""

import difflib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

_SKILL_TOOLS = Path(__file__).resolve().parent
if str(_SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(_SKILL_TOOLS))

from ln_server_client import LNStudioServerClient
from ln_component_explorer import BDE_TYPE_MAP
from ln_scm_engine import (
    resolve_activity_scm_metadata,
    build_activity_context_xml,
    find_component_file,
)
from admin_sync import (
    admin_after_get,
    admin_after_create,
    admin_after_uncheckout,
    list_admin_components,
    normalize_admin_path,
)


def _build_context(activity_dir: Optional[Path], project_name: str = "") -> Tuple[Optional[str], str]:
    context_xml = None
    dev_cp = f"{project_name}_dev" if project_name else "ProjectServer"
    if activity_dir:
        meta = resolve_activity_scm_metadata(activity_dir)
        task_id = meta["taskName"] or activity_dir.name.split(" ")[0].strip("[]")
        label_uuid = meta["labelUUID"] or task_id
        dev_cp = meta["taskContext"] or dev_cp
        context_xml = build_activity_context_xml(
            activity_name=task_id,
            base_vrc=meta["baseVRC"],
            connection_point=dev_cp,
            activity_guid=label_uuid,
            documentation=meta["taskDocumentation"] or None,
        )
    return context_xml, dev_cp


def list_component_revisions(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    version_id: str,
    project_name: str = "",
    activity_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Queries server-side revision history via FglStudio.GetRevisions in BDE mode (2).
    Returns list of revision metadata dictionaries.
    """
    context_xml, dev_cp = _build_context(activity_dir, project_name)

    req_xml = (
        f"<FglStudio>\n"
        f"  <compType>{comp_type}</compType>\n"
        f"  <compCode>{comp_name}</compCode>\n"
        f"  <versionID>{version_id}</versionID>\n"
        f"</FglStudio>"
    )

    resp_xml = client.do_bde_call(
        "FglStudio",
        "GetRevisions",
        req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
        mode="BDE",
    )

    revisions: List[Dict[str, Any]] = []
    try:
        root = ET.fromstring(resp_xml)
        for r_node in root.findall(".//revision") + root.findall(".//Revision") + root.findall(".//item"):
            num_str = r_node.attrib.get("number") or r_node.findtext("number") or "0"
            v_id = r_node.attrib.get("versionID") or r_node.findtext("versionID") or version_id
            date_str = r_node.attrib.get("date") or r_node.findtext("date") or ""
            time_str = r_node.attrib.get("time") or r_node.findtext("time") or ""
            author = r_node.attrib.get("author") or r_node.attrib.get("user") or r_node.findtext("author") or r_node.findtext("user") or ""
            comment = r_node.attrib.get("comment") or r_node.findtext("comment") or (r_node.text or "").strip()
            task = r_node.attrib.get("task") or r_node.attrib.get("taskName") or r_node.findtext("task") or ""

            revisions.append({
                "number": int(num_str) if num_str.isdigit() else 0,
                "version_id": v_id,
                "date": date_str,
                "time": time_str,
                "author": author,
                "comment": comment,
                "task": task,
            })
    except Exception:
        pass

    revisions.sort(key=lambda r: r["number"], reverse=True)
    return {
        "component_name": comp_name,
        "component_type": comp_type,
        "version_id": version_id,
        "total_revisions": len(revisions),
        "revisions": revisions,
        "raw_response": resp_xml,
    }


def get_component_revision(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    version_id: str,
    rev_number: int,
    project_name: str = "",
    activity_dir: Optional[Path] = None,
) -> str:
    """
    Retrieves the raw component XML of a historical server revision
    via StudioComponent.GetRevision (or DR_*.GetRevision) in BDE mode (2).
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    bde_name = info["bde"] if info else "DR_Table"
    context_xml, dev_cp = _build_context(activity_dir, project_name)

    req_xml = (
        f"<{bde_name}>\n"
        f"  <name>{comp_name}</name>\n"
        f"  <type>{comp_type.lower()}</type>\n"
        f"  <versionID>{version_id}</versionID>\n"
        f"  <number>{rev_number}</number>\n"
        f"  <optionalContent>yes</optionalContent>\n"
        f"</{bde_name}>"
    )

    try:
        resp_xml = client.do_bde_call(
            bde_name,
            "GetRevision",
            req_xml,
            connection_point=dev_cp,
            context_xml=context_xml,
            mode="BDE",
        )
    except Exception:
        # Fallback to StudioComponent.GetRevision
        resp_xml = client.do_bde_call(
            "StudioComponent",
            "GetRevision",
            req_xml,
            connection_point=dev_cp,
            context_xml=context_xml,
            mode="BDE",
        )

    return resp_xml


def _extract_script(content_str: str) -> str:
    """Extracts 4GL script content from raw text or XML expression CDATA."""
    if not content_str:
        return ""
    if "<expression>" in content_str:
        try:
            root = ET.fromstring(content_str)
            expr = root.find(".//expression")
            if expr is not None:
                # Might have nested expression
                inner = expr.find(".//expression")
                if inner is not None and inner.text:
                    return inner.text.strip()
                if expr.text:
                    return expr.text.strip()
        except Exception:
            pass
    return content_str.strip()


def _extract_structural_elements(xml_str: str) -> Dict[str, Dict[str, Any]]:
    """Extracts indexed structural elements (fields, forms, options, indices, hooks) from component XML."""
    elements = {}
    if not xml_str:
        return elements
    try:
        root = ET.fromstring(xml_str)
        for child in list(root):
            if child.tag == "expression" or child.tag.endswith("Script"):
                continue
            name = child.attrib.get("name") or child.findtext("name") or child.tag
            key = f"{child.tag}::{name}"
            # Capture attribute map and inner text
            attrs = dict(child.attrib)
            text = (child.text or "").strip()
            elements[key] = {
                "tag": child.tag,
                "name": name,
                "attributes": attrs,
                "text": text,
            }
    except Exception:
        pass
    return elements


def diff_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    target_version_id: Optional[str] = None,
    target_rev_number: Optional[int] = None,
    project_name: str = "",
) -> Dict[str, Any]:
    """
    Diffs local workarea component against a server revision or base copy.
    Produces:
    1. Unified 4GL script diff
    2. Structural XML elements diff (added, removed, modified)
    """
    # 1. Locate local file
    local_file = find_component_file(activity_dir, comp_name, comp_type)
    if not local_file or not local_file.exists():
        raise FileNotFoundError(f"Component '{comp_name}' ({comp_type}) not found in activity '{activity_dir}'")

    local_xml = local_file.read_text(encoding="utf-8", errors="ignore")

    # If standalone .4gl or .dal file exists locally, prioritize it for script diff
    script_candidates = [
        activity_dir / "scripts" / f"{comp_name}.4gl",
        activity_dir / "scripts" / f"{comp_name}.src",
        activity_dir / "dal" / f"{comp_name}.dal",
        local_file.with_suffix(".4gl"),
        local_file.with_suffix(".dal"),
    ]
    local_script = ""
    for sc in script_candidates:
        if sc.exists():
            local_script = sc.read_text(encoding="utf-8", errors="ignore")
            break
    if not local_script:
        local_script = _extract_script(local_xml)

    # 2. Fetch remote revision
    meta = resolve_activity_scm_metadata(activity_dir)
    version_id = target_version_id or meta.get("baseVRC") or "1"
    rev_num = target_rev_number if target_rev_number is not None else 0

    remote_xml = ""
    if rev_num > 0:
        remote_xml = get_component_revision(
            client=client,
            comp_type=comp_type,
            comp_name=comp_name,
            version_id=version_id,
            rev_number=rev_num,
            project_name=project_name,
            activity_dir=activity_dir,
        )
    else:
        from ln_component_explorer import get_component
        try:
            res = get_component(
                client=client,
                comp_type=comp_type,
                comp_name=comp_name,
                project_name=project_name or meta.get("taskName") or "EXTce01107",
                activity_dir=None,
            )
            remote_xml = res.get("xml_content", "")
        except Exception:
            # Fallback to get_component_revision 1
            try:
                remote_xml = get_component_revision(
                    client=client,
                    comp_type=comp_type,
                    comp_name=comp_name,
                    version_id=version_id,
                    rev_number=1,
                    project_name=project_name,
                    activity_dir=activity_dir,
                )
            except Exception:
                remote_xml = ""

    remote_script = _extract_script(remote_xml)

    # 3. Unified Script Diff
    local_lines = local_script.splitlines(keepends=True)
    remote_lines = remote_script.splitlines(keepends=True)
    diff_gen = difflib.unified_diff(
        remote_lines,
        local_lines,
        fromfile=f"server/{comp_name} (rev {rev_num or 'base'})",
        tofile=f"local/{comp_name}",
    )
    script_diff_text = "".join(diff_gen)

    # 4. Structural XML Diff
    local_elements = _extract_structural_elements(local_xml)
    remote_elements = _extract_structural_elements(remote_xml)

    added = []
    removed = []
    modified = []

    for k, v in local_elements.items():
        if k not in remote_elements:
            added.append(v)
        elif v != remote_elements[k]:
            modified.append({
                "key": k,
                "local": v,
                "remote": remote_elements[k],
            })

    for k, v in remote_elements.items():
        if k not in local_elements:
            removed.append(v)

    return {
        "component_name": comp_name,
        "component_type": comp_type,
        "target_version": version_id,
        "target_revision": rev_num,
        "has_script_changes": bool(script_diff_text.strip()),
        "script_diff": script_diff_text,
        "has_structural_changes": bool(added or removed or modified),
        "structural_diff": {
            "added_elements": added,
            "removed_elements": removed,
            "modified_elements": modified,
        },
    }


def generate_report_on_server(
    client: LNStudioServerClient,
    report_name: str,
    table_name: str,
    version_id: str,
    description: str = "",
    report_size: str = "80",
    report_type: str = "1",
    used_index: str = "1",
    input_fields: Optional[List[str]] = None,
    overwrite: bool = True,
    project_name: str = "",
    activity_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Invokes Server Report Wizard via DR_Report.Generate in BDE mode (2).
    Generates standard report layout and script, saves .rpt locally, and updates .admin.
    """
    context_xml, dev_cp = _build_context(activity_dir, project_name)

    # Build inputFields XML
    fields_xml_parts = []
    if input_fields:
        for f in input_fields:
            fields_xml_parts.append(f"<field>{f}</field>")
    fields_xml = "".join(fields_xml_parts)

    req_xml = (
        f"<DR_Report>\n"
        f"  <name>{report_name}</name>\n"
        f"  <versionID>{version_id}</versionID>\n"
        f"  <table>{table_name}</table>\n"
        f"  <description>{description}</description>\n"
        f"  <overwrite>{'yes' if overwrite else 'no'}</overwrite>\n"
        f"  <reportSize>{report_size}</reportSize>\n"
        f"  <reportType>{report_type}</reportType>\n"
        f"  <usedIndex>{used_index}</usedIndex>\n"
        f"  <inputFields>{fields_xml}</inputFields>\n"
        f"</DR_Report>"
    )

    resp_xml = client.do_bde_call(
        "DR_Report",
        "Generate",
        req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
        mode="BDE",
    )

    output_path = None
    if activity_dir:
        rpt_dir = activity_dir / "reports"
        rpt_dir.mkdir(parents=True, exist_ok=True)
        rpt_file = rpt_dir / f"{report_name}.rpt"
        # If server returned full DR_Report XML, use it; otherwise scaffold standard Single-XML TDE
        file_content = resp_xml if "<DR_Report" in resp_xml else (
            f"<DR_Report name=\"{report_name}\" versionID=\"{version_id}\" table=\"{table_name}\">\n"
            f"  <description>{description}</description>\n"
            f"  <reportSize>{report_size}</reportSize>\n"
            f"  <reportType>{report_type}</reportType>\n"
            f"  <expression><![CDATA[| 4GL Report script for {report_name}]]></expression>\n"
            f"</DR_Report>"
        )
        rpt_file.write_text(file_content, encoding="utf-8")
        admin_after_create(activity_dir, f"reports/{report_name}.rpt")
        output_path = str(rpt_file)

    success = "error" not in resp_xml.lower() or "<DR_Report" in resp_xml
    return {
        "success": success,
        "report_name": report_name,
        "table_name": table_name,
        "version_id": version_id,
        "output_file": output_path,
        "raw_response": resp_xml,
    }


def move_activity_components(
    client: LNStudioServerClient,
    components: List[Dict[str, str]],
    source_activity_dir: Path,
    target_task_name: str,
    target_task_uuid: str,
    target_base_vrc: str,
    target_context: str,
    target_activity_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Moves components from source activity to target activity on server via FglStudio.MoveComponent (BDE mode 2).
    Updates local activity files and .admin metadata.
    """
    context_xml, dev_cp = _build_context(source_activity_dir)

    comp_items = []
    for c in components:
        comp_items.append(f"<Component><type>{c['type']}</type><name>{c['name']}</name></Component>")
    comps_xml = "".join(comp_items)

    req_xml = (
        f"<FglStudio>\n"
        f"  <TargetActivityID>\n"
        f"    <taskName>{target_task_name}</taskName>\n"
        f"    <labelUUID>{target_task_uuid}</labelUUID>\n"
        f"    <baseVRC>{target_base_vrc}</baseVRC>\n"
        f"    <taskContext>{target_context}</taskContext>\n"
        f"  </TargetActivityID>\n"
        f"  <ComponentList>\n"
        f"    <Components>{comps_xml}</Components>\n"
        f"  </ComponentList>\n"
        f"</FglStudio>"
    )

    resp_xml = client.do_bde_call(
        "FglStudio",
        "MoveComponent",
        req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
        mode="BDE",
    )

    # Update local filesystem and .admin files if target activity dir provided
    moved_count = 0
    for c in components:
        src_file = find_component_file(source_activity_dir, c["name"], c["type"])
        if src_file and src_file.exists():
            rel_p = src_file.relative_to(source_activity_dir)
            if target_activity_dir and target_activity_dir.is_dir():
                dest_file = target_activity_dir / rel_p
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                dest_file.write_bytes(src_file.read_bytes())
                admin_after_create(target_activity_dir, rel_p.as_posix())
            # Uncheckout from source
            admin_after_uncheckout(source_activity_dir, rel_p.as_posix())
            try:
                src_file.unlink(missing_ok=True)
            except Exception:
                pass
            moved_count += 1

    success = "error" not in resp_xml.lower() or "ok" in resp_xml.lower()
    return {
        "success": success,
        "moved_components": len(components),
        "target_task": target_task_name,
        "raw_response": resp_xml,
    }


def clean_activity_components(
    client: LNStudioServerClient,
    components: List[Dict[str, str]],
    activity_dir: Path,
) -> Dict[str, Any]:
    """
    Cleans components from activity workarea via FglStudio.CleanComponents (BDE mode 2).
    Deletes files from local workspace and removes them from .admin.
    """
    context_xml, dev_cp = _build_context(activity_dir)

    comp_items = []
    for c in components:
        comp_items.append(f"<Component><type>{c['type']}</type><name>{c['name']}</name></Component>")
    comps_xml = "".join(comp_items)

    req_xml = (
        f"<FglStudio>\n"
        f"  <CleanComponents>\n"
        f"    <ComponentList>\n"
        f"      <Components>{comps_xml}</Components>\n"
        f"    </ComponentList>\n"
        f"  </CleanComponents>\n"
        f"</FglStudio>"
    )

    resp_xml = client.do_bde_call(
        "FglStudio",
        "CleanComponents",
        req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
        mode="BDE",
    )

    cleaned_count = 0
    for c in components:
        comp_file = find_component_file(activity_dir, c["name"], c["type"])
        if comp_file and comp_file.exists():
            rel_p = comp_file.relative_to(activity_dir).as_posix()
            admin_after_uncheckout(activity_dir, rel_p)
            try:
                comp_file.unlink(missing_ok=True)
            except Exception:
                pass
            cleaned_count += 1

    success = "error" not in resp_xml.lower() or "ok" in resp_xml.lower()
    return {
        "success": success,
        "cleaned_components": len(components),
        "raw_response": resp_xml,
    }
