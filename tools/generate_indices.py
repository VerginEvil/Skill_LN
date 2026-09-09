#!/usr/bin/env python3
"""Regenerate search indices for the ERP LN Programmer's Guide skill.

Usage:
    python tools/generate_indices.py [--skill-dir erp-ln-progguide]
        [--edition 25082026] [--pages 2361]
        [--source-pdf "Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud) 25082026.pdf"]

Regenerates (standard library only):
    index/INDEX.tsv                          every reference page: path TAB title
    references/FUNCTION_INDEX.md             all 4GL functions grouped by topic
    references/PUBLIC_INTERFACES_INDEX.md    all public interfaces by chapter

All Markdown links emitted are relative and verified resolvable by
``tools/validate_skill.py``.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

INDEX_FILES = {"FUNCTION_INDEX.md", "PUBLIC_INTERFACES_INDEX.md",
               "EXTENSIONS_INDEX.md", "AFS_INDEX.md"}

# Legacy section order of INDEX.tsv (conversion sequence, not alphabetical).
INDEX_GROUP_ORDER = ["guide", "sql", "extensions", "public_interfaces", "afs"]

FUNC_SIG_RE = re.compile(r"`(function\b[^`]*)`")
FENCE_RE = re.compile(r"^```[^\n]*\n(.*?)```", re.M | re.S)
CHAPTER_DIR_RE = re.compile(r"^ch(\d{1,2})_(.*)$")


def page_title(md_path: Path) -> str:
    """Title of a reference page: first Markdown heading, else stem."""
    try:
        with md_path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh.read().splitlines():
                s = line.strip()
                if s.startswith("#"):
                    return s.lstrip("#").strip()
    except OSError:
        pass
    return md_path.stem


def first_signature(md_path: Path) -> str | None:
    """First backticked ``function ...`` signature in a reference page."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = FUNC_SIG_RE.search(text)
    if m:
        return m.group(1).strip()
    # SQL grammar pages carry BNF (``<rule> ::= ...``) in the first fenced
    # block instead of a function signature; surface it as the preview.
    # (Plain code examples such as XML snippets are left out, matching the
    # legacy index which only shows signatures and grammar rules.)
    fm = FENCE_RE.search(text)
    if fm:
        preview = re.sub(r"[\u200b\u200c\u200d\ufeff]", "", fm.group(1))
        preview = re.sub(r"\s+", " ", preview).strip()
        if preview.startswith("<") and "::=" in preview:
            return preview
    return None


def is_function_page(skill: Path, rel: str) -> bool:
    """FUNCTION_INDEX inclusion rule: under ``functions_*`` or ``functions_*`` stem."""
    parts = Path(rel).parts  # references/guide/progguide/<dir>/<file>
    if len(parts) < 4 or parts[0] != "references" or parts[1] != "guide":
        return False
    return parts[3].startswith("functions_") or Path(parts[-1]).stem.startswith("functions_")


def group_name(rel: str) -> str:
    """Group key: parent dir minus ``functions_`` prefix, else parent name."""
    parent = Path(rel).parent.name
    if parent.startswith("functions_"):
        return parent[len("functions_"):]
    return parent


def generate_index_tsv(skill: Path) -> tuple[str, int]:
    refs = skill / "references"
    by_group: dict[str, list[str]] = {}
    for path in refs.rglob("*.md"):
        rel = path.relative_to(skill).as_posix()
        if path.name in INDEX_FILES:
            continue
        group = rel.split("/")[1]
        by_group.setdefault(group, []).append(
            "%s\t%s" % (rel, page_title(path).replace("\t", " ")))
    rows: list[str] = []
    for group in INDEX_GROUP_ORDER + sorted(g for g in by_group if g not in INDEX_GROUP_ORDER):
        rows.extend(sorted(by_group.get(group, [])))
    return "\n".join(rows) + "\n", len(rows)


def generate_function_index(skill: Path) -> tuple[str, int]:
    guide = skill / "references" / "guide"
    groups: dict[str, list[str]] = {}
    for path in sorted(guide.rglob("*.md"), key=lambda p: p.relative_to(skill).as_posix()):
        rel = path.relative_to(skill).as_posix()
        if not is_function_page(skill, rel):
            continue
        grp = group_name(rel)
        display = path.stem.replace(".", " ")
        sig = first_signature(path)
        if sig:
            entry = "- **%s** | `%s` -> `%s`" % (display, sig, rel)
        else:
            entry = "- **%s**  -> `%s`" % (display, rel)
        groups.setdefault(grp, []).append(entry)
    total = sum(len(v) for v in groups.values())
    lines = ["# Baan/LN 4GL Function Index", "",
             "%d functions. Grep this file, then Read the referenced .md file." % total, ""]
    for grp in sorted(groups):
        lines.append("## %s" % grp)
        lines.append("")
        lines.extend(groups[grp])
    return "\n".join(lines).rstrip() + "\n", total


