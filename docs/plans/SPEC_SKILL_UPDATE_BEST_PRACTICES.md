# Specification: Infor ERP LN Skill Enhancement & Coding Best Practices

## Problem Statement

The current `erp-ln-progguide` skill functions primarily as an API syntax dictionary and function reference lookup. While it contains comprehensive bshell function signatures and converted extension pages, it leaves developers and AI coding agents with critical knowledge gaps when designing, implementing, and optimizing Infor ERP LN solutions:

1. **Lack of Prescriptive Coding Best Practices:** Developers and AI assistants have no centralized guidance on the architectural "rules of the road" in Infor LN—such as strict Separation of Concerns (SoC) between UI scripts and DAL, when to use DAL 1 vs DAL 2, how to manage database transaction scopes, and how to avoid costly deadlocks and performance degradations.
2. **Missing Infor LN Development Tools Core Knowledge:** Foundational development workflows and component architectures documented in *Infor LN Development Tools* (e.g. Data Dictionaries, domain modeling, table reconfiguration via `crdd`, 4GL Engine execution flow, MMT Controller/Satellite sessions, PMC solution packaging, and 4GL reporting) are currently completely absent from the skill repository.
3. **Absence of Actionable Extension Hook Recipes:** Although raw chapters of the *Infor LN Extensions Development Guide 10.8* exist, developers lack practical cookbooks showing exact hook lifecycle execution sequences, standardized error signaling using `dal.set.error.message("@...")` and `return(DALHOOKERROR)`, Customer Defined Field (CDF) logic patterns (`is.applicable`, `is.mandatory`, `make.valid`, `update`), and Infor Cloud governance constraints.
4. **Ineffective AI Code Generation Guardrails:** When prompted to write LN 4GL or extension code, AI agents often generate anti-patterns (such as writing database queries/updates directly inside UI scripts, using unindexed queries, or omitting retry points) because the skill's root prompt does not enforce architectural guardrails.

---

## Solution

Upgrade the `erp-ln-progguide` skill through a hybrid approach combining complete reference ingestion, a dedicated best practices cookbook suite, and reinforced prompt guardrails:

1. **Ingest Complete Development Tools Reference (`references/dev_tools/`):**
   Parse and convert all 13 chapters of *Infor LN Development Tools 2016* into clean, standardized Markdown reference files with a dedicated overview index (`DEV_TOOLS_INDEX.md`).
2. **Author Prescriptive Best Practices Suite (`references/best_practices/`):**
   Create 5 highly focused, modular cookbooks and architectural guides:
   - `01_extension_hooks_cookbook.md` (Extensibility, hook lifecycles, error returns, CDF logic hooks, cloud limits)
   - `02_dal_architecture_and_business_logic.md` (DAL 1 vs DAL 2, SoC principles, object set hooks, business methods)
   - `03_sql_query_optimization_and_transactions.md` (Embedded Baan SQL, index alignment, cursor lifecycle, transaction/lock boundaries)
   - `04_data_model_and_domain_design.md` (Domain modeling, reference integrity, `crdd` table reconfiguration safety)
   - `05_session_and_mmt_patterns.md` (4GL session types 1-4, MMT Controller/Satellite architecture, dynamic forms, internationalization)
3. **Embed Coding Standards & Guardrails into Skill Definition (`SKILL.md`):**
   Update the root skill definition with explicit architectural guardrails and anti-pattern warnings that AI agents must enforce when analyzing or generating Infor LN code.
4. **Enhance Toolchain & Indexing (`tools/`):**
   Implement a clean TXT-to-Markdown converter (`tools/convert_txt_dev_tools.py`), update `tools/generate_indices.py` to index all new files into `INDEX.tsv`, and update `tools/validate_skill.py` and `scripts/search.py` to support and validate the new content.

---

## User Stories

