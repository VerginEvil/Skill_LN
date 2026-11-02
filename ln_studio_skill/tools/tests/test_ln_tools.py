#!/usr/bin/env python3
"""
ln_studio_skill/tools/tests/test_ln_tools.py
End-to-End Test Suite for Infor LN Studio Automation Toolset.
"""

import os
import sys
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

# Add skill tools directory to path (skill-root resolution)
_test_dir = Path(__file__).resolve().parent
_skill_root = _test_dir.parent.parent
_tools_dir = _test_dir.parent
for p in (str(_tools_dir),):
    if p not in sys.path:
        sys.path.insert(0, p)

from ln_workspace_manager import (
    list_workspaces, list_activities, resolve_activity, parse_activity_dir_name, get_workspace_root
)
from ln_schema_parser import (
    parse_schema_file, validate_and_normalize_schema, SchemaValidationError, resolve_native_datatype
)
from generate_ln_table import (
    generate_all_components, generate_table_xml, generate_label_xml, generate_domain_xml
)
from generate_ln_session import (
    generate_session, generate_session_xml
)
from inject_ln_script import (
    extract_script_from_xml, inject_script_into_xml, extract_file, inject_file
)
from admin_sync import (
    list_admin_components, add_component, remove_component, scan_and_sync_activity,
    init_admin_file, admin_after_get, admin_after_create, admin_after_checkout,
    admin_after_put, admin_after_checkin, admin_after_uncheckout, repair_admin_file,
    normalize_admin_path, get_tde_component_rel_path, find_component_file
)
from ln_error_reader import (
    parse_eclipse_markers_file, read_activity_diagnostics
)


class TestLNWorkspaceManager(unittest.TestCase):
    """Tests for ln_studio_skill/tools/ln_workspace_manager.py."""

    def test_parse_activity_dir_name(self):
        parsed = parse_activity_dir_name("dev_natt_01103 [EXTce01103]")
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed, ("dev_natt_01103", "EXTce01103"))

        parsed_hyphen = parse_activity_dir_name("dev_natt_01105-2 [EXTce01105]")
        self.assertIsNotNone(parsed_hyphen)
        self.assertEqual(parsed_hyphen, ("dev_natt_01105-2", "EXTce01105"))

        self.assertIsNone(parse_activity_dir_name("regular_directory"))

    def test_list_workspaces(self):
        wss = list_workspaces()
        self.assertIsInstance(wss, list)
        self.assertTrue(len(wss) > 0)
        self.assertIn("Team_TST", wss)

    def test_resolve_activity(self):
        act = resolve_activity("dev_natt_01105")
        self.assertIsNotNone(act)
        self.assertEqual(act["project"], "EXTce01105")
        self.assertTrue(Path(act["path"]).exists())


class TestLNSchemaParser(unittest.TestCase):
    """Tests for ln_studio_skill/tools/ln_schema_parser.py."""

    def setUp(self):
        self.sample_yaml = _skill_root / "templates" / "table_schema_sample.yaml"

    def test_valid_schema_parsing(self):
        res = parse_schema_file(self.sample_yaml)
        self.assertEqual(res["table"]["code"], "txptc200")
        self.assertEqual(res["table"]["package"], "tx")
        self.assertEqual(res["table"]["module"], "ptc")
        self.assertEqual(len(res["fields"]), 6)
        self.assertEqual(len(res["indices"]), 2)
        self.assertTrue(res["indices"][0]["primary_key"])
        self.assertEqual(res["session"]["code"], "txptc1200m000")

    def test_datatype_mappings(self):
        dt_code, _ = resolve_native_datatype("tcpono")
        self.assertEqual(dt_code, 3)

        dt_code, _ = resolve_native_datatype("tcmcs.cmnf")
        self.assertEqual(dt_code, 6)

        dt_code, _ = resolve_native_datatype("txstatus", explicit_type="enum")
        self.assertEqual(dt_code, 7)

    def test_invalid_table_naming(self):
        bad_schema = {
            "table": {"code": "invalid_table_code"},
            "fields": [{"name": "col1", "domain": "tcpono"}]
        }
        with self.assertRaises(SchemaValidationError):
            validate_and_normalize_schema(bad_schema)

    def test_invalid_field_naming(self):
        bad_schema = {
            "table": {"code": "txptc100"},
            "fields": [{"name": "very_long_field_name_over_8_chars", "domain": "tcpono"}]
        }
        with self.assertRaises(SchemaValidationError):
            validate_and_normalize_schema(bad_schema)


