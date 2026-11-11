# Specification: Infor LN Extension Modeler Non-Context Standard Code Boundary & Anti-Tamper Guardrails

- **Target Skills**: `ln_studio_skill`, `erp-ln-progguide`
- **ADR Reference**: [`docs/adr/0020-extension-modeler-non-context-std-boundary-and-anti-tamper-guardrails.md`](../adr/0020-extension-modeler-non-context-std-boundary-and-anti-tamper-guardrails.md)
- **Local Spec Path**: `.scratch/extension-modeler-std-boundary-and-anti-tamper/spec.md`

---

## 1. Problem Statement

When developers copy raw 4GL Extension scripts (e.g., Table Extensions `txest*` or Session Extensions `txess*`) from Infor LN Studio into local projects to continue development with AI agents, the script contains both auto-generated standard boilerplate code (header comments, `| Additional generated declarations`, `table` declarations, standard `#include` statements, and framework functions such as `get.extension.point.version()`, `ext.get.form.fields()`, `ext.get.command.extensions()`) and custom code wrapped inside `#context_on "<hook>"` ... `#context_off` blocks.

Currently, AI coding agents misunderstand this dual structure. Agents mistakenly edit, delete, reformat, or relocate standard declarations and framework functions that live outside `#context_on ... #context_off`. Agents frequently attempt to "clean up" the script by moving standard table/include declarations into `#context_on "declarations"` or moving custom declarations outside, breaking the code generator contract of Extension Modeler (`ttext1500m000`), corrupting the script structure, and causing compilation failures when deployed back to Infor LN Enterprise Server.

---

## 2. Solution Overview

Establish an explicit, non-negotiable architectural boundary and automated anti-tamper guardrail for Infor LN Extension scripts:

1. **Strict Non-Context Immutability**: All lines of code outside `#context_on "<hook>"` ... `#context_off` are designated as **Strict Read-Only / Immutable**. AI agents and tools must preserve every character of non-context standard boilerplate without alteration.
2. **Automatic Extension Detection**: Any 4GL script containing `#context_on` or `#context_off` directives is automatically recognized as an Extension Modeler script, immediately enforcing the non-context read-only protection.
3. **Strict No-Relocation Policy**: Declarations, includes, and functions must never be moved between the non-context standard section and `#context` blocks. Custom logic, variables, and custom includes must reside solely within `#context_on` blocks.
4. **Refined Rule EXT001**: Update the definition of `EXT001` so that standard generated includes (such as `#include <bic_dal2>` and `#include <bic_tableext>` within `| Additional generated declarations`) are recognized as valid standard boilerplate and not flagged as errors.
5. **Anti-Tamper Audit Rule EXT003**: Introduce an automated audit check in `audit_4gl.py` and `check_4gl_script.py` that validates the structural integrity of extension scripts, detects illegal modifications outside `#context`, and enforces balanced, uncorrupted `#context_on`/`#context_off` pairs.
6. **Dual-Mode Delivery**: When an agent completes modifications, it updates the cohesive local file (preserving all standard boilerplate) and presents clean, individual hook blocks in chat (stripped of `#context` wrappers) for 1-click pasting into LN UI (`ttext1500m000`).

---

## 3. User Stories

