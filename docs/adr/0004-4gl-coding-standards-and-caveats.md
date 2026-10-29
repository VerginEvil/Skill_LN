# ADR 0004: Baan 4GL Coding Standards, Anti-Patterns & Runtime Caveats

- **Status**: Accepted
- **Date**: 2026-10-22
- **Specification**: [`docs/SPEC_4GL_CODING_STANDARDS_AND_CAVEATS.md`](../SPEC_4GL_CODING_STANDARDS_AND_CAVEATS.md)
- **Implementation Plan**: [`docs/PLAN_4GL_CODING_STANDARDS_AND_CAVEATS.md`](../PLAN_4GL_CODING_STANDARDS_AND_CAVEATS.md)
- **Target Skill**: `erp-ln-progguide`

## 1. Context & Problem Statement
When generating or refactoring Baan 4GL code for Infor ERP LN, developers and AI coding agents repeatedly hit 6 language-level anti-patterns and bshell runtime caveats:
1. Silent data truncation caused by primitive type declarations (`long`, `string`, `double`) instead of Data Dictionary Domains.
2. Linkage and macro errors from omitting `#pragma used dll "o..."`, mixing `#include <...>` with application includes, or clashing `#define` constants with reserved keywords.
3. Fragile function contracts lacking directional notation (`i.`, `o.`, `io.`), `const`, `ref`, and standardized status returns.
4. UI session table buffer collisions from running unconstrained `select table.*` queries inside loops and helper functions.
5. Array dimension violations from misunderstanding 1-based indexing or omitting `fixed`/`()` array parameter syntax.
6. Fatal runtime failures including direct floating-point `==` comparisons, nested `commit.transaction()` inside DAL hooks or subroutines, unhandled `selectempty`, `goto` spaghetti, and prolonged lock windows.

## 2. Decisions Recorded
1. **Dedicated Coding Standards & Caveats Guide**:
   Create `references/best_practices/06_4gl_coding_standards_and_caveats.md` in full technical English covering all 6 pillars with side-by-side Anti-Pattern (Don't) and Compliant Pattern (Do) code blocks using realistic enterprise ERP table domains (`tdsls400`, `tccom100`, etc.).
2. **Elevated Skill Guardrails**:
   Add hard negative constraints to `erp-ln-progguide/SKILL.md` under "Infor LN Coding Standards & Architectural Guardrails" prohibiting primitive table types, direct double equality, nested commits, `goto`, and raw database writes in UI scripts.
3. **Cross-Guide Navigation**:
   Update `03_sql_query_optimization_and_transactions.md` (cross-referencing record buffer collisions and lock windows) and `04_data_model_and_domain_design.md` (cross-referencing domain vs primitive types).
4. **Catalog Indexing & Search Seam**:
   Register the new guide in `erp-ln-progguide/index/INDEX.tsv` and verify discoverability via `erp-ln-progguide/scripts/search.py --dir best_practices`.

## 3. Consequences
- **Positive**: AI models and developers will receive concrete, actionable guardrails preventing fatal bshell memory and database crashes before code is deployed.
- **Positive**: Maintains full linguistic and structural consistency with official Infor documentation.
- **Neutral**: Adds 1 reference file to the documentation suite, requiring catalog index registration.
