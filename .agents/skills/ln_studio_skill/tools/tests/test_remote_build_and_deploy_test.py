#!/usr/bin/env python3
"""
Unit tests for Ticket 05 & Task 3.2:
Remote Server Build (Compile, CRDD, CreateTables, VSC), split deploy-test modes
(compile-only vs schema-crdd with --dry-run pre-check) & prepare-end-activity.
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

    def test_deploy_test_default_compile_only_mode(self):
        """Asserts default deploy_test mode is 'compile-only' (Put -> Compile -> executeVSC -> CheckIn without CRDD)."""
        tbl_file = self.act_dir / "tx" / "table" / "ibd" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")

        self.transport.register_response("DR_Table", "Put", "<PutResponse>OK</PutResponse>")
        self.transport.register_response("DR_Table", "Compile", "<CompileResponse><status>success</status></CompileResponse>")
        self.transport.register_response("DR_Table", "executeVSC", "<executeVSCResponse><status>pass</status></executeVSCResponse>")
        self.transport.register_response("DR_Table", "CheckIn", "<CheckInResponse><status>checked_in</status></CheckInResponse>")

        res = deploy_test(
            client=self.client,
            comp_type="table",
            comp_name="txibd001",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
            comment="Safe script-only deploy",
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["mode"], "compile-only")
        self.assertTrue(res["compiled"])
        self.assertFalse(res["crdd"])
        self.assertFalse(res["tables_created"])
        self.assertTrue(res["checked_in"])

        called_methods = [c["method"] for c in self.transport.call_history]
        self.assertEqual(called_methods, ["Put", "Compile", "executeVSC", "CheckIn"])

    def test_deploy_test_schema_crdd_mode_and_dry_run_precheck(self):
        """Asserts mode='schema-crdd' supports dry_run pre-check + lock warning and full CRDD execution."""
        tbl_file = self.act_dir / "tx" / "table" / "ibd" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")

        # 1. Dry-run pre-check must not call server BDEs and must emit lock_warning
        dry_res = deploy_test(
            client=self.client,
            comp_type="table",
            comp_name="txibd001",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
            mode="schema-crdd",
            dry_run=True,
        )
        self.assertTrue(dry_res["success"])
        self.assertTrue(dry_res["dry_run"])
        self.assertIn("ConvertToRuntime", dry_res["planned_steps"])
        self.assertIn("CreateTables", dry_res["planned_steps"])
        self.assertIsNotNone(dry_res["lock_warning"])
        self.assertEqual(len(self.transport.call_history), 0)

        # 2. Full schema-crdd execution
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
            comment="Full schema deploy",
            mode="schema-crdd",
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["mode"], "schema-crdd")
        self.assertTrue(res["crdd"])
        self.assertTrue(res["tables_created"])
        self.assertIsNotNone(res["lock_warning"])

        called_methods = [c["method"] for c in self.transport.call_history]
        self.assertEqual(
            called_methods,
            ["Put", "Compile", "ConvertToRuntime", "CreateTables", "executeVSC", "CheckIn"],
        )

    def test_prepare_end_activity_reporting(self):
        tbl_file = self.act_dir / "tx" / "table" / "ibd" / "txibd001.tbl"
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

    def test_parse_compile_diagnostics_authentic_xml(self):
        xml_resp = """<compileResult>
            <summary errors="1" warnings="1"/>
            <error line="10" source="txibd001"><![CDATA[Error in expression: syntax error]]></error>
            <warning line="25" source="txibd001" level="2"><![CDATA[Unused variable]]></warning>
            <bicCommand>bic6.2 -z</bicCommand>
        </compileResult>"""
        diags = parse_compile_diagnostics(xml_resp)
        self.assertEqual(len(diags), 2)
        self.assertEqual(diags[0]["severity"], "error")
        self.assertEqual(diags[0]["line"], 10)
        self.assertEqual(diags[0]["source"], "txibd001")
        self.assertEqual(diags[0]["message"], "Error in expression: syntax error")
        self.assertEqual(diags[1]["severity"], "warning")
        self.assertEqual(diags[1]["line"], 25)
        self.assertEqual(diags[1]["code"], "2")
        self.assertEqual(diags[1]["source"], "txibd001")

    def test_compile_component_authentic_show_mode_and_activity_context(self):
        self.transport.register_response(
            "DR_Table",
            "Compile",
            """<compileResult>
                <summary errors="0" warnings="0"/>
            </compileResult>""",
        )
        res = compile_component(
            client=self.client,
            comp_type="table",
            comp_name="txibd001",
            project_name="EXTce01107",
            activity_dir=self.act_dir,
            is_checked_out=True,
        )
        self.assertTrue(res["success"])
        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["bde"], "DR_Table")
        self.assertEqual(last_call["method"], "Compile")
        self.assertEqual(last_call["mode"], "SHOW")
        self.assertIn("<isCheckedOut>yes</isCheckedOut>", last_call["request"])
        self.assertIn("<name>txibd001</name>", last_call["request"])
        self.assertIsNotNone(last_call["context_xml"])

    def test_convert_to_runtime_and_create_tables_authentic_bde_mode(self):
        self.transport.register_response("DR_Table", "ConvertToRuntime", "<ConvertToRuntimeResponse>OK</ConvertToRuntimeResponse>")
        self.transport.register_response("DR_Table", "CreateTables", "<CreateTablesResponse>OK</CreateTablesResponse>")

        crdd_ok = convert_to_runtime(self.client, "table", "txibd001", "EXTce01107", activity_dir=self.act_dir)
        self.assertTrue(crdd_ok)

        ct_ok = create_tables(self.client, "txibd001", "EXTce01107", activity_dir=self.act_dir)
        self.assertTrue(ct_ok)

        crdd_call = self.transport.call_history[-2]
        self.assertEqual(crdd_call["mode"], "BDE")
        self.assertEqual(crdd_call["controlling_attributes"], {"executionMethod": "synchronous"})
        self.assertIsNotNone(crdd_call["context_xml"])

        ct_call = self.transport.call_history[-1]
        self.assertEqual(ct_call["mode"], "BDE")
        self.assertEqual(ct_call["controlling_attributes"], {"executionMethod": "synchronous"})
        self.assertIsNotNone(ct_call["context_xml"])

    def test_execute_vsc_authentic_xml_and_admin_sync(self):
        tbl_file = self.act_dir / "tx" / "table" / "ibd" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")
        from admin_sync import admin_after_get, list_admin_components
        admin_after_get(self.act_dir, "tx/table/ibd/txibd001.tbl")

        # Test compliant VSC
        self.transport.register_response(
            "VSC",
            "executeVSC",
            """<vscResult verificationCode="COMPLIANT">
                <warning accepted="true" blocking="false" warningID="W1" messageID="M1"><![CDATA[Minor hint]]></warning>
            </vscResult>""",
        )
        res = execute_vsc(self.client, "table", "txibd001", "EXTce01107", activity_dir=self.act_dir)
        self.assertTrue(res["passed"])
        self.assertEqual(res["verification_code"], "COMPLIANT")
        self.assertEqual(len(res["warnings"]), 1)
        comps = list_admin_components(self.act_dir)
        matching = [c for c in comps if "txibd001.tbl" in c["path"]]
        self.assertTrue(len(matching) > 0)
        self.assertTrue(matching[0]["isVSCHappy"])

        # Test blocking VSC
        self.transport.register_response(
            "VSC",
            "executeVSC",
            """<vscResult verificationCode="ERROR">
                <warning accepted="false" blocking="true" warningID="ERR1" messageID="M2"><![CDATA[Critical failure]]></warning>
            </vscResult>""",
        )
        res_fail = execute_vsc(self.client, "table", "txibd001", "EXTce01107", activity_dir=self.act_dir)
        self.assertFalse(res_fail["passed"])
        comps_fail = list_admin_components(self.act_dir)
        matching_fail = [c for c in comps_fail if "txibd001.tbl" in c["path"]]
        self.assertFalse(matching_fail[0]["isVSCHappy"])

    def test_prepare_end_activity_authentic_validate_development_activity(self):
        tbl_file = self.act_dir / "tx" / "table" / "ibd" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")
        from admin_sync import admin_after_get
        admin_after_get(self.act_dir, "tx/table/ibd/txibd001.tbl")

        self.transport.register_response(
            "CMLabel",
            "GetModifiedComponents",
            """<CMLabel>
                <ModifiedComponent><name>txibd001</name><type>table</type></ModifiedComponent>
            </CMLabel>""",
        )
        self.transport.register_response(
            "DR_Solution",
            "ValidateDevelopmentActivity",
            "<DR_Solution><result>valid</result></DR_Solution>",
        )
        self.transport.register_response("VSC", "executeVSC", "<vscResult verificationCode='COMPLIANT'/>")

        report = prepare_end_activity(
            client=self.client,
            activity_dir=self.act_dir,
            project_name="EXTce01107",
        )
        self.assertTrue(report["server_valid"])
        self.assertTrue(report["ready_for_human_review"])
        val_call = [c for c in self.transport.call_history if c["method"] == "ValidateDevelopmentActivity"][-1]
        self.assertEqual(val_call["mode"], "SHOW")
        self.assertIn("<projectName>EXTce01107</projectName>", val_call["request"])
        self.assertIn("<taskName>task_build_01</taskName>", val_call["request"])
        self.assertIn("<CMLabel><CMLabel><ModifiedComponent>", val_call["request"])
        vsc_calls = [c for c in self.transport.call_history if c["method"] == "executeVSC"]
        self.assertTrue(len(vsc_calls) >= 1, "prepare_end_activity must run executeVSC by default")
        self.assertIn("<packageCombination>ce01107</packageCombination>", vsc_calls[-1]["request"])

        # With skip_vsc=True, no additional executeVSC calls are made
        prev_vsc_count = len(vsc_calls)
        report_skip = prepare_end_activity(
            client=self.client,
            activity_dir=self.act_dir,
            project_name="EXTce01107",
            skip_vsc=True,
        )
        self.assertTrue(report_skip["server_valid"])
        vsc_calls_after = [c for c in self.transport.call_history if c["method"] == "executeVSC"]
        self.assertEqual(len(vsc_calls_after), prev_vsc_count)


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

        tbl_file = act_dir / "tables" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")

        args_prep = argparse.Namespace(activity=str(act_dir), project="EXTce01107", workspace=None, json=True, mock=True)
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_prepare_end_activity(args_prep)
        out = f.getvalue()
        self.assertIn("commit_summary", json.loads(out))

        temp_dir.cleanup()

    def test_sync_activity_refreshes_committed_and_preserves_dirty(self):
        import os
        import stat
        from ln_build_pipeline import sync_activity
        from ln_server_client import MockJcaTransport, LNStudioServerClient
        from admin_sync import init_admin_file, list_admin_components, admin_after_create, admin_after_get

        with tempfile.TemporaryDirectory() as td:
            act_dir = Path(td) / "dev_act1 [EXTce01107]"
            act_dir.mkdir(parents=True, exist_ok=True)
            (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
            settings = act_dir / ".settings"
            settings.mkdir(parents=True, exist_ok=True)
            (settings / "properties.index").write_text(
                "version=1\nsoftwareProject=EXTce01107\ntaskId=dev_act1\nactivityUUID=uuid-sync-01\nbaseVRC=B61O_a_ext\n",
                encoding="utf-8",
            )
            init_admin_file(act_dir / ".admin")

            # 1. Server-committed label (local non-dirty, non-checked-out) -> should be refreshed & Read-Only
            lbl_path = act_dir / "tx" / "label" / "txwh.clot.lbl"
            lbl_path.parent.mkdir(parents=True, exist_ok=True)
            lbl_path.write_text("<DR_Label><name>txwh.clot</name><versionID>OLD</versionID></DR_Label>", encoding="utf-8")
            admin_after_get(act_dir, "tx/label/txwh.clot.lbl")

            # 2. Locally Dirty / CheckedOut session -> must NEVER be overwritten
            ses_path = act_dir / "tx" / "session" / "wh" / "txwh1100m000.ses"
            ses_path.parent.mkdir(parents=True, exist_ok=True)
            ses_path.write_text("<DR_Controller><name>txwh1100m000</name><localEdit>1</localEdit></DR_Controller>", encoding="utf-8")
            admin_after_create(act_dir, "tx/session/wh/txwh1100m000.ses")

            # 3. Server-locked parallel label (locally non-dirty) -> must be skipped
            par_path = act_dir / "tx" / "label" / "txwh.par1.lbl"
            par_path.write_text("<DR_Label><name>txwh.par1</name><versionID>OLD_PAR</versionID></DR_Label>", encoding="utf-8")
            admin_after_get(act_dir, "tx/label/txwh.par1.lbl")

            transport = MockJcaTransport()
            client = LNStudioServerClient(transport=transport)

            def on_browse(*args, **kwargs):
                return (
                    "<DataArea>"
                    "<DR_Label><name>txwh.clot</name><versionID>B61O_a_ext.9</versionID>"
                    "<isCheckedOut>no</isCheckedOut><isCheckedOutParallel>no</isCheckedOutParallel></DR_Label>"
                    "<DR_Label><name>txwh.par1</name><versionID>B61O_a_ext.2</versionID>"
                    "<isCheckedOut>no</isCheckedOut><isCheckedOutParallel>yes</isCheckedOutParallel></DR_Label>"
                    "</DataArea>"
                )

            def on_get_source(*args, **kwargs):
                return (
                    "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                    "<DR_Label>\n  <name>txwh.clot</name>\n  <versionID>B61O_a_ext.9</versionID>\n</DR_Label>\n"
                )

            transport.register_handler("StudioComponent", "GetBrowseList", on_browse)
            transport.register_handler("StudioComponent", "GetActivitySource", on_get_source)

            summary = sync_activity(client, act_dir, "EXTce01107")
            self.assertEqual(summary["refreshed_count"], 1)
            self.assertEqual(summary["refreshed"][0]["name"], "txwh.clot")

            # Refreshed file is compacted single-line and Read-Only
            new_lbl = lbl_path.read_text(encoding="utf-8")
            self.assertIn("B61O_a_ext.9", new_lbl)
            self.assertNotIn(">\n", new_lbl)
            self.assertFalse(bool(os.stat(lbl_path).st_mode & stat.S_IWRITE), "Refreshed file must be Read-Only")

            # Local dirty file was preserved untouched
            self.assertIn("<localEdit>1</localEdit>", ses_path.read_text(encoding="utf-8"))
            self.assertTrue(any(s["name"] == "txwh1100m000" for s in summary["skipped_local"]))

            # Server parallel-locked file was preserved untouched
            self.assertIn("OLD_PAR", par_path.read_text(encoding="utf-8"))
            self.assertTrue(any(s["name"] == "txwh.par1" for s in summary["skipped_server"]))

            # .admin transitioned refreshed label cleanly via admin_after_get
            adm = {e["path"]: e for e in list_admin_components(act_dir)}
            lbl_entry = adm["tx/label/txwh.clot.lbl"]
            self.assertFalse(lbl_entry["isCheckedOut"])
            self.assertFalse(lbl_entry["isDirty"])

            # Verify GetBrowseList received context_xml
            browse_calls = [c for c in transport.call_history if c["method"] == "GetBrowseList"]
            self.assertTrue(any(c.get("context_xml") for c in browse_calls))


if __name__ == "__main__":
    unittest.main()
