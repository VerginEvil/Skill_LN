# Chapter 5: Software Development Procedures

## Development process

Developers use the Infor LN Development Tools to develop the software components that make up the
application.
There is a logical progression in developing the components to create an application. The development
process explains this progression.
The Flow: Development Process
The development process steps are:
### Design Data Model

The data model design begins with identifying the entities within the data model, the attributes of the
entities and the primary keys of the entities. The elements of the data model are created in Development
Tools.
The data model is normalized so that each entity has a unique primary key, all necessary relations are
defined, and data redundancy is reduced.
The data model design process will result in a data model consisting of:
- Table Definitions that define the entities in the data model.
- Fields of tables that define the attributes of the tables. Each field will also have a domain,
- Foreign key relationships to other tables.
which is a definition of the data type, format and field validation rules. Labels are initially created
based on the field description.
- Indices that can be primary keys and alternate keys.
For details, refer to To create a data model (p. 70) .
Diagram Data Model
The diagram of the data model can be created at this point. The foreign key relationships are used to
show the relationships between tables.
For details, refer to To create a data model (p. 70) .
Implement Business Rules
Business rules are implemented in the Data Access Layer. The rules can be based on the fields, or the
record. These rules form the core of the business logic that affects the user interface of the application.
Property hooks or field hooks operate at a field level and can be used to determine if the field should
be displayed, verify valid values, calculate default values and update field values.
Object hooks operate on the row or record as a whole unit. Object hooks determine if an operation on
a row is allowed, and if additional operations should be performed on the row or an operation should be
performed on another table.
Business Methods can be implemented in the Data Access Layer. Business Methods are operations
that process a row or set or rows within a table. In order to expose business logic to external applications,
the preferred method of implementing this type of processing logic is within a library. The interface to
the library is implemented through Infor LN Studio.
For details, refer to DAL (p. 21) .
### Implement Data Model

The data model is implemented by creating tables for a company. The tables for a company are created
based on the table definitions that are active for the company’s package combination.
For details, refer to To create a data model (p. 70) .
### Create User Applications

The user applications are created. The main focus of this phase of component development is to create
user-oriented panels that list, create, modify and delete data based on the table definitions.
Create Sessions and Forms
Sessions are the tasks that execute. Forms are the user interface part of the sessions. Forms specify
the fields and labels that allow users to view and manipulate data.
For details, refer to To create sessions (p. 77) .
Create Reports
Reports format and output data from a session. Reports can contain logic such as subtotals, counts and
totals based on the data that is processed.
For details, refer to To create reports (p. 100) .
Create UI Scripts
User Interface (UI) Scripts assist the developer in providing user interface logic for a specific session.
The object and property hooks/field hooks in the DAL of the table will be active when the session
executes. The UI script provides the additional opportunity to the developer to specify logic. UI Scripts
should be session specific.
Examples of UI Script actions are:

1. Import values from another session.
2. Perform a query for a report.
3. Specify what happens when a button is clicked.
For details, refer to UI scripts (p. 54) .
### Create Business Logic

Business Logic is operations that process a row or set or rows within a table. Business Logic is not
session specific, and is implemented within a library. A session or hook can initiate the business logic.
An interface to the business logic is implemented in the Infor LN Studio. This interface allows external
applications to execute the business logic.
Business logic can be implemented as Association Logic or Aggregation Logic.
- Association logic is implementing a related table. For example, the order session requires a
- Aggregation logic is implementing a parent-child table relationship. For example, an Order
business partner, and the logic depends on the business partner data.
Header process can update all the Order Lines for the order.
The Association and Aggregation Logic are programmed in a Dynamic Link Library (DLL). The interface
to the library is implemented via Infor LN Studio.
For details, refer to Libraries (p. 35) .
### Create Menus

After the sessions, forms and business logic is complete, the user needs a way to start the sessions. A
menu is created with options for starting sessions or other menus.
For details, refer to Menus (p. 36) .
Create Business Processes
Sessions form an ordered procedure for completing a business task. This procedure is implemented as
a Business Process in the Enterprise Modeler application.
For details, refer to the Enterprise Modeler documentation.
### Document

Developers have a number of tools within the application development environment to document their
work. Developers can create technical documentation at the component level based on the component,
the release, or implement customization projects to identify components created for a specific project.
User context driven help documentation can be created for deployment in the Web Help application.
For details, refer to the Infor Web Help.
### Deploy Application

Exporting the software components from the development environment and moving the components to
a production server deploy the application. Components are imported to a production server.
For details, refer to Export and import procedure (p. 149) .
### Identify Changes

As businesses change, and workflow processes adapt and improve, application requirements change
over time. As changes are identified, application components can be added, changed or expired to suit
the business requirements.
## To develop software components

You develop software components using a variety of tools within Development Tools. To develop these
components you use a common procedure to identify, establish version control for, check-out, change,
compile and execute components in your development activities.
Components are VRC Controlled. Since you are not able to change standard components, you can
either
- Create a new component.
- Copy components to a VRC and make changes to the copy, not to the original component.
- Copy a Component to a new Component.
> [!NOTE]
When SCM is active, you must check out a component before you can change it. You must check in
the component when it is finished. For details, refer to To use the Software Configuration Management
system (SCM) (p. 142) and to To use the SCM check-in and check-out procedure (p. 144) .
Create new component
To create a new component, insert a record in the component development session. For example: to
create a new session, insert a new record in the Sessions (ttadv2500m000) session.
Copy component to make changes
To copy a component to make changes, you copy the component to a Current Package VRC. You keep
the component code in this process.
To copy a component to a Current Package VRC:

1. Start a component editing session.
2. On the appropriate menu, select Change Current Package VRC of User. Ensure your current
Package VRC is set to the correct Package and VRC.
3. Select the component you wish to copy from.
4. On the appropriate menu, select Copy to Current P-VRC.
The component is in your current Package VRC and can be edited.
Alternatively, you can copy components in bulk from one Package VRC to another. You can use the
Copy Software Components to New Package VRC (ttadv6265m000) session to copy components
from one Package VRC to another.
Copy component to new component
There are instances in the development process when you wish to re-use a component in creating a
new component.
To copy an existing component to a new component:

1. Start a component development session.
2. Use the Duplicate command to duplicate the component. Specify a new component code.
The new component is in your current Package VRC.
## To create a data model

This topic describes the procedure to create a data model.
> [!IMPORTANT]
The sections below describe the sessions that you must use to complete the procedure. However, they
do not describe all details of these sessions. For detailed session information, refer to the Infor Web
Help.
### Procedure aim

LN uses a database system to store the data required by the application. Data is stored in tables in a
relational database management system (RDBMS). The data dictionary describes the data model of
the data required in the application.
You use Development Tools to define the data dictionary and create:
- Domains
- Table Definitions, including fields, labels, foreign key relationships and indices
- Tables to store data, for one or more companies, based on the table definitions
You can use the Entity Relationship Diagrams (tgerm1500m000) session in the Enterprise Modeler
to create a graphic design of the relational data model structure. The diagram shows a (multilevel)
structure that consists of entity types and entity type relationships. For details, refer to the Infor Web
Help.
> [!NOTE]
The LN data dictionary is an active data dictionary. This means that sessions that use a table will discover
the fields, domains, relationships, indices and other information about a table when the table is used at
runtime, not at compile time. This feature allows you to change data dictionary items without recompiling
code.
### Procedure result and prerequisites

#### Result

A data model for an LN application.
#### Prerequisites

To create a data model you need:
- A development package VRC in which you can create the domains and table definitions.
- Developer authorization for this VRC.
### Procedure summary

