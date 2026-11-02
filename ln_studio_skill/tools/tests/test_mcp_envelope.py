#!/usr/bin/env python3
"""
Unit tests for Ticket 01:
MCP Tool Dispatch and Envelope Normalization.
"""

import sys
import json
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_studio_mcp import execute_tool


class TestMcpDispatchAndEnvelope(unittest.TestCase):
    """Verifies that MCP tools use proper parameter dispatch and normalized envelopes."""

    @patch("ln_studio_mcp.create_remote_activity")
    def test_ln_create_activity_dispatch(self, mock_create):
        mock_create.return_value = {"task_id": "act01", "status": "created"}
        res = execute_tool("ln_create_activity", {
            "project": "EXTce01107",
            "activity_id": "act01",
            "bootstrap_local": False,
            "mock": True
        })
        self.assertFalse(res.get("isError", False))
        mock_create.assert_called_once()
        # Verify task_id is passed, not activity_id
        _, kwargs = mock_create.call_args
        self.assertEqual(kwargs.get("task_id"), "act01")
        self.assertNotIn("activity_id", kwargs)

        data = json.loads(res["content"][0]["text"])
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("action"), "ln_create_activity")
        self.assertIn("result", data)
        self.assertIn("message", data)
        self.assertEqual(set(data.keys()), {"status", "action", "result", "message"})

    @patch("ln_studio_mcp.clean_remote_activity")
    def test_ln_clean_activity_dispatch(self, mock_clean):
        mock_clean.return_value = True
        res = execute_tool("ln_clean_activity", {
            "project": "EXTce01107",
            "activity_id": "act01",
            "mock": True
        })
        self.assertFalse(res.get("isError", False))
        mock_clean.assert_called_once()
        _, kwargs = mock_clean.call_args
        self.assertEqual(kwargs.get("task_id"), "act01")
        self.assertNotIn("activity_id", kwargs)

        data = json.loads(res["content"][0]["text"])
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("action"), "ln_clean_activity")
        self.assertEqual(data.get("result"), {"cleaned": True})

    @patch("ln_studio_mcp.create_remote_activity")
    def test_project_activity_new_activity_dispatch(self, mock_create):
        mock_create.return_value = {"task_id": "task_01", "status": "created"}
        res = execute_tool("ln_project_activity", {
            "action": "new_activity",
            "project": "EXTce01107",
            "task": "task_01",
            "mock": True
        })
        self.assertFalse(res.get("isError", False))
        mock_create.assert_called_once()
        _, kwargs = mock_create.call_args
        self.assertEqual(kwargs.get("task_id"), "task_01")
        self.assertNotIn("task_name", kwargs)
        self.assertIn("auto_open", kwargs)

        data = json.loads(res["content"][0]["text"])
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("action"), "new_activity")

    @patch("ln_studio_mcp.open_remote_activity")
    def test_project_activity_open_activity_dispatch(self, mock_open):
        mock_open.return_value = {"task_id": "task_01", "status": "opened"}
        res = execute_tool("ln_project_activity", {
            "action": "open_activity",
            "project": "EXTce01107",
            "task": "task_01",
            "workspace": "/tmp/ws",
            "mock": True
        })
        self.assertFalse(res.get("isError", False))
        mock_open.assert_called_once()
        _, kwargs = mock_open.call_args
        self.assertEqual(kwargs.get("workspace_path"), "/tmp/ws")
        self.assertNotIn("workspace_dir", kwargs)

        data = json.loads(res["content"][0]["text"])
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("action"), "open_activity")

    @patch("ln_studio_mcp.clean_remote_activity")
    def test_project_activity_clean_activity_boolean_handling(self, mock_clean):
        # clean_remote_activity returns boolean True
        mock_clean.return_value = True
        res = execute_tool("ln_project_activity", {
            "action": "clean_activity",
            "project": "EXTce01107",
            "task": "task_01",
            "mock": True
        })
        # Should not crash calling .get() on bool!
        self.assertFalse(res.get("isError", False))
        mock_clean.assert_called_once()
        _, kwargs = mock_clean.call_args
        self.assertEqual(kwargs.get("task_id"), "task_01")

        data = json.loads(res["content"][0]["text"])
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("action"), "clean_activity")
        self.assertEqual(data.get("result"), {"cleaned": True})

    @patch("ln_studio_mcp.clone_component")
    def test_ln_clone_component_dispatch(self, mock_clone):
        mock_clone.return_value = Path("/tmp/target.tbl")
        res = execute_tool("ln_clone_component", {
            "source_type": "table",
            "source_name": "txcmg001",
            "target_name": "txcmg002",
            "activity": "/tmp/act",
            "mock": True
        })
        self.assertFalse(res.get("isError", False))
        mock_clone.assert_called_once()
        _, kwargs = mock_clone.call_args
        self.assertEqual(kwargs.get("comp_type"), "table")
        self.assertEqual(kwargs.get("activity_dir"), Path("/tmp/act"))
        self.assertNotIn("activity_path", kwargs)
        self.assertNotIn("source_type", kwargs)

        data = json.loads(res["content"][0]["text"])
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("action"), "ln_clone_component")


if __name__ == "__main__":
    unittest.main()
