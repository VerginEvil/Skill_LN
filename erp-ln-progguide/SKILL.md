---
name: erp-ln-progguide
description: Infor ERP LN / Baan 4GL programmer's reference and full-stack engineering guide. Use when writing, reading, or debugging Baan/LN 4GL (bshell) code, 4GL session scripts, DAL 1 & 2 scripts, AFS/function-server automation, report scripts, LN SQL queries, bshell built-in functions, predefined variables, debugger usage, resolving SQL error states (SQLSTATE), embedding GenAI assistance (genai.*, set.genai.*) in sessions, developing Infor LN extensions (Extension Modeler, CDFs, table/session/report/BOD/OData/menu/process extension points and hooks), calling LN public interface functions / process extensions (e.g. Address.Create, Item.GetData, tdext/whext/tiext DLLs), referencing Infor LN Development Tools (Data Dictionaries, domains, tables, crdd reconfiguration, MMT sessions, PMC, SCM), or applying Infor LN coding best practices and cloud governance rules.
---

# Infor ERP LN Programmer's Guide & Best Practices (Baan 4GL)

Full text of the official Infor *Programmer's Guide* (`progguide 2610 en`), its *SQL* volume, the *Infor LN Extensions Development Guide 10.8*, the *Infor LN Development Tools (2016)* manual, the *Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud)*, the *AFS Developer's Guide (Infor Integration 6.2)*, and the **Infor LN Best Practices & Cookbooks Suite**, converted to plain Markdown: **5,700+ pages**, including **2,425 bshell function references**, **1,833 public interface / process extension references**, all **`stpapi.*` AFS primitives**, 13 complete **Development Tools** chapters, and 5 prescriptive **Architectural Cookbooks**.

## How to answer questions (token-efficient workflow)

Never read folders blindly. Use this order:

1. **Known function name** -> grep `references/FUNCTION_INDEX.md` for the name.
   Each line has the normalized signature and the exact `.md` path. Then Read only that file.
2. **Best practices & architectural rules** -> check `references/best_practices/` first before generating or reviewing code.
3. **Free-text question** ("how to open a file", "utc conversion", "query hint", "before.save.object hook", "crdd reconfiguration", "MMT satellite") -> run:
   ```
   python <skill_dir>/scripts/search.py <terms> [--dir guide|sql|extensions|public_interfaces|afs|dev_tools|best_practices|all] [--group substr] [--regex PATTERN] [--max 25]
   python <skill_dir>/scripts/search.py --list-groups        # topic folders + page counts
   ```
   Output is `file:line: snippet` matches ranked by hits. Read only promising files.
4. **All pages** -> `index/INDEX.tsv` maps every page path to its title.
5. Links between pages are relative Markdown links and resolve correctly; follow them by Reading the target path next to the current file.

## Infor LN Coding Standards & Architectural Guardrails

When analyzing, designing, or generating Infor ERP LN code, AI agents and developers **must strictly adhere** to these architectural rules:

1. **Cardinal Rule — Separation of Concerns (SoC)**:
   - **Never perform database modifications (`db.insert`, `db.update`, `db.delete`, `db.write`) or business validations directly in 4GL UI session scripts (`type 1-4`, `choice.*`, `main.table.io`).**
   - UI scripts manage form presentation, dynamic views, and window titles only.
   - All data validations, defaults, calculated fields, and table mutations **must reside strictly in the Data Access Layer (DAL 2)** or **Table Extensions**.
   - *Reference*: [DAL Architecture & Business Logic Guide](references/best_practices/02_dal_architecture_and_business_logic.md).

2. **Extension Hooks & Standardized Error Conventions**:
   - Always signal business rule failures using `dal.set.error.message("@<msg_code>", [args...])` and `return(DALHOOKERROR)` (or `false` for boolean hooks).
   - **Never invoke interactive dialogs (`message()`, `ask.enum()`, `box()`) inside Table Extension hooks or DAL scripts**; doing so hangs headless cloud processes, BOD exchanges, and REST APIs.
   - Maintain the safe `table.super()` signature pattern with `get.long.arg(1)` for optional `mode` handling.
   - *Reference*: [Extension Hooks & Cloud Governance Cookbook](references/best_practices/01_extension_hooks_cookbook.md).

3. **Embedded Baan SQL & Index Alignment**:
   - Always verify that the query's `WHERE` clause specifies equality predicates on the **leading fields** of a defined table index (`_index1`, `_index2`...).
   - Never wrap indexed database columns inside expressions or functions (e.g. avoid `toupper(tdsls400.orno)`).
   - Use `as set with 1 rows` for single-record lookups and `as prepared set` when mutating records inside the loop.
   - Eliminate N+1 query anti-patterns by joining parent and child tables in a single SQL statement.
   - *Reference*: [SQL Query Optimization & Transactions Guide](references/best_practices/03_sql_query_optimization_and_transactions.md).

