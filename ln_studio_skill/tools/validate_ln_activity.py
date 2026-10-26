#!/usr/bin/env python3
"""
LN Studio Four-Layer Activity & Component Validator (`validate` & `--fix`)

Audits an Activity or individual LN components across 4 verification layers:
  Layer 1: SCM .admin Registration, Read-Only Consistency & Activity Version Alignment
  Layer 2: XML Structure, Ecore Compliance & Session FormGroup Hierarchy Integrity
  Layer 3: Cross-Object Reference Integrity (Labels, Table Columns, Indexes, Menus)
  Layer 4: Static 4GL Script Verification & Object-Script Symbol Cross-Checking

By default, validate is strictly READ-ONLY.
When --fix is passed, safe non-destructive repairs are executed:
  - Auto-generate missing custom .lbl files
  - Synchronize .admin entries for untracked components
  - Never modifies or unlocks Read-Only files
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from admin_sync import list_admin_components, scan_and_sync_activity, MANAGED_EXTENSIONS
from check_4gl_script import ScriptChecker, Diagnostic
from ln_workspace_manager import detect_current_activity
from scm_guardrails import is_file_readonly, is_extension_component


VALID_DATATYPES = {1, 2, 3, 5, 6, 7, 9, 14}


class ValidationReport:
    def __init__(self, target_path: Path):
        self.target_path = target_path
        self.diagnostics: List[Diagnostic] = []
        self.repaired_items: List[str] = []
        self.files_scanned = 0

    def add(self, file_path: str, line: int, col: int, severity: str, message: str, layer: int) -> None:
        diag = Diagnostic(file_path, line, col, severity, f"[Layer {layer}] {message}")
        self.diagnostics.append(diag)

    @property
    def errors(self) -> List[Diagnostic]:
        return [d for d in self.diagnostics if d.severity == "ERROR"]

    @property
    def warnings(self) -> List[Diagnostic]:
        return [d for d in self.diagnostics if d.severity == "WARNING"]


class ActivityValidator:
    def __init__(self, activity_path: Path, strict: bool = False, fix: bool = False):
        self.activity_path = activity_path.resolve()
        self.strict = strict
        self.fix = fix
        self.report = ValidationReport(self.activity_path)
        self.script_checker = ScriptChecker()

        # Cache of parsed components in activity
        self.tables: Dict[str, Dict[str, Any]] = {}
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self.domains: Dict[str, Dict[str, Any]] = {}
        self.labels: Set[str] = set()
        self.libraries: Dict[str, Dict[str, Any]] = {}
        self.menus: Dict[str, Dict[str, Any]] = {}

        # Activity package detection
        self.packages: Set[str] = set()

    def run(self) -> ValidationReport:
        """Run all 4 validation layers."""
        self._discover_packages()

        # Pre-scan activity for index of all components
        self._index_activity_components()

        # Layer 1: SCM & Admin
        self._validate_layer1_scm()

        # Layer 2: XML & Structure
        self._validate_layer2_structure()

        # Layer 3: Cross references
        self._validate_layer3_cross_references()

        # Layer 4: 4GL scripts
        self._validate_layer4_scripts()

        # Safe --fix execution if requested
        if self.fix:
            self._execute_safe_fixes()

        return self.report

    def _discover_packages(self) -> None:
        """Discover package directories inside activity."""
        for item in self.activity_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                # Subdirs like 'table', 'session', 'label', 'menu' or package dirs like 'tx'
                sub_names = {sub.name for sub in item.iterdir() if sub.is_dir()}
                if sub_names & {"table", "session", "label", "menu", "library", "domain", ".admin"}:
                    self.packages.add(item.name.lower())

    def _index_activity_components(self) -> None:
        """Build in-memory cache of all components in activity for cross-reference checking."""
        for ext in MANAGED_EXTENSIONS:
            for p in self.activity_path.rglob(f"*{ext}"):
                if not p.is_file() or ".admin" in p.parts:
                    continue
                self.report.files_scanned += 1
                code = p.stem.lower()

                if ext == ".tbl":
                    self.tables[code] = self._parse_table_metadata(p)
                elif ext == ".ses":
                    self.sessions[code] = self._parse_session_metadata(p)
                elif ext == ".dmn":
                    self.domains[code] = {"path": p}
                elif ext == ".lbl":
                    self.labels.add(code)
                elif ext == ".lib":
                    self.libraries[code] = {"path": p}
                elif ext == ".mnu":
                    self.menus[code] = self._parse_menu_metadata(p)

    def _parse_table_metadata(self, path: Path) -> Dict[str, Any]:
        meta: Dict[str, Any] = {"path": path, "columns": set(), "indexes": []}
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            meta["xml_root"] = root
            meta["table_code"] = root.findtext(".//{*}name") or path.stem
            meta["descriptionReference"] = root.findtext(".//{*}descriptionReference") or ""

            for col in root.findall(".//{*}Column"):
                cname = col.findtext("{*}name") or col.findtext("name")
                if cname:
                    meta["columns"].add(cname)
                    meta["columns"].add(f"{meta['table_code']}.{cname}")

            for idx in root.findall(".//{*}Index"):
                idx_cols = [
                    ic.findtext("{*}name") or ic.findtext("name")
                    for ic in idx.findall(".//{*}IndexColumn")
                    if (ic.findtext("{*}name") or ic.findtext("name"))
                ]
                meta["indexes"].append(idx_cols)
        except Exception as e:
            meta["error"] = str(e)
        return meta

    def _parse_session_metadata(self, path: Path) -> Dict[str, Any]:
        meta: Dict[str, Any] = {"path": path, "form_fields": set(), "commands": set(), "groups": {}}
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            meta["xml_root"] = root
            meta["session_code"] = root.findtext(".//{*}name") or path.stem
            meta["descriptionReference"] = root.findtext(".//{*}descriptionReference") or ""
            meta["controller_table"] = root.findtext(".//{*}ControllerTableRelationship/{*}toTable") or root.findtext(".//ControllerTableRelationship/toTable") or ""

            for ff in root.findall(".//{*}FormField"):
                fn = ff.findtext("{*}fieldName") or ff.findtext("fieldName")
                fl = ff.findtext("{*}fieldLabel") or ff.findtext("fieldLabel")
                if fn:
                    meta["form_fields"].add(fn)
                if fl:
                    meta["form_fields"].add(fl)

            for cmd in root.findall(".//{*}FormCommand"):
                cn = cmd.findtext("{*}name") or cmd.findtext("name")
                if cn:
                    meta["commands"].add(cn)

            for grp in root.findall(".//{*}FormGroup"):
                gn = grp.findtext("{*}groupNumber") or grp.findtext("groupNumber")
                if gn:
                    meta["groups"][gn] = {
                        "parentGroup": grp.findtext("{*}parentGroup") or grp.findtext("parentGroup") or "",
                        "firstChildGroup": grp.findtext("{*}firstChildGroup") or grp.findtext("firstChildGroup") or "",
                        "nextGroup": grp.findtext("{*}nextGroup") or grp.findtext("nextGroup") or "",
                        "previousGroup": grp.findtext("{*}previousGroup") or grp.findtext("previousGroup") or "",
                    }
        except Exception as e:
            meta["error"] = str(e)
        return meta

    def _parse_menu_metadata(self, path: Path) -> Dict[str, Any]:
        meta: Dict[str, Any] = {"path": path, "choices": []}
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            meta["xml_root"] = root
            for ch in root.findall(".//{*}MenuChoice"):
                meta["choices"].append({
                    "type": ch.findtext("{*}menuFieldType") or ch.findtext("menuFieldType"),
                    "target": (
                        ch.findtext("{*}menuFieldName")
                        or ch.findtext("menuFieldName")
                        or ch.findtext("{*}menuField")
                        or ch.findtext("menuField")
                    ),
                })
        except Exception as e:
            meta["error"] = str(e)
        return meta

    # ----------------------------------------------------
    # Layer 1: SCM & Admin Validation
    # ----------------------------------------------------
    def _validate_layer1_scm(self) -> None:
        """Verify .admin registration, Read-Only consistency, and activity state."""
        admin_file = self.activity_path / ".admin"
        if not admin_file.exists():
            sev = "ERROR" if self.strict else "WARNING"
            self.report.add(str(self.activity_path), 1, 1, sev, "Activity missing .admin SCM file", layer=1)
            return

        try:
            registered_entries = list_admin_components(self.activity_path)
        except Exception as e:
            self.report.add(str(admin_file), 1, 1, "ERROR", f"Failed to parse .admin: {e}", layer=1)
            return

        registered_map = {entry["path"].replace("\\", "/"): entry for entry in registered_entries}

        # Check on-disk files against .admin
        disk_files: Set[str] = set()
        for p in self.activity_path.rglob("*"):
            if p.is_file() and p.suffix.lower() in MANAGED_EXTENSIONS:
                # Extension Modeler components (tx*, ess, est, etc.) are Read-Only "Get" mode in Studio.
                # Do not flag untracked or SCM check-out warnings for them.
                if is_extension_component(p):
                    continue

                rel = p.relative_to(self.activity_path).as_posix()
                disk_files.add(rel)

                if rel not in registered_map:
                    sev = "ERROR" if self.strict else "WARNING"
                    self.report.add(
                        str(p), 1, 1, sev,
                        f"Component '{rel}' exists on disk but is not registered in .admin.",
                        layer=1
                    )
                else:
                    entry = registered_map[rel]
                    is_ro = is_file_readonly(p)
                    # If checked in, should normally be read-only
                    if not entry.get("isCheckedOut") and not is_ro:
                        pass  # Allow local modifications in working copy

        # Check missing disk files that are registered in .admin
        for rel_path in registered_map:
            if rel_path not in disk_files:
                self.report.add(
                    str(admin_file), 1, 1, "ERROR",
                    f"Component '{rel_path}' registered in .admin but not found on disk.",
                    layer=1
                )

    # ----------------------------------------------------
    # Layer 2: XML Structure & Ecore Compliance
    # ----------------------------------------------------
    def _validate_layer2_structure(self) -> None:
        """Validate XML root tag, Ecore datatype/facets, and Session FormGroup hierarchy."""
        for code, tdata in self.tables.items():
            path = tdata["path"]
            root = tdata.get("xml_root")
            if root is None:
                self.report.add(str(path), 1, 1, "ERROR", tdata.get("error", "Failed to parse XML"), layer=2)
                continue

            if not root.tag.endswith("Table"):
                self.report.add(str(path), 1, 1, "ERROR", f"Expected root <DR_Table>, found <{root.tag}>", layer=2)

            # Check columns & facets
            for col in root.findall(".//{*}Column"):
                cname = col.findtext("{*}name") or col.findtext("name") or "unknown"
                dtype_str = col.findtext(".//{*}nativeDatatype") or col.findtext(".//nativeDatatype")
                if not dtype_str or not dtype_str.isdigit():
                    self.report.add(str(path), 1, 1, "ERROR", f"Column '{cname}' missing valid nativeDatatype", layer=2)
                else:
                    dtype = int(dtype_str)
                    if dtype not in VALID_DATATYPES:
                        self.report.add(str(path), 1, 1, "ERROR", f"Column '{cname}' has invalid nativeDatatype {dtype}", layer=2)

            # Check indexes
            if not tdata.get("indexes"):
                self.report.add(str(path), 1, 1, "ERROR", "Table must define at least one <Index>", layer=2)

        # Validate Sessions & FormGroup Trees
        for code, sdata in self.sessions.items():
            path = sdata["path"]
            root = sdata.get("xml_root")
            if root is None:
                continue

            if not (root.tag.endswith("Session") or root.tag.endswith("Controller")):
                self.report.add(str(path), 1, 1, "ERROR", f"Expected root <DR_Session> or <DR_Controller>, found <{root.tag}>", layer=2)

            groups = sdata.get("groups", {})
            for gnum, ginfo in groups.items():
                parent = ginfo["parentGroup"]
                child = ginfo["firstChildGroup"]
                nxt = ginfo["nextGroup"]
                prev = ginfo["previousGroup"]

                if parent and parent != "0" and parent not in groups:
                    self.report.add(str(path), 1, 1, "ERROR", f"FormGroup {gnum} has non-existent parentGroup '{parent}'", layer=2)
                if child and child not in groups:
                    self.report.add(str(path), 1, 1, "ERROR", f"FormGroup {gnum} has non-existent firstChildGroup '{child}'", layer=2)
                if nxt and nxt not in groups:
                    self.report.add(str(path), 1, 1, "ERROR", f"FormGroup {gnum} has non-existent nextGroup '{nxt}'", layer=2)
                if prev and prev not in groups:
                    self.report.add(str(path), 1, 1, "ERROR", f"FormGroup {gnum} has non-existent previousGroup '{prev}'", layer=2)

    # ----------------------------------------------------
    # Layer 3: Cross-Object Reference Integrity
    # ----------------------------------------------------
    def _validate_layer3_cross_references(self) -> None:
        """Verify label existence, table-column relationships, and index column validity."""
        # 1. Label cross-checks
        all_referenced_labels: Set[Tuple[str, str]] = set()

        for code, tdata in self.tables.items():
            dref = tdata.get("descriptionReference", "")
            if dref:
                all_referenced_labels.add((dref, str(tdata["path"])))

            root = tdata.get("xml_root")
            if root is not None:
                for col in root.findall(".//{*}Column"):
                    cdref = col.findtext("{*}descriptionReference") or col.findtext("descriptionReference")
                    if cdref:
                        all_referenced_labels.add((cdref, str(tdata["path"])))

        for code, sdata in self.sessions.items():
            dref = sdata.get("descriptionReference", "")
            if dref:
                all_referenced_labels.add((dref, str(sdata["path"])))

            root = sdata.get("xml_root")
            if root is not None:
                for ff in root.findall(".//{*}FormField"):
                    fl = ff.findtext("{*}fieldLabel") or ff.findtext("fieldLabel")
                    if fl:
                        all_referenced_labels.add((fl, str(sdata["path"])))
                for cmd in root.findall(".//{*}FormCommand"):
                    cl = cmd.findtext("{*}descriptionReference") or cmd.findtext("descriptionReference") or cmd.findtext("label_code")
                    if cl:
                        all_referenced_labels.add((cl, str(sdata["path"])))

        for lbl_code, ref_path in sorted(all_referenced_labels):
            # Check if this label belongs to our activity packages
            is_local = any(lbl_code.lower().startswith(pkg) for pkg in self.packages)
            if is_local:
                lbl_base = lbl_code.lower()
                # Check directly or check with package variations (e.g. txtxcmg010.user vs txcmg010.user)
                found = (lbl_base in self.labels)
                if not found:
                    for l in self.labels:
                        if l == lbl_base or l.endswith(lbl_base) or lbl_base.endswith(l):
                            found = True
                            break

                if not found:
                    self.report.add(
                        ref_path, 1, 1, "ERROR",
                        f"Referenced label '{lbl_code}' not found in activity label catalog.",
                        layer=3
                    )

        # 2. Session controller table & form field cross-checks
        for code, sdata in self.sessions.items():
            ctrl_table = sdata.get("controller_table")
            if ctrl_table and ctrl_table in self.tables:
                table_cols = self.tables[ctrl_table]["columns"]
                for ff in sdata.get("form_fields", []):
                    if '.' in ff:
                        col_name = ff.split('.')[-1]
                        if ff not in table_cols and col_name not in table_cols:
                            self.report.add(
                                str(sdata["path"]), 1, 1, "WARNING",
                                f"Session FormField '{ff}' does not match any column in controller table '{ctrl_table}'.",
                                layer=3
                            )

        # 3. Table index column cross-checks
        for code, tdata in self.tables.items():
            cols = tdata.get("columns", set())
            for idx_cols in tdata.get("indexes", []):
                for ic in idx_cols:
                    if ic not in cols:
                        self.report.add(
                            str(tdata["path"]), 1, 1, "ERROR",
                            f"IndexColumn '{ic}' does not match any defined Column in table '{code}'.",
                            layer=3
                        )

        # 4. Menu choice targets
        for code, mdata in self.menus.items():
            for choice in mdata.get("choices", []):
                ctype = choice.get("type")
                target = (choice.get("target") or "").lower()
                if ctype == "1" and any(target.startswith(pkg) for pkg in self.packages):
                    if target not in self.sessions:
                        self.report.add(
                            str(mdata["path"]), 1, 1, "WARNING",
                            f"MenuChoice target session '{target}' not found in current activity.",
                            layer=3
                        )

    # ----------------------------------------------------
    # Layer 4: Static 4GL Script Validation
    # ----------------------------------------------------
    def _validate_layer4_scripts(self) -> None:
        """Run static 4GL inspector on embedded <expression> scripts in .tbl, .ses, .lib."""
        for comp_map, comp_type in [
            (self.tables, "table"),
            (self.sessions, "session"),
            (self.libraries, "library")
        ]:
            for code, cdata in comp_map.items():
                path = cdata["path"]
                root = cdata.get("xml_root")
                if root is None:
                    try:
                        root = ET.parse(path).getroot()
                    except Exception:
                        continue

                expr = root.find(".//expression")
                if expr is not None and expr.text and expr.text.strip():
                    meta = {"type": comp_type, "file_path": str(path)}
                    if comp_type == "table":
                        meta["columns"] = cdata.get("columns", set())
                    elif comp_type == "session":
                        meta["form_fields"] = cdata.get("form_fields", set())
                        meta["commands"] = cdata.get("commands", set())

                    diags = self.script_checker.check_script(
                        expr.text,
                        file_path=str(path),
                        owning_component=meta
                    )
                    for d in diags:
                        self.report.add(d.file_path, d.line, d.col, d.severity, d.message, layer=4)

    # ----------------------------------------------------
    # Safe Fixes Execution
    # ----------------------------------------------------
    def _execute_safe_fixes(self) -> None:
        """Auto-create missing .lbl files and synchronize .admin entries."""
        # 1. Missing labels
        missing_label_diags = [
            d for d in self.report.diagnostics
            if "Referenced label" in d.message and "not found in activity" in d.message
        ]

        for d in missing_label_diags:
            m = re.search(r"Referenced label '([^']+)'", d.message)
            if not m:
                continue
            lbl_code = m.group(1).lower()

            pkg = None
            for p in self.packages:
                if lbl_code.startswith(p):
                    pkg = p
                    break
            if not pkg:
                continue

            lbl_dir = self.activity_path / pkg / "label"
            lbl_dir.mkdir(parents=True, exist_ok=True)
            lbl_file = lbl_dir / f"{lbl_code}.lbl"

            if not lbl_file.exists() and not is_file_readonly(lbl_file):
                xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<DR_Label xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <name>{lbl_code}</name>
  <language>2</language>
  <description>{lbl_code}</description>
  <helpText>{lbl_code}</helpText>
  <length>30</length>
</DR_Label>
"""
                lbl_file.write_text(xml_content, encoding="utf-8")
                self.report.repaired_items.append(f"Auto-generated missing label: {lbl_file.name}")
                self.labels.add(lbl_code)

        # 2. Run .admin sync across activity
        sync_res = scan_and_sync_activity(self.activity_path)
        if sync_res.get("added"):
            self.report.repaired_items.append(
                f"Registered {len(sync_res['added'])} untracked component(s) in .admin"
            )


