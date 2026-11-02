#!/usr/bin/env python3
"""
scripts/run_checks.py
Unified checks gateway and pre-commit guardrail for Skill_LN.
ADR 0014: Quality Hardening, CI Guardrails, and Layout Enforcement.

Usage:
    python scripts/run_checks.py                 # Run all checks (syntax, layout, tests)
    python scripts/run_checks.py --syntax-only   # Run only syntax compilation check
    python scripts/run_checks.py --layout-only   # Run only layout validation
    python scripts/run_checks.py --install-hook  # Install .git/hooks/pre-commit
"""

import os
import sys
import stat
import argparse
import compileall
import subprocess
from pathlib import Path
from typing import Optional, List

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = REPO_ROOT / "ln_studio_skill" / "tools"
TESTS_DIR = TOOLS_DIR / "tests"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))


def check_syntax() -> bool:
    """Compiles all Python sources under ln_studio_skill/tools to verify syntax."""
    print("=== [1/3] Checking Python Syntax Compilation ===")
    ok = compileall.compile_dir(str(TOOLS_DIR), quiet=1, force=False)
    if ok:
        print("[PASS] Python syntax clean.")
    else:
        print("[FAIL] Python syntax errors detected in ln_studio_skill/tools.")
    return bool(ok)


def check_layout() -> bool:
    """Verifies that all activities on disk comply with Single-XML TDE layout (ADR 0012 & ADR 0014)."""
    print("\n=== [2/3] Checking Single-XML TDE Layout Compliance ===")
    try:
        from admin_sync import validate_activity_layout
    except ImportError as e:
        print(f"[FAIL] Could not import validate_activity_layout: {e}")
        return False

    errors: List[str] = []
    # Search for any activity directories containing .project or .admin
    scanned = 0
    for cand in REPO_ROOT.rglob(".project"):
        act_dir = cand.parent
        # Skip .git and hidden root directories
        if ".git" in act_dir.parts or ".scratch" in act_dir.parts:
            continue
        scanned += 1
        errs = validate_activity_layout(act_dir)
        errors.extend(errs)

    if errors:
        for err in errors:
            print(f"  [ERROR] {err}")
        print(f"[FAIL] Single-XML layout compliance failed with {len(errors)} violation(s).")
        return False

    print(f"[PASS] Single-XML layout compliance clean ({scanned} activity workspace(s) scanned).")
    return True


def run_unit_tests() -> bool:
    """Runs the full unittest suite across ln_studio_skill/tools/tests."""
    print("\n=== [3/3] Running Unit Test Suite ===")
    cmd = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        str(TESTS_DIR),
        "-p",
        "test_*.py",
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(TOOLS_DIR)
    proc = subprocess.run(cmd, env=env)
    if proc.returncode == 0:
        print("[PASS] Full test suite passed cleanly.")
        return True
    else:
        print(f"[FAIL] Unit test suite failed with exit code {proc.returncode}.")
        return False


def install_pre_commit_hook(git_dir: Optional[Path] = None) -> Path:
    """Installs .git/hooks/pre-commit pointing to scripts/run_checks.py."""
    gdir = git_dir or (REPO_ROOT / ".git")
    hooks_dir = gdir / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    hook_file = hooks_dir / "pre-commit"

    script_content = (
        "#!/bin/sh\n"
        "# Skill_LN pre-commit guardrail (ADR 0014)\n"
        "python scripts/run_checks.py\n"
        "exit $?\n"
    )
    hook_file.write_text(script_content, encoding="utf-8")

    # Make executable on Unix-like platforms
    try:
        current_mode = os.stat(hook_file).st_mode
        os.chmod(hook_file, current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except Exception:
        pass

    print(f"[SUCCESS] Installed pre-commit hook at: {hook_file}")
    return hook_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Skill_LN Unified Checks Gateway (ADR 0014)")
    parser.add_argument("--install-hook", action="store_true", help="Install .git/hooks/pre-commit")
    parser.add_argument("--syntax-only", action="store_true", help="Run only syntax compilation")
    parser.add_argument("--layout-only", action="store_true", help="Run only layout validation")
    parser.add_argument("--skip-tests", action="store_true", help="Skip running unit tests")
    args = parser.parse_args()

    if args.install_hook:
        install_pre_commit_hook()
        return 0

    if args.syntax_only:
        return 0 if check_syntax() else 1

    if args.layout_only:
        return 0 if check_layout() else 1

    # Full checks sequence
    syntax_ok = check_syntax()
    layout_ok = check_layout()
    tests_ok = True
    if not args.skip_tests:
        tests_ok = run_unit_tests()

    if syntax_ok and layout_ok and tests_ok:
        print("\n=======================================================")
        print(" [ALL CHECKS PASSED] Repository is ready for delivery! ")
        print("=======================================================")
        return 0
    else:
        print("\n=======================================================")
        print(" [CHECKS FAILED] Please resolve reported issues above! ")
        print("=======================================================")
        return 1


if __name__ == "__main__":
    sys.exit(main())
