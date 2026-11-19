---
name: ln_studio_skill
description: Infor LN Studio automation engine (`skill-ln` CLI/MCP and Python tools). Trigger when managing Eclipse workspaces or activities, fetching or checking out/in components via JCA SCM, generating 12-type Single-Line TDE XMLs from schemas, validating labels/cross-references, running deploy-test or post-End-Activity VRC sync (`sync-activity`), inspecting server revision diffs, or delivering Extension Modeler (`tx*`) hooks via guide-and-paste. Route 4GL/DAL coding rules and bshell API lookups to `erp-ln-progguide`.
---

# Infor LN Studio Assistant Skill

Headless automation engine for Infor LN Studio (Eclipse RCP 10.8 Build 0640, Activity-Based Cloud SCM) backed by the native Rust `skill-ln` binary and Python tools (`tools/`).

## Non-Negotiable Invariants & Guardrails

- **`Pre-Fetch-Auth-Gate`**: Run `skill-ln login --status` before any remote call; when renewal fails, stop and surface the OAuth2 URL to the user (`--workspace` is inferred from CWD or `--activity`).
- **`Read-Only-SCM-Guardrail`**: Check out server components via `checkout-component` before editing; keep OS Read-Only flags intact on untouched, reference (`.reference/`), and `tx*` extension files.
- **`Single-Line TDE XML`**: Start all 12 TDE component XMLs with `<?xml version="1.0" encoding="UTF-8" standalone="no"?>` with zero inter-tag newlines outside `<![CDATA[...]]>`, `<expression>`, `<content>`, and `<documentation>`.
- **`Label Context & FieldLabel Parity`**: Use `<LabelVariant><context>` `1` (field), `2` (session/table/index/menu), `10` (FormCommand). `<FormField><fieldLabel>` strips one leading session package prefix on package-local/cloned labels, while inherited `tc` labels and `<FormCommand><descriptionReference>` stay full.
- **`Pre-Commit-Boundary`**: Automate through `deploy-test`, `validate`, and `prepare-end-activity`; `end-activity` is hard-blocked so human developers approve delivery inside LN Studio UI. After partial/full `End Activity`, run `sync-activity` to refresh committed server files without overwriting local `CheckedOut`/`Dirty` edits.
- **`Guide-and-Paste`**: Treat `tx*` Extension Modeler components (`ess`, `est`, `esb`, `esm`, `esr`) as Read-Only in Studio SCM; author locally, audit with `skill-ln audit-4gl`, and extract `#context_on` blocks (`EXT003`) for `ttext1500m000`.

## Workflows & Completion Gates

1. **Auth & Inspection** -> `skill-ln login --status`, `explorer`, `get-component` (Read-Only / `--export-script`), `import-dd-txt` (build `.ln_dd_cache.json` from `Table Definitions/*.txt` & `*-cdf.txt`). *Done when*: token is valid and target artifacts exist in workspace or `.reference/`.
2. **Generate / Edit / Sync Loop** -> `component --spec schema.yaml` / `new-extension` / `checkout-component` -> for embedded `.ses`/`.lib` scripts, run the standard loop `extract` -> edit `.cln` -> `audit-4gl --mode general` -> `inject` (enforces Read-Only check) -> `sync-admin` (non-destructive merge + `.admin.bak`; `--prune` to remove missing entries). *Done when*: `Put`/`CheckIn` (auto-running `DR_Create -> CheckOut` for new objects) returns `SUCCESS`.
3. **Validate & Test** -> `validate <act> [--filter <glob>] [--files <paths>] --strict [--fix] [--online]` and `deploy-test`. *Done when*: Layer 1–4 validation reports **0 errors** (single-line XML, `.admin`, labels/cross-refs, `.ses` layout/parity, 4GL syntax) and `deploy-test` (`compile-only` or `schema-crdd`) compiles cleanly.
4. **Handoff & Post-Commit Sync** -> `prepare-end-activity --activity <a>` (runs `ValidateDevelopmentActivity` + `VSC.executeVSC`) -> user finishes `End Activity` in UI -> `sync-activity`. *Done when*: `prepare-end-activity` reports ready (or `sync-activity` refreshes committed VRCs with 0 errors).

Run `skill-ln --help` for full subcommand options.

## Branching Reference Pointers

Open a reference file only when its branch applies:

| Workflow Branch | Authoritative Reference |
|---|---|
| **CLI Options & Recipes (62 subcommands)** | [CLI Reference Guide](references/CLI_REFERENCE.md) |
| **Stdio MCP Tools (26 tools: 4 consolidated + 22 detailed)** | [MCP Tools Reference](references/MCP_TOOLS_REFERENCE.md) |
| **Multi-Component `schema.yaml` Spec** | [Authoring Schema Guide](references/AUTHORING_SCHEMA_GUIDE.md) |
| **Single-XML TDE Facets (12 component types)** | [Component XML Schema](references/COMPONENT_XML_SCHEMA.md) |
| **DAL 2 & UI Session 4GL Details** | [DAL 2 Hooks Guide](references/DAL2_HOOKS_GUIDE.md), [UI Script Guide](references/UI_SCRIPT_GUIDE.md) |
| **4GL Coding Rules & Bshell APIs** | [Programmer's Guide Skill](../erp-ln-progguide/SKILL.md) |
