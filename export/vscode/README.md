# VS Code Extension Assets for Baan 4GL & Infor LN Studio

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
