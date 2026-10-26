# Domain Glossary: Infor ERP LN Skill Architecture

Consistent vocabulary for developing, extending, and structuring Infor ERP LN development knowledge and skills.

### Core Architecture & Runtime
- **Bshell**: The Infor LN runtime execution environment / virtual process that executes 3GL/4GL bytecode, manages database cursors, and interfaces with the UI/WebUI.
- **VRC (Version - Release - Customer)**: The layered package hierarchy in Infor LN that manages code variants and customizations (e.g., standard code `B61_c`, custom code in customer VRCs).
- **Runtime Data Dictionary**: Compiled metadata (domains, tables, forms, sessions, labels) read directly by the bshell for maximum performance, updated via "Convert to Runtime" (`crdd`).
- **Application Data Dictionary**: Editable design-time definitions stored in tools tables (`ttadv...`).

### Modern Extensibility (LN 10.8+)
- **Extension Modeler (`ttext1500m000`)**: The framework for customizing standard LN components without modifying base code ("last-mile" customization), supporting clean cloud upgrades. Authoritative coding and compilation occurs strictly in the LN UI Web interface.
- **Extension Modeler Boundary & SCM Non-Check-Out**: Extensions cannot be checked out or committed through LN Studio SCM. In LN Studio, extension scripts can only be imported via "Get" for read-only reference and debugging; direct edits to workspace `.lib` XML files are invalid and non-deployable.
- **Hook-by-Hook Local Authoring**: The workflow pattern of creating and maintaining extension source files inside the local project/repository, structured by hook/function blocks, which are then copied into individual hook windows in LN UI (`ttext1500m000`).
- **#context_on / #context_off Directives**: Native Infor LN preprocessor block directives used to encapsulate hook-level code blocks (e.g. `#context_on "before.save.object"` ... `#context_off`) within local cohesive 4GL extension source files, mapping 1-to-1 with LN UI hook entry points.
- **Agent Guide-and-Paste Protocol**: The mandatory behavioral protocol for AI agents and engineers when authoring or modifying Infor LN extensions: (1) author locally in `extensions/<type>/<comp>_ext.4gl`, (2) verify offline with `check-script` / `check_4gl_script.py`, (3) output structured step-by-step guidance in chat with LN UI `ttext1500m000` navigation and clean hook-by-hook code blocks, and (4) warn never to check out or edit in LN Studio.
- **Extension Point**: An extensible LN component type: Table, Session, Report, BOD/BDE, OData REST API, Menu, Process, or Domain.
- **Hook**: An exported function (`function extern <type> <hook-name>(...)`) called by the bshell/DAL at specific lifecycle events (e.g., `before.save.object`, `when.field.changes`, `is.valid`).
- **Session Extension (`ess`)**: Last-mile extension for standard sessions (`<pkg>/library/ess/`, `sourceType=8`), implementing UI command hooks (`function.<cmd>.is.enabled`, `before.command`, `after.command`).
- **Table Extension (`est`)**: Last-mile extension for standard tables (`<pkg>/library/est/`, `sourceType=6`), implementing DAL hooks with official `#context_on` / `#context_off` blocks.
- **CDF (Customer Defined Field)**: Custom database columns (`<table>.cdf_<name>`) added to standard or custom tables with dedicated logic hooks.
- **Cloud Governance**: Restrictions enforced on extensions in Infor Cloud (e.g., trusted vs untrusted mode, execution time governors, query limits, restricted file system access).

### Classic 4GL & Tools (Development Tools 10.5+)
- **DAL (Data Access Layer)**: The business logic layer for tables. DAL 1 (classic) and DAL 2 (modern object-oriented style with property hooks, object sets, and business methods).
- **DAL Object Hook**: High-level CRUD lifecycle method on the entity table (e.g., `before.save.object`, `after.save.object`, `before.destroy.object`, `method.is.allowed`).
- **DAL Property Hook**: Column-specific validation/logic hook formatted as `<table.column>.<suffix>` (e.g., `.is.valid`, `.make.valid`, `.is.mandatory`, `.is.readonly`, `.update`, `.check`).
- **UI Script (4GL Script)**: Client-facing session script managing user interface interactions and choice sections. Database modifications should never be placed directly in UI scripts.
- **3GL / DLL Library**: Shared callable functions (`bic_*` libraries) providing reusable business algorithms and utility routines.
- **MMT Session (Multi-Main Table)**: Complex user interfaces coordinating multiple entity tables through an MMT Controller session and linked Satellite sessions.
- **MMT Controller (`<DR_Controller>`)**: Session archetype coordinating multi-table maintenance with linked Satellite sessions via `<ControllerSatelliteRelationship>`.
- **Satellite Session**: Child session embedded in an MMT Controller displaying related detail lines.
- **Form Command (`<FormCommand>`)**: Declarative action or toolbar button in a session bound to a 4GL function or standard choice.
- **Baan SQL (Embedded SQL)**: Embedded database queries utilizing `SELECT ... SELECTDO ... SELECTEOS ... ENDSELECT` constructs with cursor-level transaction controls (`commit.transaction()`, `retry.point()`).
- **PMC (Product Maintenance Component)**: Software distribution mechanism managing individual solutions, collections, patches, and feature packs.

