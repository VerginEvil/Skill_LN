#!/usr/bin/env python3
"""One-command update pipeline for the ERP LN Programmer's Guide skill.

Usage:
    python tools/update_pipeline.py [--update-dir update]
        [--skill-dir erp-ln-progguide] [--workdir <tmp>]
        [--skip-chm] [--skip-pdf] [--skip-indices] [--skip-validate] [--dry-run]

Takes new source artifacts dropped into ``update/`` (Infor Programmer's
Guide ``*.chm`` files and the Public Interfaces ``*.pdf`` guide),
decompiles them with native ``hh.exe``, converts everything to Markdown,
regenerates the indices and validates the result, printing before/after
diff statistics.
"""

from __future__ import annotations

import argparse
import glob
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import convert_chm  # noqa: E402
import convert_pdf_interfaces  # noqa: E402
import generate_indices  # noqa: E402
import validate_skill  # noqa: E402

EDITION_RE = re.compile(r"(\d{8})\.pdf$", re.IGNORECASE)


def detect_sources(update_dir: Path) -> dict:
    """Find and validate the expected source artifacts in *update_dir*."""
    chms = sorted(update_dir.glob("progguide_*.chm"))
    pdfs = sorted(update_dir.glob("*Public Interfaces*.pdf"))
    sources: dict = {"chms": [], "pdf": None, "edition": None, "pages": 0}
    for chm in chms:
        kind = "sql" if "sql" in chm.stem.lower() else "guide"
        sources["chms"].append({"path": chm, "kind": kind})
    if pdfs:
        pdf = pdfs[-1]  # newest by filename sort
        sources["pdf"] = pdf
        m = EDITION_RE.search(pdf.name)
        sources["edition"] = m.group(1) if m else "unknown"
    return sources


def pdf_page_count(pdf: Path) -> int:
    try:
        import pymupdf
    except ImportError:
        return 0
    doc = pymupdf.open(str(pdf))
    try:
        return doc.page_count
    finally:
        doc.close()


def count_md(root: Path) -> int:
    if not root.is_dir():
        return 0
    return sum(1 for _ in root.rglob("*.md"))


def snapshot_counts(skill: Path) -> dict:
    refs = skill / "references"
    return {
        "guide": count_md(refs / "guide"),
        "sql": count_md(refs / "sql"),
        "public_interfaces": count_md(refs / "public_interfaces"),
        "total": count_md(refs),
    }


def expected_chm_outputs(src_root: Path, dst_root: Path) -> set[Path]:
    """Markdown paths (resolved) the CHM sources should produce."""
    expected: set[Path] = set()
    for ext in ("*.htm", "*.html"):
        for src in src_root.rglob(ext):
            expected.add(((dst_root / src.relative_to(src_root)).with_suffix(".md")).resolve())
    return expected


def prune_stale(dst_root: Path, expected: set[Path]) -> list[Path]:
    """Delete ``*.md`` files under *dst_root* no longer produced. Returns deleted."""
    deleted: list[Path] = []
    if not dst_root.is_dir():
        return deleted
    for existing in sorted(dst_root.rglob("*.md")):
        if existing.resolve() not in expected:
            existing.unlink()
            deleted.append(existing)
    for sub in sorted(dst_root.iterdir()):
        if sub.is_dir() and not any(sub.iterdir()):
            sub.rmdir()
    return deleted


def git_change_summary(repo: Path, limit: int = 40) -> list[str]:
    try:
        proc = subprocess.run(["git", "status", "--short", "--", "erp-ln-progguide", "tools", "docs"],
                              capture_output=True, text=True, cwd=str(repo), timeout=120)
    except (OSError, subprocess.SubprocessError):
        return []
    if proc.returncode != 0:
        return []
    lines = [l for l in proc.stdout.splitlines() if l.strip()]
    if len(lines) > limit:
        lines = lines[:limit] + ["... (%d more)" % (len(lines) - limit)]
    return lines


