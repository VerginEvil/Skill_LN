# Plan: Restructure `Skill_LN` for The Home Repo Pattern & Antigravity Layout

- **Status**: Approved (Round 3)
- **ADR**: [`docs/adr/0022-home-repo-pattern-and-antigravity-layout.md`](../adr/0022-home-repo-pattern-and-antigravity-layout.md)
- **Spec**: [`.scratch/home-repo-restructure/spec.md`](../../.scratch/home-repo-restructure/spec.md)
- **Branch**: `feat/home-repo`

---

## 1. Inventory & Destination Table

| Item | Current Location | Bucket | Destination / Action |
|---|---|---|---|
| `erp-ln-progguide`, `ln_studio_skill` | `Skill_LN/{erp-ln-progguide, ln_studio_skill}/` | `shared` | Move to `Skill_LN/.agents/skills/{erp-ln-progguide, ln_studio_skill}/`; keep release ZIP arcnames unchanged in `scripts/package_release.py` |
| `erp-ln-progguide`, `ln_studio_skill` (Antigravity `/` cache) | `~/.gemini/config/skills/` | `duplicate` (harness cache) | Keep as real-directory sync target from `.agents/skills/` via `python scripts/run_checks.py --sync-skill` (Antigravity `/` requires real directories, not junctions) |
| `erp-ln-progguide`, `ln_studio_skill` (stale/duplicate) | `~/.gemini/skills/`, `~/.agents/skills/` | `duplicate` | Delete stale copies from `~/.gemini/skills/` and duplicate copies from `~/.agents/skills/` |
| `knowledge_docs` + tenant `.ionapi` | `~/.gemini/config/skills/knowledge_docs/`, `~/.agents/skills/knowledge_docs/`, `Skill_LN/knowledge_docs/` | `duplicate` / non-skill + secret | Delete from `~/.gemini/config/skills/` and `~/.agents/skills/`; keep only `Skill_LN/knowledge_docs/` (gitignored) |
| Installed & marketplace skills (`.skill-lock.json`, `superpowers`, `caveman*`, `ponytail*`, `cavecrew`, `pstack`, `stitch`, `reverse-engineer-anything`, `plugins/*`) | User-level skill/plugin dirs | `installed` | Leave installed as-is |
| `thai-natural-writing` | `~/.gemini/config/skills/thai-natural-writing/`, `~/.agents/skills/thai-natural-writing/` | `shared` (non-LN personal) | Keep in `~/.gemini/config/skills/` (do not move into `Skill_LN`) |
| `infor_ln.md` | `Skill_LN/.antigravity/rules/infor_ln.md` | `shared` | Split into `.agents/rules/{infor-ln-coding.md, ln-studio-workflow.md, cross-repo-standards.md}` and remove `.antigravity/` |
| Home Repo steering | `Skill_LN/AGENTS.md` | `shared` | Update `AGENTS.md` for Home Repo steering + add 1-line `CLAUDE.md` (`@AGENTS.md`) |
| Private repo pointers | Scattered | `local-only` | Create `.agents/rules/repos.local.md` (`trigger: always_on`, gitignored) + `.agents/rules/repos.example.md` (tracked) |
| Child repo duplicate/empty rules | `<child-repo>/.agent/rules/{agents.md, afs.md, skill.md}` | `duplicate` / empty | On a clean local branch (preserving dirty files), remove `agents.md`, `afs.md`, `skill.md`; keep `tables.md` |
| Child repo-specific docs | Child customization repositories | `repo-specific` | Keep in respective child repos |
| Tooling, Rust & test path refs | `scripts/*`, `rust/crates/*`, `ln_studio_skill/tools/*`, `README.md` | `tooling` | Update to `.agents/skills/` (with root fallback in Rust `ln-kb`/`ln-verify` for standalone binary) |

## 2. Active Repositories Covered by `repos.local.md`

Private local paths, customer repository names, and internal GitLab URLs are kept exclusively in `.agents/rules/repos.local.md` (gitignored), covering:
- 8 active 2026 customization and supporting repositories (6 Infor LN customization repos, 1 shared DLL repo, 1 chatbot app repo)
- 2 local Infor LN Studio paths (Eclipse LN Studio workspace directory and Infor LN Studio 10.8 Build 0640 installation directory)