### Best Practice & Design Patterns
- **Separation of Concerns (SoC)**: Architectural rule in Infor LN mandating that UI logic stays in UI scripts (`type 1-4`), while all business logic, data validations, integrity checks, and CRUD operations reside strictly in the DAL (or Table Extension).
- **Hook Lifecycle**: The deterministic call sequence of extension hooks during CRUD operations (e.g. `before.open.object.set` -> `set.object.defaults` -> `<field>.check.input` -> `before.save.object` -> `after.save.object`).
- **Index Selectivity**: Designing and selecting SQL indices where leading fields match `WHERE` equality predicates, avoiding full table scans and lock escalation.
- **Controller & Satellites**: The MMT session design pattern where a single parent Controller coordinates one or more synchronized Satellite sessions displaying related detail records.

### LN Studio (Activity-Based Development, 10.8 build 0640)
- **Activity**: The unit of work in LN Studio; every component modification is linked to an activity (`<activity> [<project>]` folder), which belongs to a software project under an application. Lifecycle: open, clean, recover, reassign, end, link run configurations.
- **Read-Only SCM Guardrail**: SCM protection mechanism where components checked into LN SCM have the OS Read-Only flag set. The toolchain enforces `assert_file_writable` and aborts with `ReadOnlyComponentError` to prevent overwriting or editing checked-in components, requiring human check-out in the Eclipse workbench.
- **SCM Cache (`.admin`)**: The per-activity Eclipse SCM registration file listing tracked components and their flags (`isCreated`, `isCheckedOut`, `isDirty`, `isVSCHappy`). Regenerated from disk across all 12 managed extensions by `admin_sync.py` / `sync-admin` so Studio stops reporting phantom missing components.
- **Ecore Native Datatype**: The internal integer codes used by LN Studio's Ecore metamodel (`1`=Byte, `2`=Double, `3`=Long, `5`=Numeric, `6`=String, `7`=Enum, `9`=Date, `14`=UTC).
- **Four-Layer Activity Validator (`validate`)**: Comprehensive static verification engine auditing (1) SCM `.admin` registration and Read-Only state across 12 extensions, (2) XML root/child structure and Ecore datatypes, (3) Cross-object references (`.lbl`, `.tbl`, `.mnu`), and (4) Static 4GL syntax/completion checks on `<expression>` blocks.
- **Safe `--fix` Mode**: Non-destructive automated repair that generates missing `.lbl` files and synchronizes `.admin` registration without touching or modifying Read-Only files.
- **Problem Markers (`.markers`)**: The Eclipse binary diagnostics file per activity project recording compiler errors, warnings, and line numbers; decoded by `ln_error_reader.py` / `diagnose` into line-accurate reports (errors block a build, warnings do not).
- **Workbench**: The Eclipse RCP desktop shell hosting LN Studio perspectives, views, multipage editors, wizards, and dialogs.
- **Project VRC**: The VRC holding all finished software components for a project; SCM is activated per project VRC on the LN server (and optionally per Studio application), determining VRC numbering and CM action behavior.
- **Pinned Build Identity**: The validated runtime for this skill — LN Studio 10.8 build 0640 (April 2026 tree) with the September 2025 Application Development Guide; multi-release support is out of scope.
- **VSC (Verification of Source Code)**: Infor LN source code analysis and verification tool (`ttadv1230m000` / `ttadv1231m000`) integrated into LN Studio builders via `com.infor.ln.studio.apps.core.vscmarker`, enforcing static checks and blocking/non-blocking warnings.
- **Cloud Trusted Function (`Trusted="yes"`)**: Bshell functions certified for execution in Infor LN Cloud Multi-Tenant and GovCloud environments. Calling untrusted functions in Cloud Extensions triggers verification and security rejections.
- **DAL2 Field Hook Suffixes**: The 10 standardized method suffixes recognized by LN Studio's code assist (`.is.never.applicable`, `.is.applicable`, `.is.readonly`, `.is.derived`, `.is.mandatory`, `.is.valid`, `.update`, `.make.valid`, `.check`, `.set.defaults`).
- **TextMate Grammar (`tmLanguage.json`)**: Structured JSON regex tokenization grammar conforming to VS Code's syntax highlighting engine, classifying Baan 4GL code into scopes for colors and themes.
- **Standalone 4GL Auditor (`audit_4gl.py`)**: Zero-dependency offline verification engine in `erp-ln-progguide/scripts/` validating 4GL, DAL2, and UEDLL code against Studio syntax rules, DAL contracts, Cloud governance, and anti-pattern caveats.
