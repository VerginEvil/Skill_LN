# Domain Glossary: Infor ERP LN Skill Architecture

Consistent vocabulary for developing, extending, and structuring Infor ERP LN development knowledge and skills.

### Core Architecture & Runtime
- **Bshell**: The Infor LN runtime execution environment / virtual process that executes 3GL/4GL bytecode, manages database cursors, and interfaces with the UI/WebUI.
- **VRC (Version - Release - Customer)**: The layered package hierarchy in Infor LN that manages code variants and customizations (e.g., standard code `B61_c`, custom code in customer VRCs).
- **Runtime Data Dictionary**: Compiled metadata (domains, tables, forms, sessions, labels) read directly by the bshell for maximum performance, updated via "Convert to Runtime" (`crdd`).
- **Application Data Dictionary**: Editable design-time definitions stored in tools tables (`ttadv...`).

### Modern Extensibility (LN 10.8+)
- **Extension Modeler (`ttext1500m000`)**: The framework for customizing standard LN components without modifying base code ("last-mile" customization), supporting clean cloud upgrades.
- **Extension Point**: An extensible LN component type: Table, Session, Report, BOD/BDE, OData REST API, Menu, Process, or Domain.
- **Hook**: An exported function (`function extern <type> <hook-name>(...)`) called by the bshell/DAL at specific lifecycle events (e.g., `before.save.object`, `when.field.changes`, `is.valid`).
- **CDF (Customer Defined Field)**: Custom database columns (`<table>.cdf_<name>`) added to standard or custom tables with dedicated logic hooks.
- **Cloud Governance**: Restrictions enforced on extensions in Infor Cloud (e.g., trusted vs untrusted mode, execution time governors, query limits, restricted file system access).

### Classic 4GL & Tools (Development Tools 10.5+)
- **DAL (Data Access Layer)**: The business logic layer for tables. DAL 1 (classic) and DAL 2 (modern object-oriented style with property hooks, object sets, and business methods).
- **UI Script (4GL Script)**: Client-facing session script managing user interface interactions and choice sections. Database modifications should never be placed directly in UI scripts.
- **3GL / DLL Library**: Shared callable functions (`bic_*` libraries) providing reusable business algorithms and utility routines.
- **MMT Session (Multi-Main Table)**: Complex user interfaces coordinating multiple entity tables through a Controller session and linked Satellite sessions.
- **Baan SQL (Embedded SQL)**: Embedded database queries utilizing `SELECT ... SELECTDO ... SELECTEOS ... ENDSELECT` constructs with cursor-level transaction controls (`commit.transaction()`, `retry.point()`).
- **PMC (Product Maintenance Component)**: Software distribution mechanism managing individual solutions, collections, patches, and feature packs.

### Best Practice & Design Patterns
- **Separation of Concerns (SoC)**: Architectural rule in Infor LN mandating that UI logic stays in UI scripts (`type 1-4`), while all business logic, data validations, integrity checks, and CRUD operations reside strictly in the DAL (or Table Extension).
- **Hook Lifecycle**: The deterministic call sequence of extension hooks during CRUD operations (e.g. `before.open.object.set` -> `set.object.defaults` -> `<field>.check.input` -> `before.save.object` -> `after.save.object`).
- **Index Selectivity**: Designing and selecting SQL indices where leading fields match `WHERE` equality predicates, avoiding full table scans and lock escalation.
- **Controller & Satellites**: The MMT session design pattern where a single parent Controller coordinates one or more synchronized Satellite sessions displaying related detail records.

### LN Studio (Activity-Based Development, 10.8 build 0640)
- **Activity**: The unit of work in LN Studio; every component modification is linked to an activity (`<activity> [<project>]` folder), which belongs to a software project under an application. Lifecycle: open, clean, recover, reassign, end, link run configurations (see `ln_studio_skill/references/studio_guide/ch03_activity_based_development.md`).
- **SCM Cache (`.admin`)**: The per-activity Eclipse SCM registration file listing tracked components and their flags (`isCreated`, `isCheckedOut`, `isDirty`, `isVSCHappy`). Regenerated from disk by `admin_sync.py` / `sync-admin` so Studio stops reporting phantom missing components.
- **Problem Markers (`.markers`)**: The Eclipse binary diagnostics file per activity project recording compiler errors, warnings, and line numbers; decoded by `ln_error_reader.py` / `diagnose` into line-accurate reports (errors block a build, warnings do not).
- **Workbench**: The Eclipse RCP desktop shell hosting LN Studio perspectives, views, multipage editors, wizards, and dialogs (see `ln_studio_skill/references/studio_guide/ch01_studio_overview.md`).
- **Project VRC**: The VRC holding all finished software components for a project; SCM is activated per project VRC on the LN server (and optionally per Studio application), determining VRC numbering and CM action behavior.
- **Pinned Build Identity**: The validated runtime for this skill — LN Studio 10.8 build 0640 (April 2026 tree) with the September 2025 Application Development Guide; multi-release support is out of scope.
