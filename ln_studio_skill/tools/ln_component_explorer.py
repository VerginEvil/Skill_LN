#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_component_explorer.py
Infor LN Studio Remote Component Explorer, Get & Clone Workflows.

Handles:
1. Component browsing via StudioComponent.GetBrowseList across 12 component types.
2. In-memory inspection (get-component --inspect) for AI agents and code generators.
3. Read-only component download and .admin tracking in local Activity folders.
4. Component cloning (clone-component) from standard (tc, td, wh) to custom (tx).
"""

import os
import sys
import stat
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any

from ln_server_client import LNStudioServerClient, BdeExecutionError

BDE_TYPE_MAP = {
    "table": {"bde": "DR_Table", "ext": ".tbl", "subfolder": "tables"},
    "session": {"bde": "DR_Controller", "ext": ".ses", "subfolder": "sessions"},
    "library": {"bde": "DR_Module", "ext": ".lib", "subfolder": "libraries", "type_attr": "library"},
    "function": {"bde": "DR_Module", "ext": ".fnc", "subfolder": "functions", "type_attr": "function"},
    "domain": {"bde": "DR_Domain", "ext": ".dmn", "subfolder": "domains"},
    "label": {"bde": "DR_Label", "ext": ".lbl", "subfolder": "labels"},
    "report": {"bde": "DR_Report", "ext": ".rpt", "subfolder": "reports"},
    "message": {"bde": "DR_Message", "ext": ".msg", "subfolder": "messages"},
    "question": {"bde": "DR_Question", "ext": ".qst", "subfolder": "questions"},
    "menu": {"bde": "DR_Menu", "ext": ".mnu", "subfolder": "menus"},
    "additional": {"bde": "DR_AdditionalFile", "ext": ".add", "subfolder": "additional_files"},
}


def _split_component_name(comp_name: str) -> Tuple[str, str, str]:
    """Splits an LN component name (e.g. 'tcibd001' or 'whwmd4300m000') into (package, module, object)."""
    pkg = comp_name[:2].lower()
    mod = comp_name[2:5].lower() if len(comp_name) >= 5 else ""
    obj = comp_name[5:] if len(comp_name) > 5 else ""
    return pkg, mod, obj


def browse_components(
    client: LNStudioServerClient,
    package: str = "",
    comp_type: str = "",
    name_filter: str = "",
    connection_point: str = "ProjectServer",
) -> List[Dict[str, str]]:
    """
    Browses server components using StudioComponent.GetBrowseList BDE.
    """
    req_parts = ["<StudioComponent><GetBrowseListRequest>"]
    if package:
        req_parts.append(f"<package>{package}</package>")
    if comp_type:
        req_parts.append(f"<type>{comp_type}</type>")
    if name_filter:
        req_parts.append(f"<filter>{name_filter}</filter>")
    req_parts.append("</GetBrowseListRequest></StudioComponent>")
    req_xml = "".join(req_parts)

    resp_xml = client.do_bde_call("StudioComponent", "GetBrowseList", req_xml, connection_point=connection_point)
    root = ET.fromstring(resp_xml)

    components = []
    for elem in root.iter("Component"):
        name = elem.findtext("name") or elem.findtext("Name") or ""
        ctype = elem.findtext("type") or elem.findtext("Type") or comp_type
        pkg = elem.findtext("package") or elem.findtext("Package") or (name[:2] if len(name) >= 2 else "")
        mod = elem.findtext("module") or elem.findtext("Module") or (name[2:5] if len(name) >= 5 else "")
        desc = elem.findtext("description") or elem.findtext("Description") or ""

        if name:
            components.append({
                "name": name,
                "type": ctype,
                "package": pkg,
                "module": mod,
                "description": desc,
            })
    return components


def inspect_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    connection_point: str = "ProjectServer",
) -> Dict[str, Any]:
    """
    Fetches component definition via DR_*.Get and extracts structured schema and 4GL code
    in-memory for AI coding agents without modifying the local Activity directory.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'. Supported: {list(BDE_TYPE_MAP.keys())}")

    bde_name = info["bde"]
    pkg, mod, _ = _split_component_name(comp_name)

    req_xml = (
        f"<{bde_name}>\n"
        f"  <GetRequest>\n"
        f"    <name>{comp_name}</name>\n"
        f"    <package>{pkg}</package>\n"
        f"    <module>{mod}</module>\n"
        f"  </GetRequest>\n"
        f"</{bde_name}>"
    )

    resp_xml = client.do_bde_call(bde_name, "Get", req_xml, connection_point=connection_point)
    root = ET.fromstring(resp_xml)

    summary: Dict[str, Any] = {
        "name": comp_name,
        "type": comp_type,
        "package": pkg,
        "module": mod,
        "description": root.findtext(".//description") or "",
        "raw_xml": resp_xml,
    }

    # Extract fields if table or report
    fields = []
    fields_container = root.find(".//Fields")
    if fields_container is not None:
        for f in fields_container.findall("./Field"):
            fname = f.attrib.get("name") or f.findtext("name") or ""
            fdom = f.attrib.get("domain") or f.findtext("domain") or ""
            flbl = f.attrib.get("label") or f.findtext("label") or ""
            if fname:
                fields.append({"name": fname, "domain": fdom, "label": flbl})
    else:
        for f in root.iter("Field"):
            fname = f.attrib.get("name") or f.findtext("name") or ""
            fdom = f.attrib.get("domain") or f.findtext("domain") or ""
            flbl = f.attrib.get("label") or f.findtext("label") or ""
            if fname and fdom:
                fields.append({"name": fname, "domain": fdom, "label": flbl})
    summary["fields"] = fields

    # Extract embedded scripts (dalScript, uiScript, scriptText)
    scripts = []
    for tag in ("dalScript", "uiScript", "scriptText", "Script", "reportScript"):
        elem = root.find(f".//{tag}")
        if elem is not None and elem.text:
            scripts.append(elem.text.strip())
    summary["script"] = "\n\n".join(scripts)

    return summary


