#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_schema_parser.py
Declarative Schema Specification & Validation Engine for Infor LN Studio.

Validates and normalizes multi-component and legacy single-table specifications:
Tables, Columns, Indices, References, Domains (all datatypes), Sessions (all archetypes),
Libraries (DLL, Session Extension, Table Extension), and Menus according to Infor LN Studio 10.8 rules.
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple, Union

try:
    import yaml
except ImportError:
    yaml = None

# Validation Regexes
TABLE_CODE_PATTERN = re.compile(r"^([a-z]{2})([a-z0-9]{3})(\d{3})$")
FIELD_NAME_PATTERN = re.compile(r"^[a-z0-9_]{1,8}$")
SESSION_CODE_PATTERN = re.compile(r"^([a-z]{2})([a-z0-9]{3})(\d{4})([msrd]\d{3})$")
MENU_CODE_PATTERN = re.compile(r"^([a-z]{2})([a-z0-9]{3})(\d{4})([msrd]\d{3})$")

# Standard Infor LN Native Datatype Mappings
# 1 = Byte, 2 = Double/Float, 3 = Long/Integer, 5 = Numeric/Amount, 6 = String/Multibyte,
# 7 = Enum/Boolean, 9 = Date, 14 = UtcDateTime
DATA_TYPE_MAP = {
    "byte": 1,
    "double": 2,
    "float": 2,
    "long": 3,
    "integer": 3,
    "int": 3,
    "numeric": 5,
    "amount": 5,
    "amnt": 5,
    "string": 6,
    "str": 6,
    "text": 6,
    "multibyte": 6,
    "enum": 7,
    "enumeration": 7,
    "boolean": 7,
    "bool": 7,
    "date": 9,
    "utc": 14,
    "datetime": 14,
    "utcdatetime": 14,
}

# Known standard domains to nativeDatatype and default facets
STANDARD_DOMAINS = {
    "tcpono": {"nativeDatatype": 3, "minLength": "1", "maxLength": "6"},
    "tcmcs.long": {"nativeDatatype": 3, "minLength": "1", "maxLength": "9"},
    "tcyesno": {"nativeDatatype": 7, "minLength": "1", "maxLength": "20"},
    "tcbool": {"nativeDatatype": 7, "minLength": "1", "maxLength": "20"},
    "tccwar": {"nativeDatatype": 6, "minLength": "1", "maxLength": "6"},
    "tcdsca": {"nativeDatatype": 6, "minLength": "1", "maxLength": "30"},
    "tcmcs.str1": {"nativeDatatype": 6, "minLength": "1", "maxLength": "1"},
    "tcmcs.str3": {"nativeDatatype": 6, "minLength": "1", "maxLength": "3"},
    "tcmcs.str6": {"nativeDatatype": 6, "minLength": "1", "maxLength": "6"},
    "tcmcs.str30": {"nativeDatatype": 6, "minLength": "1", "maxLength": "30"},
    "tcmcs.str35": {"nativeDatatype": 6, "minLength": "1", "maxLength": "35"},
    "tcmcs.cmnf": {"nativeDatatype": 6, "minLength": "1", "maxLength": "6"},
    "tcmpnr": {"nativeDatatype": 6, "minLength": "1", "maxLength": "35"},
    "tcctit": {"nativeDatatype": 6, "minLength": "1", "maxLength": "3"},
    "tcdate": {"nativeDatatype": 9, "minLength": "1", "maxLength": "10"},
    "tfgld.date": {"nativeDatatype": 9, "minLength": "1", "maxLength": "10"},
    "tfgld.amnt": {"nativeDatatype": 5, "minLength": "1", "maxLength": "19"},
    "tfgld.user": {"nativeDatatype": 6, "minLength": "1", "maxLength": "16"},
    "tfgld.btno": {"nativeDatatype": 3, "minLength": "1", "maxLength": "8"},
    "tcutc": {"nativeDatatype": 14, "minLength": "1", "maxLength": "20"},
}


class SchemaValidationError(Exception):
    """Raised when schema violates Infor LN data dictionary constraints."""
    def __init__(self, errors: List[str]):
        super().__init__("\n".join(errors))
        self.errors = errors


