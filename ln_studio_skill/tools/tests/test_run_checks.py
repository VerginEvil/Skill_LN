#!/usr/bin/env python3
"""
Unit tests for CI and Unified Checks Gateway (scripts/run_checks.py).
ADR 0014 & ADR 0015: Quality Hardening, CI Guardrails, and GitHub Actions Automation.
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
        with tempfile.TemporaryDirectory() as td:
            fake_git = Path(td) / ".git"
            fake_git.mkdir(parents=True)
            # Run install hook with custom git dir
            sys.path.insert(0, str(REPO_ROOT / "scripts"))
            try:
                from run_checks import install_pre_commit_hook
                hook_path = install_pre_commit_hook(git_dir=fake_git)
                self.assertTrue(hook_path.exists())
                hook_content = hook_path.read_text(encoding="utf-8")
                self.assertIn("run_checks.py", hook_content)
            finally:
                if str(REPO_ROOT / "scripts") in sys.path:
                    sys.path.remove(str(REPO_ROOT / "scripts"))

    def test_sync_global_skill(self):
        """Asserts --sync-global synchronizes repository skill to destination directory."""
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "ln_studio_skill"
            sys.path.insert(0, str(REPO_ROOT / "scripts"))
            try:
                from run_checks import sync_global_skill
                ok = sync_global_skill(target_dir=target)
                self.assertTrue(ok)
                self.assertTrue(target.exists())
                self.assertTrue((target / "SKILL.md").exists())
                self.assertTrue((target / "tools").exists())
            finally:
                if str(REPO_ROOT / "scripts") in sys.path:
                    sys.path.remove(str(REPO_ROOT / "scripts"))


if __name__ == "__main__":
    unittest.main()
