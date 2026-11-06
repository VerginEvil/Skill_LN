# Skill_LN Development Guidelines

## Testing & Verification

Always use Python's built-in `unittest` runner (do NOT invoke `pytest` as it is not installed in the Windows Python environment):

```powershell
# Run the full test suite across all tools (erp-ln-progguide: erp-ln-progguide/tests, ln_studio_skill: ln_studio_skill/tools/tests)
python -m unittest discover -s ln_studio_skill/tools/tests -p "test_*.py"

# Run a single test file
python -m unittest ln_studio_skill/tools/tests/test_mcp_tool_execution.py

# Run unified checks (syntax compilation, layout verification, full test discovery)
python scripts/run_checks.py
```

## Agent skills

### Issue tracker

Issues and specs live as local markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context layout (`docs/glossary/GLOSSARY.md`, architecture decision records under `docs/adr/`, plans under `docs/plans/`). See `docs/agents/domain.md`.