def load_raw_schema(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Loads YAML or JSON schema file into dictionary."""
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"Schema file not found: {p}")

    ext = p.suffix.lower()
    with open(p, "r", encoding="utf-8") as f:
        if ext in (".yaml", ".yml"):
            if yaml is None:
                raise ImportError("PyYAML is required to parse YAML schemas. Run 'pip install pyyaml'.")
            return yaml.safe_load(f) or {}
        elif ext == ".json":
            return json.load(f)
        else:
            content = f.read()
            if yaml is not None:
                try:
                    return yaml.safe_load(content) or {}
                except Exception:
                    pass
            return json.loads(content)


def resolve_native_datatype(domain_name: str, explicit_type: Optional[str] = None) -> Tuple[int, Dict[str, str]]:
    """Resolves nativeDatatype code (e.g. 1, 2, 3, 5, 6, 7, 9, 14) and facets for a domain."""
    d_lower = domain_name.lower()

    if explicit_type:
        t_lower = explicit_type.lower()
        if t_lower in DATA_TYPE_MAP:
            code = DATA_TYPE_MAP[t_lower]
            default_lens = {1: "3", 2: "17", 3: "9", 5: "19", 6: "30", 7: "20", 9: "10", 14: "20"}
            return code, {"maxLength": default_lens.get(code, "30"), "minLength": "1"}

    if d_lower in STANDARD_DOMAINS:
        info = STANDARD_DOMAINS[d_lower]
        return info["nativeDatatype"], {"minLength": info.get("minLength", "1"), "maxLength": info.get("maxLength", "30")}

    # Infer by domain prefix/common patterns
    if d_lower.startswith(("tcpono", "seq", "nr", "cnt", "long", "int")):
        return 3, {"minLength": "1", "maxLength": "9"}
    if d_lower.startswith(("tcyesno", "txskip", "txoutm", "enum", "bool")):
        return 7, {"minLength": "1", "maxLength": "20"}
    if d_lower.startswith(("amnt", "amount", "num")):
        return 5, {"minLength": "1", "maxLength": "19"}
    if d_lower.startswith(("date",)):
        return 9, {"minLength": "1", "maxLength": "10"}
    if d_lower.startswith(("utc",)):
        return 14, {"minLength": "1", "maxLength": "20"}
    if d_lower.startswith(("byte",)):
        return 1, {"minLength": "1", "maxLength": "3"}
    if d_lower.startswith(("double", "float")):
        return 2, {"minLength": "1", "maxLength": "17"}

    # Default to String
    return 6, {"minLength": "1", "maxLength": "30"}


def normalize_single_table(
    raw_tbl: Dict[str, Any],
    default_version_id: str,
    default_application: str,
    errors: List[str]
) -> Dict[str, Any]:
    """Validates and normalizes an individual table specification."""
    if isinstance(raw_tbl.get("table"), dict):
        t_info = raw_tbl["table"]
        table_code = (t_info.get("code") or t_info.get("name") or "").lower()
        module = t_info.get("module") or raw_tbl.get("module")
        package = t_info.get("package") or raw_tbl.get("package")
        description = t_info.get("description") or raw_tbl.get("description", "")
        version_id = t_info.get("version_id") or raw_tbl.get("version_id", default_version_id)
        application = t_info.get("application") or raw_tbl.get("application", default_application)
    else:
        table_code = (raw_tbl.get("code") or raw_tbl.get("name") or str(raw_tbl.get("table", ""))).lower()
        module = raw_tbl.get("module")
        package = raw_tbl.get("package")
        description = raw_tbl.get("description", "")
        version_id = raw_tbl.get("version_id", default_version_id)
        application = raw_tbl.get("application", default_application)

    if not table_code:
        errors.append("Table definition missing 'code' or 'name'.")
        return {}

    m = TABLE_CODE_PATTERN.match(table_code)
    if not m:
        errors.append(
            f"Invalid table code '{table_code}'. Must be 2-char package + 3-char module + 3-digit number (e.g. 'txptc100')."
        )
        return {}

    inferred_pkg, inferred_mod, _ = m.groups()
    if not package:
        package = inferred_pkg
    elif package.lower() != inferred_pkg:
        errors.append(f"Package '{package}' does not match prefix of table code '{table_code}'.")

    if not module:
        module = inferred_mod
    elif module.lower() != inferred_mod:
        errors.append(f"Module '{module}' does not match table code '{table_code}'.")

    # Fields
    raw_fields = raw_tbl.get("fields", [])
    if not raw_fields:
        errors.append(f"Table '{table_code}' must define at least one field under 'fields'.")

    normalized_fields = []
    field_names = set()

    for idx, f in enumerate(raw_fields, start=1):
        if not isinstance(f, dict):
            errors.append(f"Table '{table_code}' field item {idx} must be a dictionary.")
            continue

        fname = (f.get("name") or "").lower()
        if not fname:
            errors.append(f"Table '{table_code}' field {idx} is missing 'name'.")
            continue

        if not FIELD_NAME_PATTERN.match(fname):
            errors.append(
                f"Invalid field name '{fname}' in table '{table_code}'. Must be 1-8 lowercase alphanumeric characters."
            )

        if fname in field_names:
            errors.append(f"Duplicate field name '{fname}' in table '{table_code}'.")
        field_names.add(fname)

        f_desc = f.get("description") or fname.capitalize()
        f_domain = f.get("domain") or f.get("datatype") or "tcmcs.str30"
        f_mandatory = bool(f.get("mandatory", False))
        f_nullable = bool(f.get("nullable", not f_mandatory))
        f_active = bool(f.get("active", True))
        f_default = str(f.get("default", f.get("default_value", "")))
        f_type_hint = f.get("type")

        native_dt, facets = resolve_native_datatype(f_domain, f_type_hint)

        if "length" in f:
            facets["maxLength"] = str(f["length"])
        elif "max_length" in f:
            facets["maxLength"] = str(f["max_length"])

        # Workbench label convention: <pkg><table_code>.<column> (e.g. txtxcmg010.user)
        field_label = f.get("label_code") or f"{package}{table_code}.{fname}"

        normalized_fields.append({
            "name": fname,
            "description": f_desc,
            "domain": f_domain,
            "position": f.get("position", idx),
            "mandatory": f_mandatory,
            "nullable": f_nullable,
            "active": f_active,
            "default_value": f_default,
            "native_datatype": native_dt,
            "facets": facets,
            "label_code": field_label,
            "zoom_program": f.get("zoom_program", ""),
            "zoom_return_field": f.get("zoom_return_field", ""),
        })

    # Indices
    raw_indices = raw_tbl.get("indices", [])
    normalized_indices = []

    if not raw_indices and normalized_fields:
        first_field = normalized_fields[0]["name"]
        raw_indices = [{
            "id": 1,
            "description": "Primary Key",
            "columns": [first_field],
            "unique": True,
            "primary_key": True
        }]

    has_pk = False
    for idx_item in raw_indices:
        idx_id = idx_item.get("id") or idx_item.get("index_number", 1)
        idx_desc = idx_item.get("description", f"Index {idx_id}")
        idx_cols = idx_item.get("columns", [])
        idx_unique = bool(idx_item.get("unique", False))
        idx_pk = bool(idx_item.get("primary_key", False))

        if idx_pk:
            if has_pk:
                errors.append(f"Table '{table_code}' has multiple primary keys defined.")
            has_pk = True
            idx_unique = True

        for c in idx_cols:
            if c not in field_names:
                errors.append(f"Index {idx_id} in table '{table_code}' references undefined field '{c}'.")

        idx_label = idx_item.get("label_code") or f"{table_code}{idx_id:03d}"

        normalized_indices.append({
            "id": idx_id,
            "description": idx_desc,
            "columns": idx_cols,
            "unique": idx_unique,
            "primary_key": idx_pk,
            "label_code": idx_label
        })

    # References
    raw_refs = raw_tbl.get("references", [])
    normalized_refs = []
    for r_idx, r in enumerate(raw_refs, start=1):
        ref_table = r.get("reference_table") or r.get("to_table")
        if not ref_table:
            errors.append(f"Table '{table_code}' reference {r_idx} missing 'reference_table'.")
            continue

        ref_mode = r.get("reference_mode", "mandatory_not_delete_restricted")
        from_cols = r.get("from_columns", r.get("from_fields", []))
        to_cols = r.get("to_columns", r.get("to_fields", []))

        normalized_refs.append({
            "reference_table": ref_table.lower(),
            "reference_mode": ref_mode,
            "from_columns": from_cols,
            "to_columns": to_cols,
            "name": r.get("name", f"ref_{ref_table}")
        })

    return {
        "code": table_code,
        "package": package,
        "module": module,
        "description": description or table_code,
        "version_id": version_id,
        "application": application,
        "label_code": table_code,
        "fields": normalized_fields,
        "indices": normalized_indices,
        "references": normalized_refs
    }


def validate_and_normalize_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates LN declarative schema and returns a normalized multi-component dictionary.
    Supports multi-table specifications and legacy single-table specifications seamlessly.
    """
    errors: List[str] = []

    version_id = schema.get("version_id", "B61O_a_ext")
    application = schema.get("application", "")

    # 1. Normalize Tables
    tables_list: List[Dict[str, Any]] = []
    raw_tables = schema.get("tables")
    if raw_tables is not None and isinstance(raw_tables, list):
        for raw_t in raw_tables:
            norm_t = normalize_single_table(raw_t, version_id, application, errors)
            if norm_t:
                tables_list.append(norm_t)
    elif "table" in schema or "fields" in schema:
        # Legacy single-table schema
        norm_t = normalize_single_table(schema, version_id, application, errors)
        if norm_t:
            tables_list.append(norm_t)

    # 2. Normalize Domains
    raw_domains = schema.get("domains", [])
    normalized_domains = []
    for d in raw_domains:
        if isinstance(d, dict):
            d_name = d.get("name", "").lower()
            d_desc = d.get("description", d_name)
            d_type = (d.get("type") or "enum").lower()
            d_len = d.get("length")
            d_disp_len = d.get("display_length", d_len or 20)

            native_dt, facets = resolve_native_datatype(d_name, d_type)
            if d_len:
                facets["maxLength"] = str(d_len)

            enums = d.get("enums", d.get("constants", []))
            normalized_enums = []
            for e_pos, enum_val in enumerate(enums, start=1):
                if isinstance(enum_val, dict):
                    e_name = enum_val.get("name")
                    e_desc = enum_val.get("description", e_name)
                    e_pos_val = enum_val.get("position", e_pos * 10)
                    e_lbl = enum_val.get("label_code", f"{d_name}{e_pos_val:03d}")
                else:
                    e_name = str(enum_val)
                    e_desc = str(enum_val).replace(".", " ").capitalize()
                    e_pos_val = e_pos * 10
                    e_lbl = f"{d_name}{e_pos_val:03d}"

                normalized_enums.append({
                    "name": e_name,
                    "description": e_desc,
                    "position": e_pos_val,
                    "label_code": e_lbl
                })

            normalized_domains.append({
                "name": d_name,
                "description": d_desc,
                "type": d_type,
                "native_datatype": native_dt,
                "facets": facets,
                "display_length": d_disp_len,
                "enums": normalized_enums,
                "version_id": version_id,
                "application": application
            })

    # 3. Normalize Sessions
    normalized_sessions = []
    raw_sessions = schema.get("sessions")
    if raw_sessions is None:
        # Check single legacy session
        single_ses = schema.get("session")
        if single_ses:
            raw_sessions = [single_ses]
        else:
            raw_sessions = []

    for s in raw_sessions:
        if isinstance(s, str):
            ses_code = s.lower()
            ses_desc = s
            ses_type = "maintain_list"
            ses_table = tables_list[0]["code"] if tables_list else ""
            satellites = []
            form_cmds = []
        elif isinstance(s, dict):
            ses_code = (s.get("code") or "").lower()
            ses_desc = s.get("description", ses_code)
            ses_type = s.get("type", "maintain_list").lower()
            ses_table = s.get("table", tables_list[0]["code"] if tables_list else "").lower()
            satellites = s.get("satellites", [])
            form_cmds = s.get("form_commands", [])
        else:
            continue

        if not ses_code and ses_table:
            ses_code = f"{ses_table[:2]}{ses_table[2:5]}1100m000".lower()

        if not SESSION_CODE_PATTERN.match(ses_code):
            errors.append(
                f"Invalid session code '{ses_code}'. Convention: 2-pkg + 3-mod + 4-num + m/s/r/d + 3-ver (e.g. 'txptc1100m000')."
            )

        # Map archetypes to window_type and sub_type
        # window_type: 1=MainWindow, 2=ListWindow, 3=MMTController
        # sub_type: 1=Maintain, 2=Display, 3=Process, 4=Print
        if ses_type == "maintain_details":
            w_type, s_type = 1, 1
        elif ses_type == "mmt_controller":
            w_type, s_type = 3, 1
        elif ses_type == "satellite":
            w_type, s_type = 1, 1
        elif ses_type == "display":
            w_type, s_type = 1, 2
        elif ses_type == "process":
            w_type, s_type = 1, 3
        elif ses_type == "print":
            w_type, s_type = 1, 4
        else:  # maintain_list (default)
            w_type, s_type = 2, 1

        norm_form_cmds = []
        for c_idx, cmd in enumerate(form_cmds, start=1):
            if isinstance(cmd, dict):
                c_name = cmd.get("name", f"exec.user.{c_idx-1}")
                c_fn = cmd.get("function", c_name)
                c_lbl = cmd.get("label_code", f"{ses_code}.cmd{c_idx}")
                c_desc = cmd.get("description", c_name)
                norm_form_cmds.append({
                    "name": c_name,
                    "function": c_fn,
                    "label_code": c_lbl,
                    "description": c_desc,
                    "position": cmd.get("position", str(c_idx)),
                    "sequence": cmd.get("sequence", str(c_idx * 10))
                })

        normalized_sessions.append({
            "code": ses_code,
            "description": ses_desc,
            "type": ses_type,
            "window_type": w_type,
            "sub_type": s_type,
            "table": ses_table,
            "satellites": satellites,
            "form_commands": norm_form_cmds,
            "label_code": ses_code,
            "version_id": version_id,
            "application": application
        })

    # 4. Normalize Libraries
    normalized_libraries = []
    for lib in schema.get("libraries", []):
        if isinstance(lib, dict):
            l_code = (lib.get("code") or "").lower()
            l_mod = (lib.get("module") or (l_code[2:5] if len(l_code) >= 5 else "gen")).lower()
            l_type = (lib.get("type") or "dll").lower()
            l_target = (lib.get("target") or "").lower()
            l_desc = lib.get("description", l_code)
            normalized_libraries.append({
                "code": l_code,
                "module": l_mod,
                "type": l_type,
                "target": l_target,
                "description": l_desc,
                "version_id": version_id,
                "application": application
            })

    # 5. Normalize Menus
    normalized_menus = []
    for mnu in schema.get("menus", []):
        if isinstance(mnu, dict):
            m_code = (mnu.get("code") or "").lower()
            m_mod = (mnu.get("module") or (m_code[2:5] if len(m_code) >= 5 else "gen")).lower()
            m_desc = mnu.get("description", m_code)
            m_choices = []
            for ch in mnu.get("choices", []):
                if isinstance(ch, dict):
                    ch_pos = ch.get("position", 10)
                    ch_type_str = ch.get("type", "session").lower()
                    ch_type_code = 1 if ch_type_str == "session" else 2
                    ch_target = ch.get("target", "")
                    ch_desc = ch.get("description", ch_target)
                    m_choices.append({
                        "position": ch_pos,
                        "type": ch_type_str,
                        "type_code": ch_type_code,
                        "target": ch_target,
                        "description": ch_desc
                    })
            normalized_menus.append({
                "code": m_code,
                "module": m_mod,
                "description": m_desc,
                "choices": m_choices,
                "version_id": version_id,
                "application": application
            })

    if errors:
        raise SchemaValidationError(errors)

    # Construct unified normalized model with backward-compatible aliases
    first_table = tables_list[0] if tables_list else {}
    first_session = normalized_sessions[0] if normalized_sessions else None

    result = {
        "version_id": version_id,
        "application": application,
        "tables": tables_list,
        "domains": normalized_domains,
        "sessions": normalized_sessions,
        "libraries": normalized_libraries,
        "menus": normalized_menus,
        # Legacy aliases
        "table": first_table,
        "fields": first_table.get("fields", []),
        "indices": first_table.get("indices", []),
        "references": first_table.get("references", []),
        "session": first_session
    }

    return result


def parse_schema_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Loads and validates a YAML or JSON schema file."""
    raw = load_raw_schema(file_path)
    return validate_and_normalize_schema(raw)


def main():
    parser = argparse.ArgumentParser(description="Validate Infor LN Multi-Object Schema File")
    parser.add_argument("schema_file", help="Path to YAML or JSON schema specification")
    parser.add_argument("--json", action="store_true", help="Print normalized schema JSON output")

    args = parser.parse_args()

    try:
        validated = parse_schema_file(args.schema_file)
        if args.json:
            print(json.dumps(validated, indent=2))
        else:
            print(f"[OK] Schema is valid:")
            print(f"  Tables:    {len(validated['tables'])}")
            for t in validated['tables']:
                print(f"    - {t['code']} ({len(t['fields'])} fields, {len(t['indices'])} indices)")
            print(f"  Domains:   {len(validated['domains'])}")
            print(f"  Sessions:  {len(validated['sessions'])}")
            print(f"  Libraries: {len(validated['libraries'])}")
            print(f"  Menus:     {len(validated['menus'])}")
    except SchemaValidationError as e:
        print("[ERROR] Schema validation failed with errors:", file=sys.stderr)
        for err in e.errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Failed to process schema: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
