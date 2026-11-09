# Functional & Technical Specification: Lean Skill Architecture, Progressive Disclosure & Automated Skill Lint Gate

- **Document ID**: `SPEC-2026-0017`
- **Triage Label**: `ready-for-agent`
- **Related Plan**: [`docs/plans/PLAN_LEAN_SKILL_ARCHITECTURE.md`](PLAN_LEAN_SKILL_ARCHITECTURE.md)
- **Related ADR**: [`docs/adr/0017-lean-skill-architecture-and-progressive-disclosure.md`](../adr/0017-lean-skill-architecture-and-progressive-disclosure.md)
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`

---

## Problem Statement

When an AI coding assistant loads `erp-ln-progguide` or `ln_studio_skill`, the entire `SKILL.md` body enters the active context window before the agent begins reasoning about the user's task. Over 16 prior iterations, both `SKILL.md` files accumulated exhaustive reference tables, YAML templates, duplicate guidelines, and low-level implementation history ("Sediment"):
- `ln_studio_skill` grew to 430 lines because it embedded a 56-row CLI command table, a 21-row MCP tool catalog, a 50-line multi-component YAML example, a 45-line internal Python directory tree, and deep transport/binary implementation details that the underlying Python/Java scripts already handle automatically.
- `erp-ln-progguide` grew to 170 lines with a 120+ word jargon-heavy frontmatter description, duplicate `Layout` and `Common tasks` tables, and 55 lines of coding standards that repeated the authoritative cookbooks.

This bloat consumes the AI's context attention budget upfront, increasing the likelihood that the agent skips critical procedural steps (such as grepping the Single-Line Grep Index first or running the Standalone 4GL Auditor before delivery), misroutes tasks between the two skills due to missing negative boundaries in the frontmatter headers, or re-introduces documentation sediment during future updates because no automated check enforces skill leanness.

---

## Solution

Refactor both skills in the **Monorepo Dual-Skill Layout** into a **Lean Procedural Skill Architecture (`<= 80` lines per `SKILL.md`)** governed by **Progressive Disclosure** and verified by an automated **Skill Markdown Lint Gate**:
1. **Crisp Context Pointers (`SKILL.md` Header)**: Keep both skills **Model-Invoked**, rewriting their frontmatter `description` fields using natural user task phrasing paired with an explicit negative boundary (`Do NOT use for...`) to cleanly separate 4GL knowledge/auditing from LN Studio workspace/SCM/generation workflows.
2. **Lean Procedural `SKILL.md` Bodies (`<= 80` Lines)**: Strip all implementation sediment and duplicate tables from both `SKILL.md` files, retaining only step-by-step procedural workflows, non-negotiable guardrails, and branching pointers.
3. **Branching Reference Files**: Extract `ln_studio_skill`'s exhaustive CLI command matrix, MCP tool catalog, and multi-component YAML authoring schema into three dedicated reference documents (`CLI_REFERENCE.md`, `MCP_TOOLS_REFERENCE.md`, `AUTHORING_SCHEMA_GUIDE.md`) opened on demand only when an agent reaches that workflow branch. Route `erp-ln-progguide` directly to its existing index and cookbook files.
4. **Canonical Leading Words**: Anchor every procedural step with standardized domain directives (`Search-Before-Read`, `Audit-Before-Deliver`, `Guide-and-Paste`, `Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, `Pre-Commit-Boundary`) documented in the Domain Glossary.
5. **Automated Skill Markdown Lint Gate & Dual-Skill Sync**: Extend the **Unified Checks Gateway** (`scripts/run_checks.py`) to mechanically enforce frontmatter validity, the `<= 80`-line ceiling, and 100% relative reference link integrity across both skills, while upgrading `--sync-skill` to detect drift and synchronize both `ln_studio_skill` and `erp-ln-progguide` to the global agent skills directory.

---

## User Stories

