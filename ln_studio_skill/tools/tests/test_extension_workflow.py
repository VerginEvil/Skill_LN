#!/usr/bin/env python3
"""
ln_studio_skill/tools/tests/test_extension_workflow.py
Comprehensive test suite for Infor LN Extension Modeler Boundary & Local Hook Workflow (ADR 0006).

Validates:
  1. SCM Guardrails & Extension Write Interception (Ticket 07)
  2. Extension Templates & Project Scaffolding CLI (Ticket 08)
  3. Studio Ingestion & Hook Extraction CLI (Ticket 09)
  4. Static Verification Engine for Extension Hooks & Cloud Governance (Ticket 10)
  5. Activity Validator [GET_ONLY_EXTENSION] Realignment (Ticket 11)
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

# Setup paths
_test_dir = Path(__file__).resolve().parent
_tools_dir = _test_dir.parent
_skill_root = _tools_dir.parent

if str(_tools_dir) not in sys.path:
    sys.path.insert(0, str(_tools_dir))

from scm_guardrails import (
    assert_file_writable, is_extension_component, ReadOnlyComponentError
)
from generate_ln_library import generate_libraries
from ln_extension_manager import (
    new_extension, import_extension, parse_extension_hooks, list_hooks,
    get_hook, copy_to_clipboard
)
from check_4gl_script import ScriptChecker, Diagnostic
from admin_sync import scan_and_sync_activity
from validate_ln_activity import ActivityValidator


class TestSCMGuardrailExtensionInterception(unittest.TestCase):
    """Ticket 07: Extension Modeler components are strictly Read-Only in LN Studio."""

    def test_is_extension_component_detection(self):
        self.assertTrue(is_extension_component(Path("txesswmd4300m0")))
        self.assertTrue(is_extension_component(Path("txestwhinh312.lib")))
        self.assertTrue(is_extension_component(Path("txesb0100.lib")))
        self.assertTrue(is_extension_component(Path("txesm0100.lib")))
        self.assertTrue(is_extension_component(Path("txesr0100.lib")))
        self.assertTrue(is_extension_component(Path("my_act/tx/library/est/txestwmd400m000.lib")))
        self.assertTrue(is_extension_component(Path("my_act/tx/library/ess/txesswmd4300m0.lib")))

        # Standard components should NOT be flagged as extensions
        self.assertFalse(is_extension_component(Path("my_act/tx/library/ibd/txibddllitem01.lib")))
        self.assertFalse(is_extension_component(Path("my_act/tx/table/txcmg011.tbl")))
        self.assertFalse(is_extension_component(Path("my_act/tx/session/txcmg0110m100.ses")))

    def test_assert_file_writable_blocks_extensions(self):
        ext_paths = [
            Path("txesswmd4300m0"),
            Path("txestwhinh312.lib"),
            Path("C:/ws/act/library/est/txestwmd400m000.lib"),
            Path("C:/ws/act/library/ess/txesswmd4300m0.lib"),
        ]
        for p in ext_paths:
            with self.assertRaises(ReadOnlyComponentError) as ctx:
                assert_file_writable(p)
            err_msg = str(ctx.exception)
            self.assertIn("Failure checking-out the component", err_msg)
            self.assertIn("Action on", err_msg)
            self.assertIn("Use session ttext1500m000", err_msg)

    def test_generate_libraries_disallows_extensions(self):
        schema = {
            "version_id": "B61O_a_ext",
            "application": "EXTce01105",
            "libraries": [
                {
                    "code": "txestwhwmd400",
                    "package": "tx",
                    "type": "table_extension",
                    "target": "whwmd400",
                }
            ]
        }
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(ReadOnlyComponentError) as ctx:
                generate_libraries(schema, output_dir=td)
            self.assertIn("Generation of 'table_extension' into LN Studio workspace is disallowed", str(ctx.exception))
            self.assertIn("new-extension", str(ctx.exception))


class TestExtensionScaffoldingAndImport(unittest.TestCase):
    """Tickets 08 & 09: Local Extension scaffolding and Studio 'Get' import."""

    def test_new_table_extension_scaffolding(self):
        with tempfile.TemporaryDirectory() as td:
            out_file = Path(td) / "whwmd400_ext.4gl"
            res = new_extension("table", "whwmd400", output_path=out_file, author="Tester")
            self.assertEqual(res, out_file)
            self.assertTrue(out_file.exists())

            content = out_file.read_text(encoding="utf-8")
            self.assertIn("Extension Script for Table whwmd400", content)
            self.assertIn('#context_on "declarations"', content)
            self.assertIn("table   twhwmd400", content)
            self.assertIn("#include <bic_dal2>", content)
            self.assertIn("#include <bic_tableext>", content)
            self.assertIn('#context_on "before.save.object"', content)
            self.assertIn("function extern long before.save.object(long mode)", content)
            self.assertIn('#context_on "after.save.object"', content)
            self.assertIn('#context_on "method.is.allowed"', content)

    def test_new_session_extension_scaffolding(self):
        with tempfile.TemporaryDirectory() as td:
            out_file = Path(td) / "whwmd4300m000_ext.4gl"
            res = new_extension("session", "whwmd4300m000", output_path=out_file, author="Tester")
            self.assertEqual(res, out_file)
            self.assertTrue(out_file.exists())

            content = out_file.read_text(encoding="utf-8")
            self.assertIn("Extension Script for Session whwmd4300m000", content)
            self.assertIn('#context_on "declarations"', content)
            self.assertIn("#include <bic_sessionext>", content)
            self.assertIn('#context_on "function.custom.action.is.enabled"', content)

    def test_import_extension_from_xml(self):
        sample_xml = """<?xml version="1.0" encoding="UTF-8"?>
