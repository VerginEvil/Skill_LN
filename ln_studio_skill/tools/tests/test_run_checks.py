#!/usr/bin/env python3
"""
Unit tests for CI and Unified Checks Gateway (scripts/run_checks.py).
ADR 0014, ADR 0015 & ADR 0017: Quality Hardening, CI Guardrails, and Skill Markdown Lint Gate.
"""

import sys
import unittest
import tempfile
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CHECKS_SCRIPT = REPO_ROOT / "scripts" / "run_checks.py"
GITHUB_CI_FILE = REPO_ROOT / ".github" / "workflows" / "ci.yml"
GITLAB_CI_FILE = REPO_ROOT / ".gitlab-ci.yml"


class TestUnifiedChecksAndCi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scripts_dir = str(REPO_ROOT / "scripts")
        if cls.scripts_dir not in sys.path:
            sys.path.insert(0, cls.scripts_dir)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "scripts_dir") and cls.scripts_dir in sys.path:
            sys.path.remove(cls.scripts_dir)

    def test_checks_script_exists(self):
        """Asserts scripts/run_checks.py exists."""
        self.assertTrue(CHECKS_SCRIPT.exists(), "scripts/run_checks.py must exist")

    def test_ci_pipeline_exists(self):
        """Asserts CI pipeline exists and invokes scripts/run_checks.py."""
        ci_file = GITHUB_CI_FILE if GITHUB_CI_FILE.exists() else GITLAB_CI_FILE
        self.assertTrue(ci_file.exists(), "CI configuration must exist (.github/workflows/ci.yml or .gitlab-ci.yml)")
        ci_text = ci_file.read_text(encoding="utf-8")
        self.assertIn("python scripts/run_checks.py", ci_text)

    def test_install_hook(self):
        """Asserts --install-hook creates an executable pre-commit hook."""
        from run_checks import install_pre_commit_hook
        with tempfile.TemporaryDirectory() as td:
            fake_git = Path(td) / ".git"
            fake_git.mkdir(parents=True)
            hook_path = install_pre_commit_hook(git_dir=fake_git)
            self.assertTrue(hook_path.exists())
            hook_content = hook_path.read_text(encoding="utf-8")
            self.assertIn("run_checks.py", hook_content)

    def test_sync_global_skill(self):
        """Asserts --sync-skill synchronizes repository skill to destination directory."""
        from run_checks import sync_global_skill
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "ln_studio_skill"
            ok = sync_global_skill(target_dir=target)
            self.assertTrue(ok)
            self.assertTrue(target.exists())
            self.assertTrue((target / "SKILL.md").exists())
            self.assertTrue((target / "tools").exists())

    def test_dual_skill_sync_and_drift(self):
        """Asserts dual-skill synchronization and drift detection for both skills."""
        from run_checks import sync_global_skill, check_skill_drift
        with tempfile.TemporaryDirectory() as td:
            skills_root = Path(td)
            ok = sync_global_skill(target_dir=skills_root)
            self.assertTrue(ok)
            self.assertTrue((skills_root / "ln_studio_skill" / "SKILL.md").exists())
            self.assertTrue((skills_root / "erp-ln-progguide" / "SKILL.md").exists())

            # Drift check should be 0 immediately after sync
            drifted = check_skill_drift(target_dir=skills_root)
            self.assertEqual(len(drifted), 0, f"Expected 0 drifted files, got: {drifted}")

            # Mutate a file in erp-ln-progguide
            progguide_skill = skills_root / "erp-ln-progguide" / "SKILL.md"
            progguide_skill.write_text("drifted content", encoding="utf-8")
            drifted_after = check_skill_drift(target_dir=skills_root)
            self.assertGreaterEqual(len(drifted_after), 1)
            self.assertTrue(any("erp-ln-progguide" in d for d in drifted_after))

    def _create_mock_skill(self, root: Path, sname: str, content: str) -> Path:
        sdir = root / sname
        sdir.mkdir(parents=True, exist_ok=True)
        (sdir / "SKILL.md").write_text(content, encoding="utf-8")
        return sdir

    def test_check_skill_markdown_compliant(self):
        """Asserts check_skill_markdown passes on compliant skill files."""
        from run_checks import check_skill_markdown
        with tempfile.TemporaryDirectory() as td:
            fake_root = Path(td)
            for sname in ("ln_studio_skill", "erp-ln-progguide"):
                sdir = fake_root / sname
                (sdir / "references").mkdir(parents=True)
                ref_file = sdir / "references" / "REF.md"
                ref_file.write_text("# Reference\n", encoding="utf-8")
                content = (
                    "---\n"
                    f"name: {sname}\n"
                    "description: Valid description for testing.\n"
                    "---\n\n"
                    f"# {sname}\n\n"
                    "Check [ref](references/REF.md) and `references/REF.md`.\n"
                )
                (sdir / "SKILL.md").write_text(content, encoding="utf-8")

            ok = check_skill_markdown(repo_root=fake_root, max_lines=80)
            self.assertTrue(ok)

    def test_check_skill_markdown_line_budget_violation(self):
        """Asserts check_skill_markdown fails when SKILL.md exceeds max_lines."""
        from run_checks import check_skill_markdown
        with tempfile.TemporaryDirectory() as td:
            fake_root = Path(td)
            lines = ["---", "name: ln_studio_skill", "description: Valid.", "---"]
            lines.extend([f"Line {i}" for i in range(85)])
            self._create_mock_skill(fake_root, "ln_studio_skill", "\n".join(lines))
            self._create_mock_skill(fake_root, "erp-ln-progguide", "---\nname: erp-ln-progguide\ndescription: Valid.\n---\n# Title\n")

            ok = check_skill_markdown(repo_root=fake_root, max_lines=80)
            self.assertFalse(ok)

    def test_check_skill_markdown_missing_frontmatter(self):
        """Asserts check_skill_markdown fails when frontmatter is missing or missing name/description."""
        from run_checks import check_skill_markdown
        with tempfile.TemporaryDirectory() as td:
            fake_root = Path(td)
            self._create_mock_skill(fake_root, "ln_studio_skill", "# Title Without Frontmatter\n")
            self._create_mock_skill(fake_root, "erp-ln-progguide", "---\nname: erp-ln-progguide\ndescription: Valid.\n---\n# Title\n")

            ok = check_skill_markdown(repo_root=fake_root, max_lines=80)
            self.assertFalse(ok)

    def test_check_skill_markdown_broken_link(self):
        """Asserts check_skill_markdown fails when a markdown link or inline code path target is missing."""
        from run_checks import check_skill_markdown
        with tempfile.TemporaryDirectory() as td:
            fake_root = Path(td)
            content = (
                "---\n"
                "name: ln_studio_skill\n"
                "description: Valid.\n"
                "---\n\n"
                "# Title\n\n"
                "See [missing](references/NOT_FOUND.md).\n"
            )
            self._create_mock_skill(fake_root, "ln_studio_skill", content)
            self._create_mock_skill(fake_root, "erp-ln-progguide", "---\nname: erp-ln-progguide\ndescription: Valid.\n---\n# Title\n")

            ok = check_skill_markdown(repo_root=fake_root, max_lines=80)
            self.assertFalse(ok)

    def test_skill_lint_only_cli_flag(self):
        """Asserts --skill-lint-only flag is supported by scripts/run_checks.py."""
        proc = subprocess.run(
            [sys.executable, str(CHECKS_SCRIPT), "--help"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertIn("--skill-lint-only", proc.stdout)


if __name__ == "__main__":
    unittest.main()
