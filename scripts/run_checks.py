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


def resolve_skill_dir(repo_root: Path, skill_name: str) -> Path:
    """Resolves canonical skill directory under .agents/skills/<name> (ADR 0022)."""
    return repo_root / ".agents" / "skills" / skill_name


STUDIO_DIR = resolve_skill_dir(REPO_ROOT, "ln_studio_skill")
TOOLS_DIR = STUDIO_DIR / "tools"
TESTS_DIR = TOOLS_DIR / "tests"
PROGGUIDE_DIR = resolve_skill_dir(REPO_ROOT, "erp-ln-progguide")
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


def _extract_frontmatter_info(
    lines: List[str], label: str
) -> Tuple[Optional[str], List[str]]:
    """Validates YAML frontmatter and extracts the description string."""
    errors: List[str] = []
    if not lines or lines[0].strip() != "---":
        return None, [f"{label} missing opening YAML frontmatter '---'."]

    closing_idx = next(
        (idx for idx in range(1, len(lines)) if lines[idx].strip() == "---"),
        -1,
    )
    if closing_idx == -1:
        return None, [f"{label} missing closing YAML frontmatter '---'."]

    fm_lines = lines[1:closing_idx]
    fm_text = "\n".join(fm_lines)
    if not re.search(r"^name:\s*\S+", fm_text, re.MULTILINE):
        errors.append(f"{label} frontmatter missing non-empty 'name'.")

    desc_text: Optional[str] = None
    for idx, line in enumerate(fm_lines):
        m = re.match(r"^description:\s*(.*)$", line)
        if not m:
            continue
        raw_val = m.group(1).strip()
        if raw_val in ("|", ">", "|-", ">-"):
            block: List[str] = []
            for sub in fm_lines[idx + 1:]:
                if sub and (sub[0].isspace()):
                    block.append(sub.strip())
                elif not sub.strip():
                    continue
                else:
                    break
            desc_text = " ".join(block).strip()
        else:
            if len(raw_val) >= 2 and raw_val[0] == raw_val[-1] and raw_val[0] in ('"', "'"):
                raw_val = raw_val[1:-1].strip()
            desc_text = raw_val
        break

    if not desc_text:
        errors.append(f"{label} frontmatter missing non-empty 'description'.")
    return desc_text, errors


def _validate_markdown_links(
    md_file: Path, display_label: str, link_re: re.Pattern
) -> List[str]:
    """Checks all relative markdown links inside a markdown file."""
    try:
        md_text = md_file.read_text(encoding="utf-8")
    except OSError:
        return []
    errors: List[str] = []
    for m in link_re.finditer(md_text):
        raw = m.group(2).strip()
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
            continue
        broken = _resolve_and_validate_path(md_file, raw)
        if broken:
            errors.append(f"{display_label}: broken markdown link -> {broken}")
    return errors


def _find_orphaned_top_level_refs(
    skill_file: Path, refs_dir: Path, link_re: re.Pattern, inline_code_re: re.Pattern
) -> List[str]:
    """Finds top-level references/*.md files unreachable from SKILL.md."""
    if not refs_dir.is_dir():
        return []
    top_refs = {p.resolve(): p for p in sorted(refs_dir.glob("*.md"))}
    if not top_refs:
        return []

    visited: set = set()
    queue: List[Path] = [skill_file.resolve()]
    while queue:
        cur = queue.pop(0)
        if cur in visited or not cur.is_file():
            continue
        visited.add(cur)
        try:
            text = cur.read_text(encoding="utf-8")
        except OSError:
            continue
        candidates = [m.group(2).strip() for m in link_re.finditer(text)]
        if cur == skill_file.resolve():
            no_fences = re.sub(r"```[\s\S]*?```", "", text)
            for m in inline_code_re.finditer(no_fences):
                for tok in m.group(1).split():
                    t = tok.strip("()[]'\",;:")
                    if t.startswith("references/"):
                        candidates.append(t)
        for raw in candidates:
            if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
                continue
            clean = raw.partition("#")[0].strip()
            if not clean or any(c in clean for c in "<>|*?"):
                continue
            resolved = (cur.parent / clean).resolve()
            if resolved in top_refs and resolved not in visited:
                queue.append(resolved)

    return [
        f"ln_studio_skill/references/{p.name}: orphaned top-level reference (not linked from SKILL.md)"
        for resolved, p in top_refs.items()
        if resolved not in visited
    ]


