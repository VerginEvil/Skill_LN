# Infor LN Studio Application Development Guide — Studio Index

Usage knowledge for **Infor LN Studio 10.8 (Eclipse RCP)**, distilled from the
*Application Development Guide (Cloud and On-premises), September 2025* (12 chapters).
Full-detail chapters preserve procedures, steps, and lists verbatim; summary chapters
give orientation-level coverage without inventing behavior beyond the source.

## Chapters Overview

| Chapter | Title | Depth | Reference File | Key Topics |
|---|---|---|---|---|
| Chapter 1 | LN Studio overview | full | [studio_guide/ch01_studio_overview.md](studio_guide/ch01_studio_overview.md) | Eclipse RCP workbench, functions and features, user roles, scope and limitations, architecture, troubleshooting, applications, cloud differences |
| Chapter 2 | Installation and configuration | full | [studio_guide/ch02_installation_and_configuration.md](studio_guide/ch02_installation_and_configuration.md) | First installation, prerequisites, workspace selection, connectivity settings, dynamic connection points, user preferences, multi-tenant/single-tenant cloud settings, updates |
| Chapter 3 | Activity based development | full | [studio_guide/ch03_activity_based_development.md](studio_guide/ch03_activity_based_development.md) | Activity-based development, SCM usage, project VRC vs application SCM, VRC numbering, CM actions, activity context, clean/recover/reassign, run configurations |
| Chapter 4 | Development procedure | full | [studio_guide/ch04_development_procedure.md](studio_guide/ch04_development_procedure.md) | Developing components, verification (warnings vs errors, problem markers), sample exercise, run/debug sessions, breakpoints, expressions, BFlow tests |
| Chapter 5 | InContext Modeling | summary | [studio_guide/ch05_incontext_modeling.md](studio_guide/ch05_incontext_modeling.md) | InContext modeling, context messages, InContext model (summary) |
| Chapter 6 | LN Studio Limitations | summary | [studio_guide/ch06_studio_limitations.md](studio_guide/ch06_studio_limitations.md) | General, Script Editor, CM, build, debugger, Web UI limitations (summary) |
| Chapter 7 | Wizards and Dialogs | full | [studio_guide/ch07_wizards_and_dialogs.md](studio_guide/ch07_wizards_and_dialogs.md) | Activity wizards/dialogs, browse/select dialogs, component creation wizard, domain/label/function/session/table creation, debugging dialogs, preferences, verify components |
| Chapter 8 | Multipage Editors | full | [studio_guide/ch08_multipage_editors.md](studio_guide/ch08_multipage_editors.md) | Multipage editors per component (domain, function, label, library, menu, message, question, report, session, table), tabs, DAL and script handling |
| Chapter 9 | Script Editor | full | [studio_guide/ch09_script_editor.md](studio_guide/ch09_script_editor.md) | Script editor, markers and ruler, code assist, comments, folding, navigation, breakpoints, WSDL source generation |
| Chapter 10 | Perspectives | summary | [studio_guide/ch10_perspectives.md](studio_guide/ch10_perspectives.md) | Application and Debug perspectives (summary) |
| Chapter 11 | Views | summary | [studio_guide/ch11_views.md](studio_guide/ch11_views.md) | Activity Explorer, Breakpoints, Component Explorer, Debug, Expressions, History, Outline, Problems, Variables, Verify Components views (summary) |
| Chapter 12 | Infor LN Project Server | summary | [studio_guide/ch12_project_server.md](studio_guide/ch12_project_server.md) | Project Server procedures, software projects, delivery activities, solutions, editors, perspectives and views (summary) |

## Detailed Chapter Breakdown

### [Chapter 1: LN Studio overview](studio_guide/ch01_studio_overview.md) (full)

- Functions and features *(p. 15)*
- User roles *(p. 18)*
- Current scope and limitations *(p. 19)*
- Architecture *(p. 19)*
- Troubleshooting *(p. 19)*
- LN Studio workbench *(p. 20)*
- Applications *(p. 22)*
- Cloud-specific differences *(p. 23)*

### [Chapter 2: Installation and configuration](studio_guide/ch02_installation_and_configuration.md) (full)

- First installation *(p. 25)*
- Prerequisites *(p. 25)*
- Installing LN Studio *(p. 26)*
- Selecting the workspace *(p. 27)*
- Defining connectivity settings *(p. 28)*
- Defining dynamic connection points *(p. 30)*
- Setting user preferences *(p. 32)*
- Specifying additional settings for multi-tenant cloud development *(p. 33)*
- Specifying additional settings for single-tenant cloud development *(p. 35)*
- Installing LN Studio updates *(p. 36)*

### [Chapter 3: Activity based development](studio_guide/ch03_activity_based_development.md) (full)

