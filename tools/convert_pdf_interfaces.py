#!/usr/bin/env python3
"""Extract Infor LN Public Interfaces & Process Extensions PDF to Markdown.

Usage:
    python tools/convert_pdf_interfaces.py --pdf <guide.pdf> --out <public_interfaces dir>

Requires ``pymupdf`` (already used for high-performance parsing of the
2,300+ page reference guide).

Layout (preserved for zero breaking changes):
    <out>/chNN_<slug>/<Interface>.md   one file per function / process extension
    <out>/ch01_introduction.md          About + Chapters 1-2 narrative
    <out>/zz_release_history.md         Appendix A release matrix

Each function file keeps the established format: ``# <Name>`` heading,
blockquote with Chapter/Group/Source, and a ``baan`` code fence with the
DLL, availability, Syntax, Usage, Input/Output and Return details.
"""

from __future__ import annotations

import argparse
import glob
import re
from pathlib import Path

try:
    import pymupdf
except ImportError:  # pragma: no cover
    pymupdf = None  # type: ignore

GUIDE_TITLE = "Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud)"

FUNC_RE = re.compile(r"^[A-Za-z][\w$]*(\.[\w$]+)+$")
CHAPTER_RE = re.compile(r"^Chapter (\d+)\b\s*(.*)$")
FOOTER_RE = re.compile(r"^\d+\s*\|\s*Infor LN")
RELEASE_RE = re.compile(r"^(\d{4}\.\d{2})\s+(\S.*)$")
ITEM_RE = re.compile(r"^[A-Za-z][\w$.]+\.[\w$.]+$")
INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WRAP_GAP = 35.0
ROW_TOL = 2.0
SPACE_DIVISOR = 3.5

# Canonical chapter directory slugs (established layout; reused so future
# editions keep identical paths even on a fresh output directory).
CHAPTER_SLUGS = {
    2: "ch02_extensibility",
    3: "ch03_common",
    4: "ch04_calendar",
    5: "ch05_intercompanytrade",
    6: "ch06_item",
    7: "ch07_engineering_data_management",
    8: "ch08_crm",
    9: "ch09_sales",
    10: "ch10_commissions_and_rebates",
    11: "ch11_product_catalogs",
    12: "ch12_purchase",
    13: "ch13_pricing",
    14: "ch14_landed_costs",
    15: "ch15_material_pricing",
    16: "ch16_planning",
    17: "ch17_standard_costs",
    18: "ch18_manufacturing_master",
    19: "ch19_job_shop",
    20: "ch20_subcontracting",
    21: "ch21_repetitive_manufacturing",
    22: "ch22_assembly",
    23: "ch23_manufacturing_tools",
    24: "ch24_manufacturing_project",
    25: "ch25_warehousing",
    26: "ch26_freight",
    27: "ch27_service",
    28: "ch28_rental",
    29: "ch29_invoicing",
    30: "ch30_taxation",
    31: "ch31_bod_bde",
    32: "ch32_factory_track",
    33: "ch33_project",
    34: "ch34_authorization_and_security",
    35: "ch35_quality_management",
    36: "ch36_financialintegration",
    37: "ch37_cash_management",
    38: "ch38_accounts_payable",
    39: "ch39_accounts_receivable",
    40: "ch40_general_ledger",
    41: "ch41_fixed_assets",
    42: "ch42_product_lifecycle_management",
    43: "ch43_extended_time_management",
    44: "ch44_object_configuration_management",
    45: "ch45_time_management",
    46: "ch46_localizations",
    47: "ch47_zwf_ag_shipment_and_customs",
    48: "ch48_software_utilities",
    49: "ch49_exchange",
    50: "ch50_job_management",
    51: "ch51_user_management",
    52: "ch52_document_output_management",
    53: "ch53_application_development",
    54: "ch54_application_personalization",
    55: "ch55_process_extensions",
}


# ---------------------------------------------------------------------------
# Pure helpers (unit-tested)
# ---------------------------------------------------------------------------

def sanitize_filename(name: str) -> str:
    """Make a function name safe as a file stem on Windows."""
    cleaned = INVALID_FILENAME_CHARS.sub("_", name).strip()
    cleaned = re.sub(r"\.+$", "", cleaned)
    return cleaned or "_"


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return re.sub(r"_+", "_", slug)