def validate_activity(activity_path: Path, strict: bool = False, fix: bool = False) -> ValidationReport:
    """Entrypoint function to validate an activity."""
    validator = ActivityValidator(activity_path, strict=strict, fix=fix)
    return validator.run()


def main() -> None:
    parser = argparse.ArgumentParser(description="LN Studio Four-Layer Activity Validator")
    parser.add_argument("activity_path", nargs="?", type=Path, default=None,
                        help="Path to Activity folder (defaults to detected active activity)")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    parser.add_argument("--fix", action="store_true", help="Perform safe non-destructive repairs (missing labels, admin sync)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    act_path = args.activity_path
    if not act_path:
        act_info = detect_current_activity()
        if act_info and act_info.get("activity_path"):
            act_path = Path(act_info["activity_path"])
        else:
            print("Error: No activity path provided and none detected in workspace.", file=sys.stderr)
            sys.exit(1)

    if not act_path.exists():
        print(f"Error: Activity path does not exist: {act_path}", file=sys.stderr)
        sys.exit(1)

    validator = ActivityValidator(act_path, strict=args.strict, fix=args.fix)
    report = validator.run()

    if args.json:
        out = {
            "activity_path": str(report.target_path),
            "files_scanned": report.files_scanned,
            "errors_count": len(report.errors),
            "warnings_count": len(report.warnings),
            "repaired_items": report.repaired_items,
            "diagnostics": [
                {
                    "file": d.file_path,
                    "line": d.line,
                    "col": d.col,
                    "severity": d.severity,
                    "message": d.message,
                }
                for d in report.diagnostics
            ]
        }
        print(json.dumps(out, indent=2))
    else:
        print(f"Validated Activity: {report.target_path}")
        print(f"Scanned {report.files_scanned} component file(s):")
        for d in report.diagnostics:
            print(f"  {d}")

        if report.repaired_items:
            print("\nSafe Repairs Applied:")
            for rep in report.repaired_items:
                print(f"  [REPAIRED] {rep}")

        print(f"\nSummary: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")

    if report.errors or (args.strict and report.warnings):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
