#!/usr/bin/env python3
"""
VS Code Extension Assets Generator for Baan 4GL

Generates production-grade assets in export/vscode/:
1. syntaxes/baan4gl.tmLanguage.json (TextMate Grammar)
2. snippets/baan4gl.code-snippets (Snippets catalog)
3. language-configuration.json (Brackets, Comments, Folding)
4. completions.json (Language Server / Completion dataset)
5. README.md (Usage & Integration Guide)
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional


def load_extracted_data(skill_dir: Path) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    db_file = skill_dir / "index" / "functions_db.json"
    dict_file = skill_dir / "references" / "studio_syntax_completion.json"

    if not db_file.exists():
        raise FileNotFoundError(f"Missing {db_file}. Run tools/extract_studio_knowledge.py first.")
    if not dict_file.exists():
        raise FileNotFoundError(f"Missing {dict_file}. Run tools/extract_studio_knowledge.py first.")

    functions_db = json.loads(db_file.read_text(encoding="utf-8"))
    syntax_dict = json.loads(dict_file.read_text(encoding="utf-8"))
    return functions_db, syntax_dict


def generate_textmate_grammar(functions_db: Dict[str, Any], syntax_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Generate comprehensive TextMate grammar for Baan 4GL."""
    keywords = sorted(syntax_dict.get("keywords", []))
    sql_keywords = sorted(syntax_dict.get("sql_keywords", []))
    predefined_vars = sorted(syntax_dict.get("predefined_variables", []))
    standard_defines = sorted(syntax_dict.get("standard_defines", []))
    dal_obj_hooks = sorted(syntax_dict.get("dal_object_hooks", []))

    # Types and storage keywords
    types = [
        "boolean", "byte", "double", "long", "string", "domain", "table", "bset", "void", "multibyte"
    ]
    modifiers = [
        "extern", "global", "fixed", "based", "const", "ref", "static"
    ]

    # Preprocessor directives
    preprocessor = [
        "#include", "#define", "#undef", "#ifdef", "#ifndef", "#if", "#elif", "#else", "#endif",
        "#ident", "#pragma", "#context_on", "#context_off"
    ]

    # Sections
    prog_secs = [re.escape(s) for s in syntax_dict.get("program_sections", [])]
    choice_secs = [re.escape(s) for s in syntax_dict.get("choice_sections", [])]
    sub_secs = [re.escape(s) for s in syntax_dict.get("sub_sections", [])]

    # Build regex patterns
    kw_pattern = r"\b(?i:" + "|".join(re.escape(k) for k in keywords) + r")\b"
    sql_pattern = r"\b(?i:" + "|".join(re.escape(k) for k in sql_keywords) + r")\b"
    types_pattern = r"\b(?i:" + "|".join(re.escape(t) for t in types) + r")\b"
    modifiers_pattern = r"\b(?i:" + "|".join(re.escape(m) for m in modifiers) + r")\b"
    vars_pattern = r"\b(?i:" + "|".join(re.escape(v) for v in predefined_vars) + r")\b"
    defines_pattern = r"\b(?:" + "|".join(re.escape(d) for d in standard_defines) + r")\b"
    dal_hooks_pattern = r"\b(?i:" + "|".join(re.escape(h) for h in dal_obj_hooks) + r")\b"

    # Function names (sample top functions or function call pattern)
    # Matching any identifier with a dot: e.g. dal.set.error.message, Json.getString
    func_call_pattern = r"\b([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)+)\b(?=\s*\()"

    grammar = {
        "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
        "name": "Baan 4GL",
        "scopeName": "source.baan4gl",
        "patterns": [
            {"include": "#comments"},
            {"include": "#strings"},
            {"include": "#numbers"},
            {"include": "#preprocessor"},
            {"include": "#sections"},
            {"include": "#sql"},
            {"include": "#keywords"},
            {"include": "#types"},
            {"include": "#modifiers"},
            {"include": "#standard_defines"},
            {"include": "#predefined_variables"},
            {"include": "#dal_hooks"},
            {"include": "#bshell_functions"}
        ],
        "repository": {
            "comments": {
                "patterns": [
                    {
                        "name": "comment.block.documentation.4gl",
                        "begin": r"(?i)^\s*(dllusage|functionusage)\b",
                        "end": r"(?i)^\s*(enddllusage|endfunctionusage)\b"
                    },
                    {
                        "name": "comment.line.pipe.4gl",
                        "match": r"\|.*$"
                    }
                ]
            },
            "strings": {
                "patterns": [
                    {
                        "name": "string.quoted.double.4gl",
                        "begin": r'"',
                        "end": r'"',
                        "patterns": [
                            {"name": "constant.character.escape.4gl", "match": r'\\.'}
                        ]
                    },
                    {
                        "name": "string.quoted.single.4gl",
                        "begin": r"'",
                        "end": r"'",
                        "patterns": [
                            {"name": "constant.character.escape.4gl", "match": r'\\.'}
                        ]
                    }
                ]
            },
            "numbers": {
                "patterns": [
                    {"name": "constant.numeric.hex.4gl", "match": r"\b0[xX][0-9a-fA-F]+\b"},
                    {"name": "constant.numeric.float.4gl", "match": r"\b\d+\.\d+([eE][+-]?\d+)?\b"},
                    {"name": "constant.numeric.integer.4gl", "match": r"\b\d+\b"}
                ]
            },
            "preprocessor": {
                "patterns": [
                    {
                        "name": "meta.preprocessor.4gl",
                        "match": r"^\s*(#include)\s+([<\"].*?[>\"])",
                        "captures": {
                            "1": {"name": "keyword.control.directive.include.4gl"},
                            "2": {"name": "string.quoted.other.header.4gl"}
                        }
                    },
                    {
                        "name": "keyword.control.directive.4gl",
                        "match": r"^\s*(?:" + "|".join(re.escape(p) for p in preprocessor) + r")\b"
                    }
                ]
            },
            "sections": {
                "patterns": [
                    {
                        "name": "entity.name.section.program.4gl",
                        "match": r"^\s*(?i:" + "|".join(prog_secs) + r")"
                    },
                    {
                        "name": "entity.name.section.choice.4gl",
                        "match": r"^\s*(?i:" + "|".join(choice_secs) + r")"
                    },
                    {
                        "name": "entity.name.section.sub.4gl",
                        "match": r"^\s*(?i:" + "|".join(sub_secs) + r")"
                    },
                    {
                        "name": "entity.name.section.dynamic.4gl",
                        "match": r"^\s*(?i:(?:field|choice|group|form)\.[a-zA-Z0-9_.]+):"
                    },
                    {
                        "name": "entity.name.section.report.4gl",
                        "match": r"^\s*(?i:(?:header|detail|before|after)\.[0-9]+):"
                    }
                ]
            },
            "sql": {
                "patterns": [
                    {
                        "name": "keyword.operator.sql.4gl",
                        "match": sql_pattern
                    }
                ]
            },
            "keywords": {
                "patterns": [
                    {
                        "name": "keyword.control.4gl",
                        "match": kw_pattern
                    }
                ]
            },
            "types": {
                "patterns": [
                    {
                        "name": "storage.type.4gl",
                        "match": types_pattern
                    }
                ]
            },
            "modifiers": {
                "patterns": [
                    {
                        "name": "storage.modifier.4gl",
                        "match": modifiers_pattern
                    }
                ]
            },
            "standard_defines": {
                "patterns": [
                    {
                        "name": "constant.language.standard.4gl",
                        "match": defines_pattern
                    }
                ]
            },
            "predefined_variables": {
                "patterns": [
                    {
                        "name": "variable.language.predefined.4gl",
                        "match": vars_pattern
                    }
                ]
            },
            "dal_hooks": {
                "patterns": [
                    {
                        "name": "support.function.dal.object.4gl",
                        "match": dal_hooks_pattern
                    },
                    {
                        "name": "support.function.dal.field.4gl",
                        "match": r"\b[a-zA-Z0-9_]+\.(?:is\.never\.applicable|is\.applicable|is\.readonly|is\.derived|is\.mandatory|is\.valid|update|make\.valid|check|set\.defaults)\b"
                    }
                ]
            },
            "bshell_functions": {
                "patterns": [
                    {
                        "name": "support.function.bshell.4gl",
                        "match": func_call_pattern
                    }
                ]
            }
        }
    }
    return grammar


