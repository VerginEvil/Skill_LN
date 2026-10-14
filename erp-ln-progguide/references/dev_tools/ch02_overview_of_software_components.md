# Chapter 2: Overview of Software Components

## Overview of software components

The following sections briefly describe various types of LN software components:
- 4GL Engine (p. 19)
- Charts (p. 20)
- DAL (p. 21)
- Dashboards (p. 25)
- Domains (p. 27)
- Forms (p. 29)
- Functions (p. 32)
- Labels (p. 33)
- Libraries (p. 35)
- Menus (p. 36)
- Messages (p. 37)
- MMT Sessions (p. 38)
- Questions (p. 41)
- Report scripts (p. 45)
- Reports (p. 42)
- Sessions (p. 46)
- SQL queries (p. 50)
- Table definitions (p. 52)
- UI scripts (p. 54)
## 4GL Engine

The 4GL engine handles the default behavior of a session. If additional functionality is needed or default
functionality needs to be by-passed, this should be programmed in a UI script (Program script).
When a session is started, the session’s object will run. The object and the form work together to perform
queries and present data on the form.
The sequence of actions that take place are:

1. The object allocates memory space for a record buffer based on the table definition.
2. The object builds a SQL statement to select rows from the main table and related tables. The
record buffer is populated within a selectdo loop.
3. The record buffer variables are updated after the query and are available for use on forms.
4. The form fields are mapped to the record buffer and display on the form.
This sequence of actions is an overview of the actions that take place within a session. The detailed
actions are coded. The 4GL Engine (also called the standard program) provides this standardized coding
and enforces consistency across sessions in the system.
The 4GL Engine controls the processing of a session:
- The session startup including checking for authorizations, loading icons and pull-down menus.
- Loading the forms, reports, and charts.
- Performing queries on the main table for the user’s company, which includes selects, inserts,
- Scrolling through data selections.
- Checking that a reference to another table exists, such as checking that a Department exists
- Handling the right forms, labels, and menus for a user’s language.
- Choose the device for output.
updates, and deletes.
for an Employee.
> [!NOTE]
The exceptions to the normal processing are contained in the Session Object. The session object uses
events to hook into the 4GL Engine, and describe the actions that should happen as a result of an event.
These additional actions are defined in the UI script (program script). For more information, refer to the
UI scripts (p. 54) section.
## Charts

Charts present data in a graphical format to the user. Charts are used in sessions and SQL queries. A
session can contain multiple charts. An SQL query can have only one chart.
The following default chart types are present in LN:
- Bar
- Layer
- Line
- Pie
- Scatter
- Stacked bar
See the following figure for an example:
Sample chart
For more information on charts, refer to the Infor Web Help.
## DAL

The Data Access Layer (DAL) allows developers to describe rules about data. A DAL is linked to a table,
not a session. Therefore, when the table is accessed, the DAL is used. In this way, different sessions
can update a table by using the same rules. In addition, integration capabilities use the DAL to ensure
updates are also processed with the same rules.
Data Access Layer (DAL) scripts implement the business rules of the application to ensure the logical
integrity of the database. DAL scripts are a Library software component that is aligned with a specific
table. These scripts are compiled into objects. When a session performs an action on a table, the DAL
for the table is loaded.
In LN, two types of Data Access Layer scripts exist: DAL 1 and DAL 2.
Business Rules
A business rule is a statement that defines or constrains some aspect or operation of the business. It
is intended to control or influence the behavior of the business operations. Business rules are logical
integrity rules, and differ from database oriented referential integrity rules.
Business Rules - example
Business rules in a purchasing system may be:
- An item can be ordered only from its supplier
- When the gross weight and net weight for an item are the same, there is no packaging
- The supplier provides the arrival date of a purchase order after the order is entered into the
- Items cannot be removed if there is stock on-hand
- The item on-order quantity is increased when an order for the item is entered
- The item on-hand quantity is increased and the on-order quantity decreased when an order
system.
arrives
Referential Integrity Rules - example
In contrast, integrity rules in a purchasing system may be:
- An item must exist for it to be ordered
- If an item has a supplier, the supplier must be known to the system
- Items can not be deleted if the item record is used elsewhere in the system
Business rules are implemented as hooks. A hook is a pre-defined function name that you create in a
Data Access Layer script. The 4GL engine will call this function as it executes user interface and database
related actions on the table that the DAL is written for.
Business rules fall into categories that determine how the business rule is implemented in the DAL.
The categories, depending on the type of DAL script, are:
- Property or Field hooks
- Object Hooks
- Field Dependencies
- Business Methods
### DAL 1

