# ADR 0022: The Home Repo Pattern & Antigravity-First `.agents/` Workspace Layout

- **Status**: Accepted
- **Date**: 2026-11-16
- **Context**: `/grill-with-docs` Architecture Review (`https://www.aihero.dev/the-home-repo-pattern`)
- **Specification & Plan**: [`.scratch/home-repo-restructure/spec.md`](../../.scratch/home-repo-restructure/spec.md) & [`docs/plans/PLAN_HOME_REPO_RESTRUCTURE.md`](../plans/PLAN_HOME_REPO_RESTRUCTURE.md)
- **Prior ADRs**:
  - [`docs/adr/0015-repository-reorganization-and-github-release-automation.md`](0015-repository-reorganization-and-github-release-automation.md) *(Superseded on Decision 1: Monorepo Dual-Skill Root Placement; Preserved on `.gitignore` hardening and GitHub Release ZIP artifact structure)*
  - [`docs/adr/0018-lean-skill-architecture-and-progressive-disclosure.md`](0018-lean-skill-architecture-and-progressive-disclosure.md) *(Preserved: `<= 80`-line `SKILL.md` budget and `check_skill_markdown` gate)*
  - [`docs/adr/0021-native-rust-skill-ln-single-binary-architecture.md`](0021-native-rust-skill-ln-single-binary-architecture.md) *(Preserved: `skill-ln` single-binary architecture; path resolution updated for `.agents/skills/` with root fallback)*

---

## 1. Context & Problem Statement

While `Skill_LN` established a strong dual-skill toolchain (`erp-ln-progguide` and `ln_studio_skill`) under ADR 0015 and ADR 0018, operating across 8 active 2026 customization/supporting repositories and two Eclipse LN Studio paths exposed four structural gaps:

1. **Fragmented Multi-Repo Context**: Starting an AI agent inside a single customer repository blinds the agent to shared standards, tools, and related repositories.
2. **Non-Standard Antigravity Workspace Layout**: Antigravity discovers workspace skills under `.agents/skills/<name>/SKILL.md` and rules under `.agents/rules/*.md`. Placing skills at the repository root and rules under `.antigravity/rules/` prevented native workspace discovery and forced manual copy-syncing.
3. **Global Skill Drift & Secret Exposure Risk**: Multiple unsynchronized copies of `erp-ln-progguide`, `ln_studio_skill`, and `knowledge_docs` existed across `~/.gemini/config/skills/`, `~/.agents/skills/`, and `~/.gemini/skills/` (which had drifted to legacy commands), and `~/.gemini/config/skills/knowledge_docs/` lacked a `SKILL.md` while duplicating a tenant `.ionapi` credential.
4. **Public Repo vs. Private Customer Pointers**: `Skill_LN` is a public GitHub repository (`VerginEvil/Skill_LN`), so embedding private customer repository names, local Windows paths, and internal GitLab URLs directly in tracked `AGENTS.md` would expose internal metadata.

---

## 2. Decision Drivers

1. **The Home Repo Pattern**: Make `Skill_LN` the single personal command center where Antigravity sessions start, holding canonical skills, shared coding standards, and navigation pointers to active repositories.
2. **Antigravity-First Discovery (With `/` Compatibility)**: Use `.agents/skills/` and `.agents/rules/` as the canonical workspace layout while keeping `~/.gemini/config/skills/` synchronized as real directory copies via `--sync-skill` (Antigravity `/` slash-command discovery does not recognize Windows directory junctions).
3. **Public/Private Separation**: Keep `Skill_LN` public and open-source while isolating private customer repo pointers in a gitignored local overlay loaded automatically by Antigravity.
4. **Progressive Disclosure for Rules**: Split monolithic rules by responsibility with `always_on` vs `model_decision` triggers so non-4GL tasks do not pay unnecessary context overhead.
5. **Zero-Breakage Expand–Contract Migration**: Preserve CI checks, release ZIP archive layouts, and standalone Rust binary (`skill-ln`) compatibility across the directory move.

---

## 3. Considered Options

- **Option A: Create a separate private Home Repo pointing to `Skill_LN`**
  - *Rejected*: User prefers consolidating directly under `Gitlab\Skill_LN\` as the single Home Repo and reorganizing its internal structure.
- **Option B: Keep skills at root and use Windows directory junctions inside `.agents/skills/`**
  - *Rejected*: Leaves root cluttered, splits canonical location from `.agents/`, and junctions have known Antigravity discovery caveats (`/` command incompatibility).
- **Option C: Adopt `.agents/` as canonical Home Repo layout inside `Skill_LN`, isolate private pointers in a gitignored `.agents/rules/repos.local.md` overlay, and maintain real-copy `--sync-skill` for `~/.gemini/config/skills/` (Chosen)**
  - *Supersedes ADR 0015 Decision 1*: Moves `erp-ln-progguide` and `ln_studio_skill` into `.agents/skills/`, while keeping release ZIP archive roots unchanged (`erp-ln-progguide-v<ver>.zip`, `ln_studio_skill-v<ver>.zip`).

---

## 4. Decision Outcome

1. **Home Repo Entry Points**:
   - `AGENTS.md` serves as the public Home Repo steering file; `CLAUDE.md` provides a 1-line `@AGENTS.md` pointer.
   - `.agents/rules/repos.local.md` (`trigger: always_on`, gitignored) stores local navigation pointers for the 8 active 2026 repos and 2 LN Studio workspace/install paths; `.agents/rules/repos.example.md` is tracked in git as a template.
2. **Canonical `.agents/` Layout (Supersedes ADR 0015 Decision 1)**:
   - Skills move to `.agents/skills/erp-ln-progguide/` and `.agents/skills/ln_studio_skill/`.
   - `.antigravity/rules/infor_ln.md` is replaced by modular rules in `.agents/rules/`:
     - `cross-repo-standards.md` (`trigger: always_on`)
     - `infor-ln-coding.md` (`trigger: model_decision`)
     - `ln-studio-workflow.md` (`trigger: model_decision`)
3. **Tooling & Binary Compatibility (Expand–Contract)**:
   - Python checks (`scripts/run_checks.py`), release packaging (`scripts/package_release.py`), developer scripts, and Rust crates (`ln-kb`, `ln-verify`) resolve `.agents/skills/` as primary path, retaining root fallback in Rust for standalone release execution.
4. **Global Hygiene & Child Repo Deduplication**:
   - `~/.gemini/config/skills/` remains the single global sync destination for `erp-ln-progguide` and `ln_studio_skill` (real copies via `run_checks.py --sync-skill`).
   - Stale `~/.gemini/skills/{erp-ln-progguide, ln_studio_skill}`, duplicate `~/.agents/skills/{erp-ln-progguide, ln_studio_skill, knowledge_docs}`, and `~/.gemini/config/skills/knowledge_docs/` (including duplicated tenant `.ionapi` credentials) are removed.
   - `thai-natural-writing` remains in global user skills; installed marketplace/plugin skills remain managed by their installers.
   - Duplicate/empty generic rules (`agents.md`, `afs.md`, `skill.md`) in the child customization repository's `.agent/rules/` are removed on a dedicated local branch while keeping its repo-specific table schema rules (`tables.md`).
