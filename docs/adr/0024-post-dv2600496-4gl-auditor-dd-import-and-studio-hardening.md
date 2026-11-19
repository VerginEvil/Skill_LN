# ADR 0024: 4GL Auditor Parity, Local DD Text Importer, Knowledge Search, and Safe Studio Sync Hardening

- **Status**: Accepted
- **Date**: 2026-11-19
- **Target Skills**: `erp-ln-progguide` & `ln_studio_skill` (Python toolchain + Native Rust `skill-ln` binary)
- **Specification**: `.scratch/post-dv2600496-skill-hardening/spec.md`
- **Prior ADRs**:
  - [`docs/adr/0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md`](0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md) *(Extended: Local Data Dictionary Text Importer & Rust DD cache resolution)*
  - [`docs/adr/0010-pre-fetch-server-authentication-guardrail-and-user-alert.md`](0010-pre-fetch-server-authentication-guardrail-and-user-alert.md) *(Extended: Canonical workspace-to-environment token key alignment)*
  - [`docs/adr/0018-lean-skill-architecture-and-progressive-disclosure.md`](0018-lean-skill-architecture-and-progressive-disclosure.md) *(Preserved: Keep `SKILL.md <= 80` lines; house deep schemas & rules in `references/`)*
  - [`docs/adr/0021-native-rust-skill-ln-single-binary-architecture.md`](0021-native-rust-skill-ln-single-binary-architecture.md) *(Extended: Full Python/Rust differential parity in `ln-linter`, `ln-kb`, `ln-scm`, `ln-auth`, and `ln-model`)*
  - [`docs/adr/0023-label-xml-parity-cloud-scm-and-vrc-sync-hardening.md`](0023-label-xml-parity-cloud-scm-and-vrc-sync-hardening.md) *(Extended: Non-destructive `.admin` merge, scoped activity validation, and LN Studio 10.8 `.ses` layout parity)*

---

## 1. Context & Problem Statement

End-to-end delivery of a multi-session UI + Table Extension customization revealed seven recurring accuracy gaps and workflow bottlenecks across `erp-ln-progguide` and `ln_studio_skill`:

1. **`.cln` Extension Misclassification & Rust DD Cache Blindness**:
   - Both Python `audit_4gl.py` and Rust `ln-linter` unconditionally classify any `.cln` file as an Extension Modeler script even when `--mode general` is specified and no `#context_on`/`#context_off` directives exist, causing false-positive `EXT001`/`EXT003` errors on standard UI session `.cln` scripts.
   - Rust `skill-ln audit-4gl` ignores `--dd-cache`, omits `--mode`/`--cloud`, and its `resolve_dd_cache()` returns `None`, disabling schema and domain rules (`TBL002`, `DMN001`–`DMN003`, `STR001`) in the native binary.
2. **Manual `.ln_dd_cache.json` Construction**:
   - Child customization repositories routinely store Infor LN `ttadv4420m000` Table Definition reports (`*.txt`) and CDF dumps (`*-cdf.txt`), yet neither Rust nor Python supports importing them into `.ln_dd_cache.json`, forcing agents to construct hundreds of lines of JSON manually whenever server auth is unavailable.
3. **Static Audit Blind Spots**:
   - Manual code review had to catch five recurring defects missed by static auditing: `dal.set.error.message("@<code>")` literal-text traps, `utc.to.date()` used instead of `utc.to.local()` + `num.to.date()` in exports, `seq.open(..., "wt")` combined with UTF-8 BOM bytes instead of `"wb"`, direct `=`/`<>` comparisons on `double` columns/variables instead of `double.cmp()`, and SQL index/binding anti-patterns (missing leading index columns, unbound `select` fields vs `:l.*`, `_index1 = {...}`).
4. **`doc-search` / `fn-search` Gaps Outside `Skill_LN`**:
   - Running `skill-ln doc-search` from a child repository fails silently (`found 0`) because `find_progguide_references_dir()` only searches 5 ancestors of CWD/exe and discards missing-corpus warnings, while multi-word queries compile into a single adjacent regex. Hook headers, preprocessor/UTF-8 topics (`utf8.export`), and domain enum constants are also underrepresented in search results.
5. **`.admin` Corruption in `sync-admin`**:
   - Rust `sync-admin` swallows `.admin` parse errors with `.unwrap_or_default()`, resets `isCheckedout=true` via `after_create`, and strips the `<activity_folder>/` prefix from `m_path` via `normalize_admin_path` (mirrored by `AdminSyncHelper.java` repair).
6. **OAuth2 Token Key Mismatch (`environments` vs `login --status`)**:
   - `login --workspace <path> --status` hashes/names the token file using the raw path string instead of resolving `WorkspaceContext.env_name` (and omits user-home `cloudenv.prefs`), diverging from `environments`.
7. **Unscoped `validate` in Dirty Activities & Outdated Session XML Schema**:
   - `validate` lacks `--filter` / `--files` scoping to isolate target components inside activities with pre-existing legacy errors, skips `<showAsButton>`, `rowScreenPosition` overlap, and Session Script–Form parity checks, Rust `inject` skips Read-Only enforcement, and `COMPONENT_XML_SCHEMA.md` + session generators diverge from real LN Studio 10.8 `.ses` `<PhysicalFormLayout>` structure.

