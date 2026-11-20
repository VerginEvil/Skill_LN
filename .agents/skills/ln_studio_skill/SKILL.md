---
name: ln_studio_skill
description: Infor LN Studio automation (`skill-ln` CLI/MCP). Use for Eclipse workspaces/activities, JCA SCM checkout/checkin, Single-Line TDE XML generation, validation, deploy-test, VRC sync, revision diff, or `tx*` Extension CLI packaging. Route 4GL/DAL coding rules and bshell APIs to `erp-ln-progguide`.
---

# Infor LN Studio Assistant Skill

Headless automation engine for Infor LN Studio (Eclipse RCP 10.8 Build 0640, Activity-Based Cloud SCM) via the native `skill-ln` CLI and Stdio MCP server. Run `skill-ln --help` or `skill-ln <subcmd> --help` for live options.

## Decision Tree

- **Standard component edit**: `checkout-component` -> `extract` / edit `.cln` / `audit-4gl` / `inject` -> `validate` -> `deploy-test`.
- **New component(s)**: define `schema.yaml` -> `component --spec schema.yaml` -> `sync-admin`.
- **Extension `tx*` (`ess`/`est`/`esb`/`esm`/`esr`)**: `Guide-and-Paste` (author locally + `audit-4gl` + `extension-hooks`; keep Studio SCM files Read-Only).
- **Post-`End Activity` refresh**: run `sync-activity` to pull committed server VRCs without overwriting local `CheckedOut`/`Dirty` edits.

## Tiered Safety Gate

- **Tier 1 — Read-Only / Local** (`login --status`, `explorer`, `get-component`, `validate`, `diagnose`, `audit-4gl`, `revisions`, `diff-component`, `import-dd-txt`): Execute directly. Emit `Pre-Fetch-Auth-Gate` banner (Object, Workspace/Env, Project/Activity, Mode) before remote calls; if silent token renewal fails, surface the OAuth2 login URL to the user.
- **Tier 2 — Dev/Test Mutating** (`checkout-component`, `checkin-component`, `deploy-test --mode compile-only`, `new-activity`, `component`, `inject`, `sync-admin`, `sync-activity`, `prepare-end-activity`): Announce target workspace, activity, and component beforehand. Uphold `Read-Only-SCM-Guardrail` by keeping OS Read-Only flags intact on untouched, `.reference/`, and `tx*` files.
- **Tier 3 — High-Risk / Destructive / `PRD` (Stop & Confirm)**: `deploy-test --mode schema-crdd`, `uncheckout-component`, `clean-activity`, `clean-components`, `move-components`, `sync-admin --prune`, or **any write operation on a `PRD` environment** -> halt and obtain explicit user confirmation before executing.
- **Hard-Blocked (`Pre-Commit-Boundary`)**: `end-activity` (`CloseTask` / `FinalizeActivity`) is unconditionally blocked so human engineers approve final delivery in LN Studio UI.

## Core XML Invariants & Workflow Completion Gates

- **`Single-Line TDE XML`**: Begin all 12 TDE component XMLs with `<?xml version="1.0" encoding="UTF-8" standalone="no"?>` with zero inter-tag newlines outside `<![CDATA[...]]>`, `<expression>`, `<content>`, and `<documentation>`.
- **`Label Context & FieldLabel Parity`**: Use `<LabelVariant><context>` `1` (field), `2` (session/table/index/menu), `10` (FormCommand). `<FormField><fieldLabel>` strips one leading session package prefix on package-local/cloned labels; inherited `tc` labels and `<FormCommand><descriptionReference>` stay full.
- **Completion Gates**:
  1. *Auth & Inspection*: `login --status` valid and target objects fetched into workspace or `.reference/`.
  2. *Generate / Edit / Sync*: `Put`/`CheckIn` (auto-running `DR_Create -> CheckOut` for new objects) returns `SUCCESS`.
  3. *Validate & Test*: `validate <act> [--filter <glob>] [--files <paths>] --strict [--fix] [--online]` reports **0** Layer 1–4 errors and `deploy-test` compiles cleanly.
  4. *Handoff & VRC Sync*: `prepare-end-activity` reports ready -> human completes `End Activity` in UI -> `sync-activity` refreshes committed VRCs with 0 errors.

## Branching Reference Pointers

| Workflow Branch | Authoritative Reference |
|---|---|
| **CLI Options & Recipes** | [CLI Reference Guide](references/CLI_REFERENCE.md) |
| **Stdio MCP Tools** | [MCP Tools Reference](references/MCP_TOOLS_REFERENCE.md) |
| **Multi-Component `schema.yaml` Spec** | [Authoring Schema Guide](references/AUTHORING_SCHEMA_GUIDE.md) |
| **Single-XML TDE Facets (12 types)** | [Component XML Schema](references/COMPONENT_XML_SCHEMA.md) |
| **LN Studio Workbench UI & Views** | [Official Studio Guide Index](references/STUDIO_INDEX.md) |
| **4GL, DAL 2, UI & Bshell APIs** | [Programmer's Guide Skill](../erp-ln-progguide/SKILL.md) |
