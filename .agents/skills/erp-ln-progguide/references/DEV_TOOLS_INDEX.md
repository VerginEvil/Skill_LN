# Infor LN Development Tools (2016)

Reference documentation for the **Infor LN Development Tools** (Release 10.5 / 2016).
Covers the software development lifecycle, 4GL engine, Data Dictionaries (runtime vs application),
Data Access Layer (DAL 1 vs DAL 2), table reconfigurations (`crdd`), Multi-Main Table (MMT) sessions,
Software Configuration Management (SCM), Product Maintenance Component (PMC), and 4GL/session/query reporting.

## Chapters Overview

| Chapter | Title | Reference File | Key Topics |
|---|---|---|---|
| Chapter 1 | Development Tools Introduction | [ch01_development_tools_introduction.md](dev_tools/ch01_development_tools_introduction.md) | Architecture overview, developer environment, component model |
| Chapter 2 | Overview of Software Components | [ch02_overview_of_software_components.md](dev_tools/ch02_overview_of_software_components.md) | 4GL Engine, DAL 1 & 2, domains, tables, sessions, forms, MMT, queries |
| Chapter 3 | Data Dictionaries | [ch03_data_dictionaries.md](dev_tools/ch03_data_dictionaries.md) | Runtime Data Dictionary (RTDD), Application Data Dictionary (ttadv), crdd |
| Chapter 4 | Development Parameters and Authorizations | [ch04_development_parameters_and_authorizations.md](dev_tools/ch04_development_parameters_and_authorizations.md) | Development parameters, authorizations, developer access controls |
| Chapter 5 | Software Development Procedures | [ch05_software_development_procedures.md](dev_tools/ch05_software_development_procedures.md) | Development procedures: Data model, table reconfiguration, sessions, forms, MMT, translations |
| Chapter 6 | Session Personalizations | [ch06_session_personalizations.md](dev_tools/ch06_session_personalizations.md) | Session personalizations, user customizations, form views |
| Chapter 7 | Version and Release Management | [ch07_version_and_release_management.md](dev_tools/ch07_version_and_release_management.md) | Version & Release Management, Package VRCs, environments, SCM check-in/out |
| Chapter 8 | LN Software Maintenance | [ch08_ln_software_maintenance.md](dev_tools/ch08_ln_software_maintenance.md) | PMC (Product Maintenance Component), solutions, collections, patches, Feature Packs |
| Chapter 9 | LN Homepages | [ch09_ln_homepages.md](dev_tools/ch09_ln_homepages.md) | LN Homepages structure, homepage functions, resource files |
| Chapter 10 | LN Reporting Overview | [ch10_ln_reporting_overview.md](dev_tools/ch10_ln_reporting_overview.md) | Reporting overview, 4GL reports vs Report Viewer, report projects |
| Chapter 11 | 4GL Reports | [ch11_4gl_reports.md](dev_tools/ch11_4gl_reports.md) | 4GL Reports architecture, layouts, report scripts |
| Chapter 12 | Session-based Reporting | [ch12_session_based_reporting.md](dev_tools/ch12_session_based_reporting.md) | Session-based reporting, Report Viewer devices, execution flow |
| Chapter 13 | Query-based Reporting | [ch13_query_based_reporting.md](dev_tools/ch13_query_based_reporting.md) | Query-based reporting, query report designs, report libraries, print sessions |

## Detailed Chapter Breakdown

### [Chapter 1: Development Tools Introduction](dev_tools/ch01_development_tools_introduction.md)

- Development Tools introduction *(p. 17)*

### [Chapter 2: Overview of Software Components](dev_tools/ch02_overview_of_software_components.md)

- Overview of software components *(p. 19)*
- 4GL Engine *(p. 19)*
- Charts *(p. 20)*
- DAL *(p. 21)*
- DAL 1 *(p. 22)*
- DAL 2 *(p. 23)*
- Field dependencies *(p. 24)*
- Business methods *(p. 24)*
- Dashboards *(p. 25)*
- To create dashboards *(p. 27)*
- Domains *(p. 27)*
- To create domains *(p. 29)*
- Forms *(p. 29)*
- Functions *(p. 32)*
- To create functions *(p. 33)*
- Labels *(p. 33)*
- To create labels *(p. 34)*
- Libraries *(p. 35)*
- To create libraries *(p. 35)*
- User Exit DLLs *(p. 35)*
- Menus *(p. 36)*
- To create menus *(p. 37)*
- Messages *(p. 37)*
- To create messages *(p. 38)*
- MMT Sessions *(p. 38)*
- To create MMT sessions *(p. 40)*
- Questions *(p. 41)*
- To create questions *(p. 42)*
- Reports *(p. 42)*
- Report structure *(p. 43)*
- To create reports *(p. 44)*
- Report scripts *(p. 45)*
- Report script structure *(p. 45)*
- To create report scripts *(p. 46)*
- Sessions *(p. 46)*
- SQL queries *(p. 50)*
- 4GL program queries *(p. 51)*
- Stand-alone queries *(p. 51)*
- Table definitions *(p. 52)*
- Fields, domains and indices *(p. 53)*
- Related Tables and References *(p. 53)*
- To create table definitions *(p. 53)*
- UI scripts *(p. 54)*
- Event sections *(p. 54)*
- To create UI scripts *(p. 55)*

