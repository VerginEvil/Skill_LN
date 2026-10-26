#!/usr/bin/env python3
"""
Standalone Baan 4GL & DAL Audit Engine

Statically audits Baan 4GL, DAL2, and UEDLL files against Infor LN Studio Build 0640
authoritative dictionaries, CloudSuite Multi-Tenant restrictions, DAL2 contracts,
and language caveats.

Zero external dependencies. Runs on pure Python 3.8+.
"""

import argparse
import difflib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

SEVERITY_LEVELS = {"INFO": 0, "WARNING": 1, "ERROR": 2}


class Diagnostic:
    def __init__(
        self,
        file: str,
        line: int,
        column: int,
        severity: str,
        code: str,
        message: str,
        snippet: str = "",
    ):
        self.file = file
        self.line = line
        self.column = column
        self.severity = severity.upper()
        self.code = code
        self.message = message
        self.snippet = snippet.strip()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file": self.file,
            "line": self.line,
            "column": self.column,
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "snippet": self.snippet,
        }

    def __str__(self) -> str:
        prefix = f"[{self.severity}] {self.code} {self.file}:{self.line}:{self.column}: {self.message}"
        if self.snippet:
            return f"{prefix}\n       -> {self.snippet}"
        return prefix


def load_syntax_dictionaries(skill_dir: Path) -> Dict[str, Any]:
    """Load syntax dictionaries from references/studio_syntax_completion.json or built-in defaults."""
    candidates = [
        skill_dir / "references" / "studio_syntax_completion.json",
        Path(__file__).resolve().parent.parent / "references" / "studio_syntax_completion.json",
        Path(__file__).resolve().parent.parent.parent / "ln_studio_skill" / "references" / "studio_syntax_completion.json",
    ]
    for c in candidates:
        if c.exists():
            try:
                return json.loads(c.read_text(encoding="utf-8"))
            except Exception:
                pass

    return {
        "program_sections": [
            "declaration:", "before.program:", "after.program:", "after.form.read:",
            "after.update.db.commit:", "before.display.object:", "before.new.object:",
            "on.error:", "functions:", "main.table.io:", "init.form:"
        ],
        "choice_sections": [
            "choice.abort.program:", "choice.update.db:", "choice.user.0:", "choice.user.1:",
            "choice.user.2:", "choice.user.3:", "choice.user.4:", "choice.user.5:",
            "choice.user.6:", "choice.user.7:", "choice.user.8:", "choice.user.9:",
            "choice.zoom:", "choice.end.program:", "choice.modify.set:", "choice.def.find:"
        ],
        "sub_sections": [
            "after.choice:", "after.delete:", "after.display.object:", "after.display:",
            "after.field:", "after.form:", "after.group:", "after.input:", "after.layout:",
            "after.read:", "after.rewrite:", "after.write:", "after.zoom:",
            "before.choice:", "before.delete:", "before.destroy.object:", "before.display.object:",
            "before.display:", "before.field:", "before.form:", "before.group:", "before.input:",
            "before.layout:", "before.open.object.set:", "before.read:", "before.rewrite:",
            "before.write:", "before.zoom:", "check.input:", "domain.error:", "init.field:",
            "init.form:", "init.group:", "on.choice:", "on.entry:", "on.exit:", "read.view:",
            "when.field.changes:"
        ],
        "dal_field_hook_suffixes": [
            {"suffix": ".is.never.applicable", "returnValue": "extern boolean", "arguments": ""},
            {"suffix": ".is.applicable", "returnValue": "extern boolean", "arguments": ""},
            {"suffix": ".is.readonly", "returnValue": "extern boolean", "arguments": ""},
            {"suffix": ".is.derived", "returnValue": "extern boolean", "arguments": ""},
            {"suffix": ".is.mandatory", "returnValue": "extern boolean", "arguments": ""},
            {"suffix": ".is.valid", "returnValue": "extern boolean", "arguments": ""},
            {"suffix": ".update", "returnValue": "extern void", "arguments": "long i.mode"},
            {"suffix": ".make.valid", "returnValue": "extern long", "arguments": "long i.mode"},
            {"suffix": ".check", "returnValue": "extern long", "arguments": "long has_changed"},
            {"suffix": ".set.defaults", "returnValue": "extern long", "arguments": "long has_changed"}
        ]
    }