1. As an Infor LN developer prompting an AI agent in natural language, I want each skill's frontmatter Context Pointer to use everyday task phrasing and state what is out of scope (`Do NOT use for...`), so that the model automatically selects the right skill without cross-skill confusion.
2. As an AI coding assistant loading `erp-ln-progguide` or `ln_studio_skill`, I want the main `SKILL.md` file to be 80 lines or fewer, so that my context window stays focused on procedural steps rather than static lookup tables.
3. As an AI coding assistant answering a 4GL or DAL question, I want `erp-ln-progguide` to enforce the `Search-Before-Read` leading word as Step 1, so that I always grep the Single-Line Grep Index or run the full-text search script instead of guessing bshell function names or reading folders blindly.
4. As an AI coding assistant writing or reviewing 4GL, DAL 2, or Extension code, I want a single concise table of Branching Reference Pointers in `erp-ln-progguide`, so that I know exactly which architectural cookbook or index file to open for my specific task without scanning duplicate layout and task tables.
5. As an Infor LN engineer, I want `erp-ln-progguide` to summarize the 6 Core 4GL & Cloud Guardrails in one line each with pointers to the authoritative cookbooks, so that Separation of Concerns, DAL error handling, leading index alignment, transaction retry points, domain declarations, and Cloud Trust rules are never overlooked.
6. As an Infor LN engineer, I want `erp-ln-progguide` to enforce the `Audit-Before-Deliver` leading word as the final step of every coding workflow, so that the agent always runs the Standalone 4GL Auditor and resolves all errors before presenting code.
7. As an AI coding assistant automating LN Studio tasks via CLI, I want all 50+ subcommands and common usage examples organized by workflow inside a dedicated CLI Branching Reference File, so that I can open the CLI catalog only when constructing CLI commands.
8. As an AI coding assistant operating via Model Context Protocol, I want the 4 Consolidated MCP Tools, 17 Detailed MCP Tools, and client registration instructions placed in a dedicated MCP Branching Reference File, so that MCP tool schemas do not clutter `SKILL.md` during non-MCP tasks.
9. As an AI coding assistant generating tables, domains, sessions, libraries, or menus from declarative specs, I want the multi-component YAML specification and example placed in a dedicated Authoring Schema Branching Reference File, so that I only load YAML schema syntax when scaffolding components.
10. As an Infor LN engineer, I want implementation sediment (such as JCA daemon TCP socket mechanics, Eclipse binary property bucket headers, `oob://` registry/clipboard threads, and internal Python module trees) removed from `ln_studio_skill`, so that the agent relies on the deterministic scripts rather than reasoning about internal plumbing.
11. As an Infor LN engineer working with remote servers, I want `ln_studio_skill` to prominently enforce `Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, and `Pre-Commit-Boundary` in its procedural steps, so that authentication alerts, check-out protections, and human final activity approval remain strictly intact.
12. As an Infor LN developer customizing standard tables or sessions via Extension Modeler (`ttext1500m000`), I want `ln_studio_skill` to enforce the `Guide-and-Paste` workflow, so that extensions are authored locally with `#context_on` blocks, statically verified, and delivered hook-by-hook for LN UI without ever attempting LN Studio SCM check-out.
13. As a repository maintainer running the Unified Checks Gateway, I want an automated Skill Markdown Lint Gate that fails if either `SKILL.md` exceeds 80 lines, lacks valid frontmatter, or contains a broken relative reference path, so that documentation bloat and broken links can never regress in CI or pre-commit hooks.
14. As a developer testing skills locally in my IDE, I want the Unified Checks Gateway's drift check and `--sync-skill` flag to cover both `ln_studio_skill` and `erp-ln-progguide`, so that both skills stay synchronized with my global agent configuration in one command.
15. As a contributor reading the project's domain documentation, I want all Leading Words and Progressive Disclosure concepts recorded in the Domain Glossary and ADR 0017, so that future skills and tickets share a consistent architectural vocabulary.

---

