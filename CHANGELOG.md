# Changelog

All notable changes to the **Skill_LN** repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.3] - 2026-11-11

### Added
- **Extension Modeler Non-Context Standard Code Boundary & Anti-Tamper Guardrails (ADR 0020)**:
  - Strict Non-Context Immutability: Mandates all code outside `#context_on "<hook>"` ... `#context_off` as strictly Read-Only / Immutable in `.antigravity/rules/infor_ln.md` Section 5.5.
  - Automatic Extension Detection: Automatically recognizes any 4GL script containing `#context_on` or `#context_off` as an Extension Modeler script.
  - Refined Rule `EXT001`: Recognizes standard generated `#include` headers (`<bic_dal2>`, `<bic_tableext>`, `<bic_sessionext>`, `<bic_text>`, `<bic_interface>`, `<bic_dam>`) under `| Additional generated declarations` as valid boilerplate, avoiding false-positive diagnostics, while custom includes outside `#context_on "declarations"` remain strictly prohibited.
  - New Anti-Tamper Rule `EXT003` (Severity: ERROR) in both `erp-ln-progguide/scripts/audit_4gl.py` and `ln_studio_skill/tools/check_4gl_script.py`: Enforces standard framework function immutability (`get.extension.point.version`, `ext.get.*`), detects improper wrapping of framework functions inside context, detects custom functions or declarations outside context, and enforces balanced `#context_on`/`#context_off` pairs.
  - 8 new unit tests across `ln_studio_skill/tools/tests/test_extension_workflow.py` and `erp-ln-progguide/tests/test_audit_4gl.py` verifying `EXT001` refinement and `EXT003` anti-tamper enforcement (37 tests in `erp-ln-progguide`, 304 in `ln_studio_skill`).

### Changed
- Updated `docs/glossary/GLOSSARY.md` with definitions for `EXT001` refinement and `EXT003`.
- Updated `erp-ln-progguide/references/best_practices/01_extension_hooks_cookbook.md` with Section 8 documenting the non-context code boundary, anti-tamper rules, and dual-mode delivery workflow.
- Updated `ln_studio_skill/SKILL.md` and `erp-ln-progguide/SKILL.md` references while respecting the `<= 80` line budget.

## [1.0.2] - 2026-11-09

### Added
- **4GL String Array & Embedded SQL Host Variable Guardrails (ADR 0019)**:
  - Static audit rule SQL008 (Severity: ERROR) in rp-ln-progguide/scripts/audit_4gl.py: Prohibits array subscripts and parentheses in SQL host variables (:var(...)), preventing SQLState 42I03: Unknown column 'i' (error 302) from the Baan SQL precompiler.
  - Static audit rule ARR002 (Severity: WARNING) in rp-ln-progguide/scripts/audit_4gl.py: Detects 1D domain string array declarations (domain <str_dmn> var(count)) where bshell treats (count) as overriding string length rather than allocating an array of strings.
  - 5 new unit tests in rp-ln-progguide/tests/test_audit_4gl.py covering SQL008 and ARR002 verification (33 total unit tests in rp-ln-progguide, 300 in ln_studio_skill).

### Fixed
- **Baan 4GL Dimensioned Array Documentation**:
  - Corrected Section 6.2 in 
eferences/best_practices/06_4gl_coding_standards_and_caveats.md to remove the misleading domain tcorno recent_orders(10) example and clarify 1D numeric/date/enum arrays (domain <dmn> arr(count) -> rr(i)) vs mandatory 2D string arrays (string arr(len, count) -> rr(1, idx)).
  - Added Section 5.7 to 
eferences/best_practices/06_4gl_coding_standards_and_caveats.md and Section 1.3 to 
eferences/best_practices/03_sql_query_optimization_and_transactions.md establishing the mandatory **Scalar Local Staging Pattern** before embedded SQL execution.
  - Synchronized rp-ln-progguide/SKILL.md Core Guardrails 3 and 5 while maintaining compliance with the strict <= 80 line budget.

## [1.0.1] - 2026-11-09

### Added
- **Lean Skill Architecture & Automated Markdown Lint Gate (ADR 0018)**:
  - Mechanical gate in `scripts/run_checks.py` checking YAML frontmatter validity (`name`, `description`), enforcing a strict `<= 80`-line ceiling, and verifying 100% relative path link integrity across all skills.
  - Dual-skill synchronization and drift detection (`--sync-skill`) for both `ln_studio_skill` and `erp-ln-progguide` to `~/.gemini/config/skills/`.
  - Dedicated Branching Reference Files in `ln_studio_skill/references/`: `CLI_REFERENCE.md` (50+ subcommands), `MCP_TOOLS_REFERENCE.md` (4 consolidated + 17 detailed tools), and `AUTHORING_SCHEMA_GUIDE.md` (multi-component YAML specs).