DAL 1 scripts were introduced in Infor Baan 5.0.0. A DAL 1 script contains database logic (e.g. logical
integrity rules), but it usually does not contain all business logic for the table it belongs to. Very often
business logic is spread across the DAL 1 script and the UI scripts.
Most UI scripts still contain business logic. They can contain, for example, logic to:
- make fields read-only.
- determine which enum constants can be selected in an enumerated field.
- update a field after a change to a related field.
Therefore it is very hard to use the DAL 1 scripts for integrations via Infor LN Business Adapter: the
business logic in the UI scripts is skipped if another application connects to a LN table. Therefore this
logic must be rebuilt in the BOIs that provide the connection. If you change the business logic in the UI
scripts, you must adapt the corresponding BOIs as well.
A DAL 1 script can contain the following types of hooks:
- Object hooks. These hooks operate on the row or record as a whole unit. Object hooks
- Delete the additional employee data in the People package when an employee is deleted.
- When a sales order line is saved, create a history record of the sales order line.
- Update the item inventory when a planned stock transaction is created.
- Property hooks. These hooks operate at a field level, and are, among other things, used to
- Validity check that the Quotation expiration date should be after the Quotation entry date.
- When adding an employee, the language of the company is the default for the employee’s
determine if operations on a row are allowed, and specify additional operations that should
be performed based on an operation of the row. Examples of object hooks are:
verify valid values and calculate default values for table fields. Examples of property hooks
are:
language.
For details on DAL 1 scripts, refer to "Data Access Layer" in the Infor ES Programmer's Guide.
To create DAL 1 scripts
You can create and edit DAL 1 scripts in the Program Scripts / Libraries (ttadv2530m000) session.
For DAL 1 scripts, the script type is "DAL".
### DAL 2

DAL 2 scripts are introduced in LN. A DAL 2 script contains all business logic (database logic + other
logic) related to a particular table. The UI scripts of the sessions operating on the table, only contain UI
logic.
DAL 2 scripts are therefore perfectly suited for integrations via Infor LN Business Adapter. Other
applications can connect, through Business Objects, to LN tables. The business logic in the table's DAL
2 script is executed automatically. So, to build an integration, you don't need to rebuild this business
logic in the BOIs that provide the interface.
Various predefined Business Objects, that can be used for integration purposes, are delivered with LN.
DAL 2 scripts are only available for tables that are used in these business objects. For the remaining
tables, DAL 1 scripts are available. Refer to the Infor LN Business Adapter documentation for details
on business objects and integration technology.
In DAL 2 various new hooks are introduced. A DAL 2 script can contain:
- Object hooks: these hooks are identical to the object hooks in DAL 1 scripts.
- Field hooks. Field hooks contain the business logic for table fields. They can contain, for
- verify valid values on a table field (logical integrity rules).
- make a field read-only. For example: the contact field of the Business Partner is not a
- make a field invisible.
- automatically update a field, after a related field was changed. See "Field Dependencies".
- make input on a field mandatory.
- hide a particular enumerated constant from an enum list.
- Business method hooks. These hooks are used to disable/enable and hide specific form
example, logic to:
required entry, and is a display field in the UI when the Business Partner is created.
commands of type "business method".
For details on DAL 2 scripts, refer to "DAL 2 Overview" in the Infor ES Programmer's Guide.
To create DAL 2 scripts
You can create and edit DAL 2 scripts in the Program Scripts / Libraries (ttadv2530m000) session.
For DAL 2 scripts, the script type is "DAL (version 2)".
### Field dependencies

In DAL 2 scripts, you can define field dependencies that are used to determine default values. Once
these field dependencies are defined, dependent fields update themselves when the fields that they
depend on are updated. The field updates are defined in the DAL as a field hook.
Dependencies are also used to update the User Interface. The 4GL Engine uses these field dependencies
to disable and enable fields, and to determine enum values.
Examples of field dependencies are:
- The packing field of the Item is yes if the gross weight and net weight of the item are different.
- An item without a gross weight cannot have a net weight and packing. A field dependency is
A field dependency is defined so that the packing field is updated if the gross or net weight
fields change.
defined so that the net weight and packing fields are disabled if the gross weight is zero.
### Business methods

