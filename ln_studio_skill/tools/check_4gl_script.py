#!/usr/bin/env python3
"""
LN Studio Static 4GL Script Inspector (`check-script`)

Statically inspects 4GL scripts (standalone .dal/.cln/.lib/.4gl or embedded <expression> in XML)
against LN Studio 10.8's Code Completion tables and syntax rules:
  1. Section header validation (static & dynamic program sections, subsections, choice sections)
  2. Block balance validation (select/endselect, if/endif, case/endcase, for/endfor, while/endwhile,
     repeat/until, #context_on/#context_off, and brace matching for functions)
  3. Symbol cross-check against owning XML object (Session FormFields, Commands, Table Columns, DAL hooks)
"""

import argparse
import difflib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


# Default fallback dictionaries in case studio_syntax_completion.json is missing
DEFAULT_PROGRAM_SECTIONS = {
    "declaration:",
    "before.program:",
    "after.program:",
    "after.form.read:",
    "after.update.db.commit:",
    "before.display.object:",
    "before.new.object:",
    "on.error:",
    "functions:",
    "main.table.io:",
    "init.form:",
}

DEFAULT_SUB_SECTIONS = {
    "after.choice:", "after.delete:", "after.display.object:", "after.display:",
    "after.field:", "after.form:", "after.group:", "after.input:", "after.layout:",
    "after.read:", "after.rewrite:", "after.skip.delete:", "after.skip.rewrite:",
    "after.skip.write:", "after.update.db.commit:", "after.write:", "after.zoom:",
    "before.choice:", "before.delete:", "before.destroy.object:", "before.display.object:",
    "before.display:", "before.field:", "before.form:", "before.group:", "before.input:",
    "before.layout:", "before.open.object.set:", "before.read:", "before.rewrite:",
    "before.skip.delete:", "before.skip.rewrite:", "before.skip.write:", "before.write:",
    "before.zoom:", "check.input:", "domain.error:", "init.field:", "init.form:",
    "init.group:", "on.choice:", "on.entry:", "on.exit:", "read.view:", "when.field.changes:"
}

DEFAULT_CHOICE_SECTIONS = {
    "choice.abort.program:", "choice.add.set:", "choice.bms:", "choice.change.frm:",
    "choice.change.order:", "choice.def.find:", "choice.end.program:", "choice.find.data:",
    "choice.first.set:", "choice.first.view:", "choice.interrupt:", "choice.last.set:",
    "choice.last.view:", "choice.modify.set:", "choice.next.half:", "choice.next.set:",
    "choice.next.view:", "choice.prev.half:", "choice.prev.set:", "choice.prev.view:",
    "choice.print.data:", "choice.recover.set:", "choice.restart.input:", "choice.run.job:",
    "choice.start.chart:", "choice.start.set:", "choice.text.manager:", "choice.update.db:",
    "choice.user.0:", "choice.user.1:", "choice.user.2:", "choice.user.3:", "choice.user.4:",
    "choice.user.5:", "choice.user.6:", "choice.user.7:", "choice.user.8:", "choice.user.9:",
    "choice.zoom:"
}

DEFAULT_DAL_OBJECT_HOOKS = {
    "before.open.object.set", "before.get.object", "after.get.object",
    "before.new.object", "after.new.object", "before.change.object",
    "after.change.object", "before.destroy.object", "after.destroy.object",
    "before.save.object", "after.save.object", "after.commit.transaction",
    "after.abort.transaction", "method.is.allowed", "set.object.defaults"
}

DEFAULT_DAL_FIELD_HOOK_SUFFIXES = {
    ".is.never.applicable", ".is.applicable", ".is.readonly", ".is.derived",
    ".is.mandatory", ".is.valid", ".update", ".make.valid", ".check", ".set.defaults"
}


class Diagnostic:
    def __init__(self, file_path: str, line: int, col: int, severity: str, message: str):
        self.file_path = file_path
        self.line = line
        self.col = col
        self.severity = severity.upper()  # ERROR or WARNING
        self.message = message

    def __str__(self) -> str:
        return f"[{self.severity}] {self.file_path}:{self.line}:{self.col}: {self.message}"


