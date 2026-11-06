# Specification: Runtime Error Prevention, Audit Guardrails, and Skill Hardening

- **Status**: `ready-for-agent`
- **Architecture Decision Record**: [`docs/adr/0017-runtime-error-prevention-audit-guardrails-and-skill-hardening.md`](../adr/0017-runtime-error-prevention-audit-guardrails-and-skill-hardening.md)
- **Local Tracker**: [`.scratch/billing-integration-retro-and-audit-hardening/spec.md`](../../.scratch/billing-integration-retro-and-audit-hardening/spec.md)
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`

---

## 1. Problem Statement

When developing and extending customizations on Infor LN Cloud Multi-Tenant, developers and AI coding agents encounter fatal runtime crashes, silent data corruption, and inverted business logic that pass standard bshell compilation and basic static linters undetected:

1. **Fatal Error 205 (Value is out of range) on Date Fields**: Standard Infor LN date domains represent Julian Day numbers (~740k). When code inadvertently introduces Unix Epoch UTC timestamps (seconds elapsed since 1970, ~1.79B) into date columns, the database driver triggers a fatal bshell crash upon record insertion.
2. **Fatal Error 205 on Mandatory Line Number Fields with Zero**: In Infor LN Accounts Receivable and Open Item architectures, invoice headers naturally utilize line number zero (`line = 0`). In bshell database driver semantics, any numeric column marked as mandatory strictly forbids zero, treating zero as unentered/empty. Assigning or copying zero into a mandatory line number field causes record insertion to abort with Error 205.
3. **Silent Logical Inversion from Cross-Domain Enum Comparisons**: When domain definitions evolve (such as transitioning from standard billing status domains to customer-specific status domains), bshell compiles enum symbols directly into raw integers without compile-time domain type safety. Comparing fields against enum symbols belonging to a different domain (or comparing against hardcoded integer literals) silently inverts document selection criteria, skipping valid records and processing invalid ones.
4. **Cloud SSO Username Truncation & Buffer Overrun**: Single Sign-On usernames from Infor OS and enterprise identity providers routinely exceed 16 characters. Assigning un-sliced usernames directly to standard 16-character user domains creates truncation hazards and database schema rejections.
5. **Interactive Debug Code Left in Automated Workflows**: Ephemeral debug popups left in batch processing sessions and data access layers block headless execution, hanging automated background tasks.
6. **Fragmented Test Verification in Tooling Repositories**: Verification gateways that omit sibling test suites allow regressions in offline audit engines to go unnoticed during continuous integration.

---

## 2. Solution Architecture

A multi-layered defensive engineering framework spanning static AST auditing, schema modeling advisories, and unified verification:

1. **Date Domain Safety Linter (`DMN002`)**: An AST-level static check that identifies and blocks assigning Unix Epoch UTC seconds or UTC time functions to Julian Day date fields, enforcing direct Julian day assignments and zero-fallback defensive guards.
2. **Mandatory Numeric Zero-Constraint Linter (`TBL003`)**: A semantic schema-aware check that inspects assignments prior to database insertions, catching attempts to write zero (or source fields known to contain zero, such as open item header lines) into columns marked mandatory in the Data Dictionary.
3. **Enum Domain Type Safety Linter (`DMN003`)**: A domain-aware rule that validates comparison operations against the Data Dictionary schema cache, preventing cross-domain enum comparisons and rejecting hardcoded non-zero integer literals on enum columns.
4. **Cloud SSO Username Slicing Guardrail (`STR001`)**: A static check that enforces domain-safe slicing on system username assignments targeting fixed-length user fields.
5. **Ephemeral Debug Code Linter (`DBG001`)**: An archetype-aware rule that enforces clean separation between interactive UI feedback and headless/batch processing logic, blocking raw debug message popups in non-interactive sessions.
6. **Consolidated Test Gateway**: A unified pre-commit and continuous integration runner that executes unit tests across all skill toolsets deterministically.

---

## 3. User Stories

1. As an Infor LN developer, I want the static audit engine to detect assignments of UTC timestamps to Julian Day date columns, so that I can eliminate `Fatal Error 205` crashes before deploying code to the cloud server.
2. As an Infor LN developer, I want clear guidance on using `date.num()` and direct table date assignment, so that document dates and due dates always contain valid Julian Day values.
3. As an Infor LN developer, I want defensive date zero-guards recommended whenever date fields are populated from external or database sources, so that uninitialized dates fall back to the current business date safely.
4. As a database modeler, I want table design tools to allow `Mandatory: Yes` on line and sequence number fields where business logic requires positive line numbers (such as sales order lines), so that domain integrity rules are not unnecessarily restricted.
5. As an Infor LN developer, I want the linter to flag any code that assigns `0` to a mandatory numeric column prior to database insertion, so that I do not trigger `Fatal Error 205` at runtime.
6. As an Infor LN developer working with Accounts Receivable open items, I want the linter to warn me when copying `line` from source invoice tables into a mandatory destination column, so that header items with `line = 0` do not abort batch processing.
7. As an Infor LN developer, I want the schema modeling tool to provide an advisory warning when creating staging or selection tables for open items, so that I am reminded to leave the line number column non-mandatory.
8. As a business logic developer, I want the linter to verify that enum comparisons match the domain assigned to the database column, so that I never accidentally compare against an enum symbol from an unrelated domain.
9. As a business logic developer, I want the linter to reject hardcoded integer literals (such as `== 1` or `<> 2`) when evaluating enum columns, so that business conditions always use clear, readable enum symbols.
10. As a business logic developer, I want the linter to permit comparison against `0` on enum columns with an advisory notice, so that standard patterns for checking uninitialized enum variables remain supported while warning of custom domains that define explicit non-zero default states.
11. As a cloud solutions engineer, I want the linter to catch assignments of `logname$` to 16-character user fields without substring slicing, so that long Single Sign-On usernames do not cause string truncation errors in cloud environments.
12. As a cloud solutions engineer, I want the prescribed SSO slicing pattern documented and enforced, so that all developers handle user attribution uniformly.
13. As an automation engineer, I want the linter to reject raw interactive `message()` calls in DAL scripts and batch processing sessions, so that automated background jobs never hang on modal dialog popups.
14. As an Infor LN developer, I want interactive `message()` calls in standard UI sessions flagged only as non-blocking warnings, so that my rapid debugging workflow during UI prototyping is not hindered.
15. As a code reviewer, I want mechanical violations (such as date mismatches, mandatory zero assignments, and cross-domain enum comparisons) caught deterministically by automated checks, so that human review can focus on architectural intent and business workflow correctness.
16. As an AI coding agent, I want clear domain glossary terms and decision records for Infor LN datatypes, so that generated 4GL scripts conform to bshell runtime constraints on the first attempt.
17. As an AI coding agent, I want the Data Dictionary cache to supply field mandatory flags and domain enum definitions automatically, so that semantic audits do not require live server connections during authoring.
18. As a repository maintainer, I want the unified check script to discover and run tests across both the Studio toolchain and the Programmer's Guide audit engine, so that all modules are verified prior to any commit or release.
19. As a CI pipeline administrator, I want test execution across all toolsets to report an aggregated pass/fail summary and exit code, so that pull requests with regressions in any component are prevented from merging.
20. As an Infor LN developer, I want comprehensive reference documentation in the Programmer's Guide explaining bshell date handling, mandatory constraints, and enum boundaries, so that team knowledge is preserved and accessible.

---

## 4. Implementation Decisions

### 1. Date Domain Safety Linter (`DMN002`)
- **Inspection Scope**: Inspects variable and table column assignment statements within 4GL scripts, DALs, and Extension Modeler sources.
- **Trigger Condition**: Triggers an `ERROR` diagnostic when the right-hand side of an assignment calls `date.to.utc(...)` or `utc.num()` while the left-hand target represents a Julian Date (identified by field suffix naming conventions like `.docd`, `.dued`, `.date`, or domain metadata specifying `Date 4` / `tfgld.date` in the Data Dictionary cache).
- **Remediation Advice**: Diagnostics must explicitly recommend direct assignment (`docd = tfacr500.docd`), current Julian day retrieval (`date.num()`), or defensive zero-guard fallback.

### 2. Mandatory Numeric Zero-Constraint Linter (`TBL003`)
- **Inspection Scope**: Analyzes data population logic preceding `db.insert(...)` and `dal.save.object(...)`.
- **Trigger Condition**: Triggers when a numeric field defined as `isMandatory: true` in the Data Dictionary schema cache receives an assignment of literal `0`, or receives a direct assignment from an open item source field known to possess zero header values (specifically `tfacr500.line`), without an intervening conditional guard.
- **Severity**: Emits an `ERROR` when schema cache strictly confirms `isMandatory: true`; emits an `ADVISORY WARNING` when schema is inferred from naming patterns.
- **Table Modeling Behavior**: Schema generators and builders retain developer-specified `isMandatory` flags, but emit an advisory note when generating staging/selection table schemas that reference Accounts Receivable or open item lines.

### 3. Enum Domain Safety & Literal Guard (`DMN003`)
- **Inspection Scope**: Evaluates relational comparison expressions (`==`, `<>`, `<`, `>`, `in`) involving table columns or variables with enum domains.
- **Cross-Domain Validation**: Triggers an `ERROR` if the enum symbol prefix on one side does not match the domain code of the column on the other side (verified via Data Dictionary cache).
- **Literal Inspection**:
  - Comparison against integer literals `>= 1` triggers an `ERROR` requiring symbolic enum representation.
  - Comparison against `0` triggers an `ADVISORY WARNING` reminding the author to verify whether the target domain has an explicit default state (e.g. `txbsta.not.applic = 1`).

### 4. Cloud SSO Username Slicing Guardrail (`STR001`)
- **Inspection Scope**: Evaluates assignments where the right-hand side references `logname$`.
- **Trigger Condition**: Triggers a `WARNING` (promoted to `ERROR` in cloud mode) if assigned directly to a field of domain `tfgld.user` or a string variable with declared length <= 16 without applying `strip$(shiftl$(logname$))(1; 16)` or safe substring extraction.

### 5. Ephemeral Debug Code Cleanup (`DBG001`)
- **Inspection Scope**: Detects raw `message(...)` invocations across all 4GL script archetypes.
- **Severity Tiering**:
  - In DAL scripts (`type dal2` / `type dal1`) and Batch processing sessions (`type 4` / session scripts with no UI interaction): Triggers an `ERROR`.
  - In Cloud mode (`--cloud`): Triggers an `ERROR`.
  - In Interactive UI sessions (`type 1`, `type 2`, `type 3`): Triggers a non-blocking `WARNING` prompting cleanup prior to production deployment.

### 6. Unified Test Suite Consolidation
- **Execution Target**: Enhances the unified check script to discover and run tests from both:
  - The Studio skill tool tests directory.
  - The Programmer's Guide tests directory.
- **Reporting Contract**: Aggregates total tests run, skipped, and failed into a single unified summary report, returning non-zero if any test fails in either directory.

---

## 5. Testing Decisions

### What Makes a Good Test
- **External Behavior Only**: Tests must exercise the public interface of the auditor and schema generators, supplying realistic 4GL scripts and Data Dictionary cache configurations, and asserting on returned diagnostic codes, severities, and line numbers. Tests must never assert on private internal regexes or intermediate AST tokens.
- **Deterministic and Offline**: All tests must execute hermetically in memory without requiring live bshell connectivity, Eclipse workspaces, or external network services.
- **High Execution Speed**: Test suites across both directories must execute in under 3 seconds total.

### Modules Tested
1. **4GL & DAL Audit Engine**:
   - `DMN002`: Positive tests (valid Julian date assignment, `date.num()`), Negative tests (`date.to.utc()` assigned to `.docd`, `utc.num()` assigned to date field).
   - `TBL003`: Positive tests (non-zero assigned to mandatory column, zero assigned to optional column), Negative tests (`0` assigned to mandatory line column before `db.insert`).
   - `DMN003`: Positive tests (matching domain enum symbols, allowed zero checks), Negative tests (cross-domain enum comparison, raw integer literal comparison).
   - `STR001`: Positive tests (properly sliced `logname$`), Negative tests (un-sliced `logname$` assigned to 16-char field).
   - `DBG001`: Positive tests (`dal.set.error.message` in DAL, structured messages), Negative tests (raw `message()` in DAL and batch session).
2. **Table Component Generator**:
   - Verification of mandatory attribute persistence and staging table advisories.
3. **Unified Checks Gateway**:
   - Automated verification that the check script executes and aggregates both test directories cleanly.

---

## 6. Out of Scope

1. **Automatic Code Modification / In-Place Rewriting**: The audit engine will diagnose violations and output actionable remediation messages, but will not automatically mutate or overwrite source code files on disk without explicit user direction.
2. **Dynamic Runtime Bshell Interception**: The solution operates purely via offline static analysis and schema validation; live bshell process hooking or runtime memory patching is out of scope.
3. **Multi-File Whole-Program Type Inference**: Cross-file variable type tracing across multiple libraries or DLLs is out of scope; type information is derived from intra-file declarations, bshell naming conventions, and the local Data Dictionary cache.
