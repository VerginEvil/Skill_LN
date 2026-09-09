"""Tests for tools/update_pipeline.py (standard library unittest only)."""
import tempfile
import unittest
from pathlib import Path

from tools.update_pipeline import detect_sources, expected_chm_outputs, prune_stale


class DetectSourcesTests(unittest.TestCase):
    def test_detects_chms_pdf_and_edition(self):
        with tempfile.TemporaryDirectory() as tmp:
            upd = Path(tmp)
            (upd / "progguide_2610_en.chm").touch()
            (upd / "progguide_2610_en_sql.chm").touch()
            (upd / "Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud) 25082026.pdf").touch()
            sources = detect_sources(upd)
            kinds = sorted(c["kind"] for c in sources["chms"])
            self.assertEqual(kinds, ["guide", "sql"])
            self.assertTrue(sources["pdf"].name.endswith("25082026.pdf"))
            self.assertEqual(sources["edition"], "25082026")

    def test_empty_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            sources = detect_sources(Path(tmp))
            self.assertEqual(sources["chms"], [])
            self.assertIsNone(sources["pdf"])

    def test_output_dir_aliases_skill_dir(self):
        import io
        from contextlib import redirect_stdout
        from tools.update_pipeline import main
        with tempfile.TemporaryDirectory() as tmp:
            upd = Path(tmp) / "upd"
            upd.mkdir()
            (upd / "progguide_2610_en.chm").touch()
            out = Path(tmp) / "out"
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc = main(["--update-dir", str(upd), "--output-dir", str(out),
                           "--skip-pdf", "--dry-run"])
            self.assertEqual(rc, 0)
            self.assertIn(str(out), buf.getvalue())


class PruneStaleTests(unittest.TestCase):
    def test_prunes_only_unexpected_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "src" / "progguide"
            (src / "functions_genai").mkdir(parents=True)
            (src / "functions_genai" / "a.htm").write_text("<html></html>", encoding="utf-8")
            dst = Path(tmp) / "dst"
            (dst / "functions_genai").mkdir(parents=True)
            keep = dst / "functions_genai" / "a.md"
            keep.write_text("# a\n", encoding="utf-8")
            stale = dst / "functions_genai" / "sub_query.md"
            stale.write_text("# stale\n", encoding="utf-8")
            expected = expected_chm_outputs(src, dst)
            self.assertIn(keep.resolve(), expected)
            deleted = prune_stale(dst, expected)
            self.assertEqual(deleted, [stale])
            self.assertTrue(keep.is_file())
            self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()
