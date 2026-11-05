# Implementation Plan: Baan 4GL Coding Standards, Anti-Patterns, and Runtime Caveats

- **Target Skill**: [`erp-ln-progguide`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/erp-ln-progguide/SKILL.md)
- **Specification Document**: [`docs/SPEC_4GL_CODING_STANDARDS_AND_CAVEATS.md`](file:///c:/Users/nutdo/OneDrive/Documents/Gitlab/Skill_LN/docs/SPEC_4GL_CODING_STANDARDS_AND_CAVEATS.md)
- **ADR Reference**: [`ADR-001`](file:///C:/Users/nutdo/.gemini/antigravity/brain/1baebaac-c9c2-4a5c-8125-6fb7d4002b9d/adr-001-4gl-best-practices.md)

---

## 1. Overview & Objectives

Transform the `erp-ln-progguide` skill by incorporating comprehensive language-level 4GL fundamentals, defensive coding patterns, and bshell runtime caveats across 6 critical areas. This upgrade eliminates common AI hallucination pitfalls and developer bugs, ensuring all generated or refactored Infor LN code strictly follows enterprise cloud standards.

### The 6 Core Pillars:
1. **Domain, Variable, and Scope Declaration**: Domain vs. primitive types (`long`, `string`, `double`), enumeration/set domain binding, local function variable scope confinement, restricted `extern` usage.
2. **DLL Linkage, Preprocessor Directives, and Macros**: `#pragma used dll "o..."` syntax, `#include <...>` vs. `#include "..."`, macro capitalization, and reserved keyword conflict prevention.
3. **Function Architecture and Parameter Passing**: Directional Hungarian parameter naming (`i.`, `o.`, `io.`), immutability enforcement with `const`, pass-by-reference with `ref`, standardized return codes (0 for OK, negative for errors).
4. **Embedded SQL & Table Record Buffer Protection**: Global record buffer overwrite mechanics, column-to-local variable binding, Table Aliases, `as set with 1 rows` point queries, explicit field predicates over `_index`, and DAL delegation (`dal.change.object()` / `dal.save.object()`) over raw `db.update()` / `db.insert()`.
5. **Domain Arrays and Dimensions**: 1-based indexing, element count definitions, and array parameter passing conventions (`fixed` and `()`).
6. **Critical Syntax Caveats & Anti-Patterns**: Floating-point epsilon comparison via `double.cmp()`, outer-boundary transaction orchestration (prohibiting commits inside DAL hooks and helper DLLs), 4GL reserved keywords avoidance, mandatory `selectempty` fallbacks, strict prohibition of `goto`, and narrow row locking windows with immediate error rollback.

---

## 2. Target File Structure & Changes

```
erp-ln-progguide/
├── references/
│   ├── best_practices/
│   │   ├── 01_extension_hooks_cookbook.md
│   │   ├── 02_dal_architecture_and_business_logic.md
│   │   ├── 03_sql_query_optimization_and_transactions.md   # [UPDATED: Cross-link to buffer protection & lock scope]
│   │   ├── 04_data_model_and_domain_design.md              # [UPDATED: Cross-link to domain vs primitive rules]
│   │   ├── 05_session_and_mmt_patterns.md
│   │   └── 06_4gl_coding_standards_and_caveats.md          # [NEW: Complete 6-pillar reference & Do/Don't guide]
│   └── ...
├── index/
│   └── INDEX.tsv                                           # [UPDATED: Register new 06 guide title and path]
├── scripts/
│   └── search.py                                           # [VERIFIED: Search CLI discoverability across all topics]
└── SKILL.md                                                # [UPDATED: Elevated hard negative constraints & nav link]
```

---

## 3. Work Breakdown Structure (Tickets)

| Ticket | Title | Target Scope | Blocked by |
|---|---|---|---|
| **01** | `01-domain-scope-and-preprocessor-standards` | Pillars 1 & 2: Domains, Variables, Scope, `#pragma used dll`, `#include`, `#define` | None |
| **02** | `02-function-contracts-and-buffer-collision-protection` | Pillars 3 & 4: Parameter contracts (`i./o./io.`, `const`, `ref`), Buffer collisions, SQL binding, DAL writes | Ticket 01 |
| **03** | `03-array-dimensions-and-fatal-runtime-caveats` | Pillars 5 & 6: 1-Based array dimensions, `double.cmp`, Transaction nesting, Reserved words, `selectempty`, `goto`, Lock scope | Ticket 02 |
| **04** | `04-skill-guardrails-elevation-and-cross-linking` | Elevate 6 rules into `SKILL.md` hard negative constraints; update `03` & `04` cookbooks | Ticket 03 |
| **05** | `05-catalog-indexing-and-search-verification` | Register in `INDEX.tsv`; verify CLI search queries and markdown link integrity | Ticket 04 |

---

## 4. Verification Seam

The primary verification seam is the CLI search engine and catalog integrity check:
- `python erp-ln-progguide/scripts/search.py <topic> --dir best_practices`
  - Verifying queries: `double.cmp`, `buffer collision`, `fixed array`, `#pragma used dll`, `selectempty`, `dal.change.object`.
- Master catalog check: Verify presence and matching title in `erp-ln-progguide/index/INDEX.tsv`.
- Markdown lint & link resolution: Verify zero broken internal hyperlinks.
