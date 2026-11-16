#!/usr/bin/env python3
"""
Unit tests for Ticket 06:
Message (.msg), Question (.qst/.que), Function (.fnc/.fun) & Additional File (.add) Generators.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from generate_ln_message import generate_message_xml, generate_messages
from generate_ln_question import generate_question_xml, generate_questions
from generate_ln_function import generate_function_xml, generate_functions
from generate_ln_additional import generate_additional_xml, generate_additionals
from admin_sync import list_admin_components, init_admin_file, MANAGED_EXTENSIONS
from validate_ln_activity import validate_activity


class TestMsgQstFncAddGenerators(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_gen_06 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        init_admin_file(self.act_dir / ".admin")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_generate_message_xml(self):
        spec = {
            "code": "txcmg0001",
            "description": "Validation error for batch",
            "severity": "3",
            "text": "Batch cannot be processed without approval.",
        }
        xml = generate_message_xml(spec, application="EXTce01107")
        self.assertIn("<DR_Message", xml)
        self.assertIn("<name>txcmg0001</name>", xml)
        self.assertIn("<severity>3</severity>", xml)
        self.assertIn("<text>Batch cannot be processed without approval.</text>", xml)

        # File creation & admin sync
        files = generate_messages([spec], activity_dir=self.act_dir, application="EXTce01107")
        self.assertEqual(len(files), 1)
        self.assertTrue(Path(files[0]["path"]).exists())
        self.assertEqual(Path(files[0]["path"]).suffix, ".msg")

        # Verify .admin has .msg
        comps = list_admin_components(self.act_dir)
        self.assertTrue(any(".msg" in c["path"] for c in comps))

    def test_generate_question_xml_and_aliases(self):
        spec = {
            "code": "txcmg0002",
            "description": "Confirm batch posting",
            "severity": "2",
            "domain": "tcyesno",
            "default_answer": "yes",
            "text": "Do you want to post this billing batch?",
        }
        xml = generate_question_xml(spec, application="EXTce01107")
        self.assertIn("<DR_Question", xml)
        self.assertIn("<name>txcmg0002</name>", xml)
        self.assertIn("<domain>tcyesno</domain>", xml)
        self.assertIn("<defaultAnswer>yes</defaultAnswer>", xml)

        # File creation with canonical .qst
        files = generate_questions([spec], activity_dir=self.act_dir, application="EXTce01107", legacy_alias=False)
        self.assertEqual(len(files), 1)
        self.assertEqual(Path(files[0]["path"]).suffix, ".qst")

        # File creation with legacy .que
        spec_que = dict(spec)
        spec_que["code"] = "txcmg0003"
        files_que = generate_questions([spec_que], activity_dir=self.act_dir, application="EXTce01107", legacy_alias=True)
        self.assertEqual(len(files_que), 1)
        self.assertEqual(Path(files_que[0]["path"]).suffix, ".que")

        # Both extensions must be recognized in MANAGED_EXTENSIONS
        self.assertIn(".qst", MANAGED_EXTENSIONS)
        self.assertIn(".que", MANAGED_EXTENSIONS)

    def test_generate_function_xml_and_script_injection(self):
        spec = {
            "code": "txcmgf001",
            "description": "Calculate Batch Totals Function",
            "script": "function extern double calculate_totals(long batch_no) { return(100.0) }",
        }
        xml = generate_function_xml(spec, application="EXTce01107")
        self.assertIn("<DR_Module", xml)
        self.assertIn("<name>txcmgf001</name>", xml)
        self.assertIn("<type>function</type>", xml)
        self.assertIn("calculate_totals", xml)

        files = generate_functions([spec], activity_dir=self.act_dir, application="EXTce01107")
        self.assertEqual(len(files), 1)
        fnc_path = Path(files[0]["path"])
        self.assertTrue(fnc_path.exists())
        self.assertEqual(fnc_path.suffix, ".fnc")

        # Verify inject_ln_script works on .fnc
        from inject_ln_script import extract_file, inject_file
        extracted_script = self.act_dir / "functions" / "txcmgf001.4gl"
        extract_file(fnc_path, extracted_script)
        self.assertTrue(extracted_script.exists())
        self.assertIn("calculate_totals", extracted_script.read_text(encoding="utf-8"))

        # Modify and inject back
        new_script_text = "function extern double calculate_totals(long batch_no) { return(250.0) }"
        extracted_script.write_text(new_script_text, encoding="utf-8")
        inject_file(extracted_script, fnc_path)
        self.assertIn("250.0", fnc_path.read_text(encoding="utf-8"))

    def test_generate_additional_file_xml(self):
        spec = {
            "code": "txcmgcfg",
            "description": "Billing Batch Configuration JSON",
            "content": '{"tax_rate": 0.07, "auto_post": true}',
            "keyword1": "config",
            "keyword2": "batch",
        }
        xml = generate_additional_xml(spec, application="EXTce01107")
        self.assertIn("<DR_AdditionalFile", xml)
        self.assertIn("<name>txcmgcfg</name>", xml)
        self.assertIn("<keyword1>config</keyword1>", xml)
        self.assertIn("tax_rate", xml)

        files = generate_additionals([spec], activity_dir=self.act_dir, application="EXTce01107")
        self.assertEqual(len(files), 1)
        self.assertTrue(Path(files[0]["path"]).exists())
        self.assertEqual(Path(files[0]["path"]).suffix, ".add")

    def test_validation_layer_recognition(self):
        # Validate that an activity with .msg, .qst, .fnc, .add passes 4-layer validation
        val_report = validate_activity(self.act_dir, strict=False)
        self.assertEqual(len(val_report.errors), 0)


if __name__ == "__main__":
    unittest.main()
