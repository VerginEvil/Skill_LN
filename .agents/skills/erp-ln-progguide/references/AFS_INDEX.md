# Infor Integration - Application Function Server (AFS) Developer's Guide

Full text of *U8627B US - Infor Integration 6.2 - Developer's Guide for Application
Function Server* (76 pages) in Markdown. Covers AFS architecture and all `stpapi.*`
4GL-engine primitives used to drive Baan/LN sessions from code (function-server /
DAL-before-DAL automation).

Source PDF: `U8627B US - Infor Integration 6.2 - Developer_s Guide for Application Function Server.pdf`.

| File | Content |
|---|---|
| `afs/about_this_guide.md` | Scope, audience, related documents |
| `afs/ch01_introduction.md` | Introduction, scope, definitions/acronyms |
| `afs/ch02_application_function_server.md` | AFS architecture, AFS-DLL structure, compilation |
| `afs/ch03_baan_4gl_engine_primitives.md` | All `stpapi.*` primitives (below) |
| `afs/ch04_special_issues.md` | Field buffer/field loop, message handling, multi-occurrence/single-occurrence dialogs, multi-main table sessions, debugging, text management |
| `afs/ch05_guidelines_for_baan_4gl_application_sessions.md` | `api.mode`, messages, `choice.again()`, hidden functionality, commands |
| `afs/appendix_a_afs_dll_example.md` | Complete AFS-DLL example source |
| `afs/appendix_b_stpcreatdll.md` | `StpCreatdll` helper session |

## Baan 4GL engine primitives (`stpapi.*`)

File: `afs/ch03_baan_4gl_engine_primitives.md`

- **Get Field Value from session**
  - `void stpapi.get.field (string session, string field, ref string value, [long element])`
- **Set Field Value in session**
  - `void stpapi.put.field(string session, string field, string value, [long element])`
- **Clear All fields**
  - `void stpapi.clear(string session)`
- **Insert Record in session**
  - `long stpapi.insert (string session, long do.save, ref string err.mesg)`
- **Update Record in session**
  - `long stpapi.update(string session, long do.save, ref string err.mesg)`
- **Delete Record from session**
  - `long stpapi.delete(string session, long do.save, ref string err.mesg)`
- **Save Session Updates to database**
  - `long stpapi.save(string session, ref string err.mesg)`
- **Recover Session updates**
  - `long stpapi.recover(string session, ref string err.mesg)`
- **Set Current Record for session**
  - `long stpapi.find(string session [, ref string err.mesg])`
- **Mark Current Record for session**
  - `long stpapi.mark(string session [, ref string err.mesg])`
- **Browse Session records**
  - `long stpapi.browse.set(string session, string option [, ref string err.mesg])`
- **Set Current View for session**
  - `long stpapi.change.view(string session [, ref string err.mesg])`
- **Browse Session Views**
  - `long stpapi.browse.view(string session, string option [, ref string err.mesg])`
- **Synchronize Multi-occurrence and Single-occurrence sessions**
  - `long stpapi.synchronize.dialog(string session, string mode, ref string err.mesg)`
- **Send Start processing command to session**
  - `void stpapi.continue.process(string session, ref string err.mesg)`
- **Set Session Report parameters**
  - `void stpapi.set.report(string session, string reportname, string device, ref string err.mesg)`
- **Send Print command to session**
  - `void stpapi.print.report(string session, ref string err.mesg)`
- **End session**
  - `void stpapi.end.session(string session [, ref string err.mesg)`
- **Execute session user option**
  - `void stpapi.application.option(string session, long form, long option, ref string err.mesg)`
- **Execute session zoom option**
  - `void stpapi.zoom.option(string session, long form, string zoom.prog, ref string err.mesg)`
- **Execute session form command**
  - `void stpapi.form.command(string session, long command.type, string command.prog, ref string err.mesg)`
- **Specify actions for subsessions**
  - `void stpapi.handle.subproc(string session, string sub.prog, string action)`
- **Get Messages from session**
  - `string stpapi.get.mess.code(string session [, ref string err.mesg])`
- **Set answers to questions in session**
  - `void stpapi.enum.answer(string session, string question, bset answer)`
- **Change Sort Order**
  - `long stpapi.sort.by(string session, string sortorder, ref string err.mesg)`

## Special issues topics

File: `afs/ch04_special_issues.md`

- To start application sessions
- Field buffer
- Field loop
- Field buffer as input
- Field buffer as output
- Message handling
- Introduction
- Functions
- Message array
- Generated error messages
- Again Choice.again()
- Form commands
- Messages from AFS and 4GL-Engine
- Multi-occurrence/Single-occurrence
- To insert records
- To update records
- To run form commands
- To retrieve data from a synchronized dialog box
- Multi-Main table sessions
- Debugging
- Text management

## Architecture topics

File: `afs/ch02_application_function_server.md`

- Architecture
- Explanation diagram:
- Explanation of the example
- Structure of the AFS-DLL
- Compilation
