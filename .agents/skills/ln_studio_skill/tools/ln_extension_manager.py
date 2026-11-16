#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_extension_manager.py
Local Infor LN Extension Modeler Lifecycle & Hook Extraction Engine.

Manages the authoring, ingestion, and hook-level partitioning of Infor LN extensions
outside the LN Studio workspace (under Git control) in compliance with ADR 0006:
  - 'new-extension': Scaffolds standard local project extension 4GL scripts from official templates.
  - 'import-extension': Ingests extension components pulled from server into LN Studio "Get" cache.
  - 'extension-hooks': Parses #context_on blocks, lists hooks, and extracts/copies clean hook code
    to OS clipboard for 1-click paste into LN UI (ttext1500m000).
"""

import os
import sys
import re
import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple, Union

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_TOOLS_DIR = Path(__file__).resolve().parent
_TEMPLATES_DIR = _SKILL_ROOT / "templates"
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from inject_ln_script import extract_script_from_xml, unescape_xml_to_4gl

CONTEXT_ON_REGEX = re.compile(r'^\s*#context_on\s+["\']([^"\']+)["\']', re.IGNORECASE)
CONTEXT_OFF_REGEX = re.compile(r'^\s*#context_off\b', re.IGNORECASE)


class HookBlock:
    """Represents a single #context_on ... #context_off hook block."""

    def __init__(self, name: str, start_line: int, end_line: int, lines: List[str]):
        self.name = name
        self.start_line = start_line
        self.end_line = end_line
        self.lines = lines

    @property
    def clean_code(self) -> str:
        """Returns the hook code stripped of #context_on and #context_off wrappers."""
        code_lines = []
        for line in self.lines:
            if CONTEXT_ON_REGEX.match(line) or CONTEXT_OFF_REGEX.match(line):
                continue
            code_lines.append(line)
        joined = "\n".join(code_lines)
        return joined.strip("\r\n") + "\n"

    @property
    def code_lines_count(self) -> int:
        """Returns number of non-wrapper lines in this hook."""
        return sum(1 for line in self.lines if not CONTEXT_ON_REGEX.match(line) and not CONTEXT_OFF_REGEX.match(line))


def find_project_root(start_path: Optional[Path] = None) -> Path:
    """Finds repository root by searching upwards for .git, docs, or SKILL_ROOT parent."""
    curr = (start_path or Path.cwd()).resolve()
    while curr and curr != curr.parent:
        if (curr / ".git").exists() or (curr / "ln_studio_skill").exists():
            return curr
        curr = curr.parent
    return Path.cwd().resolve()


def copy_to_clipboard(text: str) -> bool:
    """Copies text to the system clipboard across Windows/macOS/Linux."""
    # 1. Windows clip.exe
    if sys.platform == "win32":
        try:
            proc = subprocess.Popen(["clip.exe"], stdin=subprocess.PIPE, close_fds=True)
            proc.communicate(text.encode("utf-16le"))
            if proc.returncode == 0:
                return True
        except Exception:
            pass

        # 2. Windows PowerShell fallback
        try:
            subprocess.run(
                ["powershell", "-NoProfile", "-Command", "$input | Set-Clipboard"],
                input=text,
                text=True,
                check=True,
                capture_output=True
            )
            return True
        except Exception:
            pass

    # 3. macOS pbcopy
    if sys.platform == "darwin":
        try:
            subprocess.run(["pbcopy"], input=text.encode("utf-8"), check=True)
            return True
        except Exception:
            pass

    # 4. Linux xclip / wl-copy
    for clip_cmd in (["wl-copy"], ["xclip", "-selection", "clipboard"]):
        try:
            subprocess.run(clip_cmd, input=text.encode("utf-8"), check=True)
            return True
        except Exception:
            pass

    # 5. Tkinter fallback
    try:
        import tkinter as tk
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()
        return True
    except Exception:
        pass

    return False


def new_extension(
    ext_type: str,
    target: str,
    output_path: Optional[Union[str, Path]] = None,
    author: str = "Developer",
    project_root: Optional[Path] = None
) -> Path:
    """
    Scaffolds a new local extension 4GL file from official templates.
    ext_type: 'table' or 'session'
    target: Component code (e.g., 'whwmd400', 'whwmd4300m000')
    """
    ext_type_norm = ext_type.lower().strip()
    if ext_type_norm in ("table", "tbl", "table_extension", "est"):
        ext_type_norm = "table"
        template_file = _TEMPLATES_DIR / "table_extension_template.4gl"
    elif ext_type_norm in ("session", "ses", "session_extension", "ess"):
        ext_type_norm = "session"
        template_file = _TEMPLATES_DIR / "session_extension_template.4gl"
    else:
        raise ValueError(f"Unsupported extension type: '{ext_type}'. Expected 'table' or 'session'.")

    if not template_file.exists():
        raise FileNotFoundError(f"Template file not found: {template_file}")

    content = template_file.read_text(encoding="utf-8")
    now_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Render template variables
    rendered = (
        content.replace("{target}", target)
        .replace("{author}", author)
        .replace("{date}", now_date)
    )

    if output_path:
        out_p = Path(output_path).resolve()
    else:
        root = project_root or find_project_root()
        out_p = (root / "extensions" / ext_type_norm / f"{target}_ext.4gl").resolve()

    out_p.parent.mkdir(parents=True, exist_ok=True)
    out_p.write_text(rendered, encoding="utf-8")

    return out_p


