#!/usr/bin/env python3
"""
Unit tests for Ticket 10:
FglStudio Code Intelligence & Ad-Hoc Compile
(compile-source, search-server, call-hierarchy, open-declaration, related-components).
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
from ln_code_intelligence import (
    compile_source_adhoc,
    search_server_pattern,
    get_call_hierarchy,
    open_declaration,
    get_related_script_components,
)


class TestCodeIntelligence(unittest.TestCase):
    def setUp(self):
        self.transport = MockJcaTransport()
        self.client = LNStudioServerClient(transport=self.transport)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_intel_01 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        from admin_sync import init_admin_file
        init_admin_file(self.act_dir / ".admin")
        settings_dir = self.act_dir / ".settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        (settings_dir / "properties.index").write_text("version=1\ntaskId=task_intel_01\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_compile_source_adhoc_success(self):
        resp_xml = """<compileResult rootFileName="txcmg011">
            <summary numberOfErrors="0" numberOfWarnings="1"/>
            <warning line="15" source="txcmg011" level="2"><![CDATA[Unused variable 'x']]></warning>
            <bicCommand>bic6.2 -z txcmg011</bicCommand>
        </compileResult>"""
        self.transport.register_response("FglStudio", "compileSource", resp_xml, mode="SHOW")

        res = compile_source_adhoc(
            client=self.client,
            package_code="tx",
            source_code="function extern txcmg011() { return(0) }",
            flags="-z",
            project_name="EXTce01107",
            activity_dir=self.act_dir,
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["package_code"], "tx")
        self.assertEqual(res["bic_command"], "bic6.2 -z txcmg011")
        self.assertEqual(len(res["errors"]), 0)
        self.assertEqual(len(res["warnings"]), 1)
        self.assertEqual(res["warnings"][0]["line"], 15)

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "SHOW")
        self.assertEqual(last_call["bde"], "FglStudio")
        self.assertEqual(last_call["method"], "compileSource")
        self.assertIn("<packageCode>tx</packageCode>", last_call["request"])
        self.assertIn("function extern txcmg011", last_call["request"])
        self.assertIsNotNone(last_call["context_xml"])

    def test_compile_source_adhoc_with_errors(self):
        resp_xml = """<compileResult rootFileName="txcmg011">
            <summary numberOfErrors="1" numberOfWarnings="0"/>
            <error line="42" source="txcmg011"><![CDATA[Syntax error near 'syntax_error_here']]></error>
        </compileResult>"""
        self.transport.register_response("FglStudio", "compileSource", resp_xml, mode="SHOW")

        res = compile_source_adhoc(
            client=self.client,
            package_code="tx",
            source_code="invalid 4gl code syntax_error_here",
            activity_dir=self.act_dir,
        )
        self.assertFalse(res["success"])
        self.assertEqual(len(res["errors"]), 1)
        self.assertEqual(res["errors"][0]["line"], 42)
        self.assertIn("Syntax error", res["errors"][0]["message"])

    def test_search_server_pattern(self):
        resp_xml = """<FglStudio>
            <match component="txibd001" type="table" package="tx" line="10" snippet="select txibd001.* from txibd001"/>
            <match component="txsls0400m000" type="session" package="tx" line="55" snippet="txibd001.item = item_code"/>
        </FglStudio>"""
        self.transport.register_response("FglStudio", "Searchpattern", resp_xml, mode="BDE")

        res = search_server_pattern(
            client=self.client,
            pattern="txibd001",
            package_code="tx",
            activity_dir=self.act_dir,
        )
        self.assertEqual(res["pattern"], "txibd001")
        self.assertEqual(res["total_matches"], 2)
        self.assertEqual(res["matches"][0]["component"], "txibd001")
        self.assertEqual(res["matches"][0]["line"], 10)
        self.assertEqual(res["matches"][1]["component"], "txsls0400m000")
        self.assertEqual(res["matches"][1]["line"], 55)

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "Searchpattern")
        self.assertIn("<pattern>txibd001</pattern>", last_call["request"])

    def test_get_call_hierarchy(self):
        self.transport.register_response("fglstudio", "isValidFunction", "<result>true</result>", mode="BDE")
        resp_xml = """<FglStudio>
            <node name="zoom.to$" type="function" file="ottstpstandard" line="120"/>
            <node name="start.session" type="function" file="ottstpsession" line="45"/>
        </FglStudio>"""
        self.transport.register_response("fglstudio", "GetCallHierarchyData", resp_xml, mode="BDE")

        res = get_call_hierarchy(
            client=self.client,
            source_file_name="ottstpstandard",
            function_name="zoom.to$",
            call_mode="callers",
            activity_dir=self.act_dir,
        )
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["source_file_name"], "ottstpstandard")
        self.assertEqual(res["function_name"], "zoom.to$")
        self.assertEqual(res["total_nodes"], 2)
        self.assertEqual(res["hierarchy"][0]["function"], "zoom.to$")
        self.assertEqual(res["hierarchy"][0]["source_file"], "ottstpstandard")
        self.assertEqual(res["hierarchy"][0]["line"], 120)

        # Check that both isValidFunction and GetCallHierarchyData were dispatched
        called = [c["method"] for c in self.transport.call_history]
        self.assertIn("isValidFunction", called)
        self.assertIn("GetCallHierarchyData", called)

    def test_open_declaration(self):
        resp_xml = """<FglStudio>
            <compCodeFunction>txibddll001</compCodeFunction>
            <compTypeFunction>library</compTypeFunction>
            <lineno>88</lineno>
        </FglStudio>"""
        self.transport.register_response("FglStudio", "OpenDeclarationFunction", resp_xml, mode="BDE")

        res = open_declaration(
            client=self.client,
            comp_code="txsls0400m000",
            comp_type="session",
            function_name="txibddll001.calc_total",
            activity_dir=self.act_dir,
        )
        self.assertTrue(res["found"])
        self.assertEqual(res["component_code"], "txibddll001")
        self.assertEqual(res["component_type"], "library")
        self.assertEqual(res["line_number"], 88)

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "OpenDeclarationFunction")
        self.assertIn("<compCodeFunction>txsls0400m000</compCodeFunction>", last_call["request"])
        self.assertIn("<function>txibddll001.calc_total</function>", last_call["request"])

    def test_get_related_script_components(self):
        resp_xml = """<FglStudio>
            <component name="itcmg0001" type="include" versionID="1"/>
            <component name="txibddll001" type="library" versionID="2"/>
            <component name="txibd001" type="table" versionID="1"/>
        </FglStudio>"""
        self.transport.register_response("FglStudio", "GetScriptComponents", resp_xml, mode="BDE")

        res = get_related_script_components(
            client=self.client,
            package_code="tx",
            source_code="#include <itcmg0001>\nextern domain tcmg.id id",
            activity_dir=self.act_dir,
        )
        self.assertEqual(res["package_code"], "tx")
        self.assertEqual(res["total_components"], 3)
        names = [c["name"] for c in res["components"]]
        self.assertIn("itcmg0001", names)
        self.assertIn("txibddll001", names)
        self.assertIn("txibd001", names)

        last_call = self.transport.call_history[-1]
        self.assertEqual(last_call["mode"], "BDE")
        self.assertEqual(last_call["method"], "GetScriptComponents")
        self.assertIn("<packageCode>tx</packageCode>", last_call["request"])


class TestCodeIntelligenceCli(unittest.TestCase):
    def test_cli_subcommands(self):
        import argparse
        from ln_component_builder import (
            cmd_compile_source,
            cmd_search_server,
            cmd_call_hierarchy,
            cmd_open_declaration,
            cmd_related_components,
        )

        # 1. compile-source CLI
        args_cs = argparse.Namespace(
            package="tx",
            code="function extern test() {}",
            flags="",
            source_file=None,
            activity=None,
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_compile_source(args_cs)
        out = json.loads(f.getvalue())
        self.assertTrue(out["success"])

        # 2. search-server CLI
        args_ss = argparse.Namespace(
            pattern="test_pattern",
            package="tx",
            activity=None,
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_search_server(args_ss)
        out = json.loads(f.getvalue())
        self.assertEqual(out["pattern"], "test_pattern")

        # 3. call-hierarchy CLI
        args_ch = argparse.Namespace(
            source_file="ottstpstandard",
            function="zoom.to$",
            mode="callers",
            activity=None,
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_call_hierarchy(args_ch)
        out = json.loads(f.getvalue())
        self.assertEqual(out["function_name"], "zoom.to$")

        # 4. open-declaration CLI
        args_od = argparse.Namespace(
            comp="txsls0400m000",
            type="session",
            function="test.func",
            context="",
            activity=None,
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_open_declaration(args_od)
        out = json.loads(f.getvalue())
        self.assertEqual(out["function"], "test.func")

        # 5. related-components CLI
        args_rc = argparse.Namespace(
            package="tx",
            code="#include <itcmg0001>",
            source_file=None,
            activity=None,
            project="EXTce01107",
            workspace=None,
            json=True,
            mock=True,
        )
        f = io.StringIO()
        with redirect_stdout(f):
            cmd_related_components(args_rc)
        out = json.loads(f.getvalue())
        self.assertEqual(out["package_code"], "tx")


if __name__ == "__main__":
    unittest.main()