- Configuration Management *(p. 38)*
- Usage of SCM *(p. 38)*
- Activating SCM for a project VRC *(p. 39)*
- Activating SCM for an application *(p. 39)*
- Software components *(p. 40)*
- Development with SCM for project VRCs and applications *(p. 40)*
- VRC numbering *(p. 41)*
- CM actions *(p. 42)*
- Development without SCM *(p. 44)*
- VRC numbering *(p. 45)*
- CM actions *(p. 46)*
- Activity context *(p. 48)*
- Cleaning an activity *(p. 49)*
- Recovering an activity *(p. 50)*
- Reassigning an activity *(p. 51)*
- Linking run configurations to an activity *(p. 51)*

### [Chapter 4: Development procedure](studio_guide/ch04_development_procedure.md) (full)

- Developing software components *(p. 53)*
- Verifying software components *(p. 56)*
- Verifying software components *(p. 57)*
- Handling warnings *(p. 57)*
- Identifying problems in your code *(p. 58)*
- Sample exercise *(p. 58)*
- Running and debugging software components *(p. 60)*
- Running LN sessions *(p. 60)*
- Debugging LN sessions *(p. 62)*
- Suspending sessions *(p. 66)*
- Resuming the execution of suspended sessions *(p. 66)*
- Stepping through the execution *(p. 66)*
- Inspecting values *(p. 67)*
- Evaluating expressions *(p. 67)*
- Using breakpoints *(p. 68)*
- Running BFlow tests *(p. 72)*
- Defining log levels for BFlow events *(p. 72)*

### [Chapter 5: InContext Modeling](studio_guide/ch05_incontext_modeling.md) (summary)

- Context messages *(p. 73)*
- InContext model *(p. 73)*
- Related topics *(p. 74)*

### [Chapter 6: LN Studio Limitations](studio_guide/ch06_studio_limitations.md) (summary)

- General limitations *(p. 75)*
- Script Editor limitations *(p. 75)*
- Configuration Management (CM) limitations *(p. 76)*
- Build limitations *(p. 76)*
- Debugger limitations *(p. 77)*
- Debug View *(p. 77)*
- Variables view *(p. 77)*
- Expressions view *(p. 77)*
- Script Editor *(p. 77)*
- Watchpoint *(p. 78)*
- Web UI limitations *(p. 78)*

### [Chapter 7: Wizards and Dialogs](studio_guide/ch07_wizards_and_dialogs.md) (full)

- Activity *(p. 79)*
- Activity Information *(p. 79)*
- Activity Overview, End Activity *(p. 80)*
- Clean activity *(p. 80)*
- Open an Activity *(p. 81)*
- Reassign Activity *(p. 82)*
- Recover activity *(p. 82)*
- Recover activity *(p. 83)*
- Link Run Configurations *(p. 84)*
- Create IEX Patch *(p. 84)*
- Browse and Select *(p. 85)*
- Browse Command Sets *(p. 85)*
- Browse component *(p. 85)*
- Browse domain *(p. 86)*
- Browse Default Sizes *(p. 87)*
- Browse label *(p. 87)*
- Browse library *(p. 88)*
- Browse product ID *(p. 89)*
- Browse Queries *(p. 89)*
- Browse session *(p. 89)*
- Browse Input Fields *(p. 90)*
- Browse text field *(p. 90)*
- Browse time Format / Browse date format *(p. 90)*
- Select a Chart *(p. 91)*
- Select Component(s) *(p. 91)*
- Select Component Types *(p. 93)*
- Select a Report *(p. 94)*
- Select Table Fields *(p. 94)*
- Create a New Infor LN Software Component wizard *(p. 94)*
- Creating an additional file *(p. 96)*
- Creating a domain *(p. 101)*
- Creating a function *(p. 102)*
- Creating a label *(p. 103)*
- Creating a library *(p. 104)*
- Creating a menu *(p. 105)*
- Creating a message *(p. 106)*
- Creating a question *(p. 107)*
- Creating a report *(p. 108)*
- Creating a session *(p. 110)*
- Creating a table *(p. 111)*
- Debugging *(p. 112)*
- Execute Assignment Expression *(p. 112)*
- Line Breakpoint properties *(p. 113)*
- Method Breakpoint properties *(p. 113)*
- Watchpoint properties *(p. 114)*
- Preference Pages *(p. 114)*
- Preferences - BFlow *(p. 114)*
- Preferences - Editor *(p. 116)*
- Preferences - Launching *(p. 122)*
- Preferences - Multipage *(p. 122)*
- Views *(p. 123)*
- Preferences - Workbench *(p. 123)*
- Preferences - Infor LN Configuration Management *(p. 124)*
- Verify Software Components *(p. 125)*
- Verify Components View Filter *(p. 125)*
- Verify Warning Details *(p. 126)*
- Verify Warning Help *(p. 129)*
- Miscellaneous *(p. 130)*
- Check In comment *(p. 130)*
- Configuration Management *(p. 130)*
- Configurations *(p. 131)*
- Copy from other layouts *(p. 134)*
- Create a new Application *(p. 134)*
- Create a New Form Command *(p. 138)*
- Duplicate an Infor LN Software Component *(p. 139)*
- Application Search *(p. 141)*
- Generate Library from WSDL file *(p. 145)*
- Field Dependencies *(p. 145)*
- Create Tables *(p. 147)*
- Convert To Runtime *(p. 147)*

