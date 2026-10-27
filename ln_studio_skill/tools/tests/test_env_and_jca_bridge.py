#!/usr/bin/env python3
"""
Unit and integration tests for Ticket 01:
.ionapi Environment Manager, OAuth2 Lifecycle & Headless JCA Bridge.
"""

import os
import sys
import json
import time
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Ensure skill tools are importable
SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_env_manager import (
    parse_ionapi,
    sync_cloudenv_prefs,
    sync_connectivity_prefs,
    read_connectivity_prefs,
    list_configured_environments,
    OAuth2TokenManager,
    IonapiConfig,
)
from ln_server_client import (
    JcaTransport,
    MockJcaTransport,
    LNStudioServerClient,
    BdeExecutionError,
)


class TestIonapiEnvManager(unittest.TestCase):
    def setUp(self):
        self.sample_ionapi = {
            "ti": "TEST_TENANT_001",
            "cn": "LNStudio_Desktop",
            "dt": "11",
            "ci": "TEST_TENANT_001~client_id_abc123",
            "cs": "client_secret_xyz789",
            "iu": "https://mingle-ionapi.test.inforcloudsuite.com",
            "pu": "https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as",
            "oa": "authorization.oauth2",
            "ot": "token.oauth2",
            "or": "revoke_token.oauth2",
            "sc": "openid",
        }
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_parse_ionapi_valid(self):
        ion_file = self.temp_path / "TEST_ENV.ionapi"
        with open(ion_file, "w", encoding="utf-8") as f:
            json.dump(self.sample_ionapi, f)

        config = parse_ionapi(ion_file)
        self.assertEqual(config.tenant_id, "TEST_TENANT_001")
        self.assertEqual(config.client_id, "TEST_TENANT_001~client_id_abc123")
        self.assertEqual(config.client_secret, "client_secret_xyz789")
        self.assertEqual(config.gateway_url, "https://mingle-ionapi.test.inforcloudsuite.com")
        self.assertEqual(config.token_url, "https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/token.oauth2")
        self.assertEqual(config.auth_url, "https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/authorization.oauth2")
        self.assertEqual(config.device_type, "11")

    def test_parse_ionapi_with_service_account(self):
        sa_data = dict(self.sample_ionapi)
        sa_data["saak"] = "service_account_user"
        sa_data["sask"] = "service_account_password"
        ion_file = self.temp_path / "SA_ENV.ionapi"
        with open(ion_file, "w", encoding="utf-8") as f:
            json.dump(sa_data, f)

        config = parse_ionapi(ion_file)
        self.assertTrue(config.has_service_account())
        self.assertEqual(config.saak, "service_account_user")
        self.assertEqual(config.sask, "service_account_password")

    def test_sync_cloudenv_prefs_create_and_update(self):
        cloudenv_file = self.temp_path / "com.infor.erpln.jca.connectivity.cloudenv.prefs"
        config = IonapiConfig(
            tenant_id="TEST_TENANT_001",
            client_name="LNStudio",
            device_type="11",
            client_id="TEST_TENANT_001~client_id_abc123",
            client_secret="client_secret_xyz789",
            gateway_url="https://mingle-ionapi.test.inforcloudsuite.com",
            auth_url="https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/authorization.oauth2",
            token_url="https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/token.oauth2",
            revoke_url="https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/revoke_token.oauth2",
            scope="openid",
        )

        # 1. Create entry in empty/new file
        sync_cloudenv_prefs(cloudenv_file, "TEST_ENV", config)
        self.assertTrue(cloudenv_file.exists())
        content = cloudenv_file.read_text(encoding="utf-8")
        self.assertIn("EnvironmentsCount=1", content)
        self.assertIn("EnvironmentName0=TEST_ENV", content)
        self.assertIn("TenantID0=TEST_TENANT_001", content)
        self.assertIn(r"GatewayURL0=https\://mingle-ionapi.test.inforcloudsuite.com", content)

        # 2. Add second entry
        config2 = IonapiConfig(
            tenant_id="ANOTHER_TENANT",
            client_name="LNStudio",
            device_type="11",
            client_id="ANOTHER_TENANT~client2",
            client_secret="secret2",
            gateway_url="https://mingle-ionapi.test2.inforcloudsuite.com",
            auth_url="https://mingle-sso.test2.inforcloudsuite.com/as/auth.oauth2",
            token_url="https://mingle-sso.test2.inforcloudsuite.com/as/token.oauth2",
            revoke_url="https://mingle-sso.test2.inforcloudsuite.com/as/revoke.oauth2",
        )
        sync_cloudenv_prefs(cloudenv_file, "SECOND_ENV", config2)
        content = cloudenv_file.read_text(encoding="utf-8")
        self.assertIn("EnvironmentsCount=2", content)
        self.assertIn("EnvironmentName1=SECOND_ENV", content)

        # 3. Update existing entry without duplicating
        config.client_secret = "updated_secret_999"
        sync_cloudenv_prefs(cloudenv_file, "TEST_ENV", config)
        content = cloudenv_file.read_text(encoding="utf-8")
        self.assertIn("EnvironmentsCount=2", content)
        self.assertIn("ClientSecret0=updated_secret_999", content)

    def test_sync_connectivity_prefs(self):
        conn_file = self.temp_path / "com.infor.erpln.jca.connectivity.prefs"
        config = IonapiConfig(
            tenant_id="TEST_TENANT_001",
            client_name="LNStudio",
            device_type="11",
            client_id="TEST_TENANT_001~client_id_abc123",
            client_secret="client_secret_xyz789",
            gateway_url="https://mingle-ionapi.test.inforcloudsuite.com",
            auth_url="https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/authorization.oauth2",
            token_url="https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/token.oauth2",
            revoke_url="https://mingle-sso.test.inforcloudsuite.com:443/TEST_TENANT_001/as/revoke_token.oauth2",
        )

        sync_connectivity_prefs(
            conn_file,
            env_name="TEST_ENV",
            config=config,
            project_name="EXTce01107",
        )

        self.assertTrue(conn_file.exists())
        prefs = read_connectivity_prefs(conn_file)
        self.assertIn("ProjectServer", prefs)
        ps = prefs["ProjectServer"]
        self.assertEqual(ps.get("ActivationType"), "http_oauth2")
        self.assertEqual(ps.get("CloudEnvironment"), "TEST_ENV")
        self.assertEqual(
            ps.get("HostName"),
            "https://mingle-ionapi.test.inforcloudsuite.com/TEST_TENANT_001/LN/webservice",
        )
        self.assertIn("EXTce01107_dev", prefs)
        self.assertEqual(prefs["EXTce01107_dev"].get("SharedWith"), "ProjectServer")
        self.assertIn("EXTce01107_rt", prefs)
        self.assertEqual(prefs["EXTce01107_rt"].get("SharedWith"), "ProjectServer")

    def test_list_configured_environments(self):
        ws_root = self.temp_path / "workspaces"
        ws1 = ws_root / "SCS_TST" / ".metadata" / ".plugins" / "org.eclipse.core.runtime" / ".settings"
        ws1.mkdir(parents=True, exist_ok=True)
        conn_file1 = ws1 / "com.infor.erpln.jca.connectivity.prefs"
        conn_file1.write_text(
            "ConfigurationCount=2\n"
            "Name1=ProjectServer\n"
            "CloudEnvironment1=SCS_TST\n"
            r"HostName1=https\://mingle-ionapi.ne1.inforcloudsuite.com/SLNBGS786BCXMXWQ_TST/LN/webservice" + "\n"
            "ActivationType1=http_oauth2\n"
            "State1=valid\n",
            encoding="utf-8",
        )

        envs = list_configured_environments(workspace_root=ws_root)
        self.assertIn("SCS_TST", envs)
        self.assertEqual(envs["SCS_TST"]["tenant_id"], "SLNBGS786BCXMXWQ_TST")
        self.assertEqual(envs["SCS_TST"]["cloud_env"], "SCS_TST")


