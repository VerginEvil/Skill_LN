# ADR 0017: Runtime Error Prevention, Audit Guardrails, and Skill Hardening

- **Status**: Proposed (Under Grilling Review)
- **Date**: 2026-11-06
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`
- **Specification**: [`.scratch/billing-integration-retro-and-audit-hardening/spec.md`](../../.scratch/billing-integration-retro-and-audit-hardening/spec.md)
- **Prior ADRs**:
  - [`docs/adr/0005-progguide-studio-dictionaries-and-audit-engine.md`](0005-progguide-studio-dictionaries-and-audit-engine.md) *(Audit engine architecture)*
  - [`docs/adr/0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md`](0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md) *(Data Dictionary Cache & AST rules)*
  - [`docs/adr/0013-extension-modeler-auditor-and-hook-hardening.md`](0013-extension-modeler-auditor-and-hook-hardening.md) *(Extension Modeler rules EXT001 & EXT002)*
  - [`docs/adr/0014-quality-hardening-ci-guardrails-and-mcp-execution-parity.md`](0014-quality-hardening-ci-guardrails-and-mcp-execution-parity.md) *(Unified checks script & CI)*

---

## 1. Context & Retrospective Findings

During the real-world deployment of the Billing System Integration (SCS-CR034 / DV2600401) on Infor LN Cloud Multi-Tenant (Company 800), multiple high-severity issues caused production fatal crashes and logical inversions that escaped existing static audit checks and schema generation tools:

1. **Fatal Error 205 (Value is out of range) via Julian Date vs UTC Epoch Mismatch**:
   - Infor LN standard date domains (e.g., `tfgld.date`, `tcdate`, `Date 4`) represent a **Julian Day integer** (days since 01/01/0001, e.g. ~739,925 for Nov 2026).
   - In `Sessions/txcmg0110m100.cln`, the developer/agent introduced a helper `date.to.utc.time()` invoking `date.to.utc()` which produced a **Unix Epoch Timestamp in seconds** (~1,793,800,000+).
   - Inserting 1.79 billion into a `Date 4` column via `db.insert()` triggered bshell database driver `Fatal Error 205: Value is out of range` (`ENOTINRANGE` / SQL `22008`).
   - Neither `audit_4gl.py` nor `check_4gl_script.py` flagged passing `date.to.utc()` or UTC timestamp functions into Date fields.

2. **Fatal Error 205 via Mandatory Numeric Zero-Constraint (`line = 0`)**:
   - In temp table `txcmg010`, field `line` (`tfgld.lino`) was generated with `Mandatory: Yes` (`isMandatory: true`).
   - In Infor LN Accounts Receivable (`tfacr500`), standard sales invoice open items (`tfacr.trec.invoice`) have natural document line number `line = 0` (header items).
   - In bshell database driver semantics, **mandatory numeric fields strictly forbid 0**. Inserting `0` into a mandatory numeric field triggers `Fatal Error 205 (Out of range)`.
   - Table generation tools (`generate_ln_table.py`, schema templates) lacked guardrails preventing `mandatory: true` on line number fields.

3. **Logical Inversion via Cross-Domain Enum Comparisons**:
   - `tfacr500.cdf_stdd` domain was changed from `tfcmg.stdd` (where `1 = selected`) to custom domain `txbsta` (where `1 = not.applic`, `2 = docn.selected`).
   - Code compared `tfacr500.cdf_stdd <> tfcmg.stdd.selected` (`<> 1`), inadvertently skipping all unbilled invoices and selecting already-billed invoices.
   - Bshell compiles enums to plain integer literals; no static check prevented cross-domain enum comparisons or checked enum symbol validity against `.ln_dd_cache.json`.

4. **String Truncation in Cloud SSO Usernames**:
   - Infor LN Cloud Single Sign-On (`logname$`) returns email addresses, AD UPNs, or UUIDs exceeding 16 characters.
   - Assigning `logname$` directly to domain `tfgld.user` (16 chars) risks silent truncation or runtime SQL errors without `strip$(shiftl$(logname$))(1; 16)`.

5. **Residual Ephemeral Debug Code (`message()`) in Processing Sessions**:
   - `message()` popups were left in production processing scripts, blocking headless execution.
   - `audit_4gl.py` only checked `message()` in DAL scripts (`DAL001`), not in processing/batch sessions.

6. **Unified Check Suite Test Disconnect**:
   - `scripts/run_checks.py` only executed unit tests in `ln_studio_skill/tools/tests`, ignoring `erp-ln-progguide/tests/test_audit_4gl.py`.

---

## 2. Settled Architectural Decisions (Proposed Architecture)

### Decision 1: Domain Datatype Safety Linter (`DMN002`) & Date Zero-Guard Guidelines
1. **Linter Rule `DMN002` in `audit_4gl.py`**:
   - Flag any assignment of `date.to.utc(...)` or `utc.num()` to a variable or table column whose domain or name indicates a Julian Date (e.g. `*.docd`, `*.dued`, `*.date`, domain `tcdate`, `tfgld.date`).
   - Enforce proper date idioms: use Julian Date directly (`docd = tfacr500.docd`, `date.num()`), and reserve UTC seconds for timestamp domains (`tcmcs.long`, `utc.num()`).
2. **Defensive Date Zero-Guards**:
   - Document and audit standard zero-fallback pattern for transaction dates:
     `if tfacr500.docd <= 0 then docd = date.num() endif`.

### Decision 2: Mandatory Numeric Zero-Constraint Linter (`TBL003`) & Table Modeling Advisory
1. **Developer-Controlled Mandatory Attributes**:
   - As clarified during review, line and sequence number fields (`line`, `lino`, `seqn`) CAN legitimately be marked `Mandatory: Yes` in entity tables where business rules require line items starting from 10, 20, etc. (where 0 is invalid).
   - Therefore, the schema tools (`generate_ln_table.py`, `ln_component_builder.py`) will NOT forcibly overwrite `mandatory: false` on line fields. Instead, an advisory warning will be emitted if a table archetype indicates temporary/staging/selection tables for Accounts Receivable or open items where header line number `0` is expected.
2. **Static Code Linter (`TBL003`)**:
   - `audit_4gl.py` will inspect assignments prior to `db.insert()` or `dal.save.object()`.
   - If a numeric field is defined as `isMandatory: true` in `.ln_dd_cache.json` (or table definition), and the 4GL script explicitly assigns `0` to it (e.g. `<table>.line = 0`), or assigns from an open-item source known to have zero line numbers (such as `tfacr500.line`), the linter will trigger `TBL003` warning/error of bshell `Fatal Error 205 (ENOTINRANGE)` due to mandatory numeric zero-rejection.

### Decision 3: Enum Domain Type Safety & Cross-Domain Comparison Linter (`DMN003`)
1. **Cross-Domain Enum Linting**:
   - When inspecting comparisons (`==`, `<>`, `<`, `>`, `in`), verify that enum constants match the domain of the column/variable being evaluated (using `.ln_dd_cache.json` or table metadata).
   - Flag cross-domain comparisons (e.g., comparing a `txbsta` column against `tfcmg.stdd.*` constant).
2. **Banned Numeric Literals on Enums**:
   - Flag hardcoded integer comparisons against enum fields (e.g. `cdf_stdd == 1`), requiring symbolic enum constants (`txbsta.not.applic`).

### Decision 4: Cloud SSO Username Length & String Truncation Guardrail (`STR001`)
1. **Username Slicing Enforcement**:
   - Flag un-sliced assignment of `logname$` to fields of domain `tfgld.user` or any `string 16` target.
   - Prescribe canonical idiom: `curr_user = strip$(shiftl$(logname$))(1; 16)`.

### Decision 5: Ephemeral Debug Statement Linter (`DBG001`)
1. **Debug Call Flagging**:
   - Flag raw `message("...", ...)` calls in non-interactive / batch / processing archetypes (`type 4`, batch sessions, DALs) as warnings/errors, requiring structured logging or `mess()` with resource labels.

### Decision 6: Unified Test Suite Consolidation in `scripts/run_checks.py`
1. **Multi-Directory Test Discovery**:
   - Update `scripts/run_checks.py` to run both test suites:
     - `ln_studio_skill/tools/tests/test_*.py`
     - `erp-ln-progguide/tests/test_*.py`
2. **Comprehensive Unit Tests**:
   - Add test cases in `test_audit_4gl.py` covering `DMN002`, `DMN003`, `TBL003`, `STR001`, and `DBG001`.