<DR_Module>
  <name>txestwhwmd400</name>
  <Source>
    <sourceType>6</sourceType>
    <expression>| Test Extension
#context_on "declarations"
table twhwmd400
#include &lt;bic_dal2&gt;
#context_off

#context_on "before.save.object"
function extern long before.save.object(long mode)
{
\treturn(0);
}
#context_off
</expression>
  </Source>
</DR_Module>
"""
        with tempfile.TemporaryDirectory() as td:
            xml_path = Path(td) / "txestwhwmd400.lib"
            xml_path.write_text(sample_xml, encoding="utf-8")

            out_path = Path(td) / "imported_whwmd400_ext.4gl"
            res = import_extension(xml_path, output_path=out_path)

            self.assertEqual(res, out_path)
            content = out_path.read_text(encoding="utf-8")
            self.assertIn("#include <bic_dal2>", content)
            self.assertIn("table twhwmd400", content)
            self.assertIn("before.save.object", content)


class TestExtensionHooksExtraction(unittest.TestCase):
    """Ticket 09: Hook inspection, parsing, and clipboard export."""

    def setUp(self):
        self.sample_ext = """| Header
#context_on "declarations"
table twhwmd400
#include <bic_dal2>
#context_off

#context_on "functions"
function extern boolean validate_code()
{
    return(true)
}
#context_off

#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    return(0)
}
#context_off
"""

    def test_parse_and_list_hooks(self):
        hooks = parse_extension_hooks(self.sample_ext)
        self.assertEqual(len(hooks), 3)
        self.assertEqual(hooks[0].name, "declarations")
        self.assertEqual(hooks[1].name, "functions")
        self.assertEqual(hooks[2].name, "before.save.object")

    def test_get_hook_clean_code(self):
        hook = get_hook(self.sample_ext, "before.save.object")
        self.assertIsNotNone(hook)
        self.assertEqual(hook.name, "before.save.object")
        clean = hook.clean_code
        self.assertNotIn("#context_on", clean)
        self.assertNotIn("#context_off", clean)
        self.assertIn("function extern long before.save.object(long mode)", clean)

    def test_copy_to_clipboard(self):
        ok = copy_to_clipboard("test hook text")
        # Should succeed or fallback gracefully
        self.assertIsInstance(ok, bool)


class TestStaticVerificationExtensionRules(unittest.TestCase):
    """Ticket 10: Static Verification Engine for Extension Hooks."""

    def setUp(self):
        self.checker = ScriptChecker()

    def test_valid_table_extension_passes(self):
        script = """
#context_on "declarations"
table twhwmd400
#include <bic_dal2>
#include <bic_tableext>
#context_off

#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    return(0)
}
#context_off
"""
        diags = self.checker.check_script(script, file_path="extensions/table/whwmd400_ext.4gl")
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertEqual(len(errors), 0, f"Expected 0 errors, got: {[str(e) for e in errors]}")

    def test_nested_context_on_raises_error(self):
        script = """
#context_on "declarations"
table twhwmd400
#context_on "nested_block"
#context_off
#context_off
"""
        diags = self.checker.check_script(script, file_path="extensions/table/whwmd400_ext.4gl")
        errors = [d for d in diags if d.severity == "ERROR" and "Nested '#context_on'" in d.message]
        self.assertTrue(len(errors) > 0, "Expected nested #context_on error")

    def test_unclosed_context_on_raises_error(self):
        script = """
