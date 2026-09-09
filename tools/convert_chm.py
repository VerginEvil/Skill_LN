#!/usr/bin/env python3
"""Decompile Infor CHM help files and convert HTML topics to Markdown.

Usage:
    python tools/convert_chm.py --chm <file.chm> --out <refs/subdir>
    python tools/convert_chm.py --src-dir <decompiled/progguide> --out <refs/subdir>
    python tools/convert_chm.py --chm <file.chm> --out <refs/subdir> --workdir <tmp>

Only the Python standard library is used. Decompilation uses the native
Windows ``hh.exe -decompile`` with a synchronous wait (no third-party tools).

Output layout mirrors the decompiled ``progguide/`` tree, renaming
``*.htm`` to ``*.md`` so existing relative cross-links keep working
(rewritten ``.htm`` -> ``.md`` and normalized).
"""

from __future__ import annotations

import argparse
import html as htmlmod
import os
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path


# ---------------------------------------------------------------------------
# Link rewriting
# ---------------------------------------------------------------------------

def rewrite_href(href: str, src_file: Path, src_root: Path,
                 dst_file: Path, dst_root: Path) -> str | None:
    """Rewrite an HTML href found in *src_file* to a relative Markdown link.

    Returns the rewritten link, or None when the target cannot be mapped
    (caller should then render plain text).
    """
    if not href or href.startswith(("javascript:", "mailto:")):
        return None
    if href.startswith("#"):
        return href
    if href.startswith(("http:", "https:", "ftp:")):
        return href
    path_part, _sep, anchor = href.partition("#")
    if not path_part:
        return ("#" + anchor) if anchor else None
    target = os.path.normpath(os.path.join(str(src_file.parent), path_part))
    try:
        rel = os.path.relpath(target, str(src_root))
    except ValueError:
        return None
    if rel.startswith(".."):
        return None
    # Drop links dangling in the source itself (Infor ships a few
    # references to renamed/removed topics); the link text is kept.
    if Path(src_root).is_dir() and not os.path.exists(target):
        return None
    rel_path = Path(rel)
    if rel_path.suffix.lower() in (".htm", ".html"):
        rel_path = rel_path.with_suffix(".md")
    dst_target = dst_root / rel_path
    link = os.path.relpath(str(dst_target), str(dst_file.parent)).replace(os.sep, "/")
    if anchor:
        link += "#" + anchor
    return link


# ---------------------------------------------------------------------------
# HTML -> Markdown parser
# ---------------------------------------------------------------------------

_WS_RE = re.compile(r"\s+")
# Zero-width / BOM format characters (e.g. &#8203; in Infor sources) break
# Windows console output and add nothing for readers or grep.
_FORMAT_CHARS_RE = re.compile("[\u200b\u200c\u200d\ufeff]")


def _clean_text(text: str) -> str:
    text = htmlmod.unescape(text).replace("\xa0", " ")
    text = _FORMAT_CHARS_RE.sub("", text)
    return _WS_RE.sub(" ", text)


class _Inline:
    """Accumulates inline segments for one block-level element."""

    def __init__(self) -> None:
        self.parts: list[tuple] = []

    def add_text(self, s: str) -> None:
        s = _clean_text(s)
        if s:
            self.parts.append(("text", s))

    def add_code(self, s: str) -> None:
        s = _clean_text(s).strip()
        if s:
            self.parts.append(("code", s))

    def add_link(self, text: str, href: str | None) -> None:
        text = _clean_text(text).strip()
        if not text:
            return
        self.parts.append(("link", text, href))

    def add_em(self, s: str) -> None:
        s = _clean_text(s).strip()
        if s:
            self.parts.append(("em", s))

    def add_strong(self, s: str) -> None:
        s = _clean_text(s).strip()
        if s:
            self.parts.append(("strong", s))

    def render(self) -> str:
        out: list[str] = []
        for p in self.parts:
            kind = p[0]
            if kind == "text":
                out.append(p[1])
            elif kind == "code":
                out.append("`%s`" % p[1])
            elif kind == "link":
                text, href = p[1], p[2]
                text = text.replace("[", "\\[").replace("]", "\\]")
                if href:
                    out.append("[%s](%s)" % (text, href))
                else:
                    out.append(text)
            elif kind == "em":
                out.append("*%s*" % p[1])
            elif kind == "strong":
                out.append("**%s**" % p[1])
        text = _WS_RE.sub(" ", "".join(out)).strip()
        # Remove space before , . ; : left by tag boundaries.
        # (Parentheses keep their spaces: legacy signatures use `( )`.)
        text = re.sub(r" ([,.;:])", r"\1", text)
        return text


