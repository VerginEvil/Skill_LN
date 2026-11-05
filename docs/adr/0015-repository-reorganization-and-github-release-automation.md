# ADR 0015: Repository Reorganization, .gitignore Hardening, and GitHub Release Automation

- **Status**: Accepted
- **Date**: 2026-11-05
- **Target Skills**: `erp-ln-progguide`, `ln_studio_skill`
- **Prior ADRs**:
  - [`docs/adr/0002-ln-studio-skill-self-contained-toolchain.md`](0002-ln-studio-skill-self-contained-toolchain.md) *(Self-contained skill architecture)*
  - [`docs/adr/0014-quality-hardening-ci-guardrails-and-mcp-execution-parity.md`](0014-quality-hardening-ci-guardrails-and-mcp-execution-parity.md) *(Unified checks script & CI guardrails)*

---

## 1. Context & Problem Statement

Following the completion of the retro-improvements and quality hardening milestone (`feat/retro-improvements-and-hardening`), the repository had grown significantly in scope and complexity. A full structural audit revealed the following organizational and deployment gaps:

1. **Root Directory Clutter & Fragmented Documents**:
   The repository root contained loose plans (`plan_erp_ln_progguide_update.md`, `Tickets.md`), a legacy developer script directory (`tools/`), and unorganized markdown files (`docs/PLAN_*.md`, `docs/SPEC_*.md`), making the repository difficult to navigate and non-standard for GitHub users.
2. **Domain Documentation Layout Drift**:
   `GLOSSARY.md` lived at the root, whereas domain documentation best practices for this project call for centralized knowledge organization under `docs/glossary/GLOSSARY.md` with explicit mapping in `AGENTS.md` and `docs/agents/domain.md`.
3. **Flawed `.gitignore` Rule Trapping Documentation**:
   The previous `.gitignore` contained `docs/*` with narrow whitelists (`!docs/adr/`, `!docs/agents/`), causing critical documentation (such as `docs/MAINTENANCE_GUIDE.md` and plans) to be silently ignored by Git.
4. **Missing GitHub CI/CD & Releases Pipeline**:
   The repository was moving from GitLab to GitHub (`https://github.com/VerginEvil/Skill_LN.git`). It lacked GitHub Actions workflows for continuous integration and automated GitHub Releases packaging for the two core skills and VS Code extension assets.

---

## 2. Settled Architectural Decisions

### Decision 1: Monorepo Dual-Skill Root Placement
The two primary skills remain as first-class directories at the repository root:
- `erp-ln-progguide/`: Knowledge base, function indices, and standalone 4GL audit engine.
- `ln_studio_skill/`: Headless JCA 1.6 connector, component generators, SCM engine, and Stdio MCP server.

Moving them under a nested `skills/` directory was evaluated and rejected to maintain concise paths, preserve compatibility with agent skill discovery, and prevent breaking path assumptions in existing unit tests and scripts.

### Decision 2: Documentation & Script Reorganization
1. **Centralized Domain Glossary**:
   Relocate `GLOSSARY.md` to `docs/glossary/GLOSSARY.md`. Update `AGENTS.md` and `docs/agents/domain.md` accordingly.
2. **Historical Plans & Specifications Archive**:
   Consolidate all historical plans and specifications (`Tickets.md`, `plan_erp_ln_progguide_update.md`, `docs/PLAN_*.md`, `docs/SPEC_*.md`) into `docs/plans/`.
3. **Developer Utilities Consolidation**:
   Move `tools/export_vscode_assets.py` and `tools/extract_studio_knowledge.py` into `scripts/developer/`, and delete the redundant root `tools/` directory. Update `ln_studio_skill/tools/generate_indices.py` to search `scripts/developer/` first, maintaining backward compatibility.
4. **Sample Export Artifact Isolation**:
   Move sample export artifact `export/txibddllitem01.cln` to `erp-ln-progguide/tests/samples/`, keeping `export/vscode/` dedicated solely to VS Code extension assets.

### Decision 3: Comprehensive `.gitignore` Hardening
Replace ad-hoc ignore rules with a categorized specification:
- **Infor Credentials & Tokens**: Strict exclusion of `*.ionapi`, `.ln_studio_tokens.json`, `.ln_studio_config.json`, `.ln_dd_cache.json`, and `.cache/`.
- **Proprietary & Bulky Reference Dumps**: Exclusion of `knowledge_docs/`, `implementation/`, `.scratch/`, and `output/`.
- **Java / JCA Binaries**: Re-enforce BYOJ policy by ignoring `*.class` and `*.jar`.
- **Documentation Normalization**: Remove blanket `docs/*` ignore pattern, allowing full version control of `docs/glossary/`, `docs/adr/`, `docs/agents/`, and `docs/plans/`.

### Decision 4: GitHub Actions CI & Release Packaging Toolchain
1. **Continuous Integration (`.github/workflows/ci.yml`)**:
   Runs on `windows-latest` with Python 3.11, executing `python scripts/run_checks.py` on all pushes and pull requests to `main`.
2. **Release Automation (`.github/workflows/release.yml`)**:
   Triggered on Git tag push (`v*`). Executes quality gates, determines the version, calls `scripts/package_release.py`, extracts version notes from `CHANGELOG.md`, and creates a GitHub Release with three downloadable ZIP archives:
   - `erp-ln-progguide-v<version>.zip`
   - `ln_studio_skill-v<version>.zip`
   - `skill-ln-vscode-v<version>.zip`
3. **Packaging Utility (`scripts/package_release.py`)**:
   Pure Python hermetic bundler filtering out caches, virtual environments, VCS metadata, and `.jar` binaries.
4. **Standard Repository Files**:
   Add official `LICENSE` (MIT) and structured `CHANGELOG.md` starting at `v1.0.0`. Remove obsolete `.gitlab-ci.yml`.

---

## 3. Consequences

### Positive
- **Clean Root & Intuitive Layout**: The repository root is uncluttered, professional, and immediately understandable to new developers and AI agents.
- **Security & IP Protection**: Hardened `.gitignore` guarantees that customer credentials, OAuth2 tokens, and proprietary Infor documentation never leak to public remotes.
- **Automated Distribution**: Releases on GitHub are completely automated with one git tag push, providing ready-to-use skill packages with changelogs.
- **Documentation Integrity**: All project documentation is properly tracked by Git without unintended exclusions.

### Neutral / Trade-offs
- Internal references to `GLOSSARY.md` and `Tickets.md` now point to `docs/glossary/` and `docs/plans/`.
- Developer tools previously invoked from `tools/` must now be executed from `scripts/developer/`.
