#!/usr/bin/env python3
"""
Standalone Baan 4GL & DAL Audit Engine (Semantic, Schema & AST Validator)

Statically audits Baan 4GL, DAL2, and UEDLL files against Infor LN Studio Build 0640
authoritative dictionaries, Data Dictionary Schema Cache (.ln_dd_cache.json),
CloudSuite Multi-Tenant restrictions, DAL2 contracts, and AST/Call-Graph transaction rules.

Upgraded Rules (ADR 0008):
- TBL001: Enforces `table t<tablename>` declaration in `declaration:` for all referenced tables.
- TBL002: Validates `<table>.<field>` references against `.ln_dd_cache.json` (with `--auto-fetch-dd`).
- DMN001: Validates `domain <domain_name>` declarations against `.ln_dd_cache.json` (with `--auto-fetch-dd`).
- SYN001: Pure-Python Tokenizer & Recursive-Descent AST block parser handling `#define` macros,
          comments (`|`), subqueries, and multi-line SQL (`select`/`selectdo`/`selectempty`/`selecteos`/`endselect`).
- CAV003: Intra-file Function Call Graph detecting direct and transitive nested transactions
          (calling a helper function containing `db.retry.point()` / `commit.transaction()` inside an active transaction).

Zero external dependencies. Runs on pure Python 3.8+.
"""

import argparse
import difflib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

SEVERITY_LEVELS = {"INFO": 0, "WARNING": 1, "ERROR": 2}

# Standard Bshell built-in table pseudo-fields valid on all LN tables
BSHELL_PSEUDO_FIELDS = {
    "_compnr",
    "record_len",
    "_index1",
    "_index2",
    "_index3",
    "_index4",
    "_index5",
    "_index6",
    "_index7",
    "_index8",
    "_index9",
    "_index10",
    "_index11",
    "_index12",
}


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

    @property
    def fix_suggestion(self) -> str:
        return self.message

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


# ============================================================================
# Data Dictionary Schema Cache (.ln_dd_cache.json) & Ecore XML Indexer
# ============================================================================


