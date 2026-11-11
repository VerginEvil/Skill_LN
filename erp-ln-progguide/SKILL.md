---
name: erp-ln-progguide
description: Authoritative Infor ERP LN / Baan 4GL programmer's reference, architectural cookbooks, and static 4GL code auditor. Use when writing, debugging, or reviewing Baan/LN 4GL code, DAL 1 & 2 logic, Extension Modeler hooks (table, session), Baan SQL queries, bshell runtime APIs, or running offline 4GL code audits via scripts/audit_4gl.py. Do NOT use for LN Studio workspace management, SCM check-out/check-in, declarative component XML generation, or deploy-test (use ln_studio_skill instead).
---

# Infor ERP LN Programmer's Guide & Best Practices (Baan 4GL)

Authoritative reference for Infor ERP LN / Baan 4GL, DAL 1 & 2, Extension Modeler, embedded Baan SQL, bshell runtime APIs, and offline code auditing.

## Procedural Workflow

### 1. `Search-Before-Read` (Information Retrieval)
Never scan reference folders blindly. Locate authoritative facts in this sequence:
- **Known bshell API**: Grep `references/FUNCTION_INDEX.md` (single-line index with Cloud Trust indicators and `#include` headers) or inspect `index/functions_db.json`.
- **Free-text / Topic Search**: Run `python scripts/search.py "<terms>"` to search 5,700+ pages ranked by relevance.
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
Every generated or reviewed script must comply with these 6 non-negotiable rules:
1. **Separation of Concerns (SoC)**: Never modify tables or validate data in UI scripts (`type 1-4`, `choice.*`); all mutations belong in DAL 2 or Table Extensions ([02_dal](references/best_practices/02_dal_architecture_and_business_logic.md)).
2. **Error Conventions & No Dialogs**: Signal failures via `dal.set.error.message("@<code>")` and `return(DALHOOKERROR)`. Never call interactive dialogs (`message()`, `ask.enum()`) in DAL or Table Extensions ([01_ext](references/best_practices/01_extension_hooks_cookbook.md)).
3. **Embedded SQL Leading Index & Scalar Staging**: Match WHERE predicates to leading index columns; stage array elements into scalar host variables (SQL008); provide selectempty fallback blocks ([03_sql](references/best_practices/03_sql_query_optimization_and_transactions.md)).
4. **Transaction Bounds**: Bound mutations strictly inside `db.retry.point()` and `commit.transaction()`; never commit transactions inside DAL hooks, Table Extensions, or helper DLLs ([03_sql](references/best_practices/03_sql_query_optimization_and_transactions.md)).
5. **Defensive Declarations & Datatypes**: Use Data Dictionary domains; string arrays require 2D syntax string arr(len, count) (ARR002); 4GL arrays are 1-based; respect Julian date vs UTC epoch seconds (DMN002); avoid mandatory zero constraints on lines (TBL003) ([06_std](references/best_practices/06_4gl_coding_standards_and_caveats.md)).
6. **Cloud Governance & Extension Rules**: Comply with execution time limits (`5,000 ms`); verify Cloud Trust badges; preserve standard non-context boilerplate (`EXT003`); place custom `#include` inside `#context_on "declarations"` (`EXT001`); keep command hooks `void` ([01_ext](references/best_practices/01_extension_hooks_cookbook.md)).

### 4. `Audit-Before-Deliver` (Static Verification Gate)
Before returning or presenting any 4GL, DAL 2, or Extension script, run the offline auditor:
```bash
python scripts/audit_4gl.py <target_script> [--mode dal2|uedll|general] [--cloud]
```
Resolve all syntax errors (SYN), DAL violations (DAL), Extension boundary bugs (EXT), datatype mismatches (DMN/TBL/STR), and Cloud governance warnings (CLD) until 0 errors remain.
