#!/usr/bin/env python3
"""
Unit Test Suite for Standalone 4GL & DAL Audit Engine (`scripts/audit_4gl.py`).
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

# Add scripts directory to path
SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from audit_4gl import Auditor4GL


class TestAudit4GL(unittest.TestCase):
    def setUp(self):
        self.auditor = Auditor4GL(skill_dir=SKILL_ROOT, cloud_mode=False)
        self.cloud_auditor = Auditor4GL(skill_dir=SKILL_ROOT, cloud_mode=True)

    def test_valid_dal2_script(self):
        """Asserts 0 errors and 0 warnings on fully compliant DAL2 script."""
        script = """
#include <bic_dal>

function extern long before.save.object(long mode)
{
    if mode == DAL_NEW then
        dal.set.error.message("tcgen0001")
        return(DALHOOKERROR)
    endif
    return(0)
}

function extern void item.update(long i.mode)
{
}

function extern long item.check(long has_changed)
{
    return(0)
}
"""
        diags = self.auditor.audit_content(script, "tccom001.dal", mode="dal2")
        errors = [d for d in diags if d.severity == "ERROR"]
        warnings = [d for d in diags if d.severity == "WARNING"]
        self.assertEqual(len(errors), 0, f"Expected 0 errors, got: {[str(e) for e in errors]}")
        self.assertEqual(len(warnings), 0, f"Expected 0 warnings, got: {[str(w) for w in warnings]}")

    def test_dal_interactive_dialog_rejection(self):
        """Asserts DAL001 triggered when message() or ask.enum() is present in DAL2 script."""
        script = """
function extern long before.save.object(long mode)
{
    message("Validation failed")
    ask.enum("Do you want to proceed?", 1)
    return(0)
}
"""
        diags = self.auditor.audit_content(script, "tccom001.dal", mode="dal2")
        dal001_diags = [d for d in diags if d.code == "DAL001"]
        self.assertGreaterEqual(len(dal001_diags), 2)
        self.assertTrue(all("prohibited in DAL scripts" in d.message for d in dal001_diags))

    def test_dal_hook_signature_validation(self):
        """Asserts DAL002 triggered when .update lacks 'long i.mode' or .check lacks 'long has_changed'."""
        script = """
function extern void item.update()
{
}

function extern long item.check()
{
    return(0)
}
"""
        diags = self.auditor.audit_content(script, "tccom001.dal", mode="dal2")
        dal002_diags = [d for d in diags if d.code == "DAL002"]
        self.assertEqual(len(dal002_diags), 2)
        self.assertTrue(any("long i.mode" in d.message for d in dal002_diags))
        self.assertTrue(any("long has_changed" in d.message for d in dal002_diags))

    def test_cloud_untrusted_function(self):
        """Asserts CLD001 triggered in --cloud mode on untrusted function call."""
        script = """
#include <bic_cmf>

function void send_legacy_mail()
{
    cmf.create()
}
"""
        # In non-cloud mode, should not trigger CLD001
        diags_regular = self.auditor.audit_content(script, "myscript.cln", mode="general")
        self.assertFalse(any(d.code == "CLD001" for d in diags_regular))

        # In cloud mode, should trigger CLD001
        diags_cloud = self.cloud_auditor.audit_content(script, "myscript.cln", mode="general")
        cld001_diags = [d for d in diags_cloud if d.code == "CLD001"]
        self.assertGreaterEqual(len(cld001_diags), 1)
        self.assertTrue(any("untrusted" in d.message.lower() for d in cld001_diags))

    def test_missing_include_header(self):
        """Asserts INC001 triggered when calling Json function without #include <bic_json>."""
        script_missing = """
function void process_json()
{
    Json.getString(0, "status")
}
"""
        diags_missing = self.auditor.audit_content(script_missing, "myscript.cln", mode="general")
        inc001_diags = [d for d in diags_missing if d.code == "INC001"]
        self.assertGreaterEqual(len(inc001_diags), 1)
        self.assertTrue(any("bic_json" in d.message for d in inc001_diags))

        script_with_include = """
#include <bic_json>

function void process_json()
{
    Json.getString(0, "status")
}
"""
        diags_with = self.auditor.audit_content(script_with_include, "myscript.cln", mode="general")
        self.assertFalse(any(d.code == "INC001" for d in diags_with))

    def test_anti_pattern_double_equality(self):
        """Asserts CAV001 triggered on direct float equality 'val == 100.0'."""
        script = """
function void calculate(double amount)
{
    if amount == 100.0 then
    endif
}
"""
        diags = self.auditor.audit_content(script, "myscript.cln", mode="general")
        cav001_diags = [d for d in diags if d.code == "CAV001"]
        self.assertGreaterEqual(len(cav001_diags), 1)
        self.assertTrue(any("floating-point" in d.message.lower() for d in cav001_diags))

    def test_unbalanced_block_detection(self):
        """Asserts SYN001 triggered on unclosed select or if statements."""
        script_unclosed_select = """
function void query_data()
{
    select tcmcs001.*
    from tcmcs001
    selectdo
        | missing endselect
}
"""
        diags = self.auditor.audit_content(script_unclosed_select, "myscript.cln", mode="general")
        syn001_diags = [d for d in diags if d.code == "SYN001"]
        self.assertGreaterEqual(len(syn001_diags), 1)
        self.assertTrue(any("select" in d.message.lower() for d in syn001_diags))

        script_unclosed_if = """
function void check_cond(long flag)
{
    if flag then
        | missing endif
}
"""
        diags_if = self.auditor.audit_content(script_unclosed_if, "myscript.cln", mode="general")
        syn001_if = [d for d in diags_if if d.code == "SYN001"]
        self.assertGreaterEqual(len(syn001_if), 1)
        self.assertTrue(any("if" in d.message.lower() for d in syn001_if))

    def test_json_output_format(self):
        """Asserts schema compliance of CLI execution with --format json."""
        cli_script = SKILL_ROOT / "scripts" / "audit_4gl.py"
        test_file = SKILL_ROOT / "templates" / "DalTwo.dal"

        proc = subprocess.run(
            [sys.executable, str(cli_script), str(test_file), "--format", "json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(proc.returncode, 0)
        data = json.loads(proc.stdout)
        self.assertIn("summary", data)
        self.assertIn("diagnostics", data)
        self.assertEqual(data["summary"]["status"], "PASSED")
        self.assertIsInstance(data["diagnostics"], list)


if __name__ == "__main__":
    unittest.main()
