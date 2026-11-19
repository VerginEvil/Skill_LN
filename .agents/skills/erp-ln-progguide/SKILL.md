---
name: erp-ln-progguide
description: Infor ERP LN / Baan 4GL programmer's reference, architectural cookbooks, and static 4GL auditor (`skill-ln audit-4gl`). Trigger when writing, debugging, or auditing Baan/LN 4GL code, DAL 1 & 2 hooks, Extension Modeler scripts, Baan SQL queries, or bshell runtime APIs. Route LN Studio workspaces, SCM check-out/check-in, XML generation, and deploy-test to `ln_studio_skill`.
---

# Infor ERP LN Programmer's Guide & Best Practices (Baan 4GL)

Authoritative reference for Infor ERP LN / Baan 4GL, DAL 1 & 2, Extension Modeler, embedded Baan SQL, bshell runtime APIs, and offline code auditing.

## Procedural Workflow

### 1. `Search-Before-Read` (Information Retrieval)
Locate authoritative facts before reading full reference files:
- **Known bshell API**: Run `skill-ln fn-search "<term>"` or grep `references/FUNCTION_INDEX.md` / `index/functions_db.json`.
- **Free-text / Topic Search**: Run `skill-ln doc-search "<terms>"` to search 5,700+ pages ranked by relevance.
- **Syntax & Completion Dictionaries**: Inspect `references/STUDIO_SYNTAX_COMPLETION.md` for keywords, sections, and hook signatures.

### 2. `Branching Reference Pointers`
Open dedicated cookbooks and domain indices on demand based on task branch:

| Task Branch | Authoritative Reference |
|---|---|
| **Extension Modeler & CDFs** | [Extension Hooks Cookbook](references/best_practices/01_extension_hooks_cookbook.md) & [Extensions Index](references/EXTENSIONS_INDEX.md) |
| **DAL 1 vs DAL 2 & SoC** | [DAL Architecture Guide](references/best_practices/02_dal_architecture_and_business_logic.md) |
| **Baan SQL & Transactions** | [SQL Optimization & Transactions](references/best_practices/03_sql_query_optimization_and_transactions.md) |
| **Domain Design, Tables & `crdd`** | [Data Model & Domain Design](references/best_practices/04_data_model_and_domain_design.md) |
| **Sessions, Forms & MMT** | [Session & MMT Patterns](references/best_practices/05_session_and_mmt_patterns.md) |
| **4GL Standards & Caveats** | [4GL Coding Standards & Caveats](references/best_practices/06_4gl_coding_standards_and_caveats.md) |
| **Development Tools Manual** | [Dev Tools Master Index](references/DEV_TOOLS_INDEX.md) |
| **Public Interfaces & DLLs** | [Public Interfaces Index](references/PUBLIC_INTERFACES_INDEX.md) |
| **AFS Automation (`stpapi.*`)** | [AFS Primitives Index](references/AFS_INDEX.md) |
| **Official Studio Templates** | `templates/` (`DalTwo.dal`, `UIDatabase.cln`, `UserExitDLL.ue`) |

### 3. `Core 4GL & Cloud Guardrails`
Every generated or reviewed script must satisfy these 7 rules:
1. **Separation of Concerns (SoC)**: Keep table mutations and data validation in DAL 2 or Table Extensions rather than UI scripts (`type 1-4`, `choice.*`) ([02_dal](references/best_practices/02_dal_architecture_and_business_logic.md)).
2. **Error Conventions & Silent Hooks**: Signal failures via `dal.set.error.message("@<code>")` and `return(DALHOOKERROR)`; keep DAL and Table Extensions free of interactive dialogs (`message()`, `ask.enum()`) ([01_ext](references/best_practices/01_extension_hooks_cookbook.md)).
3. **Embedded SQL Leading Index & Scalar Staging**: Match WHERE predicates to leading index columns, stage array elements into scalar host variables (`SQL008`), and provide `selectempty` blocks ([03_sql](references/best_practices/03_sql_query_optimization_and_transactions.md)).
4. **Transaction Bounds**: Bound mutations inside top-level `db.retry.point()` and `commit.transaction()` while keeping DAL hooks, Table Extensions, and helper DLLs commit-free ([03_sql](references/best_practices/03_sql_query_optimization_and_transactions.md)).
5. **Defensive Declarations & Datatypes**: Use Data Dictionary domains, 2D syntax `string arr(len, count)` (`ARR002`), 1-based array indexing, Julian date vs UTC epoch handling (`DMN002`), and non-zero line guards (`TBL003`) ([06_std](references/best_practices/06_4gl_coding_standards_and_caveats.md)).
6. **Cloud Governance & Extension Rules**: Stay within `5,000 ms` execution limits, verify Cloud Trust badges, preserve standard non-context boilerplate (`EXT003`), place custom `#include` inside `#context_on "declarations"` (`EXT001`), and keep command hooks `void` ([01_ext](references/best_practices/01_extension_hooks_cookbook.md)).
7. **Table Extension Runtime Mode & Old-Value Safety**: Handle Runtime Layer negative modes (`-DAL_NEW`, `-DAL_UPDATE`) alongside `DAL_NEW`/`DAL_UPDATE` in `before.save.object`/`after.save.object`; read `get.long.arg(1)` before `table.super()`; capture pre-save DB values via an isolated alias in `before.save.object()` rather than `with.old.object.values.do()` in `after.save.object()` (`EXT004`/`DAL006`, [01_ext](references/best_practices/01_extension_hooks_cookbook.md)).

### 4. `Audit-Before-Deliver` (Static Verification Gate)
Before delivering any 4GL, DAL 2, or Extension script, audit offline (pass `--dd-cache` or `--dd-dir "Table Definitions"` for schema/double/index checks, or pre-build cache via `skill-ln import-dd-txt`):
```bash
skill-ln audit-4gl <target_script> [--mode auto|general|dal2|uedll] [--cloud] [--dd-dir <dir>]
```
Done when `audit-4gl` exits with **0 errors** across syntax (`SYN`), DAL (`DAL001-DAL007`), Extension (`EXT001-EXT004`), datatype/export (`DMN001-DMN004`/`TBL`/`STR001-STR002`), caveats (`CAV001-CAV004`), SQL (`SQL008-SQL011`), and Cloud (`CLD`) checks. (Standard UI `.cln` scripts without `#context_on` audit cleanly under `--mode general`.)