class DataDictionaryCache:
    """
    Manages `.ln_dd_cache.json` reading, updating, and Ecore XML parsing for
    Infor LN Tables (`.tbl`) and Domains (`.dmn`).
    """

    def __init__(self, cache_path: Optional[Path] = None, raw_data: Optional[Dict[str, Any]] = None):
        self.cache_path = Path(cache_path) if cache_path else None
        self.tables: Dict[str, Dict[str, Any]] = {}
        self.domains: Dict[str, Dict[str, Any]] = {}

        if raw_data is not None:
            self._ingest_dict(raw_data)
        elif self.cache_path and self.cache_path.exists():
            self.load(self.cache_path)

    @property
    def has_data(self) -> bool:
        return bool(self.tables or self.domains)

    def _ingest_dict(self, data: Dict[str, Any]) -> None:
        raw_tables = data.get("tables", {})
        if isinstance(raw_tables, dict):
            for tbl_name, tbl_info in raw_tables.items():
                t_key = tbl_name.lower().strip()
                if isinstance(tbl_info, list):
                    # Simplified format: {"tables": {"tcibd001": ["item", "dsca"]}}
                    self.tables[t_key] = {
                        "name": t_key,
                        "fields": {str(f).lower(): {"name": str(f).lower()} for f in tbl_info},
                        "indices": [],
                    }
                elif isinstance(tbl_info, dict):
                    raw_fields = tbl_info.get("fields", tbl_info.get("columns", {}))
                    fields_map: Dict[str, Dict[str, Any]] = {}
                    if isinstance(raw_fields, list):
                        for f in raw_fields:
                            if isinstance(f, dict):
                                fname = str(f.get("name", "")).lower()
                                if fname:
                                    fields_map[fname] = f
                            else:
                                fname = str(f).lower()
                                fields_map[fname] = {"name": fname}
                    elif isinstance(raw_fields, dict):
                        for fname, fmeta in raw_fields.items():
                            fields_map[fname.lower()] = fmeta if isinstance(fmeta, dict) else {"name": fname.lower()}
                    self.tables[t_key] = {
                        "name": t_key,
                        "description": tbl_info.get("description", ""),
                        "fields": fields_map,
                        "indices": tbl_info.get("indices", []),
                    }

        raw_domains = data.get("domains", {})
        if isinstance(raw_domains, list):
            for d in raw_domains:
                d_key = str(d).lower().strip()
                if d_key:
                    self.domains[d_key] = {"name": d_key}
        elif isinstance(raw_domains, dict):
            for d_name, d_info in raw_domains.items():
                d_key = d_name.lower().strip()
                self.domains[d_key] = d_info if isinstance(d_info, dict) else {"name": d_key}

    def load(self, path: Optional[Path] = None) -> None:
        target = Path(path) if path else self.cache_path
        if not target or not target.exists():
            return
        try:
            raw = json.loads(target.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                self._ingest_dict(raw)
        except Exception:
            pass

    def save(self, path: Optional[Path] = None) -> Optional[Path]:
        target = Path(path) if path else self.cache_path
        if not target:
            return None
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "version": "1.0",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "tables": self.tables,
            "domains": self.domains,
        }
        target.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return target

    def has_table(self, table_name: str) -> bool:
        return table_name.lower() in self.tables

    def has_field(self, table_name: str, field_name: str) -> bool:
        t_key = table_name.lower()
        f_key = field_name.lower()
        if f_key in BSHELL_PSEUDO_FIELDS or re.match(r"^_index\d+$", f_key):
            return True
        if t_key not in self.tables:
            return False
        fields = self.tables[t_key].get("fields", {})
        return f_key in fields

    def has_domain(self, domain_name: str) -> bool:
        return domain_name.lower() in self.domains

    def update_table(
        self,
        table_name: str,
        fields: Dict[str, Any],
        indices: Optional[Any] = None,
        description: str = "",
    ) -> None:
        t_key = table_name.lower().strip()
        fields_map: Dict[str, Dict[str, Any]] = {}
        for fname, fmeta in fields.items():
            fields_map[fname.lower()] = fmeta if isinstance(fmeta, dict) else {"name": fname.lower()}
        self.tables[t_key] = {
            "name": t_key,
            "description": description,
            "fields": fields_map,
            "indices": indices if indices is not None else {},
        }

    def update_domain(
        self,
        domain_name: str,
        datatype: str = "string",
        length: Optional[int] = None,
        enum_values: Optional[List[str]] = None,
    ) -> None:
        d_key = domain_name.lower().strip()
        self.domains[d_key] = {
            "name": d_key,
            "datatype": datatype,
            "length": length,
            "enum_values": enum_values or [],
        }

    def index_xml_content(self, xml_content: str, hint_name: str = "") -> Optional[Dict[str, Any]]:
        """
        Parse a `.tbl` (`<DR_Table>`) or `.dmn` (`<DR_Domain>`) XML string and update
        in-memory cache. Supports both real Ecore (`<Column>/<datatype>/<name>`, `<Enumeration>`)
        and mock `<Field>` formats.
        """
        try:
            root = ET.fromstring(xml_content.strip())
        except ET.ParseError:
            return None

        for el in root.iter():
            if "}" in el.tag:
                el.tag = el.tag.split("}", 1)[1]

        root_tag = root.tag

        if root_tag == "DR_Table":
            tbl_name = (root.attrib.get("name") or root.findtext("name") or hint_name).strip().lower()
            if not tbl_name:
                return None
            desc = (root.findtext("description") or root.attrib.get("description") or "").strip()
            fields_map: Dict[str, Dict[str, Any]] = {}

            # 1. Real Ecore <Column> elements
            for col in root.findall(".//Column"):
                c_name = (col.attrib.get("name") or col.findtext("name") or "").strip().lower()
                if not c_name:
                    continue
                dt_node = col.find("datatype")
                dmn_name = ""
                native_dt = ""
                max_len = ""
                if dt_node is not None:
                    dmn_name = (dt_node.findtext("name") or dt_node.attrib.get("name") or "").strip()
                    native_dt = (dt_node.findtext("nativeDatatype") or dt_node.attrib.get("nativeDatatype") or "").strip()
                    for facet in dt_node.findall("Facet"):
                        if facet.findtext("type") == "maxLength":
                            max_len = facet.findtext("value") or ""
                if not dmn_name:
                    dmn_name = (col.attrib.get("domain") or col.findtext("domain") or "").strip()
                c_desc = (col.findtext("description") or col.attrib.get("description") or "").strip()
                is_mand = (col.findtext("isMandatory") or col.attrib.get("mandatory") or "false").lower() == "true"
                fields_map[c_name] = {
                    "name": c_name,
                    "domain": dmn_name,
                    "datatype": native_dt,
                    "maxLength": max_len,
                    "mandatory": is_mand,
                    "description": c_desc,
                }
                if dmn_name and dmn_name.lower() not in self.domains:
                    self.domains[dmn_name.lower()] = {
                        "name": dmn_name.lower(),
                        "datatype": native_dt,
                        "inferred_from_table": tbl_name,
                    }

            # 2. Legacy/mock <Field> elements
            for fld in root.findall(".//Field"):
                f_name = (fld.attrib.get("name") or fld.findtext("name") or "").strip().lower()
                if not f_name or f_name in fields_map:
                    continue
                dmn_name = (fld.attrib.get("domain") or fld.findtext("domain") or "").strip()
                native_dt = (fld.attrib.get("type") or fld.findtext("type") or "").strip()
                fields_map[f_name] = {
                    "name": f_name,
                    "domain": dmn_name,
                    "datatype": native_dt,
                    "mandatory": (fld.attrib.get("mandatory") or "false").lower() == "true",
                    "description": (fld.attrib.get("description") or fld.findtext("description") or "").strip(),
                }
                if dmn_name and dmn_name.lower() not in self.domains:
                    self.domains[dmn_name.lower()] = {
                        "name": dmn_name.lower(),
                        "datatype": native_dt,
                        "inferred_from_table": tbl_name,
                    }

            indices_list: List[Dict[str, Any]] = []
            for idx in root.findall(".//Index"):
                idx_name = (idx.attrib.get("name") or idx.findtext("name") or "").strip()
                is_pk = (idx.findtext("isPrimaryKey") or idx.attrib.get("primary") or "false").lower() == "true"
                is_uniq = (idx.findtext("isUnique") or idx.attrib.get("unique") or "false").lower() == "true"
                cols: List[str] = []
                for ic in idx.findall(".//IndexColumn"):
                    col_ref = (ic.findtext("column") or ic.attrib.get("column") or ic.attrib.get("name") or "").strip().lower()
                    if col_ref:
                        cols.append(col_ref)
                for mf in idx.findall(".//FieldRef"):
                    col_ref = (mf.attrib.get("name") or mf.text or "").strip().lower()
                    if col_ref:
                        cols.append(col_ref)
                indices_list.append({
                    "name": idx_name,
                    "primary": is_pk,
                    "unique": is_uniq,
                    "columns": cols,
                })

            entry = {
                "name": tbl_name,
                "description": desc,
                "fields": fields_map,
                "indices": indices_list,
            }
            self.tables[tbl_name] = entry
            return {"type": "table", "name": tbl_name, "entry": entry}

        elif root_tag == "DR_Domain":
            dmn_name = (root.attrib.get("name") or root.findtext("name") or hint_name).strip().lower()
            if not dmn_name:
                return None
            desc = (root.findtext("description") or root.attrib.get("description") or "").strip()
            dt_node = root.find("datatype")
            native_dt = ""
            facets: Dict[str, str] = {}
            if dt_node is not None:
                native_dt = (dt_node.findtext("nativeDatatype") or dt_node.attrib.get("nativeDatatype") or "").strip()
                for facet in dt_node.findall("Facet"):
                    ftype = (facet.findtext("type") or "").strip()
                    fval = (facet.findtext("value") or "").strip()
                    if ftype:
                        facets[ftype] = fval
            if not native_dt:
                native_dt = (root.attrib.get("type") or root.findtext("type") or "").strip()

            enums: Dict[str, Dict[str, Any]] = {}
            for en in root.findall(".//Enumeration"):
                e_name = (en.attrib.get("name") or en.findtext("name") or "").strip()
                if e_name:
                    enums[e_name] = {
                        "position": (en.findtext("position") or en.attrib.get("position") or "").strip(),
                        "description": (en.findtext("description") or en.attrib.get("description") or "").strip(),
                        "label": (en.findtext("descriptionReference") or "").strip(),
                    }
            for ev in root.findall(".//EnumValue"):
                e_name = (ev.attrib.get("name") or ev.attrib.get("const") or ev.findtext("name") or "").strip()
                if e_name and e_name not in enums:
                    enums[e_name] = {
                        "position": (ev.attrib.get("value") or "").strip(),
                        "description": (ev.attrib.get("description") or "").strip(),
                    }

            entry = {
                "name": dmn_name,
                "description": desc,
                "datatype": native_dt,
                "facets": facets,
                "enums": enums,
            }
            self.domains[dmn_name] = entry
            return {"type": "domain", "name": dmn_name, "entry": entry}

        return None

    def index_xml_file(self, xml_path: Path, save_cache: bool = True) -> Optional[Dict[str, Any]]:
        if not xml_path.exists():
            return None
        try:
            xml_text = xml_path.read_text(encoding="utf-8", errors="replace")
            res = self.index_xml_content(xml_text, hint_name=xml_path.stem)
            if res and save_cache and self.cache_path:
                self.save()
            return res
        except Exception:
            return None


# ============================================================================
# Lightweight Pure-Python Tokenizer & Recursive-Descent AST Parser (SYN001 & CAV003)
# ============================================================================


@dataclass
class Token4GL:
    kind: str  # 'WORD', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'COLON', 'ASSIGN', 'DIRECTIVE', 'SYMBOL'
    value: str
    line: int
    column: int
    raw_line: str = ""


@dataclass
class FunctionASTNode:
    name: str
    line: int
    end_line: int = 0
    return_type: str = ""
    params: str = ""
    direct_tx_calls: List[Tuple[str, int, int, str]] = field(default_factory=list)
    callees: List[Tuple[str, int, int, str]] = field(default_factory=list)
    calls_inside_tx: List[Tuple[str, int, int, str, int]] = field(default_factory=list)
    nested_tx_starts: List[Tuple[str, int, int, str, int]] = field(default_factory=list)