### [Chapter 3: Data Dictionaries](dev_tools/ch03_data_dictionaries.md)

- Data dictionaries *(p. 57)*
- The Runtime Data Dictionary *(p. 57)*
- The Application Data Dictionary *(p. 58)*
- Convert to Runtime Data Dictionary *(p. 58)*

### [Chapter 4: Development Parameters and Authorizations](dev_tools/ch04_development_parameters_and_authorizations.md)

- Development parameters and authorizations *(p. 61)*
- Development Parameters *(p. 61)*
- Developer Authorizations *(p. 61)*

### [Chapter 5: Software Development Procedures](dev_tools/ch05_software_development_procedures.md)

- Development process *(p. 65)*
- Design Data Model *(p. 66)*
- Implement Data Model *(p. 67)*
- Create User Applications *(p. 67)*
- Create Business Logic *(p. 68)*
- Create Menus *(p. 68)*
- Document *(p. 69)*
- Deploy Application *(p. 69)*
- Identify Changes *(p. 69)*
- To develop software components *(p. 69)*
- To create a data model *(p. 70)*
- Procedure aim *(p. 71)*
- Procedure result and prerequisites *(p. 71)*
- Procedure summary *(p. 71)*
- Procedure details *(p. 72)*
- To reconfigure tables *(p. 75)*
- Procedure aim *(p. 75)*
- Procedure result and prerequisites *(p. 75)*
- Procedure summary *(p. 76)*
- Procedure details *(p. 76)*
- To create sessions *(p. 77)*
- Procedure aim *(p. 77)*
- Procedure result and prerequisites *(p. 77)*
- Procedure summary *(p. 78)*
- Procedure details *(p. 78)*
- To create forms *(p. 79)*
- Procedure aim *(p. 79)*
- Procedure result and prerequisites *(p. 80)*
- Procedure summary *(p. 80)*
- Procedure details *(p. 80)*
- To edit forms *(p. 82)*
- To edit the form content *(p. 82)*
- To edit the form structure *(p. 85)*
- To edit the form sequence *(p. 88)*
- To create commands and buttons for a session *(p. 89)*
- To specify indices for a session *(p. 91)*
- To create a form for a print session *(p. 92)*
- Review Program Script *(p. 93)*
- Edit the Form *(p. 94)*
- To create reports *(p. 100)*
- Procedure aim *(p. 100)*
- Procedure result and prerequisites *(p. 100)*
- Procedure summary *(p. 101)*
- Procedure details *(p. 101)*
- To edit reports *(p. 103)*
- To edit report input fields *(p. 103)*
- To edit report layouts *(p. 104)*
- To edit a report script *(p. 108)*
- To create dashboards *(p. 108)*
- To create the session *(p. 109)*
- To create the program script *(p. 115)*
- To create the details sessions *(p. 119)*
- To create MMT Sessions *(p. 121)*
- To create a main entity detail session *(p. 122)*
- To create a multi-main table controller session *(p. 123)*
- To create a satellite session *(p. 124)*
- To assign satellites to the controller *(p. 125)*
- To compile and run the controller session *(p. 125)*
- To integrate the controller session *(p. 126)*
- To translate software components *(p. 126)*
- Multi-language *(p. 126)*
- To translate labels, questions and messages *(p. 127)*

### [Chapter 6: Session Personalizations](dev_tools/ch06_session_personalizations.md)

- Session Personalizations *(p. 129)*

### [Chapter 7: Version and Release Management](dev_tools/ch07_version_and_release_management.md)