---

## 2. Decisions

1. **Context-Driven `.cln` Classification & Rust `audit-4gl` Flag Parity**:
   - Remove unconditional `.cln` extension assumption in both Python and Rust auditors. Treat a script as Extension Modeler only when `#context_on`/`#context_off` directives exist or (when `mode` is not explicitly `"general"`/`"session"`/`"library"`/`"table"`/`"report"`) extension path/include markers (`/est/`, `/ess/`, `_ext.4gl`, `bic_tableext`, `bic_sessionext`) match.
   - Add `--mode` and `--cloud` to Rust `skill-ln audit-4gl` and wire `--dd-cache` + automatic `.ln_dd_cache.json` loading into Rust `Auditor4GL`.
2. **Local Data Dictionary Text Importer (`import-dd-txt` & `--dd-dir`)**:
   - Implement a parser for Infor LN `ttadv4420m000` Table Definition `.txt` reports (extracting table code, fields, domains, datatypes, physical lengths, mandatory flags, indices) and `*-cdf.txt` reports (mapping CDF fields with the `cdf_` prefix).
   - Expose `skill-ln import-dd-txt <dir> [--out .ln_dd_cache.json]` for persistent cache generation (non-destructively merging into existing `.ln_dd_cache.json` while preserving richer server-fetched metadata) and `--dd-dir <dir>` on both `skill-ln audit-4gl` and `audit_4gl.py` for zero-setup on-the-fly auditing.
3. **Tiered Severity for New 4GL Static Audit Rules**:
   - **`ERROR` (delivery-blocking)**:
     - `dal.set.error.message("@<code>")` when the `@`-prefixed string matches a message code identifier rather than literal message text.
     - `seq.open(..., "wt")` when paired with raw UTF-8 BOM byte writes (`chr$(239)`, `chr$(187)`, `chr$(191)`) in the same script/function.
     - Direct `=` / `<>` / `!=` comparisons on locally declared `double` variables or Data-Dictionary-confirmed `Double` table fields (recommend `double.cmp(..., epsilon)`).
   - **`WARNING` (advisory review hint)**:
     - `utc.to.date()` used in string/file export contexts (recommend `utc.to.local()` + `num.to.date()`).
     - SQL index & binding hygiene: legacy `_index1 = {...}` predicates, unbound `select` columns (suggesting `:l.*` scalar host variables), and `WHERE` predicates missing leading index columns when DD index metadata is loaded.
4. **Global Skill Corpus Fallback & Multi-Term `doc-search`**:
   - Extend `find_progguide_references_dir()` to fall back to the synced global skill directory (`~/.gemini/config/skills/erp-ln-progguide/references`) and emit a visible `stderr` warning if the corpus cannot be located.
   - Fix `doc_search` multi-word queries to evaluate whitespace-separated terms with line-level/file-level AND matching and exact-phrase score boosting, and index hook/section headers, `utf8.export`/`utf8.import`, and domain enum constants so common 4GL lookups succeed.
5. **Fail-Fast `.admin` Parsing & Non-Destructive Safe `.admin` Merge**:
   - Remove `.unwrap_or_default()` from `sync-admin`; fail fast on `.admin` parse errors so existing SCM state is never wiped.
   - Create a `.admin.bak` backup prior to mutation, preserve existing entries' flags (`isCheckedout`, `isCreated`, `isEvercheckedIn`, `m_isDirty`, `m_isVSCHappy`) and `<activity_folder>/` `m_path` prefixes, register newly discovered files non-destructively (respecting Read-Only status), and prune missing entries only when `--prune` is explicitly passed.
6. **Canonical Workspace Token Key Resolution**:
   - Normalize `--workspace` in `login` (CLI and MCP) through `WorkspaceContext::discover` to resolve `ctx.env_name` whenever a directory path is given, search `~/.ln_studio/com.infor.erpln.jca.connectivity.cloudenv.prefs` in `load_ionapi_from_cloudenv()`, and unify `environments` and `login --status` token status + silent `refresh_token` reporting.
7. **Component-Scoped `validate`, `.ses` UI Checks, `inject` Guardrail & LN 10.8 Session Schema**:
   - Add `--filter <pattern>` and `--files <list>` to `validate` (CLI, Python, and MCP `ln_validate_activity`), loading full-activity `.admin` and label/table catalogs while emitting diagnostics only for matched target files.
   - Add `WARNING`-level checks for `<showAsButton>false</showAsButton>` on dialog/user `<FormCommand>`, overlapping `(rowScreenPosition, columnScreenPosition)` within a `<groupID>`, and **Session Script–Form Parity** (non-table `<FormField>` and `<FormCommand><activationName>` vs `extern` symbols).
   - Enforce `Read-Only-SCM-Guardrail` in Rust `skill-ln inject`, update `COMPONENT_XML_SCHEMA.md` and Python/Rust session generators to real LN Studio 10.8 `<PhysicalFormLayout>` XML, and preserve the ADR 0018 `<= 80`-line `SKILL.md` ceiling across both skills.
