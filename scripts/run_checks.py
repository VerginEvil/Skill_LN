#!/usr/bin/env python3
"""
scripts/run_checks.py
Unified checks gateway, skill markdown lint gate, and pre-commit guardrail for Skill_LN.
ADR 0014: Quality Hardening, CI Guardrails, and Layout Enforcement.
ADR 0017: Runtime Error Prevention, Audit Guardrails, and Skill Hardening.
ADR 0018: Lean Skill Architecture, Progressive Disclosure & Automated Skill Lint Gate.

Usage:
    python scripts/run_checks.py                  # Run all checks (syntax, layout, skill-lint, tests)
    python scripts/run_checks.py --syntax-only    # Run only syntax compilation check
    python scripts/run_checks.py --layout-only    # Run only layout validation
    python scripts/run_checks.py --skill-lint-only# Run only skill markdown lint gate (ADR 0018)
    python scripts/run_checks.py --install-hook   # Install .git/hooks/pre-commit
    python scripts/run_checks.py --sync-skill     # Synchronize verified skills to global config
"""

import os
import sys
import stat
import re
import argparse
import compileall
import subprocess
from pathlib import Path
from typing import Optional, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = REPO_ROOT / "ln_studio_skill" / "tools"
TESTS_DIR = TOOLS_DIR / "tests"
PROGGUIDE_DIR = REPO_ROOT / "erp-ln-progguide"
PROGGUIDE_SCRIPTS_DIR = PROGGUIDE_DIR / "scripts"
PROGGUIDE_TESTS_DIR = PROGGUIDE_DIR / "tests"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(PROGGUIDE_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(PROGGUIDE_SCRIPTS_DIR))

SKILL_CONFIGS = {
    "ln_studio_skill": ["SKILL.md", "tools", "templates", "references", "scripts"],
    "erp-ln-progguide": ["SKILL.md", "references", "index", "templates", "scripts", "tests"],
}


def check_syntax() -> bool:
    """Compiles all Python sources under ln_studio_skill/tools and erp-ln-progguide/scripts."""
    print("=== [1/4] Checking Python Syntax Compilation ===")
    ok1 = compileall.compile_dir(str(TOOLS_DIR), quiet=1, force=False)
    ok2 = True
    if PROGGUIDE_SCRIPTS_DIR.exists():
        ok2 = compileall.compile_dir(str(PROGGUIDE_SCRIPTS_DIR), quiet=1, force=False)
    if ok1 and ok2:
        print("[PASS] Python syntax clean across all tools and scripts.")
        return True
    else:
        print("[FAIL] Python syntax errors detected.")
        return False


def check_layout() -> bool:
    """Verifies that all activities on disk comply with Single-XML TDE layout (ADR 0012 & ADR 0014)."""
    print("\n=== [2/4] Checking Single-XML TDE Layout Compliance ===")
    try:
        from admin_sync import validate_activity_layout
    except ImportError as e:
        print(f"[FAIL] Could not import validate_activity_layout: {e}")
        return False

    errors: List[str] = []
    scanned = 0
    seen_dirs = set()
    for marker in (".project", ".admin"):
        for cand in REPO_ROOT.rglob(marker):
            act_dir = cand.parent.resolve()
            if ".git" in act_dir.parts or ".scratch" in act_dir.parts or act_dir in seen_dirs:
                continue
            seen_dirs.add(act_dir)
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


def _resolve_and_validate_path(
    skill_file: Path,
    raw_path: str,
    path_prefixes: Optional[Tuple[str, ...]] = None,
) -> Optional[str]:
    """Validates that a relative path string points to an existing file/directory on disk."""
    clean = raw_path.partition("#")[0].strip()
    if not clean or any(c in clean for c in "<>|*?"):
        return None
    if path_prefixes and not any(clean.startswith(prefix) for prefix in path_prefixes):
        return None
    target_path = (skill_file.parent / clean).resolve()
    if not target_path.exists():
        return clean
    return None


