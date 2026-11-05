# Specification: Baan 4GL Coding Standards, Anti-Patterns, and Runtime Caveats

## Problem Statement

Developers and AI coding assistants implementing Infor ERP LN (Baan 4GL) logic repeatedly encounter catastrophic runtime crashes, silent data corruption, and compilation failures due to the absence of centralized, authoritative guidance on language-level fundamentals, defensive coding patterns, and runtime engine caveats. Specifically:

1. **Silent Data Truncation**: Variables handling database fields are frequently declared using primitive types (`long`, `string`, `double`) rather than centralized Data Dictionary Domains. When table definitions are expanded in enterprise data dictionaries, compiled scripts do not automatically adapt, causing truncated business data during inserts and updates.
2. **Preprocessor and Linkage Failures**: Developers misuse `#include <...>` for application headers instead of `#include "..."`, omit the mandatory `#pragma used dll` directive with the `o` prefix for shared business libraries, or declare `#define` macros using 4GL reserved keywords, leading to unresolved symbols or compiler syntax errors.
3. **Unsafe Parameter Interfaces**: Subroutines and functions lack directional parameter naming (`i.`, `o.`, `io.`), fail to enforce read-only semantics with `const`, fail to return output references with `ref`, and omit standardized return status conventions (0 for success, negative for failure).
4. **Table Record Buffer Collisions**: The 4GL execution engine allocates a single shared memory record buffer for each declared table. Querying records in helper functions or loops using `select table.*` silently overwrites active form record buffers, causing severe data cross-contamination or runtime failure when saving UI forms.
5. **Array Dimension Violations**: Developers unfamiliar with Baan 4GL 1-based array indexing access index 0 or fail to use the `fixed` keyword or empty parentheses syntax when passing array parameters, triggering bshell memory violations.
6. **Fatal Runtime Anti-Patterns**: Developers write floating-point equality checks using `==` instead of precision-aware comparison functions, issue nested `commit.transaction()` calls inside DAL hooks or subroutines that break atomic unit-of-work boundaries, omit `selectempty` fallbacks, employ unstructured `goto` branching, and create unbounded table locks that trigger database deadlocks.

---

## Solution

Enhance the Infor ERP LN programmer reference and engineering skill by establishing an authoritative, complete English-language specification and coding standards guide covering all 6 pillars of 4GL programming, embedding hard negative constraints into the root skill instructions, and updating the search and catalog index:

1. **4GL Language Standards & Anti-Patterns Guide**: Create an exhaustive, production-grade guide in technical English detailing:
   - Domain declarations vs. primitive types, enumeration and set handling, and local vs. global/extern scope confinement.
   - Library linking via `#pragma used dll`, `#include` path conventions, and macro definition rules.
   - Formal function parameter contracts with directional Hungarian notation, `const`, `ref`, and standardized status returns.
   - Table buffer collision prevention, column-to-variable binding, table aliases, single-row query optimizations, explicit column projection, and DAL mutation delegation.
   - Dimensioned domain arrays, 1-based indexing rules, and array parameter passing mechanics.
   - Critical syntax caveats, including precision-safe double comparisons, outer-only transaction orchestration, reserved keyword collision avoidance, mandatory `selectempty` handling, prohibition of `goto`, and scoped table locking.
2. **Root Skill Guardrail Elevation**: Elevate these principles into mandatory, non-negotiable negative constraints within the core skill prompt, ensuring AI agents actively reject anti-patterns during code generation and code review.
3. **Cross-Guide Alignment & Discoverability**: Cross-reference the new standards within existing database optimization and data modeling architectural guides, register the new guide in the master document catalog, and verify command-line discoverability via the skill's search engine.

---

## User Stories

1. As an LN developer, I want clear rules on domain usage versus primitive types, so that my code automatically respects Data Dictionary modifications and avoids data truncation upon recompilation.
2. As an LN developer, I want guidelines on enumerations and set types, so that operational state variables are strictly bound to declared Data Dictionary domains.
3. As an LN developer, I want explicit variable scoping rules, so that local variables remain strictly confined to functions and do not leak into global session state.
4. As an LN developer, I want guidance on when to use `extern`, so that global variables are reserved exclusively for form/report bindings and cross-session communication.
5. As an LN developer, I want exact syntax patterns for library linkage using `#pragma used dll`, so that external business DLLs resolve properly at compile and load time.
6. As an LN developer, I want clear distinctions between `#include <...>` and `#include "..."`, so that standard system headers and application includes are imported without path conflicts.
7. As an LN developer, I want macro naming guidelines, so that `#define` constants are capitalized and never conflict with 4GL reserved keywords.
8. As an LN developer, I want directional parameter naming standards (`i.`, `o.`, `io.`), so that function contracts immediately communicate data flow to callers and maintainers.
9. As an LN developer, I want parameter mutability conventions (`const` and `ref`), so that input arguments cannot be accidentally mutated and return parameters are reliably captured.
10. As an LN developer, I want standardized function return codes, so that callers can uniformly inspect whether a routine succeeded (0) or failed (negative error code).
11. As an LN developer, I want to understand the 4GL Table Record Buffer architecture, so that I understand why `select table.*` in a helper function corrupts active session forms.
12. As an LN developer, I want concrete patterns for column-to-local variable binding in SQL queries, so that query results do not overwrite global table buffers.
13. As an LN developer, I want table alias conventions in embedded SQL, so that sub-queries and secondary lookups execute safely alongside primary table buffers.
14. As an LN developer, I want single-record query optimization guidelines, so that point lookups use single-row clauses rather than streaming entire recordsets.
15. As an LN developer, I want explicit field-based `WHERE` clauses instead of hardcoded index references, so that future database index tuning does not break existing logic.
16. As an LN developer, I want clear rules mandating DAL mutations over raw database operations, so that data modifications run all business validations and integrity checks.
17. As an LN developer, I want dimensioned array rules and passing conventions, so that I access 1-based arrays correctly without off-by-one errors or memory violations.
18. As an LN developer, I want precision-safe double comparison instructions, so that floating-point logic evaluates accurately using comparison routines rather than direct equality.
19. As an LN developer, I want transaction boundary rules, so that nested `commit.transaction()` calls are eliminated from DAL hooks and libraries, preserving atomic transaction boundaries.
20. As an LN developer, I want a comprehensive list of 4GL reserved keywords, so that variables and custom fields never conflict with compiler language tokens.
21. As an LN developer, I want mandatory `selectempty` handling rules, so that missing database records are cleanly captured and variables are appropriately reset.
22. As an LN developer, I want structured control flow standards prohibiting `goto`, so that codebase readability and exception handling maintain high architectural standards.
23. As an LN developer, I want scoped table locking rules, so that updates hold lock windows for the shortest possible duration and perform rollbacks on database errors.
24. As an AI assistant, I want hard negative constraints in the skill definition, so that I never produce flawed 4GL code containing buffer overwrites, direct double comparisons, or nested commits.
25. As a repository maintainer, I want all new guides cataloged and indexed, so that CLI search commands resolve queries quickly and accurately.