#context_on "declarations"
table twhwmd400
"""
        diags = self.checker.check_script(script, file_path="extensions/table/whwmd400_ext.4gl")
        errors = [d for d in diags if d.severity == "ERROR" and "Unclosed '#context_on" in d.message]
        self.assertTrue(len(errors) > 0, "Expected unclosed #context_on error")

    def test_prohibited_ui_in_table_extension_raises_error(self):
        script = """
#context_on "declarations"
table twhwmd400
#include <bic_dal2>
#context_off

#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    message("Cannot save")
    return(0)
}
#context_off
"""
        diags = self.checker.check_script(script, file_path="extensions/table/whwmd400_ext.4gl")
        errors = [d for d in diags if d.severity == "ERROR" and "prohibited in DAL scripts" in d.message]
        self.assertTrue(len(errors) > 0, "Expected prohibited UI message() error")

    def test_prohibited_transaction_in_table_extension_raises_error(self):
        script = """
#context_on "declarations"
table twhwmd400
#include <bic_dal2>
#context_off

#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    commit.transaction()
    return(0)
}
#context_off
"""
        diags = self.checker.check_script(script, file_path="extensions/table/whwmd400_ext.4gl")
        errors = [d for d in diags if d.severity == "ERROR" and "Transaction control" in d.message]
        self.assertTrue(len(errors) > 0, "Expected prohibited transaction control error")

    def test_invalid_hook_signature_raises_error(self):
        # before.save.object returning void instead of long
        script = """
#context_on "before.save.object"
function extern void before.save.object(long mode)
{
}
#context_off
"""
        diags = self.checker.check_script(script, file_path="extensions/table/whwmd400_ext.4gl")
        errors = [d for d in diags if d.severity == "ERROR" and "must return 'long'" in d.message]
        self.assertTrue(len(errors) > 0, "Expected return type error for before.save.object")

    def test_session_extension_allows_db_transaction_and_accepts_void_command_hook(self):
        script = """
#context_on "declarations"
#include <bic_sessionext>
#include <bic_dam>
#context_off

#context_on "functions"
function extern void perform_tx_update()
{
    db.retry.point()
    commit.transaction()
}
#context_off

#context_on "function.cust.action.before.command"
function extern void function.cust.action.before.command()
{
    perform_tx_update()
}
#context_off
"""
        diags = self.checker.check_script(script, file_path="extensions/session/whinh4131m000_ext.4gl")
        errors = [d for d in diags if d.severity == "ERROR"]
        self.assertEqual(len(errors), 0, f"Expected 0 errors for session extension with transactions and void command hook, got: {[str(e) for e in errors]}")

    def test_command_hook_with_return_value_and_boolean_signature_fails(self):
        # 1. Test returning boolean signature for before.command
        script_bool = """
#context_on "declarations"
#include <bic_sessionext>
#context_off

#context_on "function.cust.before.command"
function extern boolean function.cust.before.command()
{
    return(true)
}
#context_off
"""
        diags_bool = self.checker.check_script(script_bool, file_path="extensions/session/whinh4131m000_ext.4gl")
        sig_errors = [d for d in diags_bool if d.severity == "ERROR" and "must return 'void' or 'long'" in d.message]
        self.assertTrue(len(sig_errors) > 0, "Expected signature error for boolean before.command")

        # 2. Test void function returning a value expression (DAL003)
        script_void_ret = """
#context_on "declarations"
#include <bic_sessionext>
#context_off

#context_on "function.cust.before.command"
function extern void function.cust.before.command()
{
    return(true)
}
#context_off
"""
        diags_ret = self.checker.check_script(script_void_ret, file_path="extensions/session/whinh4131m000_ext.4gl")
        ret_errors = [d for d in diags_ret if d.severity == "ERROR" and "Void function" in d.message]
        self.assertTrue(len(ret_errors) > 0, "Expected DAL003 void return value error")

    def test_ext001_includes_outside_declarations_or_missing_bic_dam(self):
        # Include outside declarations
        script_outside = """
#include <bic_dam>
#context_on "declarations"
table twhwmd400
#context_off
"""
        diags_out = self.checker.check_script(script_outside, file_path="extensions/table/whwmd400_ext.4gl")
        ext001_out = [d for d in diags_out if d.severity == "ERROR" and "EXT001" in d.message]
        self.assertTrue(len(ext001_out) > 0, "Expected EXT001 error for include outside declarations")

        # Calling dal.* without <bic_dam> inside declarations
        script_missing = """
