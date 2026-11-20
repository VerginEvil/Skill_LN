# Plan: Skill Prompt Optimization, Consolidation, Tiered Safety Gate & Lint Hardening

- **Status**: Approved (Grill Rounds 1 & 2 Complete — Ready for Implementation)
- **ADR**: [`docs/adr/0025-skill-prompt-consolidation-safety-tiers-and-lint-hardening.md`](../adr/0025-skill-prompt-consolidation-safety-tiers-and-lint-hardening.md)
- **Spec**: [`.scratch/skill-prompt-optimization/spec.md`](../../.scratch/skill-prompt-optimization/spec.md)
- **Tickets**: [`.scratch/skill-prompt-optimization/issues/`](../../.scratch/skill-prompt-optimization/issues/) (`01`–`06`)
- **Primary Skill Paths**: `Skill_LN/.agents/skills/{erp-ln-progguide, ln_studio_skill}` → synced to `~/.gemini/config/skills/` via `python scripts/run_checks.py --sync-skill`

---

## 1. Expected Impact (Before vs. After)

| Metric | Before | After (Target) | Improvement |
|---|---:|---:|---|
| Always-on `AGENTS.md` + tracked `always_on` rules | 71L (~1,158 tok) | `<= 55L` (~750 tok) | **-35%** & single file |
| Always-on Context Pointers (`description` total) | 186 words (~357 tok) | `<= 78` words (~124 tok) | **-65% every turn** |
| Loaded context on a 4GL coding task (Rule + Skill) | 179L (~3,873 tok) | `<= 75L` (~1,450 tok) | **-62%** (zero double-load) |
| Loaded context on a Studio task (Rule + Skill) | 102L (~2,124 tok) | `<= 75L` (~1,350 tok) | **-36%** (zero double-load) |
| Worst-case Best Practice reference read (`06_4gl_*`) | 1,143L (~14,403 tok) | Hub ~35L + 1 Pillar ~220L (~2.7k tok) | **-81% token spike** |
| Duplicated/drifted reference files in `ln_studio_skill` | 4 files (drifted MD5) | **0 files** | Single Source of Truth |
| High-risk / `PRD` remote ops confirmation gate | Missing | **3-Tier Safety Gate** + Hard-Block | Production-safe |

---

## 2. File-by-File Execution Blueprint

### Phase 1 — Ticket 01: Consolidate `AGENTS.md` & Retire Redundant Rules
- **Delete**:
  - `.agents/rules/infor-ln-coding.md` (130L)
  - `.agents/rules/ln-studio-workflow.md` (63L)
  - `.agents/rules/cross-repo-standards.md` (27L)
- **Keep untouched**:
  - `.agents/rules/repos.local.md` (`trigger: always_on`, gitignored)
  - `.agents/rules/repos.example.md` (tracked template)
  - `CLAUDE.md` (`@AGENTS.md`)
- **Update `AGENTS.md` (`<= 55` lines)**:
  - Keep Home Repo workspace layout (`.agents/skills/` + `.agents/rules/repos.local.md` overlay only), Global Slash-Command Sync Cache (`python scripts/run_checks.py --sync-skill`), Unified Checks Gateway commands, Issue Tracker & Domain Docs pointers.
  - Fold in concise single-line bullets for:
    - Glossary & ADR alignment (`docs/glossary/GLOSSARY.md`, `docs/adr/`).
    - `Audit-Before-Deliver` gate (`skill-ln audit-4gl` before delivering any 4GL/DAL/Extension code).
    - Cross-Runtime Parity & Reuse Reviewer Standard (when modifying `ln_studio_skill/tools/*.py` or `rust/crates/*`, keep Python/Rust CLI & MCP schemas in parity and reuse shared helpers).
    - Public/Private & Secret Hygiene (no `.ionapi`, OAuth tokens, customer names, workstation paths, or internal URLs in tracked files or `~/.gemini/config/skills/`).

### Phase 2 — Ticket 02: Upgrade `.agents/skills/erp-ln-progguide/SKILL.md`
- **Target**: `<= 75` lines (hard cap `<= 80` lines), YAML `description <= 45` words.
- **Proposed Frontmatter**:
  ```yaml
  ---
  name: erp-ln-progguide
  description: Infor ERP LN / Baan 4GL coding guide, bshell API search, and static auditor (`skill-ln audit-4gl`). Use when writing, debugging, or auditing 4GL, DAL 1/2, Baan SQL, or Extension Modeler code. Route Studio workspaces, SCM, XML generation, and deploy-test to `ln_studio_skill`.
  ---
  ```