---

## Implementation Decisions

### 1. Language and Tone
- All reference documentation, code examples, architectural descriptions, and code comments must be authored exclusively in technical English to preserve consistency with official Infor LN manuals and the existing repository.
- Guidance must be prescriptive, distinguishing strict prohibitions (anti-patterns) from mandatory compliant standards.

### 2. Guide Structure & Content
- Create a dedicated best practices guide addressing the six core areas:
  - **Domain & Variable Scope**: Declarations using Data Dictionary domains, enumeration binding, function-local variable scope confinement, and restricted use of `extern` for form/report interfaces.
  - **Preprocessor & Library Linking**: Compiling external DLLs via compiler directives, standard system vs. application include syntax, and macro hygiene preventing reserved keyword collisions.
  - **Function Design & Parameter Passing**: Directional naming conventions, parameter immutability and reference semantics, and uniform error status returns.
  - **Embedded SQL & Buffer Protection**: Global table record buffer overwrite mechanics, column-to-local binding, table aliases, single-row query syntax, explicit column projection, and delegation of database writes to the Data Access Layer.
  - **Dimensioned Arrays**: 1-based indexing memory rules, element declaration syntax, and array parameter passing conventions.
  - **Critical Runtime Caveats**: Floating-point epsilon comparison routines, outer-boundary transaction orchestration, reserved word avoidance, mandatory query empty state handling, elimination of unstructured branching, and scoped row-level locking.
- Each topic must feature paired "Anti-Pattern" and "Compliant Pattern" code blocks using realistic enterprise ERP table domains and module prefixes.

### 3. Architectural Guardrail Integration
- Enhance the root skill definition by adding a dedicated subsection of hard negative constraints directly under the architectural guardrails.
- Ensure high visibility of critical failure modes so that downstream AI agents evaluate these constraints before emitting 4GL code.

### 4. Cross-Reference and Documentation Navigation
- Cross-link the new guide from existing database query optimization and data model architecture guides to provide unified navigation.
- Update the master documentation catalog to incorporate the new guide with its complete title and relative path.

### 5. Search Toolchain Integration
- Verify that the CLI search tool recognizes the new reference file under the best practices category without requiring modification to the search algorithm.

---

## Testing Decisions

### 1. Behavior-Only Testing Principles
- Tests must verify external accessibility, document discoverability, and structural link integrity across the skill repository.
- Tests will not assert on internal formatting styles, but will assert on document existence, valid index registration, and CLI search retrieval.

### 2. Modules to Test
- **Documentation Catalog**: Verify that the master index file contains an entry for the new coding standards guide with matching relative path and title.
- **Search Tool CLI**: Execute the search script targeting the best practices directory and verify that search queries for core concepts (such as buffer collision, floating-point comparison, library directive, and dimension passing) return positive matches with file names, line numbers, and relevant text snippets.
- **Cross-Reference Links**: Validate that relative markdown hyperlinks between the root skill definition, existing architectural guides, and the new guide resolve cleanly.

### 3. Prior Art
- Search CLI validation patterns previously used for the development tools and extension cookbooks (`search.py --dir best_practices`).
- Master index verification against the repository's tabular index structure (`index/INDEX.tsv`).

---

## Out of Scope

- Implementing or altering Infor LN Enterprise Server core binaries, 4GL compiler executables, or bshell C runtimes.
- Authoring translations or bilingual variations of the technical documentation.
- Modifying standard out-of-the-box Infor LN table definitions or enterprise business logic scripts.

---

## Further Notes

- This specification aligns directly with Architecture Decision Record ADR-001.
- All code examples in the resulting documentation must reflect modern Infor LN best practices (LN 10.x / Cloud Edition), prioritizing DAL 2 and Data Access Layer business logic over legacy Baan IV / Baan V direct table manipulations.
