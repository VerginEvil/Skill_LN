"""Tests for tools/validate_skill.py (standard library unittest only)."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validate_skill import check_catalog_links, check_index_tsv, check_page_links


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="val_"))
        self.skill = self.tmp / "erp-ln-progguide"
        _write(self.skill / "references/guide/progguide/functions_appl/appl.delete.md",
               "# appl.delete()\n\nSee [locks](application_locks_overview.md).\n")
        _write(self.skill / "references/guide/progguide/functions_appl/application_locks_overview.md",
               "# overview\n")
        _write(self.skill / "references/FUNCTION_INDEX.md",
               "# idx\n\n- **x** -> `references/guide/progguide/functions_appl/appl.delete.md`\n")
        _write(self.skill / "references/PUBLIC_INTERFACES_INDEX.md", "# idx\n")
        _write(self.skill / "index/INDEX.tsv",
               "references/guide/progguide/functions_appl/appl.delete.md\tappl.delete()\n"
               "references/guide/progguide/functions_appl/application_locks_overview.md\toverview\n")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_clean_tree_passes(self):
        self.assertEqual(check_index_tsv(self.skill), [])
        self.assertEqual(check_catalog_links(self.skill, "references/FUNCTION_INDEX.md"), [])
        checked, failures = check_page_links(self.skill)
        self.assertEqual(failures, [])
        self.assertGreaterEqual(checked, 2)

    def test_missing_index_entry_detected(self):
        with (self.skill / "index" / "INDEX.tsv").open("a", encoding="utf-8") as fh:
            fh.write("references/guide/progguide/functions_appl/nope.md\tnope\n")
        self.assertEqual(check_index_tsv(self.skill),
                         ["references/guide/progguide/functions_appl/nope.md"])

    def test_missing_files_reported_not_raised(self):
        import shutil
        shutil.rmtree(self.skill / "index")
        missing = check_index_tsv(self.skill)
        self.assertEqual(len(missing), 1)
        self.assertIn("unreadable", missing[0])
        broken = check_catalog_links(self.skill, "references/NOPE.md")
        self.assertEqual(len(broken), 1)
        self.assertIn("unreadable", broken[0])

    def test_broken_page_link_detected(self):
        _write(self.skill / "references/guide/progguide/functions_appl/broken.md",
               "# broken\n\nSee [ghost](ghost.md).\n")
        _checked, failures = check_page_links(self.skill)
        self.assertEqual(len(failures), 1)
        self.assertIn("broken.md -> ghost.md", failures[0])

    def test_external_links_ignored(self):
        _write(self.skill / "references/guide/progguide/functions_appl/ext.md",
               "# ext\n\nSee [web](https://example.com) and [mail](mailto:a@b.c).\n")
        _checked, failures = check_page_links(self.skill)
        self.assertEqual(failures, [])

    def test_link_like_syntax_ignored(self):
        _write(self.skill / "references/guide/progguide/functions_appl/keys.md",
               "# keys\n\nFormat: [Ctrl+][Shift+][Alt+](<single char>|F<nr>|<special key>).\n")
        _checked, failures = check_page_links(self.skill)
        self.assertEqual(failures, [])

    def test_cli_exit_code(self):
        proc = subprocess.run([sys.executable, "tools/validate_skill.py",
                               "--skill-dir", str(self.skill)],
                              capture_output=True, text=True, cwd=Path.cwd())
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("PASS", proc.stdout)


if __name__ == "__main__":
    unittest.main()