The following list shows the procedure steps and the corresponding sessions:

1. Create domains - Domains (ttadv4500m000)
2. Create table definitions, including fields, labels, foreign key relationships and indices - Table
Definitions (ttadv4520m000)
3. Convert the domains and table definitions to the runtime data dictionary - Convert to Runtime
Data Dictionary (ttadv5215m000)
4. Create tables to store data - Create Tables (ttaad4230m000)
### Procedure details

Step 1: Create domains
To create a domain:

1. Start the Domains (ttadv4500m000) session.
2. Add a row. Enter the data type, length, format and field validation rules for the domain in the
Domains (ttadv4100m000) details session.
3. Perform this step only if the data type is Enumerated or Set:
- In the Domains (ttadv4500m000) overview session, select the domain and on the
- Note: The constant description should be no longer than the defined length of the domain.
appropriate menu, click Enum/Set Data. The Enum/Set Constants (ttadv4501m000)
session starts. Enter the values for the constants, names and descriptions.
If a description is longer than the domain length, you can increase the domain length.
4. Save the new data and close the sessions.
Step 2: Create table definitions
To create a table definition:

1. Start the Table Definitions (ttadv4520m000) session.
2. Click New to start the Table Definitions (ttadv4120s000) details session. Enter the basic
table information, such as the table code and description. Save the changes and return to the
overview session..
3. Define the table fields:
- Open the new table. The Table Definitions (ttadv4520m100) session will open. This
- In the Table Fields tab, click New Table Field. The Table Fields (ttadv4122s000) details
session is a multi-main table session showing the Table Fields, Indices and Program
Scripts / Libraries for the table.
session starts. Enter the table field information. Specify, among other things, a field code,
a domain, a label, and (optionally) a reference to another table. For details, refer to the
session's online help.
- When finished, save the changes and return to the Table Definitions (ttadv4520m100)
multi-main table session.
4. Define one or more indices:
- In the Indices tab, click New Index. The Table Indices (ttadv4121s000) session starts.
- Add a row. Enter the index information, such as the index number, description and the
index parts (table fields).
5. Save the new data and close the sessions.
Points of attention:
Labels
As you enter table fields, labels will be created for
the table field descriptions. You can create a new
labels, or use existing labels. Using existing labels
provides an easy method to adapt your companies
terminology and aid translation activities.
After labels are created, you must compile the labels
so that users can use the labels as they execute
the system. You should compile labels after you
create enumerate domains, tables, sessions and
forms, reports, and other components. To compile
labels, use the Compile Labels (ttadv1243m000)
session.
Reference tables
When you specify the fields for a table, you can
define references to other tables. For this reason,
it is helpful to create tables, that will be referred to
by other tables, first.
Combined fields
Table fields can refer to a primary key of another
table. In this way, the references are built into the
data dictionary.
To define a reference to a table whose primary key
contains more than one field, you must use combined fields. Combined fields require that you define
the combined field in the reference table and in the
referring table. Combined fields are only used in
defining tables; actual fields are not created within
the database.
To create a combined field:
1. Create a new table field and, in the field properties, select the Combined Field attribute.
2. Click Child Fields to start the Child Fields
by Combined Field (ttadv4523m000) session.
3. Enter the table fields that make up the combined field.
4. Use the combined field as the first index of the
reference table.
In the field properties of the combined field in the
referring table, you can now define a reference to
the reference table.
Example:
A purchase order line for an item can have more
than one arrival at the warehouse. For this reason,
the table design requires that an arrival table is a
child of the purchase order line table. The primary
key of the purchase order line table can be viewed
as order number and position number. The arrivals
table must have a field that can refer to order number and position number. Therefore, a combined
field is used. The combined field “cmba” is created
in both tables, with the order number and position
number as the child fields. In the field properties of
the "cmba" field in the arrivals table, a reference to
the purchase order line table is defined.
Step 3: Convert the domains and table definitions to the runtime data dictionary
The table definitions are maintained in the application data dictionary. You must make the new domains
and table definitions available to the runtime environment. This process is called Convert to Runtime.
A convert to runtime is performed for tables, domains and sessions based on the package combination.
The process will search the Package VRCs of the packages in the package combination and create the
table and domain runtime files in the runtime data dictionary directory on the application server. This
directory is established when you create the package combination.
To convert to runtime:

1. Start the Convert to Runtime Data Dictionary (ttadv5215m000) session.
2. Select the Domains and Tables check boxes. Specify the appropriate ranges of package
combinations, packages and tables.
3. Click Convert.
Step 4: Create tables to store data
Tables store data. In order to store data, the table definition is used to create a table in the underlying
database for a specific company number. In most companies, a person designated as the system
administrator or database administrator will create tables.
Before you create tables, the following pre-requisites must be in place:
- The data dictionary must be converted to runtime for the package combination.
- Your LN user id must use the package combination of the company.
- A company must be created with your package combination.
- The database administration and storage requirements must be setup to create tables in the
appropriate database and storage area.
To create tables:

1. Start the Create Tables (ttaad4230m000) session. Optionally, you can start this session from
the appropriate menu in the Table Definitions session.
2. Specify the appropriate ranges of companies, packages and tables.
3. Click Create.
## To reconfigure tables (crdd)

This topic describes the procedure to reconfigure tables (`crdd`).
> [!IMPORTANT]
The sections below describe the sessions that you must use to complete the procedure. However, they
do not describe all details of these sessions. For detailed session information, refer to the Infor Web
Help.
### Procedure aim

When you change the table definitions, or the corresponding domains, for tables that already exist in
the database, you must reconfigure the tables according to the new table and domain definitions.
A table configuration process will perform these actions:
- Unload data that is in the existing table, for all companies in the package combination
- Drop the existing table, for all companies in the package combination
- Create the table according to the new table and domain definitions
- Re-load the data into the table
This is a process that you will want to control when and who performs the reconfiguration activity. You
can separate the convert process and the reconfigure process.
### Procedure result and prerequisites

#### Result

The structure of the tables in the database matches the new table and domain definitions.
#### Prerequisites

A table reconfiguration requires exclusive access to the table, because the system will drop the table.
### Procedure summary

To execute the convert and reconfigure process as 2 separate steps:

1. Convert the data dictionary information to runtime - Convert to Runtime Data Dictionary
(ttadv5215m000)
2. Reconfigure the tables in conjunction with the DBA or system administrator - Convert to
Runtime Data Dictionary (ttadv5215m000)
> [!NOTE]
You must log off and log on again to use the new tables.
### Procedure details

Step 1: Convert the data dictionary information to runtime
Run the Convert to Runtime Data Dictionary (ttadv5215m000) session with the following selection
settings:

Selected
Check Box
Domains
Yes
Tables
Yes
Reconfigure Tables
No
Step 2: Reconfigure the tables
To reconfigure the tables in conjunction with the DBA or system administrator, run the Convert to
Runtime Data Dictionary (ttadv5215m000) session with the following selection settings:

Check Box
Selected
Domains
No
Tables
No
Reconfigure Tables
Yes
## To create sessions

This topic describes the procedure to create sessions.
> [!IMPORTANT]
The sections below describe the sessions that you must use to complete the procedure. However, they
do not describe all details of these sessions. For detailed session information, refer to the Infor Web
Help.
### Procedure aim

The aim of this procedure is to create sessions for your LN application. Sessions are the main applications
that a user will use. Sessions are used to present data, edit data and process data.
Session development involves defining the attributes of a session, editing the form layout, and specifying
the specific commands and indices.
> [!IMPORTANT]
You will add the user interface logic and processing logic in later steps.
### Procedure result and prerequisites

