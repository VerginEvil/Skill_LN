# ADR 0023: Label XML Parity, Activity-Based Cloud SCM Hardening, and Post-End-Activity VRC Sync

- **Status**: Accepted
- **Date**: 2026-11-18
- **Target Skills**: `ln_studio_skill` (Python tools + Native Rust `skill-ln`)
- **Specification**: `.scratch/ln-studio-skill-hardening/spec.md`
- **Prior ADRs**:
  - [`docs/adr/0007-headless-jca-connectivity-scm-and-mcp-server.md`](0007-headless-jca-connectivity-scm-and-mcp-server.md) *(Preserved: Pre-Commit SCM Boundary — hard-blocking `EndActivity` / `CloseTask`)*
  - [`docs/adr/0010-pre-fetch-server-authentication-guardrail-and-user-alert.md`](0010-pre-fetch-server-authentication-guardrail-and-user-alert.md) *(Extended: Silent OAuth2 refresh parity & fail-fast workspace inference)*
  - [`docs/adr/0012-rea-100-percent-ln-studio-parity-and-daemon-architecture.md`](0012-rea-100-percent-ln-studio-parity-and-daemon-architecture.md) *(Extended: Byte-exact `CMComponentProperties` single-line XML & `DR_Create` lifecycle)*
  - [`docs/adr/0018-lean-skill-architecture-and-progressive-disclosure.md`](0018-lean-skill-architecture-and-progressive-disclosure.md) *(Preserved: Keep `SKILL.md <= 80` lines; document new CLI/MCP commands in `references/`)*
  - [`docs/adr/0021-native-rust-skill-ln-single-binary-architecture.md`](0021-native-rust-skill-ln-single-binary-architecture.md) *(Extended: Full Python/Rust differential parity across auth, SCM, validator, and XML engines)*

---

## 1. Context & Problem Statement

Production usage of `ln_studio_skill` on Activity-Based Cloud SCM projects uncovered five classes of parity gaps and edge-case defects between the toolchain and Eclipse Infor LN Studio 10.8 (build 0640):

1. **Label Prefixing, Context & Pretty-Print XML Crashes**:
   - In `<DR_Controller>` sessions, `<FormField><fieldLabel>` strips the current session package prefix for package-local labels (e.g., `<pkg>inr.dsca` -> `inr.dsca`), whereas `<FormCommand><descriptionReference>` requires the full label name. Cross-package labels (e.g., `wh.*` referenced in a custom package session) are not automatically inherited unless defined in the session's package or an inherited base package (`tc`).
   - `<LabelVariant><context>` was hardcoded to `3`, causing `DR_Controller.Put` rejections when `FormCommand` labels lacked `<context>10</context>`.
   - Eclipse `CMComponentProperties(IFile)` casts every direct child of the XML root to `Element` without checking `Node.ELEMENT_NODE`, throwing `ClassCastException` whenever any TDE component XML contains inter-tag whitespace or newlines.
2. **OAuth2 Token Refresh & Default Workspace Mismatch**:
   - Native Rust `skill-ln login --status` reported near-expiry tokens without executing Tier 2 `refresh_token` renewal, unlike Python `ln_env_manager.py`.
   - Omitting `--workspace` fell back to a hardcoded default workspace instead of inferring from `--activity` or failing fast when ambiguous.
3. **False `NON_SCM` Mode, `DR_Create` Lifecycle & `.admin` Drift**:
   - Projects configured with `ApplicationUsesSCM=no` alongside active `labelUUID` / `taskName` / `EXT*_dev` Activity metadata in `properties.index` were misclassified as `NON_SCM`, silently skipping server BDE calls.
   - Newly created components on the server require `DR_Create` (followed by `CheckOut` -> `Put`/`CheckIn` so Eclipse `End Activity` recognizes them).
   - `build_checkout_payload` / callers could alter `comp_name` casing, and Rust `sync-admin` overwrote existing `.admin` flags and ignored layout/exclusion rules.
4. **Post-End-Activity VRC Stale State**:
   - After partial or full `End Activity` promotion on the server (e.g., from an activity VRC to the base extension VRC), local component XMLs and `.admin` retained the older activity VRC and `isEverCheckedIn` state until refreshed.
