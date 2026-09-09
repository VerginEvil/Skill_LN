"""Tests for tools/convert_chm.py (standard library unittest only)."""
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.convert_chm import _clean_text, convert_html_string, rewrite_href

FIXTURES = Path(__file__).parent / "fixtures"


def _read_fixture(name: str) -> str:
    raw = (FIXTURES / name).read_bytes()
    for enc in ("utf-8", "windows-1252", "cp1252"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    raise AssertionError("cannot decode %s" % name)


class RewriteHrefTests(unittest.TestCase):
    def test_normalizes_chm_relative_link(self):
        src_root = Path("/r/progguide")
        src_file = src_root / "functions_genai" / "x.htm"
        dst_root = Path("/o/guide/progguide")
        dst_file = dst_root / "functions_genai" / "x.md"
        got = rewrite_href("../../progguide/tiv/tiv_overview.htm",
                           src_file, src_root, dst_file, dst_root)
        self.assertEqual(got, "../tiv/tiv_overview.md")

    def test_same_dir_link(self):
        src_root = Path("/r/progguide")
        src_file = src_root / "functions_genai" / "x.htm"
        dst_root = Path("/o/guide/progguide")
        dst_file = dst_root / "functions_genai" / "x.md"
        got = rewrite_href("overview_and_synopsis.htm",
                           src_file, src_root, dst_file, dst_root)
        self.assertEqual(got, "overview_and_synopsis.md")

    def test_anchor_preserved(self):
        src_root = Path("/r/progguide")
        src_file = src_root / "functions_database_handling" / "subquery.htm"
        dst_root = Path("/o/sql/progguide")
        dst_file = dst_root / "functions_database_handling" / "subquery.md"
        got = rewrite_href("../../progguide/functions_database_handling/sql_glossary.htm#OuterColumnReference",
                           src_file, src_root, dst_file, dst_root)
        self.assertEqual(got, "sql_glossary.md#OuterColumnReference")

    def test_outside_root_returns_none(self):
        src_root = Path("/r/progguide")
        src_file = src_root / "functions_genai" / "x.htm"
        dst_root = Path("/o/guide/progguide")
        dst_file = dst_root / "functions_genai" / "x.md"
        self.assertIsNone(rewrite_href("../../skin/General.css",
                                       src_file, src_root, dst_file, dst_root))

    def test_dangling_source_link_returns_none(self):
        import tempfile as _tf
        tmp = Path(_tf.mkdtemp(prefix="chmtest_"))
        try:
            src_root = tmp / "progguide"
            (src_root / "a").mkdir(parents=True)
            src_file = src_root / "a" / "x.htm"
            src_file.write_text("<html></html>", encoding="utf-8")
            dst_root = tmp / "out"
            dst_file = dst_root / "a" / "x.md"
            self.assertIsNone(rewrite_href("missing.htm",
                                           src_file, src_root, dst_file, dst_root))
            (src_root / "a" / "present.htm").write_text("<html></html>", encoding="utf-8")
            self.assertEqual(rewrite_href("present.htm",
                                          src_file, src_root, dst_file, dst_root),
                             "present.md")
        finally:
            import shutil as _sh
            _sh.rmtree(tmp, ignore_errors=True)

    def test_mailto_returns_none(self):
        src_root = Path("/r/progguide")
        src_file = src_root / "a" / "x.htm"
        dst_root = Path("/o")
        dst_file = dst_root / "a" / "x.md"
        self.assertIsNone(rewrite_href("mailto:documentation@infor.com",
                                       src_file, src_root, dst_file, dst_root))

    def test_format_chars_stripped(self):
        zwsp = chr(0x200B)
        shy = chr(0x200C)
        bom = chr(0xFEFF)
        self.assertEqual(_clean_text("a" + zwsp + "b" + shy + "c" + bom + "d"), "abcd")
        self.assertEqual(_clean_text("x" + zwsp + " y"), "x y")


class ConvertGenaiTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="chmtest_"))
        self.src_root = self.tmp / "progguide"
        (self.src_root / "functions_genai").mkdir(parents=True)
        (self.src_root / "tiv").mkdir(parents=True)
        (self.src_root / "misc").mkdir(parents=True)
        shutil.copy(FIXTURES / "genai.processing.start.htm",
                    self.src_root / "functions_genai" / "genai.processing.start.htm")
        for stub in ("tiv/tiv_overview.htm", "misc/managed_execution.htm",
                     "functions_genai/overview_and_synopsis.htm"):
            (self.src_root / stub).write_text("<html></html>", encoding="utf-8")
        self.dst_root = self.tmp / "out"
        self.src_file = self.src_root / "functions_genai" / "genai.processing.start.htm"
        self.dst_file = self.dst_root / "functions_genai" / "genai.processing.start.md"
        self.md = convert_html_string(_read_fixture("genai.processing.start.htm"),
                                      self.src_file, self.src_root,
                                      self.dst_file, self.dst_root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_title(self):
        self.assertTrue(self.md.startswith("# genai.processing.start()\n"))

    def test_syntax_single_code_span(self):
        self.assertIn("## Syntax:", self.md)
        self.assertIn("`function void genai.processing.start( )`", self.md)

    def test_description(self):
        self.assertIn("## Description", self.md)
        self.assertIn("GenAI processing will be started", self.md)

    def test_return_table(self):
        self.assertIn("## Return values", self.md)
        self.assertIn("| | |", self.md)
        self.assertIn("| 0 | Success. |", self.md)
        self.assertIn("Failure, session is not", self.md)

    def test_arguments_table_double_pads_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            src_root = Path(tmp) / "progguide"
            (src_root / "g").mkdir(parents=True)
            html = ("<html><body><div class=\"TopicTitle\">f()</div><div class=\"body\">"
                    "<div class=\"GeneralSection\"><div class=\"subSectionTitle\">Arguments</div>"
                    "<table border=\"0\" class=\"none\"><tbody>"
                    "<tr><td class=\"none\"><code>string</code></td>"
                    "<td class=\"none\"><code>data.in</code></td>"
                    "<td class=\"none\"><p class=\"Paragraph\">Some input.</p></td></tr>"
                    "</tbody></table></div></div></body></html>")
            md = convert_html_string(html, src_root / "g" / "f.htm", src_root,
                                     Path(tmp) / "o" / "g" / "f.md", Path(tmp) / "o")
            self.assertIn("| `string` | `data.in` |  Some input.  |", md)

    def test_context_links_normalized(self):
        self.assertIn("## Context", self.md)
        self.assertIn("[TIV](../tiv/tiv_overview.md)", self.md)
        self.assertIn("[managed execution](../misc/managed_execution.md)", self.md)
        self.assertIn("level 2590", self.md)

    def test_note_merged_as_notes_prefix(self):
        self.assertIn("Notes  This function should be called", self.md)
        self.assertNotIn("## Notes", self.md)

    def test_related_topics(self):
        self.assertIn("## Related topics", self.md)
        self.assertIn("[GenAI Functionality on Form](overview_and_synopsis.md)", self.md)

    def test_no_feedback_artifacts(self):
        self.assertNotIn("Feedback", self.md)
        self.assertNotIn("mailto:", self.md)
        self.assertNotIn("mail.gif", self.md)
        self.assertNotIn(".htm", self.md)


class ConvertBase64Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="chmtest_"))
        self.src_root = self.tmp / "progguide"
        (self.src_root / "functions_base64").mkdir(parents=True)
        (self.src_root / "3gl_features").mkdir(parents=True)
        shutil.copy(FIXTURES / "base64.encode.htm",
                    self.src_root / "functions_base64" / "base64.encode.htm")
        for stub in ("3gl_features/null_characters_in_strings.htm",
                     "3gl_features/data_types.htm",
                     "functions_base64/base64_overview.htm",
                     "functions_base64/base64_synopsis.htm"):
            (self.src_root / stub).write_text("<html></html>", encoding="utf-8")
        self.dst_root = self.tmp / "out"
        self.src_file = self.src_root / "functions_base64" / "base64.encode.htm"
        self.dst_file = self.dst_root / "functions_base64" / "base64.encode.md"
        self.md = convert_html_string(_read_fixture("base64.encode.htm"),
                                      self.src_file, self.src_root,
                                      self.dst_file, self.dst_root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_legacy_style_markers(self):
        self.assertTrue(self.md.startswith("# base64.encode()\n"))
        self.assertIn("`function long base64.encode( string data.in, ref string data.out )`", self.md)
        self.assertIn("## Arguments", self.md)
        self.assertIn("| | | |", self.md)
        self.assertIn("|---|---|---|", self.md)
        self.assertIn("`string`", self.md)
        self.assertIn("`data.in`", self.md)
        self.assertIn("[NULL-terminated](../3gl_features/null_characters_in_strings.md)", self.md)

    def test_context_code_block_preserved(self):
        self.assertIn("```", self.md)
        self.assertIn("bytesread = seq.read(", self.md)

    def test_no_htm_links_remain(self):
        self.assertNotIn(".htm", self.md)


class ConvertSubqueryTests(unittest.TestCase):
    def test_sql_topic(self):
        tmp = Path(tempfile.mkdtemp(prefix="chmtest_"))
        try:
            src_root = tmp / "progguide"
            (src_root / "functions_database_handling").mkdir(parents=True)
            src_file = src_root / "functions_database_handling" / "subquery.htm"
            for stub in ("functions_database_handling/select_statement.htm",
                         "functions_database_handling/baan_sql.htm",
                         "functions_database_handling/sql_glossary.htm"):
                (src_root / stub).write_text("<html></html>", encoding="utf-8")
            dst_root = tmp / "out"
            dst_file = dst_root / "functions_database_handling" / "subquery.md"
            md = convert_html_string(_read_fixture("subquery.htm"),
                                     src_file, src_root, dst_file, dst_root)
            self.assertTrue(md.startswith("# Subquery\n"))
            self.assertIn("## Syntax", md)
            self.assertNotIn("## Syntax:", md)
            self.assertIn("## Examples", md)
            self.assertIn("*Example 1*", md)
            self.assertIn("SELECT MAX( salary )", md)
            self.assertIn("[SELECT statement](select_statement.md)", md)
            self.assertIn("sql_glossary.md#CorrelatedSubquery", md)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