#### Result

Sessions that perform activities in your LN application.
#### Prerequisites

To create sessions you need:
- A development package VRC in which you can create the sessions.
- Developer authorization for the development VRC.
- A data model with tables on which the sessions will operate.
- The Dynamic Form Editor ( DFE) must be installed on your PC.
### Procedure summary

The following list shows the procedure steps and the corresponding sessions or programs:

1. Add a session - Sessions (ttadv2500m000)
2. Create and edit the form - Dynamic Form Editor ( DFE)
3. Specify session specific commands and buttons - Form Commands (ttadv3518m000)/ Standard
Commands (ttadv3110s000)/ Dynamic Form Editor ( DFE)
4. Specify indices - Available Indices by Session (ttadv2101s000)
5. Add the user interface logic and processing logic. You can define this logic in the session's
UI script, in functions, DLLs and DALs.
### Procedure details

Step 1: Add a session
To create a session you must add a session code in your development package VRC:

1. Start the Sessions (ttadv2500m000) session.
2. Click New. The Sessions (ttadv2100s000) details session starts.
3. In the Attributes tab, specify the session attributes, for example: the session code, the session
description and the session type. For details, refer to the session's online help.
4. Complete the session on the Form tab. Here you must specify, among other things, the number
of occurrences and the default button.
5. Click Save.
Step 2: Create and edit the form
To create and edit forms, you must use the Infor LN Dynamic Form Editor. The form editor allows you
to specify the available session types for the form (overview and detail), the field groups, labels and
fields that are used to create the form.
To start the Dynamic Form Editor:

1. In the Sessions (ttadv2500m000) session, select the session for which you want to create or
edit the form.
2. Click Edit Form .... The Dynamic Form Editor starts.
You can now perform basic form editing tasks to quickly produce a working session prototype. For details
about creating a new basic form for a session, refer to To create forms (p. 79) .
After you have a basic form setup and operational, you can change the form layout to achieve the final
result. For details, refer to To edit forms (p. 82) .
Step 3: Specify session specific commands and buttons
In addition to labels, fields and field groups, you can enhance the user interface by creating additional
elements, such as zoom buttons, standard commands, and form commands, on the form.
For details, refer to To create commands and buttons for a session (p. 89) .
Step 4: Specify indices
Specify the indices that must be available for the session.
For details, refer to To specify indices for a session (p. 91) .
Step 5: Add the user interface logic and processing logic
You can define this logic in the session's UI script, in functions, DLLs and DALs. For details, refer to the
following sections:
- UI scripts (p. 54)
- Functions (p. 32)
- Libraries (p. 35)
- DAL (p. 21)
## To create forms

This topic describes the basic form editing tasks that allow you to quickly produce a working session
prototype. From the basic setup, you will be able to change the form layout to achieve the final result.
> [!IMPORTANT]
The sections below describe the sessions that you must use to complete the procedure. However, they
do not describe all details of these sessions. For detailed session information, refer to the Infor Web
Help.
### Procedure aim

The aim of this procedure is to create forms for your LN sessions. Forms are the user interface part of
the sessions. Forms are used to interact with the user by presenting data and actions that can be
performed on that data.
To create and edit forms, you must use the Infor LN Dynamic Form Editor ( DFE). The form editor allows
you to specify the available session types for the form (overview and detail), the field groups, labels and
fields that are used to create the form.
### Procedure result and prerequisites

#### Result

Basic forms for your (new) LN session prototypes.
#### Prerequisites

To create forms you need:
- Sessions for which you can create forms
- Developer authorization for the development VRC where the sessions are stored.
- The Dynamic Form Editor ( DFE) must be installed on your PC.
### Procedure summary

The following list shows the procedure steps and the corresponding sessions or programs:

1. Start the Editor - Sessions (ttadv2500m000)
2. Specify Available Session Types - Dynamic Form Editor
3. Add Fields - Dynamic Form Editor
4. Save the Form - Dynamic Form Editor
5. Show Session Prototype - Dynamic Form Editor
6. Exit the Editor - Dynamic Form Editor
7. Compile the Form - Sessions (ttadv2500m000)
8. Start the Session - Sessions (ttadv2500m000)
### Procedure details

Step 1: Start the Editor
To start the Dynamic Form Editor:

1. Start the Sessions (ttadv2500m000) session.
2. Select the session for which you want to create the form.
3. Click Edit Form .... The Dynamic Form Editor starts.
Step 2: Specify Available Session Types
When you create a form, you must specify if the session is available as an overview session, a details
session or both.
To specify the available session types:

1. Open the properties for the session. Click Properties. The Session Properties dialog box is
started.
2. Select the available session types: select Details Session, Overview Session, or both.
Additional attributes control the placement of field groups. For details about the fields in the
dialog, refer to the Dynamic Form Editor's online help.
Step 3: Add Fields
Add table fields: on the Insert menu, click All Table Fields. The fields of the session's main table are
added to the form.
Alternatively, to select individual fields, you can click TableFields on the Insert menu.
The fields and their associated label will display within field groups.
Step 4: Save the Form
To save the form, click Save.
Step 5: Show Session Prototype
You can view the effect of your changes from within the form editor: On the File menu, click Show
Overview Session. The overview session starts. If you wish to view the details session, click Show
Details Session.
Alternatively you can exit the editor, and then compile the form and start the session from the Sessions
(ttadv2500m000) session.
Step 6: Exit the Editor
To exit the editor, click Save and Exit.
Step 7: Compile the Form
You must compile the form to create a form dump within the runtime data dictionary.
To compile the form:

1. In the Sessions (ttadv2500m000) session, select the session to which the form belongs.
2. Click Compile.
Step 8: Start the Session
You can start the session from within the developer’s workbench.
To start the session:

1. In the Sessions (ttadv2500m000) session, select the session.
2. Click Compile.
## To edit forms

After you have a basic form setup and operational, you can change the form layout to achieve the final
result. Form edit tasks are performed in the context of the basic form edit procedure.
Many of the typical form editing operations are outlined here, grouped by general area:
- To edit the form content describes the labels and fields that are displayed
- To edit the form structure describes the grouping of fields and the tabs that are displayed
- To edit the form sequence describes the order and relative placement of labels and fields
> [!IMPORTANT]
For detailed information on the Dynamic Form Editor, refer to the Dynamic Form Editor's online help.
### To edit the form content

Form layout changes affect the labels and fields that are presented on the form.
To specify fields for overview and detail sessions
You can specify, per individual field, whether the field must be displayed in the overview session, the
details session, or in both sessions:

1. Right-click a form field, and on the shortcut menu click Properties. The Field Properties
dialog starts.
2. On the Position tab, select whether the field is displayed in the Details session or in the
Overview session or in both sessions.
Select Details and Overview Session
3. To move to the other fields, click the navigation buttons in the dialog.
You can view the effect of your changes from within the form editor: On the File menu, click Show
Overview Session. The overview session starts. If you wish to view the details session, click Show
Details Session.
To add a field
You can add a field to a form based on these conditions:
- The field is defined in the main table of the session.
- The field is defined in a reference table of the main table.
- The field is defined in the program (UI) script.
To add a field to the form:

