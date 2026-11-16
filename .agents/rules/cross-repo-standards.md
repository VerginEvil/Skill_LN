---
trigger: always_on
---

# Cross-Repository Engineering Standards

Shared engineering guardrails applied across the `Skill_LN` Home Repo and all child customization repositories.

## 1. Domain & Architecture Discipline

- **Glossary Vocabulary**: Use the canonical terms defined in `docs/glossary/GLOSSARY.md` when naming concepts in specs, issues, ADRs, tests, and code.
- **ADR Alignment**: Consult relevant ADRs in `docs/adr/` before altering shared architecture. Flag any intentional contradiction explicitly rather than overriding silently.
- **Single Source of Truth**: Keep generic Infor LN / Baan 4GL / AFS rules in `Skill_LN` (`.agents/rules/` and `.agents/skills/`). Child repositories should only store repo-specific table schemas, local ADRs, and feature specs.

## 2. Static Verification Gate (`Audit-Before-Deliver`)

- Before returning, presenting, or committing any Baan 4GL, DAL 2, or Extension Modeler script across any repository, run the offline auditor:
  ```powershell
  skill-ln audit-4gl <target_script> [--mode dal2|uedll|general] [--cloud]
  ```
  (or `python .agents/skills/erp-ln-progguide/scripts/audit_4gl.py <target_script> [--mode dal2|uedll|general] [--cloud]`).
- Resolve all syntax (`SYN`), DAL (`DAL`), Extension boundary (`EXT`), datatype/schema (`DMN`/`TBL`/`STR`), and Cloud governance (`CLD`) errors before delivery.

## 3. Secret & Credential Hygiene

- Never copy `.ionapi` files, OAuth2 tokens (`.ln_studio_tokens.json`), or tenant credentials into `.agents/skills/`, global skill directories (`~/.gemini/config/skills/`), or git-tracked files.
- Never embed customer names, local workstation paths, or internal GitLab URLs into tracked files inside `Skill_LN`; keep them exclusively in `.agents/rules/repos.local.md` (gitignored).