#context_on "declarations"
#include <bic_sessionext>
#context_off

#context_on "functions"
function extern void update_record()
{
    dal.change.object("whinh435")
}
#context_off
"""
        diags_missing = self.checker.check_script(script_missing, file_path="extensions/session/whinh4131m000_ext.4gl")
        ext001_missing = [d for d in diags_missing if d.severity == "ERROR" and "Missing '#include <bic_dam>'" in d.message]
        self.assertTrue(len(ext001_missing) > 0, "Expected EXT001 error for missing <bic_dam>")

    def test_ext002_hook_scope_mismatch(self):
        # Table extension declaring Form Command hook
        script_table = """
#context_on "declarations"
table twhwmd400
#include <bic_dal2>
#include <bic_tableext>
#context_off

#context_on "function.cust.before.command"
function extern void function.cust.before.command()
{
}
#context_off
"""
        diags_tbl = self.checker.check_script(script_table, file_path="extensions/table/whwmd400_ext.4gl")
        ext002_tbl = [d for d in diags_tbl if d.severity == "ERROR" and "EXT002" in d.message and "Form Command hook" in d.message]
        self.assertTrue(len(ext002_tbl) > 0, "Expected EXT002 error for Form Command hook in Table Extension")

        # Session extension declaring Table DAL hook
        script_ses = """
#context_on "declarations"
#include <bic_sessionext>
#context_off

#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    return(0)
}
#context_off
"""
        diags_ses = self.checker.check_script(script_ses, file_path="extensions/session/whinh4131m000_ext.4gl")
        ext002_ses = [d for d in diags_ses if d.severity == "ERROR" and "EXT002" in d.message and "Table DAL hook" in d.message]
        self.assertTrue(len(ext002_ses) > 0, "Expected EXT002 error for Table DAL hook in Session Extension")

    def test_ext001_standard_generated_declarations_includes_permitted(self):
        # Standard includes under | Additional generated declarations are permitted
        script_std = """
|*******************************************************************************
|* Extension Script for Table tdsls400
|*******************************************************************************

| Hook declarations
#context_on "declarations"
| Custom declarations
#context_off

| Additional generated declarations
table   ttdsls400
#include <bic_dal2>
#include <bic_tableext>

| Hook before.save.object
#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    dal.change.object("tdsls400")
    return(0)
}
#context_off

function extern long get.extension.point.version()
{
    return(3)
}
"""
        diags = self.checker.check_script(script_std, file_path="extensions/table/tdsls400_ext.4gl")
        ext001_errors = [d for d in diags if d.severity == "ERROR" and "EXT001" in d.message]
        self.assertEqual(len(ext001_errors), 0, f"Expected 0 EXT001 errors for standard generated declarations, got: {ext001_errors}")

    def test_ext001_custom_include_outside_declarations_fails(self):
        # Custom include under | Additional generated declarations must fail EXT001
        script_custom_inc = """
| Additional generated declarations
table   ttdsls400
#include <bic_dal2>
#include <otxslidll001>

#context_on "declarations"
#context_off

function extern long get.extension.point.version()
{
    return(3)
}
"""
        diags = self.checker.check_script(script_custom_inc, file_path="extensions/table/tdsls400_ext.4gl")
        ext001_errors = [d for d in diags if d.severity == "ERROR" and "EXT001" in d.message and "otxslidll001" in d.message]
        self.assertTrue(len(ext001_errors) > 0, "Expected EXT001 error for custom include outside declarations")

    def test_ext003_standard_framework_function_outside_context_protection(self):
        # 3a. Custom function outside context must trigger EXT003
        script_custom_fn = """
#context_on "declarations"
#include <bic_sessionext>
#context_off

function extern void my_unwrapped_helper()
{
}
"""
        diags_custom = self.checker.check_script(script_custom_fn, file_path="extensions/session/whinh4131m000_ext.4gl")
        ext003_custom = [d for d in diags_custom if d.severity == "ERROR" and "EXT003" in d.message and "my_unwrapped_helper" in d.message]
        self.assertTrue(len(ext003_custom) > 0, "Expected EXT003 error for custom function outside context")

        # 3b. Standard framework function improperly wrapped inside context must trigger EXT003
        script_wrapped_std = """
