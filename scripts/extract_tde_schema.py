#!/usr/bin/env python3
"""
TDE Bytecode-to-JSON Schema Extractor & owtemplates Catalog Generator.

Clean-room JVM bytecode classfile parser and template packager for Infor LN Studio 10.8 Build 0640.
Reads `lnstudio_commoncore.jar`, `fourglstudio_core.jar`, and `com.infor.ln.studio.apps.ui`
using Python stdlib (`zipfile`, `struct`, `hashlib`, `json`) and produces:
  1. `rust/schemas/tde_schema_0640.json`
  2. `rust/schemas/owtemplates_0640.json`
  3. `rust/schemas/build_0640_manifest.json`

Enables `skill-ln` and `ln-model` to compile and execute with zero runtime dependency on JDK/JARs.
"""

import argparse
import hashlib
import io
import json
import os
import re
import struct
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# Mapping of TDE root component classes to file extensions and component types
ROOT_COMPONENT_MAP = {
    "DR_Table": {"file_extension": ".tbl", "type_name": "table"},
    "DR_Controller": {"file_extension": ".ses", "type_name": "session"},
    "DR_Domain": {"file_extension": ".dmn", "type_name": "domain"},
    "DR_Label": {"file_extension": ".lbl", "type_name": "label"},
    "DR_Menu": {"file_extension": ".mnu", "type_name": "menu"},
    "DR_Message": {"file_extension": ".msg", "type_name": "message"},
    "DR_Question": {"file_extension": ".qst", "type_name": "question"},
    "DR_Report": {"file_extension": ".rpt", "type_name": "report"},
    "DR_AdditionalFile": {"file_extension": ".add", "type_name": "additional"},
    "DR_BusinessObject": {"file_extension": ".bus", "type_name": "business_object"},
    "DR_Module": {"file_extension": ".lib", "type_name": "library"},
    "Procedure": {"file_extension": ".fnc", "type_name": "function"},
    "DR_Solution": {"file_extension": ".sol", "type_name": "solution"},
}


def parse_class_bytes(data: bytes) -> Dict[str, Any]:
    """Parse JVM classfile format (.class) constant pool, fields, and attributes."""
    if len(data) < 10:
        raise ValueError("Classfile too short")
    magic, minor, major, cp_count = struct.unpack(">IHHH", data[:10])
    if magic != 0xCAFEBABE:
        raise ValueError(f"Invalid magic: {hex(magic)}, expected 0xCAFEBABE")

    offset = 10
    cp: List[Any] = [None] * cp_count
    idx = 1
    while idx < cp_count:
        tag = data[offset]
        offset += 1
        if tag == 1:  # Utf8
            length, = struct.unpack(">H", data[offset : offset + 2])
            offset += 2
            val = data[offset : offset + length].decode("utf-8", errors="replace")
            offset += length
            cp[idx] = ("Utf8", val)
        elif tag in (3, 4):  # Integer, Float
            val_bytes = data[offset : offset + 4]
            offset += 4
            cp[idx] = (tag, val_bytes)
        elif tag in (5, 6):  # Long, Double
            val_bytes = data[offset : offset + 8]
            offset += 8
            cp[idx] = (tag, val_bytes)
            idx += 1  # 8-byte constants take two slots
        elif tag in (7, 8):  # Class, String
            ref, = struct.unpack(">H", data[offset : offset + 2])
            offset += 2
            cp[idx] = ("Class" if tag == 7 else "String", ref)
        elif tag in (9, 10, 11, 12, 17, 18):  # Fieldref, Methodref, InterfaceMethodref, NameAndType, Dynamic, InvokeDynamic
            a, b = struct.unpack(">HH", data[offset : offset + 4])
            offset += 4
            cp[idx] = (tag, (a, b))
        elif tag == 15:  # MethodHandle
            offset += 3
            cp[idx] = (tag, None)
        elif tag in (16, 19, 20):  # MethodType, Module, Package
            offset += 2
            cp[idx] = (tag, None)
        else:
            raise ValueError(f"Unknown constant pool tag: {tag} at offset {offset-1}")
        idx += 1

    access_flags, this_class, super_class, interfaces_count = struct.unpack(">HHHH", data[offset : offset + 8])
    offset += 8 + interfaces_count * 2

    this_class_name = cp[cp[this_class][1]][1].replace("/", ".")
    super_class_name = cp[cp[super_class][1]][1].replace("/", ".") if super_class > 0 else None

    fields_count, = struct.unpack(">H", data[offset : offset + 2])
    offset += 2
    declared_fields = []
    serial_version_uid = None

    for _ in range(fields_count):
        f_flags, f_name_idx, f_desc_idx, f_attrs_count = struct.unpack(">HHHH", data[offset : offset + 8])
        offset += 8
        f_name = cp[f_name_idx][1]
        f_desc = cp[f_desc_idx][1]
        f_sig = None
        c_val = None

        for _ in range(f_attrs_count):
            attr_name_idx, attr_len = struct.unpack(">HI", data[offset : offset + 6])
            offset += 6
            attr_name = cp[attr_name_idx][1]
            if attr_name == "Signature":
                sig_idx, = struct.unpack(">H", data[offset : offset + 2])
                f_sig = cp[sig_idx][1]
            elif attr_name == "ConstantValue":
                cv_idx, = struct.unpack(">H", data[offset : offset + 2])
                c_val = cp[cv_idx]
            offset += attr_len

        if f_name == "serialVersionUID" and c_val:
            try:
                # 8 bytes long big-endian
                serial_version_uid, = struct.unpack(">q", c_val[1])
            except Exception:
                pass

        is_public = bool(f_flags & 1)
        is_protected = bool(f_flags & 4)
        is_static = bool(f_flags & 8)

        # For TDE, reflection accesses public non-static fields.
        # For EMF/Ecore (.additional.*), protected fields model child features.
        if (is_public or (is_protected and "additional" in this_class_name)) and not is_static:
            if not f_name.endswith("_EDEFAULT") and f_name != "eFlags":
                declared_fields.append((f_name, f_desc, f_sig))

    methods_count, = struct.unpack(">H", data[offset : offset + 2])
    offset += 2
    for _ in range(methods_count):
        _, _, _, m_attrs_count = struct.unpack(">HHHH", data[offset : offset + 8])
        offset += 8
        for _ in range(m_attrs_count):
            _, attr_len = struct.unpack(">HI", data[offset : offset + 6])
            offset += 6 + attr_len

    return {
        "full_name": this_class_name,
        "name": this_class_name.split(".")[-1],
        "super_class": super_class_name,
        "declared_fields": declared_fields,
        "serial_version_uid": serial_version_uid,
    }