- Version and release management introduction *(p. 131)*
- An overview of version and release management *(p. 131)*
- Package combinations *(p. 131)*
- Package VRCs *(p. 132)*
- Package VRC code *(p. 133)*
- LN software environment *(p. 134)*
- Standard environment *(p. 135)*
- Runtime environment *(p. 135)*
- Development environment *(p. 136)*
- VRC derivation *(p. 137)*
- Contents of a software environment *(p. 140)*
- Copy software components concept *(p. 140)*
- Export/import software components concept *(p. 140)*
- To use the Software Configuration Management system (SCM) *(p. 142)*
- SCM Groups *(p. 143)*
- To set up the SCM environment *(p. 144)*
- Sessions *(p. 144)*
- To use the SCM check-in and check-out procedure *(p. 144)*
- Procedure *(p. 145)*
- Standard software environment procedure *(p. 145)*
- Procedure aim *(p. 145)*
- Procedure result and prerequisites *(p. 146)*
- Procedure summary *(p. 146)*
- One-step software environment procedure *(p. 147)*
- Procedure aim *(p. 147)*
- Procedure result and prerequisites *(p. 147)*
- Procedure summary *(p. 148)*
- Copy software components procedure *(p. 148)*
- Procedure aim *(p. 148)*
- Procedure result and prerequisites *(p. 148)*
- Procedure summary *(p. 148)*
- Export and import procedure *(p. 149)*
- Procedure aim *(p. 149)*
- Procedure result and prerequisites *(p. 149)*
- Procedure summary *(p. 149)*
- Purge a package VRC derivation structure procedure *(p. 150)*
- Procedure aim *(p. 150)*
- Procedure result and prerequisites *(p. 151)*
- Procedure summary *(p. 151)*

### [Chapter 8: LN Software Maintenance](dev_tools/ch08_ln_software_maintenance.md)

- PMC introduction *(p. 153)*
- PMC Benefits *(p. 153)*
- PMC overview *(p. 154)*
- PMC Architecture *(p. 154)*
- Where to find the PMC module *(p. 155)*
- Dependencies *(p. 155)*
- Individual solutions *(p. 156)*
- Collections *(p. 157)*
- Feature Packs and patches *(p. 157)*
- Justification of Feature Packs and patches *(p. 158)*
- Feature Packs *(p. 158)*
- To install a 'clean' Feature Pack *(p. 160)*
- Patches *(p. 162)*
- Distributor’s Policy *(p. 163)*
- PMC Distributor functionality *(p. 163)*
- PMC Recipient functionality *(p. 164)*
- PMC distributor procedure *(p. 165)*
- Setup *(p. 165)*
- Setup procedure *(p. 165)*
- Parameters *(p. 166)*
- base VRCs *(p. 166)*
- base VRC combinations *(p. 167)*
- To create updates *(p. 167)*
- To create solutions *(p. 167)*
- To create collections *(p. 168)*
- To create patches *(p. 169)*
- To create Feature Packs *(p. 170)*
- Feature Pack development *(p. 171)*
- System setup for standard products *(p. 171)*
- System setup for derived products *(p. 172)*
- Rules to upgrade derived products *(p. 174)*
- Building Feature Packs and the Infor Installation Wizard *(p. 175)*
- Customizations *(p. 175)*
- Patches and customizations *(p. 175)*
- Feature Packs and Customizations *(p. 177)*
- Dependencies for customizations *(p. 180)*
- Other *(p. 180)*
- PMC distributor session summary *(p. 181)*
- PMC distributor sessions *(p. 181)*

### [Chapter 9: LN Homepages](dev_tools/ch09_ln_homepages.md)

- Homepages introduction *(p. 185)*
- Introduction *(p. 185)*
- Homepage structure *(p. 186)*
- To create LN homepages *(p. 188)*
- Prerequisites *(p. 188)*
- To create homepages *(p. 188)*
- To create functions for LN homepages *(p. 192)*
- Introduction *(p. 192)*
- Homepage function types *(p. 192)*
- To translate resource files *(p. 199)*
- To translate resource files *(p. 200)*

### [Chapter 10: LN Reporting Overview](dev_tools/ch10_ln_reporting_overview.md)

- LN Reporting Overview *(p. 203)*
- 4GL reports *(p. 203)*
- Report Viewer enabled reports *(p. 204)*
- To create a report project *(p. 207)*
- To use the Report Viewer *(p. 208)*
- Toolbar buttons *(p. 208)*

### [Chapter 11: 4GL Reports](dev_tools/ch11_4gl_reports.md)

- 4GL Reports Overview *(p. 211)*

### [Chapter 12: Session-based Reporting](dev_tools/ch12_session_based_reporting.md)

- Session-based Reporting *(p. 213)*
- To create session-based reports *(p. 213)*
- To create a Report Viewer device for session-based reports *(p. 217)*
- To run session-based reports *(p. 218)*

### [Chapter 13: Query-based Reporting](dev_tools/ch13_query_based_reporting.md)

- Query-based Reporting *(p. 219)*
- To create query-based reports *(p. 222)*
- To create resource files *(p. 228)*
- To link a resource file to a report design *(p. 230)*
- To create report libraries *(p. 230)*
- To link a report library to a report design *(p. 231)*
- To create a print session for query-based reports *(p. 232)*
- To run query-based reports *(p. 234)*
- To translate resource files *(p. 235)*
- To translate resource files *(p. 235)*
- Appendix A Glossary *(p. 237)*