def existing_chapter_dirs(out_dir: Path) -> dict[int, str]:
    """Map chapter number -> existing directory name (chNN_<slug>)."""
    mapping: dict[int, str] = {}
    if out_dir.is_dir():
        for sub in sorted(out_dir.iterdir()):
            if sub.is_dir():
                m = re.match(r"^ch(\d{1,2})_", sub.name)
                if m:
                    mapping[int(m.group(1))] = sub.name
    return mapping


def chapter_dirname(num: int, title: str, mapping: dict[int, str]) -> str:
    if num in mapping:
        return mapping[num]
    if num in CHAPTER_SLUGS:
        return CHAPTER_SLUGS[num]
    short = CHAPTER_RE.match(title)
    topic = (short.group(2) if short else title) or "chapter"
    return "ch%02d_%s" % (num, slugify(topic))


def join_same_row(linelets: list[dict]) -> list[str]:
    """Join dict linelets sharing a visual row with gap-proportional spaces.

    Each linelet: {"y": y0, "x0":.., "x1":.., "text":..}. Returns row strings.
    """
    ordered = sorted(linelets, key=lambda l: (round(l["y"], 1), l["x0"]))
    rows: list[list[dict]] = []
    for ln in ordered:
        if rows and abs(ln["y"] - rows[-1][0]["y"]) <= ROW_TOL:
            rows[-1].append(ln)
        else:
            rows.append([ln])
    out: list[str] = []
    for row in rows:
        row.sort(key=lambda l: l["x0"])
        # Legacy layout strips leading indentation from every body row.
        parts = [row[0]["text"].strip()]
        for prev, cur in zip(row, row[1:]):
            gap = cur["x0"] - prev["x1"]
            nspaces = max(1, int(round(gap / SPACE_DIVISOR)))
            nspaces = min(nspaces, 12)
            parts.append(" " * nspaces + cur["text"].strip())
        out.append("".join(parts).rstrip())
    return [r for r in out if r.strip()]


def parse_release_history(lines: list[str]) -> tuple[list[str], list[tuple[str, list[str]]],
                                                      list[tuple[str, list[str]]]]:
    """Parse Appendix A text lines into (title_lines, interfaces, extensions).

    Each release group is (release, [items]). Pure function for testability.
    """
    title_lines: list[str] = []
    interfaces: list[tuple[str, list[str]]] = []
    extensions: list[tuple[str, list[str]]] = []
    section: str | None = None  # "ifaces" | "exts"
    current: tuple[str, list[str]] | None = None
    for raw in lines:
        line = raw.strip()
        if not line or FOOTER_RE.match(line):
            continue
        if line in ("Release Public Interface", "Release Process Extension"):
            continue
        if line.startswith("Appendix A"):
            title_lines.append(line)
            continue
        if line.startswith("Extensions per Infor LN"):
            if title_lines:
                title_lines[-1] = title_lines[-1] + " " + line
            else:
                title_lines.append(line)
            continue
        if line == "Public Interfaces":
            section = "ifaces"
            continue
        if line == "Process Extensions":
            section = "exts"
            current = None
            continue
        if line.startswith("The following table shows"):
            continue
        m = RELEASE_RE.match(line)
        if m and section in ("ifaces", "exts"):
            release, first = m.group(1), m.group(2).strip()
            current = (release, [first] if ITEM_RE.match(first) else [])
            (interfaces if section == "ifaces" else extensions).append(current)
            continue
        if ITEM_RE.match(line) and section in ("ifaces", "exts"):
            if current is None:
                current = ("(undated)", [])
                (interfaces if section == "ifaces" else extensions).append(current)
            current[1].append(line)
            continue
        # Other narrative lines (running heads etc.) are ignored.
    return title_lines, interfaces, extensions


# ---------------------------------------------------------------------------
# PDF structure scan
# ---------------------------------------------------------------------------

def _is_courier(fonts: set[str]) -> bool:
    return bool(fonts) and all("Courier" in f for f in fonts)


