# Architecture Decision Record (ADR) 0016: Modern Developer Platform Documentation & Monorepo README Redesign

## Status
Accepted (Full Consensus Reached across Round 1 & Round 2; Ready for Implementation)

## Date
2026-11-05

## Context & Motivation
Skill_LN has matured from internal automation scripts and reverse-engineered proofs-of-concept into a comprehensive, multi-pillar developer ecosystem:
1. `ln_studio_skill`: Headless JCA 1.6 connector, declarative 12-component Ecore modeling, SCM automation, and native JSON-RPC 2.0 Stdio MCP Server.
2. `erp-ln-progguide`: 5,700+ pages of reference documentation, 2,266 bshell functions with Cloud Multi-Tenant trust ratings, 6 architectural cookbooks, and a standalone zero-dependency 4GL/DAL static audit engine (`audit_4gl.py`).
3. `export/vscode`: Production-ready TextMate grammar, 19 snippets, and 2,491 completion symbols.

However, the existing `README.md` files read predominantly as "internal specification documents" and internal logs:
- High density of internal environment names (`SCS_TST`, `DNT_TRN`, `RDT_TST`, `EXTce01107`).
- Prominent references to internal Architecture Decision Records (`ADR 0005`, `ADR 0006`, `ADR 0007`) in high-level headings.
- Raw ASCII art tables (`+---+---+`) that wrap and break on mobile and narrow viewports.
- Deep, exhaustive tool catalogs (37 CLI subcommands, 16 MCP tools, 14 audit rules) placed on the root page without progressive disclosure.
- Missing standardized GitHub metadata ("About" description and topics).
- Lack of copy-paste ready MCP configuration matrices for modern AI agents (Claude Desktop, Cursor, Antigravity, Gemini).

To attract enterprise architects, ERP LN developers, and AI agent platform builders globally, the repository documentation must transition to a **Modern Developer Platform presentation**.

## Decision Drivers & Consensus (Full Design Tree Settled)

### 1. Root Executive Developer Portal (Q1, Q6, Q7)
- Root `README.md` acts as an Executive Platform Portal:
  - Hero Tagline: *"Unshackle Infor ERP LN Development from the Heavy Eclipse GUI — Built for Terminal & AI Agents."*
  - Direct Download Badges for Pre-built ZIP Bundles (`erp-ln-progguide.zip`, `ln_studio_skill.zip`, `skill-ln-vscode.zip`).
  - 3-Step Zero-Friction Quick Start: (1) Instant Static Audit (offline, zero-dep), (2) Headless Infor LN Connect (`connect --ionapi PRD_ENV.ionapi`), (3) Native AI Agent Integration.
  - Visual Feature Matrix with explicit `❌` vs `✅` indicators.
  - Progressive disclosure: 16 MCP tool signatures and 14 static lint rules condensed into category summary tables with collapsible `<details>` blocks.
  - Historical release notes relocated to `CHANGELOG.md` with only current version highlights.

### 2. Information Sanitization & Traceability (Q2)
- All CLI code snippets and MCP arguments sanitize internal tenant names (`SCS_TST`, `EXTce01107`) to standard placeholders (`PRD_ENV`, `DEV_ENV`, `TRN_ENV`, `PROJ_CUSTOM_01`).
- ADR numbers are removed from prominent headings and preserved as subtle hyperlinks pointing directly to `docs/adr/`.

### 3. Visual Formatting & Safety Hierarchy (Q3)
- Brittle ASCII boxes (`+---+---+`) are replaced by responsive GitHub Markdown tables with Unicode icons and navigation anchors.
- Strict GitHub Alert hierarchy:
  - `[!IMPORTANT]` for the Extension Modeler Cloud UI Boundary (ADR 0006).
  - `[!WARNING]` for the Human Commit Gate on `end-activity` (ADR 0007).

### 4. Pillar 1: Modern DevOps & AI Agent Toolkit (`ln_studio_skill/README.md`) (Q4, Q8)
- Persistent breadcrumb: `[⬅️ Back to Skill_LN Main Repository](../README.md)`
- AI Agent Configuration Matrix with copy-paste JSON configurations for Claude Desktop, Cursor, Antigravity, and Gemini CLI / generic Stdio MCP with explicit environment variable placeholders (`LN_STUDIO_HOME`, `JAVA_HOME`).
- 5-Stage Lifecycle Table organizing the 16 MCP tools and 37 CLI subcommands (Auth, Exploration, Modeling, SCM/Testing, Human Gates).
- Consolidated 12-Component Archetype Matrix with one clean YAML specification and collapsible `<details>` for advanced schemas.

### 5. Pillar 2: Static Linter & Knowledge Base (`erp-ln-progguide/README.md`) (Q5, Q9)
- Persistent breadcrumb: `[⬅️ Back to Skill_LN Main Repository](../README.md)`
- Modern Linter Rule Catalog (5 columns: Rule ID, Category, Severity [Exit Codes: Exit 1 for errors, Exit 0 for warnings], Cloud Multi-Tenant Impact, Description & Fix).
- Before & After 4GL Code Showcase using GitHub `diff` syntax (`-` vs `+`) highlighting SoC (`DAL004`) and float comparisons (`CAV001`).
- Problem-Driven 6 Architectural Cookbooks selection table.
- Architectural rationale for the single-line grep index (`FUNCTION_INDEX.md`) for AI token efficiency.

### 6. Verification & Quality Gate (Q10)
- Automated link integrity script validating 100% of internal anchors (`#...`), cross-file relative links, and asset paths across the three READMEs.
- Clean execution of repository unified checks (`python scripts/run_checks.py`).

## Architectural Decisions
1. **Repository "About" & Hero Banner**:
   - Tagline: *"Unshackle Infor ERP LN Development from the Heavy Eclipse GUI — Built for Terminal & AI Agents."*
   - Description: *"Headless JCA 1.6 toolchain, Native MCP Server, and 4GL Static Audit Engine for Infor ERP LN & CloudSuite"*
   - Topics: `infor-ln`, `baan-4gl`, `mcp-server`, `ai-agent-skills`, `static-analysis`, `erp-automation`, `eclipse-headless`.
2. **Three-Tier Information Architecture**:
   - Root `README.md`: Executive platform overview, 60-second quick start, visual feature comparison (❌ vs ✅), high-level pillar cards, and changelog highlights.
   - `ln_studio_skill/README.md`: Modern DevOps & AI Agent Toolkit guide, 5-phase lifecycle matrix (Auth, Exploration, Modeling, SCM/Testing, Human Gates), MCP JSON configuration snippets, and Extension Modeler cloud guardrail alerts.
   - `erp-ln-progguide/README.md`: Static Linter & Knowledge Base platform guide, 5-column rule catalog table (Ruff/ESLint style), before-and-after 4GL code comparisons, use-case driven cookbook selector, and AI grep-friendly single-line index rationale.
3. **Traceability Preservation**:
   - Rather than eliminating ADR and specification traceability, ADR numbers are moved into subtle badges/links or parenthetical links pointing to `docs/adr/`.
   - Batch release histories are preserved in `CHANGELOG.md` with only current version highlights shown on root.

## Consequences
### Positive
- Elevated repository presentation matching top-tier open-source developer tools.
- Frictionless onboarding for developers using AI agents (Claude Code, Cursor, Antigravity).
- Clear architectural separation between CLI automation, static linting, and IDE grammar.
- Eliminates risk of exposing confidential or internal customer environment names.

### Negative / Trade-offs
- Requires updating cross-links and anchors across 3 primary markdown documents.
- Any future tool additions will need to follow the 5-phase lifecycle and Linter table formats.