Business Methods are operations on a row or set or rows within a table. A business method is a function
that performs a task that involves manipulating or checking one or more tables in the database.
Sessions, object hooks or property hooks from another table’s DAL can call a business method. For
more information, refer to the Infor ES Programmer's Guide.
Examples of business methods are:
- The sales order line session can remove an order line. The object hook for deleting the sales
- In the Purchase Order session, check if it is allowed to change a purchase order header based
- If a purchase order issues components, the object hook for the purchase order line calls a
order line calls a business method to also remove the unpaid commissions.
on the purchase order status and the business partner status.
business method to issue the components for the purchase order. The business method inserts
items of the bill of material into a purchase order components table.
## Dashboards

Dashboard sessions are used to quickly access multiple sessions that are related to a specific object.
Examples of objects are item, work center, or project. Through a dashboard, users such as engineers
or shop floor planners can easily carry out all tasks related to their jobs. Relevant details of the object
are presented on the dashboard, as well as the possibility to open the sessions in which additional
information for the object is stored.
To summarize, the dashboard gives the user a quick overview of the status of a specific object without
having to open all related sessions immediately. With a dashboard, a user can easily perform a specific
task.
This diagram shows the sections in a dashboard:
Customer 360 (tdsmi1500m000) dashboard
A dashboard session consists of these sections:

1. Details
The Details section shows information about the object.
If you select a record in the list in the lower part of the session (3), the record's details are
displayed in the Details section (1).
2. Links
A series of links (2) is displayed to start sessions that are related to the session's object. A
check mark indicates whether the link already contains information related to a selected record
of the object.
Click the links to display, maintain, or create information related to an object's record.
3. Records
For the dashboard's object (3), a number of records is listed.
If you select a record, the record's details are displayed in the Details section (1), and you can
click the links (2) to display, maintain, or create information related to a record.
For more information on dashboards, see the Infor Web Help.
## To create dashboards

For details on how to create dashboards, see To create dashboards (p. 108) .
## Domains

Domains define common information about data such as data type, length, alignment, valid ranges,
display format, and capitalization rules.
Domains insure consistent data types for fields and variables. Domains can be linked to table fields,
form fields, and program variables.
The following table shows some domains of the tc (Common) package.

Domains for tc package
Domain
Description
Type
date
Date
UTC Date/Time
emno
Employee Num -String
ber
relc
Reconciliation El -String
ement
reop
Reorder Point
Long
rntp
Run Type
Enumerated
rutm
Run Time in Min -Double
utes
The following figure shows the details of the tc emno (Employee Number) domain.
Domain properties Example
Domains of type Enumerated or Set have constants with language-dependent descriptions. Each constant
has three characteristics:
- Numeric value that is stored in the database
- Constant Name that the programmer can use
- Constant Description that provides the description of the option to the user, in the language
of the user
For example: the tc styp (Schedule type) domain has the following constants:

Constant
Constant Nam eDescription
1
not.applicable
Not Applicable
2
pull
Pull Schedule
3
push
Push Schedule
## To create domains

You can create domains in the Domains (ttadv4500m000) session.
See To create a data model (p. 70) .
## Forms

The form is the user interface part of the session. Forms, which are presented to users, include data
and actions that users can perform on that data. The session and form are integrated; one form per
session is defined. The form definition in the session identifies the fields, labels, and options that are
available in the session's overview display window and details window.
Example
Field groups allow certain fields to be displayed together within a box, or within a tab. The Item – General
session contains more than one tab.
Item - General
Example
Some sessions can fit all their fields on one tab, like the Countries detail session.
Countries
A Form provides the rules for the user dialog, or panel, that is displayed. You create and edit sessions
and forms using the Sessions (ttadv2500m000) session. This session acts as a Developer’s workbench
as it provides access to all the major components of a session.
To create forms
To create and edit forms, you must use the Infor LN Dynamic Form Editor that is part of Development
Tools. This is a PC based application that should be installed for each developer. The Infor LN Dynamic
Form Editor also provides access to the major components of the session.
The form editor allows you to specify the available session types for the form (overview and detail), the
field groups, labels and fields that are used to create the form.
The form that is presented to the user is created dynamically:
- The form layout is used to determine the labels and fields, the grouping of the fields, and the
- The table field authorizations of the user insure that only fields that the user is allowed to view
- The mode the session is started in determines if the session is in overview mode or details
sequence of the fields.
are shown on the form.
mode.
For details, refer to
- To create sessions (p. 77)
- To create forms (p. 79)
- To edit forms (p. 82)
- To create commands and buttons for a session (p. 89)
- Dynamic sessions and dynamic forms
For more information, refer to the following topics in the Infor Web Help:
## Functions