class ASTParser4GL:
    """
    Zero-dependency pure-Python tokenizer & recursive-descent block/AST analyzer for Baan 4GL.
    Handles:
    - Preprocessor `#define` macros (including multi-line `\\` continuations)
    - Pipe comments (`|`) and string literals (`"..."`, `'...'`)
    - Multi-line `dllusage ... enddllusage` and `functionusage ... endfunctionusage`
    - Multi-line Embedded SQL (`select ... selectdo ... selectempty ... selecteos ... endselect`)
      while ignoring SQL subqueries inside parentheses `where exists (select ...)`
    - Control blocks (`if`/`endif`, `for =`/`endfor`, `while`/`endwhile`, `repeat`/`until`, `on case`/`endcase`)
    - Intra-file Function Call Graph and transaction state tracking for `CAV003`
    """

    def __init__(self, content: str, file_path: str = "<stdin>"):
        self.content = content
        self.file_path = file_path
        self.raw_lines = content.splitlines()
        self.cleaned_lines: List[str] = []
        self.tokens: List[Token4GL] = []
        self.diagnostics: List[Diagnostic] = []
        self.functions: Dict[str, FunctionASTNode] = {}

    def preprocess_and_tokenize(self) -> List[str]:
        """
        Strip comments, string literals, doc blocks, and preprocessor `#define` bodies,
        producing both cleaned code lines and a structured token stream.
        """
        in_multiline_doc = False
        in_define_continuation = False
        self.cleaned_lines = []
        self.tokens = []

        for line_no, raw_line in enumerate(self.raw_lines, start=1):
            stripped_lower = raw_line.strip().lower()

            # Multi-line doc blocks
            if in_multiline_doc:
                self.cleaned_lines.append("")
                if "enddllusage" in stripped_lower or "endfunctionusage" in stripped_lower:
                    in_multiline_doc = False
                continue

            if stripped_lower.startswith("dllusage") or stripped_lower.startswith("functionusage"):
                self.cleaned_lines.append("")
                in_multiline_doc = True
                continue

            # Strip strings and pipe comments first
            code_line, _ = strip_4gl_comments_and_strings(raw_line, False)
            code_stripped = code_line.strip()

            # Handle multi-line #define continuations so macro expansion bodies don't corrupt AST blocks
            if in_define_continuation:
                self.cleaned_lines.append("")
                if not code_stripped.endswith("\\"):
                    in_define_continuation = False
                continue

            if re.match(r"^\s*#\s*(define|pragma|ident|ifdef|ifndef|elif|else|endif|undef)\b", code_line, re.IGNORECASE):
                if code_stripped.endswith("\\"):
                    in_define_continuation = True
                self.cleaned_lines.append("")
                continue

            self.cleaned_lines.append(code_line)

            # Check #context_on / #context_off directives
            m_ctx_on = re.match(r'^\s*#context_on\s*(?:["\']([^"\']+)["\'])?', raw_line, re.IGNORECASE)
            if m_ctx_on:
                ctx_name = m_ctx_on.group(1) or "unknown"
                self.tokens.append(Token4GL("DIRECTIVE", f"#context_on:{ctx_name}", line_no, 1, raw_line))
                continue
            if re.match(r"^\s*#context_off\b", raw_line, re.IGNORECASE):
                self.tokens.append(Token4GL("DIRECTIVE", "#context_off", line_no, 1, raw_line))
                continue
            if re.match(r"^\s*#include\b", raw_line, re.IGNORECASE):
                continue

            # Tokenize cleaned line
            token_pattern = re.compile(
                r"(\{|\}|\(|\)|:=|==|<>|<=|>=|=|:|,|;|\b[a-zA-Z_][a-zA-Z0-9_.]*\b)"
            )
            for match in token_pattern.finditer(code_line):
                val = match.group(0)
                col = match.start() + 1
                if val == "{":
                    kind = "LBRACE"
                elif val == "}":
                    kind = "RBRACE"
                elif val == "(":
                    kind = "LPAREN"
                elif val == ")":
                    kind = "RPAREN"
                elif val == ":":
                    kind = "COLON"
                elif val in ("=", ":="):
                    kind = "ASSIGN"
                elif val[0].isalpha() or val[0] == "_":
                    kind = "WORD"
                else:
                    kind = "SYMBOL"
                self.tokens.append(Token4GL(kind, val, line_no, col, raw_line))

        return self.cleaned_lines

    def parse(self) -> Tuple[List[Diagnostic], Dict[str, FunctionASTNode]]:
        """
        Run recursive-descent / state-machine AST verification for block balance (SYN001)
        and build intra-file FunctionASTNodes for Call Graph transaction analysis (CAV003).
        """
        if not self.cleaned_lines and self.raw_lines:
            self.preprocess_and_tokenize()

        block_stack: List[Tuple[str, int, str]] = []  # (block_type, line_no, extra_state)
        context_stack: List[Tuple[str, int]] = []
        brace_stack: List[Tuple[str, int]] = []

        paren_depth = 0
        current_func: Optional[FunctionASTNode] = None
        tx_active_since_line: Optional[int] = None

        n = len(self.tokens)
        i = 0

        while i < n:
            tok = self.tokens[i]
            val_lower = tok.value.lower()

            # 1. Directives (#context_on / #context_off)
            if tok.kind == "DIRECTIVE":
                if tok.value.startswith("#context_on:"):
                    ctx_name = tok.value.split(":", 1)[1]
                    if context_stack:
                        parent_type, parent_line = context_stack[-1]
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                f"Nested '#context_on' is not allowed: block '{ctx_name}' opened inside '{parent_type}' (line {parent_line}).",
                                tok.raw_line,
                            )
                        )
                    context_stack.append((f'#context_on "{ctx_name}"', tok.line))
                elif tok.value == "#context_off":
                    if not context_stack:
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                "Unmatched '#context_off' without corresponding '#context_on'.",
                                tok.raw_line,
                            )
                        )
                    else:
                        context_stack.pop()
                i += 1
                continue

            # 2. Parentheses tracking (used to distinguish SQL subqueries `(select ...)` from top-level `select`)
            if tok.kind == "LPAREN":
                paren_depth += 1
                i += 1
                continue
            if tok.kind == "RPAREN":
                paren_depth = max(0, paren_depth - 1)
                i += 1
                continue

            # 3. Curly Braces & Function body tracking
            if tok.kind == "LBRACE":
                brace_stack.append(("{", tok.line))
                i += 1
                continue
            if tok.kind == "RBRACE":
                if not brace_stack:
                    self.diagnostics.append(
                        Diagnostic(
                            self.file_path,
                            tok.line,
                            tok.column,
                            "ERROR",
                            "SYN001",
                            "Unmatched closing brace '}'.",
                            tok.raw_line,
                        )
                    )
                else:
                    brace_stack.pop()
                    if current_func and not brace_stack:
                        current_func.end_line = tok.line
                        current_func = None
                        tx_active_since_line = None
                i += 1
                continue

            # 4. Function Declarations: `function [extern] [<type>] <name>(...)`
            if tok.kind == "WORD" and val_lower == "function" and not brace_stack:
                # Look ahead for function name before `(`
                j = i + 1
                words_before_paren: List[Token4GL] = []
                while j < n and self.tokens[j].kind == "WORD" and self.tokens[j].line == tok.line:
                    words_before_paren.append(self.tokens[j])
                    j += 1
                if words_before_paren and j < n and self.tokens[j].kind == "LPAREN":
                    fn_tok = words_before_paren[-1]
                    fn_name = fn_tok.value.lower()
                    fn_node = FunctionASTNode(name=fn_name, line=tok.line)
                    self.functions[fn_name] = fn_node
                    current_func = fn_node
                    tx_active_since_line = None
                i += 1
                continue

            # 5. Control & SQL Block Keywords
            if tok.kind == "WORD":
                # ON CASE
                if val_lower == "on" and i + 1 < n and self.tokens[i + 1].kind == "WORD" and self.tokens[i + 1].value.lower() == "case":
                    block_stack.append(("case", tok.line, "open"))
                    i += 2
                    continue

                if val_lower == "endcase":
                    if not block_stack or block_stack[-1][0] != "case":
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                "Unmatched 'endcase' without corresponding 'on case'.",
                                tok.raw_line,
                            )
                        )
                    else:
                        block_stack.pop()
                    i += 1
                    continue

                # SELECT / SELECTDO / SELECTEMPTY / SELECTEOS / ENDSELECT
                if val_lower == "select":
                    # Only top-level select (not inside parentheses subquery `where exists (select ...)`) requires endselect
                    if paren_depth == 0:
                        block_stack.append(("select", tok.line, "query"))
                    i += 1
                    continue

                if val_lower in ("selectdo", "selectempty", "selecteos"):
                    # Find nearest select block on stack
                    select_idx = -1
                    for idx in range(len(block_stack) - 1, -1, -1):
                        if block_stack[idx][0] == "select":
                            select_idx = idx
                            break
                    if select_idx == -1:
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                f"'{val_lower}' statement outside of an active 'select' block.",
                                tok.raw_line,
                            )
                        )
                    else:
                        # Update select phase
                        sel_type, sel_line, _ = block_stack[select_idx]
                        block_stack[select_idx] = (sel_type, sel_line, val_lower)
                    i += 1
                    continue

                if val_lower == "endselect":
                    if not block_stack or block_stack[-1][0] != "select":
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                "Unmatched 'endselect' without corresponding 'select'.",
                                tok.raw_line,
                            )
                        )
                    else:
                        block_stack.pop()
                    i += 1
                    continue

                # FOR <var> = <init> TO <limit> (exclude SQL `for update`)
                if val_lower == "for":
                    if (
                        i + 2 < n
                        and self.tokens[i + 1].kind == "WORD"
                        and self.tokens[i + 1].value.lower() != "update"
                        and self.tokens[i + 2].kind == "ASSIGN"
                    ):
                        block_stack.append(("for", tok.line, "loop"))
                    i += 1
                    continue

                if val_lower == "endfor":
                    if not block_stack or block_stack[-1][0] != "for":
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                "Unmatched 'endfor' without corresponding 'for'.",
                                tok.raw_line,
                            )
                        )
                    else:
                        block_stack.pop()
                    i += 1
                    continue

                # WHILE / ENDWHILE
                if val_lower == "while":
                    block_stack.append(("while", tok.line, "loop"))
                    i += 1
                    continue

                if val_lower == "endwhile":
                    if not block_stack or block_stack[-1][0] != "while":
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                "Unmatched 'endwhile' without corresponding 'while'.",
                                tok.raw_line,
                            )
                        )
                    else:
                        block_stack.pop()
                    i += 1
                    continue

                # REPEAT / UNTIL
                if val_lower == "repeat":
                    block_stack.append(("repeat", tok.line, "loop"))
                    i += 1
                    continue

                if val_lower == "until":
                    if not block_stack or block_stack[-1][0] != "repeat":
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                "Unmatched 'until' without corresponding 'repeat'.",
                                tok.raw_line,
                            )
                        )
                    else:
                        block_stack.pop()
                    i += 1
                    continue

                # IF / ENDIF
                if val_lower == "if":
                    block_stack.append(("if", tok.line, "cond"))
                    i += 1
                    continue

                if val_lower == "endif":
                    if not block_stack or block_stack[-1][0] != "if":
                        self.diagnostics.append(
                            Diagnostic(
                                self.file_path,
                                tok.line,
                                tok.column,
                                "ERROR",
                                "SYN001",
                                "Unmatched 'endif' without corresponding 'if'.",
                                tok.raw_line,
                            )
                        )
                    else:
                        block_stack.pop()
                    i += 1
                    continue

                # 6. Function Calls & Transaction State Tracking inside Function Bodies
                if current_func is not None and i + 1 < n and self.tokens[i + 1].kind == "LPAREN":
                    # Exclude the function's own declaration header on `current_func.line`
                    if tok.line != current_func.line or val_lower != current_func.name:
                        if val_lower in ("db.retry.point", "commit.transaction", "abort.transaction"):
                            current_func.direct_tx_calls.append((val_lower, tok.line, tok.column, tok.raw_line))
                            if val_lower == "db.retry.point":
                                if tx_active_since_line is not None:
                                    current_func.nested_tx_starts.append(
                                        (val_lower, tok.line, tok.column, tok.raw_line, tx_active_since_line)
                                    )
                                else:
                                    tx_active_since_line = tok.line
                            elif val_lower in ("commit.transaction", "abort.transaction"):
                                tx_active_since_line = None
                        else:
                            current_func.callees.append((val_lower, tok.line, tok.column, tok.raw_line))
                            if tx_active_since_line is not None:
                                current_func.calls_inside_tx.append(
                                    (val_lower, tok.line, tok.column, tok.raw_line, tx_active_since_line)
                                )

            i += 1

        # End-of-file unclosed blocks (SYN001)
        while block_stack:
            blk_type, blk_line, _ = block_stack.pop()
            self.diagnostics.append(
                Diagnostic(
                    self.file_path,
                    blk_line,
                    1,
                    "ERROR",
                    "SYN001",
                    f"Unclosed '{blk_type}' statement opened at line {blk_line}.",
                )
            )

        while context_stack:
            ctx_type, ctx_line = context_stack.pop()
            self.diagnostics.append(
                Diagnostic(
                    self.file_path,
                    ctx_line,
                    1,
                    "ERROR",
                    "SYN001",
                    f"Unclosed '{ctx_type}' opened at line {ctx_line}.",
                )
            )

        while brace_stack:
            brace_char, brace_line = brace_stack.pop()
            self.diagnostics.append(
                Diagnostic(
                    self.file_path,
                    brace_line,
                    1,
                    "ERROR",
                    "SYN001",
                    f"Unclosed brace '{brace_char}' opened at line {brace_line}.",
                )
            )

        return self.diagnostics, self.functions

    def find_transitive_tx_functions(self) -> Dict[str, List[str]]:
        """
        Compute transitive closure over the intra-file Call Graph to identify every
        function that directly or transitively calls `db.retry.point()`,
        `commit.transaction()`, or `abort.transaction()`.
        Returns mapping: `func_name -> chain_description` (e.g. `["helper_b", "commit.transaction()"]`).
        """
        tx_map: Dict[str, List[str]] = {}
        for fname, fnode in self.functions.items():
            if fnode.direct_tx_calls:
                tx_fn = fnode.direct_tx_calls[0][0]
                tx_map[fname] = [f"{tx_fn}()"]

        # Iterative relaxation for transitive callers
        changed = True
        while changed:
            changed = False
            for fname, fnode in self.functions.items():
                if fname in tx_map:
                    continue
                for callee_name, _, _, _ in fnode.callees:
                    if callee_name in tx_map:
                        tx_map[fname] = [callee_name] + tx_map[callee_name]
                        changed = True
                        break
        return tx_map


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
        main_table: Optional[str] = None,
        dd_cache: Optional[Union[DataDictionaryCache, Dict[str, Any], Path, str]] = None,
        auto_fetch_dd: bool = False,
        auto_fetch_callback: Optional[Callable[[str, str], Optional[str]]] = None,
    ):
        if not skill_dir:
            skill_dir = Path(__file__).resolve().parent.parent

        self.skill_dir = skill_dir
        self.cloud_mode = cloud_mode
        self.min_severity_level = SEVERITY_LEVELS.get(min_severity.upper(), 0)
        self.strict = strict
        self.main_table = main_table.lower().strip() if main_table else None
        self.auto_fetch_dd = auto_fetch_dd
        self.auto_fetch_callback = auto_fetch_callback

        if isinstance(dd_cache, DataDictionaryCache):
            self.dd_cache: Optional[DataDictionaryCache] = dd_cache
        elif isinstance(dd_cache, dict):
            self.dd_cache = DataDictionaryCache(raw_data=dd_cache)
        elif isinstance(dd_cache, (Path, str)):
            self.dd_cache = DataDictionaryCache(cache_path=Path(dd_cache))
        else:
            self.dd_cache = None

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

        # Explicit session / session extension indicators
        is_session = (
            re.search(r"[a-z]{5}\d{3,4}[ms]\d{3}", path_lower) is not None
            or re.search(r"m\d{3}", path_lower) is not None
            or "bic_sessionext" in content.lower()
            or "bic_interface" in content.lower()
            or "/session" in path_lower.replace("\\", "/")
            or "\\session" in path_lower
            or "ess" in path_lower
        )
        if is_session:
            return "general"

        # Content heuristics
        if "function extern long before.save.object" in content.lower() or "dal.set.error.message" in content.lower() or "bic_tableext" in content.lower():
            return "dal2"
        if ("table" in path_lower or "est" in path_lower) and ("_ext.4gl" in path_lower or ".4gl" in path_lower or ".cln" in path_lower):
            return "dal2"
        if "bic_dal2" in content.lower():
            return "dal2"
        if "ue.before.save" in content.lower() or "ue.after.save" in content.lower():
            return "uedll"

        return "general"

    def infer_main_table(self, file_path: str, content: str, mode: str) -> Optional[str]:
        """Infer the component's main table from CLI configuration, filename, or DAL hook definitions."""
        if self.main_table:
            return self.main_table

        if file_path and file_path != "<stdin>":
            stem = Path(file_path).stem.lower()
            if stem.endswith("_ext"):
                stem = stem[:-4]
            # Standard LN table code: 5 letters + 3 digits (e.g., txsli001, tcibd001)
            if re.match(r"^[a-z]{5}\d{3}$", stem):
                return stem

        # Check DAL2 field hooks in script: `function extern <ret> <table>.<field>.<hook_suffix>(...)`
        if mode == "dal2":
            for sfx in self.dal_field_hooks:
                pattern = rf"\bfunction\s+extern\s+[a-zA-Z0-9_.]+\s+([a-z]{{5}}\d{{3}})\.[a-z0-9_]+{re.escape(sfx)}\s*\("
                m = re.search(pattern, content, re.IGNORECASE)
                if m:
                    return m.group(1).lower()

        return None

    def _resolve_dd_cache(self, file_path: str) -> DataDictionaryCache:
        """Locate or initialize the active DataDictionaryCache for the target file."""
        if self.dd_cache is not None:
            return self.dd_cache

        search_dirs: List[Path] = []
        if file_path and file_path != "<stdin>":
            p = Path(file_path).resolve()
            search_dirs.extend([p.parent] + list(p.parents[:5]))
        search_dirs.append(Path.cwd())

        for d in search_dirs:
            candidate = d / ".ln_dd_cache.json"
            if candidate.exists():
                return DataDictionaryCache(cache_path=candidate)

        default_path = (Path(file_path).resolve().parent if file_path and file_path != "<stdin>" else Path.cwd()) / ".ln_dd_cache.json"
        return DataDictionaryCache(cache_path=default_path)

    def _try_auto_fetch_dd(self, dd_cache: DataDictionaryCache, comp_type: str, comp_name: str, file_path: str) -> bool:
        """
        Attempt to fetch a missing `.tbl` or `.dmn` read-only from the server (or custom callback)
        and index it into `.ln_dd_cache.json`.
        """
        if not self.auto_fetch_dd:
            return False

        # 1. Custom callback hook (useful for unit tests & dependency injection)
        if self.auto_fetch_callback is not None:
            try:
                xml_str = self.auto_fetch_callback(comp_type, comp_name)
                if xml_str:
                    dd_cache.index_xml_content(xml_str, hint_name=comp_name)
                    if dd_cache.cache_path:
                        dd_cache.save()
                    return True
            except Exception:
                pass
            return False

        # 2. Local workspace `.tbl` / `.dmn` search before hitting network
        ext = ".tbl" if comp_type == "table" else ".dmn"
        if file_path and file_path != "<stdin>":
            base_dir = Path(file_path).resolve().parent
            for parent in [base_dir] + list(base_dir.parents[:3]):
                for match_file in parent.rglob(f"{comp_name}{ext}"):
                    if dd_cache.index_xml_file(match_file, save_cache=True):
                        return True

        # 3. Invoke ln_studio_skill ComponentExplorer / Server Client read-only
        try:
            tools_dir = Path(__file__).resolve().parent.parent.parent / "ln_studio_skill" / "tools"
            if tools_dir.exists() and str(tools_dir) not in sys.path:
                sys.path.insert(0, str(tools_dir))
            from ln_server_client import LNStudioServerClient
            from ln_component_explorer import ComponentExplorer

            ws_dir = Path(file_path).resolve().parent if file_path and file_path != "<stdin>" else Path.cwd()
            client = LNStudioServerClient(workspace_dir=ws_dir)
            explorer = ComponentExplorer(client)
            res = explorer.sync_reference(
                comp_type=comp_type,
                name_pattern=comp_name,
                workspace_dir=ws_dir,
                dd_cache_path=dd_cache.cache_path,
            )
            if res.get("synced_count", 0) > 0 and dd_cache.cache_path and dd_cache.cache_path.exists():
                dd_cache.load(dd_cache.cache_path)
                return True
        except Exception:
            pass

        return False

    def audit_content(
        self,
        content: str,
        file_path: str = "<stdin>",
        mode: Optional[str] = None,
        main_table: Optional[str] = None,
        dd_cache: Optional[Union[DataDictionaryCache, Dict[str, Any], Path, str]] = None,
        auto_fetch_dd: Optional[bool] = None,
    ) -> List[Diagnostic]:
        """Perform comprehensive semantic, schema, and AST static verification on 4GL script content."""
        if not mode or mode == "auto":
            mode = self.detect_archetype(file_path, content)

        effective_main_table = (
            main_table.lower().strip()
            if main_table
            else self.infer_main_table(file_path, content, mode)
        )
        effective_auto_fetch = self.auto_fetch_dd if auto_fetch_dd is None else auto_fetch_dd

        if isinstance(dd_cache, DataDictionaryCache):
            active_dd_cache = dd_cache
        elif isinstance(dd_cache, dict):
            active_dd_cache = DataDictionaryCache(raw_data=dd_cache)
        elif isinstance(dd_cache, (Path, str)):
            active_dd_cache = DataDictionaryCache(cache_path=Path(dd_cache))
        else:
            active_dd_cache = self._resolve_dd_cache(file_path)

        diagnostics: List[Diagnostic] = []
        lines = content.splitlines()

        # Run AST Tokenizer & Recursive-Descent Block/Call-Graph Parser (SYN001 & CAV003)
        ast_parser = ASTParser4GL(content, file_path)
        cleaned_lines = ast_parser.preprocess_and_tokenize()
        ast_diags, ast_functions = ast_parser.parse()
        diagnostics.extend(ast_diags)
        transitive_tx_map = ast_parser.find_transitive_tx_functions()

        # Includes collection: `#include <header>` or `#include "header"`
        includes_found: Set[str] = set()
        for raw_line in lines:
            m_inc = re.match(r'^\s*#include\s+[<"]([a-zA-Z0-9_.]+)[>"]', raw_line)
            if m_inc:
                inc_name = m_inc.group(1).lower()
                if inc_name.endswith(".h"):
                    inc_name = inc_name[:-2]
                includes_found.add(inc_name)

        # ----------------------------------------------------
        # Pass 1: Extract `table t<tablename>` declarations (TBL001)
        # ----------------------------------------------------
        declared_tables: Set[str] = set()
        for code_line in cleaned_lines:
            if re.search(r"\btable\b", code_line, re.IGNORECASE):
                for m_tbl in re.finditer(r"\bt([a-z]{5}\d{3})\b", code_line, re.IGNORECASE):
                    declared_tables.add(m_tbl.group(1).lower())

        in_case_block = False
        brace_depth = 0
        had_positive_brace = False
        current_func_name: Optional[str] = None
        current_func_ret_type: Optional[str] = None
        current_func_is_void: bool = False
        current_func_hook_suffix: Optional[str] = None
        reported_tbl001: Set[Tuple[str, int]] = set()
        fetched_attempts: Set[Tuple[str, str]] = set()

        # Extension Modeler state
        path_lower = file_path.lower()
        stem = Path(file_path).stem.lower() if file_path and file_path != "<stdin>" else ""
        content_lower = content.lower()
        is_extension = (
            "#context_on" in content_lower
            or path_lower.endswith(".cln")
            or "_ext.4gl" in path_lower
            or "/est/" in path_lower.replace("\\", "/")
            or "/ess/" in path_lower.replace("\\", "/")
            or "table_extension" in path_lower
            or "session_extension" in path_lower
        )
        is_session_ext = is_extension and (
            re.search(r"[a-z]{5}\d{3,4}[ms]\d{3}", path_lower) is not None
            or re.search(r"m\d{3}", path_lower) is not None
            or "bic_sessionext" in content_lower
            or "bic_interface" in content_lower
            or "/session" in path_lower.replace("\\", "/")
            or "\\session" in path_lower
            or "ess" in path_lower
        )
        is_table_ext = is_extension and not is_session_ext and (
            re.match(r"^(?:txest)?[a-z]{5}\d{3}(?:_ext)?$", stem) is not None
            or "bic_tableext" in content_lower
            or "/table" in path_lower.replace("\\", "/")
            or "\\table" in path_lower
            or "est" in path_lower
        )
        current_context: Optional[str] = None
        declarations_includes: Set[str] = set()
        dal_call_lines: List[Tuple[int, str]] = []

        for line_no, raw_line in enumerate(lines, start=1):
            code_line = cleaned_lines[line_no - 1] if line_no - 1 < len(cleaned_lines) else ""
            code_line_stripped = code_line.strip()
            if not code_line_stripped:
                continue

            # Directives (#context_on / #context_off)
            m_ctx = re.match(r'^\s*#context_on\s*(?:["\']([^"\']+)["\'])?', raw_line, re.IGNORECASE)
            if m_ctx:
                ctx_name = (m_ctx.group(1) or "").strip()
                current_context = ctx_name.lower()
                ctx_lower = ctx_name.lower()
                is_cmd_hook = (
                    ctx_lower.startswith("function.")
                    and (ctx_lower.endswith(".before.command") or ctx_lower.endswith(".after.command")
                         or ctx_lower.endswith(".is.enabled") or ctx_lower.endswith(".is.visible"))
                ) or ctx_lower.endswith(".before.command") or ctx_lower.endswith(".after.command")

                is_dal_hook = (
                    ctx_lower in ("before.save.object", "after.save.object", "before.destroy.object",
                                  "after.destroy.object", "before.open.object.set", "after.open.object.set",
                                  "method.is.allowed", "set.object.defaults", "ue.before.save", "ue.after.save")
                    or any(ctx_lower.endswith(sfx) for sfx in self.dal_field_hooks)
                )

                if is_table_ext and is_cmd_hook:
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "EXT002",
                            f"Form Command hook '{ctx_name}' is not supported in Table Extension; Form Command hooks belong in Session Extensions.",
                            raw_line,
                        )
                    )
                elif is_session_ext and is_dal_hook:
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "EXT002",
                            f"Table DAL hook '{ctx_name}' is not supported in Session Extension; Table DAL hooks belong in Table Extensions.",
                            raw_line,
                        )
                    )

            if re.match(r"^\s*#context_off\b", raw_line, re.IGNORECASE):
                current_context = None

            # EXT001: Check #include placement in Extension Scripts
            if is_extension:
                m_inc = re.match(r'^\s*#include\s+([<"][^>"]+[>"])', raw_line, re.IGNORECASE)
                if m_inc:
                    inc_raw = m_inc.group(1)
                    inc_clean = inc_raw.strip("<>\".h").lower()
                    if current_context == "declarations":
                        declarations_includes.add(inc_clean)
                    else:
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "EXT001",
                                f"Direct '#include {inc_raw}' outside '#context_on \"declarations\"' will not be compiled by Extension Modeler; move inside '#context_on \"declarations\"' block.",
                                raw_line,
                            )
                        )

            # EXT001: Track DAL calls in Extension Scripts
            if is_extension and re.search(r"\b(dal\.change\.object|dal\.set\.field|dal\.save\.object|dal\.new\.object|dal\.destroy\.object)\s*\(", code_line, re.IGNORECASE):
                dal_call_lines.append((line_no, raw_line))

            # Track case context for section header disambiguation
            if re.search(r"(?<![.\w])on\s+case(?![.\w])", code_line, re.IGNORECASE):
                in_case_block = True
            elif re.search(r"(?<![.\w])endcase(?![.\w])", code_line, re.IGNORECASE):
                in_case_block = False

            for ch in code_line:
                if ch == "{":
                    brace_depth += 1
                    had_positive_brace = True
                elif ch == "}":
                    brace_depth = max(0, brace_depth - 1)

            # ----------------------------------------------------
            # 1. Section Header Checks (SYN002)
            # ----------------------------------------------------
            sec_match = re.match(r"^([a-zA-Z0-9_.]+)\s*:$", code_line_stripped)
            if sec_match:
                raw_token = sec_match.group(1)
                header_name = raw_token.lower() + ":"

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
            # 2. Table Declaration (TBL001) & Schema Field/Domain Checks (TBL002, DMN001)
            # ----------------------------------------------------
            # 2a. Domain declarations: `domain <domain_name> <var>`
            for m_dmn in re.finditer(r"\bdomain\s+([a-zA-Z][a-zA-Z0-9_.]*)\b", code_line, re.IGNORECASE):
                dmn_name = m_dmn.group(1)
                dmn_lower = dmn_name.lower()
                if dmn_lower in ("error", "true", "false"):
                    continue
                if not active_dd_cache.has_domain(dmn_lower) and effective_auto_fetch:
                    if ("domain", dmn_lower) not in fetched_attempts:
                        fetched_attempts.add(("domain", dmn_lower))
                        self._try_auto_fetch_dd(active_dd_cache, "domain", dmn_lower, file_path)
                if (active_dd_cache.domains or effective_auto_fetch) and not active_dd_cache.has_domain(dmn_lower):
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            m_dmn.start(1) + 1,
                            "ERROR",
                            "DMN001",
                            f"Domain '{dmn_name}' does not exist in Data Dictionary cache (.ln_dd_cache.json).",
                            raw_line,
                        )
                    )

            # 2b. Table field references: `<table>.<field>` (matching `([a-z]{5}\d{3})\.([a-z0-9_]+)`)
            for m_ref in re.finditer(r"(?<![a-zA-Z0-9_.])([a-z]{5}\d{3})\.([a-z0-9_]+)", code_line, re.IGNORECASE):
                prefix_before = code_line[: m_ref.start()].rstrip().lower()
                # Skip if preceded by `domain` or `zoom.from`
                if re.search(r"\bdomain$", prefix_before) or prefix_before.endswith("zoom.from"):
                    continue

                tbl_code = m_ref.group(1).lower()
                fld_code = m_ref.group(2).lower()
                col_pos = m_ref.start(1) + 1

                # Rule TBL001: Check table declaration in `declaration:` (excluding component's main table)
                if tbl_code != effective_main_table and tbl_code not in declared_tables:
                    if (tbl_code, line_no) not in reported_tbl001:
                        reported_tbl001.add((tbl_code, line_no))
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                col_pos,
                                "ERROR",
                                "TBL001",
                                f"Table '{tbl_code}' referenced via '{tbl_code}.{fld_code}' is missing 'table t{tbl_code}' in declaration: section.",
                                raw_line,
                            )
                        )

                # Rule TBL002: Validate field existence against `.ln_dd_cache.json`
                if not active_dd_cache.has_table(tbl_code) and effective_auto_fetch:
                    if ("table", tbl_code) not in fetched_attempts:
                        fetched_attempts.add(("table", tbl_code))
                        self._try_auto_fetch_dd(active_dd_cache, "table", tbl_code, file_path)

                if active_dd_cache.has_table(tbl_code):
                    if not active_dd_cache.has_field(tbl_code, fld_code):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                col_pos,
                                "ERROR",
                                "TBL002",
                                f"Field '{tbl_code}.{fld_code}' does not exist in Data Dictionary schema for table '{tbl_code}'.",
                                raw_line,
                            )
                        )
                elif effective_auto_fetch and ("table", tbl_code) in fetched_attempts:
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            col_pos,
                            "ERROR",
                            "TBL002",
                            f"Table '{tbl_code}' (for '{tbl_code}.{fld_code}') could not be found in Data Dictionary cache or server.",
                            raw_line,
                        )
                    )

            # ----------------------------------------------------
            # 3. Function & DAL Hook Signatures (DAL002, DAL003)
            # ----------------------------------------------------
            func_decl_match = re.match(
                r"^\s*(?:function\s+)?(?:extern\s+)?(?:([a-zA-Z0-9_.]+)\s+)?([a-zA-Z0-9_.]+)\s*\((.*?)\)",
                code_line,
                re.IGNORECASE,
            )
            if func_decl_match:
                f_candidate = func_decl_match.group(2).lower()
                if f_candidate in ("return", "if", "while", "for", "on", "case", "select", "endselect", "endif", "endwhile", "endfor", "endcase", "break", "continue") or f_candidate.startswith(("db.", "dal.", "commit.", "abort.", "message", "ask.", "box", "show.")):
                    func_decl_match = None

            if func_decl_match:
                ret_type = (func_decl_match.group(1) or "").lower()
                func_name = func_decl_match.group(2).lower()
                params = func_decl_match.group(3).strip()
                current_func_name = func_name
                current_func_ret_type = ret_type
                current_func_is_void = (
                    ret_type == "void"
                    or (not ret_type and (func_name.endswith(".before.command") or func_name.endswith(".after.command")))
                )
                current_func_hook_suffix = None

                # Check EXT002 on function declaration
                is_cmd_hook = (
                    func_name.startswith("function.")
                    and (func_name.endswith(".before.command") or func_name.endswith(".after.command")
                         or func_name.endswith(".is.enabled") or func_name.endswith(".is.visible"))
                ) or func_name.endswith(".before.command") or func_name.endswith(".after.command")
                is_dal_hook = (
                    func_name in ("before.save.object", "after.save.object", "before.destroy.object",
                                  "after.destroy.object", "before.open.object.set", "after.open.object.set",
                                  "method.is.allowed", "set.object.defaults", "ue.before.save", "ue.after.save")
                    or any(func_name.endswith(sfx) for sfx in self.dal_field_hooks)
                )

                if is_table_ext and is_cmd_hook:
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "EXT002",
                            f"Form Command hook '{func_name}' is not supported in Table Extension; Form Command hooks belong in Session Extensions.",
                            raw_line,
                        )
                    )
                elif is_session_ext and is_dal_hook:
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            1,
                            "ERROR",
                            "EXT002",
                            f"Table DAL hook '{func_name}' is not supported in Session Extension; Table DAL hooks belong in Table Extensions.",
                            raw_line,
                        )
                    )

                # Specific Extension & DAL Lifecycle Hooks
                if func_name == "before.save.object":
                    if ret_type in ("void", "boolean"):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Hook 'before.save.object' must return 'long' (returns error code or 0). Found: '{ret_type}'.",
                                raw_line,
                            )
                        )
                    if not re.search(r"\blong\s+[a-zA-Z0-9_.]+\b", params, re.IGNORECASE):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Hook 'before.save.object' must declare parameter 'long mode'. Found: '({params})'.",
                                raw_line,
                            )
                        )
                elif func_name == "after.save.object":
                    if ret_type and ret_type not in ("long", "void"):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Hook 'after.save.object' must return 'long' or 'void'. Found: '{ret_type}'.",
                                raw_line,
                            )
                        )
                elif func_name == "before.destroy.object":
                    if ret_type and ret_type not in ("long", "void"):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Hook 'before.destroy.object' must return 'long' or 'void'. Found: '{ret_type}'.",
                                raw_line,
                            )
                        )
                elif func_name == "after.destroy.object":
                    if ret_type and ret_type not in ("long", "void"):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Hook 'after.destroy.object' must return 'long' or 'void'. Found: '{ret_type}'.",
                                raw_line,
                            )
                        )
                elif func_name == "method.is.allowed":
                    if ret_type and ret_type != "boolean":
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Hook 'method.is.allowed' must return 'boolean'. Found: '{ret_type}'.",
                                raw_line,
                            )
                        )
                    if not re.search(r"\blong\s+[a-zA-Z0-9_.]+\b", params, re.IGNORECASE):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Hook 'method.is.allowed' must declare parameter 'long method'. Found: '({params})'.",
                                raw_line,
                            )
                        )
                elif func_name.endswith((".is.valid", ".is.readonly", ".is.mandatory", ".is.applicable", ".is.never.applicable")):
                    if ret_type and ret_type != "boolean":
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Field hook '{func_name}' must return 'boolean'. Found: '{ret_type}'.",
                                raw_line,
                            )
                        )
                elif func_name.startswith("function.") and (func_name.endswith(".is.enabled") or func_name.endswith(".is.visible")):
                    if ret_type and ret_type != "boolean":
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Command hook '{func_name}' must return 'boolean'. Found: '{ret_type}'.",
                                raw_line,
                            )
                        )
                elif func_name.startswith("function.") and (func_name.endswith(".before.command") or func_name.endswith(".after.command")):
                    if ret_type and ret_type not in ("void", "long"):
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL002",
                                f"Command hook '{func_name}' must return 'void' or 'long'. Found: '{ret_type}'. Form Command execution hooks in Extension Modeler have a 'void' prototype.",
                                raw_line,
                            )
                        )

                # Check if this matches a DAL field hook suffix
                for sfx, sfx_def in self.dal_field_hooks.items():
                    if func_name.endswith(sfx):
                        current_func_hook_suffix = sfx
                        if "void" in sfx_def.get("returnValue", ""):
                            current_func_is_void = True
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

            # DAL003 Check: return values inside void functions & DAL hooks
            if current_func_name is not None:
                ret_match = re.search(r"\breturn\s*(?:\((.*?)\)|([a-zA-Z0-9_.+\-*/\"':]+))", code_line, re.IGNORECASE)
                if ret_match:
                    ret_val = (ret_match.group(1) or ret_match.group(2) or "").strip()
                    if current_func_is_void and ret_val:
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                1,
                                "ERROR",
                                "DAL003",
                                f"Return value '{ret_val}' inside void function/hook '{current_func_name}' is not allowed in Baan 4GL; compiler blocks with 'Return value for void function not allowed'. Use bare 'return' or 'return()' without an expression.",
                                raw_line,
                            )
                        )
                    elif current_func_hook_suffix:
                        hook_info = self.dal_field_hooks.get(current_func_hook_suffix, {})
                        expected_ret = hook_info.get("returnValue", "")

                        if "boolean" in expected_ret:
                            if ret_val and ret_val.lower() not in ("true", "false", "0", "1"):
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
            # 4. Prohibited Interactive UI & Transaction Controls in DAL / Table Extensions (DAL001, DAL005)
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
                            f"Interactive dialog '{func_called}()' is prohibited in DAL scripts and Table Extension hooks; use 'dal.set.error.message()' instead.",
                            raw_line,
                        )
                    )

                trans_matches = re.finditer(r"(?<![.\w])(commit\.transaction|abort\.transaction|db\.retry\.point)\s*\(", code_line, re.IGNORECASE)
                for tm in trans_matches:
                    func_called = tm.group(1).lower()
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            line_no,
                            tm.start() + 1,
                            "ERROR",
                            "DAL005",
                            f"Transaction control '{func_called}()' is prohibited in DAL/Table Extension hooks; transaction lifecycle is managed by the DAL engine.",
                            raw_line,
                        )
                    )

            # ----------------------------------------------------
            # 5. Raw DB Mutation in UI Script (DAL004)
            # ----------------------------------------------------
            if mode == "general":
                db_mut_matches = re.finditer(
                    r"(?<![.\w])(db\.insert|db\.update|db\.delete|db\.write)\s*\(\s*([a-zA-Z0-9_]+)", code_line, re.IGNORECASE
                )
                for dbm in db_mut_matches:
                    mut_fn = dbm.group(1).lower()
                    target_tbl = dbm.group(2).lower()
                    tbl_name = target_tbl[1:] if target_tbl.startswith("t") and len(target_tbl) > 1 else target_tbl
                    is_temp = "temp" in tbl_name or tbl_name.endswith("010")
                    if active_dd_cache.has_table(tbl_name):
                        desc = (active_dd_cache.tables.get(tbl_name, {}).get("description") or "").lower()
                        if "temp" in desc:
                            is_temp = True
                    if not is_temp:
                        diagnostics.append(
                            Diagnostic(
                                file_path,
                                line_no,
                                dbm.start() + 1,
                                "ERROR",
                                "DAL004",
                                f"Direct database mutation '{mut_fn}()' on table '{tbl_name}' in UI script violates Separation of Concerns; use DAL2 instead.",
                                raw_line,
                            )
                        )

            # ----------------------------------------------------
            # 6. Direct Transaction Statements in DAL/UEDLL Subroutines (CAV003)
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

            # Reset current function state when exiting function curly braces
            if had_positive_brace and brace_depth == 0:
                current_func_name = None
                current_func_ret_type = None
                current_func_is_void = False
                current_func_hook_suffix = None
                had_positive_brace = False

        # ----------------------------------------------------
        # EXT001: Missing #include <bic_dam> or <bic_dal2> in declarations context
        # ----------------------------------------------------
        if is_extension and dal_call_lines:
            if "bic_dam" not in declarations_includes and "bic_dal2" not in declarations_includes:
                first_line, first_raw = dal_call_lines[0]
                diagnostics.append(
                    Diagnostic(
                        file_path,
                        first_line,
                        1,
                        "ERROR",
                        "EXT001",
                        "Missing '#include <bic_dam>' (or '<bic_dal2>') inside '#context_on \"declarations\"'; Extension Modeler compiler will fail with unresolved reference to function 'dal.*'.",
                        first_raw,
                    )
                )

        # ----------------------------------------------------
        # 9. Intra-File Call Graph Nested Transaction Detection (CAV003)
        # ----------------------------------------------------
        for fn_name, fn_node in ast_functions.items():
            # 9a. Direct nested db.retry.point() inside an already open transaction in the same function
            for tx_fn, call_line, call_col, raw_l, start_line in fn_node.nested_tx_starts:
                diagnostics.append(
                    Diagnostic(
                        file_path,
                        call_line,
                        call_col,
                        "ERROR",
                        "CAV003",
                        f"Nested transaction '{tx_fn}()' inside function '{fn_name}' while transaction opened at line {start_line} is still active.",
                        raw_l,
                    )
                )

            # 9b. Calling a helper function that directly or transitively starts/commits a transaction while inside an active transaction
            for callee_name, call_line, call_col, raw_l, start_line in fn_node.calls_inside_tx:
                if callee_name in transitive_tx_map:
                    chain = " -> ".join([callee_name] + transitive_tx_map[callee_name])
                    diagnostics.append(
                        Diagnostic(
                            file_path,
                            call_line,
                            call_col,
                            "ERROR",
                            "CAV003",
                            f"Nested transaction via call graph: '{fn_name}' calls '{callee_name}()' inside an active transaction (opened at line {start_line}), which executes '{chain}'.",
                            raw_l,
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
        "--main-table",
        default=None,
        help="Component main table code (e.g. txsli001) exempted from TBL001 declaration check",
    )
    parser.add_argument(
        "--dd-cache",
        default=None,
        help="Path to .ln_dd_cache.json for TBL002 and DMN001 schema validation",
    )
    parser.add_argument(
        "--auto-fetch-dd",
        action="store_true",
        help="Automatically pull missing .tbl / .dmn definitions read-only from the server and update .ln_dd_cache.json",
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
        main_table=args.main_table,
        dd_cache=Path(args.dd_cache) if args.dd_cache else None,
        auto_fetch_dd=args.auto_fetch_dd,
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
