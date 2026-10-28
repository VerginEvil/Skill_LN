#!/usr/bin/env python3
"""
Unit Test Suite for Standalone 4GL & DAL Audit Engine (`scripts/audit_4gl.py`).
Covers Task 1:
- 1.1 Table Declaration Enforcement (TBL001)
- 1.2 Data Dictionary Schema Cache & Field/Domain Verification (TBL002 & DMN001) + --auto-fetch-dd
- 1.3 Lightweight Recursive Descent AST Parser (SYN001 & Call-Graph CAV003)
- Existing DAL/Cloud/Include/Caveat rules (DAL001-004, CLD001-002, INC001, CAV001)
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Add scripts directory to path
SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from audit_4gl import Auditor4GL, DataDictionaryCache


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
        diags_regular = self.auditor.audit_content(script, "myscript.cln", mode="general")
        self.assertFalse(any(d.code == "CLD001" for d in diags_regular))

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
declaration:
    table ttcibd001

function void query_data()
{
    select tcibd001.*
    from tcibd001
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

    # =========================================================================
    # Task 1.1: Table Declaration Enforcement (Rule TBL001)
    # =========================================================================
    def test_tbl001_undeclared_table_flagged_and_main_table_exempted(self):
        """Asserts TBL001 flags referenced tables missing 'table t<name>' while exempting main_table."""
        script = """
declaration:
    table ttcibd001