Functions allow you to perform a programming task multiple times with different values. A function is
declared in the functions section of a script, in a library, or in a separate function script (include).
The possibilities for calling a function depend on how the function is declared:
- If a function is declared in the declaration section of a script, you can only call the function
- If a function is declared in a library, or in a separate function script, you can call the function
within that script.
in multiple scripts and libraries.
For more information, refer to "Functions" in the "3GL Language Features" section in the Infor ES
Programmer's Guide.
Example
The supplier session calculates the cumulative order volume within the last 30, 60 and 90 days. You
declare a function that can perform this calculation for any range of days. The function has a type so
that it can be used in an expression.
function domain cxquan supplier_volume(long day1,long day2)
{
... commands here ...
return( ... )
}
If the function is declared as a type, it must provide a return value. You call this function using the syntax:
vol_30 = supplier_volume(0,30)
vol_60 = supplier_volume(30,60)
## To create functions

To create a function in a program script or in a library, you must edit the script/library via the Program
Scripts / Libraries (ttadv2530m000) session. If you define a function in a library, you must link that
library to the scripts and libraries where you want to call the function.
To create a function in a separate function script:(include), you must create the function script through
the Functions (ttadv2560m000) session. You must include this function script (through an "#include"
statement) in the scripts and libraries where you want to call the function.
## Labels

A label is a code that is used instead of language-dependent text in forms, reports, and menus. A label
consists of a name and a content description. The content of a label can differ by language, but the label
name remains the same for all languages.
Labels in a report-layout
For each label code, you can specify:
- A label description. This is the label text which you can edit and translate.
- The length. This is the number of characters of the description.
- The height. This is the number of lines of the description.
Multiple descriptions, with different lengths and heights, can exist for the same label code. See the
following table for an example:

Label cod eLanguage
Height
Length
Description
ttttaad501.se -1 (Dutch)
qu
1
6
Volgnr
ttttaad501.se -1 (Dutch)
qu
1
10
Volgnummer
ttttaad501.se -1 (Dutch)
qu
2
6
Volg-%nummer
ttttaad501.se -2 (English)
qu
1
6
SeqNo.
ttttaad501.se -2 (English)
qu
1
12
Sequence
No.
ttttaad501.se -2 (English)
qu
2
8
Sequence%Number
> [!NOTE]
A % sign in the description indicates a line break. For example: when you place the label with the
"Sequence%Number" description in a report layout, the label is displayed as:
Sequence
Number
When you place a label on e.g. a form or a report layout, you can edit the label length requirements
within the form field / report field. In this way you can make sure that the appropriate version of the label
(e.g. the shorter version) is used in the form / report.
## To create labels

You can create labels in the Labels (ttadv1140m000) session.
If you create new labels, you must compile these in the Compile Labels (ttadv1243m000) session so
that Infor Enterprise Server can display the new labels at run time.
For more information, refer to the Infor Web Help.
## Libraries

A library, also called Dynamic Link Library (DLL), provides application-specific functions that can be
used throughout the system, by many sessions. A library is a script that is stored in a separate component.
The library is compiled independently of the program scripts that use it. Libraries are loaded at runtime
by sessions that use them. When a session needs to access a library, the library is loaded, and the
relevant routine is executed.
## To create libraries

You can create and edit libraries in the Program Scripts / Libraries (ttadv2530m000) session.
Libraries are a type of program script. The program script code should start with “dll” and the script type
should be “General Library”. This helps categorize the scripts into their general use.
> [!NOTE]
You edit and compile a library the same way that you edit and compile a program script. When you
create a function in a library, you should consider these differences:
- When you name the function, precede the function name with the library name.
- Functions are declared as EXTERN.
- The DllUsage / EndDllUsage block is used to communicate how the library function can be
used. This text will be displayed when you generate the library documentation or perform a
bic_info on the resulting object file.
For more information, refer to "Dynamic-link libraries" in the "3GL Language Features" section in the
Infor ES Programmer's Guide.
### User Exit DLLs

