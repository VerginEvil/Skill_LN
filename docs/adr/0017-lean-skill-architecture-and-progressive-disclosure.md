# ADR 0017: Lean Skill Architecture, Progressive Disclosure & Automated Skill Lint Gate

- **Status**: Accepted
- **Date**: 2026-11-09
- **Context**: `/grill-with-docs` Architecture Review (`erp-ln-progguide` & `ln_studio_skill`)

---

## 1. Context and Problem Statement

Over 16 architectural iterations, `Skill_LN`'s two primary skill instruction files accumulated significant reference tables, YAML examples, and internal implementation explanations:
- **`ln_studio_skill/SKILL.md` grew to 430 lines**, embedding a 56-row CLI subcommand table, a 21-row MCP tool table, a 50-line multi-component YAML example, a 45-line internal Python module directory tree, and deep implementation sediment (e.g., `LNStudioJcaBridge` TCP socket internals, `PropertyBucket` binary headers, and `oob://` 3-channel registry/clipboard internals).
- **`erp-ln-progguide/SKILL.md` grew to 170 lines**, containing a 120+ word YAML `description`, redundant `Layout` and `Common tasks` tables, and 55 lines of coding standards that duplicated `references/best_practices/` and `scripts/audit_4gl.py`.

When an AI agent loads a bloated `SKILL.md` into its active context window:
1. **Attention Budget Degradation**: Long static tables and implementation internals dilute procedural instructions, increasing the risk that the model skips critical steps (e.g., skipping `audit_4gl.py` or guessing bshell function names instead of grepping `FUNCTION_INDEX.md`).
2. **Trigger Ambiguity**: Overly dense technical jargon in frontmatter `description` fields or missing negative boundaries causes models to misroute tasks between `erp-ln-progguide` and `ln_studio_skill`.
3. **Unchecked Sediment Accumulation**: Without an automated mechanical check in `scripts/run_checks.py`, future iterations risk re-introducing bloat or broken reference links into `SKILL.md`.

---

## 2. Decision Drivers