def check_skill_markdown(repo_root: Optional[Path] = None, max_lines: int = 80) -> bool:
    """Verifies YAML frontmatter, line limit (<= max_lines), and relative links in SKILL.md (ADR 0018)."""
    root = repo_root or REPO_ROOT
    print(f"\n=== [3/4] Checking Skill Markdown Lint Gate (ADR 0018, <= {max_lines} lines) ===")

    skill_names = ["ln_studio_skill", "erp-ln-progguide"]
    errors: List[str] = []
    link_re = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
    inline_code_re = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
    path_prefixes = ("references/", "scripts/", "tools/", "templates/", "index/", "../")

    for sname in skill_names:
        skill_dir = root / sname
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{sname}/SKILL.md does not exist.")
            continue

        try:
            content = skill_file.read_text(encoding="utf-8")
        except OSError as e:
            errors.append(f"{sname}/SKILL.md could not be read: {e}")
            continue

        lines = content.splitlines()
        line_count = len(lines)

        # 1. Frontmatter check
        if not lines or lines[0].strip() != "---":
            errors.append(f"{sname}/SKILL.md missing opening YAML frontmatter '---'.")
        else:
            closing_idx = -1
            for idx in range(1, len(lines)):
                if lines[idx].strip() == "---":
                    closing_idx = idx
                    break
            if closing_idx == -1:
                errors.append(f"{sname}/SKILL.md missing closing YAML frontmatter '---'.")
            else:
                fm_text = "\n".join(lines[1:closing_idx])
                has_name = bool(re.search(r"^name:\s*\S+", fm_text, re.MULTILINE))
                has_desc = bool(re.search(r"^description:\s*\S+", fm_text, re.MULTILINE))
                if not has_name:
                    errors.append(f"{sname}/SKILL.md frontmatter missing non-empty 'name'.")
                if not has_desc:
                    errors.append(f"{sname}/SKILL.md frontmatter missing non-empty 'description'.")

        # 2. Line budget check
        if line_count > max_lines:
            errors.append(f"{sname}/SKILL.md: {line_count} lines exceeds maximum budget of {max_lines} lines.")

        # 3. Relative path / link resolution
        for m in link_re.finditer(content):
            raw = m.group(2).strip()
            if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
                continue
            broken = _resolve_and_validate_path(skill_file, raw)
            if broken:
                errors.append(f"{sname}/SKILL.md: broken markdown link -> {broken}")

        content_no_fences = re.sub(r"```[\s\S]*?```", "", content)
        for m in inline_code_re.finditer(content_no_fences):
            code_text = m.group(1).strip()
            for token in code_text.split():
                t = token.strip("()[]'\",;:")
                broken = _resolve_and_validate_path(skill_file, t, path_prefixes=path_prefixes)
                if broken:
                    errors.append(f"{sname}/SKILL.md: broken inline path pointer -> {broken}")

    if errors:
        for err in errors:
            print(f"  [ERROR] {err}")
        print(f"[FAIL] Skill markdown lint failed with {len(errors)} violation(s).")
        return False

    print(f"[PASS] Skill markdown lint clean (ln_studio_skill, erp-ln-progguide <= {max_lines} lines).")
    return True


def run_unit_tests() -> bool:
    """Runs the full unittest suite across erp-ln-progguide and ln_studio_skill."""
    print("\n=== [4/4] Running Unit Test Suite ===")

    # Suite 1: erp-ln-progguide/tests (if exists)
    if PROGGUIDE_TESTS_DIR.exists():
        print("--- [4a/4] Running erp-ln-progguide Test Suite ---")
        cmd_prog = [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(PROGGUIDE_TESTS_DIR),
            "-p",
            "test_*.py",
        ]
        env_prog = os.environ.copy()
        env_prog["PYTHONPATH"] = str(PROGGUIDE_SCRIPTS_DIR)
        proc_prog = subprocess.run(cmd_prog, env=env_prog)
        if proc_prog.returncode != 0:
            print(f"[FAIL] erp-ln-progguide test suite failed with exit code {proc_prog.returncode}.")
            return False

    # Suite 2: ln_studio_skill/tools/tests
    print("\n--- [4b/4] Running ln_studio_skill Test Suite ---")
    cmd_studio = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        str(TESTS_DIR),
        "-p",
        "test_*.py",
    ]
    env_studio = os.environ.copy()
    env_studio["PYTHONPATH"] = str(TOOLS_DIR)
    proc_studio = subprocess.run(cmd_studio, env=env_studio)
    if proc_studio.returncode != 0:
        print(f"[FAIL] ln_studio_skill test suite failed with exit code {proc_studio.returncode}.")
        return False

    # Suite 3: Native Rust Workspace Tests (ADR 0021 & Ticket 15)
    rust_dir = REPO_ROOT / "rust"
    if rust_dir.exists():
        print("\n--- [4c/4] Running Native Rust Workspace Test Suite (cargo test --workspace) ---")
        cargo_bin = Path(os.environ.get("USERPROFILE", "")) / ".cargo" / "bin" / "cargo.exe"
        cargo_cmd = str(cargo_bin) if cargo_bin.exists() else "cargo"
        env_rust = os.environ.copy()
        if cargo_bin.parent.exists():
            env_rust["PATH"] = str(cargo_bin.parent) + os.pathsep + env_rust.get("PATH", "")
        proc_rust = subprocess.run(
            [cargo_cmd, "test", "--workspace"],
            cwd=str(rust_dir),
            env=env_rust,
        )
        if proc_rust.returncode != 0:
            print(f"[FAIL] Native Rust workspace test suite failed with exit code {proc_rust.returncode}.")
            return False

    print("[PASS] Full test suite across all skills passed cleanly.")
    return True