LN supports the use of User Exit DLLs. Customers can implement User Exit DLLs to create extra business
logic, without having to change the standard LN software. The business logic in a User Exit DLL is
automatically executed before and after the standard 'before' and 'after' handling of save and delete
actions. In this way, you can conditionally publish data changes to the outside world.
A User Exit DLL meets these conditions:
- The name of the DLL consists of the table code with "ue" as suffix. For example, tccom001ue
- The DLL includes bic_dal, as follows: #include <bic_dal>
- ue.after.after.destroy.object()
- ue.after.before.save.object()
A User Exit DLL (UEDLL) contains specific hooks, such as the following:
In these hooks, you define the extra business logic to be executed. For 4GL sessions, the hooks are
executed just before and after the corresponding defined standard sections/hooks of the UI script and/or
DAL script. For 3GL scripts and DLLs, the hooks are executed just before and after the corresponding
database operation, such as db.insert, db.update, or db.delete.
> [!NOTE]
The business logic in a User Exit DLL should not change the standard functionality of the LN software;
for example, these DLLs are only intended for integration purposes, or to perform extra steps.
## Menus

Menus are used to organize the LN sessions in a logical folder / subfolder structure. The folders and
subfolders usually represent LN packages and modules. The Menu browser is used to open the folders
and subfolders in order to find the sessions. Sessions can be launched directly from the Menu browser.
The Menu browser is used in Infor Ming.le, Infor ES Web UI, and Infor WorkTop.
LN users can have their own customized menus. The start menu for a user must be defined in the User
Data (ttaad2500m000) session.
Menu navigation in Infor Ming.le- pull-down menus
Menu navigation in Infor Ming.le- Enterprise Navigator context application
Menu navigation in Web UI
## To create menus

To create menus you must use the Menus (ttadv3560m000) and Menu Fields (ttadv3561m000) sessions.
See the "Creating menus" topic in the Infor Web Help.
## Messages

Messages are language-independent software components that allow you to customize dialog messages.
For each message, you can specify:
- The message code. This is the unique identifier of the message across all languages.
- The message type, e.g. "Warning".
- The message. This is the message text which you can edit and translate. This message can
contain codes that are substituted when the message is displayed. For details on substitution
symbols, refer to the description of the sprintf$() function in the Infor ES Programmer's Guide.
See the following table for a sample message:

Message
Message code
Message Type
Language
tipcss0292
Warning
1 (Dutch)
Artikel reeds aanwezig
als component in productiestuklijst
2 (English)
Item already found as
component in production
BOM
Messages are used in a variety of places within the application. You can use messages:
- To replace the default reference error message on table definitions
- Within program scripts and libraries
- To set error messages from a DAL
- As the contents of a form field using the form.text$ function
If a message is produced while a session is executing, a dialog box is displayed, and you must click OK
to continue. If the session is running in a job, the message is logged in the job history messages.
## To create messages

You can create messages in the Messages (ttadv4551m000) session.
For more information, refer to:
- the Infor Web Help
- the Message Handling subtopic in the Functions topic in the Infor ES Programmer's Guide
## MMT Sessions

A multi-main table session shows multiple tables and allows you to perform maintenance commands
on the main entity and the child tables. Hence, the term “multi-main table”.
A multi-main table session shows detailed information for a main entity. Additional tabs are available
that show related tables to the entity.
Example
Customer service representatives use the Sales Order - Lines (tdsls4100m900) session to enter,
display and process sales orders. When the representative opens an order:
- The order header is displayed
- The order lines are displayed
- Other information that is related to the sales order number is displayed on additional tabs.
Sales Order Multi-Main Table Session
You can identify a multi-main table session from the two tool bars: the first toolbar is associated with
the sales order header, and the lower toolbar is associated with sales order lines, deliveries and so on.
You can create or edit an order or an order line.
Structure
The appearance of the multi-main table session is determined by the following:
- The multi-main table controller session is a maintain session for the main entity. The form of
this session determines the top portion of the session.
- In addition to the standard tool bars for maintenance of the main entity, an addition icon is
- Satellite sessions are displayed as tabs. The form of the satellite session determines the fields
- The title of the tab is the session name of the satellite session.
- The “label of object” field shows in the Lines menu and other menus.
provided. The details icon will open a details session for the main entity. This session is the
synchronized dialog for the controller session.
that are displayed in the session. A satellite session can have multiple tabs within the session.
Multi-Main Table Session Structure
For more information on MMT sessions, refer to the Infor Web Help.
## To create MMT sessions

You can create MMT sessions using the Sessions (ttadv2500m000) session. This session enables
you to create and link all the major components of an MMT session. For details, refer to To create MMT
Sessions (p. 121) .
## Questions

Questions are language-independent software components that are used to ask situation-dependent
questions to which the user must respond. At runtime, the questions are displayed in the language that
is specified for the current user.
Sample question
For each question, you can specify:
- The question code. This is the unique identifier of the question across all languages.
- The question type, e.g. "Warning".
- The question. This is the question text as it is shown when activated. The question text can
- The domain belonging to the question, and the default answer. The domain determines the
contain codes that are substituted when the question is displayed. For details on substitution
symbols, refer to the description of the sprintf$() function in the Infor ES Programmer's Guide.
possible answers to the question. The domain must have the Enumerated data type.
This table shows a sample question:

