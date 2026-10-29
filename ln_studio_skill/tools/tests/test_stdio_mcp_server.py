#!/usr/bin/env python3
"""
Unit tests for Ticket 08:
Native Stdio MCP Server (ln_studio_mcp.py) & mcp-setup CLI.
"""

import os
import sys
import json
import tempfile
import unittest
import subprocess
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

try:
    from ln_studio_mcp import (
        handle_jsonrpc_request,
        list_registered_tools,
        execute_tool,
        generate_mcp_config,
    )
except ImportError:
    # Will fail until ln_studio_mcp.py is created (TDD)
    handle_jsonrpc_request = None


class TestStdioMcpServer(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_mcp_01 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        (self.act_dir / ".settings").mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".settings" / "properties.index").write_text("", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(self.act_dir / ".admin")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_jsonrpc_initialize_and_ping(self):
        self.assertIsNotNone(handle_jsonrpc_request, "ln_studio_mcp module must be importable")
        init_req = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "clientInfo": {"name": "test-client", "version": "1.0.0"}
            }
        }
        res = handle_jsonrpc_request(init_req)
        self.assertEqual(res["jsonrpc"], "2.0")
        self.assertEqual(res["id"], 1)
        self.assertIn("serverInfo", res["result"])
        self.assertEqual(res["result"]["serverInfo"]["name"], "infor-ln-studio-mcp")

        ping_req = {"jsonrpc": "2.0", "id": 2, "method": "ping"}
        res_ping = handle_jsonrpc_request(ping_req)
        self.assertEqual(res_ping["id"], 2)
        self.assertEqual(res_ping["result"], {})

    def test_tools_list_schema(self):
        tools = list_registered_tools()
        tool_names = {t["name"] for t in tools}
        expected_tools = {
            "ln_list_environments",
            "ln_connect",
            "ln_explore_projects",
            "ln_explore_activities",
            "ln_explore_components",
            "ln_create_activity",
            "ln_clean_activity",
            "ln_get_component",
            "ln_checkout_component",
            "ln_uncheckout_component",
            "ln_checkin_component",
            "ln_create_component",
            "ln_clone_component",
            "ln_validate_activity",
            "ln_deploy_test",
            "ln_prepare_end_activity",
        }
        for et in expected_tools:
            self.assertIn(et, tool_names, f"Expected tool '{et}' missing from registered tools")

        # Verify tool schemas have type: object and properties
        for t in tools:
            self.assertIn("name", t)
            self.assertIn("description", t)
            self.assertIn("inputSchema", t)
            self.assertEqual(t["inputSchema"].get("type"), "object")

    def test_call_list_environments(self):
        res = execute_tool("ln_list_environments", {})
        self.assertFalse(res.get("isError", False))
        text = res["content"][0]["text"]
        self.assertIn("workspaces", text.lower())

    def test_call_explore_projects_mock(self):
        res = execute_tool("ln_explore_projects", {"mock": True})
        self.assertFalse(res.get("isError", False))
        text = res["content"][0]["text"]
        data = json.loads(text)
        self.assertTrue(len(data.get("projects", [])) > 0)

    def test_call_create_component_and_scm_guardrails(self):
        # Create message component via MCP
        create_res = execute_tool("ln_create_component", {
            "type": "message",
            "code": "txcmg0199",
            "description": "MCP Test Message",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
        })
        self.assertFalse(create_res.get("isError", False))
        msg_file = self.act_dir / "messages" / "txcmg0199.msg"
        self.assertTrue(msg_file.exists())

        # Check-out standard component (mock)
        chk_res = execute_tool("ln_checkout_component", {
            "type": "table",
            "name": "ttadv300",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        self.assertFalse(chk_res.get("isError", False))
        chk_data = json.loads(chk_res["content"][0]["text"])
        self.assertTrue(chk_data.get("checked_out"))
        self.assertIn("receipt", chk_data)

        # Check-in standard component (mock)
        chkin_res = execute_tool("ln_checkin_component", {
            "type": "table",
            "name": "ttadv300",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "comment": "Testing checkin receipt",
            "mock": True
        })
        self.assertFalse(chkin_res.get("isError", False))
        chkin_data = json.loads(chkin_res["content"][0]["text"])
        self.assertTrue(chkin_data.get("checkin"))
        self.assertIn("receipt", chkin_data)

        # Check-out tx extension component must be hard-blocked (ADR 0006)
        tx_chk_res = execute_tool("ln_checkout_component", {
            "type": "library",
            "name": "txesstext100",
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        self.assertTrue(tx_chk_res.get("isError", True))
        self.assertIn("ReadOnlyComponentError", tx_chk_res["content"][0]["text"])

    def test_call_prepare_end_activity_and_end_activity_gate(self):
        prep_res = execute_tool("ln_prepare_end_activity", {
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        self.assertFalse(prep_res.get("isError", False))

        # Direct end-activity call must fail with PreCommitBoundaryError (ADR 0007)
        gate_res = execute_tool("ln_end_activity", {
            "activity": str(self.act_dir),
            "project": "EXTce01107",
        })
        self.assertTrue(gate_res.get("isError", True))
        self.assertIn("PreCommitBoundaryError", gate_res["content"][0]["text"])

    def test_call_batch_checkout_and_checkin_activity_mcp(self):
        from admin_sync import add_component
        tbl = self.act_dir / "tables" / "txcmg010.tbl"
        tbl.parent.mkdir(parents=True, exist_ok=True)
        tbl.write_text("<DR_Table name='txcmg010'/>", encoding="utf-8")
        add_component(self.act_dir, "tables/txcmg010.tbl")

        chk_res = execute_tool("ln_checkout_activity", {
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "mock": True
        })
        self.assertFalse(chk_res.get("isError", False))
        data = json.loads(chk_res["content"][0]["text"])
        self.assertIn("checked_out_count", data)

        chkin_res = execute_tool("ln_checkin_activity", {
            "activity": str(self.act_dir),
            "project": "EXTce01107",
            "comment": "Batch MCP test",
            "mock": True
        })
        self.assertFalse(chkin_res.get("isError", False))
        data_in = json.loads(chkin_res["content"][0]["text"])
        self.assertIn("checked_in_count", data_in)

    def test_mcp_setup_config_generation(self):
        cfg = generate_mcp_config(client="generic")
        self.assertIn("mcpServers", cfg)
        self.assertIn("infor-ln-studio", cfg["mcpServers"])
        srv = cfg["mcpServers"]["infor-ln-studio"]
        self.assertEqual(srv["command"], sys.executable)
        self.assertTrue(any("ln_studio_mcp.py" in arg for arg in srv["args"]))

    def test_mcp_setup_cli_subcommand(self):
        target_cfg = Path(self.temp_dir.name) / "test_mcp.json"
        cmd = [
            sys.executable,
            str(SKILL_TOOLS / "ln_component_builder.py"),
            "mcp-setup",
            "--client", "generic",
            "--config-file", str(target_cfg),
            "--apply"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, msg=res.stderr)
        self.assertIn("[SUCCESS] Applied MCP registration", res.stdout)
        self.assertTrue(target_cfg.exists())
        saved = json.loads(target_cfg.read_text(encoding="utf-8"))
        self.assertIn("infor-ln-studio", saved.get("mcpServers", {}))

    def test_stdio_jsonrpc_subprocess_handshake(self):
        server_py = SKILL_TOOLS / "ln_studio_mcp.py"
        if not server_py.exists():
            self.skipTest("ln_studio_mcp.py not yet implemented")

        # Start server as subprocess over stdio
        p = subprocess.Popen(
            [sys.executable, str(server_py)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        try:
            req = json.dumps({"jsonrpc": "2.0", "id": 101, "method": "initialize", "params": {}})
            out, _ = p.communicate(input=req + "\n", timeout=5)
            response = json.loads(out.strip())
            self.assertEqual(response["id"], 101)
            self.assertEqual(response["result"]["serverInfo"]["name"], "infor-ln-studio-mcp")
        finally:
            p.kill()


if __name__ == "__main__":
    unittest.main()
