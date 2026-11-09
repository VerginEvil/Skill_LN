# ADR 0019: Baan 4GL String Array Subscript Mechanics and Embedded SQL Host Variable Guardrails (SQL008 & ARR002)

- **Status**: Accepted
- **Date**: 2026-11-09
- **Context**: Retrospective on Billing System Integration (`txcmg0510m000`), Infor LN `bic` compilation failures, and Baan SQL precompiler host variable restrictions.

---

## 1. Context and Problem Statement

During the development and compilation of `txcmg0510m000` (Multi-Occurrence UI Row Selection via `do.selection` and Targeted Primary-Key Deletion), the Infor LN `bic` 4GL compiler and SQL precompiler raised 10 critical errors:
1. **Illegal number of array subscripts for string arrays** (`mark_itbp`, `mark_ttyp`, `cust_list`):
   Declared as `domain tccom.bpid mark_itbp(500)` and accessed as `mark_itbp(1, marked_count)` or `mark_itbp(i)`.
2. **SQLState 42I03: Unknown column 'i' (error 302)**:
   Triggered on embedded SQL host variable array indexing: `where tfacr500.ttyp = :mark_ttyp(i)` or `:mark_ttyp(1, i)`.

Static analysis (`scripts/audit_4gl.py`) previously lacked mechanical guardrails to detect these syntax anti-patterns before compilation. Furthermore, `references/best_practices/06_4gl_coding_standards_and_caveats.md` contained a misleading example (`domain tcorno recent_orders(10)`) that reinforced the incorrect assumption that 1D domain declarations allocate arrays of strings.

---

## 2. Root Cause Analysis

### 2.1 String Array Subscript Mechanics in Baan 4GL (`bic` Compiler)
- In Baan 4GL, **strings are character arrays**.
- If a developer writes `domain tccom.bpid mark_itbp(500)` where `tccom.bpid` is a string domain (e.g. 9 chars), the `bic` compiler treats `(500)` as the **length of a single scalar string** (overriding the domain length), **NOT** an array of 500 strings.
- Declaring an array of strings requires **2 dimensions**:
  - **Dimension 1**: String buffer length / character width (e.g. 9 for BPID, 3 for TTYP).
  - **Dimension 2**: Number of elements in the array.
  - Syntax: `string arr(length, count)`.
- Accessing a string array requires **2 subscripts**: `arr(start_char_pos, element_index)` (e.g. `mark_itbp(1, i)`). Accessing with a single subscript `arr(i)` triggers `Illegal number of array subscripts`.
- Conversely, for **numeric, date, long, double, and enum domains**, single-dimensional syntax `domain <domain> arr(count)` is valid and accessed via `arr(i)`.

### 2.2 SQL Host Variable Subscript Restrictions (Error 302)
- In Embedded Baan SQL, host variables are prefixed with a colon (`:variable`).
- The Baan SQL precompiler only supports **scalar host variable identifiers**.
- When encountering `:mark_ttyp(i)` or `:mark_ttyp(1, i)`, the precompiler parses `:mark_ttyp` as the variable and treats `(i)` as an SQL column or table qualifier in the query abstract syntax tree.
- Since table `tfacr500` has no column named `i`, the precompiler halts with:
  `SQLState 42I03: Unknown column 'i' (error 302)`.
- The mandatory pattern is **Scalar Local Staging**: staging array elements into scalar local variables prior to query execution, and binding only scalar variables in the SQL statement.

---

## 3. Decision Outcome

We implement the following improvements across the `erp-ln-progguide` skill:

### 3.1 Static Analysis Guardrails (`scripts/audit_4gl.py`)
1. **Rule `SQL008` (Severity: ERROR)**:
   - Detects array subscripts and brackets/parentheses in SQL host variables (`:ident\s*[(\[]`).
   - Diagnostic Message: `"Array subscript or parentheses detected in SQL host variable ':{var}(...)'. Baan SQL precompiler does not support subscripts in host variables; stage array elements into scalar variables before the query."`
2. **Rule `ARR002` (Severity: WARNING)**:
   - Detects 1D domain string array declarations (`domain <str_domain> arr(count)`).
   - Utilizes `_is_string_domain()` with fallback heuristics and Data Dictionary cache inspection.
   - Diagnostic Message: `"Domain string array '%s' declared with 1D syntax; bshell treats this as string length. Use 2D syntax 'string arr(len, count)' and access with 'arr(1, idx)'."`

### 3.2 Documentation Hardening
1. **`06_4gl_coding_standards_and_caveats.md`**:
   - Fixed Section 6.2 to remove the misleading `domain tcorno recent_orders(10)` example and explicitly document the architectural distinction between numeric/enum arrays (1D `arr(count)`) and string arrays (2D `string arr(len, count)` accessed as `arr(1, idx)`).
   - Added Section 5.7 documenting Rule `SQL008` and the mandatory **Scalar Local Staging Pattern**.
2. **`03_sql_query_optimization_and_transactions.md`**:
   - Added Section 1.3 documenting host variable restrictions and the Scalar Staging Pattern.
3. **`erp-ln-progguide/SKILL.md`**:
   - Updated Core Guardrails 3 and 5 to incorporate `SQL008` and `ARR002` while preserving the strict <= 80 line budget.

### 3.3 Verification Suite
- Added 5 new unit tests in `erp-ln-progguide/tests/test_audit_4gl.py` covering `SQL008` error detection, scalar host variable passing, `ARR002` warning emission on 1D string domains, and clean passes for numeric/date/enum arrays and 2D string arrays.

---

## 4. Consequences

- **Positive**:
  - Mechanical error prevention: Agents and developers catch illegal host variable subscripts and 1D string array declarations locally before Studio compilation.
  - Zero context guessing: Documentation provides copy-paste compliant patterns for multi-occurrence selection buffers and SQL binding.
  - Test-verified: Full regression suite (33 tests in `erp-ln-progguide`, 300 tests in `ln_studio_skill`) passes cleanly.
- **Negative / Trade-offs**:
  - String array size constants must be declared via `#define` rather than relying solely on domain definitions, as Baan 4GL lacks dynamic string array resizing.