def load_syntax_catalog() -> Dict[str, Any]:
    """Load extracted LN Studio syntax catalog if available, or fall back to defaults."""
    candidates = [
        Path(__file__).resolve().parent.parent / "references" / "studio_syntax_completion.json",
        Path(__file__).resolve().parent.parent.parent / "erp-ln-progguide" / "references" / "studio_syntax_completion.json",
    ]
    for catalog_path in candidates:
        if catalog_path.exists():
            try:
                return json.loads(catalog_path.read_text(encoding="utf-8"))
            except Exception:
                pass
    return {
        "program_sections": list(DEFAULT_PROGRAM_SECTIONS),
        "sub_sections": list(DEFAULT_SUB_SECTIONS),
        "choice_sections": list(DEFAULT_CHOICE_SECTIONS),
        "dal_object_hooks": list(DEFAULT_DAL_OBJECT_HOOKS),
        "dal_field_hook_suffixes": [{"suffix": s} for s in DEFAULT_DAL_FIELD_HOOK_SUFFIXES],
    }


def load_functions_db() -> Dict[str, Any]:
    """Load bshell function catalog from erp-ln-progguide/index/functions_db.json."""
    candidates = [
        Path(__file__).resolve().parent.parent.parent / "erp-ln-progguide" / "index" / "functions_db.json",
        Path(__file__).resolve().parent.parent / "index" / "functions_db.json",
    ]
    for c in candidates:
        if c.exists():
            try:
                raw = json.loads(c.read_text(encoding="utf-8"))
                return {k.lower(): v for k, v in raw.items()}
            except Exception:
                pass
    return {}


def strip_4gl_comments_and_strings(line: str, in_multiline_doc: bool) -> Tuple[str, bool]:
    """
    Remove comments (| to end of line) and string literals ('...' or "...") from a line.
    Handles DllUsage / FunctionUsage documentation blocks.
    """
    line_lower = line.strip().lower()
    if in_multiline_doc:
        if "enddllusage" in line_lower or "endfunctionusage" in line_lower:
            return "", False
        return "", True

    if line_lower.startswith("dllusage") or line_lower.startswith("functionusage"):
        return "", True

    res = []
    i = 0
    n = len(line)
    in_str = False
    str_char = ''

    while i < n:
        c = line[i]
        if in_str:
            if c == '\\' and i + 1 < n:
                i += 2
                continue
            if c == str_char:
                in_str = False
            i += 1
            continue

        # Check start of string
        if c in ('"', "'"):
            in_str = True
            str_char = c
            res.append(' ')
            i += 1
            continue

        # Check comment start
        if c == '|':
            break

        res.append(c)
        i += 1

    return "".join(res), False