1. As an LN developer, I want to reference the complete *Infor LN Development Tools* manual in Markdown format, so that I can understand software components, VRC structures, and development procedures without consulting legacy PDF/Word files.
2. As an LN developer, I want clear guidance on the difference between Application Data Dictionary and Runtime Data Dictionary, so that I understand when and how to perform table reconfiguration (`crdd`) safely without data loss.
3. As an LN developer, I want a comprehensive Extension Hooks cookbook, so that I can implement table and session extension hooks with correct function signatures, lifecycle execution ordering, and error return codes.
4. As an LN developer, I want standard recipes for Customer Defined Field (CDF) hooks (`is.applicable`, `is.mandatory`, `is.readonly`, `make.valid`, `update`), so that custom business validations on standard tables work reliably.
5. As an LN developer, I want to understand Infor Cloud Extensibility Governance limits, so that my extension scripts comply with execution time limits, query limits, and untrusted code sandboxing.
6. As an AI assistant, I want strict architectural guardrails in `SKILL.md`, so that I never generate database update operations in UI scripts and always encapsulate business rules inside DAL or Table Extensions.
7. As an LN developer, I want an in-depth DAL 1 vs DAL 2 guide, so that I can choose the appropriate DAL architecture, implement property hooks, and define callable business methods correctly.
8. As an LN developer, I want concrete guidelines on Embedded Baan SQL query optimization, so that my queries align with table indices, avoid table locks, and prevent full table scans.
9. As an LN developer, I want best practices for cursor management and transaction boundaries (`db.retry.point()`, `commit.transaction()`, `abort.transaction()`), so that data modifications maintain ACID guarantees without causing deadlocks.
10. As an LN developer, I want a guide on domain design and reference integrity, so that table relationships enforce cascade or restricted deletion modes consistently.
11. As an LN developer, I want architectural patterns for Multi-Main Table (MMT) sessions, so that Controller and Satellite sessions synchronize parent-child records seamlessly.
12. As an LN developer, I want reporting architecture guidelines (4GL reports vs Session-based vs Query-based reports), so that I can design and maintain reports with Report Viewer integration.
13. As an LN developer, I want search CLI support (`search.py --dir dev_tools` and `--dir best_practices`), so that I can quickly query development procedures and best practices from the command line.
14. As a repository maintainer, I want automated verification (`validate_skill.py`), so that broken links, missing index mappings, or malformed markdown files are caught immediately during build.

---

## Implementation Decisions

### 1. Structure of New Content
- Ingest 13 chapters of *Infor LN Development Tools 2016* into `erp-ln-progguide/references/dev_tools/` named `ch01_development_tools_introduction.md` through `ch13_query_based_reporting.md`.
- Provide a navigation map in `erp-ln-progguide/references/DEV_TOOLS_INDEX.md`.
- Establish 5 focused guides in `erp-ln-progguide/references/best_practices/`:
  - `01_extension_hooks_cookbook.md`
  - `02_dal_architecture_and_business_logic.md`
  - `03_sql_query_optimization_and_transactions.md`
  - `04_data_model_and_domain_design.md`
  - `05_session_and_mmt_patterns.md`

### 2. Guardrails in Root Skill Definition
- Update `erp-ln-progguide/SKILL.md` to add:
  - "Infor LN Coding Standards & Architectural Guardrails" highlighting the Separation of Concerns, DAL placement rules, query index rules, and hook error conventions.
  - Quick-navigation table linking directly to the new `best_practices/` and `dev_tools/` guides.

### 3. Toolchain & Conversion Architecture
- Implement `tools/convert_txt_dev_tools.py` in pure Python (standard library only) to parse `update/Infor LN Development Tools 2016.txt`. The parser must:
  - Strip form feeds (`\x0c`), recurring header lines, copyright notices, and page numbering.
  - Detect chapter and section headings and generate cleanly formatted Markdown `#`, `##`, `###` headings.
  - Detect and structure procedure steps, summaries, and bullet lists.
- Update `tools/generate_indices.py` to scan `dev_tools/` and `best_practices/` and append all page titles into `erp-ln-progguide/index/INDEX.tsv`.
- Update `erp-ln-progguide/scripts/search.py` and `tools/validate_skill.py` to recognize `dev_tools` and `best_practices` directory trees.

---

## Testing Decisions

### 1. Behavior-Only Testing Principles
- Tests must verify external behavior and data integrity: file existence, link resolution, index consistency, search query hits, and exit codes.
- Do not assert on private internal helper functions of the conversion script.

### 2. Modules to Test
- `tools/convert_txt_dev_tools.py`: Verify that all 13 chapter markdown files and `DEV_TOOLS_INDEX.md` are generated with positive file sizes, valid UTF-8 encoding, and zero `\x0c` form feeds.
- `tools/generate_indices.py`: Verify that `index/INDEX.tsv` includes valid paths and titles for every generated file in `dev_tools/` and `best_practices/`.
- `tools/validate_skill.py`: Run full skill validation to assert that every relative link resolves, all indexed files exist, and no orphaned pages exist.
- `erp-ln-progguide/scripts/search.py`: Verify search hits for representative queries (e.g. `crdd`, `DALHOOKERROR`, `MMT Controller`, `query.extend.where`).

### 3. Prior Art
- Existing unit tests in `tools/tests/test_convert_chm.py` and `tools/tests/test_indices.py`.
- Automated test command: `python tools/validate_skill.py`.

---

## Out of Scope

- Developing or altering actual Infor LN Enterprise Server binaries or bshell runtime executables.
- Ingesting or altering binary `.chm` or `.pdf` files outside the two designated text documents in `update/`.
- Modifying the Infor LN Studio Eclipse RCP automation tools (`tools/ln_component_builder.py`, etc.) which reside in a separate sub-project.

---

## Further Notes

- All Markdown files must strictly use UTF-8 encoding and relative Markdown links.
- The glossary established in `GLOSSARY.md` and architectural decisions in `docs/adr/0001-plan-skill-update-and-coding-best-practices.md` serve as the canonical semantic reference.
