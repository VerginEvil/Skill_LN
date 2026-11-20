# Baan 4GL Coding Standards, Anti-Patterns & Runtime Caveats (Router Hub)

> **Reference Documents**: [Dev Tools Chapter 2](../dev_tools/ch02_overview_of_software_components.md) | [Dev Tools Chapter 3](../dev_tools/ch03_data_dictionaries.md) | [Dev Tools Chapter 5](../dev_tools/ch05_software_development_procedures.md) | [SQL Query Optimization](03_sql_query_optimization_and_transactions.md) | [Data Model & Domain Design](04_data_model_and_domain_design.md)  
> **Scope**: Language-level 4GL fundamentals, buffer protection, array mechanics, and bshell runtime caveats for LN Cloud and On-Premises environments.

Open **only** the pillar matching your task:

| Pillar File | Scope | Open When... |
|---|---|---|
| [06a_declarations_and_functions.md](06a_declarations_and_functions.md) | **Overview & Pillars 1–3**: Domains, List/Set enums, `extern` scope, `#pragma used dll "o..."`, `#include` `<...>` vs `"..."`, macros, `i.`/`o.`/`io.`, `const`/`ref`, `0`/`< 0` return codes | Declaring variables/domains, linking DLLs, writing macros, or designing function signatures |
| [06b_sql_buffer_protection.md](06b_sql_buffer_protection.md) | **Pillar 4**: Table buffer overwrite risk, `:l.var` binding, table aliases, `as set with 1 rows`, explicit predicates, DAL delegation, `SQL008` scalar staging | Writing Embedded Baan SQL (`select`), fixing UI form buffer corruption, or refactoring `db.*` writes |
| [06c_arrays_and_dimensions.md](06c_arrays_and_dimensions.md) | **Pillar 5**: 1-based array indexing, 1D numeric/enum vs 2D `string arr(len, count)` (`ARR002`), passing `()` and `fixed` array parameters | Declaring string/domain arrays, fixing subscript errors, or passing arrays between 4GL functions |
| [06d_syntax_caveats_and_runtime_guards.md](06d_syntax_caveats_and_runtime_guards.md) | **Pillars 6–7 & Checklist**: `double.cmp` (`CAV004`), outer-boundary commits, reserved keywords, `selectempty`, no `goto`, row locks, ADR 0017 guards (`DMN002`/`003`/`004`, `TBL003`, `STR001`/`002`, `DBG001`, `DAL007`) | Debugging Error 205/dates/enums/doubles, locking & rollbacks, UTF-8/SSO strings, or final review |

## Quick Cross-Pillar Rules

- **Bind every variable to a Data Dictionary `domain`** and keep scratch variables local to functions (`06a`).
- **Never `select table.*` inside helpers** or put array subscripts `:arr(i)` in SQL; bind `:l.var` scalars (`06b`).
- **Always 1-based index (`1..N`)** and declare string arrays as 2D `string arr(len, count)` (`06c`).
- **Never compare doubles with `==` or assign `utc.num()` to `Date 4`**; use `double.cmp()` and `date.num()` (`06d`).
