# Task Tickets: Infor LN Studio Build 0640 Dictionaries Extraction, Cloud Governance & Standalone 4GL Audit Engine

- **Specification**: [`docs/SPEC_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md`](docs/SPEC_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md)
- **Implementation Plan**: [`docs/PLAN_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md`](docs/PLAN_PROGGUIDE_STUDIO_EXTRACTION_AND_AUDIT.md)
- **Architecture Decision Records**:
  - [`docs/adr/0001-plan-skill-update-and-coding-best-practices.md`](docs/adr/0001-plan-skill-update-and-coding-best-practices.md)
  - [`docs/adr/0002-ln-studio-skill-self-contained-toolchain.md`](docs/adr/0002-ln-studio-skill-self-contained-toolchain.md)
  - [`docs/adr/0003-ln-studio-object-modeling-and-static-verification.md`](docs/adr/0003-ln-studio-object-modeling-and-static-verification.md)
  - [`docs/adr/0004-4gl-coding-standards-and-caveats.md`](docs/adr/0004-4gl-coding-standards-and-caveats.md)
  - [`docs/adr/0005-progguide-studio-dictionaries-and-audit-engine.md`](docs/adr/0005-progguide-studio-dictionaries-and-audit-engine.md)
- **Target Skills**: `erp-ln-progguide` (Primary), `ln_studio_skill` (Rule Alignment)

---

## Dependency Graph

```mermaid
flowchart TD
    T01["01: Multi-Tier Knowledge Extractor"]
    T02["02: Enriched Grep-Friendly Function Index"]
    T03["03: Standalone 4GL & DAL Audit Engine"]
    T04["04: Synchronized Rule Alignment in ln_studio_skill"]
    T05["05: Export VS Code Extension Assets Package"]
    T06["06: Test Suite, Documentation & Catalog Indexing"]

    T01 --> T02
    T01 --> T03
    T02 --> T03
    T03 --> T04
    T01 --> T05
    T03 --> T06
    T04 --> T06
    T05 --> T06

    classDef done fill:#d4edda,stroke:#28a745,stroke-width:2px;

    class T01,T02,T03,T04,T05,T06 done;
```

---

## Completed Ticket Roster (Batch: Build 0640 Dictionaries, Cloud Governance & Standalone Auditor)

| ID | Title | Blocked by | Status | Target Deliverable |
|---|---|---|---|---|
| **01** | Multi-Tier Knowledge Extractor | *None* | `done` | `tools/extract_studio_knowledge.py`, `functions_db.json`, `studio_syntax_completion.json`, `templates/` |
| **02** | Enriched Grep-Friendly Function Index | **01** | `done` | `erp-ln-progguide/references/FUNCTION_INDEX.md` |
| **03** | Standalone 4GL & DAL Audit Engine | **01, 02** | `done` | `erp-ln-progguide/scripts/audit_4gl.py` |
| **04** | Synchronized Rule Alignment with `ln_studio_skill` | **01, 03** | `done` | `ln_studio_skill/tools/check_4gl_script.py` |
| **05** | Export VS Code Extension Assets Package | **01** | `done` | `export/vscode/syntaxes/`, `snippets/`, `language-configuration.json`, `completions.json`, `README.md` |
| **06** | Test Suite, Documentation & Catalog Indexing | **03, 04, 05** | `done` | `erp-ln-progguide/tests/test_audit_4gl.py`, `erp-ln-progguide/SKILL.md`, `INDEX.tsv` |

---

## Archive / Completed Batches

<details>
<summary><b>Batch: Baan 4GL Coding Standards, Anti-Patterns & Runtime Caveats (Completed)</b></summary>

- **Specification**: [`docs/SPEC_4GL_CODING_STANDARDS_AND_CAVEATS.md`](docs/SPEC_4GL_CODING_STANDARDS_AND_CAVEATS.md)
- **Local Issues Directory**: [`.scratch/4gl-coding-standards-and-caveats/issues/`](.scratch/4gl-coding-standards-and-caveats/issues/)

| ID | Title | Status | Ticket File |
|---|---|---|---|
| **01** | Domain, Scope & Preprocessor Standards | `done` | [`01-domain-scope-and-preprocessor-standards.md`](.scratch/4gl-coding-standards-and-caveats/issues/01-domain-scope-and-preprocessor-standards.md) |
| **02** | Function Contracts & Buffer Collision Protection | `done` | [`02-function-contracts-and-buffer-collision-protection.md`](.scratch/4gl-coding-standards-and-caveats/issues/02-function-contracts-and-buffer-collision-protection.md) |
| **03** | Array Dimensions & Fatal Runtime Caveats | `done` | [`03-array-dimensions-and-fatal-runtime-caveats.md`](.scratch/4gl-coding-standards-and-caveats/issues/03-array-dimensions-and-fatal-runtime-caveats.md) |
| **04** | Skill Guardrails Elevation & Cross-Linking | `done` | [`04-skill-guardrails-elevation-and-cross-linking.md`](.scratch/4gl-coding-standards-and-caveats/issues/04-skill-guardrails-elevation-and-cross-linking.md) |
| **05** | Catalog Indexing & End-to-End Verification | `done` | [`05-catalog-indexing-and-search-verification.md`](.scratch/4gl-coding-standards-and-caveats/issues/05-catalog-indexing-and-search-verification.md) |

</details>

<details>
<summary><b>Batch: LN Studio Object Modeling, SCM Guardrails & Static Verification Engine (Completed)</b></summary>

- **Specification**: [`docs/SPEC_LN_STUDIO_OBJECT_AND_VALIDATION.md`](docs/SPEC_LN_STUDIO_OBJECT_AND_VALIDATION.md)
- **Local Issues Directory**: [`.scratch/ln-studio-object-validation/issues/`](.scratch/ln-studio-object-validation/issues/)

| ID | Title | Status | Ticket File |
|---|---|---|---|
| **01** | Pinned Studio Path, Explicit Workspace Resolution, Read-Only Guardrails & 12-Extension `.admin` Sync | `done` | [`01-workspace-scm-guardrails-and-admin-sync.md`](.scratch/ln-studio-object-validation/issues/01-workspace-scm-guardrails-and-admin-sync.md) |
| **02** | High-Fidelity Table, Domain & Label Modeling and Generation | `done` | [`02-table-domain-label-fidelity-and-generation.md`](.scratch/ln-studio-object-validation/issues/02-table-domain-label-fidelity-and-generation.md) |
| **03** | Multi-Archetype Session, MMT Controller/Satellite, Library & Menu Generation | `done` | [`03-session-mmt-library-and-menu-generation.md`](.scratch/ln-studio-object-validation/issues/03-session-mmt-library-and-menu-generation.md) |
| **04** | LN Studio Syntax Highlighting & Code Completion Extractor + Static 4GL Inspector | `done` | [`04-studio-syntax-completion-extractor-and-script-checker.md`](.scratch/ln-studio-object-validation/issues/04-studio-syntax-completion-extractor-and-script-checker.md) |
| **05** | Four-Layer Object, Cross-Reference & Script Validator (`validate` & `--fix`) | `done` | [`05-four-layer-object-and-workspace-validator.md`](.scratch/ln-studio-object-validation/issues/05-four-layer-object-and-workspace-validator.md) |
| **06** | Skill Seam Alignment, XML Schema Reference Expansion, Indexing & Live Deployment Sync | `done` | [`06-skill-seam-reference-indexing-and-live-sync.md`](.scratch/ln-studio-object-validation/issues/06-skill-seam-reference-indexing-and-live-sync.md) |

</details>