Question code
Question Type
Domain
Language
Question
ttaad31022
Warning
ttyeno
1 (Dutch)
Device geblokkeerd, opnieuw
proberen?
2 (English)
Device is locked,
try again?
## To create questions

You can create questions in the Questions (ttadv4561m000) session.
You can use questions within program scripts and libraries using the ask.enum() function.
For more information, refer to:
- the Infor Web Help
- the description of the ask.enum() function in the Infor ES Programmer's Guide
## Reports

Reports are used to show data on the screen, or print it on a printer or other output device. Reports are
used in (print) sessions and SQL queries. A session can have multiple reports. When you run a session
that has multiple reports, a list of available reports is displayed. An SQL query can have only one report.
Example
The Print Items - General (tcibd0401m000) session has multiple reports:
- Items - General (Details)
- Items - General (Summary)
- Items - General (General)
When you click Print in this session, you must select one of these reports.
Print Items - General - report selection
When you select the Items - General (Summary) report, this report is printed:
Items - General (Summary) report
### Report structure

LN reports contain one or more of the following layouts:
Layout
Description
Before.re -Layouts of this type are printed once at the beginning of the report. This layout can be used
to present information about the report. For example, the title page of the report.
port
Header
Header layouts are printed at the top of every page.
You can define this layout for each input field for which a Sort Mode is defined in the Report
fore.fiel dInput Fields (ttadv3532m000) session. Each time the value of the sorted input field changes,
this layout is printed before the Detail lines. In this way the records are grouped. If a group
of records spans more than one page, the before.field layout is repeated at the top of the
new page (following the header).
Be-
Detail
Detail layouts are used for the individual records included in the body of the report. They are
printed every time that data is sent to the report.
After.fiel dYou can define this layout for each input field for which a Sort Mode is defined in the Report
Input Fields (ttadv3532m000) session. Each time the value of the sorted input field changes,
the layout is printed after the detail lines. In this layout, the presorted input field still contains
the old value. This layout, for example, can be used to print totals for a particular group of
detail lines.
Footer
Footer layouts are printed at the bottom of each page.
This layout is used to print:
- Titles
- Page numbers
- Page totals
After.re -This layout is only printed at the end of the report, and after all other layouts. If this layout
does not fill a complete page, the footer layout will be printed at the bottom of the page,
where the After.report layout(s) is printed.
port
The contents and layouts of reports are defined in the data dictionary. In addition, you can link a report
script to a report. In a report script, you can program actions that you want to be performed at particular
stages of the report execution. For example, you can create a script to perform calculations on the report
data or to read records from related tables that are not automatically available to the report.
You program report scripts in the same way as you program 4GL program scripts, except that report
scripts use different event sections and some special functions.
## To create reports

You can create reports in the Reports (ttadv3530m000) session and in the Report Generator
(ttadv3130s100) session. You can start these sessions from the Sessions (ttadv2500m000) session
and from the Sessions (ttadv2100s000) session respectively.
You can change the report layout in the Report Editor that is part of Development Tools.
For details, refer to To create reports (p. 100) .
For more information, refer to the following topics in the Web Help:
- Reports Overview
## Report scripts

A report script allows you to customize the processing of the report. A report script consists of event
sections in which you program actions to be performed at particular states of execution of the report.
The statements programmed in a report script section consist of a combination of 3GL language
statements and report script functions.
You program report scripts in the same way as you program 4GL program scripts, except that report
scripts use different event sections and some special functions.
Report scripts allow you to:
- Perform additional queries
- Calculate complex print expressions
- Aggregate complex print expressions
- Update rows in the database
- Add fields from tables that are not queried by the program script, when you are not able to
- Manipulate pre-defined variables in the report, such as if the layout should be printed or not.
### Report script structure

A report script consists of one or more event sections in which you program actions to be performed at
particular states of execution of the report. The statements programmed in a report script section consist
of a combination of 3GL language statements and report script functions.
Report scripts support the following event sections:
- program sections, e.g. declaration, before.program, and after.program.
- report sections that correspond to a layout, e.g. before.report, header, and detail. Report
- text field sections
manipulate the program script
sections can be processed before a layout, or after a layout.
The report script is compiled automatically with the report when you compile the report.
> [!NOTE]
For details on Report scripts, refer to "Report Script Features" in the Infor ES Programmer's Guide.
Predefined variables used in a report are also listed.
## To create report scripts

