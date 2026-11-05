# Implementation Plan: Modern Developer Platform Documentation & Monorepo README Redesign

- **Specification / Context**: `/grill-with-docs`
- **Architecture Decision Record**: [`docs/adr/0016-modern-developer-platform-documentation-and-readme-redesign.md`](docs/adr/0016-modern-developer-platform-documentation-and-readme-redesign.md)
- **Target Deliverables**:
  1. `README.md` (Root Repository)
  2. `ln_studio_skill/README.md` (Pillar 1: Automation & MCP)
  3. `erp-ln-progguide/README.md` (Pillar 2: Knowledge Base & Static Linter)
  4. Repository Metadata (GitHub About & Topics proposal)

---

## 1. Objectives & Design Principles

Transform Skill_LN documentation from internal technical specifications into an international, modern developer platform:
- **Global & Modern Identity**: Strong value proposition, powerful hero banner, clean badges, professional branding.
- **Visual Hierarchy & Progressive Disclosure**: Executive portal pattern on root, deep references on sub-READMEs, collapsible details for comprehensive matrices, GitHub alert callouts.
- **Seamless Monorepo Navigation**: Hero nav bars, breadcrumbs, consistent cross-links across modules.
- **Sanitized Realistic Enterprise Identifiers**: Standardized placeholders (`PRD_ENV`, `DEV_ENV`, `TRN_ENV`, `PROJ_CUSTOM_01`), moving ADR numbers to clean footnotes.
- **AI-Agent Ready**: Copy-paste JSON configurations for Claude Desktop, Cursor, Antigravity, and Gemini CLI.

---

## 2. Decision Tree Status
- **Round 1 (Consensus Reached)**:
  - [x] Q1: Root README acts as Executive Platform Portal; CLI/MCP reference migrated to sub-READMEs.
  - [x] Q2: Sanitized environment identifiers (`PRD_ENV`, etc.) & subtle ADR hyperlinks.
  - [x] Q3: Responsive Markdown card tables & GitHub alert hierarchy (`[!IMPORTANT]`, `[!WARNING]`).
  - [x] Q4: Copy-paste JSON matrix for 4 AI agent platforms in `ln_studio_skill/README.md`.
  - [x] Q5: Linter-style 5-column Rule Catalog, Before/After 4GL code diffs, and single-line grep rationale in `erp-ln-progguide/README.md`.
- **Round 2 (Consensus Reached)**:
  - [x] Q6: 60-Second Quick Start 3-step zero-friction path on Root README.
  - [x] Q7: Direct download links for pre-packaged ZIP releases in Hero section.
  - [x] Q8: 12-Component Archetype Matrix with single consolidated YAML spec in `ln_studio_skill/README.md`.
  - [x] Q9: Linter CI/CD severity behaviors (Exit codes) and GitHub `diff` formatting in `erp-ln-progguide/README.md`.
  - [x] Q10: Automated relative link and anchor validation gate.
- **Frontier Status**: Empty. All design branches visited and settled. Ready for Execution.

---

## 2. Work Breakdown Structure (Phased Execution)

### Phase 1: Root `README.md` Modernization
- [ ] Add Hero Navigation Bar: `[⚡ Quick Start] • [🛠 Studio MCP Skill] • [📚 4GL Audit & Guide] • [🎨 VS Code Assets] • [📖 Docs & ADRs]`
- [ ] Update Hero Banner & Tagline: *"Unshackle Infor ERP LN Development from the Heavy Eclipse GUI — Built for Terminal & AI Agents."*
- [ ] Convert ASCII Box (`+---+---+`) to responsive Markdown Card Table with Unicode icons and navigation links.
- [ ] Refactor Feature Matrix (Eclipse GUI vs Skill_LN Headless) with explicit `❌` / `✅` visual diffs.
- [ ] Sanitize internal tenant names (`SCS_TST`, `DNT_TRN`, `EXTce01107` -> `PRD_ENV`, `DEV_ENV`, `PROJ_CUSTOM_01`).
- [ ] Replace inline ADR headings with parenthetical references pointing to `docs/adr/`.
- [ ] Condense "What's New in Recent Major Updates" to a high-impact summary with `<details>` block pointing to `CHANGELOG.md`.
- [ ] Wrap extensive 16 MCP tool and 14 audit rule listings into `<details>` progressive disclosure dropdowns.