1. Select the field that is before the field you wish to add. On the Insert menu, click Field. A new
field, with a label icon, is added.
2. Edit the field properties. Define the field name and attributes in the General tab. If the new
field is a table field, you can select it from a list:
- Click the zoom button next to the Field Name field. The Table Fields (ttadv4529m000)
- Select a table field. If the field is not in the main table, use the Find button to select a
session starts.
different table.
3. Define additional properties for the field. If a field is a reference only field, you can clear the
Label Code field in the Label tab to remove the label.
4. Depending on the importance of the field, you can select if you want the field to be displayed
in the overview session, the details session or both.
5. The new field is displayed in the Dynamic Form Editor. An indented field indicates that the
field is a “child” field. Child fields display next and to the right of parent fields, at the same
indentation level as fields that have the same parent. To change the indentation of a field, use
the Right and Left buttons in the editor's toolbar.
6. Save the form.
Indent Field
Checkbox Appearance
An enumerated domain that has two values can be viewed as a checkbox. The default appearance is
a drop-down list box.
To change the appearance of an enumerated domain:

1. In the field properties for the field with the enumerated domain, select the Appearance tab.
2. Select Check Box.
Enumerate Check Box
When you show the details session, the result shows the field with the enumerated domain as a checkbox.
Alternatively, you can change the appearance of the domain for any form for an enumerated domain.
To do so, insert the domain in the Domains to be Displayed as Checkbox (ttgfd4520m000) session.
### To edit the form structure

The structure of the form affects the grouping of fields and tab labels.
To add a field Group
A field group has a title. The fields in the field group are shown within an indented list.
To create a field group:

1. On the Insert menu, click Group.
2. A new group, with a folder icon, is added. The group is added immediately below the selected
field. If you need to, use the Up and Down arrow buttons to position the field group.
3. Click Properties to start the Group Properties dialog. Enter a label for the new group, and
specify the other group properties. For details about the fields in the dialog, refer to the Dynamic
Form Editor's online help.
4. Click OK. The field group label will change in the form editor.
5. Use the arrow buttons to move the fields into the group.
Group properties
Move fields into group
To align groups and fields
Field group alignment and field alignment are important in determining the layout of the form. Because
the form generation is dynamic, this alignment is the main way to control the placement of labels and
fields on the form.
Groups and field placement depends on the indentation level of the field groups, subgroups and fields.
The indentation level of a group determines if the group is a tab, or a field group (sub-group) within a
tab. Sub-groups can be aligned next to each other.
The indentation level of the field determines if the field is placed on a new line (on the left side of the
form), or as a field to the right of a previous field. The alignment of fields in columns depends on the
group alignment selection of the field group that the fields belong to.
To adjust the indentation level of field groups and fields, use the left and right arrow buttons.
Example- Field Alignment for Items
The Items form has many fields. In the Weights field group, you want the net weight to be placed to the
right of the gross weight field. You change the indentation level for the net weight field to be one level
to the right.
Field Alignment for Items
This diagram shows the result:
Field Alignment Result
Example- Group Alignment
The General group/tab in the Items form contains two sub-groups: the Weights group and the Stock
Values group. To place these sub-groups next to each other:

1. Edit the properties of the General group: specify 2 in the Subgroups next to each other field.
2. In the properties of the Weights group, select Next to other Group.
3. In the properties of the Stock Values group, select Next to other Group.
This diagram shows the result:
Group Alignment Result
The tab sequence for fields in subgroups allows you to tab through the fields in the first subgroup before
tabbing to fields in the second sub-group.
### To edit the form sequence

The sequence of the form allows you to present the data relative to its importance to the organization.
You can sequence field groups or fields. To change the sequence of a field group or field, select the
item and use the Up and Down buttons in the editor's toolbar to move the item. Alternatively, you can
drag and drop the item.
Example- Field Sequence for Items
You move the purchase price field above the supplier information, and the packing field to the Weights
field group.
The result shows the desired sequence of the fields.
Field Sequence Result
For more information on group and field alignment, refer to "Alignment" in the Dynamic Form Editor's
online help.
## To create commands and buttons for a session

You can enhance the user interface of a session by creating additional elements on the form. Some of
these elements are:
Element
Description
Zoom button sallow you to view and select a record from a reference table.
Standard
Commands
control the active toolbar icons and pull-down menu options.
Form Commands
allow you to specify options in the appropriate menu.
Form Button sallow a user to invoke a command by pressing a button.
Field Button sallow a user to perform a task related to a field.
Group Button sallow a user to perform a task related to a field group.
Secondary
Toolbars
allow form commands to start by clicking icons in a second toolbar. You use the create.extra.toolbar function within the program script to create the toolbar. For details,
refer to the Infor ES Programmer's Guide.
To add a zoom button
A zoom button appears next to a field. It is usually used to start an overview session for a reference
table, where the user is able to select a value and return to the session, and the selected value is shown
as the field value.
Example- Zoom on Item Group
In the Items session, the item group field can have a zoom button to the Item Groups session.
To add a zoom button to the form:

1. In the Dynamic Form Editor, edit the field properties for the form field.
2. Use the Zoom tab to specify action when the zoom button is pressed.
For details, refer to the Dynamic Form Editor's online help.
To edit standard commands
Standard commands control the active toolbar icons and pull-down menu options for a session.
To edit the standard commands:

1. In the Dynamic Form Editor, click Standard Commands on the Tools menu. Alternatively,
click Standard Commands on the appropriate menu in the Sessions (ttadv2500m000) session.
The Standard Commands (ttadv3110s000) session starts.
2. Select the available standard commands from the defined lists of commands. If an option is
selected, the option will appear on the session’s toolbar and menus.
3. Click OK.
Add Form Command
A form command is a session specific command. The user can invoke a form command using a command
in the appropriate menu, a form button, a field button or a group button. You create all these elements
in the same way, but use different command types to determine how the command is presented to the
user.
To create a form command:

1. In the Dynamic Form Editor, click Form Commands on the Tools menu. Alternatively, click
Form Commands on the appropriate menu in the Sessions (ttadv2500m000) session. The
Form Commands (ttadv3518m000) session starts.
2. Click New. The Form Commands (ttadv3118s000) details session starts.
3. Enter the values for the command. For details, refer to the session's online help.
4. Click Save and Close.
Form commands are typically added in conjunction with other sessions or with program script elements,
such as functions.
## To specify indices for a session

Session indices allow users to use the defined indices for a table within the session. In the user interface,
indices help users sort and categorize groups of records within a table. Web UI users can change the
index using the Sort by option in a session's View menu. Infor Ming.le users can change the index using
the down arrow next to the Search button.
Example- Indices for the Sales Orders table
The Sales Orders table has multiple indices. When these indices are active for the session, the user
can sort by the indices.
Index Change in Infor Ming.le
The indices of the table can be active for a session. An index that has more than one field can be defined
to show the first fields as a view field. A view field allows users to select only those rows that contain
the view field value within their index value.
Example- View field
The Sold-to BP index for the Sales Orders table has two fields: Sold-to Business Partner and Order.
When the user changes the index to the Sold-to BP index, the form layout changes: the Sold-to Business
Partner field is displayed as a view field above the grid. This automatic change of the form layout is
called Dynamic Index Switching.
Index Change Result
For more information, see To implement dynamic index switching in the Infor Web Help.
To specify the indices for a session
To specify the indices for a session:

1. In the Dynamic Form Editor, click the Indices command on the Tools menu. Alternatively,
click Indices... on the appropriate menu in the Sessions (ttadv2500m000) session. The
Available Indices by Session (ttadv2101s000) session starts.
2. Select the indices that you wish to have available. For each index, specify the order that the
index will show in the Sort by window, and the number of fields in the view field.
3. Click OK.
## To create a form for a print session