def check_skill_markdown(
    repo_root: Optional[Path] = None,
    max_lines: int = 80,
    max_desc_words: int = 45,
    max_steering_lines: int = 60,
) -> bool:
    """Verifies frontmatter, word/line budgets, link integrity, and reference orphans (ADR 0018 & ADR 0025)."""
    root = repo_root or REPO_ROOT
    print(
        f"\n=== [3/4] Checking Skill & Rule Markdown Lint Gate "
        f"(SKILL <= {max_lines}L, desc <= {max_desc_words}w, steering/rules <= {max_steering_lines}L) ==="
    )

    skill_names = ["ln_studio_skill", "erp-ln-progguide"]
    errors: List[str] = []
    link_re = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
    inline_code_re = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
    path_prefixes = ("references/", "scripts/", "tools/", "templates/", "index/", "../")

    for sname in skill_names:
        skill_dir = resolve_skill_dir(root, sname)
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

        desc_text, fm_errors = _extract_frontmatter_info(lines, f"{sname}/SKILL.md")
        errors.extend(fm_errors)
        if desc_text:
            desc_words = len(desc_text.split())
            if desc_words > max_desc_words:
                errors.append(
                    f"{sname}/SKILL.md: description is {desc_words} words, exceeds budget of {max_desc_words} words."
                )

        if line_count > max_lines:
            errors.append(f"{sname}/SKILL.md: {line_count} lines exceeds maximum budget of {max_lines} lines.")

        targets = [skill_file]
        if sname == "ln_studio_skill":
            refs_dir = skill_dir / "references"
            if refs_dir.is_dir():
                targets.extend(sorted(refs_dir.glob("*.md")))
            errors.extend(_find_orphaned_top_level_refs(skill_file, refs_dir, link_re, inline_code_re))
        elif sname == "erp-ln-progguide":
            bp_dir = skill_dir / "references" / "best_practices"
            if bp_dir.is_dir():
                targets.extend(sorted(bp_dir.glob("*.md")))

        for md_file in targets:
            rel_label = f"{sname}/{md_file.relative_to(skill_dir).as_posix()}"
            errors.extend(_validate_markdown_links(md_file, rel_label, link_re))

        content_no_fences = re.sub(r"```[\s\S]*?```", "", content)
        for m in inline_code_re.finditer(content_no_fences):
            code_text = m.group(1).strip()
            for token in code_text.split():
                t = token.strip("()[]'\",;:")
                broken = _resolve_and_validate_path(skill_file, t, path_prefixes=path_prefixes)
                if broken:
                    errors.append(f"{sname}/SKILL.md: broken inline path pointer -> {broken}")

    # Steering & tracked rules line budgets + relative link validation (ADR 0025)
    steering_targets: List[Tuple[Path, str]] = []
    agents_md = root / "AGENTS.md"
    if agents_md.is_file():
        steering_targets.append((agents_md, "AGENTS.md"))
    rules_dir = root / ".agents" / "rules"
    if rules_dir.is_dir():
        for rule_file in sorted(rules_dir.glob("*.md")):
            if rule_file.name == "repos.local.md":
                continue
            steering_targets.append((rule_file, f".agents/rules/{rule_file.name}"))

    for md_path, label in steering_targets:
        try:
            md_lines = md_path.read_text(encoding="utf-8").splitlines()
        except OSError as e:
            errors.append(f"{label} could not be read: {e}")
            continue
        if len(md_lines) > max_steering_lines:
            errors.append(
                f"{label}: {len(md_lines)} lines exceeds maximum budget of {max_steering_lines} lines."
            )
        errors.extend(_validate_markdown_links(md_path, label, link_re))

    if errors:
        for err in errors:
            print(f"  [ERROR] {err}")
        print(f"[FAIL] Skill markdown lint failed with {len(errors)} violation(s).")
        return False

    print(
        f"[PASS] Skill & rule markdown lint clean "
        f"(skills <= {max_lines}L / {max_desc_words}w, steering/rules <= {max_steering_lines}L)."
    )
    return True