class ScriptChecker:
    def __init__(
        self,
        catalog: Optional[Dict[str, Any]] = None,
        functions_db: Optional[Dict[str, Any]] = None,
        cloud_mode: bool = False,
    ):
        if not catalog:
            catalog = load_syntax_catalog()
        if functions_db is None:
            functions_db = load_functions_db()

        self.functions_db = functions_db
        self.cloud_mode = cloud_mode

        self.program_sections = set(catalog.get("program_sections", DEFAULT_PROGRAM_SECTIONS))
        self.sub_sections = set(catalog.get("sub_sections", DEFAULT_SUB_SECTIONS))
        self.choice_sections = set(catalog.get("choice_sections", DEFAULT_CHOICE_SECTIONS))
        self.dal_object_hooks = set(catalog.get("dal_object_hooks", DEFAULT_DAL_OBJECT_HOOKS))

        raw_suffixes = catalog.get("dal_field_hook_suffixes", [])
        self.dal_field_hook_suffixes = set()
        self.dal_field_hooks_info: Dict[str, Dict[str, Any]] = {}
        for s in raw_suffixes:
            if isinstance(s, dict):
                sfx = s.get("suffix", "")
                self.dal_field_hook_suffixes.add(sfx)
                self.dal_field_hooks_info[sfx.lower()] = s
            else:
                self.dal_field_hook_suffixes.add(str(s))
                self.dal_field_hooks_info[str(s).lower()] = {"suffix": str(s)}

        # Build combined all known section list for typo suggestion
        self.all_known_sections = sorted(
            list(self.program_sections) +
            list(self.sub_sections) +
            list(self.choice_sections)
        )

    def is_valid_section_header(self, token: str) -> Tuple[bool, Optional[str]]:
        """
        Check whether token (ending with ':') is a valid 4GL section or subsection.
        Returns (is_valid, category_or_none).
        """
        token = token.strip()
        if not token.endswith(':'):
            return False, None

        token_lower = token.lower()

        # 1. Exact static match
        if token_lower in self.program_sections:
            return True, "program_section"
        if token_lower in self.sub_sections:
            return True, "sub_section"
        if token_lower in self.choice_sections:
            return True, "choice_section"

        # 2. Dynamic program sections
        if token_lower.startswith("field."):
            return True, "field_section"
        if token_lower.startswith("choice."):
            return True, "choice_section"
        if re.match(r"^group\.[0-9a-zA-Z_]+:$", token_lower):
            return True, "group_section"
        if re.match(r"^form\.[0-9a-zA-Z_]+:$", token_lower):
            return True, "form_section"
        if token_lower.startswith("zoom.from."):
            return True, "zoom_section"
        if re.match(r"^(header|detail|before|after)\.[0-9]+:$", token_lower):
            return True, "report_section"

        return False, None

    def check_script(self, script_text: str, file_path: str = "<script>",
                     owning_component: Optional[Dict[str, Any]] = None) -> List[Diagnostic]:
        """Perform static verification of 4GL script text."""
        diagnostics: List[Diagnostic] = []
        lines = script_text.splitlines()

        # Includes collection
        includes_found: Set[str] = set()
        for raw_line in lines:
            m_inc = re.match(r'^\s*#include\s+[<"]([a-zA-Z0-9_.]+)[>"]', raw_line)
            if m_inc:
                inc_name = m_inc.group(1).lower()
                if inc_name.endswith(".h"):
                    inc_name = inc_name[:-2]
                includes_found.add(inc_name)

        is_dal = (
            file_path.lower().endswith((".dal", ".dalsrc"))
            or "dal2" in file_path.lower()
            or "before.save.object" in script_text.lower()
            or "dal.set.error.message" in script_text.lower()
            or "bic_tableext" in script_text.lower()
            or "bic_dal2" in script_text.lower()
            or "/table/" in file_path.replace("\\", "/").lower()
            or "\\table\\" in file_path.lower()
        )

        # Block balance stacks: (block_type, line_number)
        block_stack: List[Tuple[str, int]] = []
        context_stack: List[Tuple[str, int]] = []
        brace_stack: List[Tuple[str, int]] = []

        in_multiline_doc = False
        in_case_block = False

        for line_no, raw_line in enumerate(lines, start=1):
            stripped_line = raw_line.strip()
            if not stripped_line:
                continue

            # Strip comments & strings for syntax inspection
            code_line, in_multiline_doc = strip_4gl_comments_and_strings(raw_line, in_multiline_doc)
            code_line_stripped = code_line.strip()

            # ----------------------------------------------------
            # 1. Section Header Checks
            # ----------------------------------------------------
            # Check if line defines a top-level section/subsection label (e.g. `declaration:` or `before.program:`)
            # Must not be inside case statements (e.g. `case DAL_NEW:`) or default:
            section_match = re.match(r"^([a-zA-Z0-9_.]+)\s*:$", code_line_stripped)
            if section_match:
                header_name = section_match.group(1).lower() + ":"
                raw_token = section_match.group(1)

                if raw_token.lower() in ("default", "case"):
                    pass  # Case label
                elif in_case_block and (raw_token.lower().startswith("case ") or raw_token.isupper()):
                    pass  # Likely an enum case label inside on case
                else:
                    valid, category = self.is_valid_section_header(header_name)
                    if not valid:
                        # Find closest match
                        matches = difflib.get_close_matches(header_name, self.all_known_sections, n=1, cutoff=0.6)
                        suggestion = f" Did you mean '{matches[0]}'?" if matches else ""
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Unrecognized or misspelled section header '{header_name}'.{suggestion}"
                        ))

            # ----------------------------------------------------
            # 2. Block Balance Checks
            # ----------------------------------------------------
            # #context_on / #context_off check
            m_ctx = re.match(r'^\s*#context_on\s*(?:["\']([^"\']+)["\'])?', code_line, re.IGNORECASE)
            if m_ctx:
                ctx_name = m_ctx.group(1) or "unknown"
                if context_stack:
                    parent_name, parent_line = context_stack[-1]
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        f"Nested '#context_on' is not allowed: block '{ctx_name}' opened inside '{parent_name}' (line {parent_line})."
                    ))
                context_stack.append((f"#context_on \"{ctx_name}\"", line_no))
            if re.match(r"^\s*#context_off\b", code_line, re.IGNORECASE):
                if not context_stack:
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        "Unmatched '#context_off' without corresponding '#context_on'."
                    ))
                else:
                    context_stack.pop()

            # Curly braces balance
            for char_idx, char in enumerate(code_line):
                if char == '{':
                    brace_stack.append(('{', line_no))
                elif char == '}':
                    if not brace_stack:
                        diagnostics.append(Diagnostic(
                            file_path, line_no, char_idx + 1, "ERROR",
                            "Unmatched closing brace '}'."
                        ))
                    else:
                        brace_stack.pop()

            # ON CASE / ENDCASE
            if re.search(r"(?<![.\w])on\s+case(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("case", line_no))
                in_case_block = True
            elif re.search(r"(?<![.\w])endcase(?![.\w])", code_line, re.IGNORECASE):
                in_case_block = False
                if not block_stack or block_stack[-1][0] != "case":
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        "Unmatched 'endcase' without corresponding 'on case'."
                    ))
                else:
                    block_stack.pop()

            # SELECT / ENDSELECT
            select_matches = re.findall(r"(?<![.\w])select(?![.\w])", code_line, re.IGNORECASE)
            for _ in select_matches:
                block_stack.append(("select", line_no))

            endselect_matches = re.findall(r"(?<![.\w])endselect(?![.\w])", code_line, re.IGNORECASE)
            for _ in endselect_matches:
                if not block_stack or block_stack[-1][0] != "select":
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        "Unmatched 'endselect' without corresponding 'select'."
                    ))
                else:
                    block_stack.pop()

            # FOR / ENDFOR (Baan 4GL for-loop is always 'for <var> = <init> to <limit>')
            # Ignore SQL 'for update' and 'for read only'
            if re.search(r"(?<![.\w])for(?![.\w])\s+[a-zA-Z0-9_.]+\s*=", code_line, re.IGNORECASE):
                block_stack.append(("for", line_no))

            endfor_matches = re.findall(r"(?<![.\w])endfor(?![.\w])", code_line, re.IGNORECASE)
            for _ in endfor_matches:
                if not block_stack or block_stack[-1][0] != "for":
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        "Unmatched 'endfor' without corresponding 'for'."
                    ))
                else:
                    block_stack.pop()

            # WHILE / ENDWHILE
            if re.search(r"(?<![.\w])while(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("while", line_no))

            endwhile_matches = re.findall(r"(?<![.\w])endwhile(?![.\w])", code_line, re.IGNORECASE)
            for _ in endwhile_matches:
                if not block_stack or block_stack[-1][0] != "while":
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        "Unmatched 'endwhile' without corresponding 'while'."
                    ))
                else:
                    block_stack.pop()

            # REPEAT / UNTIL
            if re.search(r"(?<![.\w])repeat(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("repeat", line_no))

            until_matches = re.findall(r"(?<![.\w])until(?![.\w])", code_line, re.IGNORECASE)
            for _ in until_matches:
                if not block_stack or block_stack[-1][0] != "repeat":
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        "Unmatched 'until' without corresponding 'repeat'."
                    ))
                else:
                    block_stack.pop()

            # IF / ENDIF
            if re.search(r"(?<![.\w])if(?![.\w])", code_line, re.IGNORECASE):
                block_stack.append(("if", line_no))

            endif_matches = re.findall(r"(?<![.\w])endif(?![.\w])", code_line, re.IGNORECASE)
            for _ in endif_matches:
                if not block_stack or block_stack[-1][0] != "if":
                    diagnostics.append(Diagnostic(
                        file_path, line_no, 1, "ERROR",
                        "Unmatched 'endif' without corresponding 'if'."
                    ))
                else:
                    block_stack.pop()

            # ----------------------------------------------------
            # 3. DAL & Extension Function Hook Signatures
            # ----------------------------------------------------
            func_match = re.match(r"^\s*function(?:\s+extern)?(?:\s+([a-zA-Z0-9_.]+))?\s+([a-zA-Z0-9_.]+)\s*\((.*?)\)", code_line, re.IGNORECASE)
            if func_match:
                ret_type = (func_match.group(1) or "").lower()
                func_name = func_match.group(2).lower()
                params = func_match.group(3).strip()

                # Specific Extension & DAL Lifecycle Hooks
                if func_name == "before.save.object":
                    if ret_type in ("void", "boolean"):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Hook 'before.save.object' must return 'long' (returns error code or 0). Found: '{ret_type}'."
                        ))
                    if not re.search(r"\blong\s+[a-zA-Z0-9_.]+\b", params, re.IGNORECASE):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Hook 'before.save.object' must declare parameter 'long mode'. Found: '({params})'."
                        ))
                elif func_name == "after.save.object":
                    if ret_type and ret_type not in ("long", "void"):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Hook 'after.save.object' must return 'long' or 'void'. Found: '{ret_type}'."
                        ))
                elif func_name == "before.destroy.object":
                    if ret_type and ret_type not in ("long", "void"):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Hook 'before.destroy.object' must return 'long' or 'void'. Found: '{ret_type}'."
                        ))
                elif func_name == "after.destroy.object":
                    if ret_type and ret_type not in ("long", "void"):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Hook 'after.destroy.object' must return 'long' or 'void'. Found: '{ret_type}'."
                        ))
                elif func_name == "method.is.allowed":
                    if ret_type and ret_type != "boolean":
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Hook 'method.is.allowed' must return 'boolean'. Found: '{ret_type}'."
                        ))
                    if not re.search(r"\blong\s+[a-zA-Z0-9_.]+\b", params, re.IGNORECASE):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Hook 'method.is.allowed' must declare parameter 'long method'. Found: '({params})'."
                        ))
                elif func_name.endswith((".is.valid", ".is.readonly", ".is.mandatory", ".is.applicable", ".is.never.applicable")):
                    if ret_type and ret_type != "boolean":
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Field hook '{func_name}' must return 'boolean'. Found: '{ret_type}'."
                        ))
                elif func_name.startswith("function.") and (func_name.endswith(".is.enabled") or func_name.endswith(".before.command")):
                    if ret_type and ret_type != "boolean":
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Command hook '{func_name}' must return 'boolean'. Found: '{ret_type}'."
                        ))
                elif func_name.startswith("function.") and func_name.endswith(".after.command"):
                    if ret_type and ret_type not in ("void", "long"):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, 1, "ERROR",
                            f"Command hook '{func_name}' must return 'void' or 'long'. Found: '{ret_type}'."
                        ))

                # Check if it looks like a DAL property hook: <col>.<suffix>
                for sfx in self.dal_field_hook_suffixes:
                    if func_name.endswith(sfx):
                        col_prefix = func_name[:-len(sfx)]
                        # Check required arguments
                        hook_info = self.dal_field_hooks_info.get(sfx.lower(), {})
                        req_args = hook_info.get("arguments", "")
                        if "long i.mode" in req_args:
                            if not re.search(r"\blong\s+i\.mode\b", params, re.IGNORECASE):
                                diagnostics.append(Diagnostic(
                                    file_path, line_no, 1, "ERROR",
                                    f"DAL hook '{func_name}' must declare parameter 'long i.mode'. Found: '({params})'."
                                ))
                        elif "long has_changed" in req_args:
                            if not re.search(r"\blong\s+has_changed\b", params, re.IGNORECASE):
                                diagnostics.append(Diagnostic(
                                    file_path, line_no, 1, "ERROR",
                                    f"DAL hook '{func_name}' must declare parameter 'long has_changed'. Found: '({params})'."
                                ))

                        # If owning component table columns are provided, check column
                        if owning_component and "columns" in owning_component:
                            table_cols = owning_component["columns"]
                            col_base = col_prefix.split('.')[-1]
                            if col_prefix not in table_cols and col_base not in table_cols and not col_base.startswith("cdf_"):
                                diagnostics.append(Diagnostic(
                                    file_path, line_no, 1, "WARNING",
                                    f"DAL property hook '{func_name}' references column '{col_prefix}' not found in owning table columns."
                                ))
                        break

            # ----------------------------------------------------
            # 4. Prohibited Interactive Dialogs & Transaction Controls in DAL / Table Extensions
            # ----------------------------------------------------
            if is_dal:
                ui_matches = re.finditer(r"(?<![.\w])(message|ask\.enum|box|input\.string)\s*\(", code_line, re.IGNORECASE)
                for uim in ui_matches:
                    func_called = uim.group(1).lower()
                    diagnostics.append(Diagnostic(
                        file_path, line_no, uim.start() + 1, "ERROR",
                        f"Interactive dialog '{func_called}()' is prohibited in DAL scripts and Table Extension hooks; use 'dal.set.error.message()' instead."
                    ))

                trans_matches = re.finditer(r"(?<![.\w])(commit\.transaction|abort\.transaction|db\.retry\.point)\s*\(", code_line, re.IGNORECASE)
                for tm in trans_matches:
                    func_called = tm.group(1).lower()
                    diagnostics.append(Diagnostic(
                        file_path, line_no, tm.start() + 1, "ERROR",
                        f"Transaction control '{func_called}()' is prohibited in DAL/Table Extension hooks; transaction lifecycle is managed by the DAL engine."
                    ))

            # ----------------------------------------------------
            # 5. Function Catalog Checks (Missing Includes & Cloud Trust)
            # ----------------------------------------------------
            call_matches = re.finditer(r"\b([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)+)\s*\(", code_line)
            for cm in call_matches:
                called_fn = cm.group(1)
                called_fn_ci = called_fn.lower()
                fn_info = self.functions_db.get(called_fn_ci)
                if fn_info:
                    if self.cloud_mode and not fn_info.get("trusted", True):
                        diagnostics.append(Diagnostic(
                            file_path, line_no, cm.start() + 1, "ERROR",
                            f"Function '{called_fn}' is untrusted for Infor LN Cloud Multi-Tenant environments."
                        ))
                    req_inc = fn_info.get("include", "").lower().strip()
                    if req_inc and req_inc not in includes_found:
                        diagnostics.append(Diagnostic(
                            file_path, line_no, cm.start() + 1, "WARNING",
                            f"Function '{called_fn}' requires '#include <{req_inc}>', which is missing."
                        ))

        # Check for unclosed blocks at EOF
        while block_stack:
            blk_type, blk_line = block_stack.pop()
            diagnostics.append(Diagnostic(
                file_path, blk_line, 1, "ERROR",
                f"Unclosed '{blk_type}' block (opened at line {blk_line})."
            ))

        while context_stack:
            ctx_type, ctx_line = context_stack.pop()
            diagnostics.append(Diagnostic(
                file_path, ctx_line, 1, "ERROR",
                f"Unclosed '{ctx_type}' directive (opened at line {ctx_line})."
            ))

        while brace_stack:
            br_char, br_line = brace_stack.pop()
            diagnostics.append(Diagnostic(
                file_path, br_line, 1, "ERROR",
                f"Unclosed brace '{br_char}' (opened at line {br_line})."
            ))

        # ----------------------------------------------------
        # 4. XML Cross-Reference Symbol Verification
        # ----------------------------------------------------
        if owning_component:
            comp_type = owning_component.get("type")
            # Session script symbol cross check
            if comp_type == "session":
                session_fields = owning_component.get("form_fields", set())
                session_commands = owning_component.get("commands", set())

                for line_no, raw_line in enumerate(lines, start=1):
                    code_line, _ = strip_4gl_comments_and_strings(raw_line, False)
                    # field.<name>:
                    m_fld = re.match(r"^\s*field\.([a-zA-Z0-9_.]+)\s*:", code_line.lower())
                    if m_fld:
                        fld_name = m_fld.group(1)
                        if fld_name not in ("all", "other") and session_fields:
                            # If fields are defined, check presence
                            if fld_name not in session_fields and fld_name.split('.')[-1] not in session_fields:
                                # Only report warning if session has explicit form fields
                                diagnostics.append(Diagnostic(
                                    file_path, line_no, 1, "WARNING",
                                    f"Field section 'field.{fld_name}:' is not declared as a FormField in the session."
                                ))

                    # choice.<name>:
                    m_ch = re.match(r"^\s*choice\.([a-zA-Z0-9_.]+)\s*:", code_line.lower())
                    if m_ch:
                        ch_name = m_ch.group(1)
                        ch_full = f"choice.{ch_name}:"
                        if ch_full not in self.choice_sections:
                            if session_commands and ch_name not in session_commands:
                                diagnostics.append(Diagnostic(
                                    file_path, line_no, 1, "WARNING",
                                    f"Custom choice section 'choice.{ch_name}:' does not match any declared FormCommand in session."
                                ))

        return diagnostics


