#!/usr/bin/env python3
"""
Unit tests for Ticket 03:
- Infer --workspace from --activity path or CWD
- Fail fast listing available workspaces when ambiguous (never default silently to unrelated tenant)
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_component_builder import get_server_client, resolve_workspace_for_command


class TestAuthAndWorkspaceHardening(unittest.TestCase):
    def _make_ws(self, root: Path, name: str, env_name: str):
        ws = root / name
        settings = ws / ".metadata" / ".plugins" / "org.eclipse.core.runtime" / ".settings"
        settings.mkdir(parents=True, exist_ok=True)
        (settings / "com.infor.erpln.jca.connectivity.prefs").write_text(
            f"ActivationType1=http_oauth2\nCloudEnvironment1={env_name}\n"
            f"Company1=0\nConfigurationCount=2\n"
            f"HostName1=https\\://gw.example.com/{env_name}_T/LN/webservice\nName1=ProjectServer\n",
            encoding="utf-8",
        )
        act = ws / "act_01 [EXTdemo]"
        act.mkdir(parents=True, exist_ok=True)
        (act / ".project").write_text("<projectDescription><name>act_01 [EXTdemo]</name></projectDescription>", encoding="utf-8")
        return ws, act

    def test_infers_workspace_from_activity_path_and_cwd(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._make_ws(root, "WS_FIRST", "WS_FIRST")
            ws2, act2 = self._make_ws(root, "WS_SECOND", "WS_SECOND")

            with patch.dict(os.environ, {"LN_WORKSPACE_ROOT": str(root)}), \
                 patch("ln_workspace_manager.load_config", return_value={}):
                inferred = resolve_workspace_for_command(
                    workspace_name=None,
                    activity_hint=str(act2),
                    ws_root=root,
                )
                self.assertEqual(inferred, "WS_SECOND")

                # Infer from CWD inside act2
                old_cwd = os.getcwd()
                try:
                    os.chdir(act2)
                    inferred_cwd = resolve_workspace_for_command(
                        workspace_name=None,
                        activity_hint=None,
                        ws_root=root,
                    )
                    self.assertEqual(inferred_cwd, "WS_SECOND")
                finally:
                    os.chdir(old_cwd)

    def test_ambiguous_multi_workspace_fails_fast_instead_of_picking_first(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._make_ws(root, "WS_ALPHA", "WS_ALPHA")
            self._make_ws(root, "WS_BETA", "WS_BETA")

            old_cwd = os.getcwd()
            try:
                os.chdir(root)
                with patch.dict(os.environ, {"LN_WORKSPACE_ROOT": str(root)}), \
                     patch("ln_workspace_manager.load_config", return_value={}), \
                     patch("ln_component_builder.load_config", return_value={}):
                    with self.assertRaises(ValueError) as ctx:
                        get_server_client(workspace_name=None, mock=False, notify=False)
                    msg = str(ctx.exception)
                    self.assertIn("WS_ALPHA", msg)
                    self.assertIn("WS_BETA", msg)
            finally:
                os.chdir(old_cwd)


if __name__ == "__main__":
    unittest.main()