4. **Transaction Concurrency & Deadlock Prevention**:
   - Strictly bound all database modifications between `db.retry.point()` and `commit.transaction()` / `abort.transaction()`.
   - Minimize lock windows (`select ... for update`): compute complex logic before locking, and commit immediately after updating.
   - Always acquire locks in hierarchical order (Parent table before Child table).
   - *Reference*: [SQL Query Optimization & Transactions Guide](references/best_practices/03_sql_query_optimization_and_transactions.md).

5. **Data Dictionaries & Table Reconfiguration (`crdd`)**:
   - Distinguish design-time metadata (Application Data Dictionary in `ttadv*`) from compiled bshell binaries (Runtime Data Dictionary).
   - Follow the two-step `crdd` procedure (Convert to Runtime -> Reconfigure Tables) with exclusive table access to prevent catastrophic data loss.
   - *Reference*: [Data Model & Domain Design Guide](references/best_practices/04_data_model_and_domain_design.md).

6. **Cloud Extensibility Governance**:
   - Respect Cloud multi-tenant governor limits: max execution elapsed time = `5,000 ms`, max file output = `5 MB`.
   - Never call untrusted bshell functions (`run.prog()`, `hostname$()`) or manipulate files outside sandboxed tenant storage.
   - *Reference*: [Extension Hooks & Cloud Governance Cookbook](references/best_practices/01_extension_hooks_cookbook.md).

### Mandatory Negative Constraints & Defensive Rules (Strictly Prohibited Anti-Patterns)

During code generation, refactoring, and code review, AI agents and engineers **must proactively reject and prevent** the following anti-patterns:
- **No Primitive Database Types**: Never declare database-bound variables, parameters, or entity keys using raw primitives (`long`, `double`, `string`). Always declare variables using centralized Data Dictionary `domain <name> <var>` (e.g. `domain tcorno orno`) to eliminate silent data truncation when field sizes expand.
- **No Direct Floating-Point Equality**: Never compare float or domain amount variables using `==` or `!=`. Always use `double.cmp(val1, val2, epsilon) = 0` (e.g. `C_AMOUNT_EPSILON = 0.0001`) to prevent representation rounding failures.
- **No Nested Transaction Commits in Hooks or DLLs**: Never call `commit.transaction()`, `db.retry.point()`, or `abort.transaction()` inside DAL hooks (`before.save.object`), Table Extensions, or reusable helper DLL subroutines. Transactions must be orchestrated exclusively at outer orchestration boundaries (`choice.update.db`, batch schedulers, integration APIs).
- **No Unstructured Branching (`goto`)**: Never use `goto` jumps. Use structured control flow (`if/else`, `break`, `continue`, early `return`).
- **No Raw Database Updates in UI or Helper Scripts**: Never invoke `db.insert`, `db.update`, or `db.delete` directly in UI session scripts or helper functions. Always delegate mutations to DAL 2 (`dal.change.object()`, `dal.set.field()`, `dal.save.object()`).
- **No Unhandled Query Empty States**: Never write single-record `select` queries without a `selectempty` fallback block. Variables must be deterministically initialized or errors returned.
- **No Table Record Buffer Overwrites**: Never perform `select table.*` in helper functions or loops that share table declarations with active UI forms. Always bind queried columns directly to local host variables (`table.field:l.var`) or query via Table Aliases.
- **No 0-Based Array Access**: Never access array index `0` or iterate from `0 to N-1`. 4GL arrays are strictly 1-based (`1..N`).
- *Authoritative Reference*: [Baan 4GL Coding Standards, Anti-Patterns & Runtime Caveats Guide](references/best_practices/06_4gl_coding_standards_and_caveats.md).

---

## Layout

