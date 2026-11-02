#!/usr/bin/env python3
"""
Unit tests for Ticket 11:
Revision History, Structural Diff (revisions, diff-component),
Server Report Wizard (DR_Report.Generate) & Activity Maintenance (MoveComponent, CleanComponents).
"""

import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_server_client import MockJcaTransport, LNStudioServerClient
from ln_revision_diff import (
    list_component_revisions,
    get_component_revision,
    diff_component,
    generate_report_on_server,
    move_activity_components,
    clean_activity_components,
)
from admin_sync import init_admin_file, admin_after_create, list_admin_components


class TestRevisionDiffAndWizard(unittest.TestCase):
    def setUp(self):
        self.transport = MockJcaTransport()
        self.client = LNStudioServerClient(transport=self.transport)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_rev_01 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        init_admin_file(self.act_dir / ".admin")
        settings_dir = self.act_dir / ".settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        (settings_dir / "properties.index").write_text("version=1\ntaskId=task_rev_01\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_list_component_revisions(self):
        resp_xml = """<FglStudio>
            <revision number="1" versionID="1" date="2026-04-01" time="10:00:00" author="dev1" task="task_01" comment="Initial create"/>
            <revision number="2" versionID="1" date="2026-04-02" time="14:30:00" author="dev2" task="task_02" comment="Added validation"/>
        </FglStudio>"""
        self.transport.register_response("FglStudio", "GetRevisions", resp_xml, mode="BDE")

        res = list_component_revisions(
            client=self.client,
            comp_type="table",
            comp_name="txibd001",
            version_id="1",
            activity_dir=self.act_dir,
        )
        self.assertEqual(res["component_name"], "txibd001")
        self.assertEqual(res["total_revisions"], 2)
        # Should be sorted descending by number
        self.assertEqual(res["revisions"][0]["number"], 2)
        self.assertEqual(res["revisions"][0]["author"], "dev2")
        self.assertEqual(res["revisions"][1]["number"], 1)

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "GetRevisions")
        self.assertIn("<compCode>txibd001</compCode>", last_call["request"])
        self.assertIn("<compType>table</compType>", last_call["request"])

    def test_get_component_revision(self):
        resp_xml = """<DR_Table name="txibd001" versionID="1">
            <Field name="item" domain="tcitem"/>
            <expression><![CDATA[| 4GL script rev 2]]></expression>
        </DR_Table>"""
        self.transport.register_response("DR_Table", "GetRevision", resp_xml, mode="BDE")

        raw = get_component_revision(
            client=self.client,
            comp_type="table",
            comp_name="txibd001",
            version_id="1",
            rev_number=2,
            activity_dir=self.act_dir,
        )
        self.assertIn('name="txibd001"', raw)
        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "GetRevision")
        self.assertIn("<number>2</number>", last_call["request"])

    def test_diff_component_script_and_structural(self):
        # Create local table file
        tbl_dir = self.act_dir / "tables"
        tbl_dir.mkdir(parents=True, exist_ok=True)
        local_tbl = tbl_dir / "txibd001.tbl"
        local_tbl.write_text(
            """<DR_Table name="txibd001">
                <Field name="item" domain="tcitem" mandatory="yes"/>
                <Field name="desc" domain="tcdsca"/>
                <expression><![CDATA[
function extern txibd001.check() {
    return(1)
}
                ]]></expression>
            </DR_Table>""",
            encoding="utf-8",
        )
        admin_after_create(self.act_dir, "tables/txibd001.tbl")

        # Mock remote revision 1 (has extra field 'legacy_flag', missing 'desc', different script)
        remote_xml = """<DR_Table name="txibd001">
            <Field name="item" domain="tcitem" mandatory="no"/>
            <Field name="legacy_flag" domain="tcyesno"/>
            <expression><![CDATA[
function extern txibd001.check() {
    return(0)
}
            ]]></expression>
        </DR_Table>"""
        self.transport.register_response("DR_Table", "GetRevision", remote_xml, mode="BDE")

        diff_res = diff_component(
            client=self.client,
            comp_type="table",
            comp_name="txibd001",
            activity_dir=self.act_dir,
            target_rev_number=1,
        )
        self.assertTrue(diff_res["has_script_changes"])
        self.assertIn("-    return(0)", diff_res["script_diff"])
        self.assertIn("+    return(1)", diff_res["script_diff"])

        sd = diff_res["structural_diff"]
        self.assertTrue(diff_res["has_structural_changes"])
        # Added 'desc'
        added_names = [a["name"] for a in sd["added_elements"]]
        self.assertIn("desc", added_names)
        # Removed 'legacy_flag'
        removed_names = [r["name"] for r in sd["removed_elements"]]
        self.assertIn("legacy_flag", removed_names)
        # Modified 'item' (mandatory="yes" vs "no")
        modified_keys = [m["key"] for m in sd["modified_elements"]]
        self.assertIn("Field::item", modified_keys)

    def test_generate_report_on_server(self):
        resp_xml = """<DR_Report name="txcmg04010100" versionID="1" table="txcmg001">
            <description>General Ledger Report</description>
            <reportSize>80</reportSize>
            <reportType>1</reportType>
            <expression><![CDATA[| 4GL generated report script]]></expression>
        </DR_Report>"""
        self.transport.register_response("DR_Report", "Generate", resp_xml, mode="BDE")

        res = generate_report_on_server(
            client=self.client,
            report_name="txcmg04010100",
            table_name="txcmg001",
            version_id="1",
            description="General Ledger Report",
            report_size="80",
            report_type="1",
            used_index="1",
            input_fields=["item", "dsca", "amnt"],
            overwrite=True,
            activity_dir=self.act_dir,
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["report_name"], "txcmg04010100")
        self.assertIsNotNone(res["output_file"])
        self.assertTrue(Path(res["output_file"]).exists())

        # Verify .admin registration
        comps = list_admin_components(self.act_dir)
        matching = [c for c in comps if "txcmg04010100.rpt" in c["path"]]
        self.assertTrue(len(matching) > 0)

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "Generate")
        self.assertIn("<reportSize>80</reportSize>", last_call["request"])
        self.assertIn("<field>item</field>", last_call["request"])

    def test_move_activity_components(self):
        # Create a component in source activity
        tbl_file = self.act_dir / "tables" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")
        admin_after_create(self.act_dir, "tables/txibd001.tbl")

        # Create target activity directory
        tgt_dir = Path(self.temp_dir.name) / "task_target_02 [EXTce01107]"
        tgt_dir.mkdir(parents=True, exist_ok=True)
        init_admin_file(tgt_dir / ".admin")

        self.transport.register_response("FglStudio", "MoveComponent", "<result>ok</result>", mode="BDE")

        res = move_activity_components(
            client=self.client,
            components=[{"type": "table", "name": "txibd001"}],
            source_activity_dir=self.act_dir,
            target_task_name="task_target_02",
            target_task_uuid="UUID-TARGET-02",
            target_base_vrc="1",
            target_context="ProjectServer",
            target_activity_dir=tgt_dir,
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["moved_components"], 1)

        # File moved to target
        self.assertTrue((tgt_dir / "tables" / "txibd001.tbl").exists())
        self.assertFalse(tbl_file.exists())

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "MoveComponent")
        self.assertIn("<taskName>task_target_02</taskName>", last_call["request"])
        self.assertIn("<name>txibd001</name>", last_call["request"])

    def test_clean_activity_components(self):
        tbl_file = self.act_dir / "tables" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")
        admin_after_create(self.act_dir, "tables/txibd001.tbl")

        self.transport.register_response("FglStudio", "CleanComponents", "<result>ok</result>", mode="BDE")

        res = clean_activity_components(
            client=self.client,
            components=[{"type": "table", "name": "txibd001"}],
            activity_dir=self.act_dir,
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["cleaned_components"], 1)
        self.assertFalse(tbl_file.exists())

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "CleanComponents")
        self.assertIn("<name>txibd001</name>", last_call["request"])


