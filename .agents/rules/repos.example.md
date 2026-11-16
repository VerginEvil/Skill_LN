# Local Repo Pointer Overlay Template

Copy this file to `.agents/rules/repos.local.md` (gitignored) and add `always_on` frontmatter so Antigravity automatically loads your private workspace pointers at session start without exposing confidential paths or internal URLs in Git.

## Example Format

```markdown
---
trigger: always_on
---

# Local Repository & Workspace Pointers

## Active Customization Repositories

| Repo | Local Path | Remote / Origin | Focus & Hints |
|---|---|---|---|
| `CUST_A` | `C:\path\to\CUST_A` | `local-only` | Ticket folders (`DV*`), DAL/Extensions, local `.scratch/` |
| `CUST_B` | `C:\path\to\CUST_B` | `http://git.internal/group/cust-b.git` | `Dev` branch; repo-specific table schemas in `.agent/rules/tables.md` |

## Infor LN Studio Workspaces & Install Tree

- **Eclipse Workspace**: `C:\path\to\workspace_lnstudio` (Environments: `ENV_TST`, `ENV_TRN`)
- **LN Studio Install**: `D:\LN Studio\InforLNStudio_10_8_0`
```

## Conventions

- **Public/Private Isolation**: Keep `.agents/rules/repos.local.md` gitignored. Never copy customer names, local paths, internal GitLab URLs, or `.ionapi` credentials into tracked files.
- **Per-Repo Hints**: Note active branch names, directory structure (`Sessions/`, `Libraries/`, `Reports/`, `Extensions/`, `DV*`), and any repo-specific `.agent/rules/` or `docs/` files.