When you create a print session, you must also create the form for the session.
The form is used to enter selection ranges and processing options.
- Selection ranges specify a lower and upper range. Ranges are typically used for key fields or
alternate key fields. The fields that are inserted on the form need to correspond to the program
script variables that are used in the main SQL statement that selects rows from the database.
You can extend the SQL statement to add additional range variables.
- Processing options are used to specify additional conditions for selecting rows, or for specifying
the sort order. Some processing options will change the report group number so that a different
report is selected automatically for the user.
> [!IMPORTANT]
For detailed information on the Dynamic Form Editor, refer to the Dynamic Form Editor's online help.
## Review Program Script

Before you create the form, it is helpful to review the program script. This is particularly true if you created
the program script when you created the print session. The program script will contain the default
selection ranges.
You may have to extend the generated program script to query references to parent tables.
See the following program script for an example:
|**********************************************************
|* cxoes0421  0  VRC B61U a  dv00
|*
|* Development User
|* 2005-02-07
|**********************************************************
|* Main table cxoes021 Suppliers, Form Type 4
|**********************************************************

|****************************** declaration section *******
declaration:
table   tcxoes021 | Suppliers
table   tcxoes031 | Countries
extern  domain  cxsuno           suno.f    fixed
extern  domain  cxsuno           suno.t    fixed
|****************************** program section ************
|****************************** group section **************
group.1:
init.group:
get.screen.defaults()
|****************************** choice section *************
choice.cont.process:
on.choice:
execute(print.data)
choice.print.data:
on.choice:
if rprt_open() then
read.main.table()
rprt_close()
else
choice.again()
endif
|****************************** field section ***************
field.suno.f:
when.field.changes:
suno.t = suno.f
|****************************** function section ************
functions:
function read.main.table()
{
select cxoes021.*, cxoes031.*
from cxoes021, cxoes031
where   cxoes021._index1 inrange {:suno.f}
and {:suno.t}
and     cxoes021.ccty refers to cxoes031
order by cxoes021._index1
selectdo
rprt_send()
endselect
}
## Edit the Form

Create the form for the print session. While you can create a form in a variety of ways, this procedure
shows you how a typical form is setup for a print session.
Step 1: Insert a Group
To insert a group in the form:

1. In the Sessions (ttadv2500m000) session, select the session for which you want to create the
form.
2. Click Edit Form .... The Dynamic Form Editor starts.
3. Insert a group for selection ranges.
Insert Group
Step 2: Insert Labels
Insert a label only field, with the label corresponding to “From”. Note that the position indicator is “above”.
See the following table for an example of the Field Properties:

Input Value
Field
Field Name
label.only
Use Field as Label
Only
Yes
Label Code
ttgen.from
Position
Above
Insert a second label only field with a label code corresponding to “To”. The “To” label field is a child of
the from label field.
See the following table for an example of the Field Properties:

Field
Input Value
Field Name
label.only
Use Field as Label
Only
Yes
Label Code
ttgen.to
Position
Above
Insert Label Fields
Step 3: Insert Selection Fields
The selection fields you insert on the form must correspond to the variables that are used in the main
SQL statement in the program script.
Insert the "From" field corresponding to the first selection field. This field is denoted as a table field name
appended with a “.f”.
See the following table for an example of the Field Properties:

Field
Input Value
Field Name
suno.f
Use Field as Label
Only

