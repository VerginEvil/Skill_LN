#!/usr/bin/env python3
"""
Unit tests for Ticket 04:
Single-XML Layout Mechanical Guardrail and Admin Extension Alignment.
ADR 0014: Quality Hardening and Layout Enforcement.
"""

import sys
import unittest
import tempfile
from pathlib import Path
from unittest.mock import MagicMock

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from admin_sync import (
    MANAGED_EXTENSIONS,
    EXCLUDED_EXTENSIONS,
    init_admin_file,
    sync_admin_file,
    validate_activity_layout,
)
from ln_revision_diff import generate_report_on_server


class TestLayoutGuardrailAndAdminExtensions(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.act_dir = Path(self.temp_dir.name) / "task_layout [EXTce01107]"
        self.act_dir.mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".project").write_text("<projectDescription/>", encoding="utf-8")
        (self.act_dir / ".settings").mkdir(parents=True, exist_ok=True)
        (self.act_dir / ".settings" / "properties.index").write_text("", encoding="utf-8")
        init_admin_file(self.act_dir / ".admin")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_rptdsrc_extension_alignment(self):
        """Asserts .rptdsrc is excluded from managed extensions and added to excluded extensions."""
        self.assertNotIn(".rptdsrc", MANAGED_EXTENSIONS, ".rptdsrc must not be in MANAGED_EXTENSIONS")
        self.assertIn(".rptdsrc", EXCLUDED_EXTENSIONS, ".rptdsrc must be in EXCLUDED_EXTENSIONS per AdminSyncHelper.java")

    def test_generate_report_canonical_single_xml_layout(self):
        """Asserts generate_report_on_server places reports in canonical {pkg}/report/{mod}/{name}.rpt."""
        mock_client = MagicMock()
        mock_client.do_bde_call.return_value = "<DR_Report name=\"txcmg0110\"/>"

        res = generate_report_on_server(
            client=mock_client,
            report_name="txcmg0110",
            table_name="ttadv300",
            version_id="1",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
        )
        self.assertTrue(res["success"])
        expected_rpt = self.act_dir / "tx" / "report" / "cmg" / "txcmg0110.rpt"
        self.assertTrue(expected_rpt.exists(), f"Expected report file at canonical path {expected_rpt}")
        # Legacy plural directory must NOT exist
        legacy_dir = self.act_dir / "reports"
        self.assertFalse(legacy_dir.exists(), "Legacy plural directory 'reports/' must not be created")

        # Verify registration in .admin
        from admin_sync import list_admin_components
        admin_paths = [c["path"] for c in list_admin_components(self.act_dir)]
        self.assertIn("tx/report/cmg/txcmg0110.rpt", admin_paths)

    def test_validate_activity_layout_valid(self):
        """Asserts valid canonical layout passes validation with 0 errors."""
        canonical_file = self.act_dir / "tx" / "report" / "cmg" / "txcmg0110.rpt"
        canonical_file.parent.mkdir(parents=True, exist_ok=True)
        canonical_file.write_text("<DR_Report/>", encoding="utf-8")

        errors = validate_activity_layout(self.act_dir)
        self.assertEqual(errors, [])

    def test_validate_activity_layout_detects_legacy_plural_folders(self):
        """Asserts legacy plural folders (reports, tables, sessions) trigger hard validation errors."""
        bad_file = self.act_dir / "reports" / "txcmg0110.rpt"
        bad_file.parent.mkdir(parents=True, exist_ok=True)
        bad_file.write_text("<DR_Report/>", encoding="utf-8")

        errors = validate_activity_layout(self.act_dir)
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("reports" in e for e in errors))

    def test_sync_admin_file_raises_on_invalid_layout(self):
        """Asserts sync_admin_file raises ValueError if activity contains invalid layout."""
        bad_file = self.act_dir / "tables" / "txcmg001.tbl"
        bad_file.parent.mkdir(parents=True, exist_ok=True)
        bad_file.write_text("<table/>", encoding="utf-8")

        with self.assertRaises(ValueError) as ctx:
            sync_admin_file(self.act_dir)
        self.assertIn("Single-XML TDE layout violation", str(ctx.exception))


    def test_checkout_and_checkin_activity_raise_on_invalid_layout(self):
        """Asserts SCM engine batch checkout and checkin reject invalid layouts."""
        from ln_scm_engine import checkout_activity, checkin_activity
        bad_file = self.act_dir / "sessions" / "txcmg0110m000.ses"
        bad_file.parent.mkdir(parents=True, exist_ok=True)
        bad_file.write_text("<session/>", encoding="utf-8")

        mock_client = MagicMock()
        with self.assertRaises(ValueError) as ctx:
            checkout_activity(mock_client, self.act_dir, "EXTce01107")
        self.assertIn("Single-XML TDE layout violation", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx2:
            checkin_activity(mock_client, self.act_dir, "EXTce01107")
        self.assertIn("Single-XML TDE layout violation", str(ctx2.exception))

    def test_generate_report_short_name_fallback_to_gen(self):
        """Asserts report names with length under 6 fallback to mod 'gen'."""
        mock_client = MagicMock()
        mock_client.do_bde_call.return_value = '<DR_Report name="txcmg"/>'
        res = generate_report_on_server(
            client=mock_client,
            report_name="txcmg",
            table_name="ttadv300",
            version_id="1",
            activity_dir=self.act_dir,
            project_name="EXTce01107",
        )
        self.assertTrue(res["success"])
        expected_rpt = self.act_dir / "tx" / "report" / "gen" / "txcmg.rpt"
        self.assertTrue(expected_rpt.exists())


if __name__ == "__main__":
    unittest.main()