def inspect_component_xml(xml_path: Path) -> Tuple[Optional[str], Dict[str, Any]]:
    """
    Parse component XML (.tbl, .ses, .lib) to extract embedded <expression> text
    and metadata for cross-checking.
    """
    try:
        tree = ET.parse(xml_path)
    except Exception as e:
        return None, {"error": f"Failed to parse XML: {e}"}

    root = tree.getroot()
    expr = root.find(".//expression")
    script_text = expr.text if (expr is not None and expr.text) else ""

    meta: Dict[str, Any] = {"file_path": str(xml_path)}

    if root.tag.endswith("Table"):
        meta["type"] = "table"
        cols = set()
        table_code = root.findtext(".//name") or xml_path.stem
        for col in root.findall(".//Column"):
            cname = col.findtext("name")
            if cname:
                cols.add(cname)
                cols.add(f"{table_code}.{cname}")
        meta["columns"] = cols
        meta["table_code"] = table_code

    elif root.tag.endswith("Session"):
        meta["type"] = "session"
        fields = set()
        for ff in root.findall(".//FormField"):
            fn = ff.findtext("fieldName")
            if fn:
                fields.add(fn)
        meta["form_fields"] = fields

        cmds = set()
        for cmd in root.findall(".//FormCommand"):
            cn = cmd.findtext("name")
            if cn:
                cmds.add(cn)
        meta["commands"] = cmds

    elif root.tag.endswith("Module"):
        meta["type"] = "library"
        meta["source_type"] = root.findtext(".//sourceType")

    return script_text, meta