#context_on "functions"
function extern long get.extension.point.version()
{
    return(3)
}
#context_off
"""
        diags_wrapped = self.checker.check_script(script_wrapped_std, file_path="extensions/table/tdsls400_ext.4gl")
        ext003_wrapped = [d for d in diags_wrapped if d.severity == "ERROR" and "EXT003" in d.message and "get.extension.point.version" in d.message]
        self.assertTrue(len(ext003_wrapped) > 0, "Expected EXT003 error for standard framework function wrapped inside context")

        # 3c. Standard framework function with modified return type must trigger EXT003
        script_bad_sig = """
#context_on "declarations"
table ttdsls400
#context_off

function extern void get.extension.point.version()
{
}
"""
        diags_bad_sig = self.checker.check_script(script_bad_sig, file_path="extensions/table/tdsls400_ext.4gl")
        ext003_sig = [d for d in diags_bad_sig if d.severity == "ERROR" and "EXT003" in d.message and "get.extension.point.version" in d.message]
        self.assertTrue(len(ext003_sig) > 0, "Expected EXT003 error for modified return type on get.extension.point.version")

        # 3d. Removed/missing get.extension.point.version when | Additional generated declarations present triggers EXT003
        script_missing_std = """
| Additional generated declarations
table   ttdsls400
#include <bic_dal2>
#include <bic_tableext>

#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    return(0)
}
#context_off
"""
        diags_missing = self.checker.check_script(script_missing_std, file_path="extensions/table/tdsls400_ext.4gl")
        ext003_missing = [d for d in diags_missing if d.severity == "ERROR" and "EXT003" in d.message and "missing or was removed" in d.message]
        self.assertTrue(len(ext003_missing) > 0, "Expected EXT003 error for removed get.extension.point.version")

    def test_ext003_context_balance_and_declaration_boundaries(self):
        # Unclosed context block triggers EXT003
        script_unclosed = """
#context_on "declarations"
table ttdsls400
"""
        diags_unclosed = self.checker.check_script(script_unclosed, file_path="extensions/table/tdsls400_ext.4gl")
        ext003_unclosed = [d for d in diags_unclosed if d.severity == "ERROR" and "EXT003" in d.message and "Unclosed" in d.message]
        self.assertTrue(len(ext003_unclosed) > 0, "Expected EXT003 error for unclosed context directive")

        # Unmatched context_off triggers EXT003
        script_unmatched = """
#context_off
"""
        diags_unmatched = self.checker.check_script(script_unmatched, file_path="extensions/table/tdsls400_ext.4gl")
        ext003_unmatched = [d for d in diags_unmatched if d.severity == "ERROR" and "EXT003" in d.message and "Unmatched '#context_off'" in d.message]
        self.assertTrue(len(ext003_unmatched) > 0, "Expected EXT003 error for unmatched #context_off")

        # Custom variable declaration outside context triggers EXT003
        script_custom_decl = """
long my_custom_var

#context_on "declarations"
table ttdsls400
#context_off
"""
        diags_decl = self.checker.check_script(script_custom_decl, file_path="extensions/table/tdsls400_ext.4gl")
        ext003_decl = [d for d in diags_decl if d.severity == "ERROR" and "EXT003" in d.message and "Custom declaration" in d.message]
        self.assertTrue(len(ext003_decl) > 0, "Expected EXT003 error for custom declaration outside context")


class TestActivityValidatorExtensionRealignment(unittest.TestCase):
    """Ticket 11: Activity Validator treats tx* extensions as [GET_ONLY_EXTENSION]."""

    def test_validator_ignores_untracked_extension_in_activity(self):
        with tempfile.TemporaryDirectory() as td:
            act_path = Path(td)
            # Create minimal valid activity structure
            (act_path / ".admin").write_text("", encoding="utf-8")
            (act_path / ".project").write_text("<projectDescription/>", encoding="utf-8")

            # Place a read-only extension component inside activity
            est_dir = act_path / "tx" / "library" / "est"
            est_dir.mkdir(parents=True, exist_ok=True)
            est_file = est_dir / "txestwhwmd400.lib"
            est_file.write_text("<DR_Module><name>txestwhwmd400</name></DR_Module>", encoding="utf-8")

            validator = ActivityValidator(act_path, strict=True)
            report = validator.run()

            # The extension file must NOT trigger an untracked SCM error in Layer 1
            l1_errors = [d for d in report.errors if "[Layer 1]" in d.message and "txestwhwmd400" in d.message]
            self.assertEqual(len(l1_errors), 0, f"Expected 0 Layer 1 errors for extension, got: {l1_errors}")


if __name__ == "__main__":
    unittest.main()
