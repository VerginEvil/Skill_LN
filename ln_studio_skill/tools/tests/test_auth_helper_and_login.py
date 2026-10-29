#!/usr/bin/env python3
"""
Unit tests for ln_auth_helper.py, capture_oob.py, and 'login' subcommand.
"""

import sys
import unittest
import urllib.parse
from pathlib import Path
from unittest.mock import patch, MagicMock

_TOOLS_DIR = Path(__file__).resolve().parent.parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_env_manager import IonapiConfig, OAuth2TokenManager
from ln_auth_helper import (
    build_robust_auth_url, register_oob_protocol, unregister_oob_protocol,
    get_windows_clipboard_text, get_pending_code_file
)
from ln_component_builder import resolve_ionapi_config


class TestAuthHelperAndLogin(unittest.TestCase):

    def setUp(self):
        self.sample_config = IonapiConfig(
            tenant_id="SLNBGS786BCXMXWQ_TST",
            client_name="LN Studio",
            device_type="11",
            client_id="SLNBGS786BCXMXWQ_TST~L871tflFMmNqtUSvKdCMbXwlmqfTN5tp6Hs7AUlS2JU",
            client_secret="dummy_secret",
            gateway_url="https://mingle-ionapi.ne1.inforcloudsuite.com",
            auth_url="https://mingle-sso.ne1.inforcloudsuite.com/SLNBGS786BCXMXWQ_TST/as/authorization.oauth2",
            token_url="https://mingle-sso.ne1.inforcloudsuite.com/SLNBGS786BCXMXWQ_TST/as/token.oauth2",
            revoke_url="https://mingle-sso.ne1.inforcloudsuite.com/SLNBGS786BCXMXWQ_TST/as/revoke_token.oauth2",
            scope="",
            redirect_uri="oob://localhost/lnstudio",
        )

    def test_build_robust_auth_url_suppresses_empty_scope(self):
        url, state = build_robust_auth_url(self.sample_config)
        self.assertIn("client_id=", url)
        self.assertIn("redirect_uri=oob%3A%2F%2Flocalhost%2Flnstudio", url)
        self.assertIn(f"state={state}", url)
        self.assertNotIn("scope=", url, "Empty or openid scope must be omitted to prevent Federation Hub crash")

    def test_build_robust_auth_url_includes_custom_scope(self):
        self.sample_config.scope = "custom_scope"
        url, state = build_robust_auth_url(self.sample_config)
        self.assertIn("scope=custom_scope", url)

    def test_resolve_ionapi_config_from_knowledge_docs(self):
        name, cfg = resolve_ionapi_config(workspace_name="SCS_TST")
        self.assertEqual(name, "SCS_TST")
        self.assertEqual(cfg.tenant_id, "SLNBGS786BCXMXWQ_TST")
        self.assertTrue(cfg.client_id.startswith("SLNBGS786BCXMXWQ_TST~"))

    @unittest.skipUnless(sys.platform == "win32", "Windows specific registry test")
    def test_register_and_unregister_oob_protocol(self):
        ok = register_oob_protocol()
        self.assertTrue(ok)
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\oob\shell\open\command") as key:
            cmd = winreg.QueryValue(key, "")
            self.assertIn("capture_oob.py", cmd)

        un_ok = unregister_oob_protocol()
        self.assertTrue(un_ok)
        with self.assertRaises(FileNotFoundError):
            winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\oob")

        # Re-register for live convenience
        register_oob_protocol()

    @unittest.skipUnless(sys.platform == "win32", "Windows specific clipboard test")
    def test_clipboard_reader_safe(self):
        clip = get_windows_clipboard_text()
        self.assertTrue(clip is None or isinstance(clip, str))


if __name__ == "__main__":
    unittest.main()
