# Maintenance Guide: Updating the ERP LN Skill

One-command workflow to refresh this skill when Infor ships new documentation.

## Prerequisites

- Windows with `hh.exe` on `PATH` (ships with Windows; used as
  `hh.exe -decompile <out> <chm>` with synchronous completion monitoring).
- Python 3.10+ (developed on 3.14).
- `pymupdf` for the Public Interfaces PDF step (`pip install pymupdf`).
  The CHM converter, index generator, validator and pipeline itself use
  only the Python standard library.

## Future update in one command

1. Drop the new artifacts into `update/` (this directory is git-ignored):
   - `progguide_<VER>_en.chm` — Programmer's Guide (main volume).
     Filenames containing `sql` (e.g. `progguide_<VER>_en_sql.chm`)
     are routed to the SQL reference tree.
   - `Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud) <DDMMYYYY>.pdf`
     — the 8-digit date in the filename becomes the index edition label.
2. Run the pipeline from the repository root:

   ```bash
   python tools/update_pipeline.py --update-dir update
   ```

   Useful flags: `--dry-run` (detect sources, change nothing),
   `--skip-chm` / `--skip-pdf` / `--skip-indices` / `--skip-validate`,
   `--workdir <dir>` (keep decompiled intermediates for inspection).

3. Verify:

   ```bash
   python tools/validate_skill.py
   python erp-ln-progguide/scripts/search.py "genai.processing.start"
   python erp-ln-progguide/scripts/search.py "subquery" --dir sql
   python erp-ln-progguide/scripts/search.py "Address.Create" --dir public_interfaces
   ```

4. Review `git status` / diff stats printed by the pipeline, then commit.

## What each tool does

| Tool | Input | Output |
|---|---|---|
| `tools/convert_chm.py` | `.chm` (via `hh.exe`) or an already-decompiled tree (`--src-dir`) | Markdown mirroring the `progguide/` tree (`.htm` -> `.md`, links rewritten + normalized) |
| `tools/convert_pdf_interfaces.py` | Public Interfaces `*.pdf` (`--pdf`, glob accepted) | `chNN_<slug>/<Interface>.md`, `ch01_introduction.md`, `zz_release_history.md`; stale files pruned |
| `tools/generate_indices.py` | `erp-ln-progguide/` tree | `index/INDEX.tsv`, `references/FUNCTION_INDEX.md`, `references/PUBLIC_INTERFACES_INDEX.md` (`--edition`/`--pages` label the PI header) |
| `tools/validate_skill.py` | `erp-ln-progguide/` tree | PASS/FAIL: INDEX paths exist, catalog links resolve, all page links resolve |
| `tools/update_pipeline.py` | `update/` artifacts | Runs everything above with before/after counts + git summary |

Unit tests live in `tools/tests/` (stdlib `unittest` only):

```bash
python -m unittest discover -s tools/tests -v
```

## Conventions to preserve

- Markdown layout matches the established skill style (`# <title>()`,
  `## Syntax:`, tables, relative links) so regenerated pages blend in and
  diffs stay content-focused.
- `public_interfaces/chNN_*` directory slugs are canonicalized in
  `tools/convert_pdf_interfaces.py::CHAPTER_SLUGS`; new chapters fall back
  to slugified titles.
- `index/INDEX.tsv` group order is `guide, sql, extensions, public_interfaces, afs`
  (historical conversion sequence; see `tools/generate_indices.py`).
- `references/afs/` and `references/extensions/` are out of scope for CHM/PDF
  updates and are never touched by the pipeline.

## Troubleshooting

- `hh.exe not found` — run on Windows or pass `--src-dir` with a tree
  decompiled elsewhere.
- `pymupdf is required` — `pip install pymupdf`, or `--skip-pdf`.
- Validation failures after a run usually mean a genuinely new link target
  pattern (inspect the reported `page -> target` lines before committing).