```
references/
  best_practices/             Prescriptive architectural guides & cookbooks:
    01_extension_hooks_cookbook.md               Table/session hook lifecycles, CDF recipes, cloud governance
    02_dal_architecture_and_business_logic.md   DAL 1 vs 2, SoC rules, property hooks, business methods
    03_sql_query_optimization_and_transactions.md Baan SQL, index matching, array fetch, retry points
    04_data_model_and_domain_design.md          Domain types, table references, crdd reconfiguration
    05_session_and_mmt_patterns.md              Session types 1-4, MMT Controller/Satellite, labels
    06_4gl_coding_standards_and_caveats.md       Domains vs primitives, buffer collision, double.cmp, 1-based arrays
  dev_tools/                  Infor LN Development Tools (2016), 13 complete chapters:
    ch01_development_tools_introduction.md
    ch02_overview_of_software_components.md
    ch03_data_dictionaries.md
    ch04_development_parameters_and_authorizations.md
    ch05_software_development_procedures.md
    ch06_session_personalizations.md
    ch07_version_and_release_management.md
    ch08_ln_software_maintenance.md
    ch09_ln_homepages.md
    ch10_ln_reporting_overview.md
    ch11_4gl_reports.md
    ch12_session_based_reporting.md
    ch13_query_based_reporting.md
  guide/progguide/            main guide, mirrored from original TOC (LN 2610)
    3gl_features/             data types, variables, expressions, multibyte/UTC
    4gl_features/             4GL sections: program/form/group/field/choice/event/
                              zoom, main.table.io subsections, flow of standard program
    bol/                      Business Object Layer programming
    functions_<topic>/        ~130 function groups; each has overview.md,
                              synopsis.md (all signatures), one page per function
    functions_genai/          Native GenAI 4GL APIs (genai.processing.*, session.set.genai.*)
    multitasking/ events/     process model, event handling
    debugger/ profiler/       baan debugger commands, call graph profiler
    misc/                     bshell options/env vars/resources, predefined vars
    errors/                   Infor ES error messages
  sql/progguide/              Baan SQL reference & SQLSTATE error codes
  extensions/                 Infor LN Extensions Development Guide (10.8)
  public_interfaces/          LN Cloud Public Interfaces & Process Extensions reference (25082026)
  afs/                        AFS Developer's Guide (stpapi.* primitives)
index/INDEX.tsv               every page: path TAB title
references/DEV_TOOLS_INDEX.md master chapter and topic index for Development Tools
references/FUNCTION_INDEX.md  all 2425 functions grouped by topic, grep this first
references/EXTENSIONS_INDEX.md chapter list + orientation for the extensions guide
references/PUBLIC_INTERFACES_INDEX.md  index of all public interfaces per chapter
references/AFS_INDEX.md       stpapi.* primitive list with signatures
scripts/search.py             full-text search tool (stdlib Python only)
```

## Common tasks

| Task | Start at |
|---|---|
| **Extension Hooks Cookbook & Recipes** | `references/best_practices/01_extension_hooks_cookbook.md` |
| **DAL 1 vs DAL 2 & SoC Rules** | `references/best_practices/02_dal_architecture_and_business_logic.md` |
| **Baan SQL Optimization & Transactions** | `references/best_practices/03_sql_query_optimization_and_transactions.md` |
| **Domain Design, Tables & `crdd`** | `references/best_practices/04_data_model_and_domain_design.md` |
| **Session Types 1-4 & MMT Patterns** | `references/best_practices/05_session_and_mmt_patterns.md` |
| **4GL Coding Standards & Runtime Caveats** | `references/best_practices/06_4gl_coding_standards_and_caveats.md` |
| **Infor LN Development Tools Master Index** | `references/DEV_TOOLS_INDEX.md` |
| **Software Components Overview** | `references/dev_tools/ch02_overview_of_software_components.md` |
| **Development Procedures (Data model, forms, MMT)** | `references/dev_tools/ch05_software_development_procedures.md` |
| **Data Dictionaries (Runtime vs Application)** | `references/dev_tools/ch03_data_dictionaries.md` |
| **Version & Release Management (VRC, SCM)** | `references/dev_tools/ch07_version_and_release_management.md` |
| **PMC Maintenance (Solutions, Patches, FPs)** | `references/dev_tools/ch08_ln_software_maintenance.md` |
| Signature/usage of any bshell function | `references/FUNCTION_INDEX.md` |
| GenAI assistance in a session (LN 2610) | `guide/progguide/functions_genai/overview_and_synopsis.md`, then `genai.processing.start.md` |
| Baan SQL subquery syntax (renamed from `sub_query`) | `sql/progguide/functions_database_handling/subquery.md` |
| Baan SQL syntax (SELECT, clauses, joins) | `sql/progguide/functions_database_handling/select_statement.md` |
| Decode SQLSTATE error | `sql/progguide/sql_states_and_messages/<code>.md` |
| Add a hook to a standard table/session | `references/extensions/table_extension_point.md`, `extensions/session_extension_point.md` |
| CDF types, config, limitations | `references/extensions/customer_defined_fields.md` |
| Cloud restrictions / governors / best practices | `references/extensions/governance.md` |
| Find a public interface by name (e.g. Item.GetData) | `references/PUBLIC_INTERFACES_INDEX.md`, then `public_interfaces/chNN_*/<Name>.md` |
| stpapi.* primitive syntax/usage (AFS) | `references/AFS_INDEX.md`, then `references/afs/ch03_baan_4gl_engine_primitives.md` |

## Notes

- Sources: Infor progguide 2610 (en) + Infor LN Development Tools (2016) + Infor LN Extensions Development Guide 10.8 (01062026) + Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud) (25082026) + Infor Integration 6.2 AFS Developer's Guide (U8627B US).
- All files UTF-8 Markdown; code examples fenced; tables preserved.
- `search.py` needs only Python 3 stdlib; safe on Windows/Linux/macOS.
