---
name: ln_studio_skill
description: Infor LN Studio automation engine for managing Eclipse workspaces, remote SCM check-out/check-in, declarative component XML generation (tables, sessions, domains, menus), deploy-test verification, and Extension Modeler guide-and-paste delivery. Use when managing LN Studio activities, generating component XMLs from schemas, interacting with Infor LN servers via JCA/MCP, running activity validation, or inspecting server revision diffs. Do NOT use for general 4GL/DAL coding rules, SQL query optimization, or bshell runtime API lookups (use erp-ln-progguide instead).
---

# Infor LN Studio Assistant Skill

Automation engine for Infor LN Studio (Eclipse RCP, Activity-Based SCM) and declarative component generation.

## Non-Negotiable Guardrails

- `Pre-Fetch-Auth-Gate`: Verify OAuth2 tokens (`login --status`) and emit a user alert before fetching, downloading, or inspecting remote components.
- `Read-Only-SCM-Guardrail`: Checked-in components have OS Read-Only flags set. Never remove flags manually; always check out via `checkout-component`.
- `Pre-Commit-Boundary`: Automate up to `deploy-test` and `prepare-end-activity`. `end-activity` is hard-blocked to require human delivery approval.
- `Guide-and-Paste`: Extension Modeler components (`tx*`) cannot be checked out or edited in Studio. Author locally, verify offline, and deliver hook-by-hook for LN UI (`ttext1500m000`).

## Core Procedural Workflows

1. **`Pre-Fetch-Auth-Gate`: Environment Auth & Remote Inspection/Fetch**:
   - Verify token: `python tools/ln_component_builder.py login --workspace <ws> --status`
   - Inspect components: `python tools/ln_component_builder.py explorer --type <t> [--filter <pat>]`
   - Fetch component/script: `python tools/ln_component_builder.py get-component --type <t> --name <n> [--export-script <path>]`

2. **`Read-Only-SCM-Guardrail` & `Pre-Commit-Boundary`: SCM & Deploy-Test**:
   - Check out: `python tools/ln_component_builder.py checkout-component --type <t> --name <n> --activity <a>`
   - Test changes: `python tools/ln_component_builder.py deploy-test --type <t> --name <n> --activity <a> [--mode compile-only|schema-crdd]`
   - Verify activity: `python tools/ln_component_builder.py prepare-end-activity --activity <a>`

3. **`Single-XML TDE Layout`: Declarative Component Generation & Fix**:
   - Scaffold from schema: `python tools/ln_component_builder.py component --spec schema.yaml [--output-dir <path>]`
   - Synchronize & repair: `python tools/ln_component_builder.py validate <activity_path> --fix`
   - Synchronize SCM cache: `python tools/ln_component_builder.py sync-admin --activity <act>`

4. **`Guide-and-Paste`: Extension Modeler Delivery**:
   - Scaffold local script: `python tools/ln_component_builder.py new-extension --type <table|session> --target <comp>`
   - Verify offline: `python tools/ln_component_builder.py check-script <ext_file> --strict`
   - Deliver hook blocks: Output clean code blocks for user to paste into `ttext1500m000` (warn never to check out in Studio).

## Branching Reference Pointers

Open dedicated reference files only when branching into that specific workflow:

| Workflow Branch | Reference Document |
|---|---|
| **CLI Command Lookup (50+ subcommands)** | [CLI Reference Guide](references/CLI_REFERENCE.md) |
| **Stdio MCP Tools (4 consolidated / 21 detailed)** | [MCP Tools Reference](references/MCP_TOOLS_REFERENCE.md) |
| **Multi-Component `schema.yaml` Authoring** | [Authoring Schema Guide](references/AUTHORING_SCHEMA_GUIDE.md) |
| **Single-XML TDE XML Schema (12 types)** | [Component XML Schema](references/COMPONENT_XML_SCHEMA.md) |
| **DAL 2 Object & Property Hook Details** | [DAL 2 Hooks Guide](references/DAL2_HOOKS_GUIDE.md) |
| **UI Session 4GL Script Details** | [UI Script Guide](references/UI_SCRIPT_GUIDE.md) |
| **4GL Coding Recipes & Cookbooks** | [Programmer's Guide Skill](../erp-ln-progguide/SKILL.md) |