class TestOAuth2TokenLifecycle(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.cache_dir = Path(self.temp_dir.name) / "tokens"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.config = IonapiConfig(
            tenant_id="TEST_TENANT",
            client_name="LNStudio",
            device_type="11",
            client_id="TEST_CLIENT",
            client_secret="TEST_SECRET",
            gateway_url="https://gateway.example.com",
            auth_url="https://sso.example.com/as/authorization.oauth2",
            token_url="https://sso.example.com/as/token.oauth2",
            revoke_url="https://sso.example.com/as/revoke.oauth2",
        )
        self.manager = OAuth2TokenManager(cache_dir=self.cache_dir)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_cached_token_valid(self):
        # Store a token that expires in 1 hour
        token_data = {
            "access_token": "valid_token_123",
            "token_type": "Bearer",
            "expires_in": 3600,
            "expires_at": time.time() + 3600,
            "refresh_token": "refresh_token_456",
        }
        self.manager.save_token("MY_ENV", token_data)

        # Getting token should return valid_token_123 without calling network
        token = self.manager.get_access_token("MY_ENV", self.config)
        self.assertEqual(token, "valid_token_123")

    @patch("ln_env_manager.urllib.request.urlopen")
    def test_refresh_token_when_expired(self, mock_urlopen):
        # Store an expired token with refresh token
        token_data = {
            "access_token": "expired_token",
            "expires_in": 3600,
            "expires_at": time.time() - 100,
            "refresh_token": "valid_refresh_token",
        }
        self.manager.save_token("MY_ENV", token_data)

        # Mock token endpoint response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "access_token": "new_refreshed_token_789",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "new_refresh_token_abc",
        }).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        token = self.manager.get_access_token("MY_ENV", self.config)
        self.assertEqual(token, "new_refreshed_token_789")

    @patch("ln_env_manager.urllib.request.urlopen")
    def test_password_grant_for_service_account(self, mock_urlopen):
        self.config.saak = "service_user"
        self.config.sask = "service_password"

        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "access_token": "sa_token_xyz",
            "token_type": "Bearer",
            "expires_in": 3600,
        }).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        token = self.manager.get_access_token("SA_ENV", self.config)
        self.assertEqual(token, "sa_token_xyz")


