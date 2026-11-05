# Changelog

All notable changes to the **Skill_LN** repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-05

### Added

#### Core Pillar 1: Infor LN Studio Automation & Stdio MCP Skill (`ln_studio_skill`)
- **Native Stdio MCP Server (`ln_studio_mcp.py`)**: 16 JSON-RPC tools with unified tool envelope, input schemas, and error taxonomy for AI agents (Antigravity, Cursor, Claude Code).
- **Headless JCA 1.6 Bridge**: Pure Python and Bring-Your-Own-Jar (BYOJ) bridge communicating with Infor LN Enterprise Server via Business Data Entity (BDE) XML protocol without running Eclipse GUI.
- **Component Generators**: Automated generation for 12 Infor LN Studio component archetypes (Tables, Sessions, Scripts, Menus, Domains, Labels, Messages, Questions, Functions, Additional Files, Reports, MMT Controllers).
- **Single-XML TDE Layout Guardrail**: Automatic enforcement and repair preventing XML fragment split corruptions.
- **Pre-Commit SCM Engine**: Authentic check-in/check-out lifecycle with read-only OS file locks, pre-put script merge protection, and change conflict prevention.
- **Authentication**: CloudSuite OAuth2 (`.ionapi`) with out-of-band (OOB) browser login and local encrypted token cache.

#### Core Pillar 2: Programmer's Guide, Dev Tools & Audit Engine (`erp-ln-progguide`)
- **Knowledge Base**: 5,700+ pages of Infor LN 10.8 (Build 0640) technical reference documentation converted to grep-friendly Markdown.
- **Function Index**: 2,266 bshell and 4GL functions indexed with cloud trust ratings and documentation links.
- **Standalone 4GL Audit Engine (`audit_4gl.py`)**: Zero-dependency static analyzer enforcing 20+ lint rules, cloud governance checks, DAL/UI separation of concerns, and Extension Modeler standards (`EXT001`, `EXT002`).
- **Architecture Cookbooks**: 6 best-practice guides covering DAL 2, Extension Modeler, Baan SQL optimization, and CloudSuite extensibility.

#### Core Pillar 3: VS Code Extension Assets (`export/vscode`)
- **4GL Syntax Grammar**: TextMate grammar (`baan4gl.tmLanguage.json`) supporting Infor LN 4GL keywords, preprocessor directives, and embedded SQL.
- **Code Snippets & Completions**: 19 official 4GL templates, DAL hooks, and function signature auto-completions.

#### Repository & CI/CD Toolchain
- **GitHub Actions Workflows**: Automated syntax, layout, and hermetic unit testing pipeline (`.github/workflows/ci.yml`).
- **Release Automation (`.github/workflows/release.yml`)**: Automated build and distribution of ZIP packages (`erp-ln-progguide.zip`, `ln_studio_skill.zip`, `skill-ln-vscode.zip`) on tag push.
- **Packaging Utility (`scripts/package_release.py`)**: Standalone cross-platform distribution bundler.
- **Domain Documentation**: Reorganized architecture layout with `docs/glossary/GLOSSARY.md`, `docs/plans/`, and ADR history (`0001` - `0015`).
- **Hardened Security**: `.gitignore` audit preventing leak of Infor credentials, token caches, and proprietary offline manuals.