def load_functions_db(skill_dir: Path) -> Dict[str, Any]:
    """Load functions database from index/functions_db.json."""
    candidates = [
        skill_dir / "index" / "functions_db.json",
        Path(__file__).resolve().parent.parent / "index" / "functions_db.json",
    ]
    for c in candidates:
        if c.exists():
            try:
                raw = json.loads(c.read_text(encoding="utf-8"))
                # Build lowercase lookup dict
                db_ci: Dict[str, Any] = {}
                for k, v in raw.items():
                    db_ci[k.lower()] = v
                return db_ci
            except Exception:
                pass
    return {}


def strip_4gl_comments_and_strings(line: str, in_multiline_doc: bool) -> Tuple[str, bool]:
    """Strip string literals and pipe comments from a line, preserving code structure."""
    line_lower = line.strip().lower()
    if in_multiline_doc:
        if "enddllusage" in line_lower or "endfunctionusage" in line_lower:
            return "", False
        return "", True

    if line_lower.startswith("dllusage") or line_lower.startswith("functionusage"):
        return "", True

    res: List[str] = []
    i = 0
    n = len(line)
    in_str = False
    str_char = ""

    while i < n:
        c = line[i]
        if in_str:
            if c == "\\" and i + 1 < n:
                i += 2
                continue
            if c == str_char:
                in_str = False
            i += 1
            continue

        if c in ('"', "'"):
            in_str = True
            str_char = c
            res.append(" ")
            i += 1
            continue

        if c == "|":
            break

        res.append(c)
        i += 1

    return "".join(res), False