class TopicParser(HTMLParser):
    """Parses one Infor help HTML topic into Markdown blocks."""

    def __init__(self, src_file: Path, src_root: Path, dst_file: Path, dst_root: Path) -> None:
        super().__init__(convert_charrefs=False)
        self.src_file = src_file
        self.src_root = src_root
        self.dst_file = dst_file
        self.dst_root = dst_root
        self.topic_title = ""
        self._in_title_div = False
        self.sections: list[dict] = []
        self._current: dict | None = None
        self._para: _Inline | None = None
        self._in_pre = False
        self._pre_buf: list[str] = []
        self._in_table = False
        self._table_rows: list[list[str]] = []
        self._pending_cells: list[str] = []
        self._in_cell = False
        self._cell: _Inline | None = None
        self._in_li = False
        self._li: _Inline | None = None
        self._in_related = False
        self._in_related_title = False
        self.related: list[tuple[str, str | None]] = []
        self._in_code = False
        self._code_buf: list[str] = []
        self._in_em = False
        self._in_strong = False
        self._in_link = False
        self._link_href: str | None = None
        self._link_buf: list[str] = []
        # Skip stack for feedback tables/links ("noborder" / "FeedbackLink").
        self._skip_stack: list[str] = []
        self._in_subsection_title = False
        self._subsection_buf: list[str] = []
        self._in_note = 0
        self.note_title = ""
        self._note_open = False
        self._note_done = False
        self._in_note_title = False
        self._note_title_buf: list[str] = []
        self._div_stack: list[str] = []

    # -- helpers ---------------------------------------------------------
    def _ensure_section(self) -> dict:
        if self._current is None:
            self._current = {"title": None, "blocks": []}
            self.sections.append(self._current)
        return self._current

    def _active_inline(self) -> _Inline | None:
        if self._in_cell and self._cell is not None:
            return self._cell
        if self._in_li and self._li is not None:
            return self._li
        return self._para

    def _maybe_prefix_note(self, text: str) -> str:
        """Prefix the first paragraph of a Note div with its title.

        Legacy output renders notes inline (``Notes  <text>``) instead of a
        separate heading; this reproduces that layout.
        """
        if self._note_open and not self._note_done and self.note_title:
            self._note_done = True
            return "%s  %s" % (self.note_title, text)
        return text

    def _emit_text(self, data: str) -> None:
        if self._skip_stack or self._in_related_title:
            return
        if self._in_pre:
            self._pre_buf.append(data)
            return
        if self._in_link:
            self._link_buf.append(data)
            return
        if self._in_code:
            self._code_buf.append(data)
            return
        target = self._active_inline()
        if target is None:
            if not data.strip():
                return
            self._ensure_section()
            self._para = _Inline()
            target = self._para
        if self._in_em:
            target.add_em(data)
        elif self._in_strong:
            target.add_strong(data)
        else:
            target.add_text(data)

    def _flush_code(self) -> None:
        if not self._in_code:
            return
        self._in_code = False
        text = _clean_text("".join(self._code_buf))
        self._code_buf = []
        target = self._active_inline()
        if target is None:
            if not text.strip():
                return
            self._ensure_section()
            self._para = _Inline()
            target = self._para
        if self._in_link:
            self._link_buf.append("`%s`" % text.strip())
        else:
            target.add_code(text)

    # -- HTMLParser overrides --------------------------------------------
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        at = dict(attrs)
        cls = (at.get("class") or "")
        if tag == "div":
            self._div_stack.append(cls)
            if cls == "TopicTitle":
                self._in_title_div = True
            elif cls == "subSectionTitle":
                self._in_subsection_title = True
                self._subsection_buf = []
            elif cls == "Note":
                self._in_note += 1
                self._note_open = True
                self._note_done = False
            elif cls == "NoteSectionTitle":
                self._in_note_title = True
                self._note_title_buf = []
            elif cls == "RelatedTopics":
                self._in_related = True
            elif cls in ("GeneralSection", "ExampleSection"):
                self._ensure_section()
        elif tag == "p":
            if cls == "RelatedTopicsSectionTitle":
                self._in_related_title = True
                return
            if self._skip_stack:
                return
            if self._in_cell or self._in_li:
                return  # cell/li text flows into their inline accumulators
            self._para = _Inline()
        elif tag == "pre":
            if not self._skip_stack:
                self._in_pre = True
                self._pre_buf = []
        elif tag == "table":
            if "noborder" in cls:
                self._skip_stack.append("table")
                return
            if not self._skip_stack:
                self._in_table = True
                self._table_rows = []
                self._pending_cells = []
        elif tag in ("td", "th"):
            if self._skip_stack:
                return
            self._in_cell = True
            self._cell = _Inline()
        elif tag == "li":
            if self._skip_stack:
                return
            self._in_li = True
            self._li = _Inline()
        elif tag == "code":
            if not self._skip_stack:
                self._in_code = True
                self._code_buf = []
        elif tag in ("i", "em"):
            self._in_em = True
        elif tag in ("b", "strong"):
            self._in_strong = True
        elif tag == "a":
            href = at.get("href") or ""
            if "FeedbackLink" in cls or href.startswith("mailto:"):
                self._skip_stack.append("link")
                self._in_link = True
                self._link_buf = []
                self._link_href = None
                return
            if self._skip_stack:
                return
            self._link_href = rewrite_href(href, self.src_file, self.src_root,
                                           self.dst_file, self.dst_root)
            self._in_link = True
            self._link_buf = []
        elif tag == "br":
            if self._skip_stack:
                return
            if self._in_link:
                self._link_buf.append(" ")
            elif self._in_code:
                self._code_buf.append(" ")
            else:
                target = self._active_inline()
                if target is not None:
                    target.add_text(" ")
        # img, link, meta, etc. are ignored.

    def handle_endtag(self, tag: str) -> None:
        if tag == "div":
            cls = self._div_stack.pop() if self._div_stack else ""
            if cls == "TopicTitle":
                self._in_title_div = False
            elif cls == "subSectionTitle":
                self._in_subsection_title = False
                title = _clean_text("".join(self._subsection_buf)).strip()
                self._current = {"title": title, "blocks": []}
                self.sections.append(self._current)
            elif cls == "NoteSectionTitle":
                self._in_note_title = False
                self.note_title = _clean_text("".join(self._note_title_buf)).strip()
            elif cls == "Note":
                self._in_note = max(0, self._in_note - 1)
                if self._in_note == 0:
                    self._note_open = False
            elif cls == "RelatedTopics":
                self._in_related = False
                self._in_related_title = False
        elif tag == "p":
            if self._in_related_title:
                self._in_related_title = False
                return
            if self._para is not None:
                text = self._para.render()
                self._para = None
                if text and text != "&nbsp;":
                    text = self._maybe_prefix_note(text)
                    self._ensure_section()["blocks"].append(("para", text))
        elif tag == "pre":
            if self._in_pre:
                self._in_pre = False
                code = htmlmod.unescape("".join(self._pre_buf)).replace("\xa0", " ")
                code = _FORMAT_CHARS_RE.sub("", code)
                code = code.replace("\r\n", "\n").replace("\r", "\n")
                # Drop trailing blank lines but keep the raw leading blank
                # line: single-line <pre> renders tight, multi-line <pre>
                # keeps a blank line after the opening fence (legacy layout).
                code_lines = code.split("\n")
                while code_lines and not code_lines[-1].strip():
                    code_lines.pop()
                if any(ln.strip() for ln in code_lines):
                    self._ensure_section()["blocks"].append(("code", "\n".join(code_lines)))
                self._pre_buf = []
        elif tag == "table":
            if self._skip_stack and self._skip_stack[-1] == "table":
                self._skip_stack.pop()
                return
            if self._in_table:
                self._in_table = False
                rows = [r for r in self._table_rows if any(c.strip() for c in r)]
                if rows:
                    self._ensure_section()["blocks"].append(("table", rows))
                self._table_rows = []
                self._pending_cells = []
        elif tag in ("td", "th"):
            if self._in_cell and self._cell is not None:
                self._pending_cells.append(self._cell.render())
                self._cell = None
            self._in_cell = False
        elif tag == "tr":
            if self._in_table:
                self._table_rows.append(self._pending_cells)
                self._pending_cells = []
        elif tag == "li":
            if self._in_li and self._li is not None:
                text = self._li.render()
                if text and not self._in_related:
                    self._ensure_section()["blocks"].append(("bullet", text))
                self._li = None
            self._in_li = False
        elif tag == "code":
            self._flush_code()
        elif tag in ("i", "em"):
            self._in_em = False
        elif tag in ("b", "strong"):
            self._in_strong = False
        elif tag == "a":
            if self._skip_stack and self._skip_stack[-1] == "link":
                self._skip_stack.pop()
                self._in_link = False
                self._link_buf = []
                self._link_href = None
                return
            if not self._in_link:
                return
            self._in_link = False
            text = _clean_text("".join(self._link_buf))
            href = self._link_href
            self._link_buf = []
            self._link_href = None
            if self._in_related:
                if text.strip():
                    self.related.append((text.strip(), href))
                return
            target = self._active_inline()
            if target is not None:
                target.add_link(text, href)

    def handle_data(self, data: str) -> None:
        if self._in_title_div:
            self.topic_title += _clean_text(data)
            return
        if self._in_subsection_title:
            self._subsection_buf.append(data)
            return
        if self._in_note_title:
            self._note_title_buf.append(data)
            return
        if self._in_related_title:
            return
        if self._skip_stack and not self._in_link:
            return
        if not data.strip() and not self._in_pre:
            if self._in_link:
                self._link_buf.append(" ")
                return
            if self._in_code:
                self._code_buf.append(" ")
                return
            target = self._active_inline()
            if target is not None:
                target.add_text(" ")
            return
        self._emit_text(data)

    def handle_entityref(self, name: str) -> None:
        self._emit_text("&%s;" % name)

    def handle_charref(self, name: str) -> None:
        self._emit_text("&#%s;" % name)


