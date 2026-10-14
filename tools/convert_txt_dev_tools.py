#!/usr/bin/env python3
"""Convert Infor LN Development Tools 2016 text manual into clean Markdown references.

Usage:
    python tools/convert_txt_dev_tools.py [--src update/Infor\\ LN\\ Development\\ Tools\\ 2016.txt]
                                         [--out-dir erp-ln-progguide/references/dev_tools]
                                         [--index erp-ln-progguide/references/DEV_TOOLS_INDEX.md]

Splits the source text into 13 chapters:
    ch01_development_tools_introduction.md
    ch02_overview_of_software_components.md
    ch03_data_dictionaries.md
    ch04_development_parameters_and_authorizations.md
    ch05_software_development_procedures.md
    ch06_session_personalizations.md
    ch07_version_and_release_management.md
    ch08_ln_software_maintenance.md
    ch09_ln_homepages.md
    ch10_ln_reporting_overview.md
    ch11_4gl_reports.md
    ch12_session_based_reporting.md
    ch13_query_based_reporting.md

Also generates DEV_TOOLS_INDEX.md mapping all chapters and sections.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

CHAPTER_METADATA = [
    (1, "Development Tools Introduction", "ch01_development_tools_introduction.md"),
    (2, "Overview of Software Components", "ch02_overview_of_software_components.md"),
    (3, "Data Dictionaries", "ch03_data_dictionaries.md"),
    (4, "Development Parameters and Authorizations", "ch04_development_parameters_and_authorizations.md"),
    (5, "Software Development Procedures", "ch05_software_development_procedures.md"),
    (6, "Session Personalizations", "ch06_session_personalizations.md"),
    (7, "Version and Release Management", "ch07_version_and_release_management.md"),
    (8, "LN Software Maintenance", "ch08_ln_software_maintenance.md"),
    (9, "LN Homepages", "ch09_ln_homepages.md"),
    (10, "LN Reporting Overview", "ch10_ln_reporting_overview.md"),
    (11, "4GL Reports", "ch11_4gl_reports.md"),
    (12, "Session-based Reporting", "ch12_session_based_reporting.md"),
    (13, "Query-based Reporting", "ch13_query_based_reporting.md"),
]

FOOTER_RE = re.compile(
    r"^(?:\d+\s*\|\s*Infor LN Development Tools\s*\|\s*Development Guide|"
    r"Infor LN Development Tools\s*\|\s*Development Guide\s*\|\s*\d+)\s*$",
    re.IGNORECASE,
)

SUB_HEADING_KEYWORDS = {
    "procedure aim",
    "procedure result and prerequisites",
    "procedure summary",
    "procedure details",
    "dal 1",
    "dal 2",
    "field dependencies",
    "business methods",
    "user exit dlls",
    "the runtime data dictionary",
    "the application data dictionary",
    "convert to runtime data dictionary",
    "development parameters",
    "developer authorizations",
    "design data model",
    "implement data model",
    "create user applications",
    "create business logic",
    "create menus",
    "document",
    "deploy application",
    "identify changes",
    "package combinations",
    "package vrcs",
    "package vrc code",
    "standard environment",
    "runtime environment",
    "development environment",
    "vrc derivation",
    "individual solutions",
    "collections",
    "feature packs and patches",
    "feature packs",
    "patches",
    "distributor's policy",
    "pmc distributor functionality",
    "pmc recipient functionality",
    "setup",
    "setup procedure",
    "parameters",
    "base vrcs",
    "base vrc combinations",
    "customizations",
    "other",
    "toolbar buttons",
    "report structure",
    "report script structure",
    "to edit the form content",
    "to edit the form structure",
    "to edit the form sequence",
    "to edit report input fields",
    "to edit report layouts",
    "to edit a report script",
    "to create the session",
    "to create the program script",
    "to create the details sessions",
    "to create a main entity detail session",
    "to create a multi-main table controller session",
    "to create a satellite session",
    "to assign satellites to the controller",
    "to compile and run the controller session",
    "to integrate the controller session",
    "to translate resource files",
}


def parse_toc(text: str) -> dict[int, list[tuple[str, int]]]:
    """Extract headings and page numbers per chapter from TOC."""
    toc_start = text.find("Table of Contents")
    ch1_match = re.search(r"(?:\x0c|^)\s*Chapter\s+1\s*\r?\n", text[toc_start:])
    if not ch1_match:
        return {}
    toc_text = text[toc_start : toc_start + ch1_match.start()]

    headings_by_ch: dict[int, list[tuple[str, int]]] = {}
    current_ch = 0

    for line in toc_text.splitlines():
        line = line.strip()
        m = re.match(r"^([^\.]+)\.{3,}\s*(\d+)", line)
        if not m:
            continue
        title = m.group(1).strip()
        page = int(m.group(2))

        ch_m = re.match(r"^Chapter\s+(\d+)\s+(.*)", title, re.IGNORECASE)
        if ch_m:
            current_ch = int(ch_m.group(1))
            headings_by_ch[current_ch] = []
        elif current_ch > 0:
            # Skip if title equals the chapter title itself
            headings_by_ch[current_ch].append((title, page))

    return headings_by_ch


def clean_page_lines(page: str, ch_title: str, is_first_page: bool) -> list[str]:
    """Clean headers, footers, and artifacts from a single page."""
    raw_lines = page.splitlines()
    cleaned: list[str] = []

    for line in raw_lines:
        s = line.strip()
        if FOOTER_RE.match(s):
            continue
        cleaned.append(line)

    # Remove running header on continuation pages
    if not is_first_page and cleaned:
        # Find first non-empty line
        first_idx = None
        for i, l in enumerate(cleaned):
            if l.strip():
                first_idx = i
                break
        if first_idx is not None:
            first_val = cleaned[first_idx].strip()
            if first_val.lower() == ch_title.lower() or first_val.lower() == "infor ln development tools":
                cleaned.pop(first_idx)

    return cleaned


def format_chapter(
    ch_num: int,
    ch_title: str,
    raw_slice: str,
    toc_headings: list[tuple[str, int]],
) -> str:
    """Format a chapter slice into clean GitHub-flavored Markdown."""
    pages = raw_slice.lstrip("\x0c\r\n ").split("\x0c")
    all_lines: list[str] = []

    for p_idx, page in enumerate(pages):
        page_lines = clean_page_lines(page, ch_title, is_first_page=(p_idx == 0))
        all_lines.extend(page_lines)

    # Join lines back for processing
    content = "\n".join(all_lines)

    # Fix hyphenated words broken across line wraps (e.g. "Reconfigu-\nration" -> "Reconfiguration")
    content = re.sub(r"([A-Za-z]{2,})-\r?\n([a-z]{2,})", r"\1\2", content)

    # Build lookup for TOC headings (lowercase -> original)
    heading_lookup = {h.lower(): h for h, _p in toc_headings}

    # Split lines and rebuild structured Markdown
    lines = content.splitlines()
    output_lines: list[str] = []

    # Title header
    output_lines.append(f"# Chapter {ch_num}: {ch_title}")
    output_lines.append("")

    i = 0
    total = len(lines)

    # Skip initial chapter banner on page 0 if present
    # e.g. "Chapter 2", "Overview of Software Components", "2"
    while i < total:
        s = lines[i].strip()
        if re.match(r"^Chapter\s+\d+$", s, re.IGNORECASE):
            i += 1
            if i < total and lines[i].strip().lower() == ch_title.lower():
                i += 1
            if i < total and re.match(r"^\d+$", lines[i].strip()):
                i += 1
            break
        i += 1

    in_list = False
    in_code = False

    while i < total:
        line = lines[i]
        s = line.strip()

        if not s:
            if not in_list:
                output_lines.append("")
            i += 1
            continue

        # Check for alert boxes
        if s in ("Important!", "Important"):
            output_lines.append("> [!IMPORTANT]")
            i += 1
            continue
        if s == "Note":
            output_lines.append("> [!NOTE]")
            i += 1
            continue
        if s in ("Caution!", "Caution"):
            output_lines.append("> [!CAUTION]")
            i += 1
            continue

        # Normalize bullets (▪ \u25aa, • \u2022)
        if s.startswith("\u25aa") or s.startswith("▪") or s.startswith("•"):
            bullet_body = re.sub(r"^[\u25aa▪•]\s*", "", s)
            output_lines.append(f"- {bullet_body}")
            in_list = True
            i += 1
            continue

        # Check if line matches a known TOC heading
        s_lower = s.lower()
        # Clean potential page numbers or noise from line
        s_clean = re.sub(r"\s*\(p\.\s*\d+\)\s*", "", s).strip()
        s_clean_lower = s_clean.lower()

        matched_heading = None
        if s_clean_lower in heading_lookup:
            matched_heading = heading_lookup[s_clean_lower]
        elif s_lower in heading_lookup:
            matched_heading = heading_lookup[s_lower]

        if matched_heading and not s.startswith("- ") and not re.match(r"^\d+\.", s):
            in_list = False
            # Determine level
            if matched_heading.lower() in SUB_HEADING_KEYWORDS:
                output_lines.append(f"### {matched_heading}")
            else:
                output_lines.append(f"## {matched_heading}")
            output_lines.append("")
            i += 1
            continue

        # Check for procedure sub-headings like "Result" / "Prerequisites" / "Step N: ..."
        if s in ("Result", "Prerequisites", "Step 1", "Step 2", "Step 3", "Step 4", "Step 5"):
            output_lines.append(f"#### {s}")
            output_lines.append("")
            in_list = False
            i += 1
            continue

        # Numbered list items
        if re.match(r"^\d+\.\s+", s):
            in_list = True
            output_lines.append(s)
            i += 1
            continue

        # Regular text
        if in_list and (line.startswith("  ") or line.startswith("\t")):
            # Continuation of list item
            output_lines.append(f"  {s}")
        else:
            in_list = False
            output_lines.append(s)

        i += 1

    # Final string cleanup
    result = "\n".join(output_lines)
    # Collapse 3+ consecutive newlines to 2
    result = re.sub(r"\n{3,}", "\n\n", result)
    # Remove any lingering form-feed characters
    result = result.replace("\x0c", "")

    # Ensure searchability for common alias crdd
    if ch_num == 3:
        result = result.replace("a reconfiguration process performs the", "a reconfiguration process (`crdd`) performs the")
    elif ch_num == 5:
        result = result.replace("## To reconfigure tables\n", "## To reconfigure tables (crdd)\n")
        result = result.replace("procedure to reconfigure tables.", "procedure to reconfigure tables (`crdd`).")

    return result.strip() + "\n"


def generate_dev_tools_index(
    metadata: list[tuple[int, str, str]],
    headings_by_ch: dict[int, list[tuple[str, int]]],
) -> str:
    """Generate DEV_TOOLS_INDEX.md."""
    lines: list[str] = [
        "# Infor LN Development Tools (2016)",
        "",
        "Reference documentation for the **Infor LN Development Tools** (Release 10.5 / 2016).",
        "Covers the software development lifecycle, 4GL engine, Data Dictionaries (runtime vs application),",
        "Data Access Layer (DAL 1 vs DAL 2), table reconfigurations (`crdd`), Multi-Main Table (MMT) sessions,",
        "Software Configuration Management (SCM), Product Maintenance Component (PMC), and 4GL/session/query reporting.",
        "",
        "## Chapters Overview",
        "",
        "| Chapter | Title | Reference File | Key Topics |",
        "|---|---|---|---|",
    ]

    key_topics = {
        1: "Architecture overview, developer environment, component model",
        2: "4GL Engine, DAL 1 & 2, domains, tables, sessions, forms, MMT, queries",
        3: "Runtime Data Dictionary (RTDD), Application Data Dictionary (ttadv), crdd",
        4: "Development parameters, authorizations, developer access controls",
        5: "Development procedures: Data model, table reconfiguration, sessions, forms, MMT, translations",
        6: "Session personalizations, user customizations, form views",
        7: "Version & Release Management, Package VRCs, environments, SCM check-in/out",
        8: "PMC (Product Maintenance Component), solutions, collections, patches, Feature Packs",
        9: "LN Homepages structure, homepage functions, resource files",
        10: "Reporting overview, 4GL reports vs Report Viewer, report projects",
        11: "4GL Reports architecture, layouts, report scripts",
        12: "Session-based reporting, Report Viewer devices, execution flow",
        13: "Query-based reporting, query report designs, report libraries, print sessions",
    }

    for ch_num, title, filename in metadata:
        rel_link = f"dev_tools/{filename}"
        topics = key_topics.get(ch_num, "")
        lines.append(f"| Chapter {ch_num} | {title} | [{filename}]({rel_link}) | {topics} |")

    lines.append("")
    lines.append("## Detailed Chapter Breakdown")
    lines.append("")

    for ch_num, title, filename in metadata:
        rel_link = f"dev_tools/{filename}"
        lines.append(f"### [Chapter {ch_num}: {title}]({rel_link})")
        lines.append("")
        sections = headings_by_ch.get(ch_num, [])
        if sections:
            for s_title, page in sections:
                lines.append(f"- {s_title} *(p. {page})*")
        else:
            lines.append("- General Introduction")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert Infor LN Development Tools txt to Markdown.")
    parser.add_argument(
        "--src",
        default="update/Infor LN Development Tools 2016.txt",
        help="Path to source txt file",
    )
    parser.add_argument(
        "--out-dir",
        default="erp-ln-progguide/references/dev_tools",
        help="Destination directory for chapter markdown files",
    )
    parser.add_argument(
        "--index",
        default="erp-ln-progguide/references/DEV_TOOLS_INDEX.md",
        help="Destination path for DEV_TOOLS_INDEX.md",
    )
    args = parser.parse_args(argv)

    src_path = Path(args.src)
    out_dir = Path(args.out_dir)
    index_path = Path(args.index)

    if not src_path.is_file():
        raise FileNotFoundError(f"Source file not found: {src_path}")

    out_dir.mkdir(parents=True, exist_ok=True)
    index_path.parent.mkdir(parents=True, exist_ok=True)

    text = src_path.read_text(encoding="utf-8", errors="replace")

    # 1. Parse TOC
    headings_by_ch = parse_toc(text)

    # 2. Slice chapters
    ch_pattern = re.compile(r"(?:\x0c|^)\s*Chapter\s+(\d+)\s*\r?\n\s*([^\r\n]+)")
    matches = list(ch_pattern.finditer(text))
    app_match = re.search(r"(?:\x0c|^)\s*Appendix\s+A", text)
    end_limit = app_match.start() if app_match else len(text)

    if len(matches) != 13:
        print(f"Warning: expected 13 chapter matches, found {len(matches)}")

    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else end_limit
        ch_num = int(matches[i].group(1))
        ch_title = matches[i].group(2).strip()

        # Match with metadata
        meta = next((m for m in CHAPTER_METADATA if m[0] == ch_num), None)
        filename = meta[2] if meta else f"ch{ch_num:02d}.md"

        raw_slice = text[start:end]
        ch_headings = headings_by_ch.get(ch_num, [])

        md_content = format_chapter(ch_num, ch_title, raw_slice, ch_headings)
        out_file = out_dir / filename
        out_file.write_text(md_content, encoding="utf-8")
        print(f"Generated Chapter {ch_num:02d}: {out_file.name} ({len(md_content):,} chars)")

    # 3. Generate DEV_TOOLS_INDEX.md
    index_content = generate_dev_tools_index(CHAPTER_METADATA, headings_by_ch)
    index_path.write_text(index_content, encoding="utf-8")
    print(f"Generated Index: {index_path.name} ({len(index_content):,} chars)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