class Auditor4GL:
    def __init__(
        self,
        skill_dir: Optional[Path] = None,
        cloud_mode: bool = False,
        min_severity: str = "INFO",
        strict: bool = False,
    ):
        if not skill_dir:
            skill_dir = Path(__file__).resolve().parent.parent

        self.skill_dir = skill_dir
        self.cloud_mode = cloud_mode
        self.min_severity_level = SEVERITY_LEVELS.get(min_severity.upper(), 0)
        self.strict = strict

        self.syntax_dict = load_syntax_dictionaries(skill_dir)
        self.functions_db = load_functions_db(skill_dir)

        self.program_sections = set(s.lower() for s in self.syntax_dict.get("program_sections", []))
        self.choice_sections = set(s.lower() for s in self.syntax_dict.get("choice_sections", []))
        self.sub_sections = set(s.lower() for s in self.syntax_dict.get("sub_sections", []))

        self.dal_field_hooks: Dict[str, Dict[str, str]] = {}
        for h in self.syntax_dict.get("dal_field_hook_suffixes", []):
            if isinstance(h, dict):
                sfx = h.get("suffix", "").lower()
                self.dal_field_hooks[sfx] = h
            elif isinstance(h, str):
                self.dal_field_hooks[h.lower()] = {"suffix": h}

        self.all_known_sections = sorted(
            list(self.program_sections) + list(self.choice_sections) + list(self.sub_sections)
        )

    def is_valid_section_header(self, token: str) -> bool:
        t = token.lower().strip()
        if not t.endswith(":"):
            return False

        if t in self.program_sections or t in self.choice_sections or t in self.sub_sections:
            return True

        # Dynamic valid sections
        if t.startswith("field.") or t.startswith("choice."):
            return True
        if re.match(r"^group\.[0-9a-zA-Z_]+:$", t):
            return True
        if re.match(r"^form\.[0-9a-zA-Z_]+:$", t):
            return True
        if t.startswith("zoom.from."):
            return True
        if re.match(r"^(header|detail|before|after)\.[0-9]+:$", t):
            return True

        return False

    def detect_archetype(self, file_path: str, content: str) -> str:
        """Detect archetype mode: 'dal2', 'uedll', or 'general'."""
        path_lower = file_path.lower()
        if path_lower.endswith(".dal") or path_lower.endswith(".dalsrc") or "dal2" in path_lower:
            return "dal2"
        if path_lower.endswith(".ue") or "uedll" in path_lower:
            return "uedll"

        # Content heuristics
        if "function extern long before.save.object" in content.lower() or "dal.set.error.message" in content.lower():
            return "dal2"
        if "ue.before.save" in content.lower() or "ue.after.save" in content.lower():
            return "uedll"

        return "general"

    def audit_content(
        self,
        content: str,
        file_path: str = "<stdin>",
        mode: Optional[str] = None,
    ) -> List[Diagnostic]:
        """Perform comprehensive static verification on 4GL script content."""
        if not mode or mode == "auto":
            mode = self.detect_archetype(file_path, content)

        diagnostics: List[Diagnostic] = []
        lines = content.splitlines()

        # Includes collection: `#include <header>` or `#include "header"`
        includes_found: Set[str] = set()
        for raw_line in lines:
            m_inc = re.match(r'^\s*#include\s+[<"]([a-zA-Z0-9_.]+)[>"]', raw_line)
            if m_inc:
                inc_name = m_inc.group(1).lower()
                if inc_name.endswith(".h"):
                    inc_name = inc_name[:-2]
                includes_found.add(inc_name)

        # Block balance tracking: (type, line_no)
        block_stack: List[Tuple[str, int]] = []
        context_stack: List[Tuple[str, int]] = []
        brace_stack: List[Tuple[str, int]] = []

        in_multiline_doc = False
        in_case_block = False
        current_func_name: Optional[str] = None
        current_func_hook_suffix: Optional[str] = None

        for line_no, raw_line in enumerate(lines, start=1):
            stripped = raw_line.strip()
            if not stripped:
                continue

            code_line, in_multiline_doc = strip_4gl_comments_and_strings(raw_line, in_multiline_doc)
            code_line_stripped = code_line.strip()

            # ----------------------------------------------------
            # 1. Section Header Checks (SYN002)
            # ----------------------------------------------------
            sec_match = re.match(r"^([a-zA-Z0-9_.]+)\s*:$", code_line_stripped)
            if sec_match:
                raw_token = sec_match.group(1)
                header_name = raw_token.lower() + ":"

                # Ignore case labels (e.g. `case DAL_NEW:`) and default:
                if raw_token.lower() in ("default", "case"):
                    pass
                elif in_case_block and (raw_token.lower().startswith("case ") or raw_token.isupper()):
                    pass
                else:
                    if not self.is_valid_section_header(header_name):
                        closest = difflib.get_close_matches(header_name, self.all_known_sections, n=1, cutoff=0.6)
                        suggestion = f" Did you mean '{closest[0]}'?" if closest else ""
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "SYN002",
                                f"Unrecognized or misspelled section header '{header_name}'.{suggestion}",
                                raw_line,
                            )
                        )

            # ----------------------------------------------------
            # 2. Block Balance Tracking (SYN001)
            # ----------------------------------------------------
            # #context_on / #context_off
            if re.match(r"^\s*#context_on\b", code_line, re.IGNORECASE):
                context_stack.append(("#context_on", line_no))
            if re.match(r"^\s*#context_off\b", code_line, re.IGNORECASE):
                if not context_stack:
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "SYN001",
                            "Unmatched '#context_off' without corresponding '#context_on'.",
                            raw_line,
                        )
                    )
                else:
                    context_stack.pop()

            # Curly braces balance
            for char_idx, char in enumerate(code_line):
                if char == "{":
                    brace_stack.append(("{", line_no))
                elif char == "}":
                    if not brace_stack:
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                char_idx + 1,
                                "ERROR",
                                "SYN001",
                                "Unmatched closing brace '}'.",
                                raw_line,
                            )
                        )
                    else:
                        brace_stack.pop()
                        if current_func_name and not brace_stack:
                            current_func_name = None
                            current_func_hook_suffix = None

            # ON CASE / ENDCASE
            if re.search(r"(?<![.\w])on\s+case(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("case", line_no))
                in_case_block = True
            elif re.search(r"(?<![.\w])endcase(?![.\w])", code_line, re.IGNORECASE):
                in_case_block = False
                if not block_stack or block_stack[-1][0] != "case":
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "SYN001",
                            "Unmatched 'endcase' without corresponding 'on case'.",
                            raw_line,
                        )
                    )
                else:
                    block_stack.pop()

            # SELECT / ENDSELECT
            select_matches = re.findall(r"(?<![.\w])select(?![.\w])", code_line, re.IGNORECASE)
            for _ in select_matches:
                block_stack.append(("select", line_no))

            endselect_matches = re.findall(r"(?<![.\w])endselect(?![.\w])", code_line, re.IGNORECASE)
            for _ in endselect_matches:
                if not block_stack or block_stack[-1][0] != "select":
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "SYN001",
                            "Unmatched 'endselect' without corresponding 'select'.",
                            raw_line,
                        )
                    )
                else:
                    block_stack.pop()

            # FOR / ENDFOR (only for-loop: 'for <var> = <init> to <limit>')
            if re.search(r"(?<![.\w])for(?![.\w])\s+[a-zA-Z0-9_.]+\s*=", code_line, re.IGNORECASE):
                block_stack.append(("for", line_no))

            endfor_matches = re.findall(r"(?<![.\w])endfor(?![.\w])", code_line, re.IGNORECASE)
            for _ in endfor_matches:
                if not block_stack or block_stack[-1][0] != "for":
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "SYN001",
                            "Unmatched 'endfor' without corresponding 'for'.",
                            raw_line,
                        )
                    )
                else:
                    block_stack.pop()

            # WHILE / ENDWHILE
            if re.search(r"(?<![.\w])while(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("while", line_no))

            endwhile_matches = re.findall(r"(?<![.\w])endwhile(?![.\w])", code_line, re.IGNORECASE)
            for _ in endwhile_matches:
                if not block_stack or block_stack[-1][0] != "while":
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "SYN001",
                            "Unmatched 'endwhile' without corresponding 'while'.",
                            raw_line,
                        )
                    )
                else:
                    block_stack.pop()

            # REPEAT / UNTIL
            if re.search(r"(?<![.\w])repeat(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("repeat", line_no))

            until_matches = re.findall(r"(?<![.\w])until(?![.\w])", code_line, re.IGNORECASE)
            for _ in until_matches:
                if not block_stack or block_stack[-1][0] != "repeat":
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "SYN001",
                            "Unmatched 'until' without corresponding 'repeat'.",
                            raw_line,
                        )
                    )
                else:
                    block_stack.pop()

            # IF / ENDIF
            if re.search(r"(?<![.\w])if(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("if", line_no))

            endif_matches = re.findall(r"(?<![.\w])endif(?![.\w])", code_line, re.IGNORECASE)
            for _ in endif_matches:
                if not block_stack or block_stack[-1][0] != "if":
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "SYN001",
                            "Unmatched 'endif' without corresponding 'if'.",
                            raw_line,
                        )
                    )
                else:
                    block_stack.pop()

            # ----------------------------------------------------
            # 3. Function & DAL Hook Signatures (DAL002, DAL003)
            # ----------------------------------------------------
            func_decl_match = re.match(
                r"^\s*(?:function\s+)?(?:extern\s+)?(?:[a-zA-Z0-9_.]+\s+)?([a-zA-Z0-9_.]+)\s*\((.*?)\)",
                code_line,
            )
            if func_decl_match:
                func_name = func_decl_match.group(1).lower()
                params = func_decl_match.group(2).strip()
                current_func_name = func_name
                current_func_hook_suffix = None

                # Check if this matches a DAL field hook suffix
                for sfx, sfx_def in self.dal_field_hooks.items():
                    if func_name.endswith(sfx):
                        current_func_hook_suffix = sfx
                        # Check required arguments
                        req_args = sfx_def.get("arguments", "")
                        if "long i.mode" in req_args:
                            if not re.search(r"\blong\s+i\.mode\b", params, re.IGNORECASE):
                                diagnostics.append(
                                    Diagnostic(
                                        file_path,
                                        line_no,
                                        1,
                                        "ERROR",
                                        "DAL002",
                                        f"DAL hook '{func_name}' must declare parameter 'long i.mode'. Found: '({params})'.",
                                        raw_line,
                                    )
                                )
                        elif "long has_changed" in req_args:
                            if not re.search(r"\blong\s+has_changed\b", params, re.IGNORECASE):
                                diagnostics.append(
                                    Diagnostic(
                                        file_path,
                                        line_no,
                                        1,
                                        "ERROR",
                                        "DAL002",
                                        f"DAL hook '{func_name}' must declare parameter 'long has_changed'. Found: '({params})'.",
                                        raw_line,
                                    )
                                )
                        break

            # DAL003 Check: return values inside DAL hooks
            if current_func_hook_suffix:
                ret_match = re.search(r"\breturn\s*\((.*?)\)", code_line, re.IGNORECASE)
                if ret_match:
                    ret_val = ret_match.group(1).strip()
                    hook_info = self.dal_field_hooks.get(current_func_hook_suffix, {})
                    expected_ret = hook_info.get("returnValue", "")

                    if "boolean" in expected_ret:
                        # Should return boolean / true / false / 0 / 1
                        if ret_val and ret_val.lower() not in ("true", "false", "0", "1"):
                            # If it returns negative or DALHOOKERROR, flag it
                            if "dalhookerror" in ret_val.lower() or ret_val.startswith("-"):
                                diagnostics.append(
                                    Diagnostic(
                                        file_path,
                                        line_no,
                                        1,
                                        "ERROR",
                                        "DAL003",
                                        f"Boolean DAL hook '{current_func_name}' cannot return error code '{ret_val}'; must return true or false.",
                                        raw_line,
                                    )
                                )
                    elif "void" in expected_ret:
                        if ret_val:
                            diagnostics.append(
                                Diagnostic(
                                    file_path,
                                    line_no,
                                    1,
                                    "ERROR",
                                    "DAL003",
                                    f"Void DAL hook '{current_func_name}' cannot return a value '{ret_val}'.",
                                    raw_line,
                                )
                            )

            # ----------------------------------------------------
            # 4. Prohibited Interactive UI in DAL (DAL001)
            # ----------------------------------------------------
            if mode == "dal2":
                ui_matches = re.finditer(r"(?<![.\w])(message|ask\.enum|box|input\.string)\s*\(", code_line, re.IGNORECASE)
                for uim in ui_matches:
                    func_called = uim.group(1).lower()
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            uim.start() + 1,
                            "ERROR",
                            "DAL001",
                            f"Interactive dialog '{func_called}()' is prohibited in DAL scripts; use 'dal.set.error.message()' instead.",
                            raw_line,
                        )
                    )

            # ----------------------------------------------------
            # 5. Raw DB Mutation in UI Script (DAL004)
            # ----------------------------------------------------
            if mode == "general":
                db_mut_matches = re.finditer(
                    r"(?<![.\w])(db\.insert|db\.update|db\.delete|db\.write)\s*\(", code_line, re.IGNORECASE
                )
                for dbm in db_mut_matches:
                    mut_fn = dbm.group(1).lower()
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            dbm.start() + 1,
                            "ERROR",
                            "DAL004",
                            f"Direct database mutation '{mut_fn}()' in UI script violates Separation of Concerns; use DAL2 instead.",
                            raw_line,
                        )
                    )

            # ----------------------------------------------------
            # 6. Nested Transactions in Subroutines (CAV003)
            # ----------------------------------------------------
            if mode in ("dal2", "uedll"):
                tx_matches = re.finditer(
                    r"(?<![.\w])(db\.retry\.point|commit\.transaction|abort\.transaction)\s*\(",
                    code_line,
                    re.IGNORECASE,
                )
                for txm in tx_matches:
                    tx_fn = txm.group(1).lower()
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            txm.start() + 1,
                            "WARNING",
                            "CAV003",
                            f"Nested transaction statement '{tx_fn}()' is prohibited in {mode.upper()} scripts; transaction boundaries are managed by the caller.",
                            raw_line,
                        )
                    )

            # ----------------------------------------------------
            # 7. Float Equality Anti-Pattern (CAV001)
            # ----------------------------------------------------
            if re.search(r"==\s*\d+\.\d+|\d+\.\d+\s*==", code_line) or re.search(r"==\s*0\.0\b|0\.0\s*==", code_line):
                diagnostics.append(
                    Diagnostic(
                        file_path,
                        line_no,
                        1,
                        "WARNING",
                        "CAV001",
                        "Direct floating-point equality comparison '==' detected; use tolerance/epsilon check instead.",
                        raw_line,
                    )
                )

            # ----------------------------------------------------
            # 8. Function Call Catalog Inspections (CLD001, CLD002, INC001)
            # ----------------------------------------------------
            call_matches = re.finditer(r"\b([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)+)\s*\(", code_line)
            for cm in call_matches:
                called_fn = cm.group(1)
                called_fn_ci = called_fn.lower()

                fn_info = self.functions_db.get(called_fn_ci)
                if fn_info:
                    # Cloud Trust check (CLD001)
                    if self.cloud_mode and not fn_info.get("trusted", True):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                cm.start() + 1,
                                "ERROR",
                                "CLD001",
                                f"Function '{called_fn}' is untrusted for Infor LN Cloud Multi-Tenant environments.",
                                raw_line,
                            )
                        )

                    # Deprecation check (CLD002)
                    if fn_info.get("deprecated", False):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                cm.start() + 1,
                                "WARNING",
                                "CLD002",
                                f"Function '{called_fn}' is deprecated in Infor LN Studio catalog.",
                                raw_line,
                            )
                        )

                    # Missing Include check (INC001)
                    req_inc = fn_info.get("include", "").lower().strip()
                    if req_inc and req_inc not in includes_found:
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                cm.start() + 1,
                                "WARNING",
                                "INC001",
                                f"Function '{called_fn}' requires '#include <{req_inc}>', which is missing.",
                                raw_line,
                            )
                        )

        # Unbalanced block endings at end of file (SYN001)
        while block_stack:
            blk_type, blk_line = block_stack.pop()
            diagnostics.append(
                Diagnostic(
                    file_path,
                    blk_line,
                    1,
                    "ERROR",
                    "SYN001",
                    f"Unclosed '{blk_type}' statement opened at line {blk_line}.",
                )
            )

        while context_stack:
            ctx_type, ctx_line = context_stack.pop()
            diagnostics.append(
                Diagnostic(
                    file_path,
                    ctx_line,
                    1,
                    "ERROR",
                    "SYN001",
                    f"Unclosed '{ctx_type}' opened at line {ctx_line}.",
                )
            )

        while brace_stack:
            brace_char, brace_line = brace_stack.pop()
            diagnostics.append(
                Diagnostic(
                    file_path,
                    brace_line,
                    1,
                    "ERROR",
                    "SYN001",
                    f"Unclosed brace '{brace_char}' opened at line {brace_line}.",
                )
            )

        # Filter by severity
        filtered: List[Diagnostic] = []
        for d in diagnostics:
            if SEVERITY_LEVELS.get(d.severity, 0) >= self.min_severity_level:
                filtered.append(d)

        return filtered

    def audit_path(self, target: Path, mode: Optional[str] = None) -> List[Diagnostic]:
        """Audit single file or recursively audit directory."""
        all_diags: List[Diagnostic] = []
        if target.is_file():
            text = target.read_text(encoding="utf-8", errors="replace")
            all_diags.extend(self.audit_content(text, str(target), mode=mode))
        elif target.is_dir():
            patterns = ["*.cln", "*.dal", "*.dalsrc", "*.lib", "*.ue", "*.3gl", "*.4gl", "*.spt"]
            matched_files: List[Path] = []
            for pat in patterns:
                matched_files.extend(target.rglob(pat))
            for f in sorted(set(matched_files)):
                text = f.read_text(encoding="utf-8", errors="replace")
                all_diags.extend(self.audit_content(text, str(f), mode=mode))
        else:
            raise FileNotFoundError(f"Path not found: {target}")

        return all_diags