def chapter_short_title(chapter_dir: str, sample_file: Path | None) -> str:
    """Human short title, e.g. ch10_commissions_and_rebates -> Commissions And Rebates."""
    m = CHAPTER_DIR_RE.match(chapter_dir)
    slug = m.group(2) if m else chapter_dir
    title = ""
    if sample_file is not None and sample_file.is_file():
        try:
            for line in sample_file.read_text(encoding="utf-8", errors="replace").splitlines():
                if line.startswith("> Chapter:"):
                    title = line.split(":", 1)[1].strip()
                    break
        except OSError:
            pass
    if title:
        short = re.sub(r"^(Chapter \d+\s+)?(Public Interfaces for|Process Extensions)\s*", "", title)
        short = short.replace("&", " ").strip()
        short = re.sub(r"\s+", " ", short)
        short = re.sub(r"\band\b", "And", short)
        if short:
            return short
    return slug.replace("_", " ").title()


def generate_public_interfaces_index(skill: Path, edition: str, pages: int,
                                     source_pdf: str) -> tuple[str, int]:
    pi = skill / "references" / "public_interfaces"
    chapters: dict[int, tuple[str, list[str]]] = {}
    for path in sorted(pi.rglob("*.md"), key=lambda p: p.relative_to(skill).as_posix()):
        rel = path.relative_to(skill).as_posix()
        parent = path.parent.name
        m = CHAPTER_DIR_RE.match(parent)
        if m and path.parent != pi:
            num = int(m.group(1))
            _dirname, entries = chapters.get(num, (parent, []))
            entries.append("- [%s](%s)" % (path.stem, rel))
            chapters[num] = (parent, entries)
    total = sum(len(entries) for _, entries in chapters.values())
    pages_str = "{:,}".format(pages)
    lines = ["# Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud)", "",
             "Reference for all **%d public interface functions** and **process extensions** of Infor LN Cloud" % total,
             "(edition %s, %s pages). One file per function: description, DLL, availability" % (edition, pages_str),
             "(release/KB), syntax, Usage (Expl/Pre/Post/Input/Output), Return values.",
             "",
             "Start here when writing code that calls LN functionality from an extension",
             "(4GL Address.Create(...), Item.GetData(...) etc.) or hooks a process via a",
             "process extension DLL (\tdext.*, whext.*, \tiext.* ...).",
             "",
             "Source PDF: %s." % source_pdf,
             "",
             "## Top-level files",
             "",
             "- ch01_introduction.md - guide introduction, calling conventions",
             "- zz_release_history.md - release matrix: which interface/process extension appeared in which LN Cloud release",
             ""]
    for num in sorted(chapters):
        dirname, entries = chapters[num]
        sample = pi / dirname / (entries[0].split("[", 1)[1].split("]", 1)[0] + ".md")
        short = chapter_short_title(dirname, sample)
        lines.append("## Chapter %d: %s (%d)" % (num, short, len(entries)))
        lines.append("")
        lines.extend(entries)
        lines.append("")
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) + "\n", total


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Regenerate skill indices.")
    ap.add_argument("--skill-dir", default="erp-ln-progguide")
    ap.add_argument("--edition", default="25082026")
    ap.add_argument("--pages", type=int, default=2361)
    ap.add_argument("--source-pdf",
                    default="Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud) 25082026.pdf")
    args = ap.parse_args(argv)
    skill = Path(args.skill_dir)

    tsv, n_pages = generate_index_tsv(skill)
    (skill / "index" / "INDEX.tsv").write_text(tsv, encoding="utf-8")
    print("INDEX.tsv: %d pages" % n_pages)

    func_index, n_funcs = generate_function_index(skill)
    (skill / "references" / "FUNCTION_INDEX.md").write_text(func_index, encoding="utf-8")
    print("FUNCTION_INDEX.md: %d functions" % n_funcs)

    pi_index, n_pi = generate_public_interfaces_index(skill, args.edition, args.pages, args.source_pdf)
    (skill / "references" / "PUBLIC_INTERFACES_INDEX.md").write_text(pi_index, encoding="utf-8")
    print("PUBLIC_INTERFACES_INDEX.md: %d interfaces" % n_pi)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
