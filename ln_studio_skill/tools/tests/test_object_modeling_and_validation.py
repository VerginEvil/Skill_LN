#!/usr/bin/env python3
"""
test_object_modeling_and_validation.py

Comprehensive test suite for:
  - SCM Read-Only Guardrails (Ticket 01)
  - 12-Extension .admin SCM Sync & Explicit Workspace Resolution (Ticket 01)
  - High-Fidelity Table, Domain & Label Modeling (Ticket 02)
  - Multi-Archetype Session, MMT Controller/Satellite, Library & Menu (Ticket 03)
  - Studio Syntax/Completion Extractor & Static 4GL Inspector (Ticket 04)
  - Four-Layer Activity Validator & Safe --fix Repair (Ticket 05)
  - Master Orchestrator CLI subcommands (Ticket 05)
"""

import os
import stat
import sys
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

# Setup paths
_test_dir = Path(__file__).resolve().parent
_tools_dir = _test_dir.parent
_skill_root = _tools_dir.parent

if str(_tools_dir) not in sys.path:
    sys.path.insert(0, str(_tools_dir))

from scm_guardrails import (
    assert_file_writable, is_file_readonly, ReadOnlyComponentError
)
from ln_workspace_manager import (
    get_studio_installation_path, resolve_activity
)
from admin_sync import (
    MANAGED_EXTENSIONS, scan_and_sync_activity, list_admin_components
)
from ln_schema_parser import (
    parse_schema_file, DATA_TYPE_MAP, resolve_native_datatype
)
from generate_ln_domain import (
    generate_domain_xml, generate_domains
)
from generate_ln_table import (
    generate_all_components, generate_table_xml
)
from generate_ln_session import (
    generate_session, generate_session_xml
)
from generate_ln_library import (
    generate_library_xml, generate_libraries
)
from generate_ln_menu import (
    generate_menu_xml, generate_menus
)
from check_4gl_script import (
    ScriptChecker, Diagnostic, check_file
)
from validate_ln_activity import (
    ActivityValidator, validate_activity
)


