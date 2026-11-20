# ADR 0025: Skill Prompt Consolidation, Tiered Safety Gate & Expanded Lint Hardening

- **Status**: Accepted
- **Date**: 2026-11-20
- **Context**: `/grill-with-docs` & `/writing-for-agents` Prompt Audit (`erp-ln-progguide`, `ln_studio_skill`, `AGENTS.md`, `.agents/rules/`)
- **Specification & Plan**: [`.scratch/skill-prompt-optimization/spec.md`](../../.scratch/skill-prompt-optimization/spec.md) & [`docs/plans/PLAN_SKILL_PROMPT_OPTIMIZATION.md`](../plans/PLAN_SKILL_PROMPT_OPTIMIZATION.md)
- **Prior ADRs**:
  - [`docs/adr/0015-repository-reorganization-and-github-release-automation.md`](0015-repository-reorganization-and-github-release-automation.md) *(Preserved: Dual-skill release ZIP archive names including `ln_studio_skill`)*
  - [`docs/adr/0018-lean-skill-architecture-and-progressive-disclosure.md`](0018-lean-skill-architecture-and-progressive-disclosure.md) *(Extended: adds Context Pointer Budget `<= 45` words, Decision Trees, Positive-first framing, Tiered Safety Gate, and expanded Lint Gate checks)*
  - [`docs/adr/0022-home-repo-pattern-and-antigravity-layout.md`](0022-home-repo-pattern-and-antigravity-layout.md) *(Superseded on Decision 2: Modular Rules — retires `infor-ln-coding.md`, `ln-studio-workflow.md`, and `cross-repo-standards.md` in favor of Single-Source Skill Authority and a unified `AGENTS.md`; Preserved on Decision 1, 3, and 4)*

---

## 1. Context & Problem Statement

Following the Home Repo restructuring (ADR 0022), a full prompt and token-budget audit of `Skill_LN` uncovered five structural inefficiencies that inflate context load, degrade attention, and create safety/maintenance drift:

1. **Rule–Skill Double-Loading & Drift (~3,400 wasted tokens/session)**:
   - `.agents/rules/infor-ln-coding.md` (130L, ~2,499 tokens) and `.agents/rules/ln-studio-workflow.md` (63L, ~964 tokens) use `model_decision` triggers that overlap almost 1-to-1 with `erp-ln-progguide/SKILL.md` (49L, ~1,374 tokens) and `ln_studio_skill/SKILL.md` (39L, ~1,160 tokens). On any 4GL or Studio task, agents load both the rule and the skill simultaneously, paying double tokens while rules drift out of sync (e.g., `infor-ln-coding.md` frontmatter still lists `EXT001-EXT003` despite documenting `EXT004`, while SPS maintenance comments `.sn/.en` appear only in the rule and not in the skill).
   - `.agents/rules/cross-repo-standards.md` (`always_on`, 27L, ~444 tokens) loads alongside `AGENTS.md` (44L, ~714 tokens) on every turn in the Home Repo, duplicating `Audit-Before-Deliver` and credential hygiene rules.
2. **Bloated & Overlapping Always-On Context Pointers (~357 tokens/turn)**:
   - Four always-loaded trigger descriptions (`erp-ln-progguide` 52w, `ln_studio_skill` 63w, plus two `model_decision` rules 71w) overlap on Extension Modeler (`tx*`) tasks and list redundant synonyms instead of concise branch triggers.
3. **Reference Duplication, Drift, Orphans & Sprawl**:
   - `STUDIO_SYNTAX_COMPLETION.md` and `studio_syntax_completion.json` are duplicated across both skills and have drifted (mismatched hashes/sizes), even though both Rust (`ln-kb/build.rs`) and Python (`check_4gl_script.py`) already support loading from `erp-ln-progguide/references/`.
   - `DAL2_HOOKS_GUIDE.md` (110L) and `UI_SCRIPT_GUIDE.md` (91L) live inside `ln_studio_skill/references/` despite `ln_studio_skill` explicitly routing 4GL/DAL rules to `erp-ln-progguide`, duplicating `best_practices/02_*` and `05_*`.
   - `ln_studio_skill/references/STUDIO_INDEX.md` (396L, indexing official `studio_guide/` docs) is orphaned with no pointer from `SKILL.md`.
   - `erp-ln-progguide/references/best_practices/06_4gl_coding_standards_and_caveats.md` has grown to **1,143 lines (~14,403 tokens)**, causing a severe mid-session token spike whenever opened.
