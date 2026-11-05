# Specification: LN Studio Skill Knowledge Enrichment & Self-Contained Toolchain

## Problem Statement

Engineers and AI agents doing Infor LN development inside LN Studio (Eclipse RCP, Activity-based development with SCM) currently get limited help from the Studio assistant skill. The skill knows how to generate table/session metadata, synchronize 4GL sources, sync the SCM cache, and read compiler diagnostics, but it lacks the underlying Studio usage knowledge: how installation and connectivity are set up, how the Activity lifecycle and SCM actions work, how the development procedure (verify, run, debug) is performed, and how the workbench editors, wizards, dialogs, perspectives, and views are used. As a result the agent can run the toolchain but cannot guide the user through Studio itself, cannot explain what an Activity, the SCM cache, or the problem markers mean, and cannot recover when the workspace state disagrees with the toolchain. Separately, the toolchain lives outside the skill directory, so every copy of the skill into an agent's skill folder silently loses the executables the skill text refers to.

## Solution

Enrich the Studio assistant skill with usage knowledge distilled from the Application Development Guide (App Dev first; Integration Guide deferred to Phase 2), and relocate the entire automation toolchain inside the skill directory so a single copied folder is a working skill:

1. Relocate the toolchain (master orchestrator CLI, generators, synchronizers, diagnostics readers, workspace resolver, bridge, schema validator, converters, indexers, validators, Java helper plus binary library, and the unit test suite) into the skill, refactoring internal references to resolve from the skill root, so all documented commands keep working from the new home.
2. Ingest the 12 chapters of the Application Development Guide into a studio guide reference section with a master studio index, prioritizing installation and connectivity, Activity-based development and SCM, the development procedure including verification/debugging, wizards and dialogs, multipage editors, and the script editor, with lighter coverage of InContext modeling, limitations, perspectives, views, and the project server.
3. Wire the skill for token-efficient use: a stdlib-only full-text search script, a regenerated every-page index, and a rewritten skill definition with a task-to-entry-point navigation table and closed-loop recipes (author schema, generate, sync SCM cache, build, diagnose, fix, repeat).
4. Validate end to end and record decisions: the relocated test suite passes, skill validation reports zero broken links or orphan entries, representative searches return ranked hits, and the full pipeline runs against a real activity; architectural decisions go into a new ADR and Studio terms go into the domain glossary.

## User Stories

1. As an LN developer, I want to set up connectivity and the workspace correctly, so that my activities resolve instead of failing with missing-workspace errors.
2. As an LN developer, I want to understand the Activity lifecycle (open, clean, recover, reassign, end, link run configurations), so that I never lose work to a stale activity state.
3. As an LN developer, I want to know when SCM applies (project VRC versus application) and which CM actions to use, so that component registration matches what the toolchain expects.
4. As an LN developer, I want a single pipeline that validates my schema, generates table and session metadata, syncs the SCM cache, and builds, so that I do not click through Studio manually.
5. As an LN developer, I want to inject my 4GL source into workspace metadata and extract it back, so that my repository copy stays the source of truth.
6. As an LN developer, I want to resynchronize the SCM cache after generating files on disk, so that Studio stops reporting phantom missing components.
7. As an LN developer, I want line-accurate compiler diagnostics after a build, so that I can fix the exact failing source line.
8. As an AI agent, I want a closed-loop recipe (generate, sync, build, diagnose, fix, repeat), so that I can drive compilation to zero errors autonomously.
9. As an LN developer, I want guidance on verifying components and handling warnings versus errors, so that I know what blocks a build.
10. As an LN developer, I want to run and debug sessions (suspend, resume, step, inspect, breakpoints, expressions), so that I can diagnose runtime behavior, not just compile errors.
11. As an LN developer, I want to know which wizard or dialog to use for each task (activity, component creation, domain, label, function, browse actions), so that I stop guessing in the workbench.
12. As an LN developer, I want to understand multipage editors and the script editor (assistance, navigation, limitations), so that metadata edits do not corrupt generated artifacts.
13. As an LN developer, I want to know the documented Studio, debugger, and Web UI limitations for this release, so that I do not file or chase unfixable issues.
14. As an LN developer, I want orientation on perspectives, views, and the project server, so that I can navigate the workbench and deliver components.
15. As an AI agent, I want a full-text search over the Studio guide with scoped directories, so that I answer "how do I ..." without reading whole manuals.
16. As an AI agent, I want an every-page index and a master studio index, so that I can jump from a known topic name to the exact reference page.
17. As an AI agent, I want the skill definition to tell me the entry point for each task, so that I never invoke the wrong subcommand.
18. As a repository maintainer, I want automated skill validation, so that broken links, missing index entries, or malformed pages fail fast.
19. As a repository maintainer, I want the toolchain relocation to keep every documented command working, so that existing automation and rules do not silently break.
20. As a skill consumer, I want one copied folder to contain knowledge plus executables, so that installing the skill never ships text without tools.