def iter_page_events(page) -> tuple[list[tuple], int | None]:
    """Scan one PDF page into structural events plus printed page number.

    Returns (events, printed_no). Events: ("chapter", num, title),
    ("group", title), ("function", name), ("text", text, is_courier,
    y, x0, x1). Header/footer (Arial 8pt) lines are skipped, except the
    footer page number which is captured.
    """
    d = page.get_text("dict")
    printed_no: int | None = None
    # Keep dict blocks intact: each block is one paragraph unit.
    blocks: list[list[dict]] = []
    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        lines: list[dict] = []
        for l in b["lines"]:
            spans = l.get("spans") or []
            if not spans:
                continue
            txt = "".join(s["text"] for s in spans)
            if not txt.strip():
                continue
            fonts = set(s["font"] for s in spans)
            sizes = set(round(s["size"], 1) for s in spans)
            if FOOTER_RE.match(txt.strip()):
                try:
                    printed_no = int(txt.strip().split("|")[0].strip())
                except ValueError:
                    pass
                continue
            if sizes == {8.0} and fonts == {"ArialMT"}:
                continue  # running heads / footers carry no content
            x0, y0, x1, _y1 = l["bbox"]
            lines.append({"y": y0, "x0": x0, "x1": x1, "text": txt,
                          "fonts": fonts, "sizes": sizes})
        if lines:
            lines.sort(key=lambda l: (round(l["y"], 1), l["x0"]))
            blocks.append(lines)
    blocks.sort(key=lambda bl: (round(bl[0]["y"], 1), bl[0]["x0"]))
    events: list[tuple] = []
    for lines in blocks:
        # Join wrapped headings inside the block: consecutive same-class
        # lines with small y gap (size-20 with space, size-18 without).
        i = 0
        textblock: list[dict] = []
        while i < len(lines):
            ln = lines[i]
            sizes = ln["sizes"]
            cls = "h20" if 20.0 in sizes else ("h18" if 18.0 in sizes else None)
            if cls is not None:
                if textblock:
                    events.append(("textblock", textblock))
                    textblock = []
                parts = [ln["text"].strip()]
                y_prev = ln["y"]
                j = i + 1
                while j < len(lines):
                    nx = lines[j]
                    ncls = "h20" if 20.0 in nx["sizes"] else ("h18" if 18.0 in nx["sizes"] else None)
                    if ncls != cls or nx["y"] - y_prev >= WRAP_GAP:
                        break
                    parts.append(nx["text"].strip())
                    y_prev = nx["y"]
                    j += 1
                text = (" ".join(parts) if cls == "h20" else "".join(parts)).strip()
                if cls == "h20":
                    m = CHAPTER_RE.match(text)
                    if m:
                        events.append(("chapter", int(m.group(1)), text))
                    else:
                        events.append(("group", text))
                else:
                    if FUNC_RE.match(text):
                        events.append(("function", text))
                    else:
                        # Non-function size-18 heading (Related documents).
                        events.append(("heading18", text))
                i = j
            else:
                textblock.append(ln)
                i += 1
        if textblock:
            events.append(("textblock", textblock))
    return events, printed_no


