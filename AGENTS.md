# Skill_LN — Home Repo Steering & Development Guidelines

`Skill_LN` is the personal, Antigravity-first **Home Repo** (ADR 0022) for cross-repository Infor ERP LN development, shared coding standards, and the `skill-ln` / Python automation toolchain.

## Workspace `.agents/` Layout

- **Canonical Skills**: `.agents/skills/erp-ln-progguide/` (4GL Programmer's Guide & static auditor) and `.agents/skills/ln_studio_skill/` (Infor LN Studio automation, XML generators, SCM & MCP server).
- **Modular Rules**: `.agents/rules/`
  - `cross-repo-standards.md` (`always_on`): ADR/glossary discipline, `Audit-Before-Deliver` (`audit_4gl` / `skill-ln audit-4gl`), and credential hygiene.
  - `repos.local.md` (`always_on`, gitignored): **Local Repo Pointer Overlay** with private customer repository paths, Git remotes, and workspace hints (see `.agents/rules/repos.example.md` for the tracked template).
  - `infor-ln-coding.md` (`model_decision`): Baan 4GL, DAL 2, UI scripts, and Extension Modeler (`EXT001`–`EXT003`) rules.
  - `ln-studio-workflow.md` (`model_decision`): LN Studio CLI/MCP workflows, `Single-XML TDE Layout`, and `Pre-Fetch-Auth-Gate`.

## Global Slash-Command Sync Cache

Antigravity `/` slash-command discovery reads real directories (not Windows directory junctions) from `~/.gemini/config/skills/`. After editing anything under `.agents/skills/`, synchronize the **Global Slash-Command Sync Cache** via:

```powershell
python scripts/run_checks.py --sync-skill
```

## Testing & Verification (`Unified Checks Gateway`)

Always use Python's built-in `unittest` runner (do NOT invoke `pytest` as it is not installed in the Windows Python environment):

```powershell
# Run unified checks (syntax compilation, Single-XML TDE Layout, Skill Markdown Lint Gate, Python & Rust tests, drift check)
python scripts/run_checks.py

# Run checks and sync canonical skills to ~/.gemini/config/skills/
python scripts/run_checks.py --sync-skill

# Run a single test file
python -m unittest discover -s .agents/skills/ln_studio_skill/tools/tests -p "test_mcp_tool_execution.py"

# Run native Rust workspace tests (run inside rust/ to use rust/.cargo/config.toml)
Push-Location rust; cargo test --workspace; Pop-Location
```

## Agent Skills & Documentation

- **Issue Tracker**: Specs and local issues live under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.
- **Domain Docs**: Single-context layout (`docs/glossary/GLOSSARY.md`, architecture decision records under `docs/adr/`, plans under `docs/plans/`). See `docs/agents/domain.md`.
- **Public/Private Boundary**: Never commit customer repository names, local workstation paths, internal GitLab URLs, or `.ionapi` / token credentials into tracked files; keep them strictly in gitignored overlays (`.agents/rules/repos.local.md`) or gitignored workspace dirs (`knowledge_docs/`, `.scratch/`).
