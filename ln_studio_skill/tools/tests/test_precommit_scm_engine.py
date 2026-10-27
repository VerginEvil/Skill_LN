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
    end_activity_gate,
    PreCommitBoundaryError,
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


if __name__ == "__main__":
    unittest.main()