def get_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    read_only: bool = True,
    connection_point: str = "ProjectServer",
) -> Path:
    """
    Fetches component XML from server via DR_*.Get, writes it to activity directory,
    enforces OS Read-Only flag, and registers it in .admin SCM cache.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    ext = info["ext"]
    subfolder = info["subfolder"]
    pkg, mod, _ = _split_component_name(comp_name)

    req_xml = (
        f"<{bde_name}>\n"
        f"  <GetRequest>\n"
        f"    <name>{comp_name}</name>\n"
        f"    <package>{pkg}</package>\n"
        f"    <module>{mod}</module>\n"
        f"  </GetRequest>\n"
        f"</{bde_name}>"
    )

    resp_xml = client.do_bde_call(bde_name, "Get", req_xml, connection_point=connection_point)

    target_dir = activity_dir / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{comp_name}{ext}"

    # Clear read-only if file already exists to overwrite
    if target_file.exists():
        try:
            os.chmod(target_file, stat.S_IWRITE | stat.S_IREAD)
        except Exception:
            pass

    target_file.write_text(resp_xml, encoding="utf-8")

    if read_only:
        try:
            os.chmod(target_file, stat.S_IREAD)
        except Exception:
            pass

    # Register in .admin cache
    from admin_sync import add_component
    rel_path = target_file.relative_to(activity_dir).as_posix()
    try:
        add_component(activity_dir, rel_path)
    except Exception as e:
        print(f"[WARN] Failed to register {rel_path} in .admin: {e}", file=sys.stderr)

    return target_file


def clone_component(
    client: LNStudioServerClient,
    comp_type: str,
    source_name: str,
    target_name: str,
    activity_dir: Path,
    register_on_server: bool = True,
    connection_point: str = "ProjectServer",
) -> Path:
    """
    Fetches source component XML via Get, renames package/module/component and labels,
    writes the editable XML to activity folder, and registers it via DR_Create.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    ext = info["ext"]
    subfolder = info["subfolder"]

    src_pkg, src_mod, _ = _split_component_name(source_name)
    tgt_pkg, tgt_mod, _ = _split_component_name(target_name)

    # 1. Fetch source XML
    req_xml = (
        f"<{bde_name}>\n"
        f"  <GetRequest>\n"
        f"    <name>{source_name}</name>\n"
        f"    <package>{src_pkg}</package>\n"
        f"    <module>{src_mod}</module>\n"
        f"  </GetRequest>\n"
        f"</{bde_name}>"
    )
    resp_xml = client.do_bde_call(bde_name, "Get", req_xml, connection_point=connection_point)

    # 2. Rewrite names, package, module, and labels
    renamed_xml = resp_xml
    renamed_xml = re.sub(f'name="{re.escape(source_name)}"', f'name="{target_name}"', renamed_xml)
    renamed_xml = re.sub(f'<name>{re.escape(source_name)}</name>', f'<name>{target_name}</name>', renamed_xml)
    renamed_xml = re.sub(f'package="{re.escape(src_pkg)}"', f'package="{tgt_pkg}"', renamed_xml)
    renamed_xml = re.sub(f'<package>{re.escape(src_pkg)}</package>', f'<package>{tgt_pkg}</package>', renamed_xml)

    if src_mod and tgt_mod:
        renamed_xml = re.sub(f'module="{re.escape(src_mod)}"', f'module="{tgt_mod}"', renamed_xml)
        renamed_xml = re.sub(f'<module>{re.escape(src_mod)}</module>', f'<module>{tgt_mod}</module>', renamed_xml)

    # Rename label references: source_name.field -> target_name.field
    renamed_xml = re.sub(f'label="{re.escape(source_name)}\\.([A-Za-z0-9_]+)"', f'label="{target_name}.\\1"', renamed_xml)

    # 3. Write target component to activity folder
    target_dir = activity_dir / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{target_name}{ext}"

    if target_file.exists():
        os.chmod(target_file, stat.S_IWRITE | stat.S_IREAD)
    target_file.write_text(renamed_xml, encoding="utf-8")
    os.chmod(target_file, stat.S_IWRITE | stat.S_IREAD)

    # 4. Register in .admin cache
    from admin_sync import add_component
    rel_path = target_file.relative_to(activity_dir).as_posix()
    try:
        add_component(activity_dir, rel_path)
    except Exception as e:
        print(f"[WARN] Failed to register cloned component {rel_path} in .admin: {e}", file=sys.stderr)

    # 5. Register on server if requested
    if register_on_server:
        create_req = (
            f"<{bde_name}>\n"
            f"  <DR_CreateRequest>\n"
            f"    <name>{target_name}</name>\n"
            f"    <package>{tgt_pkg}</package>\n"
            f"    <module>{tgt_mod}</module>\n"
            f"    <content><![CDATA[{renamed_xml}]]></content>\n"
            f"  </DR_CreateRequest>\n"
            f"</{bde_name}>"
        )
        dev_cp = connection_point if connection_point != "ProjectServer" else "EXTce01107_dev"
        client.do_bde_call(bde_name, "DR_Create", create_req, connection_point=dev_cp)

    return target_file