class TestLNComponentGenerator(unittest.TestCase):
    """Tests for table and session generators."""

    def setUp(self):
        self.sample_yaml = _skill_root / "templates" / "table_schema_sample.yaml"

    def test_table_xml_generation(self):
        files = generate_all_components(self.sample_yaml, dry_run=True)
        self.assertTrue(len(files) >= 12)

        tbl_file = next(f for f in files if f["type"] == "table")
        root = ET.fromstring(tbl_file["content"])
        self.assertEqual(root.tag, "DR_Table")
        self.assertEqual(root.findtext("name"), "txptc200")
        self.assertEqual(root.findtext("type"), "table")
        self.assertIsNotNone(root.find("Column"))
        self.assertIsNotNone(root.find("Index"))
        self.assertIsNotNone(root.find("TableRelationship"))
        self.assertIsNotNone(root.find("DR_Module"))

    def test_session_xml_generation(self):
        files = generate_session(self.sample_yaml, dry_run=True)
        ses_file = next(f for f in files if f["type"] == "session")
        root = ET.fromstring(ses_file["content"])
        self.assertEqual(root.tag, "DR_Controller")
        self.assertEqual(root.findtext("name"), "txptc1200m000")
        self.assertIsNotNone(root.find("ControllerTableRelationship"))
        self.assertIsNotNone(root.find("Form"))
        self.assertIsNotNone(root.find("DR_Module"))


class TestLNScriptSync(unittest.TestCase):
    """Tests for ln_studio_skill/tools/inject_ln_script.py round-trip fidelity."""

    def test_round_trip_xml_expression(self):
        original_4gl = (
            "#include <bic_dal2>\n\n"
            "table ttxptc100\n\n"
            "function extern long before.save.object(long i.mode)\n"
            "{\n"
            "\tif (a < b && b > c) then\n"
            "\t\tdal.set.error.message(\"@test.err\")\n"
            "\t\treturn(DALHOOKERROR)\n"
            "\tendif\n"
            "\treturn(0)\n"
            "}\n"
        )
        xml_template = "<DR_Table><Source><expression>PLACEHOLDER</expression></Source></DR_Table>"
        injected_xml = inject_script_into_xml(xml_template, original_4gl)

        self.assertNotIn("< b", injected_xml)
        self.assertIn("&lt; b", injected_xml)
        self.assertIn("&amp;&amp;", injected_xml)

        extracted_4gl = extract_script_from_xml(injected_xml)
        self.assertEqual(original_4gl, extracted_4gl)