def check_hygiene(repo_root: Optional[Path] = None) -> bool:
    """Scans tracked code and skill/rule docs for local paths, internal URLs, and customer identifiers."""
    root = repo_root or REPO_ROOT
    print("\n=== [3b/5] Checking Tracked Hygiene & Leak Guardrail ===")

    proc = subprocess.run(
        ["git", "ls-files"],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print("[WARN] git ls-files unavailable; skipped hygiene scan.")
        return True

    # Collect private names dynamically from gitignored overlay if present (without hardcoding them in tracked files)
    private_tokens: List[str] = []
    local_overlay = root / ".agents" / "rules" / "repos.local.md"
    if local_overlay.is_file():
        overlay_text = local_overlay.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"`([A-Za-z0-9][A-Za-z0-9_-]*(?:_TST|_TRN|_REIN|-Customization|_Custimuzation))`", overlay_text):
            tok = m.group(1)
            if tok not in ("PRD_ENV", "DEV_ENV", "TRN_ENV", "ENV_WORKSPACE") and tok not in private_tokens:
                private_tokens.append(tok)

    patterns = [
        ("workstation_path", re.compile(r"(?i)(?:[a-z]:[/\\]{1,2}users[/\\]{1,2}(?!<)[a-z0-9._-]+|d:[/\\]{1,2}ln studio|/home/(?!<)[a-z0-9._-]+/)")),
        ("internal_ip_url", re.compile(r"https?://(?:192\.168|10\.\d+)\.\d+\.\d+")),
    ]
    if private_tokens:
        escaped = "|".join(re.escape(t) for t in private_tokens)
        patterns.append(("private_overlay_token", re.compile(rf"\b(?:{escaped})\b")))

    def _in_scope(rel_path: str) -> bool:
        if rel_path in ("scripts/run_checks.py", ".agents/rules/repos.example.md"):
            return False
        if rel_path.endswith(".md") and (
            rel_path in ("README.md", "AGENTS.md")
            or rel_path.startswith((".agents/rules/", ".agents/skills/ln_studio_skill/", ".agents/skills/erp-ln-progguide/"))
            and "/references/guide/" not in rel_path
            and "/references/public_interfaces/" not in rel_path
            and "/references/extensions/" not in rel_path
            and "/references/afs/" not in rel_path
            and "/references/best_practices/" not in rel_path
        ):
            return True
        if rel_path.startswith(".agents/skills/ln_studio_skill/tools/") and rel_path.endswith(".py") and "/tests/" not in rel_path:
            return True
        if rel_path.startswith("rust/") and "/src/" in rel_path and rel_path.endswith(".rs"):
            return True
        return False

    violations: List[str] = []
    scanned = 0
    for rel in proc.stdout.splitlines():
        if not _in_scope(rel):
            continue
        fp = root / rel
        if not fp.is_file():
            continue
        scanned += 1
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        for label, rx in patterns:
            m = rx.search(txt)
            if m:
                violations.append(f"{rel}: [{label}] matched {m.group(0)!r}")

    if violations:
        for v in violations:
            print(f"  [ERROR] {v}")
        print(f"[FAIL] Hygiene scan failed with {len(violations)} violation(s).")
        return False

    print(f"[PASS] Hygiene scan clean ({scanned} tracked file(s) scanned).")
    return True