def _render_table(rows: list[list[str]]) -> list[str]:
    ncols = max(len(r) for r in rows)
    norm = [list(r) + [""] * (ncols - len(r)) for r in rows]
    out = ["|" + " |" * ncols,
           "|" + "|".join(["---"] * ncols) + "|"]
    for r in norm:
        cells = [c.strip() for c in r]
        if ncols == 3 and cells[0].startswith("`") and cells[1].startswith("`"):
            # Legacy layout double-pads the description column of
            # Arguments tables.
            out.append("| %s | %s |  %s  |" % (cells[0], cells[1], cells[2]))
        else:
            out.append("| " + " | ".join(cells) + " |")
    return out


def _render_blocks(sections: list[dict], related: list[tuple[str, str | None]],
                   title: str) -> list[str]:
    """Render parsed sections using the established skill layout.

    Conventions (match the existing reference files so regenerated pages
    blend in): no blank line after ``##`` headings, no blank between
    consecutive paragraphs, blank line before a heading, blank-separated
    related-topic bullets, code fences preserving the raw leading blank
    line from the HTML ``<pre>`` source.
    """
    lines: list[str] = ["# %s" % title]
    prev = "title"

    def need_blank_before_heading() -> None:
        if lines and lines[-1].strip():
            lines.append("")

    def emit_bullets(items: list[str]) -> None:
        nonlocal prev
        if prev not in ("heading", "title") and lines[-1].strip():
            lines.append("")
        for i, item in enumerate(items):
            if i:
                lines.append("")
            lines.append("- %s" % item)
        prev = "list"

    for sec in sections:
        if sec["title"]:
            need_blank_before_heading()
            lines.append("## %s" % sec["title"])
            prev = "heading"
        pending_bullets: list[str] = []
        for block in sec["blocks"]:
            kind = block[0]
            if kind == "bullet":
                pending_bullets.append(block[1])
                continue
            if pending_bullets:
                emit_bullets(pending_bullets)
                pending_bullets = []
            if kind == "para":
                # No blank before plain paragraphs (legacy layout); except
                # after a list, where GFM would otherwise merge the text
                # into the last item via lazy continuation.
                if prev == "list":
                    lines.append("")
                lines.append(block[1])
                prev = "para"
            elif kind == "code":
                lines.append("```")
                lines.extend(block[1].split("\n"))
                lines.append("```")
                prev = "code"
            elif kind == "table":
                lines.extend(_render_table(block[1]))
                prev = "table"
        if pending_bullets:
            emit_bullets(pending_bullets)
    if related:
        need_blank_before_heading()
        lines.append("## Related topics")
        items = []
        for text, href in related:
            if href:
                items.append("[%s](%s)" % (text, href))
            elif text.startswith("["):
                items.append(text)
            else:
                items.append(text)
        lines.append("- %s" % items[0])
        for item in items[1:]:
            lines.append("")
            lines.append("- %s" % item)
    return lines