1. **Procedural Memory First**: `SKILL.md` must act as a lean procedural router (**<= 80 lines**), teaching *how* to execute tasks step-by-step and *where* to open supporting reference files on demand.
2. **Progressive Disclosure via Branching Reference Files**: Exhaustive command catalogs, MCP tool tables, and declarative YAML schemas must live in dedicated files under `references/`, opened only when a workflow step reaches that branch.
3. **Model-Invoked Trigger Precision**: Frontmatter `description` pointers must use natural task phrasing paired with an explicit negative boundary (`Do NOT use for...`) to prevent skill overlap.
4. **Execution Control via Leading Words**: Standardized, memorable domain terms (`Search-Before-Read`, `Audit-Before-Deliver`, `Guide-and-Paste`, `Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, `Pre-Commit-Boundary`) must anchor each procedural step.
5. **Deterministic Script Enforcement**: What must happen identically every time belongs in Python scripts (`scripts/run_checks.py`), including enforcing the `<= 80` line budget, validating relative links, and synchronizing both skills (`ln_studio_skill` and `erp-ln-progguide`) to the global agent skill directory.

---

## 3. Considered Options

- **Option A: Split into 4+ granular skills (e.g., separate skills for Extensions, SCM, SQL, Studio Generation)**
  - *Pros*: Smaller individual skill folders.
  - *Cons*: Breaks the **Monorepo Dual-Skill Layout (ADR 0015)** and release packaging (`package_release.py`), increases cross-skill routing confusion for Model-Invoked workflows, and fragments shared references.
- **Option B: Retain the Dual-Skill Topology (`erp-ln-progguide` + `ln_studio_skill`), refactor both `SKILL.md` files to <= 80 lines with Branching Reference Files, and enforce via `scripts/run_checks.py` (Chosen)**
  - *Pros*: Preserves ADR 0015 packaging and clear dual-domain separation while cutting active `SKILL.md` context consumption by >75%, eliminating sediment, and mechanically preventing future regression.

---

## 4. Decision Outcome

We adopt **Option B**:

### 4.1 Lean `SKILL.md` Budget (<= 80 Lines) & Sediment Removal
- Both `erp-ln-progguide/SKILL.md` and `ln_studio_skill/SKILL.md` are strictly capped at **80 lines maximum**.
- **Sediment Removal**: Internal script mechanics that require zero agent intervention (JVM socket queues, Eclipse binary bucket headers, registry/clipboard capture threads, internal Python helper filenames) are removed from `SKILL.md`.
- **Single-Source Rules**: No rule or table may appear twice in `SKILL.md`.

### 4.2 Model-Invoked Context Pointers with Negative Boundaries
- Both skills remain **Model-Invoked** (no `disable-model-invocation: true`), with concise frontmatter `description` fields stating:
  1. **What it does & when to use it** (in natural user command phrasing).
  2. **What is NOT its job (`Do NOT use for...`)**, explicitly handing off across the Studio Engine vs. Programmer's Guide seam.

### 4.3 Branching Reference Files Architecture
- **`erp-ln-progguide/SKILL.md`** routes directly to existing index and cookbook files (`references/FUNCTION_INDEX.md`, `references/best_practices/01..06_*.md`, `references/*_INDEX.md`, `templates/`) through a 4-step workflow:
  1. `Search-Before-Read`
  2. `Branching Reference Pointers`
  3. `Core 4GL & Cloud Guardrails`
  4. `Audit-Before-Deliver`
- **`ln_studio_skill/SKILL.md`** extracts its embedded tables and YAML examples into three new **Branching Reference Files** under `ln_studio_skill/references/`:
  1. `references/CLI_REFERENCE.md` — Categorized CLI subcommand reference and high-frequency recipes for `tools/ln_component_builder.py`.
  2. `references/MCP_TOOLS_REFERENCE.md` — Consolidated (4-tool) and detailed (17-tool) Stdio MCP reference (`tools/ln_studio_mcp.py`) and `mcp-setup` registration.
  3. `references/AUTHORING_SCHEMA_GUIDE.md` — Multi-component `schema.yaml` specification and template for declarative object generation.

### 4.4 Standardized Leading Words
Both skills enforce execution discipline using six canonical **Leading Words**:
- **`Search-Before-Read`**: Never guess 4GL signatures or read folders blindly; grep `FUNCTION_INDEX.md` or run `scripts/search.py` first.
- **`Audit-Before-Deliver`**: Always run `audit_4gl.py` / `check-script` to achieve 0 errors before delivering any 4GL, DAL, or Extension code.
- **`Guide-and-Paste`**: Author Extension Modeler (`ttext1500m000`) scripts locally with `#context_on` blocks, verify offline, and output hook-by-hook code blocks for LN UI—never check out or edit extensions in LN Studio.
- **`Pre-Fetch-Auth-Gate`**: Verify OAuth2 token status and emit a user alert with target component/activity metadata before any remote server fetch or check-out.
- **`Read-Only-SCM-Guardrail`**: Never strip OS Read-Only flags manually; require server check-out (`checkout-component`) before modifying checked-in components.
- **`Pre-Commit-Boundary`**: Automate up to `deploy-test` and `prepare-end-activity`, but hard-block `end-activity` so a human engineer approves final delivery.

### 4.5 Automated Skill Markdown Lint Gate & Dual-Skill Sync (`scripts/run_checks.py`)
- `scripts/run_checks.py` is extended with `check_skill_markdown()`, verifying for both `erp-ln-progguide/SKILL.md` and `ln_studio_skill/SKILL.md`:
  1. Valid YAML frontmatter containing non-empty `name` and `description`.
  2. Total line count `<= 80` lines.
  3. 100% resolution of all relative file/directory paths referenced in markdown links or inline code pointers.
- `check_skill_drift()` and `sync_global_skill()` (`--sync-skill`) are upgraded to detect drift and synchronize **both** `ln_studio_skill` and `erp-ln-progguide` to `~/.gemini/config/skills/`.