function extern long before.save.object(long mode)
{
    | tdsls400 is the main table of tdsls400.dal (exempted)
    if isspace(tdsls400.orno) then
        return(DALHOOKERROR)
    endif

    | tcibd001 is declared in declaration: (valid)
    select tcibd001.item
    from tcibd001
    where tcibd001._index1 = {:tdsls401.item}
    selectdo
    endselect

    return(0)
}
"""
        # tdsls400 is inferred from filename tdsls400.dal; tcibd001 is declared; tdsls401 is undeclared!
        diags = self.auditor.audit_content(script, "tdsls400.dal", mode="dal2")
        tbl001_diags = [d for d in diags if d.code == "TBL001"]
        self.assertEqual(len(tbl001_diags), 1)
        self.assertIn("tdsls401", tbl001_diags[0].message)
        self.assertIn("table ttdsls401", tbl001_diags[0].fix_suggestion)

        # Now test explicit --main-table exemption
        diags_explicit = self.auditor.audit_content(
            script, "custom_script.cln", mode="general", main_table="tdsls400"
        )
        tbl001_explicit = [d for d in diags_explicit if d.code == "TBL001"]
        self.assertEqual(len(tbl001_explicit), 1)
        self.assertIn("tdsls401", tbl001_explicit[0].message)

    # =========================================================================
    # Task 1.2: Data Dictionary Cache & Field/Domain Verification (TBL002 & DMN001)
    # =========================================================================
    def test_tbl002_and_dmn001_dd_cache_validation_and_auto_fetch(self):
        """Asserts TBL002 and DMN001 validate fields and domains against .ln_dd_cache.json and support auto-fetch."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / ".ln_dd_cache.json"
            dd_cache = DataDictionaryCache(cache_path=cache_path)
            dd_cache.update_table(
                "tdsls400",
                fields={
                    "orno": {"domain": "tcorno", "type": "string"},
                    "ofbp": {"domain": "tccom.bpid", "type": "string"},
                },
                indices={"1": ["orno"]},
            )
            dd_cache.update_domain("tcorno", datatype="string", length=9)
            dd_cache.save()

            auditor_with_dd = Auditor4GL(
                skill_dir=SKILL_ROOT,
                dd_cache=DataDictionaryCache(cache_path=cache_path),
            )

            script = """
declaration:
    table ttdsls400
    domain tcorno valid.orno
    domain tcfake.dmn bad.var

function void check_order()
{
    valid.orno = tdsls400.orno
    if isspace(tdsls400.hallucinated_field) then
    endif
}
"""
            diags = auditor_with_dd.audit_content(script, "test.cln", mode="general")
            tbl002 = [d for d in diags if d.code == "TBL002"]
            dmn001 = [d for d in diags if d.code == "DMN001"]

            # _index1 or valid fields ('orno') must NOT trigger TBL002; 'hallucinated_field' MUST trigger TBL002
            self.assertEqual(len(tbl002), 1)
            self.assertIn("tdsls400.hallucinated_field", tbl002[0].message)

            # 'tcorno' is in cache; 'tcfake.dmn' is NOT in cache -> triggers DMN001
            self.assertEqual(len(dmn001), 1)
            self.assertIn("tcfake.dmn", dmn001[0].message)

            # Test --auto-fetch-dd callback resolves missing domain/table dynamically
            fetched_items = []

            def mock_auto_fetch(comp_type: str, comp_name: str):
                fetched_items.append((comp_type, comp_name))
                if comp_type == "domain" and comp_name == "tcfake.dmn":
                    return '<DR_Domain name="tcfake.dmn"><nativeDatatype>6</nativeDatatype></DR_Domain>'
                return None

            auditor_autofetch = Auditor4GL(
                skill_dir=SKILL_ROOT,
                dd_cache=DataDictionaryCache(cache_path=cache_path),
                auto_fetch_dd=True,
                auto_fetch_callback=mock_auto_fetch,
            )
            diags_after = auditor_autofetch.audit_content(script, "test.cln", mode="general")
            self.assertIn(("domain", "tcfake.dmn"), fetched_items)
            dmn001_after = [d for d in diags_after if d.code == "DMN001"]
            self.assertEqual(len(dmn001_after), 0)

    # =========================================================================
    # Task 1.3: AST Parser (Macros, Multi-line SQL, Subqueries & Call-Graph CAV003)
    # =========================================================================
    def test_ast_parser_handles_define_macros_and_sql_subqueries(self):
        """Asserts AST parser handles #define macros, SQL subqueries (select ...), and 'for update'."""
        script = """
declaration:
    table ttdsls400
    table ttdsls401

#define OPEN_IF_VALID(x) \\
    if (x) > 0 then \\
        x = x + 1 \\
    endif

function void complex_query()
{
    long cnt
    cnt = 1
    OPEN_IF_VALID(cnt)

    select tdsls400.*
    from tdsls400 for update
    where tdsls400._index1 = {"SO0001"}
    and exists (
        select tdsls401.orno
        from tdsls401
        where tdsls401.orno = tdsls400.orno
    )
    selectdo
        for cnt = 1 to 5
        endfor
    selectempty
    selecteos
    endselect
}
"""
        diags = self.auditor.audit_content(script, "complex.cln", mode="general")
        syn001 = [d for d in diags if d.code == "SYN001"]
        self.assertEqual(len(syn001), 0, f"Expected 0 SYN001 errors, got: {[str(d) for d in syn001]}")

    def test_ast_call_graph_detects_direct_and_transitive_nested_transactions_cav003(self):
        """Asserts intra-file Call Graph catches helper functions with commit.transaction() called inside active tx."""
        script = """
declaration:
    table ttdsls400

function void deep_helper_commit()
{
    commit.transaction()
}

function void middle_helper()
{
    deep_helper_commit()
}

function void outer_batch_process()
{
    db.retry.point()
    select tdsls400.*
    from tdsls400 for update
    selectdo
        db.update(ttdsls400, db.retry)
        middle_helper()
    selectempty
    endselect
    commit.transaction()
}
"""
        diags = self.auditor.audit_content(script, "batch.cln", mode="general")
        cav003 = [d for d in diags if d.code == "CAV003"]
        self.assertGreaterEqual(len(cav003), 1)
        self.assertTrue(any("middle_helper" in d.message for d in cav003))

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
