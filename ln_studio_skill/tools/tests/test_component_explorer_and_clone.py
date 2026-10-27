#!/usr/bin/env python3
"""
Unit tests for Ticket 03:
Component Explorer & Server Get / Clone Workflows.
"""

import os
import sys
import stat
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_server_client import MockJcaTransport, LNStudioServerClient
from ln_component_explorer import (
    browse_components,
    get_component,
    inspect_component,
    clone_component,
    BDE_TYPE_MAP,
)


class TestComponentExplorerAndClone(unittest.TestCase):
    def setUp(self):
        self.transport = MockJcaTransport()
        self.client = LNStudioServerClient(transport=self.transport)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workspace_path = Path(self.temp_dir.name)

        # Bootstrap mock activity directory
        self.act_dir = self.workspace_path / "dev_act_01 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(self.act_dir / ".admin")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_browse_components(self):
        self.transport.register_response(
            "StudioComponent",
            "GetBrowseList",
            """<StudioComponent>
                <Component>
                    <name>tcibd001</name>
                    <type>table</type>
                    <package>tc</package>
                    <module>ibd</module>
                    <description>General Item Data</description>
                </Component>
                <Component>
                    <name>tdsls400</name>
                    <type>table</type>
                    <package>td</package>
                    <module>sls</module>
                    <description>Sales Orders</description>
                </Component>
            </StudioComponent>""",
        )
        comps = browse_components(self.client, package="tc", comp_type="table")
        self.assertEqual(len(comps), 2)
        self.assertEqual(comps[0]["name"], "tcibd001")
        self.assertEqual(comps[0]["package"], "tc")

    def test_get_component_inspect_mode(self):
        self.transport.register_response(
            "DR_Table",
            "Get",
            """<DR_Table name="tcibd001" package="tc" module="ibd">
                <description>General Item Data</description>
                <Fields>
                    <Field name="item" domain="tcitem" label="tcibd001.item"/>
                    <Field name="dsca" domain="tcdsca" label="tcibd001.dsca"/>
                </Fields>
                <Indices>
                    <Index number="1" unique="true">
                        <Field name="item"/>
                    </Index>
                </Indices>
                <dalScript>
                    function extern long before.save.object() { return(0) }
                </dalScript>
            </DR_Table>""",
        )
        summary = inspect_component(self.client, "table", "tcibd001")
        self.assertEqual(summary["name"], "tcibd001")
        self.assertEqual(summary["type"], "table")
        self.assertEqual(len(summary["fields"]), 2)
        self.assertEqual(summary["fields"][0]["name"], "item")
        self.assertIn("before.save.object", summary["script"])

    def test_get_component_workspace_mode_read_only(self):
        self.transport.register_response(
            "DR_Table",
            "Get",
            """<DR_Table name="tcibd001" package="tc" module="ibd">
                <description>General Item Data</description>
            </DR_Table>""",
        )
        saved_file = get_component(
            client=self.client,
            comp_type="table",
            comp_name="tcibd001",
            activity_dir=self.act_dir,
            read_only=True,
        )
        self.assertTrue(saved_file.exists())
        self.assertEqual(saved_file.name, "tcibd001.tbl")

        # Verify OS read-only attribute
        from scm_guardrails import is_file_readonly
        self.assertTrue(is_file_readonly(saved_file))

        # Verify .admin registration
        from admin_sync import list_admin_components
        comps = list_admin_components(self.act_dir)
        found = any("tcibd001.tbl" in c["path"] for c in comps)
        self.assertTrue(found)

    def test_clone_component(self):
        self.transport.register_response(
            "DR_Table",
            "Get",
            """<DR_Table name="tcibd001" package="tc" module="ibd">
                <description>General Item Data</description>
                <Fields>
                    <Field name="item" domain="tcitem" label="tcibd001.item"/>
                </Fields>
            </DR_Table>""",
        )
        self.transport.register_response(
            "DR_Table",
            "DR_Create",
            "<DR_Table><status>created</status></DR_Table>",
        )

        cloned_file = clone_component(
            client=self.client,
            comp_type="table",
            source_name="tcibd001",
            target_name="txibd001",
            activity_dir=self.act_dir,
            register_on_server=True,
        )
        self.assertTrue(cloned_file.exists())
        self.assertEqual(cloned_file.name, "txibd001.tbl")

        content = cloned_file.read_text(encoding="utf-8")
        self.assertIn('name="txibd001"', content)
        self.assertIn('package="tx"', content)
        self.assertIn('label="txibd001.item"', content)

        # Cloned file must be writable
        from scm_guardrails import is_file_readonly
        self.assertFalse(is_file_readonly(cloned_file))


class TestComponentCliIntegration(unittest.TestCase):
    def test_cmd_explorer_and_get(self):
        from ln_component_builder import cmd_explorer, cmd_get_component, cmd_clone_component
        import argparse
        import io
        from contextlib import redirect_stdout

        # Test explorer subcommand
        args_exp = argparse.Namespace(package="tc", type="table", filter=None, workspace=None, json=True, mock=True)
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_explorer(args_exp)
        out = f.getvalue()
        self.assertIn("components", json.loads(out))

        # Test get inspect mode
        args_get = argparse.Namespace(
            type="table", name="tcibd001", inspect=True, activity=None, workspace=None, json=True, mock=True
        )
        f_get = io.StringIO()
        with redirect_stdout(f_get):
            cmd_get_component(args_get)
        out_get = f_get.getvalue()
        data_get = json.loads(out_get)
        self.assertEqual(data_get["name"], "tcibd001")


if __name__ == "__main__":
    unittest.main()
