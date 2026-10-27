#!/usr/bin/env python3
"""
Unit tests for Ticket 07:
Report (.rpt & .rptdsrc) Ecore Generator & Script Synchronizer.
"""

import os
import sys
import base64
import tempfile
import unittest
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from generate_ln_report import generate_report_xml, generate_reports
from admin_sync import list_admin_components, init_admin_file
from validate_ln_activity import validate_activity


class TestReportEcoreGenerator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_rpt_01 [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        init_admin_file(self.act_dir / ".admin")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_generate_report_xml_structure(self):
        spec = {
            "code": "txcmg04010100",
            "description": "Billing Batch Summary Report",
            "paper_width": 80,
            "input_fields": [
                {
                    "fieldname": "btno",
                    "domain": "tcmcs.long",
                    "is_table_field": False,
                    "sort_sequence": 1,
                    "sort_mode": 1,
                },
                {
                    "fieldname": "cdec",
                    "domain": "tcdsca",
                    "is_table_field": False,
                    "sort_sequence": 99,
                    "sort_mode": 1,
                },
            ],
            "layouts": [
                {
                    "type": 2,  # page_header
                    "rows": 2,
                    "columns": 80,
                    "specials": [
                        {"type": 8, "label": "tcgen.h.date", "row": 1, "col": 1, "len": 10},
                        {"type": 8, "label": "tcgen.page", "row": 1, "col": 65, "len": 10},
                    ],
                },
                {
                    "type": 4,  # detail
                    "rows": 2,
                    "columns": 80,
                    "output_fields": [
                        {"print_expression": "btno", "domain": "tcmcs.long", "row": 1, "col": 1, "len": 9},
                        {"print_expression": "cdec", "domain": "tcdsca", "row": 1, "col": 15, "len": 30},
                    ],
                },
            ],
        }

        xml = generate_report_xml(spec, application="EXTce01107")
        self.assertIn("<DR_Report", xml)
        self.assertIn("<name>txcmg04010100</name>", xml)
        self.assertIn("<type>report</type>", xml)
        self.assertIn("<fieldname>btno</fieldname>", xml)
        self.assertIn("<domain>tcmcs.long</domain>", xml)
        self.assertIn("<Layout>", xml)
        self.assertIn("<PhysicalReportLayout>", xml)
        self.assertIn("<ReportLayoutText>", xml)
        self.assertIn("<ReportOutputField>", xml)
        self.assertIn("<ReportSpecial>", xml)
        self.assertIn("<PageSetup>", xml)

    def test_generate_report_files_and_admin_sync(self):
        spec = {
            "code": "txcmg04010100",
            "description": "Billing Batch Summary Report",
            "script": "before.program:\n\t| Init report\ndetail.1:\n\tlayout.1()\n",
            "input_fields": [
                {"fieldname": "btno", "domain": "tcmcs.long"},
            ],
        }

        files = generate_reports([spec], activity_dir=self.act_dir, application="EXTce01107")
        self.assertTrue(len(files) >= 1)
        rpt_file = Path(files[0]["path"])
        self.assertTrue(rpt_file.exists())
        self.assertEqual(rpt_file.suffix, ".rpt")

        # Verify .admin tracks .rpt
        comps = list_admin_components(self.act_dir)
        self.assertTrue(any(".rpt" in c["path"] for c in comps))

    def test_report_script_synchronization_and_validation(self):
        # Create report with script
        spec = {
            "code": "txgre00010100",
            "description": "Inventory Report",
            "script": "before.program:\n\tset.transaction.readonly()\ndetail.1:\n\tprint.detail()\n",
            "input_fields": [{"fieldname": "item", "domain": "tcitem"}],
        }
        files = generate_reports([spec], activity_dir=self.act_dir, application="EXTce01107")
        rpt_path = Path(files[0]["path"])

        # Check script extraction
        from inject_ln_script import extract_file, inject_file
        script_out = self.act_dir / "reports" / "txgre00010100.4gl"
        extract_file(rpt_path, script_out)
        self.assertTrue(script_out.exists())
        self.assertIn("before.program:", script_out.read_text(encoding="utf-8"))

        # 4-layer activity validation must recognize reports
        val_report = validate_activity(self.act_dir, strict=False)
        self.assertEqual(len(val_report.errors), 0)

    def test_report_cli_builder_and_diagnostics(self):
        import subprocess
        # Test CLI report generator
        cmd = [
            sys.executable,
            str(SKILL_TOOLS / "ln_component_builder.py"),
            "report",
            "--code", "txcmg04010199",
            "--desc", "Test CLI Report",
            "--activity", str(self.act_dir),
            "--paper-width", "80",
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, msg=res.stderr)
        self.assertIn("[SUCCESS] Created report:", res.stdout)
        created_rpt = self.act_dir / "reports" / "txcmg04010199.rpt"
        self.assertTrue(created_rpt.exists())

        # Validate with ActivityValidator directly
        from validate_ln_activity import ActivityValidator
        validator = ActivityValidator(self.act_dir)
        report = validator.run()
        self.assertEqual(len(report.errors), 0)
        self.assertIn("txcmg04010199", validator.reports)


if __name__ == "__main__":
    unittest.main()
