# ADR 0014: Quality Hardening, CI Guardrails, Layout Enforcement, and MCP Tool Execution Parity

- **Status**: Accepted
- **Date**: 2026-11-02
- **Target Skill**: `ln_studio_skill`
- **Specification**: [`.scratch/retro-improvements-and-hardening/spec.md`](../../.scratch/retro-improvements-and-hardening/spec.md)
- **Prior ADRs**:
  - [`docs/adr/0007-headless-jca-connectivity-scm-and-mcp-server.md`](0007-headless-jca-connectivity-scm-and-mcp-server.md) *(Introduced LN Studio Stdio MCP Server)*
  - [`docs/adr/0010-pre-fetch-server-authentication-guardrail-and-user-alert.md`](0010-pre-fetch-server-authentication-guardrail-and-user-alert.md) *(Pre-fetch authentication and user alert banners)*
  - [`docs/adr/0012-rea-100-percent-ln-studio-parity-and-daemon-architecture.md`](0012-rea-100-percent-ln-studio-parity-and-daemon-architecture.md) *(100% REA Parity, Persistent JCA Daemon, and Single-XML TDE Layout)*

---

## 1. Context & Problem Statement

Following the completion and two-axis review of the 100% REA Parity milestone (`feat/rea-100-percent-ln-studio-parity`), a retrospective identified five concrete reliability and engineering gaps:

1. **MCP Tool Signature Mismatch & Runtime `TypeError`**:
   In `ln_studio_mcp.py`, actions like `new_activity`, `open_activity`, and `clean_activity` had argument and type assumptions that drifted from `ln_project_activity_manager.py` (e.g. passing `task_name` instead of `task_id`, `workspace_dir` instead of `workspace_path`, and calling `.get()` on boolean returns). Although JSON-RPC schemas were tested in `test_stdio_mcp_server.py`, the actual tool execution dispatch (`execute_tool`) was never invoked in tests.
2. **Missing CI Pipeline (`.gitlab-ci.yml`) & Local Pre-Commit Guardrail**:
   The repository had no automated continuous integration pipeline on GitLab and no active `.git/hooks/pre-commit`, requiring manual execution of tests and leaving code changes vulnerable to regressions.
3. **Mechanical Single-XML TDE Layout & Admin Whitelist Violations**:
   - `ln_revision_diff.py:404` (`generate_report_on_server`) wrote report files to legacy plural folder `activity_dir / "reports" / ...` instead of the canonical `{pkg}/report/{mod}/{name}.{ext}` layout required by ADR 0012, risking silent deletion by Eclipse LN Studio's `Administration.removeObsoleteComponents()`.
   - `admin_sync.py` included `".rptdsrc"` in `MANAGED_EXTENSIONS` instead of `EXCLUDED_EXTENSIONS`, conflicting with `AdminSyncHelper.java`.
4. **Agent Navigation Ambiguity for Test Execution**:
   Incoming AI agents attempted `pytest` first, failing because pytest was not installed in the Windows environment, due to a lack of documented test commands in `AGENTS.md`.
5. **Code Smells & Signature Collision**:
   `_build_context` was duplicated verbatim across `ln_code_intelligence.py` and `ln_revision_diff.py`, and `find_component_file` existed in both `admin_sync.py` and `ln_scm_engine.py` with conflicting signatures.

---

## 2. Settled Architectural Decisions

### Decision 1: Normalized MCP Tool Envelope & End-to-End Execution Testing
1. **Normalized Envelope Contract**:
   All 20 MCP tools registered in `ln_studio_mcp.py` MUST normalize action results into a consistent dictionary envelope:
   ```json
   {
     "status": "success" | "error",
     "action": "<action_name>",
     "result": <data>,
     "message": "<human_readable_message>"
   }
   ```
   Primitive and boolean results (e.g. `clean_activity`, `move_components`) are wrapped into `result: {"cleaned": bool}` or similar structured forms so callers never suffer `TypeError` or `AttributeError`.
2. **Hermetic Mock Execution Test Suite (`test_mcp_tool_execution.py`)**:
   Create a dedicated unit test suite exercising `execute_tool(name, params)` for all 20 registered tools across all supported actions, mocking at the manager layer (`unittest.mock.patch`) to verify parameter parsing, type conversion, and envelope formatting in < 2 seconds without external dependencies.

### Decision 2: Unified Verification Script (`scripts/run_checks.py`) & GitLab CI
1. **Single Source of Truth**:
   Implement `scripts/run_checks.py` executing:
   - Syntax compilation check: `python -m compileall ln_studio_skill/tools/`
   - Mechanical layout verification: `validate_activity_layout()`
   - Full test discovery: `python -m unittest discover -s ln_studio_skill/tools/tests -p "test_*.py"`
2. **GitLab CI Pipeline (`.gitlab-ci.yml`)**:
   Add a GitLab CI pipeline defining `test` and `lint` stages executing `python scripts/run_checks.py`.
3. **Pre-Commit Hook Integration**:
   Provide `--install-hook` in `scripts/run_checks.py` to automatically configure `.git/hooks/pre-commit`.

### Decision 3: Mechanical Single-XML TDE Layout & Admin Sync Enforcement
1. **Report Layout Alignment**:
   In `ln_revision_diff.py`, `generate_report_on_server` must extract `{mod}` from report name (characters 2-4 if length >= 6, else default to `"gen"`) and place reports strictly at `{pkg}/report/{mod}/{report_name}.rpt`, registering `"{pkg}/report/{mod}/{report_name}.rpt"` in `.admin`.
2. **Admin Sync Extension Alignment**:
   Move `".rptdsrc"` from `MANAGED_EXTENSIONS` to `EXCLUDED_EXTENSIONS` in `admin_sync.py` to match `AdminSyncHelper.java`.
3. **Mechanical Guardrail (`validate_activity_layout`)**:
   Add an automated validator in `admin_sync.py` that raises a hard `ValueError` if any component in an activity resides in legacy plural directories (`reports/`, `tables/`, `sessions/`), preventing commit and SCM actions.

### Decision 4: Agent Navigation & Test Command Pointer in `AGENTS.md`
1. Update `AGENTS.md` to explicitly state the canonical test command:
   ```bash
   python -m unittest discover -s ln_studio_skill/tools/tests -p "test_*.py"
   ```
   and the quality check script:
   ```bash
   python scripts/run_checks.py
   ```

### Decision 5: Helper Centralization & Signature Disambiguation
1. **Centralize SCM Context Builder**:
   Consolidate duplicated `_build_context` implementations into `ln_scm_engine.py` as `resolve_activity_context_xml(activity_dir, project_name)` and import it in `ln_code_intelligence.py` and `ln_revision_diff.py`.
2. **Rename Ambiguous Function**:
   Rename `find_component_file` in `admin_sync.py` to `find_component_by_coords` to eliminate collision with `ln_scm_engine.find_component_file`.