def check_parity(repo_root: Optional[Path] = None) -> bool:
    """Verifies Python <-> Rust Stdio MCP tool parity and documentation alignment."""
    root = repo_root or REPO_ROOT
    print("\n=== [3c/5] Checking Python <-> Rust MCP & Doc Parity ===")
    errors: List[str] = []

    try:
        import ln_studio_mcp
        py_tools = {t["name"] for t in getattr(ln_studio_mcp, "TOOLS_REGISTRY", [])}
    except Exception as e:
        print(f"[FAIL] Could not import ln_studio_mcp.TOOLS_REGISTRY: {e}")
        return False

    tools_rs = root / "rust" / "bins" / "skill-ln" / "src" / "mcp" / "tools.rs"
    if not tools_rs.is_file():
        print(f"[FAIL] Missing Rust MCP registry: {tools_rs}")
        return False

    rs_text = tools_rs.read_text(encoding="utf-8")
    rs_tools = set(re.findall(r'"name":\s*"(ln_[a-z0-9_]+)"', rs_text))

    only_py = sorted(py_tools - rs_tools)
    only_rs = sorted(rs_tools - py_tools)
    if only_py:
        errors.append(f"MCP tools only in Python ln_studio_mcp.py: {only_py}")
    if only_rs:
        errors.append(f"MCP tools only in Rust tools.rs: {only_rs}")

    mcp_ref = root / ".agents" / "skills" / "ln_studio_skill" / "references" / "MCP_TOOLS_REFERENCE.md"
    if mcp_ref.is_file():
        ref_text = mcp_ref.read_text(encoding="utf-8")
        missing_in_ref = sorted(t for t in (py_tools & rs_tools) if f"`{t}`" not in ref_text)
        if missing_in_ref:
            errors.append(f"MCP_TOOLS_REFERENCE.md missing documented tool(s): {missing_in_ref}")

    if errors:
        for err in errors:
            print(f"  [ERROR] {err}")
        print(f"[FAIL] Python <-> Rust MCP parity check failed with {len(errors)} violation(s).")
        return False

    print(f"[PASS] Python <-> Rust MCP parity verified ({len(py_tools)} tools documented & registered).")
    return True


def detect_staged_scopes(repo_root: Optional[Path] = None) -> Tuple[bool, bool, bool]:
    """Determines which test suites need to run based on git staged files."""
    root = repo_root or REPO_ROOT
    proc = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return True, True, True

    staged = [line.strip().replace("\\", "/") for line in proc.stdout.splitlines() if line.strip()]
    if not staged:
        return False, False, False

    touches_checks = any(p == "scripts/run_checks.py" for p in staged)
    run_progguide = touches_checks or any(
        p.startswith(".agents/skills/erp-ln-progguide/") and p.endswith(".py")
        for p in staged
    )
    run_studio = touches_checks or any(
        p.startswith(".agents/skills/ln_studio_skill/") and p.endswith(".py")
        for p in staged
    )
    run_rust = any(p.startswith("rust/") for p in staged)
    return run_progguide, run_studio, run_rust


