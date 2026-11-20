---
name: erp-ln-progguide
description: Infor ERP LN / Baan 4GL coding guide, bshell API search, and static auditor (`skill-ln audit-4gl`). Use when writing, debugging, or auditing 4GL, DAL 1/2, Baan SQL, or Extension Modeler code. Route Studio workspaces, SCM, XML generation, and deploy-test to `ln_studio_skill`.
---

# Infor ERP LN Programmer's Guide & Best Practices (Baan 4GL)

Authoritative guide for Infor ERP LN / Baan 4GL, DAL 1 & 2, Extension Modeler, Baan SQL, bshell APIs, and offline auditing.

## Decision Tree

- **API or syntax lookup** -> Step 1 (`Search-Before-Read`: `skill-ln fn-search` / `doc-search`).
- **Authoring or reviewing code** -> Step 2 (open only the matching Cookbook / Hub branch).
- **Modifying a script in an activity** -> Step 3 (apply Core 4GL guardrails + SPS `.sn`/`.en` comments).
- **Ready to deliver or commit** -> Step 4 (`Audit-Before-Deliver` via `skill-ln audit-4gl`, exit `0`).

## 1. `Search-Before-Read`

Locate facts via CLI search before opening large reference trees:
- **bshell API / Topic Search**: Run `skill-ln fn-search "<term>"` or `skill-ln doc-search "<terms>"`.
- **Syntax & Hooks**: Inspect `references/STUDIO_SYNTAX_COMPLETION.md` for keywords, sections, and hook signatures.
- **Large Index Files**: Grep `references/FUNCTION_INDEX.md`, `references/PUBLIC_INTERFACES_INDEX.md`, or `index/functions_db.json` by symbol—always search selectively rather than reading multi-thousand-line index files whole.

## 2. `Branching Reference Pointers`

| Task Branch | Authoritative Reference |
|---|---|
| **Extension Modeler & CDFs** | [Extension Hooks Cookbook](references/best_practices/01_extension_hooks_cookbook.md) & [Extensions Index](references/EXTENSIONS_INDEX.md) |
| **DAL 1 vs DAL 2 & SoC** | [DAL Architecture Guide](references/best_practices/02_dal_architecture_and_business_logic.md) |
| **Baan SQL & Transactions** | [SQL Optimization & Transactions](references/best_practices/03_sql_query_optimization_and_transactions.md) |
| **Domain Design, Tables & `crdd`** | [Data Model & Domain Design](references/best_practices/04_data_model_and_domain_design.md) |
| **Sessions, Forms & MMT** | [Session & MMT Patterns](references/best_practices/05_session_and_mmt_patterns.md) |
| **4GL Standards & Caveats (Hub + Pillars `06a`–`06d`)** | [4GL Coding Standards Hub](references/best_practices/06_4gl_coding_standards_and_caveats.md) |
| **Development Tools / Public Interfaces / AFS** | [Dev Tools](references/DEV_TOOLS_INDEX.md), [Public Interfaces](references/PUBLIC_INTERFACES_INDEX.md), [AFS](references/AFS_INDEX.md) |
| **Official Studio Templates** | `templates/` (`DalTwo.dal`, `UIDatabase.cln`, `UserExitDLL.ue`) |

## 3. Core 4GL, SPS & Cloud Guardrails

1. **Separation of Concerns (SoC)**: Keep table mutations and validations in DAL 2 or Table Extensions; keep UI scripts (`type 1-4`, `choice.*`) presentation-only ([02_dal](references/best_practices/02_dal_architecture_and_business_logic.md)).
2. **Error Conventions & Silent Hooks**: Report errors via `dal.set.error.message("@<code>")` and `return(DALHOOKERROR)`; keep DAL and Table Extensions free of UI dialogs (`message()`, `ask.enum()`) ([01_ext](references/best_practices/01_extension_hooks_cookbook.md)).
3. **Embedded SQL Leading Index & Scalar Staging**: Align `WHERE` predicates with leading index fields, stage array elements into scalar host variables (`SQL008`), and include `selectempty` branches ([03_sql](references/best_practices/03_sql_query_optimization_and_transactions.md)).
4. **Transaction Bounds**: Wrap mutations in top-level `db.retry.point()` / `commit.transaction()` (Session Extensions coordinating DAL 2 calls may manage transactions); keep DAL hooks, Table Extensions, and helper DLLs commit-free ([03_sql](references/best_practices/03_sql_query_optimization_and_transactions.md)).
5. **Defensive Declarations & Datatypes**: Use Data Dictionary domains, 2D syntax `string arr(len, count)` (`ARR002`), 1-based indexing, separate Julian days vs UTC epochs (`DMN002`), and non-zero line guards (`TBL003`) ([06_hub](references/best_practices/06_4gl_coding_standards_and_caveats.md)).
6. **Cloud Governance & Extension Rules**: Stay within `5,000 ms`, use Cloud-Trusted APIs, leave non-context boilerplate untouched (`EXT003`), put custom `#include` inside `#context_on "declarations"` (`EXT001`), and keep command execution hooks `void` with bare `return` ([01_ext](references/best_practices/01_extension_hooks_cookbook.md)).
7. **Table Extension Save Modes & Old Values**: Handle `-DAL_NEW`/`-DAL_UPDATE` alongside `DAL_NEW`/`DAL_UPDATE`, read `get.long.arg(1)` before `table.super()`, and capture pre-save rows via an isolated alias in `before.save.object()` instead of `with.old.object.values.do()` in `after.save.object()` (`EXT004`/`DAL006`).
8. **SPS Maintenance Comments**: Wrap modified or inserted blocks with `|#<activity_name>.sn` ... `|#<activity_name>.en`, and wrap commented-out obsolete code with `|#<activity_name>.so` ... `|#<activity_name>.eo`.

## 4. `Audit-Before-Deliver` Completion Gate

Pass `--dd-cache` or `--dd-dir "Table Definitions"` for schema/index checks (or pre-build via `skill-ln import-dd-txt`):
```bash
skill-ln audit-4gl <target_script> [--mode auto|general|dal2|uedll] [--cloud] [--dd-dir <dir>]
```
Done when `audit-4gl` exits `0` with **0 errors** across `SYN`, `DAL001-DAL007`, `EXT001-EXT004`, `DMN001-DMN004`/`TBL`/`STR001-STR002`, `CAV001-CAV004`, `SQL008-SQL011`, and `CLD` checks.