## Implementation Decisions

- Relocation is an atomic clean break: the toolchain moves inside the skill and every consumer reference (skill definition, readme, agent rules, pipeline and index tooling, ignore rules) is migrated in the same slice; no compatibility shim is left behind. Expand-contract was considered and explicitly rejected by the user.
- Internal coupling is refactored from location-dependent references to skill-root resolution: the orchestrator and sibling modules resolve each other and the workspace configuration relative to their own location, so the skill works regardless of where the containing repository is checked out.
- The existing command surface is frozen: subcommand names and their semantics (generate, inject, extract, sync, diagnose, build, full pipeline with dry-run and skip-build variants) do not change; only their home changes.
- Knowledge ingestion follows the established converter precedent from the programmer's-guide track: strip form feeds and recurring header/footer/page-number artifacts, detect chapter and section headings into clean heading levels, preserve procedure steps and lists, emit one page per chapter with stable names, and write everything as UTF-8 Markdown with skill-relative links.
- The studio guide covers all 12 Application Guide chapters with deliberate depth weighting: full detail for installation/connectivity, Activity/SCM, development procedure and debugging, wizards/dialogs, multipage editors, and the script editor; summary treatment for InContext modeling, limitations, perspectives, views, and the project server.
- Discovery follows the programmer's-guide pattern at the skill level: scoped full-text search (studio guide scope plus an all scope), a group filter, a list-groups mode, ranked file-plus-snippet output, stdlib only, safe on all supported operating systems.
- The skill definition is rewritten around tasks, not tools: a task-to-entry-point table plus three end-to-end recipes (new table plus session from scratch, business rules in DAL sources, closed-loop autonomous debugging), with the pinned Studio release stated and live-workspace scanning explicitly permitted including real activity names.
- No schema or data-model changes: the declarative authoring schema accepted by the generators is unchanged.
- This spec respects the accepted skill-update ADR and the domain glossary; a follow-up ADR records the relocation plus ingestion decisions, and new Studio terms (Activity, SCM cache, problem markers, workbench, project VRC, pinned build identity) extend the glossary rather than redefining existing entries.

## Testing Decisions

- A good test asserts external behavior only (commands exit codes and human-readable output, files exist with positive size and valid encoding, index entries resolve, search returns ranked hits, validation passes) and never asserts on private helpers inside converters or generators.
- Primary seam is the highest existing CLI seam: the orchestrator subcommands in dry-run and diagnose modes, the skill validator, and the search script. A secondary seam is converter output integrity (chapter pages exist, no form feeds, index covers every page). The relocated unit suite runs purely as regression.
- Modules under test: the relocated orchestrator and its subcommand handlers; the workspace resolver and SCM synchronizer; the generators and bidirectional synchronizer via round-trip behavior; the diagnostics reader against fixture and live markers; the new guide converter via output integrity; the regenerated index and search via representative queries (connectivity, Activity clean/recover, SCM cache sync, problem markers, breakpoints); the validator via zero-problem runs for the skill.
- Prior art: the existing toolchain unit suite, the skill validator's index-plus-link checks, and the programmer's-guide search script's ranked-hit behavior, all reused rather than reinvented.

## Out of Scope

- Ingesting the Integration Development Guide (business interface implementations, BOD modeling, hook reference, event publishing) — tracked as Phase 2 with an explicit non-duplication boundary against the existing extensibility reference.
- Changing generator output semantics or the authoring schema; altering Studio, Eclipse, or server binaries; touching live production activities beyond read-only diagnostics and explicitly requested pipeline runs.
- Multi-release support beyond the pinned Studio build; cloud-versus-on-premises behavioral differences are documented only as stated in the source guide.
- Rewriting the programmer's-guide skill or its indices except where shared pipeline/validator tooling needs a new skill target.

## Further Notes

- Source identity: Application Development Guide, cloud and on-premises edition, September 2025, twelve chapters, roughly three quarters of a megabyte and fourteen thousand lines of source text.
- Pinned runtime: LN Studio 10.8 build 0640 (April 2026 tree); the example workspace contains eight activities and live scanning of installation plugins, workspace metadata, SCM caches, and problem markers is permitted.
- Glossary and ADR linkage from the prior track remain canonical; new terms must use their vocabulary and the new ADR must record the ingestion depth weighting, the atomic-relocation choice, and the Phase 2 boundary.