def infer_extension_metadata(source_path: Path, raw_text: str) -> Tuple[str, str]:
    """Infers extension type ('table' or 'session') and target component code."""
    stem = source_path.stem.lower()

    ext_type = "table"
    target = stem

    # Check source type in XML if present
    if "<sourceType>8</sourceType>" in raw_text or "bic_sessionext" in raw_text:
        ext_type = "session"
    elif "<sourceType>6</sourceType>" in raw_text or "bic_tableext" in raw_text or "bic_dal2" in raw_text:
        ext_type = "table"

    # Infer from filename prefixes
    if stem.startswith("txest"):
        ext_type = "table"
        target = stem[5:]
    elif stem.startswith("txess"):
        ext_type = "session"
        target = stem[5:]
    elif "est" in source_path.parts:
        ext_type = "table"
        if stem.startswith("tx"):
            target = stem[2:]
    elif "ess" in source_path.parts:
        ext_type = "session"
        if stem.startswith("tx"):
            target = stem[2:]

    # Remove trailing _ext or similar if present
    if target.endswith("_ext"):
        target = target[:-4]

    return ext_type, target


def import_extension(
    source: Union[str, Path],
    output_path: Optional[Union[str, Path]] = None,
    ext_type: Optional[str] = None,
    project_root: Optional[Path] = None
) -> Path:
    """
    Imports an extension script from LN Studio activity workspace (pulled via 'Get'),
    normalizing #context_on blocks into standard local project format.
    """
    src_p = Path(source).resolve()
    if not src_p.exists():
        raise FileNotFoundError(f"Source file does not exist: {src_p}")

    raw_content = src_p.read_text(encoding="utf-8")

    # If XML (.lib), extract script from <expression>
    if src_p.suffix.lower() == ".lib" or "<DR_Module>" in raw_content:
        script_code = extract_script_from_xml(raw_content)
        if not script_code:
            raise ValueError(f"No <expression> 4GL script found in '{src_p}'")
    else:
        script_code = raw_content

    inferred_type, target = infer_extension_metadata(src_p, raw_content)
    final_type = (ext_type or inferred_type).lower().strip()

    if output_path:
        out_p = Path(output_path).resolve()
    else:
        root = project_root or find_project_root()
        out_p = (root / "extensions" / final_type / f"{target}_ext.4gl").resolve()

    # Normalize script: ensure clean line endings
    normalized = "\n".join(line.rstrip() for line in script_code.splitlines()).strip() + "\n"

    out_p.parent.mkdir(parents=True, exist_ok=True)
    out_p.write_text(normalized, encoding="utf-8")

    return out_p


def parse_extension_hooks(file_path_or_content: Union[str, Path]) -> List[HookBlock]:
    """Parses all #context_on ... #context_off hook blocks from file or string."""
    if isinstance(file_path_or_content, Path) or (isinstance(file_path_or_content, str) and "\n" not in file_path_or_content and Path(file_path_or_content).exists()):
        text = Path(file_path_or_content).read_text(encoding="utf-8")
    else:
        text = str(file_path_or_content)

    lines = text.splitlines()
    hooks: List[HookBlock] = []

    curr_name: Optional[str] = None
    curr_start: int = 0
    curr_lines: List[str] = []

    for line_idx, line in enumerate(lines, start=1):
        m_on = CONTEXT_ON_REGEX.match(line)
        if m_on:
            if curr_name is not None:
                # Nested or unclosed block
                hooks.append(HookBlock(curr_name, curr_start, line_idx - 1, curr_lines))
            curr_name = m_on.group(1).strip()
            curr_start = line_idx
            curr_lines = [line]
            continue

        if CONTEXT_OFF_REGEX.match(line):
            if curr_name is not None:
                curr_lines.append(line)
                hooks.append(HookBlock(curr_name, curr_start, line_idx, curr_lines))
                curr_name = None
                curr_lines = []
            continue

        if curr_name is not None:
            curr_lines.append(line)

    if curr_name is not None:
        hooks.append(HookBlock(curr_name, curr_start, len(lines), curr_lines))

    return hooks


def list_hooks(file_path_or_content: Union[str, Path]) -> List[Dict[str, Any]]:
    """Returns summary list of all hooks present in an extension file or content."""
    hooks = parse_extension_hooks(file_path_or_content)
    return [
        {
            "name": h.name,
            "start_line": h.start_line,
            "end_line": h.end_line,
            "code_lines": h.code_lines_count
        }
        for h in hooks
    ]


def get_hook(file_path_or_content: Union[str, Path], hook_name: str) -> Optional[HookBlock]:
    """Finds a specific hook block by name (case-insensitive)."""
    hooks = parse_extension_hooks(file_path_or_content)
    hook_name_norm = hook_name.lower().strip()
    for h in hooks:
        if h.name.lower().strip() == hook_name_norm:
            return h
    return None
