#!/usr/bin/env python3
"""
Unit tests for Ticket 01:
- Single-line TDE XML invariant (CDATA/expression-safe compaction) across generators, --fix, and BDE writers
- Parameterized LabelVariant <context> (1=field, 2=session/table, 10=FormCommand)
- Auto-adding <context>10</context> variant on editable shared labels vs Read-Only guard
"""

import os
import re
import stat
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from generate_ln_table import compact_tde_xml, generate_label_xml
from generate_ln_report import generate_report_xml
from generate_ln_message import generate_message_xml
from generate_ln_question import generate_question_xml
from generate_ln_function import generate_function_xml
from generate_ln_additional import generate_additional_xml
from generate_ln_session import generate_session
from validate_ln_activity import validate_activity
from admin_sync import init_admin_file, admin_after_create


def _has_newline_outside_script(xml: str) -> bool:
    stripped = re.sub(r"<!\[CDATA\[.*?\]\]>", "", xml, flags=re.S)
    stripped = re.sub(r"<expression>.*?</expression>", "", stripped, flags=re.S)
    stripped = re.sub(r"<content>.*?</content>", "", stripped, flags=re.S)
    return "\n" in stripped or "\r" in stripped


class TestXmlAndLabelHardening(unittest.TestCase):
    def test_compact_tde_xml_preserves_cdata_and_normalizes_header(self):
        pretty = (
            '<?xml version="1.0" encoding="UTF-8"?>\r\n'
            '<DR_Report>\r\n'
            '  <name>txinr04100100</name>\r\n'
            '  <Source>\r\n'
            '    <expression><![CDATA[\n'
            'detail.1:\n'
            '  if a > 0 then\n'
            '    | keep newlines <tag>\n'
            '  endif\n'
            ']]></expression>\r\n'
            '  </Source>\r\n'
            '</DR_Report>\r\n'
        )
        compacted = compact_tde_xml(pretty)
        self.assertTrue(compacted.startswith('<?xml version="1.0" encoding="UTF-8" standalone="no"?>'))
        self.assertFalse(_has_newline_outside_script(compacted))
        self.assertIn("detail.1:\n  if a > 0 then\n    | keep newlines <tag>\n  endif", compacted)
        self.assertTrue(compacted.endswith("</DR_Report>"))

    def test_all_generators_emit_single_line_xml_outside_script(self):
        rpt = generate_report_xml(
            {
                "code": "txinr04100100",
                "description": "Test Report",
                "script": "before.program:\n\t| line 2\n",
                "input_fields": [{"fieldname": "item", "domain": "tcitem"}],
            },
            application="EXTce01108",
        )
        msg = generate_message_xml({"code": "txinr0001", "description": "Err"}, application="EXTce01108")
        qst = generate_question_xml({"code": "txinr0002", "description": "Qst"}, application="EXTce01108")
        fnc = generate_function_xml(
            {"code": "txinrf001", "description": "Fn", "script": "function extern void f()\n{\n}\n"},
            application="EXTce01108",
        )
        add = generate_additional_xml(
            {"code": "txinrcfg", "description": "Cfg", "content": "{\n  \"a\": 1\n}"},
            application="EXTce01108",
        )

        for name, xml in [("report", rpt), ("message", msg), ("question", qst), ("function", fnc), ("additional", add)]:
            self.assertTrue(
                xml.startswith('<?xml version="1.0" encoding="UTF-8" standalone="no"?>'),
                f"{name} missing standalone='no' header",
            )
            self.assertFalse(_has_newline_outside_script(xml), f"{name} contains newlines outside CDATA/expression")

    def test_label_context_parameterization_and_session_command_contexts(self):
        lbl_field = generate_label_xml("txinr.dsca", "Description", "B61O_a_ext", "EXTce01108", context=1)
        lbl_ses = generate_label_xml("txinr1110m000", "Gov Licenses", "B61O_a_ext", "EXTce01108", context=2)
        lbl_cmd = generate_label_xml("txinr.export.csv", "Export CSV", "B61O_a_ext", "EXTce01108", context=10)

        self.assertIn("<context>1</context>", lbl_field)
        self.assertIn("<context>2</context>", lbl_ses)
        self.assertIn("<context>10</context>", lbl_cmd)

        with tempfile.TemporaryDirectory() as td:
            out_dir = Path(td)
            spec = {
                "application": "EXTce01108",
                "version_id": "B61O_a_ext",
                "session": {
                    "code": "txinr1110m000",
                    "description": "Gov Licenses",
                    "table": "txinr110",
                    "form_commands": [
                        {"name": "export.csv", "description": "Export CSV", "label_code": "txinr.export.csv"}
                    ],
                },
            }
            files = generate_session(schema_file=spec, output_dir=str(out_dir))
            by_name = {f["name"]: f["content"] for f in files}
            self.assertIn("<context>2</context>", by_name["txinr1110m000"])
            self.assertIn("<context>10</context>", by_name["txinr.export.csv"])

    def test_reusing_editable_label_for_form_command_adds_context10_and_blocks_readonly(self):
        with tempfile.TemporaryDirectory() as td:
            act_dir = Path(td) / "dev_test [EXTce01108]"
            lbl_dir = act_dir / "tx" / "label"
            lbl_dir.mkdir(parents=True, exist_ok=True)
            (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
            init_admin_file(act_dir / ".admin")

            # Existing editable label with only context=2
            existing_lbl = lbl_dir / "txinr1210m000.lbl"
            existing_lbl.write_text(
                generate_label_xml("txinr1210m000", "Sub Session", "B61O_a_ext", "EXTce01108", context=2),
                encoding="utf-8",
            )
            admin_after_create(act_dir, "tx/label/txinr1210m000.lbl")

            spec = {
                "application": "EXTce01108",
                "version_id": "B61O_a_ext",
                "session": {
                    "code": "txinr1110m000",
                    "description": "Main Session",
                    "table": "txinr110",
                    "form_commands": [
                        {"name": "open.sub", "description": "Sub Session", "label_code": "txinr1210m000"}
                    ],
                },
            }
            generate_session(schema_file=spec, activity_path=str(act_dir))
            updated = existing_lbl.read_text(encoding="utf-8")
            self.assertIn("<context>2</context>", updated)
            self.assertIn("<context>10</context>", updated)
            self.assertFalse(_has_newline_outside_script(updated))

            # Now mark Read-Only with only context=1 and verify error without mutation
            ro_lbl = lbl_dir / "txinr.ro.cmd.lbl"
            ro_content = generate_label_xml("txinr.ro.cmd", "RO Cmd", "B61O_a_ext", "EXTce01108", context=1)
            ro_lbl.write_text(ro_content, encoding="utf-8")
            os.chmod(ro_lbl, stat.S_IREAD)
            try:
                spec["session"]["form_commands"] = [
                    {"name": "ro.cmd", "description": "RO Cmd", "label_code": "txinr.ro.cmd"}
                ]
                with self.assertRaises(Exception):
                    generate_session(schema_file=spec, activity_path=str(act_dir))
                self.assertEqual(ro_lbl.read_text(encoding="utf-8"), ro_content)
            finally:
                os.chmod(ro_lbl, stat.S_IWRITE | stat.S_IREAD)

    def test_validator_layer2_rejects_multiline_xml_and_fix_compacts_single_line_labels(self):
        with tempfile.TemporaryDirectory() as td:
            act_dir = Path(td) / "dev_test [EXTce01108]"
            lbl_dir = act_dir / "tx" / "label"
            tbl_dir = act_dir / "tx" / "table" / "inr"
            lbl_dir.mkdir(parents=True, exist_ok=True)
            tbl_dir.mkdir(parents=True, exist_ok=True)
            (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
            init_admin_file(act_dir / ".admin")

            # Pretty-printed label must be flagged by Layer 2
            bad_lbl = lbl_dir / "txinr.bad.lbl"
            bad_lbl.write_text(
                '<?xml version="1.0" encoding="UTF-8"?>\n<DR_Label>\n  <name>txinr.bad</name>\n</DR_Label>\n',
                encoding="utf-8",
            )
            tbl_file = tbl_dir / "txinr110.tbl"
            tbl_file.write_text(
                '<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Table><name>txinr110</name><descriptionReference>txinr.missing</descriptionReference><Column><name>item</name><datatype><nativeDatatype>6</nativeDatatype></datatype></Column><Index><IndexColumn><name>item</name></IndexColumn></Index></DR_Table>',
                encoding="utf-8",
            )

            report = validate_activity(act_dir, strict=False, fix=False)
            self.assertTrue(any("single-line" in d.message.lower() or "whitespace" in d.message.lower() for d in report.errors))

            # --fix compacts writable bad_lbl and creates single-line missing label with LabelVariant
            validate_activity(act_dir, strict=False, fix=True)
            fixed_bad = bad_lbl.read_text(encoding="utf-8")
            self.assertFalse(_has_newline_outside_script(fixed_bad))
            created_lbl = (lbl_dir / "txinr.missing.lbl").read_text(encoding="utf-8")
            self.assertTrue(created_lbl.startswith('<?xml version="1.0" encoding="UTF-8" standalone="no"?>'))
            self.assertIn("<LabelVariant>", created_lbl)
            self.assertFalse(_has_newline_outside_script(created_lbl))

    def test_session_field_label_prefix_stripping_and_command_full_name(self):
        from generate_ln_session import generate_session_xml
        ses = {
            "code": "txinr1110m000",
            "description": "Gov Licenses",
            "table": "txinr110",
            "form_commands": [
                {"name": "export.csv", "description": "Export CSV", "label_code": "txinr.export.csv"}
            ],
        }
        tbl = {
            "code": "txinr110",
            "description": "Gov Licenses",
            "fields": [
                {"name": "dsca", "label_code": "txinr.dsca", "description": "Desc"},
                {"name": "cwar", "label_code": "txwh.cwar", "description": "Warehouse"},
                {"name": "item", "label_code": "tcibd001.item", "description": "Item"},
                {"name": "btno", "label_code": "txtxcmg012.btno", "description": "Batch"},
            ],
        }
        xml = generate_session_xml(ses, tbl, application="EXTce01108")
        self.assertIn("<fieldLabel>inr.dsca</fieldLabel>", xml)
        self.assertIn("<fieldLabel>wh.cwar</fieldLabel>", xml)
        self.assertIn("<fieldLabel>tcibd001.item</fieldLabel>", xml)
        self.assertIn("<fieldLabel>txcmg012.btno</fieldLabel>", xml)
        self.assertIn("<descriptionReference>txinr.export.csv</descriptionReference>", xml)

    def test_session_cross_package_probing_reuses_skips_locked_and_generates_missing(self):
        with tempfile.TemporaryDirectory() as td:
            act_dir = Path(td) / "dev_test [EXTce01108]"
            (act_dir / "tx" / "label").mkdir(parents=True, exist_ok=True)
            (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
            init_admin_file(act_dir / ".admin")

            # Mock server browse returning existing txaddress, locked txinr.addr, and tcibd001.item
            def fake_probe(package: str):
                if package == "tx":
                    return [
                        {"name": "txaddress", "locked": False},
                        {"name": "txinr.addr", "locked": True, "lockActivity": "other_act"},
                    ]
                if package == "tc":
                    return [{"name": "tcibd001.item", "locked": False}]
                return []

            spec = {
                "application": "EXTce01108",
                "version_id": "B61O_a_ext",
                "table": {
                    "code": "txinr110",
                    "description": "Gov Licenses",
                    "fields": [
                        {"name": "addr", "label_code": "txinr.addr", "description": "Address Lock"},
                        {"name": "adr2", "label_code": "txaddress", "description": "Address"},
                        {"name": "clot", "label_code": "wh.clot", "description": "Lot"},
                        {"name": "item", "label_code": "tcibd001.item", "description": "Item"},
                    ],
                },
                "session": {
                    "code": "txinr1110m000",
                    "description": "Gov Licenses",
                    "table": "txinr110",
                },
            }
            files = generate_session(schema_file=spec, activity_path=str(act_dir), probe_labels_fn=fake_probe)
            names = {f["name"] for f in files}
            # txwh.clot auto-generated; txaddress (exists on server), tcibd001.item (in tc), txinr.addr (locked) skipped
            self.assertIn("txwh.clot", names)
            self.assertNotIn("txaddress", names)
            self.assertNotIn("tcibd001.item", names)
            self.assertNotIn("txinr.addr", names)
            self.assertTrue((act_dir / "tx" / "label" / "txwh.clot.lbl").exists())

    def test_validator_layer3_uses_reference_labels_and_pkg_prefix_lookup(self):
        with tempfile.TemporaryDirectory() as td:
            ws_dir = Path(td)
            ref_lbl_dir = ws_dir / ".reference" / "label"
            ref_lbl_dir.mkdir(parents=True, exist_ok=True)
            (ref_lbl_dir / "txwh.cwar.lbl").write_text(
                generate_label_xml("txwh.cwar", "Warehouse", "B61O_a_ext", "EXTce01108", context=1),
                encoding="utf-8",
            )

            act_dir = ws_dir / "dev_test [EXTce01108]"
            ses_dir = act_dir / "tx" / "session" / "inr"
            lbl_dir = act_dir / "tx" / "label"
            ses_dir.mkdir(parents=True, exist_ok=True)
            lbl_dir.mkdir(parents=True, exist_ok=True)
            (act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
            init_admin_file(act_dir / ".admin")
            (lbl_dir / "txinr1110m000.lbl").write_text(
                generate_label_xml("txinr1110m000", "Session", "B61O_a_ext", "EXTce01108", context=2),
                encoding="utf-8",
            )
            (lbl_dir / "txinr.dsca.lbl").write_text(
                generate_label_xml("txinr.dsca", "Desc", "B61O_a_ext", "EXTce01108", context=1),
                encoding="utf-8",
            )
            ses_xml = (
                '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
                '<DR_Controller><name>txinr1110m000</name><descriptionReference>txinr1110m000</descriptionReference>'
                '<Form><PhysicalFormLayout>'
                '<FormField><fieldName>txinr110.dsca</fieldName><fieldLabel>inr.dsca</fieldLabel></FormField>'
                '<FormField><fieldName>wh.cwar</fieldName><fieldLabel>wh.cwar</fieldLabel></FormField>'
                '<FormField><fieldName>txinr110.miss</fieldName><fieldLabel>inr.missing</fieldLabel></FormField>'
                '</PhysicalFormLayout></Form></DR_Controller>'
            )
            (ses_dir / "txinr1110m000.ses").write_text(ses_xml, encoding="utf-8")

            report = validate_activity(act_dir, strict=False, fix=False)
            l3_msgs = [d.message for d in report.errors if "[Layer 3]" in d.message]
            self.assertFalse(any("inr.dsca" in m or "txinr.dsca" in m for m in l3_msgs), l3_msgs)
            self.assertFalse(any("wh.cwar" in m or "txwh.cwar" in m for m in l3_msgs), l3_msgs)
            self.assertTrue(any("txinr.missing" in m or "inr.missing" in m for m in l3_msgs), l3_msgs)

    def test_xml_escaping_and_cdata_closing_tag_preservation(self):
        from generate_ln_table import generate_label_xml, ensure_label_context_variant, compact_tde_xml, has_multiline_outside_script
        lbl = generate_label_xml("txinr.esc", "Sales & Purchase <USD>", "B61O_a_ext", "EXTdemo", context=1)
        self.assertIn("Sales &amp; Purchase &lt;USD&gt;", lbl)
        merged, changed = ensure_label_context_variant(lbl, 10, "Open & <Export>")
        self.assertTrue(changed)
        self.assertIn("Open &amp; &lt;Export&gt;", merged)
        self.assertIn("<context>10</context>", merged)

        table_with_cdata = (
            '\ufeff<?xml version="1.0" encoding="UTF-8"?>\n'
            '<DR_Table>\n'
            '  <name>txinr110</name>\n'
            '  <expression><![CDATA[string s = "</expression>"\n  s = "ok"]]></expression>\n'
            '</DR_Table>\n'
        )
        comp = compact_tde_xml(table_with_cdata)
        self.assertTrue(comp.startswith('<?xml version="1.0" encoding="UTF-8" standalone="no"?>'))
        self.assertIn('string s = "</expression>"\n  s = "ok"', comp)
        self.assertFalse(has_multiline_outside_script(comp))


if __name__ == "__main__":
    unittest.main()