def _get_target_pairs(target_dir: Optional[Path]) -> List[Tuple[str, Path, Path, bool]]:
    """Resolves (skill_name, src_dir, dest_dir, include_prefix) pairs for drift & sync."""
    dest_base = target_dir or (Path.home() / ".gemini" / "config" / "skills")
    if target_dir and target_dir.name in SKILL_CONFIGS:
        return [(target_dir.name, REPO_ROOT / target_dir.name, target_dir, False)]
    return [
        (sname, REPO_ROOT / sname, dest_base / sname, True)
        for sname in SKILL_CONFIGS
    ]


def check_skill_drift(target_dir: Optional[Path] = None) -> List[str]:
    """Detects file drift between the repository skills and the global installed skills."""
    drifted: List[str] = []
    for sname, src, dest, include_prefix in _get_target_pairs(target_dir):
        if not dest.exists() or not src.exists():
            continue
        items_to_check = SKILL_CONFIGS.get(sname, ["SKILL.md", "references"])
        for item in items_to_check:
            s_base = src / item
            if not s_base.exists():
                continue
            if s_base.is_file():
                d_file = dest / item
                if not d_file.exists() or s_base.read_bytes() != d_file.read_bytes():
                    drifted.append(f"{sname}/{item}" if include_prefix else item)
            elif s_base.is_dir():
                for src_file in s_base.rglob("*"):
                    if not src_file.is_file() or "__pycache__" in src_file.parts or src_file.name.endswith(".pyc") or ".git" in src_file.parts:
                        continue
                    rel = src_file.relative_to(src).as_posix()
                    dest_file = dest / rel
                    if not dest_file.exists() or src_file.read_bytes() != dest_file.read_bytes():
                        drifted.append(f"{sname}/{rel}" if include_prefix else rel)
    return drifted


def sync_global_skill(target_dir: Optional[Path] = None) -> bool:
    """Synchronizes verified repository skill files to global skills directory."""
    import shutil
    for sname, src, dest, _ in _get_target_pairs(target_dir):
        if not src.exists():
            print(f"[FAIL] Source skill directory not found: {src}")
            return False
        dest.mkdir(parents=True, exist_ok=True)
        items_to_sync = SKILL_CONFIGS.get(sname, ["SKILL.md"])
        for item in items_to_sync:
            s_item = src / item
            d_item = dest / item
            if not s_item.exists():
                continue
            if s_item.is_file():
                shutil.copy2(s_item, d_item)
            elif s_item.is_dir():
                shutil.copytree(
                    s_item,
                    d_item,
                    dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git*")
                )
        print(f"[SUCCESS] Synchronized {sname} to: {dest}")

    return True


def install_pre_commit_hook(git_dir: Optional[Path] = None) -> Path:
    """Installs .git/hooks/pre-commit pointing to scripts/run_checks.py."""
    gdir = git_dir or (REPO_ROOT / ".git")
    hooks_dir = gdir / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    hook_file = hooks_dir / "pre-commit"

    script_content = (
        "#!/bin/sh\n"
        "# Skill_LN pre-commit guardrail (ADR 0014, ADR 0017 & ADR 0018)\n"
        "python scripts/run_checks.py\n"
        "exit $?\n"
    )
    hook_file.write_text(script_content, encoding="utf-8")

    try:
        current_mode = os.stat(hook_file).st_mode
        os.chmod(hook_file, current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except Exception:
        pass

    print(f"[SUCCESS] Installed pre-commit hook at: {hook_file}")
    return hook_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Skill_LN Unified Checks Gateway (ADR 0014, ADR 0017 & ADR 0018)")
    parser.add_argument("--install-hook", action="store_true", help="Install .git/hooks/pre-commit")
    parser.add_argument("--syntax-only", action="store_true", help="Run only syntax compilation")
    parser.add_argument("--layout-only", action="store_true", help="Run only layout validation")
    parser.add_argument("--skill-lint-only", action="store_true", help="Run only skill markdown lint gate (ADR 0018)")
    parser.add_argument("--skip-tests", action="store_true", help="Skip running unit tests")
    parser.add_argument("--sync-skill", action="store_true", help="Synchronize verified repository skill files to global skills directory")
    args = parser.parse_args()

    if args.install_hook:
        install_pre_commit_hook()
        return 0

    if args.syntax_only:
        return 0 if check_syntax() else 1

    if args.layout_only:
        return 0 if check_layout() else 1

    if args.skill_lint_only:
        return 0 if check_skill_markdown() else 1

    # Full checks sequence
    syntax_ok = check_syntax()
    layout_ok = check_layout()
    markdown_ok = check_skill_markdown()
    tests_ok = True
    if not args.skip_tests:
        tests_ok = run_unit_tests()

    if syntax_ok and layout_ok and markdown_ok and tests_ok:
        if args.sync_skill:
            sync_global_skill()
        else:
            drifted = check_skill_drift()
            if drifted:
                print(f"\n[NOTE] Detected {len(drifted)} drifted skill file(s) relative to global skill installation.")
                print("       Pass --sync-skill to synchronize repository skill changes to global directory.")
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