### [Chapter 8: Multipage Editors](studio_guide/ch08_multipage_editors.md) (full)

- Additional File Editor *(p. 151)*
- Overview tab *(p. 152)*
- TDE Documentation tab *(p. 153)*
- BFlow Editor *(p. 153)*
- General tab *(p. 153)*
- Variables tab *(p. 154)*
- Actions tab *(p. 154)*
- XML tab *(p. 155)*
- TDE Documentation tab *(p. 155)*
- Business Object Editor *(p. 155)*
- Overview tab *(p. 155)*
- TDE Documentation tab *(p. 156)*
- Domain Editor *(p. 156)*
- Overview tab *(p. 157)*
- Enum - Set Data tab *(p. 165)*
- Documentation tab *(p. 167)*
- TDE Documentation tab *(p. 167)*
- Function Editor *(p. 167)*
- Overview tab *(p. 167)*
- Source tab *(p. 168)*
- Documentation tab *(p. 169)*
- TDE Documentation tab *(p. 169)*
- Label Editor *(p. 169)*
- Overview tab *(p. 170)*
- Translation tab *(p. 173)*
- Documentation tab *(p. 174)*
- TDE Documentation tab *(p. 174)*
- Using labels *(p. 174)*
- Library Editor *(p. 174)*
- Overview tab *(p. 175)*
- Source tab *(p. 178)*
- Documentation tab *(p. 178)*
- TDE Documentation tab *(p. 178)*
- Menu Editor *(p. 178)*
- Overview tab *(p. 179)*
- Preview tab *(p. 181)*
- Documentation tab *(p. 182)*
- TDE Documentation tab *(p. 182)*
- Message Editor *(p. 182)*
- Overview tab *(p. 183)*
- TDE Documentation tab *(p. 184)*
- Messages *(p. 185)*
- Question Editor *(p. 185)*
- Overview tab *(p. 186)*
- TDE Documentation tab *(p. 188)*
- Questions *(p. 188)*
- Report Editor *(p. 189)*
- Overview tab *(p. 190)*
- Input Fields tab *(p. 194)*
- Layouts tab *(p. 197)*
- Source tab *(p. 202)*
- Documentation tab *(p. 202)*
- TDE Documentation tab *(p. 203)*
- Session Editor *(p. 203)*
- Overview tab *(p. 203)*
- Script tab *(p. 207)*
- Source tab *(p. 211)*
- User Interface tab *(p. 211)*
- Form Definition tab *(p. 214)*
- Form Commands tab *(p. 225)*
- Satellite Sessions tab *(p. 232)*
- Documentation tab *(p. 234)*
- TDE Documentation tab *(p. 234)*
- Dynamic index switching *(p. 234)*
- Multi Main Table sessions *(p. 235)*
- Session Model Editor *(p. 242)*
- Session tab *(p. 242)*
- Context Messages tab *(p. 243)*
- TDE Documentation tab *(p. 244)*
- Table Editor *(p. 244)*
- Overview tab *(p. 245)*
- Fields tab *(p. 247)*
- Indices tab *(p. 253)*
- Script tab *(p. 254)*
- Source tab *(p. 256)*
- Documentation tab *(p. 257)*
- TDE Documentation tab *(p. 257)*
- Table definitions *(p. 257)*
- Data Access Layer (DAL) *(p. 258)*
- Table InContext Model Editor *(p. 262)*
- Table tab *(p. 262)*
- Context Messages tab *(p. 264)*
- TDE Documentation tab *(p. 266)*

### [Chapter 9: Script Editor](studio_guide/ch09_script_editor.md) (full)