class TestJcaBridgeAndServerClient(unittest.TestCase):
    def test_mock_jca_transport_ping(self):
        transport = MockJcaTransport()
        client = LNStudioServerClient(transport=transport)
        self.assertTrue(client.ping())

    def test_mock_jca_transport_do_bde_call(self):
        transport = MockJcaTransport()
        transport.register_response(
            "Application",
            "List",
            "<ApplicationList><Application><name>LN</name><title>Infor LN</title></Application></ApplicationList>",
        )

        client = LNStudioServerClient(transport=transport)
        xml_resp = client.do_bde_call("Application", "List", "<Request/>")
        self.assertIn("<Application>", xml_resp)
        self.assertIn("<name>LN</name>", xml_resp)

    def test_bde_error_raises_exception(self):
        transport = MockJcaTransport()
        transport.register_error(
            "SoftwareProject_V2",
            "Show",
            "Project EXTce01107 not found on server",
        )

        client = LNStudioServerClient(transport=transport)
        with self.assertRaises(BdeExecutionError) as ctx:
            client.do_bde_call("SoftwareProject_V2", "Show", "<ProjectName>EXTce01107</ProjectName>")
        self.assertIn("EXTce01107", str(ctx.exception))


class TestBuilderCliIntegration(unittest.TestCase):
    def test_cmd_environments(self):
        from ln_component_builder import cmd_environments
        import argparse
        import io
        from contextlib import redirect_stdout

        args = argparse.Namespace(json=True, workspace_root=None)
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_environments(args)
        output = f.getvalue()
        # Verify JSON output structure
        data = json.loads(output)
        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()