def scan_document(pdf_path: Path):
    """Scan the whole guide. Returns (functions, intro_pages, appendix_lines, stats).

    functions: list of dicts {name, chapter_num, chapter, group, pages,
    printed, linelets}. intro_pages: list of (events, printed_no) for the
    About..Chapter-3-start range. appendix_lines: raw text lines.
    """
    if pymupdf is None:
        raise RuntimeError("pymupdf is required (pip install pymupdf).")
    doc = pymupdf.open(str(pdf_path))
    functions: list[dict] = []
    intro_pages: list[tuple] = []
    appendix_lines: list[str] = []
    cur_chapter_num = 0
    cur_chapter = ""
    cur_group = "-"
    cur_func: dict | None = None
    in_appendix = False
    in_intro = False
    chapter3_started = False
    stats = {"pages": doc.page_count, "duplicates": []}
    seen: set[str] = set()

    def close_func() -> None:
        nonlocal cur_func
        cur_func = None

    for idx in range(doc.page_count):
        page = doc[idx]
        events, printed = iter_page_events(page)
        printed_no = printed if printed is not None else idx + 1
        page_intro: list[tuple] = []
        for ev in events:
            kind = ev[0]
            if kind == "chapter":
                _k, num, title = ev
                if "Appendix" in title:
                    in_appendix = True
                    in_intro = False
                    close_func()
                    continue
                cur_chapter_num = num
                cur_chapter = title
                cur_group = "-"
                close_func()
                if num == 1:
                    in_intro = True
                if num >= 3:
                    chapter3_started = True
                if in_intro:
                    page_intro.append(ev)
            elif kind == "group":
                if ev[1] == "About this guide" and not chapter3_started:
                    in_intro = True
                if ev[1].startswith("Appendix"):
                    in_appendix = True
                    in_intro = False
                    close_func()
                    appendix_lines.append(ev[1])
                    continue
                if in_appendix:
                    appendix_lines.append(ev[1])
                    continue
                cur_group = ev[1]
                close_func()
                if in_intro and not in_appendix:
                    page_intro.append(ev)
            elif kind == "function":
                name = ev[1]
                close_func()
                if in_appendix:
                    continue
                # Function titles inside Chapters 1-2 belong to BOTH the
                # intro narrative (rendered inline) and per-function files.
                # Titles in Chapter 3+ end the intro range.
                if chapter3_started and cur_chapter_num >= 3:
                    in_intro = False
                if in_intro and not in_appendix:
                    page_intro.append(ev)
                if (cur_chapter_num, name) in seen:
                    stats["duplicates"].append(name)
                    cur_func = None
                    continue
                seen.add((cur_chapter_num, name))
                cur_func = {"name": name, "chapter_num": cur_chapter_num,
                            "chapter": cur_chapter, "group": cur_group,
                            "pages": [idx], "printed": [printed_no],
                            "linelets": []}
                functions.append(cur_func)
            elif kind == "heading18":
                close_func()
                if in_appendix:
                    appendix_lines.append(ev[1])
                    continue
                if in_intro and not in_appendix:
                    page_intro.append(ev)
            elif kind == "textblock":
                if in_appendix:
                    for ln in ev[1]:
                        appendix_lines.append(ln["text"])
                else:
                    if cur_func is not None:
                        for ln in ev[1]:
                            cur_func["linelets"].append(
                                {"y": ln["y"], "x0": ln["x0"],
                                 "x1": ln["x1"], "text": ln["text"],
                                 "page": idx})
                        if idx not in cur_func["pages"]:
                            cur_func["pages"].append(idx)
                            cur_func["printed"].append(printed_no)
                    if in_intro and not in_appendix:
                        page_intro.append(ev)
        if page_intro:
            intro_pages.append((page_intro, printed_no))
    doc.close()
    return functions, intro_pages, appendix_lines, stats


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def render_function(func: dict) -> str:
    # Row-join per page: y-coordinates restart on every page, so linelets
    # from different pages must never merge into one row.
    by_page: dict[int, list[dict]] = {}
    for ln in func["linelets"]:
        by_page.setdefault(ln["page"], []).append(ln)
    body: list[str] = []
    for page_no in sorted(by_page):
        body.extend(join_same_row(by_page[page_no]))
    start, end = min(func["printed"]), max(func["printed"])
    lines = ["# %s" % func["name"], "",
             "> Chapter: %s" % func["chapter"],
             ">",
             "> Group: %s" % func["group"],
             ">",
             "> Source: %s, pp. %d-%d" % (GUIDE_TITLE, start, end),
             "",
             "```baan"]
    lines.extend(body)
    lines.append("```")
    return "\n".join(lines).rstrip() + "\n"