def convert_html_string(html_text: str, src_file: Path, src_root: Path,
                        dst_file: Path, dst_root: Path) -> str:
    """Convert one HTML topic string to a Markdown document."""
    parser = TopicParser(src_file, src_root, dst_file, dst_root)
    parser.feed(html_text)
    parser.close()
    title = _clean_text(parser.topic_title).strip() or dst_file.stem
    lines = _render_blocks(parser.sections, parser.related, title)
    # Collapse 3+ blank lines, strip trailing blanks.
    cleaned: list[str] = []
    blanks = 0
    for ln in lines:
        if ln.strip():
            blanks = 0
            cleaned.append(ln.rstrip())
        else:
            blanks += 1
            if blanks <= 1:
                cleaned.append("")
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    return "\n".join(cleaned) + "\n"


def convert_file(src_html: Path, src_root: Path, dst_md: Path, dst_root: Path) -> bool:
    """Convert a single HTML file; returns True when written."""
    raw = src_html.read_bytes()
    html_text = None
    for enc in ("utf-8", "windows-1252", "cp1252", "latin-1"):
        try:
            html_text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if html_text is None:
        return False
    md = convert_html_string(html_text, src_html, src_root, dst_md, dst_root)
    dst_md.parent.mkdir(parents=True, exist_ok=True)
    dst_md.write_text(md, encoding="utf-8")
    return True


