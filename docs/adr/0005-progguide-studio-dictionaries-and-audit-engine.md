# ADR 0005: LN Studio Build 0640 Dictionaries Extraction, Cloud Governance & Standalone 4GL Audit Engine

- **Status**: Accepted
- **Date**: 2026-10-26
- **Target Skill**: `erp-ln-progguide` (with synchronized static rule alignment in `ln_studio_skill`)
- **Specification**: [`docs/SPEC_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md`](../SPEC_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md)
- **Implementation Plan**: [`docs/PLAN_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md`](../PLAN_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md)
- **Work Roster**: [`Tickets.md`](../../Tickets.md) (Tickets 01 through 06)
- **Prior ADRs**:
  - [`docs/adr/0001-plan-skill-update-and-coding-best-practices.md`](0001-plan-skill-update-and-coding-best-practices.md)
  - [`docs/adr/0002-ln-studio-skill-self-contained-toolchain.md`](0002-ln-studio-skill-self-contained-toolchain.md)
  - [`docs/adr/0003-ln-studio-object-modeling-and-static-verification.md`](0003-ln-studio-object-modeling-and-static-verification.md)
  - [`docs/adr/0004-4gl-coding-standards-and-caveats.md`](0004-4gl-coding-standards-and-caveats.md)

---

## 1. Context & Motivation

Infor LN Studio 10.8 build 0640 (April 2026 distribution, located at `d:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64`) contains rich internal metadata, OSGi bundles, and eclipse plugins defining the exact syntax, code completion, DAL hooks, and function catalogs for Infor LN development.

However, the primary knowledge skill `erp-ln-progguide` suffered from critical gaps:
1. **Unenriched Function Index**: `erp-ln-progguide/references/FUNCTION_INDEX.md` indexed 2,425 functions but lacked critical Cloud Governance indicators (`Trusted="yes|no"`), deprecation status (`Deprecated="yes|no"`), script scope restrictions (`ScriptType="DAL"|"4GL"|"UEDLL"|"all"`), and required include headers (`include="bic_dal"`, `bic_json`, `bic_curl`, etc.).
2. **Absence of Machine-Readable Function Catalog**: Agents had to grep markdown pages or parse raw HTML, leading to missed include headers and runtime bshell compilation failures.
3. **No Standalone 4GL/DAL Code Auditor**: Unlike `ln_studio_skill` which had an activity-level validator, `erp-ln-progguide` had no offline verification script. Developers and agents writing 4GL or DAL2 code outside an Eclipse activity had no way to statically check their code against LN Studio syntax rules, DAL hook contracts, CloudSuite Multi-Tenant restrictions, or best practices.
4. **Lack of Prepared Assets for Future Tooling**: Developers building external tooling (such as VS Code extensions for Baan 4GL syntax highlighting and code completion) lacked pre-extracted, ready-to-use TextMate grammars and snippet packages.

---

## 2. Decisions Recorded

### 2.1 Extraction Scope from LN Studio Build 0640
Extract three tiers of authoritative metadata directly from the pinned Studio installation into `erp-ln-progguide`:
1. **Authoritative Function Catalog**: Parse `com.infor.ln.studio.apps.progguide_10.8.0.0614/help/index/functionlist.xml` (2,274 functions) into `erp-ln-progguide/index/functions_db.json` capturing:
   - `name`, `syntax`, `return_type`, `parameters`
   - `trusted` (Cloud Multi-Tenant certified)
   - `deprecated` (Obsolete or superseded functions)
   - `script_type` (`all`, `DAL`, `4GL`, `UEDLL`, `3GL`, `SPT`)
   - `include` (Mandatory header file, e.g. `bic_dam`, `bic_json`, `bic_curl`, `bic_dal`)
   - `help_id` and relative markdown documentation path.
2. **Syntax, Keywords & DAL Completion Dictionaries**: Extract from `lnstudio_commonui.jar` into `erp-ln-progguide/references/studio_syntax_completion.json`:
   - 80 4GL reserved keywords (`IScriptEditorKeywords`)
   - 92 Embedded SQL keywords (`IScriptEditorSQLKeywords`)
   - 9 Program sections, 43 Subsections, 60 Choice sections, 9 Report sections
   - 176 Predefined variables and 49 Standard defines
   - 15 DAL Object Hooks (`CodeCompletion.DAL_OBJECT_HOOKS`)
   - 10 DAL Field Hook Suffixes (`CodeCompletion.DAL_FIELD_HOOK_SUFFIXES`) with parameter and return signatures.