def render_introduction(intro_events: list[tuple], start: int, end: int) -> str:
    lines = ["# Introduction", "",
             "> Chapter: Chapter 1 Introduction",
             ">",
             "> Group: -",
             ">",
             "> Source: %s, pp. %d-%d" % (GUIDE_TITLE, start, end),
             ""]
    # Flatten to a simple stream: headings, paragraphs, courier runs.
    pending_courier: list[str] = []
    func_lines: list[str] | None = None

    def flush_courier() -> None:
        if pending_courier:
            lines.append("```baan")
            lines.extend(r for r in pending_courier if r.strip())
            lines.append("```")
            lines.append("")
            pending_courier.clear()

    def flush_func() -> None:
        nonlocal func_lines, prev
        if func_lines is not None:
            rows = [r for r in func_lines if r.strip()]
            if rows:
                lines.append("```baan")
                lines.extend(rows)
                lines.append("```")
                lines.append("")
            func_lines = None
            prev = "code"

    def heading(text: str) -> None:
        flush_func()
        if pending_courier:
            flush_courier()
        if lines and lines[-1].strip():
            lines.append("")
        lines.append("## %s" % text)
        lines.append("")

    prev = "start"
    for ev in intro_events:
        kind = ev[0]
        if kind in ("chapter", "group", "heading18"):
            heading(ev[-1])
            prev = "heading"
        elif kind == "function":
            flush_func()
            flush_courier()
            if lines and lines[-1].strip():
                lines.append("")
            lines.append("## %s" % ev[1])
            lines.append("")
            func_lines = []
            prev = "heading"
        elif kind == "codeblock":
            if func_lines is not None:
                func_lines.extend(ev[1])
            else:
                flush_courier()
                lines.append("```baan")
                lines.extend(r for r in ev[1] if r.strip())
                lines.append("```")
                lines.append("")
            prev = "code"
        elif kind == "para":
            if func_lines is not None:
                func_lines.append(ev[1])
            else:
                flush_courier()
                if prev in ("code", "func"):
                    if lines and lines[-1].strip():
                        lines.append("")
                lines.append(ev[1])
                prev = "para"
    flush_func()
    flush_courier()
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines).rstrip() + "\n"


def intro_text_rows(intro_pages: list[tuple]) -> tuple[list[tuple], int, int]:
    """Flatten intro pages to render events + printed page span.

    Emits ("para", text) per narrative block (wrapped rows joined),
    ("codeblock", [rows]) for courier blocks, passing headings through.
    """
    flat: list[tuple] = []
    numbers: list[int] = []
    for events, printed in intro_pages:
        numbers.append(printed)
        for ev in events:
            if ev[0] != "textblock":
                flat.append(ev)
                continue
            linelets = [{"y": ln["y"], "x0": ln["x0"], "x1": ln["x1"],
                         "text": ln["text"]} for ln in ev[1]]
            cour = [_is_courier(ln["fonts"]) for ln in ev[1]]
            rows = join_same_row(linelets)
            rows = [r for r in rows if r.strip()]
            if not rows:
                continue
            if all(cour):
                flat.append(("codeblock", rows))
            else:
                flat.append(("para", " ".join(r.strip() for r in rows)))
    span = (min(numbers), max(numbers)) if numbers else (0, 0)
    # Merge "available functions" listings: legacy narrative joins the
    # intro line with the following single-token names on one line.
    merged: list[tuple] = []
    idx = 0
    while idx < len(flat):
        ev = flat[idx]
        if (ev[0] == "para" and ev[1].rstrip().endswith("available:")
                and idx + 1 < len(flat) and flat[idx + 1][0] == "para"
                and FUNC_RE.match(flat[idx + 1][1].strip())):
            parts = [ev[1].strip()]
            idx += 1
            while idx < len(flat) and flat[idx][0] == "para" \
                    and FUNC_RE.match(flat[idx][1].strip()):
                parts.append(flat[idx][1].strip())
                idx += 1
            merged.append(("para", " ".join(parts)))
        else:
            merged.append(ev)
            idx += 1
    return merged, span[0], span[1]


