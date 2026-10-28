#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_component_explorer.py
Infor LN Studio Remote Component Explorer, Read-Only Reference Sync (`.reference/<type>/`),
Auto-DD Indexer (`.ln_dd_cache.json`), Get & Clone Workflows.

Handles:
1. Component browsing via StudioComponent.GetBrowseList across 12 component types + extensions.
2. In-memory inspection (get-component --inspect) supporting real Ecore (<Column>, <Enumeration>, <expression>).
3. Read-only component download into Activity folders (get-component) or `.reference/<type>/` (sync-reference).
4. Automatic Data Dictionary indexing into `.ln_dd_cache.json` whenever `.tbl` or `.dmn` XMLs are fetched.
5. Component cloning (clone-component) from standard (tc, td, wh) to custom (tx), strictly blocking extensions (ADR 0006).
"""

import fnmatch
import json
import os
import re
import stat
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from ln_server_client import BdeExecutionError, LNStudioServerClient
from scm_guardrails import is_extension_component

BDE_TYPE_MAP = {
    "table": {"bde": "DR_Table", "ext": ".tbl", "subfolder": "tables"},
    "session": {"bde": "DR_Controller", "ext": ".ses", "subfolder": "sessions"},
    "library": {"bde": "DR_Module", "ext": ".lib", "subfolder": "libraries", "type_attr": "library"},
    "extension": {"bde": "DR_Module", "ext": ".lib", "subfolder": "extensions", "type_attr": "extension", "readonly_only": True},
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
    """Splits an LN component name (e.g. 'tcibd001' or 'whwmd4300m000' or 'txcmg.clor') into (package, module, object)."""
    clean = comp_name.strip()
    pkg = clean[:2].lower() if len(clean) >= 2 else ""
    if "." in clean:
        first_part = clean.split(".", 1)[0]
        mod = first_part[2:].lower() if len(first_part) > 2 else ""
        obj = clean.split(".", 1)[1]
    else:
        mod = clean[2:5].lower() if len(clean) >= 5 else ""
        obj = clean[5:] if len(clean) > 5 else ""
    return pkg, mod, obj


def parse_dd_xml_to_entry(xml_content: str, hint_name: str = "") -> Optional[Dict[str, Any]]:
    """
    Parses a `.tbl` (`<DR_Table>`) or `.dmn` (`<DR_Domain>`) XML document (both real Ecore
    `<Column>/<datatype>/<name>` / `<Enumeration>` and mock `<Field>` / `<EnumValue>`)
    into a structured Data Dictionary cache entry.
    """
    try:
        root = ET.fromstring(xml_content.strip())
    except ET.ParseError:
        return None

    # Strip XML namespaces so XPath queries work seamlessly on Ecore xmlns documents
    for el in root.iter():
        if "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]

    root_tag = root.tag

    if root_tag == "DR_Table":
        tbl_name = (root.attrib.get("name") or root.findtext("name") or hint_name).strip().lower()
        if not tbl_name:
            return None
        desc = (root.findtext("description") or root.attrib.get("description") or "").strip()
        fields_map: Dict[str, Dict[str, Any]] = {}
        inferred_domains: Dict[str, Dict[str, Any]] = {}

        # 1. Real Ecore <Column> elements
        for col in root.findall(".//Column"):
            c_name = (col.attrib.get("name") or col.findtext("name") or "").strip().lower()
            if not c_name:
                continue
            dt_node = col.find("datatype")
            dmn_name = ""
            native_dt = ""
            max_len = ""
            if dt_node is not None:
                dmn_name = (dt_node.findtext("name") or dt_node.attrib.get("name") or "").strip()
                native_dt = (dt_node.findtext("nativeDatatype") or dt_node.attrib.get("nativeDatatype") or "").strip()
                for facet in dt_node.findall("Facet"):
                    if facet.findtext("type") == "maxLength":
                        max_len = facet.findtext("value") or ""
            if not dmn_name:
                dmn_name = (col.attrib.get("domain") or col.findtext("domain") or "").strip()
            c_desc = (col.findtext("description") or col.attrib.get("description") or "").strip()
            c_lbl = (col.findtext("descriptionReference") or col.attrib.get("label") or col.findtext("label") or "").strip()
            is_mand = (col.findtext("isMandatory") or col.attrib.get("mandatory") or "false").lower() == "true"
            fields_map[c_name] = {
                "name": c_name,
                "domain": dmn_name,
                "datatype": native_dt,
                "maxLength": max_len,
                "mandatory": is_mand,
                "label": c_lbl,
                "description": c_desc,
            }
            if dmn_name:
                inferred_domains[dmn_name.lower()] = {
                    "name": dmn_name.lower(),
                    "datatype": native_dt,
                    "inferred_from_table": tbl_name,
                }

        # 2. Legacy/mock <Field> elements
        for fld in root.findall(".//Field"):
            f_name = (fld.attrib.get("name") or fld.findtext("name") or "").strip().lower()
            if not f_name or f_name in fields_map:
                continue
            dmn_name = (fld.attrib.get("domain") or fld.findtext("domain") or "").strip()
            if not dmn_name and f_name:
                continue
            native_dt = (fld.attrib.get("type") or fld.findtext("type") or "").strip()
            c_lbl = (fld.attrib.get("label") or fld.findtext("label") or "").strip()
            fields_map[f_name] = {
                "name": f_name,
                "domain": dmn_name,
                "datatype": native_dt,
                "mandatory": (fld.attrib.get("mandatory") or "false").lower() == "true",
                "label": c_lbl,
                "description": (fld.attrib.get("description") or fld.findtext("description") or "").strip(),
            }
            if dmn_name:
                inferred_domains[dmn_name.lower()] = {
                    "name": dmn_name.lower(),
                    "datatype": native_dt,
                    "inferred_from_table": tbl_name,
                }

        indices_dict: Dict[str, List[str]] = {}
        for idx_pos, idx in enumerate(root.findall(".//Index"), start=1):
            idx_name = (idx.attrib.get("name") or idx.attrib.get("number") or idx.findtext("name") or str(idx_pos)).strip()
            cols: List[str] = []
            for ic in idx.findall(".//IndexColumn"):
                col_ref = (
                    ic.findtext("column")
                    or ic.findtext("name")
                    or ic.attrib.get("column")
                    or ic.attrib.get("name")
                    or ""
                ).strip().lower()
                if col_ref:
                    cols.append(col_ref)
            for mf in idx.findall(".//Field"):
                col_ref = (mf.attrib.get("name") or mf.findtext("name") or "").strip().lower()
                if col_ref and col_ref not in cols:
                    cols.append(col_ref)
            indices_dict[str(idx_name)] = cols

        return {
            "kind": "table",
            "name": tbl_name,
            "entry": {
                "name": tbl_name,
                "description": desc,
                "fields": fields_map,
                "indices": indices_dict,
            },
            "inferred_domains": inferred_domains,
        }

    elif root_tag == "DR_Domain":
        dmn_name = (root.attrib.get("name") or root.findtext("name") or hint_name).strip().lower()
        if not dmn_name:
            return None
        desc = (root.findtext("description") or root.attrib.get("description") or "").strip()
        dt_node = root.find("datatype")
        native_dt = ""
        facets: Dict[str, str] = {}
        if dt_node is not None:
            native_dt = (dt_node.findtext("nativeDatatype") or dt_node.attrib.get("nativeDatatype") or "").strip()
            for facet in dt_node.findall("Facet"):
                ftype = (facet.findtext("type") or "").strip()
                fval = (facet.findtext("value") or "").strip()
                if ftype:
                    facets[ftype] = fval
        if not native_dt:
            native_dt = (
                root.findtext("nativeDatatype")
                or root.attrib.get("nativeDatatype")
                or root.attrib.get("type")
                or root.findtext("type")
                or ""
            ).strip()

        enums: Dict[str, Dict[str, Any]] = {}
        for en in root.findall(".//Enumeration"):
            e_name = (
                en.attrib.get("name")
                or en.findtext("name")
                or en.findtext("constant")
                or en.attrib.get("constant")
                or ""
            ).strip()
            if e_name:
                enums[e_name] = {
                    "position": (en.findtext("position") or en.attrib.get("position") or "").strip(),
                    "description": (en.findtext("description") or en.attrib.get("description") or "").strip(),
                    "label": (en.findtext("descriptionReference") or "").strip(),
                }
        for ev in root.findall(".//EnumValue"):
            e_name = (ev.attrib.get("name") or ev.attrib.get("const") or ev.findtext("name") or "").strip()
            if e_name and e_name not in enums:
                enums[e_name] = {
                    "position": (ev.attrib.get("value") or "").strip(),
                    "description": (ev.attrib.get("description") or "").strip(),
                }

        return {
            "kind": "domain",
            "name": dmn_name,
            "entry": {
                "name": dmn_name,
                "description": desc,
                "datatype": native_dt,
                "facets": facets,
                "enums": enums,
                "enum_values": list(enums.keys()),
            },
        }

    return None


def update_dd_cache_from_xml(
    xml_content: str,
    dd_cache_path: Path,
    hint_name: str = "",
) -> Optional[Dict[str, Any]]:
    """
    Parses `.tbl` or `.dmn` XML content and atomically updates `.ln_dd_cache.json`.
    """
    parsed = parse_dd_xml_to_entry(xml_content, hint_name=hint_name)
    if not parsed:
        return None

    cache_data: Dict[str, Any] = {"version": "1.0", "tables": {}, "domains": {}}
    if dd_cache_path.exists():
        try:
            loaded = json.loads(dd_cache_path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                cache_data["tables"] = loaded.get("tables", {}) if isinstance(loaded.get("tables"), dict) else {}
                cache_data["domains"] = loaded.get("domains", {}) if isinstance(loaded.get("domains"), dict) else {}
        except Exception:
            pass

    if parsed["kind"] == "table":
        cache_data["tables"][parsed["name"]] = parsed["entry"]
        for d_name, d_meta in parsed.get("inferred_domains", {}).items():
            if d_name not in cache_data["domains"]:
                cache_data["domains"][d_name] = d_meta
    elif parsed["kind"] == "domain":
        cache_data["domains"][parsed["name"]] = parsed["entry"]

    cache_data["updated_at"] = datetime.now(timezone.utc).isoformat()
    dd_cache_path.parent.mkdir(parents=True, exist_ok=True)
    dd_cache_path.write_text(json.dumps(cache_data, indent=2, ensure_ascii=False), encoding="utf-8")
    return parsed


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
    dd_cache_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Fetches component definition via DR_*.Get and extracts structured schema and 4GL code
    in-memory for AI coding agents without modifying the local Activity directory.
    Supports both real Ecore (<Column>, <Enumeration>, <expression>) and mock (<Field>) XMLs.
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

    if dd_cache_path and comp_type.lower() in ("table", "domain"):
        update_dd_cache_from_xml(resp_xml, dd_cache_path, hint_name=comp_name)

    summary: Dict[str, Any] = {
        "name": comp_name,
        "type": comp_type,
        "package": pkg,
        "module": mod,
        "description": root.findtext(".//description") or "",
        "raw_xml": resp_xml,
    }

    # Extract fields using real Ecore <Column> + legacy <Field>
    fields = []
    parsed_dd = parse_dd_xml_to_entry(resp_xml, hint_name=comp_name)
    if parsed_dd and parsed_dd["kind"] == "table":
        for fname, fmeta in parsed_dd["entry"]["fields"].items():
            fields.append({
                "name": fname,
                "domain": fmeta.get("domain", ""),
                "label": fmeta.get("label", ""),
                "datatype": fmeta.get("datatype", ""),
                "mandatory": fmeta.get("mandatory", False),
            })
        summary["indices"] = parsed_dd["entry"].get("indices", [])
    elif parsed_dd and parsed_dd["kind"] == "domain":
        summary["datatype"] = parsed_dd["entry"].get("datatype", "")
        summary["enums"] = parsed_dd["entry"].get("enums", {})
    else:
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

    # Extract embedded scripts (real Ecore <expression> + mock dalScript/uiScript/scriptText)
    scripts = []
    for tag in ("expression", "dalScript", "uiScript", "scriptText", "Script", "reportScript"):
        for elem in root.findall(f".//{tag}"):
            if elem is not None and elem.text and elem.text.strip():
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
    dd_cache_path: Optional[Path] = None,
) -> Path:
    """
    Fetches component XML from server via DR_*.Get, writes it to activity directory,
    enforces OS Read-Only flag, registers it in .admin SCM cache (except extensions),
    and updates `.ln_dd_cache.json` automatically for `.tbl` and `.dmn` components.
    """
    ctype_lower = comp_type.lower()
    info = BDE_TYPE_MAP.get(ctype_lower)
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    # Enforce Extension Modeler Rule (ADR 0006): Extensions are strictly Read-Only Get
    if ctype_lower == "extension" or info.get("readonly_only"):
        read_only = True

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

    if target_file.exists():
        try:
            os.chmod(target_file, stat.S_IWRITE | stat.S_IREAD)
        except Exception:
            pass

    target_file.write_text(resp_xml, encoding="utf-8")

    if read_only or is_extension_component(target_file):
        try:
            os.chmod(target_file, stat.S_IREAD)
        except Exception:
            pass

    # Auto-index into .ln_dd_cache.json if table or domain
    if ctype_lower in ("table", "domain"):
        eff_dd_path = dd_cache_path or (activity_dir.parent / ".ln_dd_cache.json")
        update_dd_cache_from_xml(resp_xml, eff_dd_path, hint_name=comp_name)

    # Register in .admin cache ONLY if not an extension
    if ctype_lower != "extension" and not is_extension_component(target_file):
        from admin_sync import add_component
        rel_path = target_file.relative_to(activity_dir).as_posix()
        try:
            add_component(activity_dir, rel_path)
        except Exception as e:
            print(f"[WARN] Failed to register {rel_path} in .admin: {e}", file=sys.stderr)

    return target_file


def sync_reference(
    client: LNStudioServerClient,
    comp_type: str,
    name_pattern: str,
    workspace_dir: Optional[Path] = None,
    dd_cache_path: Optional[Path] = None,
    connection_point: str = "ProjectServer",
    workspace_root: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Downloads requested components (`table`, `domain`, `session`, `extension`, etc.)
    in Read-Only reference mode into `<workspace_dir>/.reference/<type>/` without modifying
    any Activity `.admin` file.
    Automatically parses `.tbl` and `.dmn` XMLs and updates `.ln_dd_cache.json`.
    """
    ctype_lower = comp_type.lower()
    info = BDE_TYPE_MAP.get(ctype_lower)
    if not info:
        raise ValueError(
            f"Unsupported component type '{comp_type}'. Supported: {list(BDE_TYPE_MAP.keys())}"
        )

    bde_name = info["bde"]
    ext = info["ext"]
    eff_ws_dir = workspace_dir or workspace_root or Path.cwd()
    ws_root = Path(eff_ws_dir).resolve()
    ref_dir = ws_root / ".reference" / ctype_lower
    ref_dir.mkdir(parents=True, exist_ok=True)
    eff_dd_cache = Path(dd_cache_path).resolve() if dd_cache_path else (ws_root / ".ln_dd_cache.json")

    # Resolve target component names (supports exact name or wildcard pattern like `tcibd*`)
    target_names: List[str] = []
    if "*" in name_pattern or "?" in name_pattern:
        pkg_prefix = re.sub(r"[*?].*$", "", name_pattern)[:2].lower()
        browsed = browse_components(
            client=client,
            package=pkg_prefix,
            comp_type=ctype_lower if ctype_lower != "extension" else "library",
            name_filter=name_pattern,
            connection_point=connection_point,
        )
        for item in browsed:
            cname = item.get("name", "")
            if cname and fnmatch.fnmatch(cname.lower(), name_pattern.lower()):
                target_names.append(cname)
    else:
        target_names = [name_pattern.strip()]

    synced_files: List[str] = []
    dd_indexed: List[str] = []

    for comp_name in target_names:
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
        try:
            resp_xml = client.do_bde_call(bde_name, "Get", req_xml, connection_point=connection_point)
        except Exception:
            continue

        if not resp_xml or not resp_xml.strip():
            continue

        out_file = ref_dir / f"{comp_name}{ext}"
        if out_file.exists():
            try:
                os.chmod(out_file, stat.S_IWRITE | stat.S_IREAD)
            except Exception:
                pass

        out_file.write_text(resp_xml, encoding="utf-8")
        try:
            os.chmod(out_file, stat.S_IREAD)
        except Exception:
            pass

        synced_files.append(str(out_file))

        # Auto-index .tbl and .dmn into .ln_dd_cache.json
        if ctype_lower in ("table", "domain") or "<DR_Table" in resp_xml or "<DR_Domain" in resp_xml:
            indexed = update_dd_cache_from_xml(resp_xml, eff_dd_cache, hint_name=comp_name)
            if indexed:
                dd_indexed.append(indexed["name"])

    return {
        "type": ctype_lower,
        "pattern": name_pattern,
        "reference_dir": str(ref_dir),
        "dd_cache_path": str(eff_dd_cache),
        "synced_count": len(synced_files),
        "count": len(synced_files),
        "files": synced_files,
        "downloaded": [{"name": Path(f).stem, "path": f} for f in synced_files],
        "dd_indexed": dd_indexed,
        "read_only": True,
    }


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
    Strictly blocks Extension Modeler objects per ADR 0006.
    """
    ctype_lower = comp_type.lower()
    if ctype_lower == "extension" or source_name.lower().endswith((".eso", ".eto", ".ere")):
        from scm_guardrails import ReadOnlyComponentError
        raise ReadOnlyComponentError(
            "Extension Modeler Rule (ADR 0006): Extension objects cannot be cloned, checked out, "
            "modified, or pushed to LN Studio. Use 'sync-reference --type extension' for read-only reference "
            "and author extension hooks via manual Copy-Paste in LN UI Cloud (ttext1500m000)."
        )

    info = BDE_TYPE_MAP.get(ctype_lower)
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


class ComponentExplorer:
    """High-level object-oriented wrapper around component exploration and reference sync."""

    def __init__(self, client: LNStudioServerClient):
        self.client = client

    def browse(self, package: str = "", comp_type: str = "", name_filter: str = "") -> List[Dict[str, str]]:
        return browse_components(self.client, package=package, comp_type=comp_type, name_filter=name_filter)

    def inspect(self, comp_type: str, comp_name: str, dd_cache_path: Optional[Path] = None) -> Dict[str, Any]:
        return inspect_component(self.client, comp_type=comp_type, comp_name=comp_name, dd_cache_path=dd_cache_path)

    def get(
        self,
        comp_type: str,
        comp_name: str,
        activity_dir: Path,
        read_only: bool = True,
        dd_cache_path: Optional[Path] = None,
    ) -> Path:
        return get_component(
            self.client,
            comp_type=comp_type,
            comp_name=comp_name,
            activity_dir=activity_dir,
            read_only=read_only,
            dd_cache_path=dd_cache_path,
        )

    def sync_reference(
        self,
        comp_type: str,
        name_pattern: str,
        workspace_dir: Path,
        dd_cache_path: Optional[Path] = None,
    ) -> Dict[str, Any]:
        return sync_reference(
            self.client,
            comp_type=comp_type,
            name_pattern=name_pattern,
            workspace_dir=workspace_dir,
            dd_cache_path=dd_cache_path,
        )