- Script Editor Preferences *(p. 269)*
- Source Tab *(p. 270)*
- Markers and Marker bar *(p. 271)*
- Overview ruler *(p. 274)*
- Editor shortcut menu *(p. 275)*
- Keyboard shortcuts *(p. 277)*
- Comparing Source Code Versions *(p. 278)*
- Application Search *(p. 278)*
- Application search procedure for servers with Enterprise Server 8.6 and lower *(p. 278)*
- Application search procedure for servers with Enterprise Server 8.7 and higher *(p. 279)*
- Code Assist *(p. 279)*
- Comments *(p. 282)*
- Toggling comments *(p. 282)*
- Maintenance comments *(p. 283)*
- Adding comments *(p. 284)*
- Folding *(p. 284)*
- Defining folding preferences *(p. 286)*
- Incremental Find *(p. 286)*
- Keyword Search *(p. 286)*
- Mark Occurrences *(p. 287)*
- Open Declaration *(p. 288)*
- Viewing general properties *(p. 288)*
- Viewing source code *(p. 289)*
- Functions and arguments *(p. 289)*
- Miscellaneous elements *(p. 291)*
- Quick Outline view *(p. 292)*
- Text Hovering *(p. 293)*
- ToDo Comments *(p. 293)*
- Toggle Breakpoints *(p. 294)*
- Generating Source from WSDL *(p. 294)*

### [Chapter 10: Perspectives](studio_guide/ch10_perspectives.md) (summary)

- Application perspective *(p. 296)*
- Debug perspective *(p. 297)*

### [Chapter 11: Views](studio_guide/ch11_views.md) (summary)

- Activity Explorer view *(p. 299)*
- Toolbar *(p. 300)*
- Shortcut menu *(p. 301)*
- Icons and decorators *(p. 305)*
- Breakpoints view *(p. 308)*
- Toolbar *(p. 308)*
- Shortcut menu *(p. 309)*
- Icons and decorators *(p. 309)*
- BFlow Palette view *(p. 310)*
- Component Explorer view *(p. 311)*
- Toolbar *(p. 312)*
- Shortcut menu *(p. 312)*
- Icons and decorators *(p. 313)*
- Debug view *(p. 314)*
- Toolbar *(p. 314)*
- Shortcut menu *(p. 315)*
- Icons *(p. 316)*
- Limitations *(p. 316)*
- Dependent InContext Models view *(p. 316)*
- Toolbar *(p. 317)*
- Shortcut menu *(p. 317)*
- Expressions view *(p. 317)*
- Toolbar *(p. 318)*
- Shortcut menu *(p. 319)*
- Icons and decorators *(p. 319)*
- Limitations *(p. 320)*
- History view *(p. 320)*
- Columns *(p. 321)*
- Toolbar *(p. 321)*
- Shortcut menu *(p. 322)*
- Outline view *(p. 323)*
- Toolbar *(p. 323)*
- Shortcut menu *(p. 324)*
- Icons *(p. 324)*
- Problems view *(p. 325)*
- Toolbar *(p. 326)*
- Shortcut menu *(p. 326)*
- Icons *(p. 326)*
- Progress view *(p. 327)*
- Toolbar *(p. 327)*
- Icons *(p. 328)*
- Tasks view *(p. 328)*
- Toolbar *(p. 329)*
- Shortcut menu *(p. 329)*
- Icons *(p. 329)*
- Variables view *(p. 330)*
- Toolbar *(p. 331)*
- Shortcut menu *(p. 331)*
- Icons and decorators *(p. 332)*
- Limitations *(p. 333)*
- Verify Components view *(p. 333)*
- Toolbar *(p. 334)*
- Shortcut menu *(p. 334)*
- Icons *(p. 334)*
- Table Fields view *(p. 335)*
- Shortcut menu *(p. 335)*
- Call Hierarchy view *(p. 335)*

### [Chapter 12: Infor LN Project Server](studio_guide/ch12_project_server.md) (summary)

- Procedures *(p. 339)*
- Defining a software project *(p. 339)*
- Delivering software components *(p. 340)*
- Dialogs *(p. 342)*
- Create a Software Project *(p. 342)*
- Create a new Activity *(p. 343)*
- Compile activity overview *(p. 345)*
- Open a Delivery Activity *(p. 345)*
- Create a Solution *(p. 346)*
- Add development activity *(p. 347)*
- Browse Solutions *(p. 347)*
- Browse Solution Types *(p. 349)*
- Select Component(s) for delivery *(p. 349)*
- Project Server View Filter *(p. 351)*
- Multipage Editors *(p. 351)*
- Solution Editor *(p. 351)*
- Perspectives *(p. 355)*
- Project Server perspective *(p. 355)*
- Views *(p. 355)*
- Software Project Explorer view *(p. 355)*
- Delivery Explorer view *(p. 358)*
- Glossary *(p. 361)*

## Phase 2 boundary

The *Integration Development Guide* (business interfaces, BOD modeling, hook
reference, event publishing) is **out of scope** here and tracked as Phase 2.
It must not duplicate the extensibility reference in `erp-ln-progguide`.
