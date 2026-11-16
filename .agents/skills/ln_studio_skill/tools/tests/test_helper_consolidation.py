#!/usr/bin/env python3
"""
Unit tests for Ticket 05:
SCM Helper Consolidation and admin_sync Disambiguation.
ADR 0014: Quality Hardening and Helper Consolidation.
"""

import sys
import unittest
from pathlib import Path

SKILL_TOOLS = Path(__file__).resolve().parent.parent
if str(SKILL_TOOLS) not in sys.path:
    sys.path.insert(0, str(SKILL_TOOLS))

from ln_scm_engine import resolve_activity_context_xml
from admin_sync import find_component_by_coords
import ln_code_intelligence
import ln_revision_diff


class TestHelperConsolidation(unittest.TestCase):
    def test_resolve_activity_context_xml_exported(self):
        """Asserts resolve_activity_context_xml works when activity_dir is None."""
        ctx, cp = resolve_activity_context_xml(None, "EXTce01107")
        self.assertIsNone(ctx)
        self.assertEqual(cp, "EXTce01107_dev")

    def test_code_intelligence_and_revision_diff_use_shared_helper(self):
        """Asserts both modules use the consolidated resolve_activity_context_xml."""
        self.assertEqual(ln_code_intelligence.resolve_activity_context_xml, resolve_activity_context_xml)
        self.assertEqual(ln_revision_diff.resolve_activity_context_xml, resolve_activity_context_xml)

    def test_find_component_by_coords_callable(self):
        """Asserts find_component_by_coords is exported and callable."""
        self.assertTrue(callable(find_component_by_coords))


if __name__ == "__main__":
    unittest.main()
