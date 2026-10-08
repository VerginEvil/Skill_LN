#!/usr/bin/env python3
"""
tools/ln_schema_parser.py
Declarative Schema Specification & Validation Engine for Infor LN Studio.

Validates table, column, index, reference, domain, and session specifications
from YAML/JSON files according to Infor LN 10.8 Data Dictionary conventions.
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

# Standard Infor LN Native Datatype Mappings
# 1 = Byte, 2 = Double/Float, 3 = Long/Integer, 6 = String/Text, 7 = Enum, 14 = UtcDateTime
DATA_TYPE_MAP = {
    "long": 3,
    "integer": 3,
    "int": 3,
    "string": 6,
    "str": 6,
    "text": 6,
    "enum": 7,
    "enumeration": 7,
    "boolean": 7,
    "bool": 7,
    "double": 2,
    "float": 2,
    "utc": 14,
    "datetime": 14,
    "date": 14,
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
    "tcdate": {"nativeDatatype": 14, "minLength": "1", "maxLength": "10"},
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
            # Try YAML first, then JSON
            content = f.read()
            if yaml is not None:
                try:
                    return yaml.safe_load(content) or {}
                except Exception:
                    pass
            return json.loads(content)


def resolve_native_datatype(domain_name: str, explicit_type: Optional[str] = None) -> Tuple[int, Dict[str, str]]:
    """Resolves nativeDatatype code (e.g. 3, 6, 7) and facets for a domain."""
    d_lower = domain_name.lower()

    if explicit_type:
        t_lower = explicit_type.lower()
        if t_lower in DATA_TYPE_MAP:
            code = DATA_TYPE_MAP[t_lower]
            return code, {"maxLength": "30", "minLength": "1"}

    if d_lower in STANDARD_DOMAINS:
        info = STANDARD_DOMAINS[d_lower]
        return info["nativeDatatype"], {"minLength": info.get("minLength", "1"), "maxLength": info.get("maxLength", "30")}

    # Infer by domain prefix/common patterns
    if d_lower.startswith(("tcpono", "seq", "nr", "cnt")):
        return 3, {"minLength": "1", "maxLength": "6"}
    if d_lower.startswith(("tcyesno", "txskip", "txoutm", "enum")):
        return 7, {"minLength": "1", "maxLength": "50"}
    if d_lower.startswith(("date", "utc")):
        return 14, {"minLength": "1", "maxLength": "10"}

    # Default to String
    return 6, {"minLength": "1", "maxLength": "30"}


def validate_and_normalize_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates LN table schema specification and enriches it with calculated
    attributes, label codes, and datatype facets.
    """
    errors: List[str] = []

    # 1. Validate Table Header
    table = schema.get("table")
    if not table:
        errors.append("Schema missing 'table' definition.")
        raise SchemaValidationError(errors)

    if isinstance(table, dict):
        table_code = table.get("code") or table.get("name")
        module = table.get("module")
        package = table.get("package")
        description = table.get("description", "")
        version_id = table.get("version_id", "B61O_a_ext")
        application = table.get("application", "")
    else:
        table_code = str(table)
        module = schema.get("module")
        package = schema.get("package")
        description = schema.get("description", "")
        version_id = schema.get("version_id", "B61O_a_ext")
        application = schema.get("application", "")

    if not table_code:
        errors.append("Table definition must include 'code' or 'name'.")
    else:
        table_code = table_code.lower()
        m = TABLE_CODE_PATTERN.match(table_code)
        if not m:
            errors.append(
                f"Invalid table code '{table_code}'. Must be 2-char package + 3-char module + 3-digit number (e.g. 'txptc100')."
            )
        else:
            inferred_pkg, inferred_mod, _ = m.groups()
            if not package:
                package = inferred_pkg
            elif package.lower() != inferred_pkg:
                errors.append(f"Package '{package}' does not match prefix of table code '{table_code}'.")

            if not module:
                module = inferred_mod
            elif module.lower() != inferred_mod:
                errors.append(f"Module '{module}' does not match table code '{table_code}'.")

    # 2. Validate Fields
    raw_fields = schema.get("fields", [])
    if not raw_fields:
        errors.append("Schema must define at least one field under 'fields'.")

    normalized_fields = []
    field_names = set()

    for idx, f in enumerate(raw_fields, start=1):
        if not isinstance(f, dict):
            errors.append(f"Field item {idx} must be a dictionary.")
            continue

        fname = (f.get("name") or "").lower()
        if not fname:
            errors.append(f"Field {idx} is missing 'name'.")
            continue

        if not FIELD_NAME_PATTERN.match(fname):
            errors.append(
                f"Invalid field name '{fname}'. Must be 1-8 lowercase alphanumeric characters."
            )

        if fname in field_names:
            errors.append(f"Duplicate field name '{fname}'.")
        field_names.add(fname)

        f_desc = f.get("description") or fname.capitalize()
        f_domain = f.get("domain") or f.get("datatype") or "tcmcs.str30"
        f_mandatory = bool(f.get("mandatory", False))
        f_nullable = bool(f.get("nullable", not f_mandatory))
        f_active = bool(f.get("active", True))
        f_default = str(f.get("default", f.get("default_value", "")))
        f_type_hint = f.get("type")

        native_dt, facets = resolve_native_datatype(f_domain, f_type_hint)

        # Allow schema to override facets (e.g. maxLength)
        if "length" in f:
            facets["maxLength"] = str(f["length"])
        elif "max_length" in f:
            facets["maxLength"] = str(f["max_length"])

        field_label = f.get("label_code") or f"txt{table_code}.{fname}"

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

    # 3. Validate Indices
    raw_indices = schema.get("indices", [])
    normalized_indices = []

    if not raw_indices and normalized_fields:
        # Auto-create Index 1 on first field if none specified
        first_field = normalized_fields[0]["name"]
        raw_indices = [{
            "id": 1,
            "description": "Primary Key",
            "columns": [first_field],
            "unique": True,
            "primary_key": True
        }]

    has_pk = False
    for i_idx, ind in enumerate(raw_indices, start=1):
        if not isinstance(ind, dict):
            errors.append(f"Index item {i_idx} must be a dictionary.")
            continue

        idx_id = str(ind.get("id", i_idx))
        idx_desc = ind.get("description", f"Index {idx_id}")
        is_pk = bool(ind.get("primary_key", idx_id == "1"))
        if is_pk:
            has_pk = True
        is_unique = bool(ind.get("unique", is_pk))

        cols = ind.get("columns", [])
        if not cols:
            errors.append(f"Index {idx_id} has no columns.")

        index_cols = []
        for c_pos, col in enumerate(cols, start=1):
            if isinstance(col, dict):
                col_name = col.get("name", "").lower()
                sort_order = col.get("sort", "asc").lower()
            else:
                col_name = str(col).lower()
                sort_order = "asc"

            if col_name not in field_names:
                errors.append(f"Index {idx_id} references non-existent field '{col_name}'.")

            index_cols.append({
                "column": col_name,
                "position": c_pos,
                "sorting_order": sort_order
            })

        idx_label = ind.get("label_code") or f"{table_code}{int(idx_id):02d}"

        normalized_indices.append({
            "id": idx_id,
            "description": idx_desc,
            "primary_key": is_pk,
            "unique": is_unique,
            "active": bool(ind.get("active", True)),
            "columns": index_cols,
            "label_code": idx_label
        })

    if not has_pk and normalized_indices:
        # Default index 1 to primary key
        normalized_indices[0]["primary_key"] = True

    # 4. Validate Table Relationships (Foreign Keys)
    raw_refs = schema.get("references", schema.get("relationships", []))
    normalized_refs = []

    for r_idx, ref in enumerate(raw_refs, start=1):
        if not isinstance(ref, dict):
            errors.append(f"Reference item {r_idx} must be a dictionary.")
            continue

        to_table = (ref.get("to_table") or ref.get("table", "")).lower()
        if not to_table:
            errors.append(f"Reference {r_idx} missing 'to_table'.")
            continue

        col_maps = ref.get("columns", ref.get("mapping", []))
        normalized_maps = []
        if isinstance(col_maps, dict):
            for f_from, f_to in col_maps.items():
                if f_from.lower() not in field_names:
                    errors.append(f"Reference to '{to_table}' maps unknown field '{f_from}'.")
                normalized_maps.append({"from": f_from.lower(), "to": f_to.lower()})
        elif isinstance(col_maps, list):
            for cm in col_maps:
                if isinstance(cm, dict):
                    f_from = cm.get("from", "").lower()
                    f_to = cm.get("to", "").lower()
                    if f_from not in field_names:
                        errors.append(f"Reference to '{to_table}' maps unknown field '{f_from}'.")
                    normalized_maps.append({"from": f_from, "to": f_to})
                elif isinstance(cm, str):
                    # Same field name in both tables
                    if cm.lower() not in field_names:
                        errors.append(f"Reference to '{to_table}' maps unknown field '{cm}'.")
                    normalized_maps.append({"from": cm.lower(), "to": cm.lower()})

        del_rule = ref.get("delete_rule", "cascade").lower()
        upd_rule = ref.get("update_rule", "cascade").lower()

        normalized_refs.append({
            "name": ref.get("name", to_table),
            "to_table": to_table,
            "delete_rule": del_rule,
            "update_rule": upd_rule,
            "multiplicity": ref.get("multiplicity", "oneToOne"),
            "columns": normalized_maps
        })

    # 5. Validate Custom Domains (if any)
    raw_domains = schema.get("domains", [])
    normalized_domains = []
    for d in raw_domains:
        if isinstance(d, dict):
            d_name = d.get("name", "").lower()
            d_desc = d.get("description", d_name)
            d_type = d.get("type", "enum")
            enums = d.get("enums", d.get("constants", []))
            normalized_enums = []
            for e_pos, enum_val in enumerate(enums, start=1):
                if isinstance(enum_val, dict):
                    e_name = enum_val.get("name")
                    e_desc = enum_val.get("description", e_name)
                    e_pos_val = enum_val.get("position", e_pos * 10)
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
                "native_datatype": 7 if d_type in ("enum", "enumeration") else 6,
                "enums": normalized_enums
            })

    # 6. Validate Session (if specified)
    session_spec = schema.get("session")
    normalized_session = None
    if session_spec:
        if isinstance(session_spec, str):
            ses_code = session_spec.lower()
            ses_desc = description
        elif isinstance(session_spec, dict):
            ses_code = (session_spec.get("code") or f"{table_code[:2]}{table_code[2:5]}1100m000").lower()
            ses_desc = session_spec.get("description", description)
        else:
            ses_code = f"{table_code[:2]}{table_code[2:5]}1100m000".lower()
            ses_desc = description

        if not SESSION_CODE_PATTERN.match(ses_code):
            errors.append(
                f"Invalid session code '{ses_code}'. Convention: 2-pkg + 3-mod + 4-num + m/s/r/d + 3-ver (e.g. 'txptc1100m000')."
            )

        normalized_session = {
            "code": ses_code,
            "description": ses_desc,
            "window_type": 2,  # List Window
            "sub_type": 1,     # Maintain
            "table": table_code,
            "label_code": ses_code
        }

    if errors:
        raise SchemaValidationError(errors)

    return {
        "table": {
            "code": table_code,
            "package": package,
            "module": module,
            "description": description or table_code,
            "version_id": version_id,
            "application": application,
            "label_code": table_code
        },
        "fields": normalized_fields,
        "indices": normalized_indices,
        "references": normalized_refs,
        "domains": normalized_domains,
        "session": normalized_session
    }


def parse_schema_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Loads and validates a YAML or JSON schema file."""
    raw = load_raw_schema(file_path)
    return validate_and_normalize_schema(raw)


def main():
    parser = argparse.ArgumentParser(description="Validate Infor LN Table/Session Schema File")
    parser.add_argument("schema_file", help="Path to YAML or JSON schema specification")
    parser.add_argument("--json", action="store_true", help="Print normalized schema JSON output")

    args = parser.parse_args()

    try:
        validated = parse_schema_file(args.schema_file)
        if args.json:
            print(json.dumps(validated, indent=2))
        else:
            tbl = validated["table"]
            print(f"[OK] Schema is valid:")
            print(f"  Table:       {tbl['code']} ({tbl['package']}/{tbl['module']}) - '{tbl['description']}'")
            print(f"  Fields:      {len(validated['fields'])} columns")
            print(f"  Indices:     {len(validated['indices'])} index(es)")
            print(f"  References:  {len(validated['references'])} relation(s)")
            if validated["session"]:
                print(f"  Session:     {validated['session']['code']} - '{validated['session']['description']}'")
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