3. **Official Script & Code Templates**: Extract from `com.infor.ln.studio.common.core_*.jar` (`ScriptTemplates/`) and `DefaultFourglTemplates.xml` into `erp-ln-progguide/templates/`.

### 2.2 Enriched `FUNCTION_INDEX.md`
Rebuild `erp-ln-progguide/references/FUNCTION_INDEX.md` into a single-line, grep-friendly format displaying governance badges:
```markdown
- **<func_name>** | `[Cloud: Trusted|Untrusted]` `[Deprecated]` `[Scope: <script_type>]` `[Inc: <header>]` | `<signature>` -> `<relative_md_link>`
```
This enables instantaneous static verification during AI grep passes without reading full files.

### 2.3 Standalone 4GL & DAL Audit Engine (`scripts/audit_4gl.py`)
Create a fast, standalone Python CLI audit tool in `erp-ln-progguide/scripts/audit_4gl.py` supporting:
- **Block & Syntax Integrity**: Balance of `select/endselect`, `if/endif`, `on case/endcase`, `for/endfor`, `while/endwhile`, `repeat/until`, `#context_on/#context_off`, `{}`.
- **DAL2 Contract Enforcement**:
  - Validates method suffixes (`.is.applicable`, `.is.readonly`, `.update`, `.check`, etc.).
  - Enforces required argument signatures (`long i.mode` for `.update`, `long has_changed` for `.check`).
  - Prohibits interactive UI dialogs (`message()`, `ask.enum()`, `box()`) inside DAL hooks and table extensions.
- **Cloud Multi-Tenant Governance (`--cloud`)**: Flags all calls to `trusted="no"` bshell functions and deprecated APIs.
- **Mandatory Include Verifier**: Flags calls to library functions missing their required `#include <...>` headers (e.g. `json.*` without `#include <bic_json>`).
- **Best-Practice Anti-Pattern Detection**: Flags direct floating-point `==` comparisons, unconstrained buffer mutations, and primitive variable declarations where table domains are required.
- **Output Formats**: Colored ANSI console output for human developers and `--format json` for automated pipelines/diagnostics.

### 2.4 Synchronized Rule Alignment with `ln_studio_skill`
Update `ln_studio_skill/tools/check_4gl_script.py` to ingest the updated dictionaries and rule definitions, ensuring both skills enforce 100% identical Layer 4 static verification standards.

### 2.5 VS Code Extension Assets Preparation (`export/vscode/`)
Generate modular, decoupled VS Code extension assets ready for future packaging:
- `export/vscode/syntaxes/baan4gl.tmLanguage.json`: Complete TextMate syntax highlighting grammar.
- `export/vscode/snippets/baan4gl.code-snippets`: Rich code snippets for 4GL constructs, DAL2 hooks, and SQL statements.
- `export/vscode/language-configuration.json`: Comment syntax (`|`), brackets, auto-closing quotes.
- `export/vscode/completions.json`: Structured completions and parameter hints dataset.
*Note: Development, testing, and packaging of the actual VS Code extension itself is strictly excluded from this batch and will be tackled in a future project.*

---

## 3. Consequences

### Positive
- `erp-ln-progguide` transitions from a passive documentation repository into an active, verifiable development and auditing platform.
- AI agents and developers gain instant visibility into Cloud Multi-Tenant compatibility and required includes before writing or compiling code.
- Zero-dependency offline auditing (`audit_4gl.py`) runs in milliseconds without requiring an Eclipse runtime or live bshell connection.
- Ready-to-use VS Code extension assets eliminate future redundant extraction work.

### Neutral
- Adds maintenance of `functions_db.json` and `scripts/audit_4gl.py` to `erp-ln-progguide`.
- `FUNCTION_INDEX.md` line lengths increase due to metadata badges, but remain strictly single-line for grep friendliness.
