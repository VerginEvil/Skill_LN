# ADR 0002: LN Studio Skill Self-Contained Toolchain & Studio Guide Ingestion

- **Status**: Accepted
- **Date**: 2026-10-15
- **Spec**: `docs/SPEC_LN_STUDIO_SKILL_UPDATE.md`
- **Prior ADR**: `docs/adr/0001-plan-skill-update-and-coding-best-practices.md` (remains canonical for the programmer's-guide track)

## Decisions Recorded

1. **Atomic relocation (clean break, no shim)**: the entire automation toolchain
   (`ln_component_builder`, generators, synchronizers, diagnostics reader, workspace
   resolver, build bridge, schema validator, converters, indexers, validator, Java helper
   plus binary library, unit suite with fixtures) moved from repo-root `tools/` into
   `ln_studio_skill/tools/`, with every live consumer reference (skill definition, readme,
   agent rules, shared pipeline/index tooling, ignore rules) migrated in the same slice.
   Expand-contract (dual-home shim period) was considered and explicitly rejected by the
   user. Historical plan/spec documents (`docs/PLAN_LN_STUDIO_AUTOMATION.md`,
   `docs/SPEC_LN_STUDIO_AUTOMATION.md`, `Tickets.md` prior-track roster) intentionally keep
   their original `tools/` paths as build history. Internal coupling was refactored from
   location-dependent imports (`tools.*` via repo root on `sys.path`) to skill-root
   resolution (`_SKILL_ROOT`/`_TOOLS_DIR` derived from `__file__`), so the skill works
   regardless of repository checkout path. The command surface is frozen: subcommand names
   and semantics (generate, inject, extract, sync, diagnose, build, full pipeline with
   dry-run and skip-build variants) did not change; only their home changed.

2. **Guide depth weighting**: all 12 Application Development Guide chapters
   (September 2025, cloud and on-premises edition) were ingested via the new stdlib-only
   converter `ln_studio_skill/tools/convert_txt_studio_guide.py` (precedent:
   `convert_txt_dev_tools.py`) into `ln_studio_skill/references/studio_guide/` with master
   index `references/STUDIO_INDEX.md`. Full-detail chapters: ch01 overview, ch02
   installation/connectivity, ch03 activity/SCM, ch04 development procedure including
   verification/debugging, ch07 wizards/dialogs, ch08 multipage editors, ch09 script
   editor. Summary chapters: ch05 InContext modeling, ch06 limitations, ch10 perspectives,
   ch11 views, ch12 project server. Summary chapters still carry the full cleaned source
   text (no invented behavior); the weighting is recorded in the index so agents know
   where to read deeply. Discovery follows the programmer's-guide pattern at the skill
   level: `ln_studio_skill/scripts/search.py` (`--dir studio_guide|all`, group filter,
   list-groups, ranked file-plus-snippet, stdlib only) plus the regenerated every-page
   `ln_studio_skill/index/INDEX.tsv`.

3. **Phase 2 boundary**: ingesting the Integration Development Guide (business interface
   implementations, BOD modeling, hook reference, event publishing) is out of scope and
   tracked as Phase 2, with an explicit non-duplication boundary against the existing
   extensibility reference in `erp-ln-progguide` (`references/extensions/`,
   `PUBLIC_INTERFACES_INDEX.md`, best-practices cookbooks). The studio skill links to
   `erp-ln-progguide` guardrails repo-relatively (`../erp-ln-progguide/...`, best-effort
   when both skills are installed side by side); the skill validator covers each skill
   tree independently and does not resolve cross-skill links.

## Validation (2026-10-15)

- Relocated unit suite: 69 tests pass (`python -m unittest discover -s
  ln_studio_skill/tools/tests`, 1 pre-existing PDF-source skip).
- Skill validation: `validate_skill.py --skill-dir ln_studio_skill` PASS (0 missing, 0
  broken, 16 pages) and `--skill-dir erp-ln-progguide` PASS (0 missing, 0 broken, 5008 pages).
- Representative searches (`connectivity`, `clean activity`, `recover activity`, `SCM`,
  `problem`, `breakpoints`, all `--dir studio_guide`) return the expected guide pages
  near the top (ch02 for connectivity, ch03 for activity/SCM, ch04 for problems/breakpoints).
- Live pipeline against real activity `dev_natt_01103` (DNT_TRN workspace): dry-run
  pipeline generates 16 components; `sync-admin` reports in-sync (0 added/0 removed);
  `diagnose` reports 0 errors; `build` runs in offline mode (no Studio window in this
  environment, bridge returns 0 with F5/Ctrl+B instruction). Full write pipeline verified
  against a temp output dir (16 files: 1 tbl, 1 ses, 1 dmn, 13 lbl).

## Consequences

- Positive: one copied folder (`ln_studio_skill/`) is a working skill — text plus tools —
  and agents get task-to-entry-point navigation with closed-loop recipes instead of
  tool-centric guessing.
- Negative: `erp-ln-progguide` maintenance docs now point at `ln_studio_skill/tools/`
  for shared converters/indices/validation (coupling accepted: studio skill owns the
  toolchain); historical plan/spec docs keep stale `tools/` paths by design.