def find_progguide_root(decompiled: Path) -> Path:
    """Locate the ``progguide`` content root inside a decompiled CHM tree."""
    cand = decompiled / "progguide"
    if cand.is_dir():
        return cand
    for sub in sorted(decompiled.rglob("progguide")):
        if sub.is_dir():
            return sub
    return decompiled


def convert_tree(src_root: Path, dst_root: Path) -> dict:
    """Convert every ``*.htm(l)`` under *src_root* into ``*.md`` under *dst_root*."""
    stats = {"found": 0, "written": 0, "skipped": 0}
    html_files = sorted(list(src_root.rglob("*.htm")) + list(src_root.rglob("*.html")))
    stats["found"] = len(html_files)
    for src in html_files:
        rel = src.relative_to(src_root)
        dst = (dst_root / rel).with_suffix(".md")
        try:
            if convert_file(src, src_root, dst, dst_root):
                stats["written"] += 1
            else:
                stats["skipped"] += 1
        except Exception as exc:  # noqa: BLE001 - report and continue
            print("WARN: failed %s: %s" % (src, exc), file=sys.stderr)
            stats["skipped"] += 1
    return stats


def decompile_chm(chm_path: Path, workdir: Path) -> Path:
    """Decompile *chm_path* with native ``hh.exe`` (synchronous) into *workdir*.

    Returns the decompiled output directory. Raises on failure.
    """
    chm_path = chm_path.resolve()
    if not chm_path.is_file():
        raise FileNotFoundError("CHM not found: %s" % chm_path)
    hh = shutil.which("hh.exe") or shutil.which("hh")
    if not hh:
        raise RuntimeError("hh.exe not found on PATH; cannot decompile CHM files.")
    out_dir = workdir / chm_path.stem
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Synchronous process completion monitoring (equivalent of -Wait).
    proc = subprocess.run([hh, "-decompile", str(out_dir), str(chm_path)],
                          capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        raise RuntimeError("hh.exe failed (rc=%s): %s" % (proc.returncode, proc.stderr[:2000]))
    return out_dir


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert Infor CHM help to Markdown.")
    ap.add_argument("--chm", default=None, help="input .chm file to decompile + convert")
    ap.add_argument("--src-dir", default=None, help="already-decompiled content dir (skips hh.exe)")
    ap.add_argument("--out", required=True, help="output references subdir")
    ap.add_argument("--workdir", default=None, help="temp dir for decompilation")
    args = ap.parse_args(argv)

    if not args.chm and not args.src_dir:
        ap.error("provide --chm and/or --src-dir")
    dst_root = Path(args.out)
    total = {"found": 0, "written": 0, "skipped": 0}
    if args.src_dir:
        src_root = find_progguide_root(Path(args.src_dir))
        stats = convert_tree(src_root, dst_root)
        for k in total:
            total[k] += stats[k]
    if args.chm:
        import tempfile
        workdir = Path(args.workdir) if args.workdir else Path(tempfile.mkdtemp(prefix="chm_"))
        workdir.mkdir(parents=True, exist_ok=True)
        out_dir = decompile_chm(Path(args.chm), workdir)
        src_root = find_progguide_root(out_dir)
        stats = convert_tree(src_root, dst_root)
        for k in total:
            total[k] += stats[k]
    print("CHM conversion: found=%d written=%d skipped=%d -> %s"
          % (total["found"], total["written"], total["skipped"], dst_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