## Implementation Decisions

### Decision 1: Retain Dual-Skill Topology with Model-Invoked Context Pointers
- **Scope**: Skill headers for `erp-ln-progguide` and `ln_studio_skill`.
- **Design**: Preserve the **Monorepo Dual-Skill Layout** (ADR 0015) and keep both skills Model-Invoked. Rewrite each YAML frontmatter `description` into a compact two-part pointer:
  1. Positive triggers phrased in natural developer requests (e.g., writing/debugging/auditing Baan 4GL, DAL 2, Extension hooks, SQL, AFS vs. managing LN Studio workspaces, SCM check-out/check-in, generating component XMLs, running `deploy-test`).
  2. Explicit negative boundary (`Do NOT use for...`) directing the agent to the companion skill when a request crosses the seam.

### Decision 2: 4-Step Lean Procedural Structure for `erp-ln-progguide` (`<= 80` Lines)
- **Scope**: `erp-ln-progguide` main instruction file.
- **Design**: Replace the 170-line document with a compact (`~65` lines) procedural router structured around four ordered steps:
  1. **`Search-Before-Read`**: Direct known function lookups to single-line `grep` on the Function Index, and free-text topic lookups to the stdlib search script.
  2. **`Branching Reference Pointers`**: Consolidate the redundant `Layout` tree and `Common tasks` table into a single ~12-row routing table mapping task types to existing cookbooks (`01`–`06`), master indices, and Studio script templates.
  3. **`Core 4GL & Cloud Guardrails`**: Condense the mandatory architectural rules and negative constraints into 6 single-line rules (Separation of Concerns, DAL error convention & no UI dialogs, SQL leading index & `selectempty`, `db.retry.point()` transaction bounds, `domain` variables / `double.cmp` / 1-based arrays, and Cloud Trust / `EXT001` / `EXT002`), deferring detailed code examples to the cookbooks.
  4. **`Audit-Before-Deliver`**: Require running the Standalone 4GL Auditor (`--mode dal2|uedll|general`, `--cloud`) until 0 errors are reported before returning code.