class TestLNAdminSync(unittest.TestCase):
    """Tests for ln_studio_skill/tools/admin_sync.py."""

    def test_admin_file_manipulation(self):
        act = resolve_activity("dev_natt_01105")
        if not act:
            self.skipTest("dev_natt_01105 not found")

        src_admin = Path(act["path"]) / ".admin"
        if not src_admin.exists():
            self.skipTest(".admin not present")

        with tempfile.TemporaryDirectory() as td:
            tpath = Path(td)
            shutil.copyfile(src_admin, tpath / ".admin")

            initial = list_admin_components(tpath)
            self.assertTrue(len(initial) > 0)

            add_component(tpath, "tx/table/ptc/txptc999.tbl")
            after_add = list_admin_components(tpath)
            self.assertEqual(len(after_add), len(initial) + 1)

            remove_component(tpath, "tx/table/ptc/txptc999.tbl")
            after_rem = list_admin_components(tpath)
            self.assertEqual(len(after_rem), len(initial))

    def test_normalize_admin_path(self):
        """Asserts paths are normalized to exact project-relative without leading slash or :<act>/ prefix."""
        self.assertEqual(normalize_admin_path("tx/table/cmg/txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl")
        self.assertEqual(normalize_admin_path(":dev_act/tx/table/cmg/txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl")
        self.assertEqual(normalize_admin_path("/tx/domain/txcmg.remk.dmn"), "tx/domain/txcmg.remk.dmn")
        self.assertEqual(normalize_admin_path("tx\\table\\cmg\\txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl")

    def test_tde_path_resolution_module_vs_package_scoped(self):
        """Asserts Native Single-XML TDE layout distinguishes module-scoped vs package-scoped types."""
        # Module-scoped: {pkg}/{type}/{mod}/{name}.{ext}
        self.assertEqual(
            get_tde_component_rel_path("tx", "table", "cmg", "txcmg011"),
            "tx/table/cmg/txcmg011.tbl",
        )
        self.assertEqual(
            get_tde_component_rel_path("tx", "session", "cmg", "txcmg0110m000"),
            "tx/session/cmg/txcmg0110m000.ses",
        )
        self.assertEqual(
            get_tde_component_rel_path("tx", "library", "ibd", "txibddll001"),
            "tx/library/ibd/txibddll001.lib",
        )
        # Package-scoped: {pkg}/{type}/{name}.{ext} (no module folder)
        self.assertEqual(
            get_tde_component_rel_path("tx", "domain", "", "txcmg.remk"),
            "tx/domain/txcmg.remk.dmn",
        )
        self.assertEqual(
            get_tde_component_rel_path("tx", "label", "", "txtxcmg011.header"),
            "tx/label/txtxcmg011.header.lbl",
        )
        self.assertEqual(
            get_tde_component_rel_path("tx", "message", "", "txcmg0001"),
            "tx/message/txcmg0001.msg",
        )

    def test_find_component_file_tde_and_legacy_fallback(self):
        """Asserts find_component_file discovers TDE path first, then legacy plural subfolders."""
        with tempfile.TemporaryDirectory() as td:
            tpath = Path(td)
            tde_file = tpath / "tx" / "table" / "cmg" / "txcmg011.tbl"
            tde_file.parent.mkdir(parents=True, exist_ok=True)
            tde_file.write_text("<DR_Table/>", encoding="utf-8")

            found_tde = find_component_file(tpath, "tx", "table", "cmg", "txcmg011")
            self.assertEqual(found_tde, tde_file)

            # Legacy plural fallback
            legacy_file = tpath / "tables" / "txcmg012.tbl"
            legacy_file.parent.mkdir(parents=True, exist_ok=True)
            legacy_file.write_text("<DR_Table/>", encoding="utf-8")

            found_legacy = find_component_file(tpath, "tx", "table", "cmg", "txcmg012")
            self.assertEqual(found_legacy, legacy_file)

    def test_cmstudio_state_machine_transitions(self):
        """Asserts CMStudio authentic state transitions (after_get, after_create, after_checkout, after_put, after_checkin, after_uncheckout)."""
        with tempfile.TemporaryDirectory() as td:
            tpath = Path(td)
            init_admin_file(tpath / ".admin")

            comp_rel = "tx/table/cmg/txcmg011.tbl"

            # 1. after_create: isCreated=true, isCheckedout=true, m_isDirty=true, m_isVSCHappy=false
            self.assertTrue(admin_after_create(tpath, comp_rel))
            comps = {c["path"]: c for c in list_admin_components(tpath)}
            self.assertIn(comp_rel, comps)
            c = comps[comp_rel]
            self.assertTrue(c["isCreated"])
            self.assertTrue(c["isCheckedOut"])
            self.assertTrue(c["isDirty"])
            self.assertFalse(c["isVSCHappy"])
            self.assertEqual(c["m_path"], comp_rel)

            # 2. after_put: m_isDirty=false, isCheckedout=true
            self.assertTrue(admin_after_put(tpath, comp_rel))
            comps = {c["path"]: c for c in list_admin_components(tpath)}
            self.assertFalse(comps[comp_rel]["isDirty"])
            self.assertTrue(comps[comp_rel]["isCheckedOut"])

            # 3. after_checkin: isCreated=false, isCheckedout=false, isEvercheckedIn=true, m_isDirty=false
            self.assertTrue(admin_after_checkin(tpath, comp_rel))
            comps = {c["path"]: c for c in list_admin_components(tpath)}
            self.assertFalse(comps[comp_rel]["isCreated"])
            self.assertFalse(comps[comp_rel]["isCheckedOut"])
            self.assertTrue(comps[comp_rel]["isEverCheckedIn"])
            self.assertFalse(comps[comp_rel]["isDirty"])

            # 4. after_checkout: isCreated=false, isCheckedout=true, m_isDirty=false
            self.assertTrue(admin_after_checkout(tpath, comp_rel))
            comps = {c["path"]: c for c in list_admin_components(tpath)}
            self.assertFalse(comps[comp_rel]["isCreated"])
            self.assertTrue(comps[comp_rel]["isCheckedOut"])
            self.assertFalse(comps[comp_rel]["isDirty"])

            # 5. after_get: isCreated=false, isCheckedout=false, m_isDirty=false
            comp2 = "tx/domain/txcmg.remk.dmn"
            self.assertTrue(admin_after_get(tpath, comp2))
            comps = {c["path"]: c for c in list_admin_components(tpath)}
            self.assertIn(comp2, comps)
            self.assertFalse(comps[comp2]["isCreated"])
            self.assertFalse(comps[comp2]["isCheckedOut"])
            self.assertFalse(comps[comp2]["isDirty"])

            # 6. after_uncheckout on uncommitted created item: removes entry
            uncommitted = "tx/table/cmg/txcmg099.tbl"
            self.assertTrue(admin_after_create(tpath, uncommitted))
            self.assertIn(uncommitted, {c["path"]: c for c in list_admin_components(tpath)})
            self.assertTrue(admin_after_uncheckout(tpath, uncommitted))
            self.assertNotIn(uncommitted, {c["path"]: c for c in list_admin_components(tpath)})

    def test_repair_admin_file_cleans_legacy_prefix_and_standalone_scripts(self):
        """Asserts repair_admin_file strips :<activity>/ prefix and removes standalone scripts (.src, .4gl, .dal)."""
        with tempfile.TemporaryDirectory() as td:
            tpath = Path(td)
            init_admin_file(tpath / ".admin")

            # Add entries
            add_component(tpath, ":legacy_act/tx/table/cmg/txcmg011.tbl")
            add_component(tpath, "tx/table/cmg/txcmg011.4gl")
            add_component(tpath, "tx/domain/txcmg.remk.dmn")

            # Run repair
            self.assertTrue(repair_admin_file(tpath))

            comps = {c["path"]: c for c in list_admin_components(tpath)}
            self.assertIn("tx/table/cmg/txcmg011.tbl", comps)
            self.assertIn("tx/domain/txcmg.remk.dmn", comps)
            self.assertNotIn("tx/table/cmg/txcmg011.4gl", comps)
            self.assertEqual(comps["tx/table/cmg/txcmg011.tbl"]["m_path"], "tx/table/cmg/txcmg011.tbl")


class TestLNErrorReader(unittest.TestCase):
    """Tests for ln_studio_skill/tools/ln_error_reader.py."""

    def test_parse_real_markers_file(self):
        markers_path = (
            get_workspace_root() / "Team_TST" / ".metadata" / ".plugins" /
            "org.eclipse.core.resources" / ".projects" / "dev_natt_01103 [EXTce01103]" / ".markers"
        )
        if not markers_path.exists():
            self.skipTest(".markers file not present")

        markers = parse_eclipse_markers_file(markers_path)
        self.assertTrue(len(markers) > 0)
        sample = markers[0]
        self.assertIn("file", sample)
        self.assertIn("line", sample)
        self.assertIn("severity", sample)
        self.assertIn("message", sample)


if __name__ == "__main__":
    unittest.main()