- **Runtime Error Prevention & 4GL Audit Guardrails (ADR 0017)**:
  - Five new static audit rules in `erp-ln-progguide/scripts/audit_4gl.py`:
    - `DMN002`: Combined date/time field storage caveat (`utc.num()` vs legacy Julian date + time integers).
    - `TBL003`: Leading index alignment and `as set with 1 rows` query performance optimization.
    - `DMN003`: Enum domain zero-value and empty initialization safeguard (`.empty`).
    - `STR001`: Trailing space stripping in string comparisons (`strip$()` / `trim$()`).
    - `DBG001`: Residual debug statements detection (`suspend()`, `message()`, `inputstr()`).
  - Auto-injection of sequence fields (`tset`) for primary keys lacking trailing sequence numbers in `ln_studio_skill/tools/generate_ln_table.py`.
  - Comprehensive unit test suite in `erp-ln-progguide/tests/test_audit_4gl.py` (28 tests).

### Changed
- **Lean Procedural Architecture for `erp-ln-progguide/SKILL.md`**: Refactored from 170 lines down to 48 lines with natural Context Pointer, explicit negative boundary (`Do NOT use for...`), 4-step workflow (`Search-Before-Read` -> `Branching Reference Pointers` -> `Core 4GL & Cloud Guardrails` -> `Audit-Before-Deliver`), and direct cookbook routing.
- **Lean Procedural Architecture for `ln_studio_skill/SKILL.md`**: Refactored from 430 lines down to 51 lines with natural Context Pointer, negative boundary, non-negotiable guardrails (`Pre-Fetch-Auth-Gate`, `Read-Only-SCM-Guardrail`, `Pre-Commit-Boundary`, `Guide-and-Paste`), and 4 core procedural workflows.
- **Implementation Sediment Removal**: Purged TCP socket internals, binary property bucket headers, clipboard/registry implementation details, and internal Python module lists from active `SKILL.md` contexts.
- **Unified Test Discovery**: Extended `scripts/run_checks.py` to automatically discover and run all tests across both `erp-ln-progguide/tests` and `ln_studio_skill/tools/tests` (300 total tests passing).

---

## [1.0.0] - 2026-11-05

### Added

#### Core Pillar 1: Infor LN Studio Automation & Stdio MCP Skill (`ln_studio_skill`)
- **Native Stdio MCP Server (`ln_studio_mcp.py`)**: 16 JSON-RPC tools with unified tool envelope, input schemas, and error taxonomy for AI agents (Antigravity, Cursor, Claude Code).
- **Headless JCA 1.6 Bridge**: Pure Python and Bring-Your-Own-Jar (BYOJ) bridge communicating with Infor LN Enterprise Server via Business Data Entity (BDE) XML protocol without running Eclipse GUI.
- **Component Generators**: Automated generation for 12 Infor LN Studio component archetypes (Tables, Sessions, Scripts, Menus, Domains, Labels, Messages, Questions, Functions, Additional Files, Reports, MMT Controllers).
- **Single-XML TDE Layout Guardrail**: Automatic enforcement and repair preventing XML fragment split corruptions.
- **Pre-Commit SCM Engine**: Authentic check-in/check-out lifecycle with read-only OS file locks, pre-put script merge protection, and change conflict prevention.
- **Authentication**: CloudSuite OAuth2 (`.ionapi`) with out-of-band (OOB) browser login and local encrypted token cache.

#### Core Pillar 2: Programmer's Guide, Dev Tools & Audit Engine (`erp-ln-progguide`)
- **Knowledge Base**: 5,700+ pages of Infor LN 10.8 (Build 0640) technical reference documentation converted to grep-friendly Markdown.
- **Function Index**: 2,266 bshell and 4GL functions indexed with cloud trust ratings and documentation links.
- **Standalone 4GL Audit Engine (`audit_4gl.py`)**: Zero-dependency static analyzer enforcing 20+ lint rules, cloud governance checks, DAL/UI separation of concerns, and Extension Modeler standards (`EXT001`, `EXT002`).
- **Architecture Cookbooks**: 6 best-practice guides covering DAL 2, Extension Modeler, Baan SQL optimization, and CloudSuite extensibility.

#### Core Pillar 3: VS Code Extension Assets (`export/vscode`)
- **4GL Syntax Grammar**: TextMate grammar (`baan4gl.tmLanguage.json`) supporting Infor LN 4GL keywords, preprocessor directives, and embedded SQL.
- **Code Snippets & Completions**: 19 official 4GL templates, DAL hooks, and function signature auto-completions.

#### Repository & CI/CD Toolchain
- **GitHub Actions Workflows**: Automated syntax, layout, and hermetic unit testing pipeline (`.github/workflows/ci.yml`).
- **Release Automation (`.github/workflows/release.yml`)**: Automated build and distribution of ZIP packages (`erp-ln-progguide.zip`, `ln_studio_skill.zip`, `skill-ln-vscode.zip`) on tag push.
- **Packaging Utility (`scripts/package_release.py`)**: Standalone cross-platform distribution bundler.
- **Domain Documentation**: Reorganized architecture layout with `docs/glossary/GLOSSARY.md`, `docs/plans/`, and ADR history (`0001` - `0015`).
- **Hardened Security**: `.gitignore` audit preventing leak of Infor credentials, token caches, and proprietary offline manuals.