class TestRevisionDiffCli(unittest.TestCase):
    def test_cli_subcommands(self):
        import argparse
        from ln_component_builder import (
            cmd_revisions,
            cmd_diff_component,
            cmd_generate_report_server,
            cmd_move_components,
            cmd_clean_components,
        )

        temp_dir = tempfile.TemporaryDirectory()
        act_dir = Path(temp_dir.name) / "task_cli_rev [EXTce01107]"
        act_dir.mkdir(parents=True, exist_ok=True)
        (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        init_admin_file(act_dir / ".admin")
        settings_dir = act_dir / ".settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        (settings_dir / "properties.index").write_text("version=1\ntaskId=task_cli_rev\n", encoding="utf-8")

        # 1. revisions CLI
        args_rev = argparse.Namespace(
            type="table",
            name="txibd001",
            version="1",
            activity=str(act_dir),
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_revisions(args_rev)
        out = json.loads(f.getvalue())
        self.assertEqual(out["component_name"], "txibd001")

        # 2. generate-report-server CLI
        args_gen = argparse.Namespace(
            code="txcmg04010100",
            table="txcmg001",
            version="1",
            desc="CLI report test",
            paper_width="80",
            report_type="1",
            index="1",
            fields="item,dsca",
            no_overwrite=False,
            activity=str(act_dir),
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_generate_report_server(args_gen)
        out = json.loads(f.getvalue())
        self.assertTrue(out["success"])

        # 3. diff-component CLI
        tbl_file = act_dir / "tables" / "txibd001.tbl"
        tbl_file.parent.mkdir(parents=True, exist_ok=True)
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")
        admin_after_create(act_dir, "tables/txibd001.tbl")

        args_diff = argparse.Namespace(
            type="table",
            name="txibd001",
            revision=1,
            version="1",
            activity=str(act_dir),
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_diff_component(args_diff)
        out = json.loads(f.getvalue())
        self.assertEqual(out["component_name"], "txibd001")

        # 4. move-components CLI
        args_mv = argparse.Namespace(
            components="table:txibd001",
            source_activity=str(act_dir),
            target_task="task_target",
            target_uuid="UUID-TGT",
            target_vrc="1",
            target_context="ProjectServer",
            target_activity=None,
            type="table",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_move_components(args_mv)
        out = json.loads(f.getvalue())
        self.assertTrue(out["success"])

        # 5. clean-components CLI
        tbl_file.write_text("<DR_Table name='txibd001'/>", encoding="utf-8")
        admin_after_create(act_dir, "tables/txibd001.tbl")
        args_cln = argparse.Namespace(
            components="table:txibd001",
            activity=str(act_dir),
            type="table",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_clean_components(args_cln)
        out = json.loads(f.getvalue())
        self.assertTrue(out["success"])

        temp_dir.cleanup()


if __name__ == "__main__":
    unittest.main()
