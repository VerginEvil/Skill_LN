#!/usr/bin/env python3
"""Validate the ERP LN Programmer's Guide skill tree.

Usage:
    python tools/validate_skill.py [--skill-dir erp-ln-progguide]

Checks (standard library only):
    1. Every path listed in ``index/INDEX.tsv`` exists on disk.
    2. Every relative Markdown link in ``references/FUNCTION_INDEX.md``
       and ``references/PUBLIC_INTERFACES_INDEX.md`` resolves to a file.
    3. Every relative in-page link (``*.md`` targets) across all reference
       pages resolves (anchors are not checked, only file existence).

Exits 0 when everything resolves, 1 otherwise, printing a summary plus
the first few failures of each class.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SHOW_MAX = 15


def _link_target(raw: str) -> str | None:
    raw = raw.strip()
    if not raw or raw.startswith(("#", "mailto:")):
        return None
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", raw):
        return None  # http:, https:, ftp: ...
    path, _sep, _anchor = raw.partition("#")
    path = path.strip()
    if not path:
        return None
    if any(c in path for c in "<>|*?"):
        # Not a file target: documentation syntax that merely looks like a
        # link, e.g. ``[Alt+](<single char>|F<nr>|<special key>)``.
        return None
    return path


def check_index_tsv(skill: Path) -> list[str]:
    """All INDEX.tsv entries exist. Returns missing paths."""
    missing: list[str] = []
    tsv = skill / "index" / "INDEX.tsv"
    try:
        lines = tsv.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return ["%s (unreadable: %s)" % (tsv.as_posix(), exc)]
    for line in lines:
        if not line.strip():
            continue
        rel = line.split("\t", 1)[0].strip()
        if not (skill / rel).is_file():
            missing.append(rel)
    return missing


def check_catalog_links(skill: Path, catalog: str) -> list[str]:
    """All relative links in a catalog index resolve. Returns failures."""
    failures: list[str] = []
    try:
        text = (skill / catalog).read_text(encoding="utf-8")
    except OSError as exc:
        return ["%s (unreadable: %s)" % (catalog, exc)]
    for raw in LINK_RE.findall(text):
        target = _link_target(raw)
        if target is None:
            continue
        if not (skill / target).is_file():
            failures.append("%s -> %s" % (catalog, target))
    return failures


def check_page_links(skill: Path) -> tuple[int, list[str]]:
    """All relative page links across references resolve.

    Returns (pages_checked, failures as 'page -> target').
    """
    failures: list[str] = []
    checked = 0
    for path in sorted((skill / "references").rglob("*.md")):
        checked += 1
        rel = path.relative_to(skill).as_posix()
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            failures.append("%s (unreadable)" % rel)
            continue
        for raw in LINK_RE.findall(text):
            target = _link_target(raw)
            if target is None:
                continue
            if target.startswith("references/"):
                # Catalog-style skill-relative link (used by the index files).
                resolved = skill / target
            else:
                resolved = Path(os.path.normpath(os.path.join(str(path.parent), target)))
            if not resolved.is_file():
                failures.append("%s -> %s" % (rel, target))
    return checked, failures


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate skill index/link integrity.")
    ap.add_argument("--skill-dir", default="erp-ln-progguide")
    args = ap.parse_args(argv)
    skill = Path(args.skill_dir)

    errors = 0
    missing = check_index_tsv(skill)
    print("INDEX.tsv: %s (%d missing)" % ("OK" if not missing else "FAIL", len(missing)))
    for m in missing[:SHOW_MAX]:
        print("  missing: %s" % m)
    errors += len(missing)

    for catalog in ("references/FUNCTION_INDEX.md", "references/PUBLIC_INTERFACES_INDEX.md"):
        failures = check_catalog_links(skill, catalog)
        print("%s: %s (%d broken)" % (catalog, "OK" if not failures else "FAIL", len(failures)))
        for f in failures[:SHOW_MAX]:
            print("  broken: %s" % f)
        errors += len(failures)

    checked, page_failures = check_page_links(skill)
    print("page links: %s (%d pages, %d broken)"
          % ("OK" if not page_failures else "FAIL", checked, len(page_failures)))
    for f in page_failures[:SHOW_MAX]:
        print("  broken: %s" % f)
    errors += len(page_failures)

    print("validate_skill: %s (%d problem(s))" % ("PASS" if not errors else "FAIL", errors))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