def run_unit_tests(
    run_progguide: bool = True,
    run_studio: bool = True,
    run_rust: bool = True,
) -> bool:
    """Runs the unittest and Rust workspace test suites across erp-ln-progguide, ln_studio_skill, and rust/."""
    print("\n=== [4/4] Running Unit Test Suite ===")

    # Suite 1: erp-ln-progguide/tests (if exists)
    if not run_progguide:
        print("--- [4a/4] Skipped erp-ln-progguide Test Suite (no staged Python changes) ---")
    elif PROGGUIDE_TESTS_DIR.exists():
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
    if not run_studio:
        print("\n--- [4b/4] Skipped ln_studio_skill Test Suite (no staged Python changes) ---")
    else:
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
    if not run_rust:
        print("\n--- [4c/4] Skipped Native Rust Workspace Test Suite (no staged rust/ changes) ---")
    elif rust_dir.exists():
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

        # Suite 4d: Anti-stub static source guard + skill-ln.exe smoke check
        print("\n--- [4d/4] Running Rust Anti-Stub & CLI Binary Smoke Check ---")
        forbidden_patterns = [
            "<DR_Message name=",
            "<DR_Question name=",
            "<DR_Function name=",
            "<DR_Additional name=",
            "<DR_Report name=",
            "http://localhost:8080/jca",
        ]
        for src_rel in ("rust/bins/skill-ln/src/commands.rs", "rust/bins/skill-ln/src/mcp/tools.rs"):
            src_path = REPO_ROOT / src_rel
            if src_path.exists():
                src_text = src_path.read_text(encoding="utf-8")
                for pat in forbidden_patterns:
                    if pat in src_text:
                        print(f"[FAIL] Forbidden stub pattern '{pat}' found in {src_rel}")
                        return False

        bin_candidates = [
            Path("C:/Temp/skill_ln_target/release/skill-ln.exe"),
            Path("C:/Temp/skill_ln_target/debug/skill-ln.exe"),
            rust_dir / "target" / "release" / "skill-ln.exe",
            rust_dir / "target" / "debug" / "skill-ln.exe",
        ]
        exe_path = next((p for p in bin_candidates if p.exists()), None)
        if exe_path is not None:
            for args in (["--version"], ["fn-search", "db.eq"]):
                p = subprocess.run([str(exe_path), *args], cwd=str(REPO_ROOT), capture_output=True, text=True)
                if p.returncode != 0:
                    print(f"[FAIL] {exe_path.name} {' '.join(args)} failed (rc={p.returncode}): {p.stderr}")
                    return False
        else:
            print("[WARN] skill-ln.exe binary not found in target dirs; skipped process smoke check.")

        # Check whether installed skill-ln on PATH is stale compared to Rust sources
        import shutil
        installed_bin = shutil.which("skill-ln")
        if installed_bin:
            installed_mtime = Path(installed_bin).stat().st_mtime
            newest_rs = max((p.stat().st_mtime for p in rust_dir.rglob("*.rs")), default=0.0)
            if newest_rs > installed_mtime:
                print(f"[WARN] Installed binary '{installed_bin}' is older than Rust source files.")
                print("       Run 'python scripts/run_checks.py --install-bin' (or copy target/release/skill-ln.exe) to refresh PATH.")

    print("[PASS] Full test suite across all skills passed cleanly.")
    return True


def _get_target_pairs(
    target_dir: Optional[Path],
    repo_root: Optional[Path] = None,
) -> List[Tuple[str, Path, Path, bool]]:
    """Resolves (skill_name, src_dir, dest_dir, include_prefix) pairs for drift & sync."""
    root = repo_root or REPO_ROOT
    dest_base = target_dir or (Path.home() / ".gemini" / "config" / "skills")
    if target_dir and target_dir.name in SKILL_CONFIGS:
        return [(target_dir.name, resolve_skill_dir(root, target_dir.name), target_dir, False)]
    return [
        (sname, resolve_skill_dir(root, sname), dest_base / sname, True)
        for sname in SKILL_CONFIGS
    ]


def _files_differ(src: Path, dst: Path) -> bool:
    """Fast file comparison using size + mtime_ns before falling back to byte comparison."""
    if not dst.exists():
        return True
    s_stat = src.stat()
    d_stat = dst.stat()
    if s_stat.st_size != d_stat.st_size:
        return True
    if s_stat.st_mtime_ns == d_stat.st_mtime_ns:
        return False
    return src.read_bytes() != dst.read_bytes()


def check_skill_drift(
    target_dir: Optional[Path] = None,
    repo_root: Optional[Path] = None,
) -> List[str]:
    """Detects file drift between the repository skills and the global installed skills."""
    drifted: List[str] = []
    for sname, src, dest, include_prefix in _get_target_pairs(target_dir, repo_root=repo_root):
        if not dest.exists() or not src.exists():
            continue
        items_to_check = SKILL_CONFIGS.get(sname, ["SKILL.md", "references"])
        for item in items_to_check:
            s_base = src / item
            if not s_base.exists():
                continue
            if s_base.is_file():
                d_file = dest / item
                if _files_differ(s_base, d_file):
                    drifted.append(f"{sname}/{item}" if include_prefix else item)
            elif s_base.is_dir():
                for src_file in s_base.rglob("*"):
                    if not src_file.is_file() or "__pycache__" in src_file.parts or src_file.name.endswith(".pyc") or ".git" in src_file.parts:
                        continue
                    rel = src_file.relative_to(src).as_posix()
                    dest_file = dest / rel
                    if _files_differ(src_file, dest_file):
                        drifted.append(f"{sname}/{rel}" if include_prefix else rel)
    return drifted


