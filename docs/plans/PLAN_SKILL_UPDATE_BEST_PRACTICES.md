# Implementation Plan: Infor ERP LN Skill Enhancement & Coding Best Practices

- **Target Skill**: [`erp-ln-progguide`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/erp-ln-progguide/SKILL.md)
- **ADR Reference**: [`docs/adr/0001-plan-skill-update-and-coding-best-practices.md`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/docs/adr/0001-plan-skill-update-and-coding-best-practices.md)
- **Domain Glossary**: [`GLOSSARY.md`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/GLOSSARY.md)

---

## 1. Overview & Objectives

Transform the `erp-ln-progguide` skill from an API/function lookup catalog into a **complete, full-stack Infor LN engineering skill** that actively guides AI and human developers in writing idiomatic, performant, and cloud-compliant code.

### Source Materials:
1. **`update/Infor LN Development Tools 2016.txt`** (360 KB, 13 chapters): Covers the fundamental software development lifecycle, 4GL engine, DAL 1 vs DAL 2, domains, tables, queries, MMT sessions, PMC, and reporting.
2. **`update/Infor LN Extensions Development Guide 108 (01062026).txt`** (285 KB, 16 chapters): Covers modern Extensibility, Extension Modeler, Table/Session/Report/BOD/OData/Menu/Process hooks, CDF logic, and cloud governance.

---

## 2. Knowledge Architecture & Deliverables

```
erp-ln-progguide/
├── references/
│   ├── best_practices/                           # [NEW] Synthesized actionable guides & cookbooks
│   │   ├── 01_extension_hooks_cookbook.md        # Hook lifecycle, execution order, error patterns, CDF logic
│   │   ├── 02_dal_architecture_and_business_logic.md # DAL 1 vs 2, SoC rules, business methods, object sets
│   │   ├── 03_sql_query_optimization_and_transactions.md # Embedded Baan SQL, index matching, locks, retry points
│   │   ├── 04_data_model_and_domain_design.md    # Domain types/formats, table references, reconfig (crdd)
│   │   └── 05_session_and_mmt_patterns.md        # 4GL session types, MMT Controller/Satellite design, forms
│   │
│   ├── dev_tools/                                # [NEW] 13 Chapters converted from Dev Tools 2016
│   │   ├── ch01_development_tools_introduction.md
│   │   ├── ch02_overview_of_software_components.md
│   │   ├── ch03_data_dictionaries.md
│   │   ├── ch04_development_parameters_and_authorizations.md
│   │   ├── ch05_software_development_procedures.md
│   │   ├── ch06_session_personalizations.md
│   │   ├── ch07_version_and_release_management.md
│   │   ├── ch08_ln_software_maintenance.md
│   │   ├── ch09_ln_homepages.md
│   │   ├── ch10_ln_reporting_overview.md
│   │   ├── ch11_4gl_reports.md
│   │   ├── ch12_session_based_reporting.md
│   │   └── ch13_query_based_reporting.md
│   │
│   ├── DEV_TOOLS_INDEX.md                        # [NEW] Overview and chapter map for Development Tools
│   ├── EXTENSIONS_INDEX.md                       # [UPDATED] Cross-linked with extension_hooks_cookbook
│   ├── FUNCTION_INDEX.md                         # Bshell functions index
│   └── ...
│
├── index/
│   └── INDEX.tsv                                 # [UPDATED] Regenerated to index all dev_tools & best_practices
│
├── scripts/
│   └── search.py                                 # Search tool support for --dir dev_tools and --dir best_practices
│
└── SKILL.md                                      # [UPDATED] Core Coding Standards & Best Practice Guardrails
```

---

## 3. Detailed Contents of Best Practice Guides

### 1) `01_extension_hooks_cookbook.md`
- **Extensibility Concepts**: Modifying standard LN without altering base code; last-mile customization.
- **Hook Execution Lifecycle**: Deterministic order during insert/update/delete operations.
- **Error Handling Pattern**: Mandatory usage of `dal.set.error.message("@<msg_code>")` and `return(DALHOOKERROR)`.
- **CDF Logic Hook Cookbook**:
  - `<cdf>.is.applicable()`
  - `<cdf>.is.mandatory()`
  - `<cdf>.is.readonly()`
  - `<cdf>.make.valid()` / `<cdf>.is.valid()`
  - `<cdf>.update()`