### Phase 2: `ln_studio_skill/README.md` Modernization (Pillar 1: Automation & MCP)
- [ ] Add breadcrumb navigation: `[⬅️ Back to Skill_LN Main Repository](../README.md)`
- [ ] Add AI Agent Configuration Matrix with direct copy-paste JSON snippets:
  - Claude Desktop (`claude_desktop_config.json`)
  - Cursor (`.cursor/mcp.json`)
  - Antigravity (`antigravity.json`)
  - Gemini CLI / Generic Stdio MCP
- [ ] Group 16 MCP Tools & 37 CLI Subcommands into a 5-Stage Lifecycle Table:
  1. *Environment & Auth*: `connect`, `environments`
  2. *Remote Exploration*: `explore_projects`, `explore_activities`, `explore_components`
  3. *Component Modeling & Cloning*: `create_component` (12 types), `clone_component`, `sync-reference`
  4. *SCM & Live Cloud Testing*: `checkout`, `uncheckout`, `checkin`, `deploy_test`
  5. *Verification & Human Gate*: `validate_activity`, `prepare_end_activity`, `end_activity`
- [ ] Insert GitHub Alert `[!IMPORTANT]` on Extension Modeler boundary: Read-only check-out interception, `import-extension`, `#context_on` clipboard extraction, and LN UI Cloud paste workflow.
- [ ] Insert GitHub Alert `[!WARNING]` on Human Commit Gate: hard-blocked `end-activity` and SCM safety.

### Phase 3: `erp-ln-progguide/README.md` Modernization (Pillar 2: Linter & Knowledge Base)
- [ ] Add breadcrumb navigation: `[⬅️ Back to Skill_LN Main Repository](../README.md)`
- [ ] Standardize `audit_4gl.py` Rule Catalog into a 5-Column Linter Table:
  - `Rule ID` | `Category` | `Severity` | `Cloud Impact` | `Description & Recommended Fix`
- [ ] Add Before & After Baan 4GL Code Showcase:
  - Direct database mutation in UI script (SoC violation `DAL004`) vs Clean DAL2 business logic.
  - Dangerous float equality comparison (`CAV001`) vs `double.cmp()`.
  - Misplaced `#include` outside `#context_on` (`EXT001`).
- [ ] Restructure 6 Architectural Cookbooks into a Problem-Driven Selection Guide:
  - "Writing Table/Session Extensions?" -> `01_extension_hooks_cookbook.md`
  - "Structuring Business Logic & Validations?" -> `02_dal_architecture_and_business_logic.md`
  - "Optimizing Baan SQL & Transactions?" -> `03_sql_query_optimization_and_transactions.md`
  - "Designing Domains & Table Reconfiguration?" -> `04_data_model_and_domain_design.md`
  - "Building MMT Controller/Satellites?" -> `05_mmt_sessions_and_satellites.md`
  - "Avoiding Subshell Traps & Float Bugs?" -> `06_common_caveats_and_anti_patterns.md`
- [ ] Add architectural explanation: "Why Single-Line Function Index?" explaining how `FUNCTION_INDEX.md` enables sub-second, token-efficient `grep` lookup for AI agents without bloating context windows.

### Phase 4: Quality Verification & Link Integrity
- [ ] Run automated repository test suite (`python scripts/run_checks.py`) to confirm zero regressions.
- [ ] Verify all relative Markdown links and anchor tags across the 3 READMEs.
