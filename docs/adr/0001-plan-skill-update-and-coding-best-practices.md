# ADR 0001: Infor ERP LN Skill Update & Coding Best Practices Architecture

- **Status**: Accepted
- **Date**: 2026-10-14
- **Decisions Recorded**:
  1. **Knowledge Structure**: Hybrid Approach. Ingest full 13 chapters of *Infor LN Development Tools 2016* into `references/dev_tools/` with a dedicated index (`DEV_TOOLS_INDEX.md`), create a dedicated `references/best_practices/` cookbook/pattern suite, and embed strict coding guardrails into `SKILL.md`.
  2. **Scope of Best Practices**: Full-stack LN coverage spanning both Modern Cloud Extensibility (Extension Hooks, CDFs, Cloud Governance) and Core 4GL Engineering (DAL 1/2, Baan SQL Query Optimization, Domain/Table Design, MMT).
  3. **Best Practices Suite Modularization**: Partition `references/best_practices/` into 5 focused guides:
     - `01_extension_hooks_cookbook.md`: Hook lifecycle, error handling patterns (`DALHOOKERROR`), CDF logic hooks, standard field hooks, cloud governance limits.
     - `02_dal_architecture_and_business_logic.md`: DAL 1 vs 2, SoC rules (no DB updates in UI scripts), property hooks, business methods, object sets.
     - `03_sql_query_optimization_and_transactions.md`: Embedded Baan SQL syntax, index alignment, array fetching, transaction scope, lock prevention.
     - `04_data_model_and_domain_design.md`: Domain design, table modeling, primary keys, reference integrity, table reconfiguration (`crdd`) safety.
     - `05_session_and_mmt_patterns.md`: Session types, MMT Controller/Satellite architecture, form commands, multi-language/labels.
  4. **Tooling & Pipeline**:
     - Implement `tools/convert_txt_dev_tools.py` to parse and convert `update/Infor LN Development Tools 2016.txt` cleanly into Markdown chapters.
     - Update `tools/generate_indices.py` to index `references/dev_tools/` and `references/best_practices/` into `index/INDEX.tsv`.
     - Update `tools/validate_skill.py` to ensure all links and files validate without error.

## Consequences (Pending User Approval)
- Positive: AI assistant will not just recall function signatures, but produce idiomatic, cloud-ready, performant Infor LN code adhering to Infor's official architecture.
- Negative: Increases skill content volume; requires index update via `tools/generate_indices.py` or index script.
