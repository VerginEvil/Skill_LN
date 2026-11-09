# Implementation Plan: Lean Skill Architecture, Progressive Disclosure & Automated Skill Lint Gate

- **Specification**: [`docs/plans/SPEC_LEAN_SKILL_ARCHITECTURE.md`](SPEC_LEAN_SKILL_ARCHITECTURE.md) (`.scratch/lean-skill-architecture/spec.md`)
- **Architecture Decision Record**: [`docs/adr/0018-lean-skill-architecture-and-progressive-disclosure.md`](../adr/0018-lean-skill-architecture-and-progressive-disclosure.md)
- **Active Tickets**: [`docs/plans/Tickets.md`](Tickets.md) (`.scratch/lean-skill-architecture/issues/01..04-*.md`)
- **Target Deliverables**:
  1. `scripts/run_checks.py` & `ln_studio_skill/tools/tests/test_run_checks.py` (Skill Markdown Lint Gate + Dual-Skill Sync)
  2. `erp-ln-progguide/SKILL.md` (Refactored from 170 lines to `<= 80` lines)
  3. `ln_studio_skill/references/CLI_REFERENCE.md` (Extracted 50+ CLI subcommands & common recipes)
  4. `ln_studio_skill/references/MCP_TOOLS_REFERENCE.md` (Extracted 21 MCP tools & `mcp-setup` guide)
  5. `ln_studio_skill/references/AUTHORING_SCHEMA_GUIDE.md` (Extracted multi-component `schema.yaml` guide)
  6. `ln_studio_skill/SKILL.md` (Refactored from 430 lines to `<= 80` lines)

---

## 1. Objectives & Design Principles