4. **Stale Environment Caches & Missing Safety Confirmation Tiers**:
   - `ln_studio_skill/SKILL.md` hardcodes volatile counts (`62 subcommands` when `CLI_REFERENCE.md` documents 60 and `skill-ln --help` exposes 64) instead of deferring to `skill-ln --help`.
   - While `end-activity` is hard-blocked (`Pre-Commit-Boundary`), high-risk remote operations (`deploy-test --mode schema-crdd`, `uncheckout-component`, `clean-activity`, `clean-components`, `move-components`, `sync-admin --prune`, and any write operation targeting a Production `PRD` tenant) lack an explicit stop-and-confirm guardrail in `SKILL.md`.
5. **Narrow Lint Coverage & Doc Hygiene Leaks**:
   - `check_skill_markdown()` in `scripts/run_checks.py` enforces `<= 80` lines only on `SKILL.md`, leaving `AGENTS.md`, `.agents/rules/*.md`, frontmatter `description` lengths, and orphaned top-level `references/*.md` unguarded. Tracked documentation examples also still contain developer-specific activity identifiers.

---

## 2. Decision Drivers

1. **Single-Source Skill Authority**: Each domain concern has exactly one authoritative instruction file—eliminating double-loading between `.agents/rules/` and `.agents/skills/`.
2. **Prompt / Context Caching Stability**: Keep the always-on system prefix (`AGENTS.md` + `repos.local.md` + 2 concise skill `description` pointers) small, deterministic, and low-churn so prefix caching maximizes cache hits.
3. **Writing-for-Agents Discipline**: Front-load leading words, one trigger per distinct branch, positive-first framing paired with hard guardrails, compact decision trees, and zero stale environment caches (`--help` is the source of truth).
4. **Defense-in-Depth Safety**: Clearly separate Read-Only, Dev/Test Mutating, High-Risk/Destructive/PRD Confirmation, and Hard-Blocked operations.
5. **Zero-Regression Stability**: Preserve Dual-Skill Topology and `ln_studio_skill` folder/package naming (avoiding unnecessary 116-file blast radius) and preserve backward-compatible links when splitting sprawling references.

---

## 3. Considered Options

- **Option A: Keep `model_decision` rules as thin `<= 25L` wrappers pointing to skills, and rename `ln_studio_skill` to `ln-studio`**
  - *Rejected*: Still pays always-on pointer tokens for two redundant rule descriptions, risks renewed rule–skill drift, and renaming `ln_studio_skill` triggers a 116-file refactor across Rust, Python, tests, release ZIPs, and global slash-command paths for minimal functional gain.
- **Option B: Split into 3+ skills (extracting `ln-extension-modeler`)**
  - *Rejected*: Breaks ADR 0015/0018 dual-skill packaging and adds another always-on skill pointer when clear branch wording already resolves the `tx*` seam cleanly.
- **Option C: Establish Single-Source Skill Authority, consolidate always-on steering into `AGENTS.md`, keep Dual-Skill Topology & `ln_studio_skill` naming, apply Reference Hub-and-Pillar Split, enforce a 3-Tier Safety Gate, and harden the Unified Checks Gateway lint gate (Chosen)**
  - *Pros*: Cuts always-on pointer overhead by ~65%, eliminates ~3,400 tokens/session of rule–skill double-loading, drops worst-case reference token spikes from ~14.4k to ~2–3k, closes remote destructive/PRD safety gaps, and mechanically prevents regression.

---

## 4. Decision Outcome

### 4.1 Single-Source Skill Authority & Rule Retirement (Supersedes ADR 0022 Decision 2)
- Retire `.agents/rules/infor-ln-coding.md`, `.agents/rules/ln-studio-workflow.md`, and `.agents/rules/cross-repo-standards.md`.
- Consolidate essential cross-repository discipline (Glossary/ADR alignment, `Audit-Before-Deliver` summary, Public/Private credential hygiene) and `Skill_LN` tool-development rules (Cross-Runtime Python ↔ Rust MCP parity and helper reuse) into a single root `AGENTS.md` (`<= 60` lines).
- Retain `.agents/rules/` exclusively for `.agents/rules/repos.local.md` (`trigger: always_on`, gitignored) and `.agents/rules/repos.example.md` (tracked template).
- Migrate unique non-duplicated rules into their authoritative skills: SPS Maintenance Comments (`|#<activity_name>.sn/.en`) move into `erp-ln-progguide/SKILL.md`.