- **Standard Field Overrides**: Validating and setting defaults on standard fields via Table/Session hooks.
- **Cloud Governance**: Execution time limits, query record limits, untrusted vs trusted mode, file system sandbox.

### 2) `02_dal_architecture_and_business_logic.md`
- **Separation of Concerns (Cardinal Rule)**: UI scripts handle UI presentation and form flow only. **Never perform database writes or business validations in UI scripts**. All business logic belongs in the DAL.
- **DAL 1 vs DAL 2**: Structural differences, migration considerations, object-oriented concepts in DAL 2.
- **Object Set Hooks**: `before.open.object.set`, `before.read.object`, `set.object.defaults`.
- **Method Authorization**: Controlling allowed actions via `method.is.allowed(long method)`.
- **Business Methods**: Defining public methods on business objects and invoking them.

### 3) `03_sql_query_optimization_and_transactions.md`
- **Embedded Baan SQL Syntax**: `select ... from ... where ... selectdo ... selecteos ... endselect`.
- **Index Optimization Rules**: Index leading field matching, selectivity, avoiding full table scans.
- **Cursor & Memory Management**: Set-oriented fetching (`as set with <N> rows`), clearing cursors, avoiding nested loop queries.
- **Query Extensions**: `query.extend.select()`, `query.extend.from()`, `query.extend.where()`.
- **Transaction & Concurrency Safety**: Transaction boundaries, `db.retry.point()`, `commit.transaction()`, `abort.transaction()`, minimizing lock windows (`for update`).

### 4) `04_data_model_and_domain_design.md`
- **Domain Modeling**: Reusability of domains, display formats, list domains (constants), combined domains, domain check expressions.
- **Table Design**: Primary key selection, candidate indices, foreign key references (Restricted, Cascading, Nullifies).
- **Reconfigure Tables (`crdd`)**: Converting application data dictionary to runtime dictionary, preserving existing data during table restructuring.

### 5) `05_session_and_mmt_patterns.md`
- **Session Types**: Overview (Type 1), Details (Type 2), Multi-Main (Type 3), Print/Processing (Type 4).
- **MMT Architecture**: Controller session with linked Satellite sessions; parent-child synchronization mechanisms.
- **Form Commands & Menus**: Standard form commands vs custom form commands, activating logic.
- **Multi-language Support**: Labels, messages, and questions internationalization best practices.

---

## 4. Tooling & Pipeline Implementation

### 1) `tools/convert_txt_dev_tools.py`
- Parses `update/Infor LN Development Tools 2016.txt`.
- Cleans page breaks (`\x0c`), form feeds, header artifacts, and page number lines.
- Splits into 13 clean Markdown files named `ch01_...md` to `ch13_...md`.
- Generates `erp-ln-progguide/references/DEV_TOOLS_INDEX.md`.

### 2) `tools/generate_indices.py` Update
- Enhance discovery to scan:
  - `references/dev_tools/*.md`
  - `references/best_practices/*.md`
- Add entries to `erp-ln-progguide/index/INDEX.tsv`.

### 3) `tools/validate_skill.py` & `erp-ln-progguide/scripts/search.py` Update
- Ensure validation checks all links in `dev_tools/` and `best_practices/`.
- Ensure `search.py` supports filtering by `--dir dev_tools` and `--dir best_practices`.

---

## 5. Execution Steps

1. **Phase 1: Converter Tooling & Reference Ingestion**
   - Write and run `tools/convert_txt_dev_tools.py`.
   - Verify all 13 chapters and `DEV_TOOLS_INDEX.md` are generated cleanly.
2. **Phase 2: Authoring the Best Practices Suite**
   - Write `01_extension_hooks_cookbook.md`.
   - Write `02_dal_architecture_and_business_logic.md`.
   - Write `03_sql_query_optimization_and_transactions.md`.
   - Write `04_data_model_and_domain_design.md`.
   - Write `05_session_and_mmt_patterns.md`.
3. **Phase 3: Skill Definition & Guardrails Update**
   - Update `erp-ln-progguide/SKILL.md` with Coding Standards & Guardrails.
   - Cross-link in `references/EXTENSIONS_INDEX.md` and `references/DEV_TOOLS_INDEX.md`.
4. **Phase 4: Toolchain & Index Regeneration**
   - Update `tools/generate_indices.py` and run it.
   - Run `tools/validate_skill.py` to confirm zero broken links.
   - Test queries via `erp-ln-progguide/scripts/search.py`.
5. **Phase 5: Final Review & Git Commit**
   - Check diff and status.