- **Body Structure (Positive-first)**:
  1. **Compact Decision Tree** (4 lines): API/function lookup → `Search-Before-Read` | Code authoring/review → open matching Cookbook branch | Modification in an activity → wrap edits with SPS comments | Before delivery → `Audit-Before-Deliver`.
  2. **Step 1: `Search-Before-Read`** — Run `skill-ln fn-search "<term>"` or `skill-ln doc-search "<terms>"`; consult `references/STUDIO_SYNTAX_COMPLETION.md` for syntax/hooks; avoid reading huge multi-thousand-line index files whole (`FUNCTION_INDEX.md`, `PUBLIC_INTERFACES_INDEX.md` — grep or CLI search only).
  3. **Step 2: Branching Reference Pointers** — Table pointing to cookbooks (`01`..`05`), the new `06_4gl_coding_standards_and_caveats.md` Hub (noting its 4 pillars `06a`–`06d`), domain indices (`EXTENSIONS_INDEX.md`, `DEV_TOOLS_INDEX.md`, `PUBLIC_INTERFACES_INDEX.md`, `AFS_INDEX.md`), and `templates/`.
  4. **Step 3: Core 4GL, SPS & Cloud Guardrails** — Concise positive-first checklist preserving all 7 existing guardrails + migrated **SPS Maintenance Comments** (`|#<activity_name>.sn` / `.en`, `.so` / `.eo`).
  5. **Step 4: `Audit-Before-Deliver` Completion Gate** — Run `skill-ln audit-4gl <target_script> [--mode auto|general|dal2|uedll] [--cloud] [--dd-dir <dir>]`; done when exit code is `0` with **0 errors**.

### Phase 3 — Ticket 03: Upgrade `.agents/skills/ln_studio_skill/SKILL.md` & 3-Tier Safety Gate
- **Target**: `<= 75` lines (hard cap `<= 80` lines), YAML `description <= 45` words.
- **Proposed Frontmatter**:
  ```yaml
  ---
  name: ln_studio_skill
  description: Infor LN Studio automation (`skill-ln` CLI/MCP). Use for Eclipse workspaces/activities, JCA SCM checkout/checkin, Single-Line TDE XML generation, validation, deploy-test, VRC sync, revision diff, or `tx*` Extension CLI packaging. Route 4GL/DAL coding rules and bshell APIs to `erp-ln-progguide`.
  ---
  ```
- **Body Structure (Positive-first, zero stale counts)**:
  1. **Compact Decision Tree** (4 lines): Standard component edit → `checkout-component` → `extract`/edit/`audit-4gl`/`inject` → `validate` → `deploy-test` | New component(s) → `schema.yaml` → `component` → `sync-admin` | Extension `tx*` (`ess`/`est`/`esb`/`esm`/`esr`) → `Guide-and-Paste` (local `.4gl` + `audit-4gl` + `extension-hooks`, Read-Only in Studio SCM) | Post-`End Activity` → `sync-activity`.
  2. **Tiered Safety Gate** (compact table/list):
     - **Tier 1 (Read-Only / Local)**: `login --status`, `explorer`, `get-component`, `validate`, `diagnose`, `audit-4gl`, `revisions`, `diff-component` → run directly; emit `Pre-Fetch-Auth-Gate` target banner (Object, Workspace/Env, Project/Activity, Mode) before remote calls and surface OAuth2 URL if silent refresh fails.
     - **Tier 2 (Dev/Test Mutating)**: `checkout-component`, `checkin-component`, `deploy-test --mode compile-only`, `new-activity`, `component`, `inject`, `sync-admin`, `sync-activity` → announce target workspace/activity/component before running; preserve Read-Only flags on untouched/`.reference/`/`tx*` files (`Read-Only-SCM-Guardrail`).
     - **Tier 3 (High-Risk / Destructive / `PRD` — Stop & Confirm)**: `deploy-test --mode schema-crdd`, `uncheckout-component`, `clean-activity`, `clean-components`, `move-components`, `sync-admin --prune`, or **any write operation on a `PRD` environment** → **halt and require explicit user confirmation before executing**.
     - **Hard-Blocked (`Pre-Commit-Boundary`)**: `end-activity` is unconditionally blocked so a human engineer completes final delivery in LN Studio UI.
  3. **Core XML & Workflow Completion Gates** — Preserve `Single-Line TDE XML` invariant, `Label Context & FieldLabel Parity` (`1`/`2`/`10` + package-prefix rule), and 4-stage workflow (`Auth` → `Edit/Sync` → `Validate & Deploy-Test` → `Prepare-End-Activity & Sync-Activity`). Direct agents to `skill-ln --help` / `skill-ln <subcmd> --help` instead of hardcoding subcommand/tool counts or nudging `tools/` source reads.
  4. **Branching Reference Pointers** — Link `CLI_REFERENCE.md`, `MCP_TOOLS_REFERENCE.md`, `AUTHORING_SCHEMA_GUIDE.md`, `COMPONENT_XML_SCHEMA.md`, `STUDIO_INDEX.md` (newly linked!), and `../erp-ln-progguide/SKILL.md` (removing deleted `DAL2_HOOKS_GUIDE.md` & `UI_SCRIPT_GUIDE.md`).

### Phase 4 — Ticket 04: Reference Consolidation, Orphan Resolution & Doc Hygiene
- **Delete duplicated/drifted files in `.agents/skills/ln_studio_skill/references/`**:
  - `STUDIO_SYNTAX_COMPLETION.md`
  - `studio_syntax_completion.json`
  - `DAL2_HOOKS_GUIDE.md`
  - `UI_SCRIPT_GUIDE.md`
