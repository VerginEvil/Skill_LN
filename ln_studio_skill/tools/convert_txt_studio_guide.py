#!/usr/bin/env python3
"""Convert Infor LN Studio Application Development Guide text into clean Markdown.

Usage:
    python ln_studio_skill/tools/convert_txt_studio_guide.py
        [--src "update/Infor LN Studio Application Development Guide (Cloud and On-premises) 09-2025.txt"]
        [--out-dir ln_studio_skill/references/studio_guide]
        [--index ln_studio_skill/references/STUDIO_INDEX.md]

Splits the source text into 12 chapters (one page per chapter, stable names)
plus a master STUDIO_INDEX.md mapping chapters to sections.

Depth weighting (recorded in docs/adr/0002-*):
    full detail: ch01 overview, ch02 installation/connectivity, ch03 activity/SCM,
                 ch04 development procedure incl. verification/debugging,
                 ch07 wizards/dialogs, ch08 multipage editors, ch09 script editor.
    summary:     ch05 InContext modeling, ch06 limitations, ch10 perspectives,
                 ch11 views, ch12 project server.
Summary chapters still carry the full cleaned source text (no invention);
the weighting is recorded in the index so agents know where to read deeply.

Converter precedent: ln_studio_skill/tools/convert_txt_dev_tools.py (strip form feeds and
recurring header/footer/page-number artifacts, detect chapter/section
headings, preserve procedure steps and lists, UTF-8 Markdown, skill-relative
links). Standard library only.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CHAPTER_METADATA = [
    (1, "LN Studio overview", "ch01_studio_overview.md"),
    (2, "Installation and configuration", "ch02_installation_and_configuration.md"),
    (3, "Activity based development", "ch03_activity_based_development.md"),
    (4, "Development procedure", "ch04_development_procedure.md"),
    (5, "InContext Modeling", "ch05_incontext_modeling.md"),
    (6, "LN Studio Limitations", "ch06_studio_limitations.md"),
    (7, "Wizards and Dialogs", "ch07_wizards_and_dialogs.md"),
    (8, "Multipage Editors", "ch08_multipage_editors.md"),
    (9, "Script Editor", "ch09_script_editor.md"),
    (10, "Perspectives", "ch10_perspectives.md"),
    (11, "Views", "ch11_views.md"),
    (12, "Infor LN Project Server", "ch12_project_server.md"),
]

FULL_DETAIL = {1, 2, 3, 4, 7, 8, 9}

RUNNING_HEADERS = {
    "contents",
    "about this guide",
    "ln studio overview",
    "installation and configuration",
    "activity based development",
    "development procedure",
    "incontext modeling",
    "ln studio limitations",
    "wizards and dialogs",
    "multipage editors",
    "script editor",
    "perspectives",
    "views",
    "infor ln project server",
    "glossary",
}

FOOTER_RE = re.compile(
    r"^Infor LN Studio Application Development Guide \(Cloud and On-premises\) \|\s*\d+\s*$"
)

# Headings that are clearly subordinate (tabs, toolbars, breakpoint props, ...).
SUB_HEADING_RE = re.compile(
    r"(tab$|toolbar$|shortcut menu$|icons|decorators$|properties$|"
    r"details$|help$|filter$|comment$|configurations$|messages$|"
    r"documentation tab$|^to |^step \d+|^result$|^prerequisites$)",
    re.IGNORECASE,
)

BULLET_RE = re.compile(r"^[\u25aa\u2022\u25cf\uf0b7\ufffd▪•·\-]\s*")


def parse_toc(text: str) -> dict[int, list[tuple[str, int]]]:
    """Extract headings and page numbers per chapter from the Contents TOC."""
    toc_start = text.find("Contents")
    if toc_start < 0:
        return {}
    # Body chapter 1 starts the end of the TOC region.
    m = re.search(r"(?m)^Chapter\s+1:\s{1,2}[^\.\n]+?\s*$", text[toc_start:])
    toc_text = text[toc_start:toc_start + m.start()] if m else text[toc_start:]
    headings: dict[int, list[tuple[str, int]]] = {}
    current = 0
    for raw in toc_text.splitlines():
        line = raw.strip()
        dm = re.match(r"^(.*?)\.{3,}\s*(\d+)\s*$", line)
        if not dm:
            continue
        title = re.sub(r"\s+", " ", dm.group(1).strip())
        page = int(dm.group(2))
        ch = re.match(r"^Chapter\s+(\d+)\s*:?\s*(.*)$", title, re.IGNORECASE)
        if ch:
            current = int(ch.group(1))
            headings[current] = []
        elif current > 0 and title:
            headings[current].append((title, page))
    return headings


def clean_page_lines(page: str, is_first_page: bool = False) -> list[str]:
    """Remove footer, running header, and page-number artifacts from one page."""
    cleaned: list[str] = []
    for line in page.splitlines():
        s = line.strip()
        if FOOTER_RE.match(s):
            continue
        if re.match(r"^\d+$", s) and len(s) <= 4:
            # Lone page number leftovers are handled with header/footer;
            # keep them only when they look like content (rare).
            continue
        cleaned.append(line.rstrip())
    # Drop running header: first non-empty line matching a known header.
    for i, line in enumerate(cleaned):
        if line.strip():
            if line.strip().lower() in RUNNING_HEADERS:
                cleaned.pop(i)
            break
    return cleaned


def format_chapter(
    ch_num: int,
    ch_title: str,
    raw_slice: str,
    toc_headings: list[tuple[str, int]],
    depth: str,
) -> str:
    """Format a chapter slice into clean Markdown."""
    pages = raw_slice.split("\x0c")
    all_lines: list[str] = []
    for page in pages:
        all_lines.extend(clean_page_lines(page))
    content = "\n".join(all_lines)
    content = re.sub(r"([A-Za-z]{2,})-\r?\n([a-z]{2,})", r"\1\2", content)
    content = content.replace("\x0c", "")

    heading_lookup = {h.lower(): h for h, _p in toc_headings}
    lines = content.splitlines()
    out: list[str] = [f"# Chapter {ch_num}: {ch_title}", ""]
    if depth == "summary":
        out.append(
            "> Summary treatment for this release: orientation-level coverage. "
            "The full cleaned source text is preserved below; consult the source "
            "guide for exhaustive detail."
        )
        out.append("")

    # Skip the chapter banner ("Chapter N" / title) at the top.
    i = 0
    total = len(lines)
    while i < total:
        s = lines[i].strip()
        if re.match(r"^Chapter\s+\d+\s*:?\s*", s):
            i += 1
            if i < total and lines[i].strip().lower() in (ch_title.lower(), ""):
                i += 1
            break
        i += 1

    in_list = False
    while i < total:
        line = lines[i]
        s = line.strip()
        if not s:
            if not in_list:
                out.append("")
            i += 1
            continue
        if s in ("Important!", "Important"):
            out.append("> [!IMPORTANT]")
            i += 1
            continue
        if s == "Note:" or s == "Note":
            out.append("> [!NOTE]")
            i += 1
            in_list = False
            continue
        if s in ("Caution!", "Caution", "Caution:"):
            out.append("> [!CAUTION]")
            i += 1
            continue
        bm = BULLET_RE.match(s)
        if bm:
            body = BULLET_RE.sub("", s)
            out.append(f"- {body}")
            in_list = True
            i += 1
            continue
        s_clean = re.sub(r"\s*\(p\.\s*\d+\)\s*", "", s).strip()
        key = s_clean.lower()
        matched = heading_lookup.get(key)
        if matched and not s.startswith("- ") and not re.match(r"^\d+[\.\)]\s+", s):
            in_list = False
            level = "###" if SUB_HEADING_RE.search(matched) else "##"
            out.append(f"{level} {matched}")
            out.append("")
            i += 1
            continue
        if re.match(r"^\d+[\.\)]\s+\S", s) or re.match(r"^\d+\s+[A-Z]", s):
            in_list = True
            out.append(s)
            i += 1
            continue
        if in_list and (line.startswith("  ") or line.startswith("\t")):
            out.append(f"  {s}")
        else:
            in_list = False
            out.append(s)
        i += 1

    result = "\n".join(out)
    result = re.sub(r"\n{3,}", "\n\n", result)
    result = result.replace("\x0c", "")
    return result.strip() + "\n"


def generate_studio_index(
    metadata: list[tuple[int, str, str]],
    headings_by_ch: dict[int, list[tuple[str, int]]],
) -> str:
    """Generate STUDIO_INDEX.md mapping chapters to sections."""
    key_topics = {
        1: "Eclipse RCP workbench, functions and features, user roles, scope and limitations, architecture, troubleshooting, applications, cloud differences",
        2: "First installation, prerequisites, workspace selection, connectivity settings, dynamic connection points, user preferences, multi-tenant/single-tenant cloud settings, updates",
        3: "Activity-based development, SCM usage, project VRC vs application SCM, VRC numbering, CM actions, activity context, clean/recover/reassign, run configurations",
        4: "Developing components, verification (warnings vs errors, problem markers), sample exercise, run/debug sessions, breakpoints, expressions, BFlow tests",
        5: "InContext modeling, context messages, InContext model (summary)",
        6: "General, Script Editor, CM, build, debugger, Web UI limitations (summary)",
        7: "Activity wizards/dialogs, browse/select dialogs, component creation wizard, domain/label/function/session/table creation, debugging dialogs, preferences, verify components",
        8: "Multipage editors per component (domain, function, label, library, menu, message, question, report, session, table), tabs, DAL and script handling",
        9: "Script editor, markers and ruler, code assist, comments, folding, navigation, breakpoints, WSDL source generation",
        10: "Application and Debug perspectives (summary)",
        11: "Activity Explorer, Breakpoints, Component Explorer, Debug, Expressions, History, Outline, Problems, Variables, Verify Components views (summary)",
        12: "Project Server procedures, software projects, delivery activities, solutions, editors, perspectives and views (summary)",
    }
    lines = [
        "# Infor LN Studio Application Development Guide — Studio Index",
        "",
        "Usage knowledge for **Infor LN Studio 10.8 (Eclipse RCP)**, distilled from the",
        "*Application Development Guide (Cloud and On-premises), September 2025* (12 chapters).",
        "Full-detail chapters preserve procedures, steps, and lists verbatim; summary chapters",
        "give orientation-level coverage without inventing behavior beyond the source.",
        "",
        "## Chapters Overview",
        "",
        "| Chapter | Title | Depth | Reference File | Key Topics |",
        "|---|---|---|---|---|",
    ]
    for ch_num, title, filename in metadata:
        depth = "full" if ch_num in FULL_DETAIL else "summary"
        topics = key_topics.get(ch_num, "")
        lines.append(
            f"| Chapter {ch_num} | {title} | {depth} | [studio_guide/{filename}](studio_guide/{filename}) | {topics} |"
        )
    lines += ["", "## Detailed Chapter Breakdown", ""]
    for ch_num, title, filename in metadata:
        depth = "full" if ch_num in FULL_DETAIL else "summary"
        lines.append(f"### [Chapter {ch_num}: {title}](studio_guide/{filename}) ({depth})")
        lines.append("")
        for s_title, page in headings_by_ch.get(ch_num, []):
            lines.append(f"- {s_title} *(p. {page})*")
        if not headings_by_ch.get(ch_num):
            lines.append("- General Introduction")
        lines.append("")
    lines += [
        "## Phase 2 boundary",
        "",
        "The *Integration Development Guide* (business interfaces, BOD modeling, hook",
        "reference, event publishing) is **out of scope** here and tracked as Phase 2.",
        "It must not duplicate the extensibility reference in `erp-ln-progguide`.",
        "",
    ]
    return "\n".join(lines).strip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert LN Studio Application Guide txt to Markdown.")
    ap.add_argument("--src", default="update/Infor LN Studio Application Development Guide (Cloud and On-premises) 09-2025.txt")
    ap.add_argument("--out-dir", default="ln_studio_skill/references/studio_guide")
    ap.add_argument("--index", default="ln_studio_skill/references/STUDIO_INDEX.md")
    args = ap.parse_args(argv)

    src = Path(args.src)
    out_dir = Path(args.out_dir)
    index_path = Path(args.index)
    if not src.is_file():
        raise FileNotFoundError(f"Source file not found: {src}")
    out_dir.mkdir(parents=True, exist_ok=True)
    index_path.parent.mkdir(parents=True, exist_ok=True)

    text = src.read_text(encoding="utf-8", errors="replace")
    headings_by_ch = parse_toc(text)

    body_pat = re.compile(r"(?m)^Chapter\s+(\d+):\s{1,2}([^\.\n]+?)\s*$")
    matches = [m for m in body_pat.finditer(text) if "..." not in m.group(0)]
    if len(matches) != 12:
        print(f"Warning: expected 12 chapter matches, found {len(matches)}")
    gloss = re.search(r"(?m)^Glossary\s*$", text)
    end_limit = gloss.start() if gloss else len(text)

    for k in range(len(matches)):
        start = matches[k].start()
        end = matches[k + 1].start() if k + 1 < len(matches) else end_limit
        ch_num = int(matches[k].group(1))
        meta = next((m for m in CHAPTER_METADATA if m[0] == ch_num), None)
        if meta is None:
            continue
        _, ch_title, filename = meta
        depth = "full" if ch_num in FULL_DETAIL else "summary"
        md = format_chapter(ch_num, ch_title, text[start:end], headings_by_ch.get(ch_num, []), depth)
        out = out_dir / filename
        out.write_text(md, encoding="utf-8")
        print(f"Generated Chapter {ch_num:02d} ({depth}): {filename} ({len(md):,} chars)")

    index_md = generate_studio_index(CHAPTER_METADATA, headings_by_ch)
    index_path.write_text(index_md, encoding="utf-8")
    print(f"Generated Index: {index_path.name} ({len(index_md):,} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
