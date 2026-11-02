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
from properties_index import PropertyBucket
from ln_project_activity_manager import (
    list_applications,
    show_application,
    list_software_projects,
    get_software_project_details,
    list_remote_activities,
    get_remote_activity_details,
    create_remote_activity,
    open_remote_activity,
    list_activity_modified_components,
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

    def test_show_application(self):
        """Tests show_application querying Application.Show in SHOW mode."""
        self.transport.register_response(
            "Application",
            "Show",
            """<Application>
                <name>LN</name>
                <description>Infor Enterprise CloudSuite LN</description>
                <release>B61O_a_ext</release>
                <Packages>
                    <Package>tc</Package>
                    <Package>td</Package>
                    <Package>tx</Package>
                </Packages>
            </Application>""",
        )
        app = show_application(self.client, "LN")
        self.assertEqual(app["name"], "LN")
        self.assertEqual(app["description"], "Infor Enterprise CloudSuite LN")
        self.assertEqual(app["release"], "B61O_a_ext")
        self.assertIn("tx", app["packages"])
        call = self.transport.call_history[-1]
        self.assertEqual(call["mode"], "SHOW")
        self.assertEqual(call["bde"], "Application")
        self.assertEqual(call["method"], "Show")

    def test_software_project_v2_show_full_metadata_and_task_fields(self):
        """Tests SoftwareProject_V2.Show extracting full project version, repo addresses, and task labelUUID vs taskUUID."""
        self.transport.register_response(
            "SoftwareProject_V2",
            "Show",
            """<SoftwareProject_V2>
                <projectName>EXTce01105</projectName>
                <projectDescription>Customer Customizations 01105</projectDescription>
                <projectVersionID>B61O_a_ext</projectVersionID>
                <developmentEnvironment>EXT</developmentEnvironment>
                <developmentRepositoryAddress>EXTce01105_dev</developmentRepositoryAddress>
                <runtimeRepositoryAddress>EXTce01105_rt</runtimeRepositoryAddress>
                <applicationServer>app_server_ln01</applicationServer>
                <isPartialEndAllowed>true</isPartialEndAllowed>
                <isSharingActivitiesAllowed>true</isSharingActivitiesAllowed>
                <integrationWithPMC>false</integrationWithPMC>
                <package>tc</package>
                <package>tx</package>
                <Tasks>
                    <Task>
                        <taskName>dev_natt_01105</taskName>
                        <labelUUID>dce45112-c35b-45e1-949a-b8b4b3664f99</labelUUID>
                        <taskUUID>SOL-PMC-998811</taskUUID>
                        <taskVersionID>2</taskVersionID>
                        <taskDescription>Dev. Natthaphon 01105</taskDescription>
                        <taskDocumentation>Documentation notes</taskDocumentation>
                        <taskRequirementID>REQ-7744</taskRequirementID>
                        <typeOfTask>enhancement</typeOfTask>
                        <assignedTo>nsrikase</assignedTo>
                        <taskStatus>opened</taskStatus>
                        <taskSeverity>medium</taskSeverity>
                        <functionalChange>yes</functionalChange>
                        <ActivityRelationships>
                            <ActivityRelationship>
                                <relatedActivityName>dev_natt_01103</relatedActivityName>
                                <relationshipType>predecessor</relationshipType>
                            </ActivityRelationship>
                        </ActivityRelationships>
                    </Task>
                </Tasks>
            </SoftwareProject_V2>""",
        )
        proj = get_software_project_details(self.client, "EXTce01105")
        self.assertEqual(proj["projectName"], "EXTce01105")
        self.assertEqual(proj["projectVersionID"], "B61O_a_ext")
        self.assertEqual(proj["baseVRC"], "B61O_a_ext")
        self.assertEqual(proj["developmentEnvironment"], "EXT")
        self.assertEqual(proj["developmentRepositoryAddress"], "EXTce01105_dev")
        self.assertEqual(proj["runtimeRepositoryAddress"], "EXTce01105_rt")
        self.assertTrue(proj["isPartialEndAllowed"])
        self.assertFalse(proj["integrationWithPMC"])
        self.assertIn("tx", proj["packages"])

        self.assertEqual(len(proj["tasks"]), 1)
        task = proj["tasks"][0]
        self.assertEqual(task["taskName"], "dev_natt_01105")
        self.assertEqual(task["task_id"], "dev_natt_01105")
        self.assertEqual(task["labelUUID"], "dce45112-c35b-45e1-949a-b8b4b3664f99")
        self.assertEqual(task["uuid"], "dce45112-c35b-45e1-949a-b8b4b3664f99")
        self.assertEqual(task["taskUUID"], "SOL-PMC-998811")
        self.assertNotEqual(task["labelUUID"], task["taskUUID"])  # Ground truth distinction
        self.assertEqual(task["taskVersionID"], "2")
        self.assertEqual(task["typeOfTask"], "enhancement")
        self.assertEqual(task["assignedTo"], "nsrikase")
        self.assertEqual(task["taskStatus"], "opened")
        self.assertEqual(len(task["relationships"]), 1)
        self.assertEqual(task["relationships"][0]["relatedActivityName"], "dev_natt_01103")

    def test_get_remote_activity_details_with_filter(self):
        """Tests get_remote_activity_details passing filter_expression for specific task."""
        self.transport.register_response(
            "SoftwareProject_V2",
            "Show",
            """<SoftwareProject_V2>
                <projectName>EXTce01105</projectName>
                <Tasks>
                    <Task>
                        <taskName>dev_natt_01105</taskName>
                        <labelUUID>uuid-1122-3344</labelUUID>
                        <taskUUID>SOL-01</taskUUID>
                        <taskStatus>opened</taskStatus>
                        <assignedTo>nutdo</assignedTo>
                    </Task>
                </Tasks>
            </SoftwareProject_V2>""",
        )
        act = get_remote_activity_details(self.client, "EXTce01105", "dev_natt_01105")
        self.assertIsNotNone(act)
        self.assertEqual(act["taskName"], "dev_natt_01105")
        self.assertEqual(act["labelUUID"], "uuid-1122-3344")

        # Verify filter expression was passed to transport
        call = self.transport.call_history[-1]
        self.assertEqual(call["filter_expression"], "Task.taskName == 'dev_natt_01105'")

    def test_bootstrap_local_activity_writes_binary_properties_index(self):
        """Asserts bootstrap_local_activity writes binary PropertyBucket in workspace .metadata."""
        act_dir = bootstrap_local_activity(
            workspace_path=self.workspace_path,
            task_id="task_prop_bin",
            project_name="EXTce01105",
            activity_uuid="uuid-bin-999",
            dev_connection="EXTce01105_dev",
        )
        meta_file = (
            self.workspace_path / ".metadata" / ".plugins" / "org.eclipse.core.resources" /
            ".projects" / "task_prop_bin [EXTce01105]" / ".indexes" / "properties.index"
        )
        self.assertTrue(meta_file.exists())
        bucket = PropertyBucket.load(meta_file)
        self.assertEqual(bucket.get_property("ProjectName"), "EXTce01105")
        self.assertEqual(bucket.get_property("TaskName"), "task_prop_bin")
        self.assertEqual(bucket.get_property("Label"), "uuid-bin-999")
        self.assertEqual(bucket.get_property("ApplicationUsesSCM"), "yes")
        self.assertEqual(bucket.get_property("repository", qualifier="org.eclipse.team.core"), "com.infor.ln.studio.apps.core.cmprovider")

    def test_new_activity_createsoftwaretaskv2_payload_and_server_response(self):
        """Tests create_remote_activity with full CreateSoftwareTaskV2.xml payload and labelUUID parsing."""
        self.transport.register_response(
            "SoftwareProject_V2",
            "Change",
            """<SoftwareProject_V2>
                <Task>
                    <taskName>dev_natt_01109</taskName>
                    <labelUUID>uuid-created-5566-7788</labelUUID>
                    <taskVersionID>1</taskVersionID>
                    <taskStatus>created</taskStatus>
                </Task>
            </SoftwareProject_V2>""",
        )
        res = create_remote_activity(
            client=self.client,
            project_name="EXTce01109",
            task_id="dev_natt_01109",
            description="Task for ticket 06 testing",
            task_documentation="Comprehensive docs",
            task_requirement_id="REQ-8899",
            type_of_task="enhancement",
            assigned_to="developer1",
            severity="high",
            functional_change="yes",
        )
        self.assertEqual(res["task_id"], "dev_natt_01109")
        self.assertEqual(res["labelUUID"], "uuid-created-5566-7788")
        self.assertEqual(res["taskVersionID"], "1")
        self.assertEqual(res["status"], "created")

        # Verify outgoing request payload matches CreateSoftwareTaskV2.xml
        call = self.transport.call_history[-1]
        self.assertEqual(call["bde"], "SoftwareProject_V2")
        self.assertEqual(call["method"], "Change")
        req = call["request"]
        self.assertIn('<SoftwareProject_V2 actionType="unchanged">', req)
        self.assertIn('<projectName>EXTce01109</projectName>', req)
        self.assertIn('<Task actionType="create">', req)
        self.assertIn('<taskName>dev_natt_01109</taskName>', req)
        self.assertIn('<assignedTo>developer1</assignedTo>', req)
        self.assertIn('<taskDescription>Task for ticket 06 testing</taskDescription>', req)
        self.assertIn('<taskDocumentation>Comprehensive docs</taskDocumentation>', req)
        self.assertIn('<taskRequirementID>REQ-8899</taskRequirementID>', req)
        self.assertIn('<taskSeverity>high</taskSeverity>', req)
        self.assertIn('<functionalChange>yes</functionalChange>', req)

    def test_open_remote_activity_lifecycle(self):
        """Tests open_remote_activity status transition, properties.index write, and modified components check."""
        # 1. Project details response
        self.transport.register_response(
            "SoftwareProject_V2",
            "Show",
            """<SoftwareProject_V2>
                <projectName>EXTce01105</projectName>
                <projectVersionID>B61O_a_ext</projectVersionID>
                <developmentEnvironment>EXT</developmentEnvironment>
                <developmentRepositoryAddress>EXTce01105_dev</developmentRepositoryAddress>
                <runtimeRepositoryAddress>EXTce01105_rt</runtimeRepositoryAddress>
                <Tasks>
                    <Task>
                        <taskName>dev_natt_01105</taskName>
                        <labelUUID>dce45112-c35b-45e1-949a-b8b4b3664f99</labelUUID>
                        <taskVersionID>1</taskVersionID>
                        <taskStatus>created</taskStatus>
                    </Task>
                </Tasks>
            </SoftwareProject_V2>""",
        )
        # 2. Status change to opened
        self.transport.register_response(
            "SoftwareProject",
            "Change",
            """<SoftwareProject>
                <Task>
                    <taskName>dev_natt_01105</taskName>
                    <taskStatus>opened</taskStatus>
                    <taskVersionID>2</taskVersionID>
                </Task>
            </SoftwareProject>""",
        )
        # 3. Modified components
        self.transport.register_response(
            "CMLabel",
            "GetModifiedComponents",
            """<CMLabel>
                <ModifiedComponent>
                    <name>txcmg011</name>
                    <type>table</type>
                    <package>tx</package>
                </ModifiedComponent>
            </CMLabel>""",
        )

        res = open_remote_activity(
            client=self.client,
            project_name="EXTce01105",
            task_name="dev_natt_01105",
            workspace_path=self.workspace_path,
            sync_modified=True,
        )

        self.assertEqual(res["task_id"], "dev_natt_01105")
        self.assertEqual(res["labelUUID"], "dce45112-c35b-45e1-949a-b8b4b3664f99")
        self.assertEqual(res["taskVersionID"], "2")
        self.assertEqual(res["status"], "opened")
        self.assertEqual(len(res["modified_components"]), 1)
        self.assertEqual(res["modified_components"][0]["name"], "txcmg011")

        # Verify binary properties.index
        meta_file = (
            self.workspace_path / ".metadata" / ".plugins" / "org.eclipse.core.resources" /
            ".projects" / "dev_natt_01105 [EXTce01105]" / ".indexes" / "properties.index"
        )
        self.assertTrue(meta_file.exists())
        bucket = PropertyBucket.load(meta_file)
        self.assertEqual(bucket.get_property("Label"), "dce45112-c35b-45e1-949a-b8b4b3664f99")
        self.assertEqual(bucket.get_property("ApplicationRelease"), "B61O_a_ext")
        self.assertEqual(bucket.get_property("TaskVersionID"), "2")
        self.assertEqual(bucket.get_property("TaskContext"), "EXTce01105_dev")
        self.assertEqual(bucket.get_property("DevelopmentEnvironment"), "EXT")

    def test_clean_remote_activity_authentic_payload_and_control_area(self):
        """Tests clean_remote_activity sending CleanActivity with ProjectClean and ActivityID in ControlArea."""
        self.transport.register_response(
            "FglStudio",
            "CleanActivity",
            "<Success/>",
        )
        res = clean_remote_activity(
            client=self.client,
            project_name="EXTce01105",
            task_id="dev_natt_01105",
            activity_uuid="uuid-clean-target-123",
            project_clean=False,
        )
        self.assertTrue(res)
        call = self.transport.call_history[-1]
        self.assertEqual(call["bde"], "FglStudio")
        self.assertEqual(call["method"], "CleanActivity")
        self.assertEqual(call["connection_point"], "EXTce01105_dev")
        self.assertIn("<ProjectClean>no</ProjectClean>", call["request"])
        self.assertIn("<ActivityID>uuid-clean-target-123</ActivityID>", call["context_xml"])


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