def sync_global_skill(
    target_dir: Optional[Path] = None,
    repo_root: Optional[Path] = None,
) -> bool:
    """Synchronizes verified repository skill files to global skills directory."""
    import shutil
    for sname, src, dest, _ in _get_target_pairs(target_dir, repo_root=repo_root):
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
                if d_item.is_dir():
                    for existing in list(d_item.rglob("*")):
                        if existing.is_file() and "__pycache__" not in existing.parts and not existing.name.endswith(".pyc") and ".git" not in existing.parts:
                            rel_existing = existing.relative_to(d_item)
                            if not (s_item / rel_existing).is_file():
                                existing.unlink(missing_ok=True)
                shutil.copytree(
                    s_item,
                    d_item,
                    dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git*")
                )
        print(f"[SUCCESS] Synchronized {sname} to: {dest}")

    return True


def install_pre_commit_hook(git_dir: Optional[Path] = None) -> Path:
    """Installs .git/hooks/pre-commit pointing to scripts/run_checks.py --pre-commit."""
    gdir = git_dir or (REPO_ROOT / ".git")
    hooks_dir = gdir / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    hook_file = hooks_dir / "pre-commit"

    script_content = (
        "#!/bin/sh\n"
        "# Skill_LN pre-commit guardrail (ADR 0014, ADR 0017 & ADR 0018)\n"
        "python scripts/run_checks.py --pre-commit\n"
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
    parser.add_argument("--pre-commit", action="store_true", help="Fast pre-commit mode: always run static gates, run Python/Rust test suites only for staged scopes")
    parser.add_argument("--syntax-only", action="store_true", help="Run only syntax compilation")
    parser.add_argument("--layout-only", action="store_true", help="Run only layout validation")
    parser.add_argument("--skill-lint-only", action="store_true", help="Run only skill markdown lint gate (ADR 0018)")
    parser.add_argument("--skip-tests", action="store_true", help="Skip running unit tests")
    parser.add_argument("--sync-skill", action="store_true", help="Synchronize verified repository skill files to global skills directory")
    parser.add_argument("--install-bin", action="store_true", help="Build release skill-ln binary and install to ~/.cargo/bin/")
    args = parser.parse_args()

    if args.install_bin:
        import shutil
        rust_dir = REPO_ROOT / "rust"
        rc = subprocess.run(["cargo", "build", "--release", "--bin", "skill-ln"], cwd=str(rust_dir)).returncode
        if rc != 0:
            return rc
        rel_exe = Path("C:/Temp/skill_ln_target/release/skill-ln.exe")
        if not rel_exe.exists():
            rel_exe = rust_dir / "target" / "release" / "skill-ln.exe"
        dest_dir = Path.home() / ".cargo" / "bin"
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(rel_exe, dest_dir / rel_exe.name)
        print(f"[SUCCESS] Installed {rel_exe.name} to: {dest_dir / rel_exe.name}")
        return 0

    if args.install_hook:
        install_pre_commit_hook()
        return 0

    if args.syntax_only:
        return 0 if check_syntax() else 1

    if args.layout_only:
        return 0 if check_layout() else 1

    if args.skill_lint_only:
        return 0 if check_skill_markdown() else 1

    # Full checks sequence (or staged-scope filtered tests under --pre-commit)
    syntax_ok = check_syntax()
    layout_ok = check_layout()
    markdown_ok = check_skill_markdown()
    hygiene_ok = check_hygiene()
    parity_ok = check_parity()
    tests_ok = True
    if not args.skip_tests:
        if args.pre_commit:
            run_prog, run_stud, run_rust = detect_staged_scopes()
            tests_ok = run_unit_tests(
                run_progguide=run_prog,
                run_studio=run_stud,
                run_rust=run_rust,
            )
        else:
            tests_ok = run_unit_tests()

    if syntax_ok and layout_ok and markdown_ok and hygiene_ok and parity_ok and tests_ok:
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