def print_colored_summary(diagnostics: List[Diagnostic], total_files: int, execution_failed: bool):
    """Print human-readable ANSI colored diagnostic report."""
    err_count = sum(1 for d in diagnostics if d.severity == "ERROR")
    warn_count = sum(1 for d in diagnostics if d.severity == "WARNING")
    info_count = sum(1 for d in diagnostics if d.severity == "INFO")

    print("\n" + "=" * 70)
    print(" INFOR LN 4GL & DAL STATIC AUDIT REPORT")
    print("=" * 70)

    if not diagnostics:
        print("\n [PASSED] 0 issues detected across audited files.\n")
        return

    # Group by file
    by_file: Dict[str, List[Diagnostic]] = {}
    for d in diagnostics:
        by_file.setdefault(d.file, []).append(d)

    for fpath, items in by_file.items():
        print(f"\nFile: {fpath}")
        print("-" * len(f"File: {fpath}"))
        for d in items:
            badge = f"[{d.severity}]"
            print(f"  Line {d.line:4d}:{d.column:2d}  {d.code:6s}  {badge:9s}  {d.message}")
            if d.snippet:
                print(f"            | {d.snippet}")

    print("\n" + "-" * 70)
    status_str = "FAILED" if execution_failed else "PASSED"
    print(f"Summary: {total_files} file(s) audited. {err_count} errors, {warn_count} warnings, {info_count} info.")
    print(f"Audit Status: {status_str}")
    print("=" * 70 + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Standalone Infor LN 4GL & DAL Audit Engine against Studio Build 0640 standards."
    )
    parser.add_argument("target_path", help="Path to 4GL file (.cln, .dal, .ue, etc.) or directory")
    parser.add_argument(
        "--mode",
        choices=["auto", "general", "dal2", "uedll"],
        default="auto",
        help="Enforce specific script archetype rules (default: auto)",
    )
    parser.add_argument(
        "--cloud",
        action="store_true",
        help="Enforce Infor LN CloudSuite Multi-Tenant restrictions (prohibit untrusted functions)",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format: text (human summary) or json (machine diagnostic array)",
    )
    parser.add_argument(
        "--severity",
        choices=["info", "warning", "error"],
        default="info",
        help="Minimum severity level to report (default: info)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with non-zero exit code if ANY error or warning is reported",
    )
    parser.add_argument(
        "--skill-dir",
        default=None,
        help="Path to erp-ln-progguide directory (default: parent directory of script)",
    )

    args = parser.parse_args()
    target = Path(args.target_path)
    skill_dir = Path(args.skill_dir) if args.skill_dir else None

    auditor = Auditor4GL(
        skill_dir=skill_dir,
        cloud_mode=args.cloud,
        min_severity=args.severity,
        strict=args.strict,
    )

    try:
        diagnostics = auditor.audit_path(target, mode=args.mode)
    except Exception as e:
        print(f"Error during audit: {e}", file=sys.stderr)
        return 2

    err_count = sum(1 for d in diagnostics if d.severity == "ERROR")
    warn_count = sum(1 for d in diagnostics if d.severity == "WARNING")
    info_count = sum(1 for d in diagnostics if d.severity == "INFO")

    has_failures = err_count > 0 or (args.strict and warn_count > 0)
    total_files = 1 if target.is_file() else len(set(d.file for d in diagnostics)) or 1

    if args.format == "json":
        output = {
            "summary": {
                "total_files": total_files,
                "error_count": err_count,
                "warning_count": warn_count,
                "info_count": info_count,
                "status": "FAILED" if has_failures else "PASSED",
            },
            "diagnostics": [d.to_dict() for d in diagnostics],
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print_colored_summary(diagnostics, total_files, has_failures)

    return 1 if has_failures else 0


if __name__ == "__main__":
    sys.exit(main())
