# Skill_LN — Home Repo Steering & Development Guidelines

`Skill_LN` is the personal, Antigravity-first **Home Repo** (ADR 0022 / ADR 0025) for cross-repository Infor ERP LN development, shared coding standards, and the `skill-ln` / Python automation toolchain.

## Workspace `.agents/` Layout (Single-Source Skill Authority)

- **Canonical Skills**: [erp-ln-progguide](.agents/skills/erp-ln-progguide/SKILL.md) (4GL/DAL/Extension coding guide, bshell APIs, `skill-ln audit-4gl`) and [ln_studio_skill](.agents/skills/ln_studio_skill/SKILL.md) (LN Studio CLI/MCP automation, TDE XML, SCM & Safety Tiers).
- **Modular Rules (`.agents/rules/`)**: Reserved strictly for `repos.local.md` (`always_on`, gitignored **Local Repo Pointer Overlay**) and [repos.example.md](.agents/rules/repos.example.md) (tracked template).
- **Global Slash-Command Sync Cache**: Antigravity `/` discovery reads real directories (not junctions) from `~/.gemini/config/skills/`. Sync after editing `.agents/skills/`:
  ```powershell
  python scripts/run_checks.py --sync-skill
  ```

## Engineering & Tooling Guardrails

- **Domain & ADR Discipline**: Use canonical terms from [GLOSSARY.md](docs/glossary/GLOSSARY.md) and consult [docs/adr/](docs/adr/) before altering shared architecture. Keep generic 4GL/LN rules in `Skill_LN`; child repos store only local schemas, ADRs, and specs.
- **`Audit-Before-Deliver`**: Run `skill-ln audit-4gl <script> [--mode auto|general|dal2|uedll] [--cloud]` and resolve all errors before returning or committing any 4GL, DAL 2, or Extension script.
- **Cross-Runtime Parity & Reuse**: When editing `.agents/skills/ln_studio_skill/tools/*.py` or `rust/`, keep Python and Rust CLI/MCP schemas in parity (`MCP_TOOLS_REFERENCE.md`) and reuse existing helpers (`ensure_label_context_variant`, `compact_tde_xml`, `map_tde_extension_to_type`).
- **Public/Private & Secret Hygiene**: Never commit `.ionapi`, OAuth tokens (`.ln_studio_tokens.json`), customer names, workstation paths, or internal URLs into tracked files or `~/.gemini/config/skills/`.

## Testing & Verification (`Unified Checks Gateway`)

Use Python's built-in `unittest` runner (do NOT invoke `pytest`):

```powershell
# Full gate (syntax, Single-XML layout, Skill & Rule lint, hygiene, parity, Python & Rust tests)
python scripts/run_checks.py

# Full gate + sync canonical skills to ~/.gemini/config/skills/
python scripts/run_checks.py --sync-skill

# Single Python test file or native Rust workspace tests
python -m unittest discover -s .agents/skills/ln_studio_skill/tools/tests -p "test_mcp_tool_execution.py"
Push-Location rust; cargo test --workspace; Pop-Location
```

## Issue Tracker & Domain Docs

- **Issue Tracker**: Specs and local issues live under `.scratch/<feature>/` ([issue-tracker.md](docs/agents/issue-tracker.md)).
- **Domain Docs**: Single-context layout (`docs/glossary/GLOSSARY.md`, `docs/adr/`, `docs/plans/`, [domain.md](docs/agents/domain.md)).