def check_file(file_path: Path, owning_xml: Optional[Path] = None, cloud_mode: bool = False) -> List[Diagnostic]:
    """Check a single file (either XML with expression or standalone 4GL script)."""
    checker = ScriptChecker(cloud_mode=cloud_mode)

    if file_path.suffix.lower() in (".tbl", ".ses", ".lib"):
        script_text, meta = inspect_component_xml(file_path)
        if not script_text:
            return []
        return checker.check_script(script_text, file_path=str(file_path), owning_component=meta)

    # Standalone script file (.dal, .cln, .4gl, .bic)
    script_text = file_path.read_text(encoding="utf-8", errors="replace")
    owning_meta = None
    if owning_xml and owning_xml.exists():
        _, owning_meta = inspect_component_xml(owning_xml)

    return checker.check_script(script_text, file_path=str(file_path), owning_component=owning_meta)


def main() -> None:
    parser = argparse.ArgumentParser(description="LN Studio Static 4GL Script Inspector")
    parser.add_argument("path", type=Path, help="Path to 4GL script or XML component file/directory")
    parser.add_argument("--owning-xml", type=Path, default=None, help="Owning XML component for symbol verification")
    parser.add_argument("--cloud", action="store_true", help="Enforce Infor LN Cloud Multi-Tenant rules")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    target = args.path
    if not target.exists():
        print(f"Error: Target path does not exist: {target}", file=sys.stderr)
        sys.exit(1)

    files_to_check: List[Path] = []
    if target.is_dir():
        for ext in ("*.tbl", "*.ses", "*.lib", "*.dal", "*.cln", "*.4gl", "*.bic"):
            files_to_check.extend(target.rglob(ext))
    else:
        files_to_check.append(target)

    all_diagnostics: List[Diagnostic] = []
    for f in sorted(files_to_check):
        diags = check_file(f, owning_xml=args.owning_xml, cloud_mode=args.cloud)
        all_diagnostics.extend(diags)

    errors = [d for d in all_diagnostics if d.severity == "ERROR"]
    warnings = [d for d in all_diagnostics if d.severity == "WARNING"]

    if args.json:
        out = {
            "total_files": len(files_to_check),
            "errors_count": len(errors),
            "warnings_count": len(warnings),
            "diagnostics": [
                {
                    "file": d.file_path,
                    "line": d.line,
                    "col": d.col,
                    "severity": d.severity,
                    "message": d.message,
                }
                for d in all_diagnostics
            ]
        }
        print(json.dumps(out, indent=2))
    else:
        print(f"Checked {len(files_to_check)} component(s):")
        for d in all_diagnostics:
            print(f"  {d}")
        print(f"\nSummary: {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (args.strict and warnings):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