Domain
cx suno
Form Field
Yes, fmin($#)
Label Code
oes021.suno
Position
Before
Zoom
Session
Zoom To
cxoes0121m000
Return Field
cxoes021.suno
Insert the "To" field corresponding to the first selection field. This field is denoted as a table field name
appended with a “.t”.
See the following table for an example of the Field Properties:

Field
Input Value
Field Name
suno.t
Use Field as Label
Only

Domain
cx suno
Form Field
Yes, fmax($#)
Label Code

Position

Zoom
Session
Zoom To
cxoes0121m000
Return Field
cxoes021.suno
Insert Selection Range Fields
Step 4: Edit Standard Commands
Click Standard Commands on the Tools menu. The Standard Commands (ttadv3110s000) session
starts. Edit the Standard Commands for the form so that the following commands are available:

Commands
Available
Modify Record(s)
Yes
Print Report
Yes
Cancel
Yes
Make Job
Yes (Optional)
Save Defaults
Yes (Optional)
Get Defaults
Yes (Optional)
Step 5: Save the form
Save the form.
You can view the effect of your changes from within the form editor: On the File menu, click Show
Details Session. The session starts.
Form Result
Save and Exit the form.
## To create reports

> [!IMPORTANT]
The sections below describe the sessions that you must use to complete the procedure. However, they
do not describe all details of these sessions. For detailed session information, refer to the Infor Web
Help.
### Procedure aim

The aim of this procedure is to create reports for your LN application. Reports are used to print data to
the screen, to a printer or to another output device.
### Procedure result and prerequisites

#### Result

Reports to print data from your LN application.
#### Prerequisites

To create reports you need:
- A development package VRC in which you can create the reports.
- Developer authorization for the development VRC.
### Procedure summary

The following figure shows the procedure steps and the corresponding sessions or programs:
To create reports - procedure flow
While not part of the flow, you may also have to edit the program script to complete your report.
### Procedure details

Step 1: Create a report or create a session
You can create a new report for an existing print session, or create a new print session with a
corresponding report.
To create a report:

1. Start the Reports (ttadv3530m000) session.
2. Click New.
3. You will be asked if you want to start the report generator. Click Yes to start the generator.
- Note: If you click No, you must create the report manually. In that case, skip the "Generate
report" step in this procedure and proceed with the "Edit report" step.
Alternatively, you can also create a report by duplicating an existing report.
To create a new print session:

1. Start the Sessions (ttadv2500m000) session.
2. Click New. The Sessions (ttadv2100s000) details session starts.
3. Enter the new session. A print session should have at least these attributes:
- Session Type: Print
- Default Button Command Type: Standard Command
- Default Button: Print.data
4. Save the new session. Do not close the Sessions (ttadv2100s000) details session.
5. Click Report Generator to start the generator.
Step 2: Generate report
You can generate a (basic) report. Subsequently, you can edit the generated report until the report
matches your requirements.
To generate a report:

1. Start the report generator. You can start the report generator from the Reports (ttadv3530m000)
session and from the Sessions (ttadv2100s000) session. See the previous step in this
procedure.
2. Edit the report generator options: You must specify the main table and the fields for the report,
and various other attributes, such as the report code, the report size, and the report type. For
details refer to the online help of the Report Generator (ttadv3130s100) session.
- Note: to select fields, you must click Select Fields. The Select Report Fields
(ttadv3130s200) session starts. Select the fields you wish to output in the report, and click
Save and Close to return to the report generator.
3. Click Generate. The report is compiled automatically.
Step 3: Edit report
You can now edit the report until it matches your requirements. You can, among other things, add new
layouts to the report, edit the layouts in the report editor, change the sorting and/or grouping of records,
and create a report script.
For details, refer to To edit reports (p. 103) .
Step 4: Compile
Click Compile in the Reports (ttadv3530m000) session. A Compilation result window opens with the
result of the compilation.
Step 5: Link report to session or create and edit form
When you create a new report for an existing print session, you must link the report to that session.
To link a report to an existing session:

1. In the Sessions (ttadv2500m000) session, select the session you wish to link the report to.
2. On the appropriate menu, click Reports.... The Reports (ttadv3530m000) session starts.
3. On the appropriate menu, click Link Report to Session. The Add Report to Session
(ttadv2112s000) session starts.
4. Specify the Report Group, the Serial Number, and the report code you wish to link to the
session. For details, refer to the Infor Web Help.
5. Click OK. The report is now displayed in the reports list for the session.
6. Exit the Reports session.
7. In the Sessions (ttadv2500m000) session, click Compile. This action converts the new session
structure to the runtime dictionary.
When you create a new report as part of a new print session, the report is automatically linked to the
new session. Before you can print the new report, you must create a form for the new print session. For
details, refer to To create a form for a print session (p. 92) .
## To edit reports

This topic describes the following report editing operations:
- To edit report input fields
- To edit report layouts
- To edit a report script
> [!IMPORTANT]
The sections below describe the sessions that you must use to edit reports. However, they do not
describe all details of these sessions. For detailed session information, refer to the Infor Web Help.
### To edit report input fields

In a report, you can create, edit and delete report input fields.
A report input field defines the data that will appear on the report. You can use any value from the
program script as a report input field.
You can add a field as a report input field when:
- The field is a table field and it is selected by the program script
- The field is a variable and it is defined in the program script (or library)
> [!NOTE]
You can define variables in a report script. Report script variables can be used in a print expression to
output the variable value. However, you should not define a report script variable as a report input field.
To create a report input field:

1. In the Reports (ttadv3530m000) session, select the report you wish to edit.
2. On the appropriate menu, click Input Fields.... The Report Input Fields (ttadv3532m000)
overview session starts.
3. If the report field does not exist for the report, click New to add a report input field. The details
session starts.
4. Enter a report input field, or click the Zoom icon to display table fields. You may wish to enter
the table id in the Field Name field to quickly find the correct table field.
5. Complete the dialog. Save the changes and close the dialogs.
### To edit report layouts

An LN report usually contains multiple report layouts, such as Header, Before.field and Detail.
Report layouts specify the report fields and the position of those fields on a report line. The report layouts
execute depending on the data that is processed from the report input fields.
For information on the types of layouts, refer to Reports (p. 42) .
To view report layouts
A report can have multiple layouts. To view the report layouts, in the Reports (ttadv3530m000) session
click Layouts..., or click the Layouts... command on the appropriate menu. The Report Layouts
(ttadv3531m000) session starts. The layouts for the report are displayed.
To edit all layouts
You edit the layouts to change the report contents and positions.
To edit all the layouts, in the Report Layouts (ttadv3531m000) session, click the Edit All Layouts...
command on the appropriate menu. The report layout editor starts.
Edit All Layouts
The layout editor contains many options. Not all the options are shown here. To view the help options,
click Help on the Help menu.
The major editing tasks are moving fields and labels, drawing boxes, and creating report fields.
To move fields and labels
You need to move fields and labels in order to align columns or make room for other data fields. To
move a field or label:

1. Select the field or label (do not double-click).
2. Holding your mouse button, drag the mouse or use the arrow keys to place the field in another
location in the layout.
3. Drop the field in the desired location. When using the arrow keys, you must press Esc.
In addition to moving labels, you may need to change the label length, or create new labels with shorter
lengths in order for the label to fit in the column width.
To create or edit a report field
A report field is denoted in the editor with the capital F’s (“FFF”).
To create a report field:

1. Place your cursor in the top left position where you want the new field.
2. On the Edit menu, click Form Field. Alternatively, you can press CTRL + F simultaneously.
The Report Fields (ttadv3134s000) session starts.
3. Enter a print expression. A print expression can be:
- A report input field
- A report script variable
- A calculated expression from 1 or more other input fields (or report script variables)
4. Specify the remaining report field options in the Display, Conditions and Font tabs.
To edit a report field: double-click on the field to start the Report Fields (ttadv3134s000) session, where
you can modify the field's properties.
To draw boxes and graphical characters
After adding report fields, the content is complete, and you may wish to align the data in columns. You
align data into columns using the boxes, or graphical characters.
To draw a box:

1. Position the cursor in the top left position of the box.
2. On the Edit menu, click Draw Box. The cursor changes to a plus (+) sign.
3. Click the cursor on the bottom right corner of the box. The box is now complete.
Draw Box - cursor changes to plus (+) sign
Draw Box Complete
A box will draw irrespective of any adjoining lines.
You can join lines or boxes using graphical characters.
To insert a graphical character:

1. On the Mode menu, click Toggle Graphics to enter graphical mode.
2. Use your numeric keypad to select the appropriate character. See the figure below. Use the
pipe (|) key for vertical lines and the hyphen (-) for horizontal lines.
3. On the Mode menu, click Toggle Graphics to exit graphical mode.
Numeric Keypad and Graphical Characters
To create a layout
Typical reasons for creating a layout are:
- Before field layouts to create sub-headings
- After Field Layouts to calculate sub-totals using the aggregate functions
- After Report layout to create a grand total using the aggregate functions
- An additional Detail layout to print optional detail information on a new line
To create a layout:

1. In the Report Layouts (ttadv3531m000) session, click New. The Report Layouts
(ttadv3131s000) details session starts.
2. Enter the layout information.
3. Edit the layout in the report editor: place the desired fields and/or labels in the new layout.
Example
The items are printed by item group. At the end of each item group a sub-total is displayed.
To achieve this, you must:
- Make sure that the records are sorted by Item Group: in the report input field properties, define
- Add a before.field layout. In the layout properties, you must select the Item Group field.
- Start the report editor and place the Item Group field and the corresponding label in the new
- Add an after.field layout. In the layout properties, you must select the Item Group field.
- Start the report editor and place the desired sub-totals in the after.field layout.
a sort mode for the Item Group field.
before.field layout.
- For example: to place a sub-total for the Stock on Hand field (cxoes020.stoh) you must
place the cxoes020.stoh field in the after.field layout. In the field properties you must select
the "Total" aggregate function.
Report with sub-totals per Item Group
### To edit a report script

A report script allows you to customize the processing of the report.
Report scripts have sections that correspond to a layout. A section can be processed before a layout,
or after a layout. The report script is compiled with the report when the report is compiled.
For details on report scripts, refer to:
- Report scripts (p. 45)
- "Report Script Features" in the Infor ES Programmer's Guide. Predefined variables used in a
report are also listed.
To edit a report script, you must use the Reports (ttadv3530m000) session.
## To create dashboards

To create a dashboard you must:
- create the dashboard session and its form using the Sessions (ttadv2500m000) session. The
- Create a UI script for the dashboard session: The UI script controls most of the actions,
- Create details sessions that allow the dashboard user to drill-down into the details of the
dashboard session uses the main table of the entity that you want to select.
including the selection, calculation and starting the details sessions.
overview presented in the dashboard.
> [!IMPORTANT]
The sections below describe the sessions that you must use to create a dashboard. However, they do
not describe all details of these sessions. For detailed session information, refer to the Infor Web Help.
### To create the session

The dashboard session uses the main table of the entity that you want to select. The session is similar
to an overview session. However, an overview session usually has a synchronized dialog to its details
session. A dashboard session controls the synchronization to the various details sessions within the
program script.
Example- Items Dashboard
You need to create a dashboard session that uses the Items as the main entity. When you select an
item, the dashboard will show the item, description, purchase price, stock on-hand and stock on-order
for the item. Next to the purchase price, it will calculate the last purchase price. Next to the stock on-hand,
it will display the inventory value (valued at purchase price). Next to the stock on-order, it will show the
latest order date for orders that have not been delivered. A document button is available to view purchase
orders for the item.
You create an items dashboard session, using the Items table. The session is a display session type.
This table shows the session properties:

Package
cx
Module
oes
Session
0520m000
Description
Item Dashboard
Standard Script
No
Program Script
cx oes 0520
Main Table
cx oes 020
Start Command Type
No Start Command
Start Command
0
Session Status
Developing
Dynamic Session
Yes
Integrated
Yes
Session Type
Display
Window Type
List Window
Main Session
Yes
Synchronized Dialog
[Empty]
To create the form
This diagram shows a dashboard session:
Dashboard session - form sections
The form of a dashboard session consists of these sections:

1. Details
This section contains fields that are declared as variables, as opposed to table fields. While
not required, these fields are typically defined in one or more groups.
2. Links
This section contains check boxes and buttons. The check boxes are variables that are defined
in the session's program script. The check boxes do not have labels. The buttons are field
level form commands, that are linked to the check boxes. The form commands use labels to
provide the names for the buttons.
3. Records
The records are displayed in a grid. The grid is typically defined in another group. The grid
contains table fields and the number of fields in the grid may be limited to a few key fields. A
new group is not required, but helps you in separating the Links and Records sections.
The form contains group boxes and field buttons. Therefore Rich View should be selected in the Session
Properties of the form.
Example- Items Dashboard
You create an items dashboard session using the Items table. The session is a display session type.
Dashboard Form Editor
In the Dynamic Form Editor you must specify the session properties, the field properties and form
commands.
Specify these properties in the Session Properties dialog box:

Field
Value
Overview Session
Yes
Rich View
Yes
Remaining field sNo
Fields in the view area are variables that are defined in the session's program script, such as "sel.item".
See the sample script in this section for more examples. Specify the following properties in the Position
tab in the Field Properties dialog box:

Value
Field
Overview Session
Yes
View Field
Yes
Remaining fields
No / empty
The field properties for the Documents check box fields do not have a label code. The button next to
each document check box is defined as a field level form command, which is linked to the corresponding
check box field. The form command executes a function that will be defined in the program script.
This table shows the properties of the field level form command that is linked to the "sel.orders" check
box:

ID
1
Activate a
Function
Session/Function/Business
Method
exec.orders
Parent (Menu)
0
Sort Sequence
0
Command Type
Field
Group/Field Number
90
Label
oes022.orli
Long description
Order Lines
Short Description
Order Lines
Shortcut Key
[Empty]
Separator
No
You can use the Show Overview Session command in the Dynamic Form Editor to start the session.
Show Overview Session Result
### To create the program script

The program script controls most of the actions, including the selection, calculation and starting the
details sessions.
The actions that occur when the user selects a row are programmed in a mark.occur event. This event
will gather the information for the selected value, and enable the form commands. It will also
re-synchronize the details sessions.
The detail sessions are started via a form command. Since the script will control the synchronization, it
is preferred that the form commands call a function in the script. This function is defined as an extern
function.
Example- Items Dashboard
The Items dashboard needs to:
- Declare the form variables.
- Declare the tables used in the calculation of the form variables (unless a library calculates
- Contain actions for the mark.occur event
- Contain actions for the functions called by the field level form commands
- Start a synchronized child process in the functions called by the field level form command.
these values)
Uses the start.synchronized.child function.
See the following code for an example:
|*********************************************************
|* cxoes0520  0  VRC B61U a  dv00
|* Items Dashboard
|* Development User
|* 2005-02-10
|*********************************************************
|* Main table cxoes020 Items, Form Type 1
|*********************************************************

|****************************** declaration section ******
declaration:
table   tcxoes020 | Items
table   tcxoes022 | PO Headers
table   tcxoes023 | PO Lines

extern domain cxitem sel.item
extern domain cxdscr sel.dscr
extern domain cxprice sel.ppri, sel.lopp, sel.sval
extern domain cxquan  sel.stoh, sel.stoo
extern domain cxdate  sel.lodt
extern domain cxyeno  sel.orders

long orders.session.child.id, dummy.ret
|****************************** program section **********
|****************************** group section ************
|****************************** choice section ***********
choice.mark.occur:
after.choice:
if number.of.marks = 1 then
|use a pre-defined var to test that only
|one item is selected from the list
fill.sel.values()
sync.open.session()
else
clear.sel.values()
endif
| need to display values because they are not
| displayed automatically
display.all()

|****************************** function section *********
functions:
function fill.sel.values()
{
sel.item = cxoes020.item
sel.dscr = cxoes020.dscr
sel.stoh = cxoes020.stoh
sel.stoo = cxoes020.stoo
sel.ppri = cxoes020.ppri
sel.sval = sel.stoh * sel.ppri
get.last.order.info.for.item()
}
function clear.sel.values()
{
sel.item = " "
sel.dscr = " "
sel.ppri = 0.0
sel.lopp = 0.0
sel.sval = 0.0
sel.stoh = 0
sel.stoo = 0
sel.lodt = 0
sel.orders = cxyeno.no
}
function get.last.order.info.for.item()
{
|* last purchase price is latest order, no matter of status
select cxoes022.*, cxoes023.*
from   cxoes022, cxoes023
where  cxoes023.orno refers to cxoes022
and    cxoes023.item = :sel.item
order by cxoes022.odat desc
as set with 1 rows
selectdo
sel.lopp = cxoes023.ppri
sel.orders = cxyeno.yes
selectempty
sel.lopp = 0
sel.orders = cxyeno.no
endselect
|* last purchase order date is latest open order
|* stat <> delivered
select cxoes022.*, cxoes023.*
from   cxoes022, cxoes023
where  cxoes023.orno refers to cxoes022
and    cxoes023.item = :sel.item
and    cxoes022.stat <> cxstat.delivered
order by cxoes022.odat desc
as set with 1 rows
selectdo
sel.lodt = cxoes022.odat
selectempty
sel.lodt = 0
endselect
}
function extern exec.orders()
{
if sel.orders = cxyeno.yes then
| document is checked, start the child process
if orders.session.child.id then
| already started the session, so re-use it
| but refresh with new item values
| if closed, will set child.id to 0
dummy.ret = synchronize.with.child(orders.session.child.id)
endif
if not orders.session.child.id then
| need to start the session
session.zoomindex = 1
| if there is a alt key by item, we could use it
orders.session.child.id = start.synchronized.child(
"cxoes0523m100",
"cxoes020.item",
"cxoes020.item")
|* start orders by item. Send parent var of cxoes023.item,
|* and child var of cxoes020 for query extension to
|* work in child session.
endif
endif
}
function sync.open.session()
{
| have the dashboard sync the open sessions when a new
| item value is selected
if orders.session.child.id then
| already started the session, so re-use it
| but refresh with new item values
dummy.ret = synchronize.with.child(orders.session.child.id)
endif
}
When you compile this script, the session can compute values.
Item Dashboard with Computed Values
Select another item to show the values for that item.
Item Dashboard
### To create the details sessions

The details sessions allow the dashboard user to drill-down into the details of the overview presented
in the dashboard. A details session will typically import the values from the dashboard session, and start
or limit the display to those records. The program scripts of the details sessions can be modified to
import these values and in some cases, extend the query so that only the desired rows are displayed.
Example- Items Dashboard
You have created an Items dashboard session using the Items table. The order lines for the Item must
be shown in a details session. The Purchase Order Lines (cxoes0523m100) session uses the Purchase
Order Lines (cxoes023) table to show purchase order lines. You edit the form of this session to insure
that the Item field is a view field.
Purchases by Item Form
The program script extends the query in the before.program section. The query extension is required
because there is not an index on the field that contains the filter.
|*************************************************************
|* cxoes0523  0  VRC B61U a  dv00
|* Purchases by Item
|* Development User
|* 2005-01-07
|*************************************************************
|* Main table cxoes023 Purchase Order Lines, Form Type 1
|*************************************************************

|****************************** declaration section **********
declaration:
table   tcxoes020 | Items
table   tcxoes023 | Purchase Order Lines
|****************************** program section **************
|* import item from calling session
|* query extension to create filter
before.program:
query.extend.where(" cxoes023.item = :cxoes020.item")
|****************************** group section ****************

When this session is started from the dashboard, the session will show only the orders for the item that
is selected in the dashboard.
Dashboard with Detail Session
When you select another item, and click the Documents button, the details session will synchronize.
The item from the dashboard session will be sent to the details session, and the purchase orders for
that item will display.
Select Item on Dashboard with Detail Session
## To create MMT Sessions

> [!IMPORTANT]
The sections below describe the sessions that you must use to create MMT sessions. However, they
do not describe all details of these sessions. For detailed session information, refer to the Infor Web
Help.
This diagram shows the procedure steps and the corresponding sessions or programs:
The flow: Create a multi-main table session
### To create a main entity detail session

If you want the multi-main table controller session to use a details session, you must determine if the
details session already exists, or if you need to create it.
When you create the details session, you must enter a label code in the Label of Object field in the
session properties. This allows the label to show on the multi-main table controller session for opening
the details session.
Example- details session
The Purchase Order Headers (cxoes0122m000) session already exists, and you can use it as the details
session. You enter a label code in the Label of Object field.

Field
Input Value
Label of Object
oes022 (Purchase Order Headers)
### To create a multi-main table controller session

To create the multi-main table controller session:

1. Start the Sessions (ttadv2500m000) session and specify the properties for the controller
session. Points of attention:
- Session Type: Maintain
- Window Type: Multi Main Table
- Main Session: Yes
- Synchronized Dialog: the code of the main entity detail session, e.g. cxoes0122m000
2. Edit the form and insert the fields you wish to have in the session.
Example- multi-main table controller session
The Purchase Orders multi-main table controller session is created with the following properties:

Field
Input Value
Package
cx
Module
oes
Session
0122s100
Description
Purchase Orders
Standard Script
No
Program Script
cxoes0122s100
Main Table
cxoes022
Start Command Type
No Start Command
Start Command
0
Session Status
Developing
Dynamic Session
Yes
Integrated
Yes
Session Type
Maintain
Window Type
Multi Main Table
Main Session
Yes
Synchronized Dialog
cxoes0122m000
### To create a satellite session

You can use an existing satellite session, or create a new one. The key field that links the satellite entity
to the main entity must be a view field in the form. You must specify a label of object for the satellite
session.
Example- satellite session
The Purchase Order Lines (cxoes0123m000) session is an existing satellite session. You enter a label
code in the Label of Object field in the session's properties.

Input Value
Field
Label of Object
oes023 (Purchase Order Lines)
### To assign satellites to the controller

You must link the satellite sessions to the multi-main table controller session.
To do so:

1. Start the Sessions (ttadv2500m000) session.
2. Select the multi-main table controller session.
3. On the appropriate menu, click MMT Satellite Sessions. The Satellite Sessions
(ttadv3110m000) session starts.
4. Click New.
5. Enter the next index number.
6. Enter the satellite session code.
7. Either enter the field mapping information, or click Generate Field Mapping.
Example- assign satellite sessions
You link the Purchase Order Lines (cxoes0123m000) session as a satellite session to the Purchase
Orders (cxoes0122s100) multi-main table controller session. You enter the following field mapping:

Field name in satellite
Field name in MMT session
cxoes022.orno
cxoes023.orno
### To compile and run the controller session

You must compile the multi-main table controller session after you assign a satellite session.
To compile the session:

1. Start the Sessions (ttadv2500m000) session.
2. Select the session.
3. Click Compile.
You can now run the multi-main table controller session.
### To integrate the controller session

The multi-main table controller session is the equivalent of a details session for the main entity. Therefore,
you should integrate the session, either as a synchronized dialog of the main overview session for the
table, or as a child session of an overview display session.
To integrate the controller session, using the session as a synchronized dialog:

1. Start the Sessions (ttadv2500m000) session.
2. Select the main overview session for the table. Modify the properties of this session: Fill the
Synchronized Dialog field with the multi-main table controller session code.
3. Save the session.
Example- Multi-main table controller session integrated with overview session
You modify the Purchase Orders (cxoes0122m000) overview session so that it uses the multi-main table
controller session (cxoes0122s100) as a synchronized dialog. When you open a purchase order in the
overview session, the multi-main table controller session opens with the purchase order that you selected.
## To translate software components

In LN you can export the labels, questions, and messages from a development or translation system
and import them into other LN environments. Export and import of labels is performed by using
XML-formatted files. Every XML file contains a selection of translatable components based on the user’s
settings. The translated language files can be imported back into the Infor environment. The import
process includes a conversion to runtime. All descriptions are stored as labels which can be handled
by the same import and export processes.
## Multi-language

Most LN implementations use several system languages simultaneously. In addition, various languages
for user reports such as customer facing documents sometimes also require languages other than the
local languages used.
LN uses the Language Translation System (LTS) to both reduce the language-dependency of the LN
applications and to lower the costs of media creation.
Translatable software components, such as labels, questions, and messages, are stored separate from
language-independent software components, such as form and report designs. The descriptions of the
translatable software components are stored per language.
Language-independent components contain only references to translatable components. E.g. a form
layout or a report layout contains label codes, and a UI script can contain message codes or question
codes. The descriptions of the labels, messages and questions are read at runtime, depending on the
language of the user.
Example
You use 2 system languages: Dutch and English.
Your LN system contains, among other things:
- Form layouts and report layouts (one set for all languages)
- 2 sets of label descriptions, message descriptions and question descriptions. (Dutch and
English)
The form of the Add Session to Job (ttaad5102s000) session contains a label ttaad320.seqn. The
description of this label is stored in 2 languages:

Label description
Language
Dutch
Volgnummer
English
Sequence No.
When a user runs the session, the label description is displayed depending on the user's language.
High Ascii Tolerance
If you plan to deliver software components or translations from your LN environment and your environment
does not run in Unicode mode, you must set the high_ascii_tolerance resource to 0.
If high_ascii_tolerance is not set to 0, problems will occur when the delivered components are imported
in Unicode environments.
To set high_ascii_tolerance to 0, add the following line in the $BSE/lib/defaults/all file:
high_ascii_tolerance:0
> [!IMPORTANT]
The sections below describe the sessions that you must use to translate software components. However,
they do not describe all details of these sessions. For detailed session information, refer to the Infor
Web Help.
## To translate labels, questions and messages

LN enables you to translate labels, questions and messages.
Basic procedure

1. Use the following sessions to translate the labels, questions and messages.:
- Labels (ttadv1140m000)
- Question Descriptions (ttadv4166m000)
- Message Descriptions (ttadv4150m000)
2. Run the Compile Labels (ttadv1243m000) session to store the new label descriptions in the
runtime data dictionary.
Additional sessions
The following sessions are useful if you want to distribute translated components from a
translation/development system to other systems, or if you want to perform the translation in an external
application, e.g. in a professional translation application such as Transit.
Session
Description
Export Language Dependent Data to XML - Wizar dUse this session to export the components to XML
files.
(ttadv8910m000)
Merge Tool for XML-files with Language Dependen tUse this session to merge multiple XML files containing language-dependent components into one
file.
Components (ttadv8930m000)
Import Language-Dependent Data from XML -
Wizard (ttadv8920m000)
Use this session to import the content of XML files
containing language-dependent components into
an LN environment. Note: After you import the
components, you must compile the labels.
