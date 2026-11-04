#!/usr/bin/env python3
"""
Unit tests for Ticket 03:
GitLab CI and Unified Checks Gateway (scripts/run_checks.py).
ADR 0014: Unified Checks Script and Pre-Commit Guardrail.
"""

import sys
import unittest
import tempfile
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CHECKS_SCRIPT = REPO_ROOT / "scripts" / "run_checks.py"
CI_FILE = REPO_ROOT / ".gitlab-ci.yml"


class TestUnifiedChecksAndCi(unittest.TestCase):
    def test_checks_script_exists(self):
        """Asserts scripts/run_checks.py exists."""
        self.assertTrue(CHECKS_SCRIPT.exists(), "scripts/run_checks.py must exist")

    def test_gitlab_ci_yaml_exists(self):
        """Asserts .gitlab-ci.yml exists and contains required stages."""
        self.assertTrue(CI_FILE.exists(), ".gitlab-ci.yml must exist")
        ci_text = CI_FILE.read_text(encoding="utf-8")
        self.assertIn("lint", ci_text)
        self.assertIn("test", ci_text)
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
        """Asserts sync_global_skill synchronizes skill files to target directory."""
        with tempfile.TemporaryDirectory() as td:
            target_skill_dir = Path(td) / "ln_studio_skill"
            sys.path.insert(0, str(REPO_ROOT / "scripts"))
            try:
                from run_checks import sync_global_skill
                res = sync_global_skill(target_dir=target_skill_dir)
                self.assertTrue(res)
                self.assertTrue(target_skill_dir.exists())
                self.assertTrue((target_skill_dir / "SKILL.md").exists())
                self.assertTrue((target_skill_dir / "tools" / "ln_component_builder.py").exists())
            finally:
                if str(REPO_ROOT / "scripts") in sys.path:
                    sys.path.remove(str(REPO_ROOT / "scripts"))


if __name__ == "__main__":
    unittest.main()
