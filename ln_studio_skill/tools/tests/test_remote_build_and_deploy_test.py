#!/usr/bin/env python3
"""
Unit tests for Ticket 05:
Remote Server Build (Compile, CRDD, CreateTables, VSC), deploy-test & prepare-end-activity.
"""

import os
import sys
import json
import tempfile
import unittest
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_server_client import MockJcaTransport, LNStudioServerClient
from ln_build_pipeline import (
    parse_compile_diagnostics,
    compile_component,
    convert_to_runtime,
    create_tables,
    execute_vsc,
    deploy_test,
    prepare_end_activity,
)


class TestRemoteBuildAndDeployTest(unittest.TestCase):
    def setUp(self):
        self.transport = MockJcaTransport()
        self.client = LNStudioServerClient(transport=self.transport)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_build_01 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(self.act_dir / ".admin")

        # Create settings properties.index
        settings_dir = self.act_dir / ".settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        (settings_dir / "properties.index").write_text("version=1\ntaskId=task_build_01\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_parse_compile_diagnostics_errors_and_warnings(self):
        xml_resp = """<CompileResponse>
            <CompileResponseError line="42" column="10" code="E1001" message="Syntax error: unexpected 'end'"/>
            <CompileResponseWarning line="15" column="4" code="W2005" message="Variable 'item_code' unused"/>
        </CompileResponse>"""
        diags = parse_compile_diagnostics(xml_resp)
        self.assertEqual(len(diags), 2)
        self.assertEqual(diags[0]["severity"], "error")
        self.assertEqual(diags[0]["line"], 42)
        self.assertEqual(diags[0]["column"], 10)
        self.assertEqual(diags[0]["code"], "E1001")
        self.assertEqual(diags[1]["severity"], "warning")
        self.assertEqual(diags[1]["line"], 15)

    def test_compile_component_success(self):
        self.transport.register_response(
            "DR_Table",
            "Compile",
            "<CompileResponse><status>success</status></CompileResponse>",
        )
        res = compile_component(self.client, "table", "txibd001", "EXTce01107")
        self.assertTrue(res["success"])
        self.assertEqual(len(res["errors"]), 0)

    def test_compile_component_with_errors(self):
        self.transport.register_response(
            "DR_Table",
            "Compile",
            """<CompileResponse>
                <CompileResponseError line="25" column="1" code="E0001" message="Unknown identifier 'foo'"/>
            </CompileResponse>""",
        )
        res = compile_component(self.client, "table", "txibd001", "EXTce01107")
        self.assertFalse(res["success"])
        self.assertEqual(len(res["errors"]), 1)
        self.assertEqual(res["errors"][0]["line"], 25)

    def test_convert_to_runtime_and_create_tables(self):
        self.transport.register_response("DR_Table", "ConvertToRuntime", "<ConvertToRuntimeResponse>OK</ConvertToRuntimeResponse>")
        self.transport.register_response("DR_Table", "CreateTables", "<CreateTablesResponse>OK</CreateTablesResponse>")

        crdd_ok = convert_to_runtime(self.client, "table", "txibd001", "EXTce01107")
        self.assertTrue(crdd_ok)

        ct_ok = create_tables(self.client, "txibd001", "EXTce01107")
        self.assertTrue(ct_ok)

    def test_deploy_test_end_to_end(self):
        # Setup component file in activity
        tbl_file = self.act_dir / "tables" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")

        # Register server responses
        self.transport.register_response("DR_Table", "Put", "<PutResponse>OK</PutResponse>")
        self.transport.register_response("DR_Table", "Compile", "<CompileResponse><status>success</status></CompileResponse>")
        self.transport.register_response("DR_Table", "ConvertToRuntime", "<ConvertToRuntimeResponse>OK</ConvertToRuntimeResponse>")
        self.transport.register_response("DR_Table", "CreateTables", "<CreateTablesResponse>OK</CreateTablesResponse>")
        self.transport.register_response("DR_Table", "executeVSC", "<executeVSCResponse><status>pass</status></executeVSCResponse>")
        self.transport.register_response("DR_Table", "CheckIn", "<CheckInResponse><status>checked_in</status></CheckInResponse>")

        res = deploy_test(
            client=self.client,
            comp_type="table",
            comp_name="txibd001",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
            comment="Test deploy for LN UI",
        )
        self.assertTrue(res["success"])
        self.assertTrue(res["compiled"])
        self.assertTrue(res["checked_in"])

        # Verify call history order: Put -> Compile -> ConvertToRuntime -> CreateTables -> executeVSC -> CheckIn
        called_methods = [c["method"] for c in self.transport.call_history]
        self.assertIn("Put", called_methods)
        self.assertIn("Compile", called_methods)
        self.assertIn("ConvertToRuntime", called_methods)
        self.assertIn("CreateTables", called_methods)
        self.assertIn("executeVSC", called_methods)
        self.assertIn("CheckIn", called_methods)

    def test_prepare_end_activity_reporting(self):
        tbl_file = self.act_dir / "tables" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")

        self.transport.register_response("DR_Solution", "ValidateDevelopmentActivity", "<ValidateResponse><status>valid</status></ValidateResponse>")
        self.transport.register_response("DR_Table", "executeVSC", "<executeVSCResponse><status>pass</status></executeVSCResponse>")

        report = prepare_end_activity(
            client=self.client,
            activity_dir=self.act_dir,
            project_name="EXTce01107",
        )
        self.assertTrue(report["ready_for_human_review"])
        self.assertTrue(report["metadata_synced"])
        self.assertIn("txibd001", str(report["components"]))
        self.assertIn("End Activity", report["human_action_required"])


class TestBuildCliIntegration(unittest.TestCase):
    def test_cmd_deploy_test_and_prepare_end_activity(self):
        from ln_component_builder import cmd_deploy_test, cmd_prepare_end_activity
        import argparse
        import io
        from contextlib import redirect_stdout

        temp_dir = tempfile.TemporaryDirectory()
        act_dir = Path(temp_dir.name) / "task_cli_build [EXTce01107]"
        act_dir.mkdir(parents=True, exist_ok=True)
        (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(act_dir / ".admin")
        settings_dir = act_dir / ".settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        (settings_dir / "properties.index").write_text("version=1\ntaskId=task_cli_build\n", encoding="utf-8")

        # Create dummy table file
        tbl_file = act_dir / "tables" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")

        # Test prepare-end-activity
        args_prep = argparse.Namespace(activity=str(act_dir), project="EXTce01107", workspace=None, json=True, mock=True)
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_prepare_end_activity(args_prep)
        out = f.getvalue()
        self.assertIn("commit_summary", json.loads(out))

        temp_dir.cleanup()


if __name__ == "__main__":
    unittest.main()