You can create and edit report scripts in the Reports (ttadv3530m000) session.
For more information, refer to the following topics in the Web Help:
- Reports Overview
## Sessions

A session performs an activity. Sessions are used to present data, edit data, and process data. Each
session has a code. The session code is displayed in the status bar of the session window. A session
consists of multiple components that work together, such as a form and an object. A session object is
a compiled UI script.
Overview session and details session
An overview session shows multiple rows from a table in a grid. Overview sessions are also called
Multi-Occurrence sessions, because they display multiple records, or occurrences, from the same table.
Scroll bars allow you to view rows above or below the current rows that are displayed in the grid. Based
on security authorizations, you are able to insert, edit, copy, and delete entries in the grid.
Overview session
A details session shows one row and is also called a single-occurrence session. The details session is
opened when you insert, edit or copy from the overview session. The details session allows you to edit
individual field values and save your changes. The session may also have additional options that can
be performed using buttons, icons or specific menu options.
Details session
Synchronization
The details session is a synchronized dialog of the overview session. Synchronized sessions work
together.
- When the details record changes, the overview session will show the changes if the affected
fields are on the overview session form.
- When a record is selected in the overview session, the details session will show the selected
record.
Usually the overview session and the details session are two separate sessions, for example: the Items
(tcibd0501m000) overview session and the Items (tcibd0501m000) details session. See the previous
figures.
However, the overview session and the details session can be the same session. For example the
Employees - General (tccom0101m000) session can run as an overview session and as a details session.
You use the form editor to indicate the fields that appear in the overview session, and which fields appear
in the details session.
Employees - General (tccom0101m000) - overview session
Employees - General (tccom0101m000) - details session
Structure of a Session
A session is a collection of system components that work together to perform a task. Each component
will have a unique identifier, or code, to distinguish it from other components. The system components
include:
- Form
- Table definitions
- Reports
- Charts
- An object that is a compiled UI script
Components of a session
To create sessions
You can create and edit sessions and forms using the Sessions (ttadv2500m000) session. This session
acts as a Developer’s workbench as it provides access to all the major components of a session. For
details, refer to To create sessions (p. 77) .
For more information on sessions and forms, refer to the following topics in the Infor Web Help:
- Dynamic sessions and dynamic forms
- Session Synchronization
- To implement dynamic index switching
- Multi Main Table sessions
## SQL queries

Queries are the backbone of a database-oriented application. You use Structured Query Language
(SQL) to retrieve information from the database.
LN supports multiple Relational Database Management Systems. Each database system is supported
in the architecture by using a driver: a database specific program that translates SQL syntax from the
SQL used in the object to the SQL used by the database system.
In LN the following types of SQL queries are used:
- 4GL program queries
- Stand-alone queries
## 4GL program queries

You can create queries in 4GL scripts or libraries, e.g. in a UI script, a report script, a DLL or a DAL.
These queries can read and update data in the database. At runtime, the queries are triggered during
session execution, for example by an event or by a form command.
> [!NOTE]
There are two ways to use LN SQL in an LN 4GL program. You can embed it in the language (embedded
SQL), or you can create queries using 4GL functions (dynamic SQL). For more information, refer to the
"SQL programming" subtopic in the " LN SQL" topic in the Infor ES Programmer's Guide.
An embedded query starts with a SELECT statement that allows you retrieve a selection of data from
a number of tables based on conditions defined in the WHERE clause.
The SELECT statement has the general syntax:
SELECT columns ...
FROM table(s) ...
WHERE each row fulfills the condition(s) ...
The columns you select are typically table fields that are selected from tables. The where clause in an
embedded query allows you to specify conditions using either columns that are selected or based on
variables declared in your program script. The rows you select can be processed individually within a
selectdo loop. The selectdo loop provides an iteration mechanism for the records selected by the SELECT
statement.
For details, refer to " LN SQL" in the Infor ES Programmer's Guide.
To create or modify queries in a 4GL script or library, you must use the Program Scripts / Libraries
(ttadv2530m000) session.
## Stand-alone queries

A stand-alone query is a query that is not embedded in any other software component, and that is
executed independently.
Stand-alone queries can only read data from the database. A stand-alone query cannot add, delete, or
update records in the database.
The general structure of a stand-alone query is:
SELECT                 For the examples the statements are
<select list>         written in capitals. In the Text
Editor both uppercase and lowercase
letters can be used.
FROM
<from list>
[WHERE
<where condition>
[GROUP BY
<group condition>
[HAVING
<having condition>
]
]
]
[ORDER BY
<order list>
]

