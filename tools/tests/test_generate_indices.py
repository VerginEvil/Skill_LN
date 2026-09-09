"""Tests for tools/generate_indices.py (standard library unittest only)."""
import unittest
from pathlib import Path
import tempfile

from tools.generate_indices import (
    chapter_short_title,
    first_signature,
    generate_function_index,
    generate_index_tsv,
    generate_public_interfaces_index,
    group_name,
    is_function_page,
    page_title,
)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class HelperTests(unittest.TestCase):
    def test_page_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "x.md"
            p.write_text("# Hello()\n\nbody\n", encoding="utf-8")
            self.assertEqual(page_title(p), "Hello()")

    def test_page_title_fallback_stem(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "plain.md"
            p.write_text("no heading\n", encoding="utf-8")
            self.assertEqual(page_title(p), "plain")

    def test_page_title_verbatim(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "x.md"
            p.write_text("# Appendix B - StpCreatdll\n", encoding="utf-8")
            self.assertEqual(page_title(p), "Appendix B - StpCreatdll")

    def test_first_signature(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "x.md"
            p.write_text("# a.b()\n\n`function long a.b( string x )`\n", encoding="utf-8")
            self.assertEqual(first_signature(p), "function long a.b( string x )")

    def test_first_signature_skips_include(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "x.md"
            p.write_text("# c.d\n\n`#include <bic>`\n`function long c.d( long id )`\n",
                         encoding="utf-8")
            self.assertEqual(first_signature(p), "function long c.d( long id )")

    def test_first_signature_bnf_preview(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "and_sc.md"
            p.write_text("# AND boolean operator\n\n## Syntax\n```\n\n<and boolean operator>\n"
                         "    ::= Search condition AND Search condition\n```\n",
                         encoding="utf-8")
            self.assertEqual(first_signature(p),
                             "<and boolean operator> ::= Search condition AND Search condition")

    def test_first_signature_ignores_plain_fence(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "synopsis.md"
            p.write_text("# Base64 synopsis\n```\nlong\n```\n", encoding="utf-8")
            self.assertIsNone(first_signature(p))

    def test_first_signature_ignores_xml_example(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "api.md"
            p.write_text("# XML API\n```\n\n<?xml version=\"1.0\"?>\n<CMF>\n```\n",
                         encoding="utf-8")
            self.assertIsNone(first_signature(p))

    def test_is_function_page(self):
        from pathlib import PurePosixPath  # noqa
        skill = Path("/s")
        self.assertTrue(is_function_page(skill, "references/guide/progguide/functions_appl/a.md"))
        self.assertTrue(is_function_page(skill, "references/guide/progguide/report_scripts/functions_x.md"))
        self.assertFalse(is_function_page(skill, "references/guide/progguide/misc/a.md"))
        self.assertFalse(is_function_page(skill, "references/sql/progguide/functions_database_handling/a.md"))
        self.assertFalse(is_function_page(skill, "references/guide/progguide/documentation.md"))

    def test_group_name(self):
        self.assertEqual(group_name("references/guide/progguide/functions_appl/a.md"), "appl")
        self.assertEqual(group_name("references/guide/progguide/report_scripts/f.md"), "report_scripts")

    def test_chapter_short_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            sample = Path(tmp) / "X.md"
            sample.write_text("# X\n\n> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates\n",
                              encoding="utf-8")
            self.assertEqual(chapter_short_title("ch10_commissions_and_rebates", sample),
                             "Commissions And Rebates")
            self.assertEqual(chapter_short_title("ch99_x", None), "X")


class MiniTreeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="idx_"))
        self.skill = self.tmp / "erp-ln-progguide"
        _write(self.skill / "references/guide/progguide/functions_appl/appl.delete.md",
               "# appl.delete()\n\n## Syntax:\n`function long appl.delete( const string name )`\n")
        _write(self.skill / "references/guide/progguide/functions_appl/application_locks_overview.md",
               "# Application locks: overview\n\nbody\n")
        _write(self.skill / "references/guide/progguide/misc/predefined_variables.md",
               "# Predefined variables\n\nbody\n")
        _write(self.skill / "references/public_interfaces/ch03_common/Address.Create.md",
               "# Address.Create\n\n> Chapter: Chapter 3 Public Interfaces for Common\n")
        _write(self.skill / "references/public_interfaces/ch01_introduction.md", "# Introduction\n")
        _write(self.skill / "references/FUNCTION_INDEX.md", "stale\n")
        (self.skill / "index").mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_index_tsv_excludes_index_files(self):
        tsv, n = generate_index_tsv(self.skill)
        self.assertEqual(n, 5)
        self.assertNotIn("FUNCTION_INDEX", tsv)
        self.assertIn("references/guide/progguide/functions_appl/appl.delete.md\tappl.delete()", tsv)

    def test_function_index(self):
        md, total = generate_function_index(self.skill)
        self.assertEqual(total, 2)
        self.assertIn("2 functions. Grep this file", md)
        self.assertIn("## appl", md)
        self.assertIn("- **appl delete** | `function long appl.delete( const string name )`"
                      " -> `references/guide/progguide/functions_appl/appl.delete.md`", md)
        self.assertIn("- **application_locks_overview**  ->", md)
        self.assertNotIn("predefined_variables", md)

    def test_public_interfaces_index(self):
        md, total = generate_public_interfaces_index(self.skill, "25082026", 2361, "guide 25082026.pdf")
        self.assertEqual(total, 1)
        self.assertIn("**1 public interface functions**", md)
        self.assertIn("## Chapter 3: Common (1)", md)
        self.assertIn("- [Address.Create](references/public_interfaces/ch03_common/Address.Create.md)", md)
        self.assertIn("## Top-level files", md)


if __name__ == "__main__":
    unittest.main()