1. As an Infor LN developer, I want to paste raw extension scripts copied from LN Studio into my local project, so that the AI assistant can help implement custom business hooks without corrupting standard framework boilerplate.
2. As an Infor LN developer, I want AI agents to never edit, delete, or reformat code outside `#context_on` and `#context_off`, so that standard generated declarations and framework functions remain intact.
3. As an Infor LN developer, I want AI agents to refrain from moving standard `table` or `#include` lines into `#context_on "declarations"`, so that the script retains 1-to-1 parity with Infor LN Studio.
4. As an Infor LN developer, I want any file containing `#context_on` directives to be automatically identified as an Extension script, so that I don't have to repeatedly instruct the agent about extension editing rules.
5. As an Infor LN developer, I want `audit_4gl.py` and `check_4gl_script.py` to recognize standard generated includes in the `| Additional generated declarations` section, so that false-positive `EXT001` errors are eliminated.
6. As an Infor LN developer, I want custom `#include` directives (e.g. custom DLLs) to be placed exclusively within `#context_on "declarations"`, so that the Infor LN server code generator properly routes them to the compiled declarations segment.
7. As an Infor LN developer, I want an automated `EXT003` anti-tamper rule, so that any unintentional deletion or modification of standard framework functions (`get.extension.point.version`, `ext.get.*`) is immediately caught before deployment.
8. As an Infor LN developer, I want the agent to be capable of adding new `#context_on "<hook>"` blocks when implementing new hooks, so that I can extend sessions and tables without damaging existing code.
9. As an Infor LN developer, I want the agent to output clean, hook-by-hook code blocks in chat, so that I can easily copy-paste each hook into LN UI `ttext1500m000` modal windows.
10. As an Infor LN developer, I want the local repository file to maintain full-fidelity raw 4GL source, so that our Git repository tracks complete, syntactically valid scripts that match what LN Studio exports.
11. As an AI assistant, I want unambiguous architectural boundaries and rules, so that I know precisely where custom code begins and where generated standard framework code must not be touched.
12. As a CI/CD pipeline operator, I want `python scripts/run_checks.py` to statically verify all extension rules across the repository, so that code drift or broken hooks are caught before committing.

---

## 4. Implementation Decisions

- **Architectural Boundary**: The contents of an extension script are strictly partitioned into:
  - **Non-Context STD Section**: Pre-context header, `| Additional generated declarations`, and post-context framework functions (`get.extension.point.version()`, `ext.get.*()`). This section is strictly Read-Only / Immutable.
  - **Context Hook Blocks**: Any code wrapped between `#context_on "<hook>"` and `#context_off`. This section is editable and contains user-authored logic.
- **Script Classification**: `detect_archetype()` and static audit engines will detect any file containing `#context_on` as an extension script and apply Extension Modeler validation rules.
- **Rule EXT001 Refinement**: Re-scope `EXT001` so that direct `#include` statements within the standard `| Additional generated declarations` block are permitted, while custom includes outside `#context_on "declarations"` remain prohibited.
- **New Rule EXT003**: Introduce `EXT003 [ERROR]` to flag any alteration to standard framework functions, invalid nesting of `#context_on`, unclosed context blocks, or placement of custom executable code outside `#context`.
- **Extension Manager & CLI Alignment**: Ensure `ln_extension_manager.py` respects standard boilerplate during `import-extension` and `extension-hooks`, allowing round-trip parsing without stripping boilerplate from local files.
- **Guidelines & Rules Integration**: Add the non-context read-only rule to `.antigravity/rules/infor_ln.md` Section 5, update `docs/glossary/GLOSSARY.md`, and author ADR 0020.

---

## 5. Testing Decisions

- **Testing Seam**: The tests will be executed at the existing high-level test seam:
  - `python -m unittest ln_studio_skill/tools/tests/test_extension_workflow.py`
  - Repository gateway: `python scripts/run_checks.py`
- **Good Test Criteria**: Tests must assert observable external verification behavior:
  - Valid scripts with standard boilerplate outside `#context` and custom code inside `#context` must pass with 0 errors.
  - Scripts where standard includes appear in `| Additional generated declarations` must not trigger `EXT001`.
  - Scripts where custom includes are placed outside `#context_on "declarations"` must trigger `EXT001`.
  - Scripts where non-context framework functions are modified, removed, or improperly wrapped in `#context` must trigger `EXT003`.
  - Scripts with unclosed or nested `#context_on` blocks must trigger syntax errors.
- **Prior Art**:
  - `ln_studio_skill/tools/tests/test_extension_workflow.py`: `TestExtensionWorkflow`, `TestExtensionSyntaxAndAuditorRules`.
  - `scripts/run_checks.py`: Unified gateway running all unit tests, markdown linting, and syntax checks.

---

## 6. Out of Scope

- Modifying Infor LN Studio Eclipse plugins or Java SCM proxies.
- Interacting with live Infor CloudSuite servers or bypassing LN UI `ttext1500m000`.
- Altering standard 3GL DLL library authoring (`--type dll` in `<pkg>/library/<mod>/`).

---

## 7. Further Notes

- ADR 0020 (`docs/adr/0020-extension-modeler-non-context-std-boundary-and-anti-tamper-guardrails.md`) serves as the permanent architectural record.
- The Agent Guide-and-Paste protocol remains the primary operational workflow for deploying extensions to LN UI.