1. **Lean Procedural Memory (`<= 80` Lines)**: Keep `SKILL.md` ultra-thin so AI agents absorb the step-by-step workflow and non-negotiable guardrails without burning context window tokens on static tables.
2. **Progressive Disclosure via Branching Reference Files**: Move exhaustive CLI tables, MCP catalogs, and YAML schemas into dedicated files under `references/`, opened only when a workflow step reaches that branch.
3. **High-Precision Model-Invoked Context Pointers**: Write frontmatter `description` fields with natural developer phrasing and explicit `Do NOT use for...` negative boundaries so `erp-ln-progguide` and `ln_studio_skill` never compete for the same task.
4. **Execution Control with Leading Words**: Anchor every step with canonical domain terms (`Search-Before-Read`, `Audit-Before-Deliver`, `Guide-and-Paste`, `Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, `Pre-Commit-Boundary`).
5. **Deterministic Gate Enforcement**: Enforce the `<= 80`-line ceiling, YAML frontmatter presence, and 100% relative link resolution inside `scripts/run_checks.py` so documentation bloat cannot return.

---

## 2. Decision Tree Status (`/grill-with-docs`)

- **Round 1 (Consensus Reached)**:
  - [x] **Q1 (Skill Topology)**: Retain the 2 core skills (`erp-ln-progguide` and `ln_studio_skill`) per ADR 0015 and use Branching Reference Files rather than splitting into additional top-level skills.
  - [x] **Q2 (Invocation Strategy)**: Keep both skills Model-Invoked with natural-language `description` triggers and explicit `Do NOT use for...` negative boundaries.
  - [x] **Q3 (Line Budget & Sediment Removal)**: Cap `SKILL.md` at `<= 80` lines, purge internal implementation sediment (JVM TCP sockets, binary headers, `oob://` internals, internal module lists), and move large tables/YAML specs to `references/`.
  - [x] **Q4 (Leading Words)**: Standardize on `Search-Before-Read`, `Audit-Before-Deliver`, `Guide-and-Paste`, `Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, and `Pre-Commit-Boundary` across skills, `GLOSSARY.md`, and ADR 0018.
- **Round 2 (Consensus Reached)**:
  - [x] **Q5 (`erp-ln-progguide/SKILL.md` Structure)**: Organize into 4 procedural steps (`Search-Before-Read` -> `Branching Reference Pointers` -> `Core 4GL & Cloud Guardrails` -> `Audit-Before-Deliver`) routing to existing `references/` files.
  - [x] **Q6 (`ln_studio_skill` Branching Reference Files)**: Create `CLI_REFERENCE.md`, `MCP_TOOLS_REFERENCE.md`, and `AUTHORING_SCHEMA_GUIDE.md` in `ln_studio_skill/references/`, reducing `ln_studio_skill/SKILL.md` to 4 core workflows + guardrails + pointers.
  - [x] **Q7 (Automated Lint Gate & Dual-Skill Sync)**: Add `check_skill_markdown()` (`<= 80` lines, frontmatter, relative links) and dual-skill `--sync-skill` support to `scripts/run_checks.py` with unit tests.
- **Frontier Status**: Empty. Shared understanding confirmed.

---

## 3. Work Breakdown Structure (Tracer-Bullet Tickets)

### Ticket 01: Automated Skill Markdown Lint Gate & Dual-Skill Synchronization (`scripts/run_checks.py`)
- **Blocked by**: *None (can start immediately)*
- **Deliverables**:
  - Implement `check_skill_markdown(repo_root, max_lines=80)` in `scripts/run_checks.py` checking frontmatter (`name`, `description`), line budget (`<= 80`), and relative file/directory references.
  - Add `--skill-lint-only` CLI flag and integrate `check_skill_markdown` into the default `run_checks.py` pipeline.
  - Upgrade `check_skill_drift()` and `sync_global_skill()` to support both `ln_studio_skill` and `erp-ln-progguide`.
  - Add unit tests in `ln_studio_skill/tools/tests/test_run_checks.py` verifying pass/fail conditions in isolated temp directories.

### Ticket 02: Lean Procedural Refactoring of `erp-ln-progguide/SKILL.md`
- **Blocked by**: **Ticket 01**
- **Deliverables**:
  - Rewrite `erp-ln-progguide/SKILL.md` frontmatter `description` with natural triggers and `Do NOT use for...` negative boundary.
  - Replace the 170-line body with the 4-step procedural workflow (`Search-Before-Read`, `Branching Reference Pointers`, `Core 4GL & Cloud Guardrails`, `Audit-Before-Deliver`) under 80 lines.
  - Verify `erp-ln-progguide/SKILL.md` passes `check_skill_markdown()` with 0 broken links.

### Ticket 03: `ln_studio_skill` Branching Reference Extraction & Lean `SKILL.md` Refactoring
- **Blocked by**: **Ticket 01**
- **Deliverables**:
  - Create `ln_studio_skill/references/CLI_REFERENCE.md` (all CLI subcommands grouped by workflow + practical recipes).
  - Create `ln_studio_skill/references/MCP_TOOLS_REFERENCE.md` (4 consolidated + 17 detailed MCP tools + `mcp-setup`).
  - Create `ln_studio_skill/references/AUTHORING_SCHEMA_GUIDE.md` (multi-component `schema.yaml` spec & Single-XML TDE rules).
  - Rewrite `ln_studio_skill/SKILL.md` (`<= 80` lines) with natural Context Pointer, Non-Negotiable Guardrails (`Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, `Pre-Commit-Boundary`, `Guide-and-Paste`), 4 Core Procedural Workflows, and Branching Pointers.
  - Verify `ln_studio_skill/SKILL.md` passes `check_skill_markdown()` with 0 broken links.

### Ticket 04: End-to-End Gateway Verification, Packaging & Global Skill Synchronization
- **Blocked by**: **Ticket 02, Ticket 03**
- **Deliverables**:
  - Run `python scripts/run_checks.py --sync-skill` to verify all unit tests, syntax checks, Single-XML layout checks, and Skill Markdown Lint Gate pass, and synchronize both skills to `~/.gemini/config/skills/`.
  - Verify release bundle generation (`python scripts/package_release.py`) includes the new Branching Reference Files cleanly.