5. **BDE Query & VSC Parameter Gaps**:
   - `StudioComponent.GetBrowseList` requires `context_xml` for activity-scoped VRC resolution and SQL `%` wildcards instead of `*`.
   - `VSC.executeVSC` omitted the project's package combination and (in Rust) passed an empty `conid`, while `prepare-end-activity` skipped `executeVSC` execution.

---

## 2. Decisions

1. **CDATA-Safe Single-Line TDE XML Invariant**:
   - All 12 TDE component XML generators, validator `--fix` writers, and BDE disk writers (`get`, `checkout`, `DR_Create`, `sync-activity`) MUST emit `<?xml version="1.0" encoding="UTF-8" standalone="no"?>` followed by single-line XML with inter-tag whitespace stripped while preserving `<![CDATA[...]]>` payloads verbatim.
   - Layer 2 validation (Python and Rust) verifies single-line TDE XML compliance.
2. **Package-Aware Label Prefixing, Context Parameterization & Cross-Package Probing**:
   - `<FormField><fieldLabel>` strips the session's package prefix for package-local and cloned cross-package labels while preserving inherited base-package (`tc`) labels; `<FormCommand><descriptionReference>` always emits the full label name.
   - `LabelVariant <context>` is parameterized (`1` field, `2` session/table, `10` FormCommand). When an editable local label in the active activity is reused as a `FormCommand`, generators/`--fix` append a `<context>10</context>` variant; Read-Only or externally locked labels emit an actionable error/warning instead of mutating protected files.
   - Layer 3 validation stays **offline by default** (checking activity `.lbl` files plus `<workspace>/.reference/label/` and fixing Rust child-element `<descriptionReference>` collection), with `--online` probing `StudioComponent.GetBrowseList` (`includeProjectLock="yes"`). Session generation probes the server when authenticated and auto-generates missing `<session_pkg><cross_pkg_label>.lbl` definitions unless locked in another activity.
3. **Fail-Fast Workspace Inference & Unified OAuth2 Refresh**:
   - Infer `--workspace` from `--activity` path (`<ws_root>/<workspace>/<activity>`) or CWD; when ambiguous, fail fast listing discovered workspaces (unless only a single workspace or explicit config exists) instead of falling back to a hardcoded tenant.
   - Align Rust `skill-ln` (`login`, `login --status`, `project-info`) with Python Tier 2 silent `refresh_token` renewal, `cloudenv.prefs` `.ionapi` discovery, and `connectivity.prefs` sync.
4. **Activity-Based Cloud SCM Detection & Seamless `DR_Create` Lifecycle**:
   - `is_project_scm_enabled` MUST treat an activity as SCM-enabled when `properties.index` contains valid `labelUUID` / `taskName` / `*_dev` Activity-Based Cloud SCM metadata, even when `ApplicationUsesSCM=no`. Fix the `.indexes/` path segment in Rust `scm_engine.rs`.
   - Preserve exact component name casing across all SCM payloads.
   - `Put` / `CheckIn` automatically detect unregistered new components and execute `DR_Create` -> `CheckOut` -> `Put` / `CheckIn`.
   - Align Rust `sync-admin` with Python `admin_sync.py` (TDE layout validation, exclusion of `.admin`/`.metadata`/extension files, flag preservation, `after_create` for new files, pruning deleted files).
5. **Post-End-Activity VRC Sync (`sync-activity`) & VSC Execution**:
   - Add `sync-activity` across Python CLI, Rust `skill-ln`, and both Stdio MCP servers: queries `StudioComponent.GetBrowseList` with activity `context_xml`, refreshes only components that are committed on the server (`isCheckedOut=no`, `isCheckedOutParallel=no`) and not locally `Dirty` via `GetActivitySource`, compacts XML, sets Read-Only, and updates `.admin` via `admin_after_get` while leaving active `CheckedOut`/`Dirty` items untouched.
   - Convert `*` -> `%` in `GetBrowseList` queries, always pass activity `context_xml` when scoped, and pass package combination + valid `conid` to `VSC.executeVSC` inside `prepare-end-activity` by default (with `--skip-vsc` opt-out).
6. **100% Python & Rust Parity**:
   - Every behavioral fix, regression test, and differential check MUST land in both `.agents/skills/ln_studio_skill/tools/` and `rust/`, followed by rebuilding `skill-ln.exe` and running `python scripts/run_checks.py --sync-skill`.