### 4.2 Dual-Skill Topology, Naming Exception & Context Pointer Budget (`<= 45` words)
- Retain the Dual-Skill Topology (`erp-ln-progguide` and `ln_studio_skill`) under `.agents/skills/` and their real-directory sync cache in `~/.gemini/config/skills/` (`--sync-skill`).
- Formally document the `ln_studio_skill` `snake_case` naming exception (grandfathered to preserve 116 tracked references, Rust binary paths, and ADR 0015 release ZIP artifact names); any *future* skills must use `kebab-case`.
- Cap YAML frontmatter `description` at **<= 45 words** per skill, with sharp non-overlapping `tx*` Extension boundaries:
  - `erp-ln-progguide`: 4GL/DAL/SQL/Extension Modeler code authoring, debugging, bshell API search, and offline auditing.
  - `ln_studio_skill`: Eclipse workspaces/activities, JCA SCM, Single-Line TDE XML generation, validation, deploy-test, VRC sync, revision diffs, and `tx*` Extension CLI packaging/extraction.

### 4.3 `SKILL.md` Body Upgrades (`<= 80` lines) & 3-Tier Safety Gate
- Both `SKILL.md` files remain capped at `<= 80` lines and adopt:
  1. A **Compact Decision Tree** (4–5 lines) at the top for immediate branch routing.
  2. **Positive-first phrasing** paired with explicit guardrails.
  3. **Zero stale environment caches** (remove hardcoded subcommand/tool counts and internal `tools/` source nudges; direct agents to `skill-ln --help` / `skill-ln <cmd> --help`).
  4. **Tiered Safety Gate** in `ln_studio_skill/SKILL.md`:
     - **Tier 1 — Read-Only / Local**: `login --status`, `explorer`, `get-component`, `validate`, `audit-4gl`, `fn-search`, `doc-search` → run directly (emit `Pre-Fetch-Auth-Gate` target banner before remote fetches).
     - **Tier 2 — Dev/Test Mutating**: `checkout-component`, `checkin-component`, `deploy-test --mode compile-only`, `new-activity`, `component`, `inject`, `sync-admin`, `sync-activity` → announce target workspace/activity/component before execution.
     - **Tier 3 — High-Risk / Destructive / Production (`PRD`)**: `deploy-test --mode schema-crdd`, `uncheckout-component`, `clean-activity`, `clean-components`, `move-components`, `sync-admin --prune`, or **any write operation targeting a `PRD` environment** → **STOP and obtain explicit user confirmation before executing**.
     - **Hard-Blocked (`Pre-Commit-Boundary`)**: `end-activity` / `CloseTask` / `FinalizeActivity` remains unconditionally blocked for human delivery in LN Studio UI.

### 4.4 Reference Consolidation, Orphan Linking & Hub-and-Pillar Split
- Remove four duplicated/drifted reference files from `ln_studio_skill/references/`: `STUDIO_SYNTAX_COMPLETION.md`, `studio_syntax_completion.json`, `DAL2_HOOKS_GUIDE.md`, and `UI_SCRIPT_GUIDE.md` (regenerating `ln_studio_skill/index/INDEX.tsv`), making `erp-ln-progguide/references/` the single source of truth for syntax completion and 4GL/DAL/UI guides.
- Link `ln_studio_skill/references/STUDIO_INDEX.md` from `ln_studio_skill/SKILL.md`'s branching table so the official LN Studio Workbench guide (`studio_guide/`) is discoverable rather than orphaned.
- Refactor `erp-ln-progguide/references/best_practices/06_4gl_coding_standards_and_caveats.md` (1,143 lines) into a **~35-line Router Hub** preserving all incoming relative links, backed by **4 focused Pillar files** (`~165–260` lines each):
  1. `06a_declarations_and_functions.md` (Pillars 1–3: Domains, Scopes, DLLs, Functions)
  2. `06b_sql_buffer_protection.md` (Pillar 4: Embedded SQL & Record Buffer Protection)
  3. `06c_arrays_and_dimensions.md` (Pillar 5: Domain Arrays & Dimension Mechanics)
  4. `06d_syntax_caveats_and_runtime_guards.md` (Pillars 6–7: Syntax Caveats & ADR 0017 Runtime Guards)

### 4.5 Expanded Skill & Rule Lint Gate & Hygiene (`scripts/run_checks.py`)
- Extend `check_skill_markdown()` in `scripts/run_checks.py` to enforce:
  1. `SKILL.md <= 80` lines and YAML frontmatter `description <= 45` words.
  2. `AGENTS.md <= 60` lines and every tracked `.agents/rules/*.md <= 60` lines.
  3. Relative markdown link resolution across `AGENTS.md`, `.agents/rules/*.md`, both `SKILL.md` files, and `references/*.md`.
  4. Top-level orphan detection for `ln_studio_skill/references/*.md` (every top-level `.md` must be reachable from `SKILL.md` or another linked reference).
- Replace developer-specific activity identifiers in tracked reference docs (`MCP_TOOLS_REFERENCE.md` and retired `ln-studio-workflow.md`) with generic placeholders (`dev_user_001 [EXT01]`).
