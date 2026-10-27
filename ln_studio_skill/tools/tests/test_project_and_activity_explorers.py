#!/usr/bin/env python3
"""
Unit tests for Ticket 02:
Software Project & Activity Explorers + Local Activity Bootstrap.
"""

import os
import sys
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_server_client import MockJcaTransport, LNStudioServerClient
from ln_project_activity_manager import (
    list_applications,
    list_software_projects,
    get_software_project_details,
    list_remote_activities,
    create_remote_activity,
    clean_remote_activity,
    bootstrap_local_activity,
)


class TestProjectAndActivityExplorers(unittest.TestCase):
    def setUp(self):
        self.transport = MockJcaTransport()
        self.client = LNStudioServerClient(transport=self.transport)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workspace_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_list_applications(self):
        self.transport.register_response(
            "Application",
            "List",
            """<Applications>
                <Application>
                    <name>LN</name>
                    <description>Infor CloudSuite LN Application</description>
                </Application>
                <Application>
                    <name>DEM</name>
                    <description>Dynamic Enterprise Modeler</description>
                </Application>
            </Applications>""",
        )
        apps = list_applications(self.client)
        self.assertEqual(len(apps), 2)
        self.assertEqual(apps[0]["name"], "LN")
        self.assertEqual(apps[1]["name"], "DEM")

    def test_list_software_projects(self):
        self.transport.register_response(
            "SoftwareProject",
            "List",
            """<SoftwareProjects>
                <SoftwareProject>
                    <name>EXTce01107</name>
                    <description>Customer Customizations Extension Project</description>
                    <status>active</status>
                </SoftwareProject>
                <SoftwareProject>
                    <name>STD108</name>
                    <description>Standard 10.8 Base</description>
                    <status>active</status>
                </SoftwareProject>
            </SoftwareProjects>""",
        )
        projs = list_software_projects(self.client)
        self.assertEqual(len(projs), 2)
        self.assertEqual(projs[0]["name"], "EXTce01107")
        self.assertEqual(projs[0]["status"], "active")

    def test_get_software_project_details(self):
        self.transport.register_response(
            "SoftwareProject_V2",
            "Show",
            """<SoftwareProject_V2>
                <name>EXTce01107</name>
                <description>Customer Project</description>
                <baseVRC>10.8.0.0</baseVRC>
                <workSetVRC>10.8_ext</workSetVRC>
                <PackageAssignments>
                    <Package>tc</Package>
                    <Package>td</Package>
                    <Package>wh</Package>
                    <Package>tx</Package>
                </PackageAssignments>
            </SoftwareProject_V2>""",
        )
        details = get_software_project_details(self.client, "EXTce01107")
        self.assertEqual(details["name"], "EXTce01107")
        self.assertEqual(details["workSetVRC"], "10.8_ext")
        self.assertIn("tx", details["packages"])

    def test_list_remote_activities(self):
        self.transport.register_response(
            "SoftwareProject_V2",
            "Show",
            """<SoftwareProject_V2>
                <name>EXTce01107</name>
                <Tasks>
                    <Task>
                        <taskId>dev_natt_1107-1</taskId>
                        <uuid>uuid-1122-3344-5566</uuid>
                        <description>First test activity</description>
                        <owner>nutdo</owner>
                        <status>open</status>
                    </Task>
                    <Task>
                        <taskId>dev_natt_1107-2</taskId>
                        <uuid>uuid-9988-7766-5544</uuid>
                        <description>Second test activity</description>
                        <owner>nutdo</owner>
                        <status>open</status>
                    </Task>
                </Tasks>
            </SoftwareProject_V2>""",
        )
        acts = list_remote_activities(self.client, "EXTce01107")
        self.assertEqual(len(acts), 2)
        self.assertEqual(acts[0]["task_id"], "dev_natt_1107-1")
        self.assertEqual(acts[0]["uuid"], "uuid-1122-3344-5566")

    def test_create_remote_activity(self):
        self.transport.register_response(
            "SoftwareProject_V2",
            "Change",
            """<SoftwareProject_V2>
                <Tasks action="create">
                    <Task>
                        <taskId>new_task_01</taskId>
                        <uuid>generated-uuid-abc</uuid>
                        <status>created</status>
                    </Task>
                </Tasks>
            </SoftwareProject_V2>""",
        )
        res = create_remote_activity(self.client, "EXTce01107", "new_task_01", "Create new component activity")
        self.assertEqual(res["task_id"], "new_task_01")
        self.assertEqual(res["uuid"], "generated-uuid-abc")

        # Verify outgoing BDE call payload
        call = self.transport.call_history[-1]
        self.assertEqual(call["bde"], "SoftwareProject_V2")
        self.assertEqual(call["method"], "Change")
        self.assertIn("new_task_01", call["request"])
        self.assertIn("Create new component activity", call["request"])

    def test_bootstrap_local_activity(self):
        act_dir = bootstrap_local_activity(
            workspace_path=self.workspace_path,
            task_id="task_bootstrap_01",
            project_name="EXTce01107",
            activity_uuid="uuid-boot-123",
            dev_connection="EXTce01107_dev",
        )
        self.assertTrue(act_dir.exists())
        self.assertEqual(act_dir.name, "task_bootstrap_01 [EXTce01107]")

        # 1. Check .project
        proj_file = act_dir / ".project"
        self.assertTrue(proj_file.exists())
        proj_xml = proj_file.read_text(encoding="utf-8")
        self.assertIn("<name>task_bootstrap_01 [EXTce01107]</name>", proj_xml)
        self.assertIn("com.infor.ln.studio.apps.core.fourglStudio", proj_xml)
        self.assertIn("com.infor.ln.studio.apps.core.bic", proj_xml)

        # 2. Check .admin
        admin_file = act_dir / ".admin"
        self.assertTrue(admin_file.exists())

        # 3. Check properties.index or Eclipse persistent project properties
        props_file = act_dir / ".settings" / "properties.index"
        self.assertTrue(props_file.exists())
        props_content = props_file.read_text(encoding="utf-8")
        self.assertIn("uuid-boot-123", props_content)
        self.assertIn("EXTce01107_dev", props_content)

    def test_clean_remote_activity(self):
        self.transport.register_response(
            "FglStudio",
            "CleanActivity",
            "<FglStudio><CleanActivityResponse><status>success</status></CleanActivityResponse></FglStudio>",
        )
        res = clean_remote_activity(self.client, "EXTce01107", "dev_natt_1107-1")
        self.assertTrue(res)
        call = self.transport.call_history[-1]
        self.assertEqual(call["bde"], "FglStudio")
        self.assertEqual(call["method"], "CleanActivity")


class TestProjectActivityCliIntegration(unittest.TestCase):
    def test_cmd_project_and_activity(self):
        from ln_component_builder import cmd_project, cmd_activity
        import argparse
        import io
        from contextlib import redirect_stdout

        # Test project command
        args_proj = argparse.Namespace(project=None, workspace=None, json=True, mock=True)
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_project(args_proj)
        out = f.getvalue()
        self.assertIn("projects", json.loads(out))

        # Test activity command
        args_act = argparse.Namespace(project="EXTce01107", workspace=None, json=True, mock=True, create=None, desc=None)
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_activity(args_act)
        out_act = f.getvalue()
        self.assertIn("activities", json.loads(out_act))


if __name__ == "__main__":
    unittest.main()
