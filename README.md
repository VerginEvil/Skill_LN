[![Infor LN](https://img.shields.io/badge/ERP-Infor%20LN-blue.svg)](https://www.infor.com)
[![Agent Skill](https://img.shields.io/badge/AI%20Skill-Claude%20Code%20%7C%20OpenClaw%20%7C%20Cursor-green.svg)](#)

# Skill: Infor ERP LN Programmer's Guide (Baan 4GL)

Agent skill for AI coding assistants working with Infor ERP LN / Baan 4GL.
The official Infor *Programmer's Guide*
(`progguide 2610 en`), its *SQL* volume, the *LN Extensions Development
Guide 10.8*, the *LN Public Interfaces & Process Extensions Reference Guide
(Cloud) 25082026* and the *AFS Developer's Guide (Infor Integration 6.2)*,
converted to plain token-efficient Markdown that agents can grep and read
directly — one file per function, agents read only the pages they need.

- **2,970 + 155 + 162 + 2,361 + 76 pages** | **2,425 function references** |
  **1,833 public interfaces / process extensions** | **AFS `stpapi.*`
  primitives** | search with `scripts/search.py`

## What's new: LN 2610 + Public Interfaces 25082026

- **Native GenAI 4GL APIs** (`guide/progguide/functions_genai/`): embed AI
  assistance in standard UI sessions — `genai.processing.start()` /
  `genai.processing.ready()`, `set.genai.field()`, `session.set.genai()`
  (+ `.icon` variant), `set.genai.command(s)` (TIV 2496+).
- **1,833 public interfaces** (was 1,805): +28 new, including the
  `whext.dll0019.*` warehouse-advice hooks, `Invoice.SplitRevenueByComponent`,
  `Installment.Approve`, `Invoice.ReprintV2`, and the 2026.07/2026.08 release
  matrix in `public_interfaces/zz_release_history.md`.
- **SQL modernization**: `sub_query` renamed to `subquery`
  (`sql/progguide/functions_database_handling/subquery.md`), plus
  `base64.validate()` and `http.service.info()` in the 4GL guide.
- **Reproducible toolchain**: `tools/` converts CHM/PDF sources and rebuilds
  all indices with a single command (see [Updating](#updating)).

## Installation: point your agent at this skill

Copy the `erp-ln-progguide/` folder to your tool's skills directory:

| Tool | Location |
|---|---|
| Claude Code | `~/.claude/skills/erp-ln-progguide/` (global) or `.claude/skills/` in the project |
| OpenClaw | `~/.openclaw/skills/erp-ln-progguide/` (global) or `.openclaw/skills/` in the project |
| Cursor | `.cursor/skills/erp-ln-progguide/` in the project |
| Gemini CLI / Antigravity | `~/.gemini/skills/erp-ln-progguide/` (global) or `.gemini/skills/` in the project |
| opencode | `~/.config/opencode/skill/erp-ln-progguide/` (global) or `.opencode/skill/` in the project |
| Generic agents | `~/.agents/skills/erp-ln-progguide/` or `.agents/skills/` in the project |

The agent picks the skill up automatically for Baan/LN 4GL, DAL, AFS, LN SQL,
SQLSTATE, extension and public-interface work, per the `description` in
`SKILL.md`.

## Usage (what the agent does)

```bash
# 1) Known function name -> grep the index, read one file
grep -i "genai.processing.start" erp-ln-progguide/references/FUNCTION_INDEX.md
grep -i "Address.Create" erp-ln-progguide/references/PUBLIC_INTERFACES_INDEX.md

# 2) Free-text search (stdlib Python only)
python erp-ln-progguide/scripts/search.py genai.processing.start
python erp-ln-progguide/scripts/search.py subquery --dir sql
python erp-ln-progguide/scripts/search.py "Address.Create" --dir public_interfaces
python erp-ln-progguide/scripts/search.py utc.add --dir guide
python erp-ln-progguide/scripts/search.py --list-groups
python erp-ln-progguide/scripts/search.py --regex "SQLSTATE" --dir sql

# 3) Every page -> index/INDEX.tsv maps path to title
```

## Repository layout

```
erp-ln-progguide/
├── SKILL.md                     # entry point: Baan 4GL crash course + task routing
├── scripts/search.py            # full-text search (Python stdlib only)
├── index/INDEX.tsv              # title -> path for all ~5,000 pages
└── references/
    ├── FUNCTION_INDEX.md        # all 4GL functions by topic (grep first)
    ├── PUBLIC_INTERFACES_INDEX.md # all public interfaces by chapter
    ├── EXTENSIONS_INDEX.md / AFS_INDEX.md
    ├── guide/progguide/...      # main guide: 2,970 topics (incl. functions_genai/)
    ├── sql/progguide/...        # LN SQL + SQLSTATE messages (155 topics)
    ├── extensions/...           # LN Extensions Development Guide (17 chapters)
    ├── public_interfaces/...    # Public Interfaces, 55 chapters + release history
    └── afs/...                  # AFS Developer's Guide (stpapi.*)
tools/
├── update_pipeline.py           # one-command update: decompile -> convert -> index -> validate
├── convert_chm.py               # CHM (hh.exe) -> Markdown, stdlib only
├── convert_pdf_interfaces.py    # Public Interfaces PDF -> Markdown (pymupdf)
├── generate_indices.py          # rebuild INDEX.tsv + both catalog indices
├── validate_skill.py            # index/link integrity checker
└── tests/                       # unittest suite (stdlib only)
docs/MAINTENANCE_GUIDE.md        # step-by-step future-update guide
update/                          # source artifacts, git-ignored (CHMs + reference PDF)
```

## Updating

When Infor ships new docs, drop the files into `update/` and run:

```bash
python tools/update_pipeline.py --update-dir update
python tools/validate_skill.py
```

Details in [`docs/MAINTENANCE_GUIDE.md`](docs/MAINTENANCE_GUIDE.md).

## Sources & counts

| Source | Edition | Pages |
|---|---|---|
| Infor Programmer's Guide (Baan 4GL) | 2610 en | 2,970 topics |
| Programmer's Guide, SQL volume | 2610 en | 155 topics |
| LN Extensions Development Guide | 10.8 (01062026) | 162 |
| Public Interfaces & Process Extensions (Cloud) | 25082026 | 2,361 |
| AFS Developer's Guide (Infor Integration 6.2) | U8627B US | 76 |

All files are UTF-8 Markdown; code examples are fenced; tables preserved;
links are relative and machine-validated (`validate_skill.py`: 0 broken).
