#!/usr/bin/env python3
"""
Unit tests for Ticket 04:
Pre-Commit SCM Engine (Check-Out, Uncheckout, Put, Check-In & Hard-Blocked End Activity).
"""

import os
import sys
import stat
import json
import tempfile
import unittest
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_server_client import MockJcaTransport, LNStudioServerClient
from scm_guardrails import ReadOnlyComponentError
from ln_scm_engine import (
    checkout_component,
    uncheckout_component,
    put_component,
    checkin_component,
    checkout_activity,
    checkin_activity,
    end_activity_gate,
    PreCommitBoundaryError,
    ServerSCMExecutionError,
    VerificationReceipt,
    CheckedOutPath,
    build_checkout_payload,
    build_checkin_payload,
    build_uncheckout_payload,
    build_activity_context_xml,
    parse_scm_receipt,
    discover_dirty_components,
    segregate_extension_components,
    format_extension_guide_markdown,
    DEPENDENCY_ORDER,
)


class TestPrecommitScmEngine(unittest.TestCase):
    def setUp(self):
        self.transport = MockJcaTransport()
        self.client = LNStudioServerClient(transport=self.transport)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_scm_01 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(self.act_dir / ".admin")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_checkout_component_success(self):
        self.transport.register_response(
            "DR_Table",
            "CheckOut",
            """<DR_Table name="tdsls400" package="td" module="sls">
                <description>Sales Orders</description>
                <revision>1.2</revision>
            </DR_Table>""",
        )

        checked_out_file = checkout_component(
            client=self.client,
            comp_type="table",
            comp_name="tdsls400",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
        )
        self.assertTrue(checked_out_file.exists())
        self.assertEqual(checked_out_file.name, "tdsls400.tbl")

        # Verify file is writable (Read-Only cleared)
        from scm_guardrails import is_file_readonly
        self.assertFalse(is_file_readonly(checked_out_file))

        # Verify .admin status isCheckedOut=True
        from admin_sync import list_admin_components
        comps = list_admin_components(self.act_dir)
        matched = [c for c in comps if "tdsls400.tbl" in c["path"]]
        self.assertTrue(len(matched) > 0)
        self.assertTrue(matched[0]["isCheckedOut"])

    def test_checkout_extension_component_blocked_by_guardrail(self):
        # ADR 0006 guardrail: tx* extension modeler components are strictly Get-Only
        with self.assertRaises(ReadOnlyComponentError) as ctx:
            checkout_component(
                client=self.client,
                comp_type="library",
                comp_name="txesstext100",
                activity_dir=self.act_dir,
                project_name="EXTce01107",
            )
        self.assertIn("ttext1500m000", str(ctx.exception))

    def test_uncheckout_component(self):
        # Pre-create checked-out file
        tbl_file = self.act_dir / "tables" / "tdsls400.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='tdsls400'/>", encoding="utf-8")

        self.transport.register_response(
            "DR_Table",
            "UndoCheckOut",
            "<DR_Table><status>uncheck_out_success</status></DR_Table>",
        )

        uncheckout_component(
            client=self.client,
            comp_type="table",
            comp_name="tdsls400",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
        )

        call = self.transport.call_history[-1]
        self.assertEqual(call["bde"], "DR_Table")
        self.assertEqual(call["method"], "UndoCheckOut")

        # After uncheckout, file should be set to Read-Only
        from scm_guardrails import is_file_readonly
        self.assertTrue(is_file_readonly(tbl_file))

    def test_checkin_component(self):
        tbl_file = self.act_dir / "tables" / "tdsls400.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='tdsls400'><desc>Updated</desc></DR_Table>", encoding="utf-8")

        self.transport.register_response(
            "DR_Table",
            "CheckIn",
            "<DR_Table><status>checked_in</status><revision>1.3</revision></DR_Table>",
        )

        checkin_component(
            client=self.client,
            comp_type="table",
            comp_name="tdsls400",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
            comment="Updated sales order header description",
        )

        call = self.transport.call_history[-1]
        self.assertEqual(call["bde"], "DR_Table")
        self.assertEqual(call["method"], "CheckIn")
        self.assertIn("Updated sales order header description", call["request"])

        # File should be read-only after check-in
        from scm_guardrails import is_file_readonly
        self.assertTrue(is_file_readonly(tbl_file))

    def test_end_activity_hard_blocked_by_guardrail(self):
        # ADR 0007: End Activity is hard-blocked to keep human developer in the loop
        with self.assertRaises(PreCommitBoundaryError) as ctx:
            end_activity_gate(
                project_name="EXTce01107",
                task_id="task_scm_01",
            )
        self.assertIn("hard-blocked", str(ctx.exception).lower())
        self.assertIn("Infor LN Studio", str(ctx.exception))

    def test_authentic_payload_builders(self):
        # Ticket 01: Authentic BDE payloads reversed via REA
        chk_xml = build_checkout_payload("DR_Table", "txcmg010", "table", "B61O_a_ext", "task_scm_01", "task_scm_01")
        self.assertIn("<DR_Table>", chk_xml)
        self.assertIn("<name>txcmg010</name>", chk_xml)
        self.assertIn("<type>table</type>", chk_xml)
        self.assertIn("<versionID>B61O_a_ext</versionID>", chk_xml)
        self.assertIn("<taskLabel>task_scm_01</taskLabel>", chk_xml)
        self.assertIn("<optionalContent>yes</optionalContent>", chk_xml)

        ctx_xml = build_activity_context_xml("task_scm_01", "B61O_a_ext", "EXTce01107_dev", "uuid-123")
        self.assertIn("<ActivityID>", ctx_xml)
        self.assertIn("<activityName>task_scm_01</activityName>", ctx_xml)
        self.assertIn("<activityUUID>uuid-123</activityUUID>", ctx_xml)
        self.assertIn("<baseVRC>B61O_a_ext</baseVRC>", ctx_xml)
        self.assertIn("<activityContext>EXTce01107_dev</activityContext>", ctx_xml)

        raw_xml = "<DR_Table name='txcmg010'><desc>Test</desc></DR_Table>"
        chkin_xml = build_checkin_payload(raw_xml, "DV2600401 fix")
        self.assertIn("<Version><documentation>DV2600401 fix</documentation></Version>", chkin_xml)
        self.assertIn("<DR_Table name=\"txcmg010\">", chkin_xml)

        undo_xml = build_uncheckout_payload("DR_Table", "txcmg010", "table")
        self.assertIn("<versionID>see Activity ID</versionID>", undo_xml)

    def test_verification_receipt_and_anti_deception_guardrail(self):
        # Ticket 02: Verification receipts and halt on server rejection
        tbl_file = self.act_dir / "tables" / "txcmg010.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txcmg010'/>", encoding="utf-8")

        # Simulate server error response (e.g. lock failure)
        self.transport.register_response(
            "DR_Table",
            "CheckIn",
            "<error><message>Component txcmg010 is locked by user other</message></error>",
        )

        with self.assertRaises(ServerSCMExecutionError) as ctx:
            checkin_component(
                client=self.client,
                comp_type="table",
                comp_name="txcmg010",
                activity_dir=self.act_dir,
                project_name="EXTce01107",
                comment="Attempt checkin",
            )
        self.assertIn("Component txcmg010 is locked", str(ctx.exception))

        # Anti-deception: verify receipt parsing on valid response
        valid_resp = "<DR_Table name='txcmg010' versionID='1.4' timestamp='2026-10-29T10:00:00Z'><status>Success</status></DR_Table>"
        receipt = parse_scm_receipt(valid_resp, "txcmg010", "table", "CheckIn", "task_scm_01", "guid-123", "B61O_a_ext")
        self.assertEqual(receipt.component_name, "txcmg010")
        self.assertEqual(receipt.version_id, "1.4")
        self.assertEqual(receipt.status, "SUCCESS")
        self.assertEqual(receipt.operation, "CheckIn")

    def test_discover_dirty_components(self):
        # Ticket 03: Dirty discovery from disk
        from admin_sync import add_component
        tbl = self.act_dir / "tx" / "table" / "cmg" / "txcmg010.tbl"
        tbl.parent.mkdir(parents=True, exist_ok=True)
        tbl.write_text("<DR_Table name='txcmg010'/>", encoding="utf-8")
        add_component(self.act_dir, "tx/table/cmg/txcmg010.tbl")

        dirty = discover_dirty_components(self.act_dir)
        names = [d["name"] for d in dirty]
        self.assertIn("txcmg010", names)

    def test_batch_activity_scm_dependency_order_and_receipts(self):
        # Ticket 03: Batch checkout and checkin in dependency order
        from admin_sync import add_component
        ses_file = self.act_dir / "tx" / "session" / "cmg" / "txcmg0110m100.ses"
        tbl_file = self.act_dir / "tx" / "table" / "cmg" / "txcmg010.tbl"
        ses_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        ses_file.write_text("<DR_Controller name='txcmg0110m100'/>", encoding="utf-8")
        tbl_file.write_text("<DR_Table name='txcmg010'/>", encoding="utf-8")

        add_component(self.act_dir, "tx/session/cmg/txcmg0110m100.ses")
        add_component(self.act_dir, "tx/table/cmg/txcmg010.tbl")

        self.transport.register_response(
            "DR_Table", "CheckOut", "<DR_Table name='txcmg010' versionID='1.1'><status>Success</status></DR_Table>"
        )
        self.transport.register_response(
            "DR_Controller", "CheckOut", "<DR_Controller name='txcmg0110m100' versionID='1.1'><status>Success</status></DR_Controller>"
        )

        res = checkout_activity(
            client=self.client,
            activity_dir=self.act_dir,
            project_name="EXTce01107",
            components=[("session", "txcmg0110m100"), ("table", "txcmg010")],
        )
        self.assertEqual(res["checked_out_count"], 2)
        # Verify Table was processed BEFORE Session in dependency order
        bdes_called = [c["bde"] for c in self.transport.call_history if c["method"] == "CheckOut"]
        self.assertEqual(bdes_called, ["DR_Table", "DR_Controller"])

    def test_extension_segregation_and_markdown_guide(self):
        # Ticket 04: Extension components segregation
        comps = [
            {"name": "txcmg010", "type": "table", "is_extension": False},
            {"name": "txesscmg010", "type": "library", "is_extension": True},
        ]
        std, ext = segregate_extension_components(comps)
        self.assertEqual(len(std), 1)
        self.assertEqual(std[0]["name"], "txcmg010")
        self.assertEqual(len(ext), 1)
        self.assertEqual(ext[0]["name"], "txesscmg010")

        md = format_extension_guide_markdown(ext, self.act_dir)
        self.assertIn("ttext1500m000", md)
        self.assertIn("txesscmg010", md)

    def test_fail_fast_without_blind_rollback(self):
        # Ticket 03: Fail fast without rolling back already successful components
        from admin_sync import add_component
        tbl1 = self.act_dir / "tx" / "table" / "cmg" / "txcmg010.tbl"
        tbl2 = self.act_dir / "tx" / "table" / "cmg" / "txcmg011.tbl"
        tbl1.parent.mkdir(parents=True, exist_ok=True)
        tbl2.parent.mkdir(parents=True, exist_ok=True)
        tbl1.write_text("<DR_Table name='txcmg010'/>", encoding="utf-8")
        tbl2.write_text("<DR_Table name='txcmg011'/>", encoding="utf-8")
        add_component(self.act_dir, "tx/table/cmg/txcmg010.tbl")
        add_component(self.act_dir, "tx/table/cmg/txcmg011.tbl")

        # Mock first success, second failure using dynamic handler
        def _checkin_handler(req, cp, ctx):
            if "txcmg010" in req:
                return "<DR_Table name='txcmg010' versionID='1.2'><status>Success</status></DR_Table>"
            else:
                return "<error><message>Lock error on txcmg011</message></error>"

        self.transport.register_handler("DR_Table", "CheckIn", _checkin_handler)

        with self.assertRaises(ServerSCMExecutionError) as ctx:
            checkin_activity(
                client=self.client,
                activity_dir=self.act_dir,
                project_name="EXTce01107",
                comment="Batch test",
                components=[("table", "txcmg010"), ("table", "txcmg011")],
            )
        self.assertIn("Batch CheckIn halted on 'txcmg011'", str(ctx.exception))
        self.assertIn("Successfully checked in 1 components prior to failure", str(ctx.exception))


    def test_non_scm_project_checkout_and_checkin(self):
        # Set up properties.index with ApplicationUseSCM: no
        settings_dir = self.act_dir / ".settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        (settings_dir / "properties.index").write_bytes(b"version=1\nApplicationUseSCM=no\n")

        # Verify is_project_scm_enabled returns False
        from scm_guardrails import is_project_scm_enabled, is_tracked_checked_in
        scm_enabled, reason = is_project_scm_enabled(self.act_dir)
        self.assertFalse(scm_enabled)
        self.assertIn("ApplicationUseSCM=no", reason)

        # Create a component file
        tbl = self.act_dir / "tables" / "txcmg011.tbl"
        tbl.parent.mkdir(parents=True, exist_ok=True)
        tbl.write_text("<DR_Table><name>txcmg011</name><Version/></DR_Table>", encoding="utf-8")
        from admin_sync import add_component
        add_component(self.act_dir, "tables/txcmg011.tbl")

        # Since SCM is disabled, is_tracked_checked_in should return False
        checked_in, _ = is_tracked_checked_in(tbl, self.act_dir)
        self.assertFalse(checked_in)

        # Non-SCM checkout_component
        cko_res = checkout_component(
            client=self.client,
            comp_type="table",
            comp_name="txcmg011",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
        )
        self.assertTrue(cko_res.exists())
        self.assertEqual(cko_res.receipt["scm_mode"], "NON_SCM")
        self.assertEqual(cko_res.receipt["status"], "SUCCESS")

        # Non-SCM checkin_component
        cki_receipt = checkin_component(
            client=self.client,
            comp_type="table",
            comp_name="txcmg011",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
            comment="DV2600401: Billing system hardening",
        )
        self.assertEqual(cki_receipt["scm_mode"], "NON_SCM")
        self.assertEqual(cki_receipt["status"], "SUCCESS")
        # Verify comment is embedded in the component file
        content = tbl.read_text(encoding="utf-8")
        self.assertIn("<documentation>DV2600401: Billing system hardening</documentation>", content)


