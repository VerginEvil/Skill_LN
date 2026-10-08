#!/usr/bin/env python3
"""
tools/tests/test_ln_tools.py
End-to-End Test Suite for Infor LN Studio Automation Toolset.
"""

import os
import sys
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

# Add project root and tools directory to path
_test_dir = Path(__file__).resolve().parent
_repo_root = _test_dir.parent.parent
_tools_dir = _test_dir.parent
for p in (str(_repo_root), str(_tools_dir)):
    if p not in sys.path:
        sys.path.insert(0, p)

from tools.ln_workspace_manager import (
    list_workspaces, list_activities, resolve_activity, parse_activity_dir_name, get_workspace_root
)
from tools.ln_schema_parser import (
    parse_schema_file, validate_and_normalize_schema, SchemaValidationError, resolve_native_datatype
)
from tools.generate_ln_table import (
    generate_all_components, generate_table_xml, generate_label_xml, generate_domain_xml
)
from tools.generate_ln_session import (
    generate_session, generate_session_xml
)
from tools.inject_ln_script import (
    extract_script_from_xml, inject_script_into_xml, extract_file, inject_file
)
from tools.admin_sync import (
    list_admin_components, add_component, remove_component, scan_and_sync_activity
)
from tools.ln_error_reader import (
    parse_eclipse_markers_file, read_activity_diagnostics
)


class TestLNWorkspaceManager(unittest.TestCase):
    """Tests for tools/ln_workspace_manager.py."""

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
    """Tests for tools/ln_schema_parser.py."""

    def setUp(self):
        self.sample_yaml = _repo_root / "ln_studio_skill" / "templates" / "table_schema_sample.yaml"

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
        self.sample_yaml = _repo_root / "ln_studio_skill" / "templates" / "table_schema_sample.yaml"

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
    """Tests for tools/inject_ln_script.py round-trip fidelity."""

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
    """Tests for tools/admin_sync.py."""

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


class TestLNErrorReader(unittest.TestCase):
    """Tests for tools/ln_error_reader.py."""

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