def run_pipeline(args) -> int:
    t0 = time.time()
    repo = Path.cwd()
    update_dir = Path(args.update_dir)
    skill = Path(args.skill_dir)
    refs = skill / "references"
    print("== ERP LN skill update pipeline ==")
    print("update dir: %s | skill dir: %s" % (update_dir, skill))

    sources = detect_sources(update_dir)
    if not args.skip_chm and not sources["chms"]:
        print("ERROR: no progguide_*.chm found in %s" % update_dir)
        return 2
    if not args.skip_pdf and sources["pdf"] is None:
        print("ERROR: no *Public Interfaces*.pdf found in %s" % update_dir)
        return 2
    for chm in sources["chms"]:
        print("source CHM [%s]: %s" % (chm["kind"], chm["path"].name))
    if sources["pdf"] is not None:
        print("source PDF [edition %s]: %s" % (sources["edition"], sources["pdf"].name))
    before = snapshot_counts(skill)
    print("before: guide=%d sql=%d public_interfaces=%d total=%d" % (
        before["guide"], before["sql"], before["public_interfaces"], before["total"]))
    if args.dry_run:
        print("dry-run: nothing executed.")
        return 0

    workdir = Path(args.workdir) if args.workdir else Path(tempfile.mkdtemp(prefix="ln_update_"))
    workdir.mkdir(parents=True, exist_ok=True)
    try:
        # --- CHM conversion -------------------------------------------------
        if not args.skip_chm:
            for chm in sources["chms"]:
                step = time.time()
                sub = "sql" if chm["kind"] == "sql" else "guide"
                dst_root = refs / sub / "progguide"
                print("-- decompiling %s ..." % chm["path"].name)
                decompiled = convert_chm.decompile_chm(chm["path"], workdir)
                src_root = convert_chm.find_progguide_root(decompiled)
                print("-- converting %s -> %s ..." % (src_root, dst_root))
                stats = convert_chm.convert_tree(src_root, dst_root)
                deleted = prune_stale(dst_root, expected_chm_outputs(src_root, dst_root))
                print("   found=%d written=%d skipped=%d pruned=%d (%.1fs)" % (
                    stats["found"], stats["written"], stats["skipped"],
                    len(deleted), time.time() - step))
                for d in deleted[:20]:
                    print("   pruned: %s" % d.relative_to(skill).as_posix())
        # --- PDF conversion -------------------------------------------------
        edition, npages = sources["edition"], 0
        if not args.skip_pdf and sources["pdf"] is not None:
            step = time.time()
            npages = pdf_page_count(sources["pdf"])
            print("-- converting PDF (%d pages) -> references/public_interfaces ..." % npages)
            stats = convert_pdf_interfaces.convert_pdf(sources["pdf"], refs / "public_interfaces")
            print("   functions=%d written=%d unchanged=%d deleted=%d "
                  "release_ifaces=%d release_exts=%d duplicates=%r (%.1fs)" % (
                      stats["functions"], stats["written"], stats["unchanged"],
                      stats["deleted"], stats.get("release_interfaces", 0),
                      stats.get("release_extensions", 0),
                      stats.get("duplicates", []), time.time() - step))
        # --- Indices --------------------------------------------------------
        if not args.skip_indices:
            step = time.time()
            if edition is None:
                edition = args.edition
            if not npages:
                npages = args.pages
            tsv, n_pages = generate_indices.generate_index_tsv(skill)
            (skill / "index" / "INDEX.tsv").write_text(tsv, encoding="utf-8")
            func_index, n_funcs = generate_indices.generate_function_index(skill)
            (refs / "FUNCTION_INDEX.md").write_text(func_index, encoding="utf-8")
            source_pdf = sources["pdf"].name if sources["pdf"] is not None else args.source_pdf
            pi_index, n_pi = generate_indices.generate_public_interfaces_index(
                skill, edition, npages, source_pdf)
            (refs / "PUBLIC_INTERFACES_INDEX.md").write_text(pi_index, encoding="utf-8")
            print("indices: INDEX.tsv=%d FUNCTION_INDEX=%d PUBLIC_INTERFACES_INDEX=%d (%.1fs)"
                  % (n_pages, n_funcs, n_pi, time.time() - step))
        # --- Validation -----------------------------------------------------
        if not args.skip_validate:
            print("-- validating ...")
            problems = 0
            missing = validate_skill.check_index_tsv(skill)
            print("   INDEX.tsv: %d missing" % len(missing))
            problems += len(missing)
            for catalog in ("references/FUNCTION_INDEX.md",
                            "references/PUBLIC_INTERFACES_INDEX.md"):
                broken = validate_skill.check_catalog_links(skill, catalog)
                print("   %s: %d broken" % (catalog, len(broken)))
                problems += len(broken)
            checked, page_broken = validate_skill.check_page_links(skill)
            print("   page links: %d pages, %d broken" % (checked, len(page_broken)))
            problems += len(page_broken)
            if problems:
                print("VALIDATION FAILED: %d problem(s)" % problems)
                return 1
            print("validation: PASS")
    finally:
        if not args.workdir:
            shutil.rmtree(workdir, ignore_errors=True)
            print("workdir cleaned: %s" % workdir)

    after = snapshot_counts(skill)
    print("after:  guide=%d sql=%d public_interfaces=%d total=%d" % (
        after["guide"], after["sql"], after["public_interfaces"], after["total"]))
    print("delta:  guide=%+d sql=%+d public_interfaces=%+d total=%+d (%.1fs total)" % (
        after["guide"] - before["guide"], after["sql"] - before["sql"],
        after["public_interfaces"] - before["public_interfaces"],
        after["total"] - before["total"], time.time() - t0))
    changes = git_change_summary(repo)
    if changes:
        print("git changes (erp-ln-progguide/tools/docs):")
        for line in changes:
            print("  %s" % line)
    print("pipeline: DONE")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Update the ERP LN skill from update/ artifacts.")
    ap.add_argument("--update-dir", default="update")
    ap.add_argument("--skill-dir", default="erp-ln-progguide")
    ap.add_argument("--output-dir", default=None,
                    help="alias for --skill-dir (ticket 01 CLI contract)")
    ap.add_argument("--workdir", default=None)
    ap.add_argument("--edition", default="25082026")
    ap.add_argument("--pages", type=int, default=2361)
    ap.add_argument("--source-pdf",
                    default="Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud) 25082026.pdf")
    ap.add_argument("--skip-chm", action="store_true")
    ap.add_argument("--skip-pdf", action="store_true")
    ap.add_argument("--skip-indices", action="store_true")
    ap.add_argument("--skip-validate", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    if args.output_dir is not None:
        args.skill_dir = args.output_dir
    return run_pipeline(args)


if __name__ == "__main__":
    raise SystemExit(main())