class TestScmCliIntegration(unittest.TestCase):
    def test_cmd_checkout_uncheckout_and_checkin(self):
        from ln_component_builder import cmd_checkout_component, cmd_uncheckout_component, cmd_checkin_component
        import argparse
        import io
        from contextlib import redirect_stdout

        temp_dir = tempfile.TemporaryDirectory()
        act_dir = Path(temp_dir.name) / "task_cli [EXTce01107]"
        act_dir.mkdir(parents=True, exist_ok=True)
        (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(act_dir / ".admin")

        args = argparse.Namespace(
            type="table", name="tdsls400", activity=str(act_dir), project="EXTce01107", workspace=None, mock=True
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_checkout_component(args)
        out = f.getvalue()
        self.assertIn("Checked out", out)

        temp_dir.cleanup()

    def test_cmd_checkout_and_checkin_activity(self):
        from ln_component_builder import cmd_checkout_activity, cmd_checkin_activity
        import argparse
        import io
        from contextlib import redirect_stdout
        from admin_sync import add_component

        temp_dir = tempfile.TemporaryDirectory()
        act_dir = Path(temp_dir.name) / "task_cli [EXTce01107]"
        act_dir.mkdir(parents=True, exist_ok=True)
        (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(act_dir / ".admin")

        tbl = act_dir / "tables" / "txcmg010.tbl"
        tbl.parent.mkdir(parents=True, exist_ok=True)
        tbl.write_text("<DR_Table name='txcmg010'/>", encoding="utf-8")
        add_component(act_dir, "tables/txcmg010.tbl")

        # Test batch checkout
        args_chk = argparse.Namespace(
            activity=str(act_dir), project="EXTce01107", workspace=None, json=True, mock=True
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_checkout_activity(args_chk)
        out = f.getvalue()
        self.assertIn('"checked_out_count"', out)

        # Test batch checkin
        args_chkin = argparse.Namespace(
            activity=str(act_dir), project="EXTce01107", workspace=None, comment="Test batch", json=True, mock=True
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_checkin_activity(args_chkin)
        out = f.getvalue()
        self.assertIn('"checked_in_count"', out)

        temp_dir.cleanup()



if __name__ == "__main__":
    unittest.main()
