"""
Unit tests for ADR 0010: Pre-Fetch Server & Activity Authentication Verification & User Notification Guardrail.
"""

import io
import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

TOOLS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS_DIR))

from ln_env_manager import (
    IonapiConfig,
    OAuth2TokenManager,
    check_workspace_auth,
)
from ln_component_builder import get_server_client
from ln_studio_mcp import execute_tool


class TestPrefetchAuthGuardrail(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.cache_dir = Path(self.temp_dir.name)
        self.token_mgr = OAuth2TokenManager(cache_dir=self.cache_dir)
        self.config = IonapiConfig(
            tenant_id="TEST_TENANT",
            client_name="LNStudio",
            device_type="11",
            client_id="TEST_CLIENT",
            client_secret="TEST_SECRET",
            gateway_url="https://gateway.example.com",
            auth_url="https://sso.example.com/oauth2/authorize",
            token_url="https://sso.example.com/oauth2/token",
            revoke_url="https://sso.example.com/oauth2/revoke",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_check_token_status_missing(self):
        st = self.token_mgr.check_token_status("NON_EXISTENT_ENV")
        self.assertEqual(st["status"], "missing")
        self.assertIsNone(st["expires_in"])
        self.assertFalse(st["has_refresh_token"])

    def test_check_token_status_valid(self):
        tok_data = {
            "access_token": "valid_token_xyz",
            "refresh_token": "refresh_abc",
            "expires_at": time.time() + 3600,
        }
        self.token_mgr.save_token("TEST_ENV", tok_data)
        st = self.token_mgr.check_token_status("TEST_ENV")
        self.assertEqual(st["status"], "valid")
        self.assertTrue(st["expires_in"] > 300)
        self.assertTrue(st["has_refresh_token"])
        self.assertEqual(st["access_token"], "valid_token_xyz")

    def test_check_token_status_needs_refresh(self):
        # Expiry within safety buffer (e.g. 100 seconds left)
        tok_data = {
            "access_token": "expiring_token",
            "refresh_token": "refresh_abc",
            "expires_at": time.time() + 100,
        }
        self.token_mgr.save_token("TEST_ENV", tok_data)
        st = self.token_mgr.check_token_status("TEST_ENV")
        self.assertEqual(st["status"], "needs_refresh")
        self.assertTrue(st["has_refresh_token"])

    def test_check_token_status_expired(self):
        # Expired and no refresh token
        tok_data = {
            "access_token": "expired_token",
            "expires_at": time.time() - 50,
        }
        self.token_mgr.save_token("TEST_ENV", tok_data)
        st = self.token_mgr.check_token_status("TEST_ENV")
        self.assertEqual(st["status"], "expired")
        self.assertFalse(st["has_refresh_token"])

    def test_ensure_authenticated_token_valid(self):
        tok_data = {
            "access_token": "valid_123",
            "expires_at": time.time() + 3600,
        }
        self.token_mgr.save_token("TEST_ENV", tok_data)
        notifications = []
        tok = self.token_mgr.ensure_authenticated_token(
            env_name="TEST_ENV",
            config=self.config,
            auto_login=False,
            notify_fn=notifications.append,
        )
        self.assertEqual(tok, "valid_123")
        self.assertTrue(any("Active token verified" in n for n in notifications))

    def test_ensure_authenticated_token_silent_refresh(self):
        tok_data = {
            "access_token": "old_token",
            "refresh_token": "refresh_xyz",
            "expires_at": time.time() - 10,
        }
        self.token_mgr.save_token("TEST_ENV", tok_data)

        refreshed_data = {
            "access_token": "new_refreshed_token",
            "expires_in": 3600,
        }
        with patch.object(self.token_mgr, "refresh_access_token", return_value=refreshed_data):
            notifications = []
            tok = self.token_mgr.ensure_authenticated_token(
                env_name="TEST_ENV",
                config=self.config,
                auto_login=False,
                notify_fn=notifications.append,
            )
            self.assertEqual(tok, "new_refreshed_token")
            self.assertTrue(any("Token successfully refreshed" in n for n in notifications))

    def test_ensure_authenticated_token_unauthenticated_raises(self):
        notifications = []
        with self.assertRaises(PermissionError) as ctx:
            self.token_mgr.ensure_authenticated_token(
                env_name="TEST_ENV",
                config=self.config,
                auto_login=False,
                notify_fn=notifications.append,
            )
        self.assertIn("No valid token or refresh token", str(ctx.exception))
        self.assertIn("login --workspace", str(ctx.exception))

    def test_get_server_client_mock_prefetch_alert(self):
        buf = io.StringIO()
        with patch("sys.stdout", buf):
            client, info = get_server_client(
                workspace_name="mock_ws",
                mock=True,
                target_object="txibddllitem01",
                target_type="library",
                target_activity="dev_natt_1107-1",
                notify=True,
            )
        out = buf.getvalue()
        self.assertIn("[PRE-FETCH ALERT]", out)
        self.assertIn("txibddllitem01", out)
        self.assertIn("dev_natt_1107-1", out)
        self.assertIsNotNone(client)

    def test_mcp_ln_login_check_only(self):
        res = execute_tool("ln_login", {"check_only": True, "workspace": "SCS_TST"})
        self.assertFalse(res.get("isError", False))
        data = json.loads(res["content"][0]["text"])
        self.assertIn("status", data)
        self.assertIn("workspace", data)


if __name__ == "__main__":
    unittest.main()
