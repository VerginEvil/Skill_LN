#!/usr/bin/env python3
"""
Unit tests for Ticket 02:
Hermetic Mock Execution Test Suite for all MCP Tools in ln_studio_mcp.py.
ADR 0014: Quality Hardening and MCP Tool Execution Parity.
"""

import sys
import json
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_studio_mcp import execute_tool


class TestMcpToolExecution(unittest.TestCase):
    """Hermetic test suite exercising execute_tool for all registered MCP tools and actions."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_mcp [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        (self.act_dir / ".settings").mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".settings" / "properties.index").write_text("", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def _assert_envelope(self, res, expected_action, expect_error=False):
        self.assertEqual(res.get("isError", False), expect_error, f"Unexpected isError for {expected_action}")
        self.assertIn("content", res)
        self.assertTrue(len(res["content"]) > 0)
        self.assertEqual(res["content"][0]["type"], "text")
        data = json.loads(res["content"][0]["text"])
        expected_status = "error" if expect_error else "success"
        self.assertEqual(data.get("status"), expected_status)
        self.assertEqual(data.get("action"), expected_action)
        self.assertIn("result", data)
        self.assertIn("message", data)
        return data

    # 1. ln_list_environments
    @patch("ln_studio_mcp.list_configured_environments")
    def test_ln_list_environments(self, mock_list):
        mock_list.return_value = [{"workspace": "Team", "env": "PROD"}]
        res = execute_tool("ln_list_environments", {})
        data = self._assert_envelope(res, "ln_list_environments")
        self.assertIn("workspaces", data["result"])

    # 2. ln_connect
    @patch("ln_studio_mcp.sync_connectivity_prefs")
    @patch("ln_studio_mcp.sync_cloudenv_prefs")
    @patch("ln_studio_mcp.parse_ionapi")
    def test_ln_connect(self, mock_parse, mock_cloud, mock_conn):
        mock_cfg = MagicMock()
        mock_cfg.description = "Test Cloud"
        mock_cfg.token_url = "https://sso.test/token"
        mock_parse.return_value = mock_cfg
        mock_cloud.return_value = True
        mock_conn.return_value = True

        ionapi_file = Path(self.temp_dir.name) / "test.ionapi"
        ionapi_file.write_text("{}", encoding="utf-8")
        res = execute_tool("ln_connect", {"ionapi_file": str(ionapi_file), "workspace": "Team"})
        data = self._assert_envelope(res, "ln_connect")
        self.assertTrue(data["result"]["imported"])

    # 3. ln_explore_projects
    @patch("ln_studio_mcp.list_software_projects")
    def test_ln_explore_projects(self, mock_projs):
        mock_projs.return_value = ["EXTce01107", "COMMON"]
        res = execute_tool("ln_explore_projects", {"mock": True})
        data = self._assert_envelope(res, "ln_explore_projects")
        self.assertEqual(data["result"]["projects"], ["EXTce01107", "COMMON"])

    # 4. ln_explore_activities
    @patch("ln_studio_mcp.list_remote_activities")
    def test_ln_explore_activities(self, mock_acts):
        mock_acts.return_value = [{"task_id": "act_01"}]
        res = execute_tool("ln_explore_activities", {"project": "EXTce01107", "mock": True})
        data = self._assert_envelope(res, "ln_explore_activities")
        self.assertEqual(len(data["result"]["activities"]), 1)

    # 5. ln_explore_components
    @patch("ln_studio_mcp.browse_components")
    def test_ln_explore_components(self, mock_browse):
        mock_browse.return_value = [{"name": "ttadv300"}]
        res = execute_tool("ln_explore_components", {"type": "table", "mock": True})
        data = self._assert_envelope(res, "ln_explore_components")
        self.assertEqual(data["result"]["type"], "table")

    # 6. ln_create_activity
    @patch("ln_studio_mcp.bootstrap_local_activity")
    @patch("ln_studio_mcp.create_remote_activity")
    def test_ln_create_activity(self, mock_create, mock_boot):
        mock_create.return_value = {"task_id": "new_act", "status": "created"}
        res = execute_tool("ln_create_activity", {
            "project": "EXTce01107",
            "activity_id": "new_act",
            "bootstrap_local": False,
            "mock": True
        })
        data = self._assert_envelope(res, "ln_create_activity")
        self.assertTrue(data["result"]["success"])

    # 7. ln_clean_activity
    @patch("ln_studio_mcp.clean_remote_activity")
    def test_ln_clean_activity(self, mock_clean):
        mock_clean.return_value = True
        res = execute_tool("ln_clean_activity", {
            "project": "EXTce01107",
            "activity_id": "new_act",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_clean_activity")
        self.assertEqual(data["result"], {"cleaned": True})

    # 8. ln_get_component
    @patch("ln_studio_mcp.get_component")
    @patch("ln_studio_mcp.inspect_component")
    @patch("ln_studio_mcp.sync_reference")
    def test_ln_get_component(self, mock_sync, mock_inspect, mock_get):
        mock_get.return_value = Path("/saved/file.tbl")
        res = execute_tool("ln_get_component", {
            "type": "table",
            "name": "ttadv300",
            "activity": str(self.act_dir),
            "mock": True
        })
        data = self._assert_envelope(res, "ln_get_component")
        self.assertTrue(data["result"]["read_only"])

        # inspect_only
        mock_inspect.return_value = {"inspected": True}
        res_insp = execute_tool("ln_get_component", {
            "type": "table",
            "name": "ttadv300",
            "inspect_only": True,
            "mock": True
        })
        self._assert_envelope(res_insp, "ln_get_component")

        # reference_only
        mock_sync.return_value = {"synced": 1}
        res_ref = execute_tool("ln_get_component", {
            "type": "table",
            "name": "ttadv300",
            "reference_only": True,
            "mock": True
        })
        self._assert_envelope(res_ref, "ln_get_component")

    # 9. ln_sync_reference
    @patch("ln_studio_mcp.sync_reference")
    def test_ln_sync_reference(self, mock_sync):
        mock_sync.return_value = {"synced": 3}
        res = execute_tool("ln_sync_reference", {
            "type": "table",
            "name": "ttadv300",
            "workspace_dir": str(self.act_dir),
            "mock": True
        })
        data = self._assert_envelope(res, "ln_sync_reference")
        self.assertEqual(data["result"]["synced"], 3)

    # 10. ln_checkout_component
    @patch("ln_studio_mcp.checkout_component")
    def test_ln_checkout_component(self, mock_co):
        mock_res = MagicMock()
        mock_res.__str__.return_value = str(self.act_dir / "test.tbl")
        mock_res.receipt = MagicMock(to_dict=lambda: {"hash": "abc"})
        mock_co.return_value = mock_res

        res = execute_tool("ln_checkout_component", {
            "type": "table",
            "name": "ttadv300",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_checkout_component")
        self.assertTrue(data["result"]["checked_out"])

    # 11. ln_uncheckout_component
    @patch("ln_studio_mcp.uncheckout_component")
    def test_ln_uncheckout_component(self, mock_unco):
        mock_unco.return_value = True
        res = execute_tool("ln_uncheckout_component", {
            "type": "table",
            "name": "ttadv300",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_uncheckout_component")
        self.assertTrue(data["result"]["uncheckout"])

    # 12. ln_checkin_component
    @patch("ln_studio_mcp.checkin_component")
    def test_ln_checkin_component(self, mock_ci):
        mock_ci.return_value = {"hash": "def456"}
        res = execute_tool("ln_checkin_component", {
            "type": "table",
            "name": "ttadv300",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_checkin_component")
        self.assertTrue(data["result"]["checkin"])

    # 13. ln_checkout_activity
    @patch("ln_studio_mcp.checkout_activity")
    def test_ln_checkout_activity(self, mock_coa):
        mock_coa.return_value = {"activity_checked_out": True}
        res = execute_tool("ln_checkout_activity", {
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_checkout_activity")
        self.assertTrue(data["result"]["activity_checked_out"])

    # 14. ln_checkin_activity
    @patch("ln_studio_mcp.checkin_activity")
    def test_ln_checkin_activity(self, mock_cia):
        mock_cia.return_value = {"activity_checked_in": True}
        res = execute_tool("ln_checkin_activity", {
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_checkin_activity")
        self.assertTrue(data["result"]["activity_checked_in"])

    # 15. ln_create_component
    @patch("ln_studio_mcp.generate_messages")
    def test_ln_create_component(self, mock_gen):
        mock_gen.return_value = [Path(self.act_dir / "msg.xml")]
        res = execute_tool("ln_create_component", {
            "type": "message",
            "code": "txcmg0001",
            "activity": str(self.act_dir),
            "project": "EXTce01107"
        })
        data = self._assert_envelope(res, "ln_create_component")
        self.assertEqual(len(data["result"]["created_files"]), 1)

    # 16. ln_clone_component
    @patch("ln_studio_mcp.clone_component")
    def test_ln_clone_component(self, mock_clone):
        mock_clone.return_value = self.act_dir / "target.tbl"
        res = execute_tool("ln_clone_component", {
            "comp_type": "table",
            "source_name": "txcmg001",
            "target_name": "txcmg002",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_clone_component")
        self.assertIn("cloned_path", data["result"])

    # 17. ln_validate_activity
    @patch("ln_studio_mcp.validate_activity")
    def test_ln_validate_activity(self, mock_val):
        report = MagicMock()
        report.files_scanned = 5
        report.errors = []
        report.warnings = []
        mock_val.return_value = report

        res = execute_tool("ln_validate_activity", {"activity": str(self.act_dir)})
        data = self._assert_envelope(res, "ln_validate_activity")
        self.assertTrue(data["result"]["valid"])

    # 18. ln_deploy_test
    @patch("ln_studio_mcp.deploy_test")
    def test_ln_deploy_test(self, mock_dt):
        mock_dt.return_value = {"success": True, "compile": "OK"}
        res = execute_tool("ln_deploy_test", {
            "type": "table",
            "name": "ttadv300",
            "activity": str(self.act_dir),
            "mock": True
        })
        data = self._assert_envelope(res, "ln_deploy_test")
        self.assertTrue(data["result"]["success"])

    # 19. ln_prepare_end_activity
    @patch("ln_studio_mcp.prepare_end_activity")
    def test_ln_prepare_end_activity(self, mock_prep):
        mock_prep.return_value = {"ready_for_human_review": True}
        res = execute_tool("ln_prepare_end_activity", {
            "activity": str(self.act_dir),
            "mock": True
        })
        data = self._assert_envelope(res, "ln_prepare_end_activity")
        self.assertTrue(data["result"]["ready_for_human_review"])

    # 20. ln_end_activity
    @patch("ln_studio_mcp.end_activity_gate")
    def test_ln_end_activity(self, mock_gate):
        mock_gate.return_value = None
        res = execute_tool("ln_end_activity", {
            "activity": "task_01",
            "project": "EXTce01107"
        })
        data = self._assert_envelope(res, "ln_end_activity")
        self.assertTrue(data["result"]["completed"])

    # 21. ln_project_activity (all actions)
    @patch("ln_studio_mcp.get_software_project_details")
    @patch("ln_studio_mcp.list_remote_activities")
    @patch("ln_studio_mcp.create_remote_activity")
    @patch("ln_studio_mcp.open_remote_activity")
    @patch("ln_studio_mcp.clean_remote_activity")
    @patch("ln_studio_mcp.move_activity_components")
    @patch("ln_studio_mcp.clean_activity_components")
    def test_ln_project_activity_actions(self, mock_clean_comp, mock_move, mock_clean_act, mock_open_act, mock_create_act, mock_list_act, mock_info):
        # project_info
        mock_info.return_value = {"baseVRC": "B61U_a"}
        res = execute_tool("ln_project_activity", {"action": "project_info", "project": "EXTce01107", "mock": True})
        self._assert_envelope(res, "project_info")

        # list_activities
        mock_list_act.return_value = [{"task_id": "t1"}]
        res = execute_tool("ln_project_activity", {"action": "list_activities", "project": "EXTce01107", "mock": True})
        self._assert_envelope(res, "list_activities")

        # new_activity
        mock_create_act.return_value = {"task_id": "t2", "status": "created"}
        res = execute_tool("ln_project_activity", {"action": "new_activity", "project": "EXTce01107", "task": "t2", "mock": True})
        self._assert_envelope(res, "new_activity")

        # open_activity
        mock_open_act.return_value = {"task_id": "t2", "status": "opened"}
        res = execute_tool("ln_project_activity", {"action": "open_activity", "project": "EXTce01107", "task": "t2", "mock": True})
        self._assert_envelope(res, "open_activity")

        # clean_activity
        mock_clean_act.return_value = True
        res = execute_tool("ln_project_activity", {"action": "clean_activity", "project": "EXTce01107", "task": "t2", "mock": True})
        data = self._assert_envelope(res, "clean_activity")
        self.assertEqual(data["result"], {"cleaned": True})

        # move_components
        mock_move.return_value = {"success": True, "moved": 1}
        res = execute_tool("ln_project_activity", {
            "action": "move_components",
            "source_activity": str(self.act_dir),
            "mock": True
        })
        self._assert_envelope(res, "move_components")

        # clean_components
        mock_clean_comp.return_value = {"success": True, "cleaned": 1}
        res = execute_tool("ln_project_activity", {
            "action": "clean_components",
            "activity": str(self.act_dir),
            "mock": True
        })
        self._assert_envelope(res, "clean_components")

    # 22. ln_code_intelligence (all actions)
    @patch("ln_studio_mcp.search_server_pattern")
    @patch("ln_studio_mcp.get_call_hierarchy")
    @patch("ln_studio_mcp.open_declaration")
    @patch("ln_studio_mcp.generate_report_on_server")
    def test_ln_code_intelligence_actions(self, mock_gen_rpt, mock_open_decl, mock_call_h, mock_search):
        # search_server
        mock_search.return_value = {"matches": []}
        res = execute_tool("ln_code_intelligence", {"action": "search_server", "pattern": "select", "mock": True})
        self._assert_envelope(res, "search_server")

        # call_hierarchy
        mock_call_h.return_value = {"calls": []}
        res = execute_tool("ln_code_intelligence", {"action": "call_hierarchy", "source_file": "txcmg001.cln", "function_name": "calc", "mock": True})
        self._assert_envelope(res, "call_hierarchy")

        # open_declaration
        mock_open_decl.return_value = {"found": True, "line": 42}
        res = execute_tool("ln_code_intelligence", {"action": "open_declaration", "comp_code": "txcmg001", "comp_type": "table", "function_name": "init", "mock": True})
        self._assert_envelope(res, "open_declaration")

        # generate_report_server
        mock_gen_rpt.return_value = {"success": True, "report_name": "txcmg0110"}
        res = execute_tool("ln_code_intelligence", {"action": "generate_report_server", "report_name": "txcmg0110", "table_name": "ttadv300", "mock": True})
        self._assert_envelope(res, "generate_report_server")

    # 23. ln_version_diff (all actions)
    @patch("ln_studio_mcp.list_component_revisions")
    @patch("ln_studio_mcp.get_component_revision")
    @patch("ln_studio_mcp.diff_component")
    def test_ln_version_diff_actions(self, mock_diff, mock_get_rev, mock_list_rev):
        # list_revisions
        mock_list_rev.return_value = {"revisions": [1, 2]}
        res = execute_tool("ln_version_diff", {"action": "list_revisions", "comp_type": "table", "comp_name": "ttadv300", "mock": True})
        self._assert_envelope(res, "list_revisions")

        # get_revision
        mock_get_rev.return_value = "<tableRev1/>"
        res = execute_tool("ln_version_diff", {"action": "get_revision", "comp_type": "table", "comp_name": "ttadv300", "mock": True})
        data = self._assert_envelope(res, "get_revision")
        self.assertEqual(data["result"]["xml"], "<tableRev1/>")

        # diff_component
        mock_diff.return_value = {"diff": "--- +++"}
        res = execute_tool("ln_version_diff", {"action": "diff_component", "comp_type": "table", "comp_name": "ttadv300", "activity": str(self.act_dir), "mock": True})
        self._assert_envelope(res, "diff_component")

    # 24. ln_adhoc_compile
    @patch("ln_studio_mcp.compile_source_adhoc")
    def test_ln_adhoc_compile(self, mock_compile):
        mock_compile.return_value = {"success": True, "output": "Compilation OK"}
        res = execute_tool("ln_adhoc_compile", {
            "package_code": "tx",
            "source_code": "function extern void test() {}",
            "mock": True
        })
        data = self._assert_envelope(res, "ln_adhoc_compile")
        self.assertTrue(data["result"]["success"])


if __name__ == "__main__":
    unittest.main()
