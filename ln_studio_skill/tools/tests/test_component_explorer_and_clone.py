#!/usr/bin/env python3
"""
Unit tests for Ticket 03 & Task 2.2:
Component Explorer, Server Get / Clone Workflows, sync-reference (.reference/<type>/),
and automatic .ln_dd_cache.json indexing for Ecore .tbl and .dmn XMLs.
"""

import os
import sys
import stat
import json
import tempfile
import unittest
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_server_client import MockJcaTransport, LNStudioServerClient
from ln_component_explorer import (
    browse_components,
    get_component,
    inspect_component,
    clone_component,
    sync_reference,
    BDE_TYPE_MAP,
)
from scm_guardrails import ReadOnlyComponentError, is_file_readonly


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

    def test_get_component_workspace_mode_read_only_and_dd_cache_update(self):
        dd_cache_file = self.workspace_path / ".ln_dd_cache.json"
        self.transport.register_response(
            "DR_Table",
            "Get",
            """<DR_Table xmlns="http://www.infor.com/businessline/application/dr">
                <name>txcmg011</name>
                <description>Billing Batch Header</description>
                <Column>
                    <datatype><name>tcmcs.long</name><nativeDatatype>3</nativeDatatype></datatype>
                    <name>btno</name>
                    <fieldLabel>txcmg011.btno</fieldLabel>
                </Column>
                <Column>
                    <datatype><name>tcamnt</name><nativeDatatype>5</nativeDatatype></datatype>
                    <name>tamt</name>
                    <fieldLabel>txcmg011.tamt</fieldLabel>
                </Column>
                <Index>
                    <IndexColumn><name>btno</name></IndexColumn>
                </Index>
            </DR_Table>""",
        )
        saved_file = get_component(
            client=self.client,
            comp_type="table",
            comp_name="txcmg011",
            activity_dir=self.act_dir,
            read_only=True,
            dd_cache_path=dd_cache_file,
        )
        self.assertTrue(saved_file.exists())
        self.assertEqual(saved_file.name, "txcmg011.tbl")
        self.assertTrue(is_file_readonly(saved_file))

        # Verify Ecore <Column>/<Index> parsed into .ln_dd_cache.json
        self.assertTrue(dd_cache_file.exists())
        cache_data = json.loads(dd_cache_file.read_text(encoding="utf-8"))
        self.assertIn("txcmg011", cache_data["tables"])
        self.assertIn("btno", cache_data["tables"]["txcmg011"]["fields"])
        self.assertEqual(cache_data["tables"]["txcmg011"]["fields"]["btno"]["domain"], "tcmcs.long")
        self.assertEqual(cache_data["tables"]["txcmg011"]["indices"]["1"], ["btno"])

    def test_sync_reference_table_domain_extension_read_only(self):
        """Asserts sync_reference downloads into .reference/<type>/ Read-Only without modifying .admin and indexes DD cache."""
        dd_cache_file = self.workspace_path / ".ln_dd_cache.json"
        self.transport.register_response(
            "DR_Domain",
            "Get",
            """<DR_Domain xmlns="http://www.infor.com/businessline/application/dr">
                <name>txcmg.stat</name>
                <nativeDatatype>7</nativeDatatype>
                <Enumeration><constant>open</constant><description>Open</description></Enumeration>
                <Enumeration><constant>closed</constant><description>Closed</description></Enumeration>
            </DR_Domain>""",
        )
        res = sync_reference(
            client=self.client,
            comp_type="domain",
            name_pattern="txcmg.stat",
            workspace_root=self.workspace_path,
            dd_cache_path=dd_cache_file,
        )
        self.assertEqual(res["count"], 1)
        ref_file = Path(res["downloaded"][0]["path"])
        self.assertTrue(ref_file.exists())
        self.assertIn(".reference", ref_file.parts)
        self.assertTrue(is_file_readonly(ref_file))

        cache_data = json.loads(dd_cache_file.read_text(encoding="utf-8"))
        self.assertIn("txcmg.stat", cache_data["domains"])
        self.assertEqual(cache_data["domains"]["txcmg.stat"]["enum_values"], ["open", "closed"])

    def test_clone_component_and_block_extension_cloning(self):
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
        self.assertFalse(is_file_readonly(cloned_file))

        # Attempting to clone an extension component must raise ReadOnlyComponentError (ADR 0006)
        with self.assertRaises(ReadOnlyComponentError):
            clone_component(
                client=self.client,
                comp_type="extension",
                source_name="txestwmd400",
                target_name="txestwmd401",
                activity_dir=self.act_dir,
            )


if __name__ == "__main__":
    unittest.main()