- **Verify code & indices**:
  - Confirm `check_4gl_script.py`, `audit_4gl.py`, `extract_studio_dictionaries.py`, `rust/crates/ln-kb/build.rs`, and `validate_skill.py` resolve cleanly against `erp-ln-progguide/references/studio_syntax_completion.json`.
  - Regenerate `.agents/skills/ln_studio_skill/index/INDEX.tsv` via `generate_indices.py` so `validate_skill.py` and `test_validate_skill.py` pass cleanly.
- **Sanitize tracked docs**:
  - Replace `dev_natt_1107-1` in `.agents/skills/ln_studio_skill/references/MCP_TOOLS_REFERENCE.md` (and verify no other tracked skill/doc files expose developer-specific activity IDs) with `dev_user_001 [EXT01]`.
  - Remove stale hardcoded count text if drifted in `CLI_REFERENCE.md` / `MCP_TOOLS_REFERENCE.md` headers or sync accurately.

### Phase 5 — Ticket 05: Split `06_4gl_coding_standards_and_caveats.md` into Hub + 4 Pillars
- **Keep `.agents/skills/erp-ln-progguide/references/best_practices/06_4gl_coding_standards_and_caveats.md` as a ~35-line Router Hub** (preserving incoming links from `03_sql_*`, `04_data_model_*`, `README.md`, `ADR 0004`, `ADR 0019`) with a clean table routing to:
  1. `06a_declarations_and_functions.md` (Pillars 1–3: Domains/Variables/Scopes, DLL Linkage & Preprocessor, Function Architecture & Parameters)
  2. `06b_sql_buffer_protection.md` (Pillar 4: Embedded SQL & Table Record Buffer Protection)
  3. `06c_arrays_and_dimensions.md` (Pillar 5: Domain Arrays & Dimension Mechanics)
  4. `06d_syntax_caveats_and_runtime_guards.md` (Pillars 6–7: Critical Syntax Caveats & Anti-Patterns + ADR 0017 Runtime Error Prevention & Quick Reference Checklist)
- Regenerate `.agents/skills/erp-ln-progguide/index/INDEX.tsv` so `validate_skill.py` passes with 0 missing/unindexed files.
- Ensure zero content loss during the split (every rule, code example, and ADR 0017 guard preserved verbatim in its target pillar).

### Phase 6 — Ticket 06: Harden `scripts/run_checks.py` Lint Gate, Add Tests & Sync Global Cache
- **Expand `check_skill_markdown()` in `scripts/run_checks.py`**:
  1. `SKILL.md <= 80` lines AND frontmatter `description <= 45` words.
  2. `AGENTS.md <= 60` lines and every tracked `.agents/rules/*.md <= 60` lines (excluding gitignored `repos.local.md`).
  3. Validate relative markdown links in `AGENTS.md`, `.agents/rules/*.md`, both `SKILL.md` files, and `references/*.md` (including `erp-ln-progguide/references/best_practices/*.md`).
  4. Detect orphaned top-level `.md` files in `ln_studio_skill/references/` (every `references/*.md` must be linked from `SKILL.md` or another linked reference).
  5. Update `check_hygiene()` if helpful to guard `AGENTS.md` as well (already skips `repos.example.md`).
- **Update/Add Unit Tests**:
  - Extend existing `test_run_checks.py` (or `test_skill_lint_gate.py`) to test: `description > 45 words` failure, `AGENTS.md > 60L` failure, rule `> 60L` failure, orphaned `references/*.md` detection, and passing clean fixture.
- **Final Verification & Global Sync**:
  ```powershell
  python scripts/run_checks.py --sync-skill
  python .agents/skills/ln_studio_skill/tools/validate_skill.py --skill-dir .agents/skills/erp-ln-progguide
  python .agents/skills/ln_studio_skill/tools/validate_skill.py --skill-dir .agents/skills/ln_studio_skill
  python scripts/package_release.py --version v-smoke --output-dir .scratch/release-smoke
  ```
  (Clean up `.scratch/release-smoke` after verifying ZIP contents.)

---

## 3. Handoff Prompt for Fresh Session (Gemini 4 Hydrogen)

Copy-paste into a new session inside `Skill_LN`:

> Execute the approved specification in `.scratch/skill-prompt-optimization/spec.md` and plan `docs/plans/PLAN_SKILL_PROMPT_OPTIMIZATION.md` (governed by `docs/adr/0025-skill-prompt-consolidation-safety-tiers-and-lint-hardening.md`). Work through tickets `01` through `06` in `.scratch/skill-prompt-optimization/issues/` in dependency order, updating each ticket's `Status:` and checkboxes as you complete it. Finish by running `python scripts/run_checks.py --sync-skill` and verifying `validate_skill.py` on both `.agents/skills/erp-ln-progguide` and `.agents/skills/ln_studio_skill` pass with zero errors.