def render_release_history(title_lines: list[str], interfaces: list[tuple[str, list[str]]],
                           extensions: list[tuple[str, list[str]]],
                           start: int, end: int) -> str:
    title = " ".join(title_lines).strip() or "Appendix A - Public Interfaces and Process Extensions per Infor LN Cloud release"
    title = re.sub(r"\s+", " ", title)
    lines = ["# %s" % title, "",
             "> Chapter: Appendix",
             ">",
             "> Group: -",
             ">",
             "> Source: %s, pp. %d-%d" % (GUIDE_TITLE, start, end),
             "",
             "## Public Interfaces",
             "",
             "The following table shows the Infor LN Cloud releases in which new Public Interfaces were released:",
             ""]
    for release, items in interfaces:
        lines.append("### %s" % release)
        lines.append("")
        for item in items:
            lines.append("- %s" % item)
        lines.append("")
    lines.append("## Process Extensions")
    lines.append("")
    lines.append("The following table shows the Infor LN Cloud releases in which new Process Extensions were released:")
    lines.append("")
    for release, items in extensions:
        lines.append("### %s" % release)
        lines.append("")
        for item in items:
            lines.append("- %s" % item)
        lines.append("")
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def convert_pdf(pdf_path: Path, out_dir: Path) -> dict:
    stats: dict = {"functions": 0, "written": 0, "deleted": 0, "unchanged": 0}
    if pymupdf is None:
        raise RuntimeError("pymupdf is required (pip install pymupdf).")
    functions, intro_pages, appendix_lines, scan_stats = scan_document(pdf_path)
    stats.update(scan_stats)
    mapping = existing_chapter_dirs(out_dir)
    written: set[Path] = set()

    for func in functions:
        dirname = chapter_dirname(func["chapter_num"], func["chapter"], mapping)
        mapping.setdefault(func["chapter_num"], dirname)
        dest = out_dir / dirname / (sanitize_filename(func["name"]) + ".md")
        content = render_function(func)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.is_file() and dest.read_text(encoding="utf-8") == content:
            stats["unchanged"] += 1
        else:
            dest.write_text(content, encoding="utf-8")
        written.add(dest.resolve())
        stats["written"] += 1
    stats["functions"] = len(functions)

    # Introduction narrative.
    flat, start, end = intro_text_rows(intro_pages)
    intro_dest = out_dir / "ch01_introduction.md"
    intro_content = render_introduction(flat, start, end)
    if intro_dest.is_file() and intro_dest.read_text(encoding="utf-8") == intro_content:
        stats["unchanged"] += 1
    else:
        intro_dest.write_text(intro_content, encoding="utf-8")
    written.add(intro_dest.resolve())

    # Release history (Appendix A).
    title_lines, interfaces, extensions = parse_release_history(appendix_lines)
    doc = pymupdf.open(str(pdf_path))
    app_start = app_end = doc.page_count
    for i in range(doc.page_count):
        if "Appendix A" in doc[i].get_text():
            app_start = i + 1
            break
    doc.close()
    zz_dest = out_dir / "zz_release_history.md"
    zz_content = render_release_history(title_lines, interfaces, extensions,
                                        app_start, app_end)
    if zz_dest.is_file() and zz_dest.read_text(encoding="utf-8") == zz_content:
        stats["unchanged"] += 1
    else:
        zz_dest.write_text(zz_content, encoding="utf-8")
    written.add(zz_dest.resolve())
    stats["release_interfaces"] = sum(len(items) for _, items in interfaces)
    stats["release_extensions"] = sum(len(items) for _, items in extensions)

    # Delete stale files (mirror the new edition exactly).
    for existing in sorted(out_dir.rglob("*.md")):
        if existing.resolve() not in written:
            existing.unlink()
            stats["deleted"] += 1
    for sub in sorted(out_dir.iterdir()):
        if sub.is_dir() and not any(sub.iterdir()):
            sub.rmdir()
    return stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert Public Interfaces PDF to Markdown.")
    ap.add_argument("--pdf", required=True, help="input reference guide PDF")
    ap.add_argument("--out", required=True, help="output public_interfaces dir")
    args = ap.parse_args(argv)
    pdfs = sorted(glob.glob(args.pdf)) if any(c in args.pdf for c in "*?[") else [args.pdf]
    if not pdfs:
        ap.error("no PDF matched: %s" % args.pdf)
    total = {"functions": 0, "written": 0, "deleted": 0, "unchanged": 0}
    for pdf in pdfs:
        stats = convert_pdf(Path(pdf), Path(args.out))
        for k in total:
            total[k] += stats.get(k, 0)
        print("PDF conversion: functions=%d written=%d unchanged=%d deleted=%d "
              "release_ifaces=%d release_exts=%d duplicates=%r -> %s"
              % (stats["functions"], stats["written"], stats["unchanged"],
                 stats["deleted"], stats.get("release_interfaces", 0),
                 stats.get("release_extensions", 0),
                 stats.get("duplicates", []), args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