def generate_snippets_catalog(syntax_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Generate rich VS Code snippets from official templates and DAL2 contracts."""
    snippets: Dict[str, Any] = {}

    # Official templates from DefaultFourglTemplates.xml
    for tpl in syntax_dict.get("templates", []):
        tpl_name = tpl.get("name", "").strip()
        tpl_desc = tpl.get("description", "").strip()
        pattern = tpl.get("pattern", "")

        # Transform pattern placeholders into VS Code snippet format
        # Baan templates use ${name} or ${cursor}
        transformed = pattern.replace("${cursor}", "$0")
        lines = transformed.splitlines()

        slug = re.sub(r"[^a-zA-Z0-9_]+", "_", tpl_name).strip("_").lower()
        snippets[f"Template: {tpl_name}"] = {
            "prefix": [slug, tpl_name.lower()],
            "body": lines,
            "description": tpl_desc,
        }

    # Custom DAL2 hook snippets
    snippets["DAL2: Field Update Hook"] = {
        "prefix": ["dal.update", "hook.update"],
        "body": [
            "function extern void ${1:field}.update(long i.mode)",
            "{",
            "\ton case i.mode",
            "\tcase DAL_NEW:",
            "\t\t$0",
            "\t\tbreak",
            "\tcase DAL_UPDATE:",
            "\t\tbreak",
            "\tendcase",
            "}"
        ],
        "description": "DAL2 property update hook with i.mode handling"
    }

    snippets["DAL2: Field Check Hook"] = {
        "prefix": ["dal.check", "hook.check"],
        "body": [
            "function extern long ${1:field}.check(long has_changed)",
            "{",
            "\tif has_changed then",
            "\t\tif ${2:condition} then",
            "\t\t\tdal.set.error.message(\"${3:message_code}\")",
            "\t\t\treturn(DALHOOKERROR)",
            "\t\tendif",
            "\tendif",
            "\treturn(0)",
            "}"
        ],
        "description": "DAL2 property validation check hook"
    }

    snippets["DAL2: Field Is Applicable Hook"] = {
        "prefix": ["dal.is.applicable", "hook.is.applicable"],
        "body": [
            "function extern boolean ${1:field}.is.applicable()",
            "{",
            "\treturn(${2:true})",
            "}"
        ],
        "description": "DAL2 property applicability condition hook"
    }

    snippets["DAL2: Field Is Readonly Hook"] = {
        "prefix": ["dal.is.readonly", "hook.is.readonly"],
        "body": [
            "function extern boolean ${1:field}.is.readonly()",
            "{",
            "\treturn(${2:false})",
            "}"
        ],
        "description": "DAL2 property read-only condition hook"
    }

    snippets["DAL2: Before Save Object Hook"] = {
        "prefix": ["dal.before.save", "before.save.object"],
        "body": [
            "function extern long before.save.object(long mode)",
            "{",
            "\ton case mode",
            "\tcase DAL_NEW:",
            "\t\t$0",
            "\t\tbreak",
            "\tcase DAL_UPDATE:",
            "\t\tbreak",
            "\tendcase",
            "\treturn(0)",
            "}"
        ],
        "description": "DAL2 object-level before.save.object lifecycle hook"
    }

    snippets["DAL2: After Save Object Hook"] = {
        "prefix": ["dal.after.save", "after.save.object"],
        "body": [
            "function extern long after.save.object(long mode)",
            "{",
            "\t$0",
            "\treturn(0)",
            "}"
        ],
        "description": "DAL2 object-level after.save.object lifecycle hook"
    }

    snippets["4GL: Database Retry Point"] = {
        "prefix": ["retry.point", "db.retry.point"],
        "body": [
            "db.retry.point()",
            "",
            "select ${1:table}.*",
            "from   ${1:table} for update",
            "where  ${2:condition}",
            "selectdo",
            "\t$0",
            "\tdb.update(${1:table}, db.retry)",
            "\tcommit.transaction()",
            "selectempty",
            "\tabort.transaction()",
            "endselect"
        ],
        "description": "Standard 4GL transaction block with retry point"
    }

    return snippets


def generate_language_configuration() -> Dict[str, Any]:
    """Generate VS Code language-configuration.json."""
    return {
        "comments": {
            "lineComment": "|"
        },
        "brackets": [
            ["{", "}"],
            ["(", ")"],
            ["[", "]"]
        ],
        "autoClosingPairs": [
            {"open": "{", "close": "}"},
            {"open": "(", "close": ")"},
            {"open": "[", "close": "]"},
            {"open": "\"", "close": "\"", "notIn": ["string", "comment"]},
            {"open": "'", "close": "'", "notIn": ["string", "comment"]}
        ],
        "surroundingPairs": [
            ["{", "}"],
            ["(", ")"],
            ["[", "]"],
            ["\"", "\""],
            ["'", "'"]
        ],
        "folding": {
            "markers": {
                "start": r"^\s*(?:dllusage|functionusage|select|if|while|for|case)\b",
                "end": r"^\s*(?:enddllusage|endfunctionusage|endselect|endif|endwhile|endfor|endcase)\b"
            }
        },
        "indentationRules": {
            "increaseIndentPattern": r"^\s*(?:function|if|while|for|select|on\s+case|declaration:|before\.program:|functions:|field\.[a-zA-Z0-9_.]+:|choice\.[a-zA-Z0-9_.]+:)\b.*$",
            "decreaseIndentPattern": r"^\s*(?:endif|endwhile|endfor|endselect|endcase|\})\b"
        }
    }


def generate_completions_dataset(functions_db: Dict[str, Any], syntax_dict: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate completions and hover documentation array for 2,274 bshell functions."""
    completions: List[Dict[str, Any]] = []

    # 1. Bshell functions
    for name, f in sorted(functions_db.items(), key=lambda x: x[0].lower()):
        syntax = f.get("syntax", "")
        desc = f.get("description", "")
        trusted = f.get("trusted", False)
        deprecated = f.get("deprecated", False)
        inc = f.get("include", "")
        scope = f.get("script_type", "all")
        doc_path = f.get("doc_path", "")

        # Format Markdown documentation
        md_lines = [f"### `{syntax}`\n", desc, ""]
        md_lines.append(f"- **Cloud**: {'`Trusted`' if trusted else '`Untrusted`'}")
        if deprecated:
            md_lines.append("- **Status**: `Deprecated`")
        if inc:
            md_lines.append(f"- **Required Header**: `#include <{inc}>`")
        if scope != "all":
            md_lines.append(f"- **Script Scope**: `{scope}`")
        if doc_path:
            md_lines.append(f"- **Guide**: [`{Path(doc_path).name}`]({doc_path})")

        completions.append({
            "label": name,
            "kind": "Function",
            "detail": syntax,
            "documentation": {
                "kind": "markdown",
                "value": "\n".join(md_lines)
            },
            "cloudStatus": "Trusted" if trusted else "Untrusted",
            "deprecated": deprecated,
            "include": inc,
            "scope": scope,
        })

    # 2. Predefined variables
    for var in sorted(syntax_dict.get("predefined_variables", [])):
        completions.append({
            "label": var,
            "kind": "Variable",
            "detail": f"Bshell Predefined Variable: {var}",
            "documentation": {
                "kind": "markdown",
                "value": f"**`{var}`** - Infor LN bshell runtime predefined system variable."
            }
        })

    # 3. Standard defines
    for define in sorted(syntax_dict.get("standard_defines", [])):
        completions.append({
            "label": define,
            "kind": "Constant",
            "detail": f"Standard Define: {define}",
            "documentation": {
                "kind": "markdown",
                "value": f"**`{define}`** - Standard preprocessor constant definition."
            }
        })

    return completions


def generate_vscode_readme() -> str:
    """Generate export/vscode/README.md documentation."""
    return """# VS Code Extension Assets for Baan 4GL & Infor LN Studio

This package contains pre-extracted, production-grade assets generated from **Infor LN Studio 10.8 Build 0640** (`April-2026`). These assets are immediately usable for authoring VS Code extensions or integrating with language tooling.

---

## 1. Package Structure

```
export/vscode/
├── syntaxes/
│   └── baan4gl.tmLanguage.json       # Complete TextMate Grammar for syntax highlighting
├── snippets/
│   └── baan4gl.code-snippets         # Rich 4GL & DAL2 snippets collection
├── language-configuration.json       # Comments (|), bracket pairs, auto-closing & folding
├── completions.json                  # 2,274 bshell functions catalog with Cloud badges
└── README.md                         # Integration instructions (this document)
```

---

## 2. Using in a VS Code Extension

To use these assets in a new or existing VS Code extension:

### In `package.json`:
```json
{
  "name": "infor-ln-4gl",
  "displayName": "Baan 4GL for Infor LN",
  "description": "Syntax highlighting, snippets, and completion for Infor LN Baan 4GL & DAL2",
  "version": "1.0.0",
  "engines": {
    "vscode": "^1.80.0"
  },
  "categories": ["Programming Languages", "Snippets"],
  "contributes": {
    "languages": [
      {
        "id": "baan4gl",
        "aliases": ["Baan 4GL", "baan4gl", "4gl"],
        "extensions": [".cln", ".dal", ".dalsrc", ".ue", ".lib", ".4gl", ".3gl", ".spt", ".bic"],
        "configuration": "./language-configuration.json"
      }
    ],
    "grammars": [
      {
        "language": "baan4gl",
        "scopeName": "source.baan4gl",
        "path": "./syntaxes/baan4gl.tmLanguage.json"
      }
    ],
    "snippets": [
      {
        "language": "baan4gl",
        "path": "./snippets/baan4gl.code-snippets"
      }
    ]
  }
}
```

---

## 3. Asset Details

### TextMate Grammar (`syntaxes/baan4gl.tmLanguage.json`)
- **Keywords**: 80 reserved language keywords (`if`, `while`, `select`, `case`, etc.).
- **SQL Keywords**: 92 embedded SQL keywords (`order by`, `as prepared set`, etc.).
- **Sections**: Program, subsection, choice, report, and dynamic sections (`field.*:`, `choice.*:`).
- **Functions**: Bshell function calls and DAL property hooks.
- **Predefined Symbols**: 176 bshell variables and 49 standard defines.
- **Comments & Strings**: Pipe comments (`|`), DllUsage documentation blocks, and escaped strings.

### Snippets (`snippets/baan4gl.code-snippets`)
- Official 12 Studio code templates (case, dllusage, functionusage, select, loops).
- Modern DAL2 hooks (`.update`, `.check`, `.is.applicable`, `.is.readonly`, `before.save.object`).
- Retry-point database transaction templates.

### Completion Dataset (`completions.json`)
- Contains 2,274 functions with:
  - Exact signature and return type.
  - Cloud Multi-Tenant compatibility badge (`Trusted` vs `Untrusted`).
  - Mandatory include header requirement (`#include <bic_... >`).
  - Markdown documentation and guide links.
"""


def main() -> int:
    skill_dir = Path("erp-ln-progguide")
    export_dir = Path("export/vscode")

    print("=== VS Code Extension Assets Export Pipeline ===")
    print(f"Skill Directory : {skill_dir}")
    print(f"Export Directory: {export_dir}")

    functions_db, syntax_dict = load_extracted_data(skill_dir)

    syntaxes_dir = export_dir / "syntaxes"
    snippets_dir = export_dir / "snippets"
    syntaxes_dir.mkdir(parents=True, exist_ok=True)
    snippets_dir.mkdir(parents=True, exist_ok=True)

    # 1. syntaxes/baan4gl.tmLanguage.json
    print("\n[1/5] Generating TextMate grammar (syntaxes/baan4gl.tmLanguage.json)...")
    tm_grammar = generate_textmate_grammar(functions_db, syntax_dict)
    tm_file = syntaxes_dir / "baan4gl.tmLanguage.json"
    tm_file.write_text(json.dumps(tm_grammar, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"-> Generated {tm_file}")

    # 2. snippets/baan4gl.code-snippets
    print("\n[2/5] Generating snippets catalog (snippets/baan4gl.code-snippets)...")
    snippets = generate_snippets_catalog(syntax_dict)
    snip_file = snippets_dir / "baan4gl.code-snippets"
    snip_file.write_text(json.dumps(snippets, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"-> Generated {snip_file} ({len(snippets)} snippets)")

    # 3. language-configuration.json
    print("\n[3/5] Generating language configuration (language-configuration.json)...")
    lang_conf = generate_language_configuration()
    conf_file = export_dir / "language-configuration.json"
    conf_file.write_text(json.dumps(lang_conf, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"-> Generated {conf_file}")

    # 4. completions.json
    print("\n[4/5] Generating completions dataset (completions.json)...")
    completions = generate_completions_dataset(functions_db, syntax_dict)
    comp_file = export_dir / "completions.json"
    comp_file.write_text(json.dumps(completions, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"-> Generated {comp_file} ({len(completions)} completion proposals)")

    # 5. README.md
    print("\n[5/5] Generating integration README (README.md)...")
    readme_content = generate_vscode_readme()
    readme_file = export_dir / "README.md"
    readme_file.write_text(readme_content, encoding="utf-8")
    print(f"-> Generated {readme_file}")

    print("\nVS Code extension assets successfully exported!")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