def resolve_field_kind_and_target(fname: str, fdesc: str, fsig: Optional[str]) -> Tuple[str, Optional[str]]:
    """Determines XML field kind ('string', 'cdata', 'list', 'object') and target class type."""
    if fname in ("_cdata", "#cdata-section"):
        return "cdata", None

    if fdesc == "Ljava/util/List;" or fdesc.startswith("Ljava/util/"):
        kind = "list"
        if fsig:
            m = re.search(r"<L([^;>]+);>", fsig)
            if m:
                target = m.group(1).replace("/", ".").split(".")[-1]
            else:
                target = "String"
        else:
            target = "Object"
        return kind, target

    primitive_or_string = (
        "Ljava/lang/String;",
        "I", "Z", "J", "D", "F", "S", "B", "C",
        "Ljava/lang/Boolean;", "Ljava/lang/Integer;", "Ljava/lang/Long;", "Ljava/lang/Double;",
    )
    if fdesc in primitive_or_string:
        return "string", None

    if fdesc.startswith("L"):
        target_full = fdesc[1:-1].replace("/", ".")
        target = target_full.split(".")[-1]
        return "object", target

    return "string", None


def extract_schema(studio_dir: Path, output_dir: Path) -> Dict[str, Any]:
    """Extracts TDE classes, owtemplates, and build manifest into JSON schemas."""
    plugins_dir = studio_dir / "plugins"
    common_core_plugin_jar = None
    apps_core_plugin_jar = None
    apps_ui_dir = None

    if plugins_dir.exists():
        for item in plugins_dir.iterdir():
            name = item.name
            if name.startswith("com.infor.ln.studio.common.core_") and name.endswith(".jar"):
                common_core_plugin_jar = item
            elif name.startswith("com.infor.ln.studio.apps.core_") and name.endswith(".jar"):
                apps_core_plugin_jar = item
            elif name.startswith("com.infor.ln.studio.apps.ui_") and item.is_dir():
                apps_ui_dir = item

    # Fallbacks if running from cached jars or different layout
    if not common_core_plugin_jar:
        cand = Path.home() / ".ln_studio" / "jars" / "lnstudio_commoncore.jar"
        if cand.exists():
            print(f"Using fallback lnstudio_commoncore.jar at {cand}")

    print(f"Reading common.core from: {common_core_plugin_jar}")
    print(f"Reading apps.core from: {apps_core_plugin_jar}")
    print(f"Reading apps.ui from: {apps_ui_dir}")

    # 1. Read inner JARs
    z_common_outer = zipfile.ZipFile(common_core_plugin_jar)
    inner_common_bytes = z_common_outer.read("lnstudio_commoncore.jar")
    z_common_inner = zipfile.ZipFile(io.BytesIO(inner_common_bytes))

    z_apps_outer = zipfile.ZipFile(apps_core_plugin_jar)
    inner_apps_bytes = z_apps_outer.read("fourglstudio_core.jar")
    z_apps_inner = zipfile.ZipFile(io.BytesIO(inner_apps_bytes))

    # 2. Collect class entries
    tde_entries = [
        n for n in z_common_inner.namelist()
        if (n.startswith("com/infor/ln/studio/common/core/model/tde/")
            or "DR_Solution" in n)
        and n.endswith(".class")
    ]

    add_entries = [
        n for n in z_apps_inner.namelist()
        if n.startswith("com/infor/ln/studio/apps/core/model/additional/")
        and n.endswith(".class")
    ]

    print(f"Discovered {len(tde_entries)} TDE/PS classfiles and {len(add_entries)} Additional classfiles.")

    raw_classes: Dict[str, Dict[str, Any]] = {}
    class_manifest: Dict[str, Any] = {}

    for entry in tde_entries:
        data = z_common_inner.read(entry)
        parsed = parse_class_bytes(data)
        full_name = parsed["full_name"]
        raw_classes[full_name] = parsed
        class_manifest[full_name] = {
            "sha256": hashlib.sha256(data).hexdigest(),
            "serial_version_uid": parsed["serial_version_uid"],
            "field_count": len(parsed["declared_fields"]),
        }

    for entry in add_entries:
        data = z_apps_inner.read(entry)
        parsed = parse_class_bytes(data)
        full_name = parsed["full_name"]
        raw_classes[full_name] = parsed
        class_manifest[full_name] = {
            "sha256": hashlib.sha256(data).hexdigest(),
            "serial_version_uid": parsed["serial_version_uid"],
            "field_count": len(parsed["declared_fields"]),
        }

    # 3. Build class hierarchy & resolve fields
    schema_classes: Dict[str, Any] = {}
    classes_by_full_name: Dict[str, Any] = {}

    for full_name, parsed in raw_classes.items():
        simple_name = parsed["name"]
        root_info = ROOT_COMPONENT_MAP.get(simple_name)
        is_root = root_info is not None
        file_ext = root_info["file_extension"] if root_info else None

        fields_meta = []
        for fname, fdesc, fsig in parsed["declared_fields"]:
            kind, target = resolve_field_kind_and_target(fname, fdesc, fsig)
            fields_meta.append({
                "name": fname,
                "kind": kind,
                "target_type": target,
                "descriptor": fdesc,
            })

        class_def = {
            "name": simple_name,
            "full_name": full_name,
            "super_class": parsed["super_class"],
            "is_root_component": is_root,
            "file_extension": file_ext,
            "fields": fields_meta,
        }
        classes_by_full_name[full_name] = class_def

    # Precompute flattened all_fields (inherited fields from root/base to leaf)
    for full_name, c_def in classes_by_full_name.items():
        chain = []
        curr = full_name
        seen = set()
        while curr and curr not in seen and curr != "java.lang.Object":
            seen.add(curr)
            if curr in classes_by_full_name:
                chain.append(classes_by_full_name[curr])
                curr = classes_by_full_name[curr].get("super_class")
            else:
                break
        
        # Superclasses first (TDEProperties -> LabeledComponent -> Concrete)
        chain.reverse()
        all_fields_map: Dict[str, Any] = {}
        for ancestor in chain:
            for f in ancestor["fields"]:
                all_fields_map[f["name"]] = f
        c_def["all_fields"] = list(all_fields_map.values())

    # Map both simple name and full name in schema
    for full_name, c_def in classes_by_full_name.items():
        simple_name = c_def["name"]
        if simple_name not in schema_classes:
            schema_classes[simple_name] = c_def
        schema_classes[full_name] = c_def

    # 4. Extract owtemplates and ScriptTemplates
    templates_catalog: Dict[str, Any] = {
        "owtemplates": {},
        "script_templates": {},
    }

    # From common.core
    for name in z_common_outer.namelist():
        if name.startswith("owtemplates/") and name.endswith(".xml"):
            xml_bytes = z_common_outer.read(name)
            xml_str = xml_bytes.decode("utf-8", errors="replace")
            tname = os.path.basename(name)
            m_root = re.search(r"<([a-zA-Z0-9_]+)[\s>]", xml_str)
            root_tag = m_root.group(1) if m_root else "Unknown"
            templates_catalog["owtemplates"][tname] = {
                "name": tname,
                "source": "common.core",
                "root_tag": root_tag,
                "sha256": hashlib.sha256(xml_bytes).hexdigest(),
                "content": xml_str,
            }
        elif name.startswith("ScriptTemplates/") and not name.endswith("/"):
            tpl_bytes = z_common_outer.read(name)
            tpl_str = tpl_bytes.decode("utf-8", errors="replace")
            sname = os.path.basename(name)
            templates_catalog["script_templates"][sname] = {
                "name": sname,
                "source": "common.core",
                "sha256": hashlib.sha256(tpl_bytes).hexdigest(),
                "content": tpl_str,
            }

    # From apps.ui
    if apps_ui_dir:
        ui_ow_dir = apps_ui_dir / "owtemplates"
        if ui_ow_dir.is_dir():
            for f in ui_ow_dir.glob("*.xml"):
                xml_bytes = f.read_bytes()
                xml_str = xml_bytes.decode("utf-8", errors="replace")
                m_root = re.search(r"<([a-zA-Z0-9_]+)[\s>]", xml_str)
                root_tag = m_root.group(1) if m_root else "Unknown"
                templates_catalog["owtemplates"][f.name] = {
                    "name": f.name,
                    "source": "apps.ui",
                    "root_tag": root_tag,
                    "sha256": hashlib.sha256(xml_bytes).hexdigest(),
                    "content": xml_str,
                }

    print(f"Extracted {len(templates_catalog['owtemplates'])} owtemplates and {len(templates_catalog['script_templates'])} ScriptTemplates.")

    # 5. Build Manifest
    build_manifest = {
        "build_id": "10_8_0_build0640-x86_64",
        "jars": {
            "com.infor.ln.studio.common.core": {
                "path": str(common_core_plugin_jar),
                "sha256": hashlib.sha256(common_core_plugin_jar.read_bytes()).hexdigest(),
            },
            "lnstudio_commoncore.jar": {
                "sha256": hashlib.sha256(inner_common_bytes).hexdigest(),
                "class_count": len(tde_entries),
            },
            "com.infor.ln.studio.apps.core": {
                "path": str(apps_core_plugin_jar),
                "sha256": hashlib.sha256(apps_core_plugin_jar.read_bytes()).hexdigest(),
            },
            "fourglstudio_core.jar": {
                "sha256": hashlib.sha256(inner_apps_bytes).hexdigest(),
                "class_count": len(add_entries),
            },
        },
        "classes": class_manifest,
    }

    # 6. Output Files
    output_dir.mkdir(parents=True, exist_ok=True)
    tde_schema_file = output_dir / "tde_schema_0640.json"
    owtemplates_file = output_dir / "owtemplates_0640.json"
    manifest_file = output_dir / "build_0640_manifest.json"

    tde_payload = {
        "version": "10.8.0.0640",
        "root_components": ROOT_COMPONENT_MAP,
        "classes": schema_classes,
    }

    tde_schema_file.write_text(json.dumps(tde_payload, indent=2, ensure_ascii=False), encoding="utf-8")
    owtemplates_file.write_text(json.dumps(templates_catalog, indent=2, ensure_ascii=False), encoding="utf-8")
    manifest_file.write_text(json.dumps(build_manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[OK] Wrote schema to {tde_schema_file} ({os.path.getsize(tde_schema_file):,} bytes)")
    print(f"[OK] Wrote templates to {owtemplates_file} ({os.path.getsize(owtemplates_file):,} bytes)")
    print(f"[OK] Wrote manifest to {manifest_file} ({os.path.getsize(manifest_file):,} bytes)")

    return tde_payload


def main():
    parser = argparse.ArgumentParser(description="Extract Infor LN Studio 10.8 Build 0640 TDE Bytecode Schema")
    parser.add_argument(
        "--studio-dir",
        type=Path,
        default=Path(r"D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64"),
        help="Path to Infor LN Studio installation directory",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("rust/schemas"),
        help="Output directory for generated JSON schemas",
    )
    args = parser.parse_args()

    extract_schema(args.studio_dir, args.output_dir)


if __name__ == "__main__":
    main()