class TestSCMGuardrails(unittest.TestCase):
    """Ticket 01: Read-Only SCM protection."""

    def test_writable_file_passes(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "writable.tbl"
            p.write_text("<DR_Table/>", encoding="utf-8")
            # Should not raise
            assert_file_writable(p)
            self.assertFalse(is_file_readonly(p))

    def test_nonexistent_file_passes(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "new_file.tbl"
            assert_file_writable(p)

    def test_readonly_file_raises_error(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "readonly.tbl"
            p.write_text("<DR_Table/>", encoding="utf-8")
            # Set read-only
            os.chmod(p, stat.S_IREAD)
            self.assertTrue(is_file_readonly(p))
            with self.assertRaises(ReadOnlyComponentError):
                assert_file_writable(p)
            # Cleanup permissions for rmtree
            os.chmod(p, stat.S_IWRITE)


class TestWorkspaceAndAdminSync(unittest.TestCase):
    """Ticket 01: Pinned Studio Path & 12-Extension .admin Sync."""

    def test_pinned_studio_path_default(self):
        p = get_studio_installation_path()
        self.assertEqual(str(p), r"D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64")

    def test_managed_extensions_contains_all_12_types(self):
        expected = {
            ".tbl", ".ses", ".lib", ".dmn", ".lbl", ".mnu",
            ".rpt", ".rptdsrc", ".msg", ".que", ".add", ".fun"
        }
        self.assertEqual(MANAGED_EXTENSIONS, expected)


class TestTableAndDomainFidelity(unittest.TestCase):
    """Ticket 02: Table, Domain & Label modeling."""

    def test_datatype_map_ecore_codes(self):
        self.assertEqual(DATA_TYPE_MAP["byte"], 1)
        self.assertEqual(DATA_TYPE_MAP["double"], 2)
        self.assertEqual(DATA_TYPE_MAP["long"], 3)
        self.assertEqual(DATA_TYPE_MAP["numeric"], 5)
        self.assertEqual(DATA_TYPE_MAP["amount"], 5)
        self.assertEqual(DATA_TYPE_MAP["string"], 6)
        self.assertEqual(DATA_TYPE_MAP["enum"], 7)
        self.assertEqual(DATA_TYPE_MAP["boolean"], 7)
        self.assertEqual(DATA_TYPE_MAP["date"], 9)
        self.assertEqual(DATA_TYPE_MAP["utc"], 14)

    def test_domain_xml_generation(self):
        content = generate_domain_xml(
            domain_spec={
                "name": "txcmg.remk",
                "package": "tx",
                "description": "Billing Remarks",
                "datatype": 6,
                "native_datatype": 6,
                "facets": {"maxLength": "100"}
            },
            version_id="B61O_a_ext",
            application="EXTce01107"
        )
        root = ET.fromstring(content)
        self.assertEqual(root.tag, "DR_Domain")
        self.assertEqual(root.findtext(".//{*}name") or root.findtext("name"), "txcmg.remk")
        self.assertEqual(root.findtext(".//{*}nativeDatatype") or root.findtext("nativeDatatype"), "6")
        self.assertEqual(root.findtext(".//{*}Facet/{*}type") or root.findtext(".//Facet/type"), "maxLength")
        self.assertEqual(root.findtext(".//{*}Facet/{*}value") or root.findtext(".//Facet/value"), "100")


class TestSessionLibraryAndMenu(unittest.TestCase):
    """Ticket 03: Multi-archetype session, library and menu generation."""

    def test_mmt_controller_session(self):
        field_defs = [
            {"name": "btno", "domain": "tcmcs.long", "type_code": 3, "label": "txtxcmg011.btno", "label_desc": "Batch No"},
            {"name": "cdec", "domain": "tcdsca", "type_code": 6, "label": "txtxcmg011.cdec", "label_desc": "Description"},
        ]
        form_commands = [
            {"name": "exec.user.0", "function": "generate.billing", "label_code": "txcmg0110m100.cmd1", "description": "Generate Billing"}
        ]
        session_spec = {
            "code": "txcmg0110m100",
            "package": "tx",
            "module": "cmg",
            "table": "txcmg011",
            "description": "Billing Batch Header",
            "type": "mmt_controller",
            "satellites": ["txcmg0510m000", "txcmg0512m000"],
            "form_commands": form_commands
        }
        table_spec = {
            "code": "txcmg011",
            "fields": field_defs
        }
        xml_str = generate_session_xml(session_spec, table_spec, "EXTce01107")
        root = ET.fromstring(xml_str)
        self.assertEqual(root.tag, "DR_Controller")
        self.assertEqual(root.findtext(".//{*}type") or root.findtext("type"), "session")
        satellites = [
            sat.findtext("name")
            for sat in root.findall(".//ControllerSatelliteRelationship")
        ]
        self.assertEqual(satellites, ["txcmg0510m000", "txcmg0512m000"])
        cmd_names = [
            cmd.findtext("name")
            for cmd in root.findall(".//FormCommand")
        ]
        self.assertIn("exec.user.0", cmd_names)

    def test_library_generation(self):
        # General DLL
        lib_spec = {
            "code": "txibddllitem01",
            "package": "tx",
            "module": "ibd",
            "type": "dll",
            "description": "Item DLL"
        }
        dll_xml = generate_library_xml(lib_spec, "EXTce01107")
        root = ET.fromstring(dll_xml)
        self.assertTrue(root.tag.endswith("Module"))
        self.assertEqual(root.findtext(".//sourceType"), "6")

        # Table Extension
        est_spec = {
            "code": "txestwhinh312",
            "package": "tx",
            "module": "est",
            "type": "table_extension",
            "target": "whinh312",
            "description": "Table Ext"
        }
        est_xml = generate_library_xml(est_spec, "EXTce01107")
        root_est = ET.fromstring(est_xml)
        self.assertEqual(root_est.findtext(".//sourceType"), "6")
        expr_text = root_est.findtext(".//expression")
        self.assertIn('#context_on "functions"', expr_text)

    def test_menu_generation(self):
        choices = [
            {"position": 10, "type": "session", "target": "txcmg0110m100", "description": "Billing Batch"}
        ]
        menu_spec = {
            "code": "txgld0000m001",
            "package": "tx",
            "module": "gld",
            "description": "Enhancements",
            "choices": choices
        }
        mnu_xml = generate_menu_xml(menu_spec, "EXTce01107")
        root = ET.fromstring(mnu_xml)
        self.assertTrue(root.tag.endswith("Menu"))
        self.assertEqual(root.findtext("name"), "txgld0000m001")
        target = root.findtext(".//MenuChoice/menuFieldName")
        self.assertEqual(target, "txcmg0110m100")


class TestStatic4GLScriptChecker(unittest.TestCase):
    """Ticket 04: Static 4GL Script Inspector."""

    def setUp(self):
        self.checker = ScriptChecker()

    def test_valid_script_clean_pass(self):
        script = """
declaration:
#include <bic_dal2>
table ttxcmg011

function extern boolean method.is.allowed(long i.method)
{
	on case i.method
	case DAL_NEW:
		break
	endcase
	return(true)
}

function extern long before.save.object(long mode)
{
	if mode = DAL_NEW then
		txcmg011.cdec = "test"
	endif
	return(0)
}
"""
        diags = self.checker.check_script(script)
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertEqual(len(errors), 0)

    def test_unrecognized_section_header(self):
        script = """
declaration:
table ttxcmg011

before.progam:
	txcmg011.cdec = "typo"
"""
        diags = self.checker.check_script(script)
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertTrue(any("misspelled section header" in d.message and "before.program:" in d.message for d in errors))

    def test_unclosed_if_block(self):
        script = """
before.program:
	if a = 1 then
		b = 2
"""
        diags = self.checker.check_script(script)
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertTrue(any("Unclosed 'if' block" in d.message for d in errors))

    def test_unclosed_select_block(self):
        script = """
functions:
function void test()
{
	select txcmg011.*
	from   txcmg011
	selectdo
		a = 1
}
"""
        diags = self.checker.check_script(script)
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertTrue(any("Unclosed 'select' block" in d.message for d in errors))

    def test_sql_for_update_does_not_trigger_endfor_error(self):
        script = """
functions:
function void test()
{
	select txcmg011.*
	from   txcmg011 for update
	where  txcmg011.btno = 1
	selectdo
		db.delete(ttxcmg011)
	endselect
}
"""
        diags = self.checker.check_script(script)
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertEqual(len(errors), 0)

    def test_dotted_identifier_does_not_trigger_select_error(self):
        script = """
choice.user.1:
on.choice:
	toggle.select.all()
"""
        diags = self.checker.check_script(script)
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertEqual(len(errors), 0)


class TestFourLayerValidatorAndFix(unittest.TestCase):
    """Ticket 05: 4-Layer Activity Validator and Safe --fix."""

    def test_validator_detects_untracked_and_fixes(self):
        with tempfile.TemporaryDirectory() as td:
            act_path = Path(td) / "dev_test [EXTtest]"
            pkg_dir = act_path / "tx"
            lbl_dir = pkg_dir / "label"
            tbl_dir = pkg_dir / "table" / "cmg"
            lbl_dir.mkdir(parents=True, exist_ok=True)
            tbl_dir.mkdir(parents=True, exist_ok=True)

            # Create mock table referencing a label that doesn't exist
            tbl_file = tbl_dir / "txcmg999.tbl"
            tbl_xml = """<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <name>txcmg999</name>
  <descriptionReference>txtxcmg999.header</descriptionReference>
  <Column>
    <name>btno</name>
    <datatype><nativeDatatype>3</nativeDatatype></datatype>
    <descriptionReference>txtxcmg999.btno</descriptionReference>
  </Column>
  <Index>
    <IndexColumn><name>btno</name></IndexColumn>
  </Index>
</DR_Table>
"""
            tbl_file.write_text(tbl_xml, encoding="utf-8")

            # Run validator without fix
            validator = ActivityValidator(act_path, strict=False, fix=False)
            report = validator.run()
            # Should detect missing labels (txtxcmg999.header and txtxcmg999.btno)
            self.assertTrue(any("txtxcmg999.header" in d.message for d in report.errors))

            # Run validator with --fix
            validator_fix = ActivityValidator(act_path, strict=False, fix=True)
            report_fix = validator_fix.run()
            # Missing labels should have been auto-generated
            self.assertTrue((lbl_dir / "txtxcmg999.header.lbl").exists())
            self.assertTrue((lbl_dir / "txtxcmg999.btno.lbl").exists())
            self.assertTrue(len(report_fix.repaired_items) > 0)


if __name__ == "__main__":
    unittest.main()