### Decision 3: Branching Reference Extraction & 4-Workflow Router for `ln_studio_skill` (`<= 80` Lines)
- **Scope**: `ln_studio_skill` main instruction file and `references/` directory.
- **Design**:
  - Create three new Branching Reference Files under `ln_studio_skill`'s reference directory:
    1. **CLI Reference (`CLI_REFERENCE.md`)**: Complete subcommand lookup table grouped by lifecycle stage (Environment & Auth, Project & Activity, Explorer & SCM, Code Intelligence & Diff, Component Generation, Extension Modeler Helpers, Validation & Build) plus high-frequency command examples (token status check, one-step extension script export, daemon control).
    2. **MCP Tools Reference (`MCP_TOOLS_REFERENCE.md`)**: The 4 Consolidated High-Efficiency MCP Tools, the 17 Detailed Backward-Compatible MCP Tools, and `mcp-setup` registration commands for Claude, Cursor, and Antigravity.
    3. **Authoring Schema Guide (`AUTHORING_SCHEMA_GUIDE.md`)**: Declarative multi-component YAML specification covering domains, tables, sessions/MMT controllers, libraries, and menus, plus Single-XML TDE Layout rules.
  - Purge internal implementation sediment (`LNStudioJcaBridge` TCP socket internals, `PropertyBucket` binary magic bytes, `oob://` registry/clipboard implementation details, and the 35-file internal Python module list) from the main skill file.
  - Structure the main `ln_studio_skill` instruction file (`~70` lines) around:
    - **Skill Seam & Non-Negotiable Guardrails**: `Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, `Pre-Commit-Boundary`, and `Guide-and-Paste`.
    - **4 Core Procedural Workflows**: (1) Environment Auth & Remote Inspection/Fetch, (2) Standard Component SCM & `deploy-test`, (3) Declarative YAML Component Generation & `validate --fix`, and (4) Extension Modeler (`ttext1500m000`) `Guide-and-Paste` Authoring.
    - **Branching Reference Pointers**: A concise routing table directing the agent to open `CLI_REFERENCE.md`, `MCP_TOOLS_REFERENCE.md`, `AUTHORING_SCHEMA_GUIDE.md`, `COMPONENT_XML_SCHEMA.md`, `DAL2_HOOKS_GUIDE.md`, or `UI_SCRIPT_GUIDE.md` only when needed.

### Decision 4: Automated Skill Markdown Lint Gate & Dual-Skill Synchronization
- **Scope**: Unified Checks Gateway (`scripts/run_checks.py`).
- **Design**:
  - Add `check_skill_markdown(repo_root, max_lines=80)` to the Unified Checks Gateway and execute it as part of the standard check sequence:
    1. Verify both skills' main instruction files exist and start with valid YAML frontmatter containing non-empty `name` and `description` fields.
    2. Enforce that each main skill instruction file has at most `max_lines` (default `80`) lines.
    3. Extract relative paths referenced in Markdown links and inline code pointers (`references/...`, `scripts/...`, `tools/...`, `templates/...`, `index/...`) and verify that every referenced target exists on disk.
  - Generalize `check_skill_drift()` and `sync_global_skill()` (`--sync-skill`) to iterate over both `ln_studio_skill` and `erp-ln-progguide`, synchronizing each skill's verified files to the user's global skills directory (`~/.gemini/config/skills/<skill_name>`).

---

## Testing Decisions

### High-Level Testing Seam
Following the principle of testing external behavior at the highest possible seam with minimal seam proliferation, **all verification centers on a single existing seam: the Unified Checks Gateway (`scripts/run_checks.py`) and its unit test suite (`test_run_checks.py`)**:
- **What makes a good test**: Tests must assert observable contract outcomes—whether `check_skill_markdown()` accepts compliant skill files and rejects files that exceed 80 lines, lack YAML frontmatter, or contain broken reference links; and whether `sync_global_skill()` / `check_skill_drift()` accurately synchronize and detect drift across both skills in isolated temporary directories. Tests must never hardcode exact prose sentences from `SKILL.md`.
- **Modules under test**:
  1. `scripts/run_checks.py` (`check_skill_markdown`, `check_skill_drift`, `sync_global_skill`, and full CLI gateway execution).
  2. Live repository skill artifacts (`erp-ln-progguide/SKILL.md`, `ln_studio_skill/SKILL.md`, and their `references/` files) validated end-to-end by running `check_skill_markdown()` against `REPO_ROOT`.
- **Prior Art**:
  - `ln_studio_skill/tools/tests/test_run_checks.py` (`TestUnifiedChecksAndCi` testing `install_pre_commit_hook` and `sync_global_skill` with `tempfile.TemporaryDirectory`).
  - `ln_studio_skill/tools/tests/test_readme_links.py` (verifying relative Markdown link resolution across repository documentation).

---

## Out of Scope

- Changing the runtime behavior or CLI arguments of `ln_component_builder.py`, `ln_studio_mcp.py`, `audit_4gl.py`, or `search.py`.
- Modifying the contents of the 5,700+ ingested Infor LN reference pages under `erp-ln-progguide/references/guide/`, `sql/`, `extensions/`, `public_interfaces/`, `afs/`, or `dev_tools/`.
- Splitting `erp-ln-progguide` or `ln_studio_skill` into additional top-level skill directories or changing `scripts/package_release.py` archive names.
- Setting `disable-model-invocation: true` on either primary skill (both remain Model-Invoked by design).

---

## Further Notes

- Whenever future lessons are learned from real agent runs (e.g., new 4GL edge cases or Studio CLI recipes), rule details and examples must be added to the appropriate file in `references/` or `scripts/audit_4gl.py` rather than expanding `SKILL.md` past the 80-line ceiling.