The output of a stand-alone query is sent to a report or to a chart.
You can create stand-alone queries in the Query Data (ttadv3580m000) session. This session enables
you to create queries with Easy SQL or with the Text Manager:
- Easy SQL helps users with insufficient knowledge of the structure of the data model to define
- The Text Manager enables you to create more complex queries.
- via the Query Data (ttadv3580m000) session
- via the Execute Query (ttadv3280m000) session
- from a menu. You must first add the query, as a menu field of type "Query", to a menu.
queries in a simple, menu-driven way.
You can execute stand-alone queries in the following ways:
For details, refer to the Infor Web Help.
## Table definitions

A table definition defines the structure of a table. A table definition contains fields and indices. Table
fields are linked to domains that define the data type and several characteristics of the fields.
Table Data Example
## Fields, domains and indices

A table has fields. Table fields store individual pieces of data such as a customer name, the quantity of
an item ordered, or the date that a journal entry was made.
Table fields are linked to domains. Domains are components that define common information about
data such as:
- the data type, e.g. a character type for customer name, a number type for quantity, and a date
- valid ranges, or
- special characteristics such as capitalization rules.
type for journal date,
Domains insure consistent data types for similar table fields.
Table Fields and Domains Example
A table must have at least one index. An index consists of one or more table fields that are used to sort
and search records in the table. The first index is always the Primary key, which is the unique identification
for a record in a table.
## Related Tables and References

The table may have a related table. A related table means that a field in the table will refer to the key
field of another table. In this way, data can have relationships: customers can have orders; inventory
stores items in warehouses; and employees work in a department. You can use a tool in the Enterprise
Modeler to create diagrams from these defined relationships.
## To create table definitions

You can create table definitions in the Table Definitions (ttadv4520m000) session.
For details, refer to To create a data model (p. 70) .
## UI scripts

The default behavior of a session is handled by the 4GL engine. If you require additional functionality
or want to bypass the default functionality, you program your changes in the session's UI script (Program
script). The UI script is compiled in the session object. The object contains only the exceptions to the
normal operating procedures of the system. The 4GL Engine executes the normal operating procedures
of the system, and you write the exceptions.
The UI script contains events to hook into the 4GL Engine, and describe the actions that should happen
as a result of an event. Events trigger code. When the session runs and an event triggers, the 4GL
Engine uses the session object to perform the appropriate actions.
Actions that could take place as the result of an event are:
- Calculate a field value before a field displays.
- Synchronize the current (parent) session with a child session when you run a form command.
- Send a file to the user’s PC when you save a record.
For example: a parent session that uses the Orders table is synchronized with a child session
that uses the Order lines table.
The syntax of the UI script contains complete programming syntax capabilities such as variable
declarations, expressions, operators, transfer of control, iterations (loops), functions, embedded SQL,
and a full featured functions library.
> [!NOTE]
As a developer, you must be diligent to provide only user interface elements in the UI script. Logical
integrity and business logic elements will be added in the Data Access Layer (DAL).
## Event sections

UI scripts consist of one or more event sections in which you program actions to be performed at particular
states of execution of the 4GL Engine. It is not necessary to program all sections; only those for which
you need to provide the required functionality. The statements programmed in a section can be a
combination of 3GL/4GL functions and 3GL statements.
The event sections are categorized. A section type consists of a main section and, for most section
types, subsections. A main section indicates the object for which the programmed actions must be
executed. A subsection specifies when the actions must be executed. The section types are:

Section Type
Main section
Subsections
Program
Yes
No
Zoom From
Yes
Yes
Form
Yes
Yes
Group
Yes
Yes
Choice
Yes
Yes
Field
Yes
Yes
Main Table
Yes
Yes
Field sections are only used for non-table fields, table fields are handled by the DAL script.
Main table sections must not be used anymore, because the logic for the Main table is done via the
DAL.
For more information, refer to the "Event sections" subtopic in the "4GL Language Features" topic in
the Infor ES Programmer's Guide. The related help topic for the Flow of the 4GL engine is useful for
advanced developers to understand event loops and the sequence of events in the 4GL engine.
## To create UI scripts

You can create and edit UI scripts in the Program Scripts / Libraries (ttadv2530m000) session. When
you create a new session in the Sessions (ttadv2500m000) session, a corresponding UI script is
generated automatically.
