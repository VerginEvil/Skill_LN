# Chapter 7: Wizards and Dialogs

## Activity

## Activity Information

Use this dialog to view the properties of an LN Studio Activity, and to add other activities to the context of the
selected activity.
Settings
This dialog shows detailed information on:
- The selected activity.
- The Software Project to which the activity belongs.
- The Application to which the software project is linked.
See the online help of these dialogs:
- Create a new Activity
- Create a Software Project
- New Application
Context
You can use this tab to put another Activity in the context of the current activity. This is useful if you want to
use components developed in another activity by another Software Engineer or by yourself. For example: You
want to use a DLL, that is currently modified by another software engineer, in a UI script.
See Activity context on page 48.
To add an activity:
1 Click Add and select the project to which the desired activity belongs.
2 Click Add Activity and select the desired activity from the list.
3 Click OK.
The Can Open check box is read-only. It indicates whether you are assigned to the activity.
## Activity Overview, End Activity

This dialog is displayed when you end an activity.
The dialog shows the components in the activity that are new or modified.
If the Partial End Allowed check box in the software project properties is selected, you can partially end the
activity. Use the Selected check box to select the components for which you want to end the activity.
If you selected all components, the activity is ended completely and disappears from the Activity Explorer.
> [!NOTE]
- You can only completely end an activity if all components in that activity are checked in.
- The Project VRC contains all finished software components for the project. From this VRC, deliveries to
customers are performed when the project is completed.
- See Activity based development on page 37.
Selected
If this check box is selected, the component is moved from the Activity VRC to the Project VRC, and becomes
available to other software engineers.
If this check box is cleared, the component stays available in the activity VRC.
Type
The component type, such as session or label.
Name
The name of the component.
User(s)
The user who modified the component.
Blocked by
The activity, which blocks the end activity process, and its owner.
The end activity process is blocked if the previous activity is not yet released and delivered.
You can only end an activity, if the previous activity is released and delivered. Otherwise the End Activity
action is blocked. The name of the previous activity, which blocks the End Activity process, and its owner
are displayed.
## Clean activity

Use this dialog box to remove unchanged components from one or all activities.
The cleaning process performs these actions:
- Removes all components that are not checked out, created, or modified from the selected activities.
In the Activity Explorer, these components have a  decorator in the bottom right corner of the software
component image.
- Ignores all new, modified, and checked out components.
In the Activity Explorer, these components have a  or  decorator in the bottom right corner of the
software component image.
Clean all activities
If this option is selected, components are removed from all activities displayed in the Activity Explorer.
Clean selected activity
If this option is selected, components are removed from the activity you selected in the Activity Explorer.
## Open an Activity

Use this wizard to open a new activity.
To open an activity:
1 In the Select Project page, select your software project from the list and click Next. The Select Activity
page is displayed.
2 Select your activity from the list and click Finish.
Select Project
Use this page to select the project to which the activity belongs.
All fields, except Project name, are read-only.
Project name
The project to which the activity belongs.
You can select the project name from a drop-down list.
All other fields
For details on the other fields, see the online help of the Create a Software Project dialog.
Select Activity
Use this page to select the activity you want to open.
All fields, except Activity name, are read-only.
Activity name
The activity you want to open.
You can select the activity name from a drop-down list.
All other fields
For details on the other fields, see the online help of the Create a new Activity dialog.
## Reassign Activity

Use this dialog to assign an activity to another user.
Note: After you have assigned an activity to another user:
- The other user has full permissions for the activity.
- You have only limited permissions for the activity.
- You can reassign the activity to yourself again.
See Reassigning an activity on page 51.
You can start this dialog from the shortcut menu in the Activity Explorer view.
Reassign to
Select the user, to which you want to assign your activity, from the list.
## Recover activity

Use this dialog to recover an activity. You can start this dialog from the Activity Explorer view.
The recovery process restores files that belong to the selected activity from the Configuration Management
System on the server, and stores them in your local workspace. This is very useful, for example, after a PC
crash: On your new PC, you can start LN Studio, open your activity, and restore your local workspace from
the server.
Click OK to confirm your selections. The Recover activity dialog starts. Here, you can view the recovery
actions that aree taken and decide whether you want to proceed with the recovery process.
See Recover activity on page 83.
Modified components in the current activity
Recover existing components
If this check box is selected, LN Studio restores all your new, modified, and checked out components from
the server and stores the corresponding files in your local workspace.
In the Activity Explorer, these components have a  or  decorator in the bottom right corner of the
software component image.
Note: Selecting this check box is mandatory if you recover your activity after a code freeze.
Modified components of other user(s)
Process modified components of other user(s)
If this check box is selected, components of other users, assigned to the activity, are also processed. If this
check box is cleared, these components are ignored.
Select one of the following options:
LN Studio corrects the administrative information about these components in your local workspace,
when necessary.
If the components in your local workspace are corrupt, new components are retrieved from the
server.
Repair
Recover
Delete
LN Studio restores these components from the server and stores the corresponding files in your
local workspace.
For example: you open a shared activity. The components developed by other users are not displayed automatically. Use this option to display these components.
LN Studio removes these components from your local workspace, so they are not displayed in
the Activity Explorer anymore.
Non modified components
This field indicates the action that is performed for components that are not checked out, modified, or
created.
In the Activity Explorer, these components have a  decorator in the bottom right corner of the software
component image.
Allowed values
LN Studio ignores these components. The components are not removed from your activity and
local workspace.
LN Studio restores these components from the server and stores the corresponding files in your
local workspace.
LN Studio removes these components from your activity and local workspace.
Note: The Clean activity command in the Activity Explorer view does the same.
Ignore
Recover
Delete
## Recover activity

This dialog starts automatically when you recover an activity. It shows the actions that are executed when
you start the recovery.
This table shows an example:
Type
session
label
library
table
Action
tezzz3110m000 Delete
Recover
tezzzdbl310sb0 Recover
Recover
Name
tezzzabcd1234
tezzz102
Reason
Non activity component, option 'delete' set
Recover also Existing files
Recover also Existing files
Recover also Existing files
Click OK to perform the actions displayed. Click Cancel if you do not want to perform these actions.
After the recovery, the results are displayed. This table shows an example:
Type
session
label
Action
tezzz3110m000 Delete
Recover
Name
tezzzabcd1234
Result
Ok
Ok
Type
library
table
Action
tezzzdbl310sb0 Recover
Recover
Name
tezzz102
Result
Ok
Ok
Type
The component type, such as label or session.
Name
The name of the software component.
Action
The action that will be executed during the recovery.
Reason
The reason for the recovery action.
This field is displayed before you start the recovery.
Result
The result of the recovery action.
This field is displayed after the recovery.
### Link Run Configurations

Use this window to link existing run configurations to an activity.
You can start this dialog from the Activity Explorer view.
The window shows the available run configurations. Select the desired configuration(s) and click Link.
## Create IEX Patch

Use this dialog to create an IEX patch from an activity and place it in a folder.
Options
Primary language only
If this check box is selected, language-dependent components, such as reports, are only exported in the
primary language.
If this check box is cleared, language-dependent components are exported in all available languages.
Include sources
If this check box is selected, sources, such as UI scripts, are included in the patch.
Destination
Development server
If this option is selected, the patch is created on the LN development server.
Client
If this option is selected, the patch is created on your client computer.
If this option is selected, the patch is created on another remote system. Click New to specify a remote
system.
Disconnect connection after patch creation
If this check box is selected, the connection with the destination system is automatically closed when the
patch is ready.
Folder
The folder, on the destination system, to store the patch.
Filename
The name of the patch file.
## Browse and Select

## Browse Command Sets

Use this dialog to select a command set for a session.
A command set is a selection of standard commands. At runtime, the user can run these commands through
standard buttons and menu commands.
Each combination of a session type and a form type has its own command set, such as:
- D1.O: command set for display sessions with a type 1 form.
- M1.O: command set for maintenance sessions with a type 1 form.
You can start this dialog from the Session Editor.
To select a command set, click the desired set and click OK to close the browse dialog.
## Browse component

Use this dialog to find and select a component.
You can start this dialog from various wizards and editors, such as:
- The Create a New Infor LN Software Component wizard: You can use the dialog, for example, to select
a main table for a new session.
- The Table Editor: You can use the dialog, for example, to select a reference message for a table.
- The Session Editor: You can use the dialog, for example, to select a report for a print session.
To select a component:
1 Find the component: Browse the list of components or, in the Name field, specify the first character(s)
of the component name and click the binoculars button.
2 Click the desired component and click OK to close the browse dialog.
Note: The slider bar and the navigation buttons enable you to find components in one package only. To find
components in a different package, specify the package code in the Name field, and click the binoculars
button.
For these component types, you can use the New command to create a new component:
- Session
- Library
- Table
- Domain
- Report
- Message
- Question
- Label
- Menu
See the following section.
Create a new component
To create a new component:
1 Click New. The appropriate page of the Create a New Infor LN Software Component wizard starts. For
example, the Library Properties page, or the Menu Properties page.
2 Fill in the required component properties.
3 Click Finish to generate the component and to close the Create a New Infor LN Software Component
wizard.
- The Browse component dialog is closed automatically.
- The name of the new component is filled in automatically in the wizard or multipage editor, where
you started the Browse component dialog.
## Browse domain

Use this dialog to find and select a domain.
You can start this dialog, for example, from:
- The Create a New Infor LN Software Component wizard
- The Report Editor
- The Question Editor
To select a domain:
1 Find the domain: complete one of these steps:
- Browse the list of domains.
- Select Search on Name. Then, in the Name field, specify the first character(s) of the domain name
and click the binoculars button.
- Select Search on Description / Search Key and, in the Package field, select a package. Then, in the
Description / Search key field, specify a part of the domain's description / search key and click the
binoculars button.
2 Click the desired domain and click OK to close the browse dialog.
Note: The slider bar and the navigation buttons enable you to find domains in one package only. To find
domains in a different package, select Search on Name. Then, in the Name field, type the package code and
click the binoculars button.
You can only select domains in packages that belong to the application displayed in the Component Explorer.
Use the New command to create a new domain. See the following section.
Create a new domain
To create a new domain:
1 Click New. The Domain Properties page of the Create a New Infor LN Software Component wizard
starts.
2 Fill in the required domain properties.
3 Click Finish to generate the domain and to close the Create a New Infor LN Software Component
wizard.
- The Browse domain dialog is closed automatically.
- The name of the new domain is filled in automatically in the wizard or multipage editor, where you
started the Browse domain dialog.
## Browse Default Sizes

Use this dialog to select a default size, for example A4, for a report.
You can start this dialog, for example, from the Create a New Infor LN Software Component wizard and
from the Report Editor.
To select a default size, click the desired size and click OK to close the browse dialog.
## Browse label

Use this dialog to find and select a label.
You can start this dialog, for example, from the Session editor.
To select a label:
1 Find the label: take one of the following steps:
- Browse the list of labels.
- Select Search on Name. Then, in the Name field, type the first character(s) of the label name and
click the binoculars button.
- Select Search on Description / Search Key and, in the Package field, select a package. Then, in the
Description / Search key field, type a part of the label's description / search key and click the
binoculars button.
2 Click the desired label and click OK to close the browse dialog.
Note: The slider bar and the navigation buttons enable you to find labels in one package only. To find labels
in a different package, select Search on Name. Then, in the Name field, type the package code and click the
binoculars button.
You can only select labels in packages that belong to the application displayed in the Component Explorer.
Use the New command to create a new label. See the following section.
Create a new label
To create a new label:
1 Click New. The Label Properties page of the Create a New Infor LN Software Component wizard starts.
2 Fill in the required label properties.
3 Click Finish to generate the label and to close the Create a New Infor LN Software Component wizard.
- The Browse label dialog is closed automatically.
- The name of the new label is filled in automatically in the wizard or multipage editor, where you
started the Browse label dialog.
## Browse library

Use this dialog to find and select a library.
You can start this dialog, for example, from the Table Editor.
To select a library:
1 Find the library: complete one of these steps:
- Browse the list of libraries.
- Select Search on Name. Then, in the Name field, specify the first character(s) of the library name
and click the binoculars button.
- Select Search on Description / Search Key and, in the Package field, select a package. Then, in the
Description / Search key field, type a part of the library's description / search key and click the
binoculars button.
2 Click the desired library and click OK to close the browse dialog.
Note: The slider bar and the navigation buttons enable you to find libraries in one package only. To find
libraries in a different package, type the package code in the Name field, and click the binoculars button.
You can only select libraries in packages that belong to the application displayed in the Component Explorer.
## Browse product ID

Use this dialog box to find and select a product ID.
You can start this dialog box, for example, from the Library Editor.
To select a product ID:
1 Find the product ID: Browse the list of product IDs.
2 Click the desired product ID and click OK to close the browse dialog box.
## Browse Queries

Use this dialog to find and select a query.
You can start this dialog from the Menu editor.
To select a query:
1 Find the query: Browse the list of queries.
2 Click the desired query and click OK to close the browse dialog.
Note: The slider bar enables you only to browse the list of queries currently displayed. To display the remaining
queries, use the navigation buttons, or type the first character(s) of a query name, and click the binoculars
button.
## Browse session

Use this dialog to find and select a session.
You can start this dialog, for example, from the Menu Editor.
To select a session:
1 Find the session: Browse the list of sessions or, in the Name field, specify the first character(s) of the
session name and click the binoculars button.
2 Click the desired session and click OK to close the browse dialog.
Note: The slider bar and the navigation buttons enable you to find sessions in one package only. To find
sessions in a different package, type the package code in the Name field, and click the binoculars button.
Use the New command to create a new session. See the following section.
Create a new session
To create a new session:
1 Click New. The Session Properties page of the Create a New Infor LN Software Component wizard
starts.
2 Fill in the required session properties.
3 Click Finish to generate the session and to close the Create a New Infor LN Software Component
wizard.
- The Browse session dialog is closed automatically.
- The name of the new session is filled in automatically in the wizard or multipage editor, where you
started the Browse session dialog.
## Browse Input Fields

Use this dialog box to select table fields for a report.
You can start this dialog box from the Report Editor.
Click the desired field and click OK to close the dialog box.
Note: The dialog box shows the fields of a single table. To select another table, click Browse.
## Browse text field

Use this dialog to find and select a text field.
You can start this dialog, for example, from the Session Editor.
To select a text field:
1 Find the text field: Browse the list of text fields or, in the Name field, specify the first character(s) of the
text field name and click the binoculars button.
2 Click the desired text field and click OK to close the browse dialog.
Note: The slider bar and the navigation buttons enable you to find text fields in one package only. To find
text fields in a different package, type the package code in the Name field, and click the binoculars button.
## Browse time Format / Browse date format

Use this dialog to find and select a time or date format.
You can start this dialog, for example, from the Domain Editor. For domains of data type "UTC Date/Time",
the dialog displays a list of time formats. For domains of data type "Date", the dialog displays a list of date
formats.
To select a format:
1 Find the format: Browse the list of formats.
2 Click the desired format and click OK to close the browse dialog.
## Select a Chart

Use this dialog box to link a chart to a session. Each session can have several charts.
You can start this dialog box from the Session Editor.
Session
The session to which you link the chart.
Chart
The chart name. The name is a combination of the package, the module, and the chart code.
Click Browse to start a dialog box where you can select charts.
Chart Group
You can change the chart group in the UI script of the session.
Allowed values
Chart group 1.
## Select Component(s)

Use this dialog to add software components from the LN server to your current activity.
To start the dialog:
1 In the Activity Explorer view, select an activity, or a subfolder, or a component in an activity.
2 On the LN Studio toolbar, click Select a Software Component, or press ALT+Q.
The dialog consists of 2 tabs, that you can use to search in 2 different ways:
- Select on code
- Search on description
Note: When you add a component to your activity, the appropriate editor can start automatically for the
component. This depends on your workbench preference settings. See the description of the Preferences -
Workbench dialog.
Select on code
Use this tab to search on the first part of the component code.
Adding a component to the selected activity
To add a component to the selected activity:
1 Optionally: In the upper right part of the tab, click the drop-down menu button. The Select Component
Types dialog starts. In this dialog you can specify additional settings for the search process.
2 In the Component Code field, enter the first part of the component code. For example: tdpur01.
3 Click the ellipsis button, or press CTRL+SPACE. A list of components, which match the pattern, is displayed.
If you type additional characters, LN Studio automatically updates this list.
4 If you want the dialog to close automatically after you click OK, select the Close Dialog after processing
selection check box.
5 Select the desired component and click OK. The component is now added to your current activity.
To sort search results
- To sort the search results by type, name, or description, click the corresponding column header.
- To toggle between ascending and descending sort mode, click the involved column header.
Note: As you type the package code and the module code (the first 5 characters of the component code), LN
Studio automatically shows a list of matching packages and modules, and updates this list after each character
typed. For example:
Search results displayed
Code
All packages starting with t.
Package td and all its modules.
All modules of package td that start with r. For example, tdrec and tdrpl.
Component
t
td
tdr
If you press Enter after you entered a pattern in the Component Code field, LN Studio automatically adds
all components, whose names exactly match the pattern, to your current activity.
Fields
Component Code
Specify the (first part of the) component code you are searching for.
To display a list of components, which match the pattern, click the ellipsis button, or press CTRL+SPACE.
Type
The component type, such as session or label.
Name
The component name.
Description
The description of the component.
Additional Information
Additional information about the component. For example, the label context.
Close Dialog after processing selection
If this check box is selected, the dialog is closed automatically after you click OK.
If this check box is cleared, the dialog is still displayed after you click OK, so you can perform another search.
Search on description
Use this tab to search on a part of the component's description.
To add a component to the selected activity:
1 Optionally: In the upper right part of the tab, click the drop-down menu button. The Select Component
Types dialog starts. In this dialog you can specify additional settings for the search process.
2 In the Package field, select a package from the list.
3 Specify the search pattern, and click the binoculars button. A list of components that match the search
pattern is displayed.
4 If you want the dialog to close automatically after you click OK, select the Close Dialog after processing
selection check box.
5 Select the desired component and click OK. The component is now added to your current activity.
Fields
Package
Select a package from the list.
Search Pattern
Specify the search pattern.
To display a list of components, which match the pattern, click the binoculars button.
Type
The component type, such as session or label.
Name
The component name.
Description
The description of the component.
Close Dialog after processing selection
If this check box is selected, the dialog is closed automatically after you click OK.
If this check box is cleared, the dialog is still displayed after you click OK, so you can perform another search.
## Select Component Types

Use this dialog box to specify additional settings for the search process that you want to start in the Select
Component(s) dialog box.
To define the additional settings:
1 Use the check boxes to select the components you want to search.
2 Optionally, clear the Expired check box to exclude expired components from the search.
3 Specify a maximum number of components to be displayed per search.
4 Click OK to save the settings and to return to the Select Component(s) dialog box.
Note: Click Reset Defaults to return to the default settings for this dialog box.
## Select a Report

Use this dialog box to link a report to a session. A session can have several reports.
You can start this dialog box from the Session Editor.
Session
The session to which you link the report.
Report
The report name. A report is uniquely identified by the combination of package code, module code, and
report code.
Click Browse to start a dialog box where you can select reports.
Report Group
The report groups are useful if specific reports must be used in specific situations. You can change the report
group in the session's UI script. Only the report(s) of one report group can be selected at run time.
Allowed values
Report group 1.
Example
A session has various reports divided into 2 report groups: group 1 - "Detailed Reports" and group 2 - "Summary
Reports". The session's form contains a "print what" selection field where users can select whether they
want to print a "Detailed Report" or a "Summary Report". If a user selects "Detailed Report", the user can
only select a report from group 1. If a user selects "Summary Report", the user can only select a report from
group 2.
## Select Table Fields

Use this window to select table fields for a report.
You can start this dialog box from the Create a New Infor LN Software Component wizard.
Click the desired fields and click OK to close the dialog box.
Note: The dialog box shows the fields of a single table. To select another table, click Browse.
You can select multiple fields simultaneously.
## Create a New Infor LN Software Component wizard

Use this wizard to create a software component.
In this wizard, you can create these software components in your local workspace:
- Session
- Report
- Table
- Domain
- Library
- Function
- Menu
- Label
- Message
- Question
- Additional File
After you create the component, it is displayed in your Activity Explorer view. Edit the component using a
component-specific editor.
In the first window of the wizard, specify the software development activity. Then, select the type of component
you want to create for this activity.
In the second window of the wizard, fill in some component-specific properties to initialize the new component.
Some of these properties, such as the name of the component, can only be set when you create the new
component using the wizard, and cannot be changed afterwards.
Creating a component
To create a software component:
1 Start the wizard
To start the Create a New Infor LN Software Component wizard, on the File menu of LN Studio, select
New > Infor LN Component.
2 Select activity
Specify the activity in the Activity field. This is the software development activity in which you create
the new component.
3 Select component type
Specify which type of component you want to create in the Component Type field.
4 Specify component properties
To continue in the following page of the wizard, click Next. This second window is specific to the
component you previously selected and used to set some required properties for the new component.
Fill in the required properties and click Finish to create the component in your local workspace.
The created component appears in the Activity Explorer view of the Application perspective. You can
now edit the new component in the corresponding editor.
Note: Some of these properties, such as identifying attributes and references to labels, can only be set
when you create a new component. For components already created, these properties cannot be changed.
For more information, see the Help topic on the concerned component.
LN Software Component
## Activity

The name of the software development activity for which you create the component.
Behind the activity, the involved software development project is indicated between square brackets.
Allowed values
You must select one of the activities from the drop-down list. This lists contains all activities that are currently
open in your workspace.
Component Type
The component type.
Allowed values
This table shows the component types you can select from the list:
Description
Sessions are the basic functional elements of LN applications and are used to perform
actions or tasks.
LN reports are used to output data from the database to a variety of devices, such
as printers, displays, and files. One or more LN reports must be linked either to an
LN print session or to an LN SQL Query.
Tables are data structures that are used to store data and that consists of a list of
records, each entry being identified by a unique key and containing a set of related
values.
A domain specifies the data type, the value range, (default) display format, length
and so on. Domains can be linked to table fields, form fields, and program variables.
A library is a collection of files, programs or subroutines that is used to perform specific tasks for other libraries, program scripts or sessions of LN applications.
A function is a self-contained software routine that can perform a task for the program
in which the function is written, or for another program. With the #include statement
you can include a function in a program script.
An LN menu is a list of options from which a user can make a selection to perform a
desired action, such as starting sessions, other menus, and queries.
An LN label is code that is used instead of language-dependent text in forms, reports,
and menus. A label consists of a name and a content description.
LN messages are language independent software components used to show situationdependent information to the user.
LN questions are language independent software components that are used to ask
situation-dependent questions to which the user must respond.
A generic component, such as an XML schema file, a GIF image, and so on.
Component Type
Session
Report
Table
Domain
Library
Function
Menu
Label
Message
Question
Additional File
## Creating an additional file

You can use the Create a New Infor LN Software Component wizard to create these types of additional file:
- BFlow Step
This type of additional file is used in the BFlow test framework to test application business logic. The file
is saved as a .bflow file.
- BFlow Case
This type of additional file is used in the BFlow test framework to test application business logic. The file
is saved as a .bfcase file.
- Other
This type of file includes the other additional file types. For example, .xml files, .gif files, .jpg files, .png
files, and .svg files.
Creating an additional file of type Other
Use the Additional File Properties window of the Create a New Infor LN Software Component wizard to
initialize and create a new additional file in your local workspace. This window is the wizard's second dialog
box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
Note: The Create a New Infor LN Software Component wizard does not create a file. Instead, the wizard
links an existing file, such as an XML schema file or a GIF image, to a specific package, module, and package
VRC. Therefore, before you start the wizard, put the additional file in a directory on your machine.
1 Select File > New > Infor LN Component.
2 In the Component Type field, select Additional File.
3 Click Next. The Select Type page is displayed.
4 Select Other and click Next.
The Additional File Properties page is displayed.
5 Specify this information:
Name
Specify a package code and a module code, and click Browse. Then browse to the folder where the
additional file is stored and select the file. The name of the selected file is appended to the package and
module name. The name of the folder is displayed in the File Path field.
For example, you specify package tc and module com, and you select the test01.gif file. Therefore, the
additional file name becomes tccomtest01.gif.
Description
Specify the description of the additional file.
All fields of the Additional File Properties window are required. After you created the additional file,
you cannot change its name. However, you can change the description.
For more information about the additional file properties, see the online help of the Additional File
Editor.
6 Create the additional file.
To create the additional file in your local workspace and to exit the wizard, click Finish. The created
additional file is displayed in the Activity Explorer view of the Application perspective.
You can now edit the new additional file in the Additional File Editor.
Creating and importing BFlow test scripts
1 Select File > New > Infor LN Component.
2 In the Component Type field, select Additional File.
3 Click Next. The Select Type page is displayed.
4 Select BFlow Step and click Next.
The select BFlow Template page is displayed.
5 Select the desired template.
This table shows the templates you can select:
Description
This template contains the overview_session and detail_session
variables. You must specify Get Fields actions.
This template contains the overview_session and detail_session
variables. You must specify Set Fields actions.
This template contains the overview_session and detail_session
variables. You must specify Set Fields actions.
This template contains the overview_session and detail_session
variables. You must specify Set Fields actions.
This template contains the overview_session variable.
BFlow - FORM COMMAND - Template This template contains the overview_session and form_command
variables.
This template contains the session and form_command variables.
You must specify Set Fields actions.
This template contains the overview_session variable.
This template contains no variables.
Option
BFlow - READ - Template
BFlow - MODIFY - Template
BFlow - NEW - Template
BFlow - DUPLICATE - Template
BFlow - DELETE - Template
BFlow - PROCESS - Template
BFlow - WORKFLOW - Template
NONE
After you selected a template, the variables of that template are displayed in the grid.
6 Specify the values for the variables in the grid. These values are used when the BFlow is created.
> [!NOTE]
- For the form_command variable, click the Value column in the grid and select the desired form command
from the list.
- If a synchronized dialog is defined for the overview_session, you can leave the value of the detail_ses
sion variable blank.
7 Click Next.
Depending on the selected template, one of these pages is displayed:
- Add Get Fields actions
- Add Set Fields actions
- Additional File Properties
8 If the Add Get Fields actions page is displayed, complete these steps:
a Specify this information:
Type
Select one of these values in the drop-down box:
- Overview: only overview fields are displayed.
- Details: only details fields are displayed.
Default: Depends on the session type
Show Initially hidden fields
If this check box is selected, if the form field was initially hidden, this field is also displayed in the
tree to select.
Default: Cleared
Show Only Search Key Fields
If this check box is selected, only key fields of a specified index are displayed.
You can select the index in an additional input field.
Default: Cleared
Show Only Maintable Fields
If this check box is selected, only fields of the main table of the session are displayed.
Default: Cleared
Generate Step for the new actions
If this check box is selected, a step is created under the current action. All generated actions are
added to this step.
Default: Selected
Add missing actions in step
If this check box is selected, missing Get Field actions are added to the already existing step. If
multiple steps are present in the flow, then you can select a particular step in a drop-down box.
This check box is only enabled if the previous check box, Generate Step for the new actions, is
cleared.
Default: Cleared
Generate Variables
If this check box is selected, output variables are created for the selected fields. If an input variable
with the same name already exists, this variable changes to an input/output variable.
Default: Selected
Prefix
If you specify a prefix, the names of any generated variables start with this prefix. A prefix is required
if you generate variables for different sessions with the same field names.
Default: 'o.'
b Click Next. For all selected fields, an action is generated. Depending on the information you specified,
variables may also be generated for the selected fields.
The generated actions are displayed in the Actions tab in the BFlow Editor.
If you selected Generate Variables, the generated variables are displayed in the General tab in the
BFlow Editor.
9 If the Add Set Fields actions page is displayed, complete these steps:
a Specify this information:
Type
Select one of these values in the drop-down box:
- Overview: only overview fields are displayed.
- Details: only details fields are displayed.
Default: Depends on the session type
Show Initially hidden fields
If this check box is selected, if the form field was initially hidden, this field is also displayed in the
tree to select.
Default: Cleared
Show Only Search Key Fields
If this check box is selected, only key fields of a specified index are displayed.
You can select the index in an additional input field.
Default: Cleared
Show Only Maintable Fields
If this check box is selected, only fields of the main table of the session are displayed.
Default: Cleared
Generate Step for the new actions
If this check box is selected, a step is created under the current action. All generated actions are
added to this step.
Default: Selected
Add missing actions in step
If this check box is selected, missing Set Field actions are added to the already existing step. If
multiple steps are present in the flow, then you can select a particular step in a drop-down box.
This check box is only enabled if the previous check box, Generate Step for the new actions, is
cleared.
Default: Cleared
Generate Variables
If this check box is selected, output variables are created for the selected fields. If an input variable
with the same name already exists, this variable changes to an input/output variable.
Default: Selected
Prefix
If you specify a prefix, the names of any generated variables start with this prefix. A prefix is required
if you generate variables for different sessions with the same field names.
Default: 'i.'
Generate If Variables
If this check box is selected, an If variable action is created.
Default: Selected
Generate Info Fields
If this check box is selected, an Info Field action is created.
Default: Selected
b Click Next. For all selected fields, an action is generated. Depending on the information you specified,
variables may also be generated for the selected fields.
The generated actions are displayed in the Actions tab in the BFlow Editor.
If you selected Generate Variables, the generated variables are displayed in the General tab in the
BFlow Editor.
10 On the Additional File Properties page, the default name and description of the new BFlow test script
are displayed.
You can change these values. If you do so, specify the file name in this format:
[package][module][filename].bflow
11 Click Finish.
Creating and importing BFlow test cases
1 Select File > New > Infor LN Component.
2 In the Component Type field, select Additional File.
3 Click Next. The Select Type page is displayed.
4 Select BFlow Case and click Next.
The Additional File Properties page is displayed.
5 Specify the name and description of the additional file.
Specify the file name in this format:
[package][module][filename].bfcase
To import an existing test case, click Browse and select the desired file. Alternatively, specify the file
name manually.
## Creating a domain

Use the Domain Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new Domain in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
Note: To use the new domain in an LN application, convert the domain to runtime.
## Creating a domain

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new domain. Select Domain
as the component type.
c To go to the Domain Properties window, click Next.
2 Specify the required domain properties.
In the Domain Properties window, specify this information:
Name
This is a text value. The domain name must start with the code of the package in which the domain is
used.
Description
The description of the domain.
Data Type
The data type of the domain, which is the internal representation of data, such as a string, long, double,
date or UTC Date Time.
If you select a text data type ( String, Set, Enumerated or MultiByte String), specify a Length value greater
than 0.
Length
The length in characters if the data type of the domain is a (multi-byte) string, or the default display
length for data types UTC Date Time, Date, Enumerated and Set.
For the latter two data types, the length defines the maximum number of characters of the descriptions
of the Enumerated or Set data type. Any description with more characters will simply be cut off at the
specified length.
The name, description and data type are always mandatory. The length is only mandatory for data types
String, Set, Enumerated and MultiByte String.
After you created the domain, you cannot change its name anymore. You can change the other properties.
For more information about the domain properties, see the online help of the Domain Editor.
3 Create the domain.
To create the domain in your local workspace and to exit the wizard, click Finish. The created domain
appears in the Activity Explorer view of the Application perspective.
You can now edit the new domain in the Domain Editor.
## Creating a function

Use the Function Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new function in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
Note: Before you use the new function in an LN application, build the function in LN Studio. If the auto-build
preference is switched on, the function is built automatically.
## Creating a function

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new function. Select
Function as the component type.
c To go to the Function Properties window, click Next.
2 Specify the required function properties.
In the Function Properties window, specify this information:
Name
This is a text value. The function name must start with the code of the package and module in which the
function is used.
Description
The description of the function.
All fields of the Function Properties window are mandatory. After you created the function, you cannot
change its name anymore. You can change the description.
For more information about the function properties, see Function Editor on page 167.
3 Create the function.
To create the function in your local workspace and to exit the wizard, click Finish. The created function
appears in the Activity Explorer view of the Application perspective.
The wizard of LN Studio will automatically create some general source code for the new function, including
a header with metadata and an empty 'skeleton' function.
You can now edit the new function in the Function Editor.
## Creating a label

Use the Label Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new label in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
Note: Before you use the new label in an LN application, compile the label.
## Creating a label

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new label. Select Label
as the component type.
c To go to the Label Properties window, click Next.
2 Specify the required label properties.
In the Label Properties window, specify this information:
Name
This is a text value. The label name must start with the code of the package in which the label is used.
Description
The actual text of the label. You create the label to apply this text in various situations.
Context
The context indicates in which situations you will use the label.
You can only create labels with one of these contexts:
- General Use
- Form Commands
- External Use
- Cascading Item on Button
Labels with other contexts are generated automatically when you create the corresponding software
components. For example, when you create a session, the Create a New Infor LN Software Component
wizard stores the session description you entered in a label with context Session Description.
All fields of the Label Properties window are mandatory. After you created the label, you cannot change
its name and context anymore. You can change the description. As a default, the label type is General
Use.
For more information about the label properties, see the online help of the Label Editor.
3 Create the label.
To create the label in your local workspace and to exit the wizard, click Finish. The created label appears
in the Activity Explorer view of the Application perspective.
The label is created in the primary language of the application.
You can now edit the new label in the Label Editor.
Note: A new label with one variant is created. The specified description becomes the description of the label
and the description of the label variant. In the label editor, you can only edit the latter.
## Creating a library

Use the Library Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new Library in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
Note: Before you use the new Library in an LN application, build the library in LN Studio. If the auto-build
preference is switched on, the library is built automatically.
## Creating a library

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new library. Select Library
as the component type.
c To go to the Library Properties window, click Next.
2 Specify the required library properties.
In the Library Properties window, specify this information:
Name
This is a text value. The library name must start with the code of the package and module in which the
library is located.
Description
The description of the library.
Type
Select a library type from the drop-down list. These library types are used:
- General Library: General DLL - Dynamic Link Library
- Integration DLL: Dynamic Link Library that integrates between packages
All fields of the Library Properties window are mandatory. After you created the library, you cannot
change its name anymore. You can change the other properties. As a default, the library type is General
Library.
For more information about the library properties, see Library Editor on page 174.
3 Create the library.
To create the library in your local workspace and to exit the wizard, click Finish. The created library
appears in the Activity Explorer view of the Application perspective.
The wizard automatically creates some general source code for the new library, including a header with
metadata and an empty 'skeleton' function.
If the name of the DLL consists of the table code with "ue" as suffix, such as whinh200ue, a User Exit DLL
is created. See "User Exit DLL Overview" in the Infor ES Programmers Guide (Infor Customer Portal
KB2924522).
You can now edit the new library in the Library Editor.
## Creating a menu

Use the Menu Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new menu in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
## Creating a menu

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new menu. Select Menu
as the component type.
c To go to the Menu Properties window, click Next.
2 Specify the required menu properties.
In the Menu Properties window, specify this information:
Name
The name of the menu, which includes the following:
- The package code (2 characters).
- The module code (3 characters).
- The menu identification code (8 characters).
After you created the menu, you cannot change its name.
Description
LN Studio automatically stores the description in a label. If you want to change the description after the
menu is created, edit this label in the label editor.
All fields of the Menu Properties window are mandatory.
For more information about the menu properties, see the online help of the Menu Editor.
3 Create the menu.
To create the menu in your local workspace and to exit the wizard, click Finish. The created menu appears
in the Activity Explorer view of the Application perspective.
You can now edit the new menu in the Menu Editor.
## Creating a message

Use the Message Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new message in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
## Creating a message

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new message. Select
Message as the component type.
c To go to the Message Properties window, click Next.
2 Specify the required message properties.
In the Message Properties window, specify this information:
Name
This is a text value. The message name must start with the code of the package in which the message is
used.
Description
The actual text of the message. Create the message to apply this text in various situations. The message
can contain codes that are substituted when the message is displayed.
Message Type
The message type indicates whether the message represents information, a warning or an error.
All fields of the Message Properties window are mandatory. After you create the message, you cannot
change its name, but you can change the other properties. As a default, the message type is Warning.
For more information about the message properties, see the online help of the Message Editor.
3 Create the message.
To create the message in your local workspace and to exit the wizard, click Finish. The created message
appears in the Activity Explorer view of the Application perspective.
The message is created in the primary language of the application.
You can now edit the new message in the Message Editor.
## Creating a question

Use the Question Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new question in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
## Creating a question

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new question. Select
Question as the component type.
c To go to the Question Properties window, click Next.
2 Specify the required question properties.
In the Question Properties window, specify this information:
Name
This is a text value. The question name must start with the code of the package in which the question is
used.
Description
The actual text of the question. Create the question to apply this text in various situations.
Question Type
The question type indicates the severity of the question as information, warning or error. As a default,
the question type is Warning.
Domain
The domain that determines the possible answers to the question. Click Browse to select a domain. The
domain must have the data type Enumerated.
Default Answer
The default answer to the question. Select one of the enumerate constants belonging to the specified
domain.
All fields of the Question Properties window are mandatory. After you created the question, you cannot
change its name anymore. You can change the other properties.
For more information about the question properties, see the online help of the Question Editor.
3 Create the question.
To create the question in your local workspace and to exit the wizard, click Finish. The created question
appears in the Activity Explorer view of the Application perspective.
The question is created in the primary language of the application.
You can now edit the new question in the Question Editor.
## Creating a report

Use the Report Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new report in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
Note: To implement the new report in an LN application, you must synchronize with the server and compile
the report.
## Creating a report

1 Start the wizard and select the component type.
a Start the wizard.
See Create a New Infor LN Software Component wizard on page 94.
b Specify the software development activity for which you want to create the new report.
c Select Report as the component type.
d Click Next. The Select Report Mode window is displayed.
2 Select the report mode.
a In the Select Report Mode window, select how you want to create the report.
- To generate the report, select the Generate Report check box.
- To create the report manually, clear the Generate Report check box.
b Click Next.The Report Properties window is displayed.
3 Specify the required report properties.
The layout of the Report Properties window depends on how you create the report.
- If you create the report manually, specify this information:
Name
This is a text value. The report name must start with the code of the package and the module in
which the report is used. After the report is created, you cannot change its name.
Description
This is a text value. LN Studio automatically stores the description that you enter in a label. If you
want to change the description after the report is created, edit this label in the label editor.
Report Size
To specify a size, click Browse and select a value from the Browse Default Sizes dialog box.
- If you generate the report, specify this information:
Table
The table code of the main table. The combination of the package code, the module code, and the
table number identifies a table. Specify the package code of the table, then click Browse and select
a table from the Browse component dialog box.
Use All Table Fields
If this check box is selected, all table fields of the main table are printed on the report. If this check
box is cleared, click Select Fields and select the desired fields from the Select Table Fields dialog
box.
Report Code
The identification code of the report. A report is identified by a unique combination of package
code, module code and report identifier. To regenerate an existing report, click Browse and select
the report code from the Browse component dialog box. After the report is created, you cannot
change its code.
Report Description
LN Studio automatically stores the description that you enter in a label. If you want to change the
description after the report is created, edit this label in the label editor.
Report Size
To specify a size, click Browse and select a value from the Browse Default Sizes dialog box.
Report Type
Choose one of these options:
- Type 1: Single occurrence report. The fields on the report are printed vertically. Use this report
type if a lot of fields, that do not fit horizontally on a report, must be printed.
- Type 2: Multi occurrence report. The fields on the report are printed horizontally.
- Type 3: Multi occurrence report with a group layout. The fields on the report are printed
horizontally. In addition you can print group headers and group totals.
Use Index
Specify the number of the index. The index is used to print the report in the order according to the
key fields specified in the index.
New Page On
This field is only applicable for type 3 reports.
The number of group fields which must be printed on a new page. If one of these fields changes, a
page break is forced.
The total number of group fields must be less than the total number of key fields.
New Page Off
This field is only applicable for type 3 reports.
The number of group fields which must be printed on a new page.
The total number of group fields must be less than the total number of key fields.
Overwrite Existing Components
If this check box is selected, existing software components are overwritten.
For more information about the report properties, see the online help of the Report Editor.
4 Create the report.
To create the report in your local workspace and to exit the wizard, click Finish. The created report
appears in the Activity Explorer view of the Application perspective.
You can now edit the new report in the Report Editor.
Note: When you create a report in a new application, these labels for general use are automatically created
in the label folder in the Activity Explorer:
- [package code]ttgen.h.comp.lbl - Company
- [package code]ttgen.h.date.lbl- Date
- [package code]ttgen.page.lbl - Page
## Creating a session

Use the Session Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new session in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
Note: To implement the new session in an LN application, synchronize with the server and compile the session.
## Creating a session

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new session. Select
Session as the desired component type.
c To go to the Session Properties window, click Next.
2 Specify the required session properties.
In the Session Properties window, specify these properties:
- Name
- Description
The Name and Description have text values. The session name must start with the code of the package
and the module in which the session is used. After the session is created, you cannot change its name.
The wizard stores the session description in a label. If you want to change the session description, edit
this label in the Label Editor.
To specify one of the other properties is optional. If you do not specify a value, the properties are unset
or get a default value (as displayed in the window). This table shows the used default values:
Remarks
Mandatory and read-only after the session has been
created
Mandatory
Mandatory
Script
Mandatory if Standard Script is No
dling
Read-only field. Equal to the session's Name and Description
Mandatory
Mandatory
Optional
Optional
Property
Name
Default value
- 
Description
Standard
- 
No
Script Type
UI Script with Database Han-
UI Script
- 
Display
Window Type Dialog
True
Main Table
Session Type
Main Session
- 
For more information on the session properties, see Session Editor on page 203.
3 Create the session.
To create the session in your local workspace and to exit the wizard, click Finish. The created session
appears in the Activity Explorer view of the Application perspective.
You can now edit the new session in the Session Editor.
## Creating a table

Use the Table Properties window of the Create a New Infor LN Software Component wizard to initialize
and create a new table in your local workspace. This window is the wizard's second dialog box.
For more general information about the wizard, see Create a New Infor LN Software Component wizard on
page 94.
## Creating a table

1 Start the wizard and select the component type.
a Start the wizard.
b Specify the software development activity for which you want to create the new table. Select Table
as the component type.
c To go to the Table Properties window, click Next.
2 Specify the required table properties.
In the Table Properties window, specify the following properties for the table.
Name
The name of the table.
Table names must have this format: <package code><module code><table number>.
This table shows an example:
tt (tools)
Package
Code
Module
Code
Table number
adv (application development)
01 (sequence number of table)
After you created the table, you cannot change its name.
Description
LN Studio automatically stores the description in a label. If you want to change the description after the
table is created, edit this label in the label editor.
All fields of the Table Properties window are mandatory.
For more information about the table properties, see Table Editor on page 244.
3 Create the table.
To create the table in your local workspace and to exit the wizard, click Finish. The created table appears
in the Activity Explorer view of the Application perspective.
You can now edit the new table in the Table Editor.
## Debugging

## Execute Assignment Expression

Use this dialog to specify an expression. The expression is executed only once.
You can start this dialog from the shortcut menu in the Expressions view.
Expression
Specify the expression in this format: <variable>:=<value>.
For example: curr.compnr:=299
> [!NOTE]
- You can select expressions specified earlier from the list.
- If you select a variable name in the script editor before you start the Execute Assignment Expression
command, this expression is displayed in the dialog: <variable name>:=
For example, you select the task.child.process variable in the script. Then, on the shortcut menu, you
click Execute Assignment Expression. The Execute Assignment Expression dialog starts and contains
this expression: task.child.process:=
Add Watch Expression
If this check box is selected, the name of the variable is displayed in the Expressions view.
For example, if you enter curr.compnr:=299, the curr.compnr variable is displayed in the Expressions view.
If this check box is cleared, the name of the variable is not displayed in the Expressions view.
### Line Breakpoint properties

Use this dialog to view or modify the properties of a line breakpoint.
Note: You cannot use this dialog to create new breakpoints.
For details on how to set new breakpoints, see Using breakpoints on page 68.
Location
The component, such as a script or library, where the breakpoint is set.
Line Number
The line number in the source code where the breakpoint is set.
Enabled
If this check box is selected, the breakpoint is enabled. The program execution suspends when the breakpoint
is reached.
If this check box is cleared, the breakpoint is disabled. The breakpoint is ignored during the program execution.
### Method Breakpoint properties

Use this dialog to view or modify the properties of a method breakpoint.
Note: You cannot use this dialog to create new breakpoints.
For details on how to set new breakpoints, see Using breakpoints on page 68.
Location
The component, such as a script or library, where the breakpoint is set.
Function
The name of the method for which the breakpoint is set.
Enabled
If this check box is selected, the breakpoint is enabled. The program execution suspends when the breakpoint
is reached.
If this check box is cleared, the breakpoint is disabled. The breakpoint is ignored during the program execution.
Function Entry
If this check box is selected, the program execution suspends when the execution reaches the function for
which the breakpoint is set.
### Watchpoint properties

Use this dialog to view or modify the properties of a watchpoint.
Note: For details on how to set new watchpoints, see Using breakpoints on page 68.
Location
The component, for example a script or library, where the watchpoint is set.
Variable
The name of the variable for which the watchpoint is set.
Enabled
If this check box is selected, the watchpoint is enabled. The program execution suspends, based on the
setting specified in the Suspend on field.
If this check box is cleared, the watchpoint is disabled. The watchpoint is ignored during the program
execution.
Suspend on
Indicates when the program execution will suspend.
Allowed values
The program execution suspends when the value of the variable changes.
tion
The program execution suspends when the variable gets the indicated value.
See the previous figure for an example. The session will suspend when the curr.ke
y variable gets the value 2.
Variable Modifica-
Variable Value
## Preference Pages

## Preferences - BFlow

Use this dialog window to specify your BFlow preferences.
Clear console before launch
If this check box is selected, the LN Studio Console is cleared before a BFlow run or debug configuration is
launched.
Note: In a multi-tenant environment you cannot run or debug BFlows with LN Studio. You can run BFlows
in the LN UI to see the result.
BFlow events log level
Select the global log level for BFlow events. Use this setting to control the type and amount of log events
received from the server that are displayed in the console.
To improve the performance when running BFlow cases that have many steps, select a log level that generates
fewer log messages.
This table shows, per log level, the log messages that are received.
Log Levels
Debug
Log Messages
ENVIRONMENT
STATE
NOTICE
WARNING
ERROR
SESSION
CONNECTION
STEP
INFO
Minimal
Medium
Full
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
Preferences - Templates
Use this dialog window to create, edit, and remove BFlow templates.
Overview window
Use the check boxes to enable and disable templates. If a check box is selected, you can select the
corresponding template when you create a BFlow step in the Create a New Infor LN Software Component
wizard.
Use these buttons to manipulate and configure templates:
Button
New
Edit
Remove
Description
Opens a dialog box to create a new template.
Opens a dialog box to edit the currently selected template.
Removes all selected templates.
Button
Restore Removed
Revert to Default
Description
Restores any predefined templates that have been removed.
Import
Export
Restores any predefined templates to their default configuration.
This action does not modify user-created templates.
Imports templates from an XML file in the file system.
Exports all selected templates to an XML file in the file system.
Edit Template dialog window
Name
The name of the template.
Context
Indicates the type of template. For BFlow templates, the context is always BFlowTest.
Automatically insert
Has no meaning for BFlow templates.
Description
The description of the template.
Pattern
The pattern of the template. This is the text inserted in the Create a New Infor LN Software Component
wizard when you select the template.
In the template pattern, you can use predefined template variables. Variables are resolved to their concrete
value when the template is evaluated in its context. You can specify variables using simple or full syntax. If
there are multiple possible matches for a variable, they are presented as proposals to the user.
To add a variable to the template pattern, click Insert Variable and select the desired variable from the list.
You can select general and LN-specific template variables.
## Preferences - Editor

Use this dialog window to specify your script editor preferences.
These settings only apply to the LN Studio Script Editor.
Marker Identifier
Determines the text that is added in the source code, when you add maintenance comments.
Allowed values
The name of the current Activity.
The ID of the business requirement to which the current activity belongs.
ID
Activity Name
Activity Requirement
Project Name
Project Requirement
ID
The name of the current Software Project.
The ID of the business requirement to which the current project belongs.
Example
Marker Identifier = "Activity Name", and your current activity is "myactivity".
In the Script Editor, you mark lines as new. The following maintenance comments are added:
- Behind the first new line: " |#myactivity.sn ".
- Behind the last new line: " |#myactivity.en ".
See "Comments" in the Infor LN Studio Application Development Guide.
Show Mark Occurrences
If this check box is selected, Mark Occurrences is enabled, so occurrences of the selected element are marked
in the source code. See "Mark Occurrences" in the  Infor LN Studio Application Development Guide.
Highlight Matching Brackets
If this check box is selected, the script editor can highlight matching brackets in the source code.
Usage: Place the cursor directly behind a bracket. The corresponding bracket is highlighted automatically.
This functionality applies to the following types of brackets:
- Parentheses: (, ).
- Braces: {, }.
Remove Trailing Whitespaces on Save
If this check box is selected, the script editor removes trailing whitespaces (space and tab) of each line in the
source code during save actions.
Delay key manager
The number of milliseconds after which the editor's parser will react to the last key-event.
This only works if the editor is in asynchronous mode.
Max LOC of syn. behaviour
The maximum number of lines of code for which the editor can run in synchronous mode. For the remaining
lines, the editor switches to asynchronous mode.
> [!NOTE]
In synchronous mode, the parser directly reacts to each key-event. As a result, all changes are colored
immediately.
If you enter 0 in this field, the editor always runs in asynchronous mode.
Max LOC of parser
The maximum number of lines of code the parser can handle.
If a script has more lines, the parser does not react anymore. Therefore, all editor functionality that requires
the parser's output drops out. This enhances the performance when editing very large scripts.
Max LOC of syntax highlighting
The maximum number of lines of code to which syntax highlighting can be applied.
If a script has more lines, the parser does not react anymore. Therefore, all editor functionality that requires
the parser's output drops out. This enhances the performance when editing very large scripts.
Background Color
Use this field to set the background color for your editor.
Choose one of the following options:
The default background color is white.
faults
Choose the color from a basic color schema or define custom colors.
System De-
Custom
> [!NOTE]
The editor only uses this color for source code of checked out components. If a component is not checked
out, the source code is read-only and the editor uses the ReadOnly color.
ReadOnly
Use this field to set the background color for read-only source code, such as source code of components that
are not checked out.
Choose the color from a basic color schema or define custom colors.
Preferences - Code Assist
Use this dialog window to specify your Code assist preferences.
These settings only apply to the LN Studio Script Editor.
See "Code Assist" in the  Infor LN Studio Application Development Guide.
Code Assist
Enable Code Assist
Select this check box to enable the code assist feature.
Present proposals in alphabetical order
If this check box is selected, Code assist presents the list of suggested completions in alphabetical order.
Automatically insert
If this check box is selected, and if there is only one completion proposal for the string you entered in the
Script Editor, code assist will automatically insert the proposal at the cursor position.
Example
In the Script Editor, you type " she " and press CTRL+SPACE. Code assist automatically inserts the following
text, because this is the only completion proposal available: " shell(command,mode) ".
Completion proposal background
The background color for the completion proposal.
Completion proposal foreground
The foreground color (text color) for the completion proposal.
Auto Activation
Enable auto activation
If this check box is selected, Code Assist starts automatically when you type the auto activation trigger
character.
Auto activation delay
The delay in milliseconds between the moment you type the auto activation trigger character, and the
moment Code assist starts automatically.
Auto activation trigger Char for Infor LN
The character that triggers the auto activation of Code assist. The default is a dot (.).
Preferences - Folding
Use this dialog window to specify your Folding preferences.
These settings only apply to the LN Studio Script Editor.
See "Folding" in the  Infor LN Studio Application Development Guide.
Enable folding
If this check box is selected, you can fold and unfold the selected region types when you open a new editor.
If this check box is cleared, you cannot fold and unfold any region type in the script editor.
Collapse all selected region types when opening the Editor
If this check box is selected, all selected region types are collapsed automatically when you open the script
editor.
Folding these region types:
Functions
If this check box is selected, folding is enabled for functions.
Header
If this check box is selected, folding is enabled for header comments.
Macro's
If this check box is selected, folding is enabled for macros.
Section
If this check box is selected, folding is enabled for script sections, such as the declaration section, the
before.program section, and field sections in a UI script.
Preferences - Syntax
Use this dialog window to specify syntax coloring preferences.
These settings only apply to the LN Studio Script Editor.
Limitations
The script editor does not recognize syntax patterns because no syntax parser is available in this release.
Therefore, if a variable has a name identical to a keyword such as "domain", "function", or "case", the variable
is colored as a keyword. For example:
- You add the following code to the declaration section of a UI script: long case.
- case is colored as a keyword, because the editor does not recognize it as a variable.
Syntax Coloring
Specify the syntax coloring settings for various elements in the program text.
To specify the syntax coloring settings for an element:
1 Select the element from the list.
2 Specify whether the element must be bold and/or italic.
3 Click the color button.
4 Select the color from a basic color schema or define custom colors.
Preview
Shows a preview of your syntax coloring settings.
Preferences - Templates
Use this dialog window to create, edit, and remove templates.
These settings only apply to the LN Studio Script Editor.
To insert a template in the script editor, use the Code Assist feature.
Overview window
Use the check boxes to enable and disable templates. If a check box is selected, you can use Code Assist to
insert the corresponding template in your source code.
Use these buttons to manipulate and configure templates:
Button
New
Edit
Remove
Restore Removed
Revert to Default
Description
Opens a dialog box to create a new template.
Opens a dialog box to edit the currently selected template.
Removes all selected templates.
Restores any predefined templates that have been removed.
Import
Export
Restores any predefined templates to their default configuration.
This action does not modify user-created templates.
Imports templates from an XML file in the file system.
Exports all selected templates to an XML file in the file system.
Edit Template dialog window
Name
The name of the template.
Context
This is a standard Eclipse option that is not used by LN Studio.
Automatically insert
If this check box is selected, code assist automatically inserts the template at the cursor position, if the
template is the only completion proposal for the string you entered in the Script Editor.
Description
The description of the template.
Pattern
The pattern of the template. This is the text inserted in the editor when you select the template.
In the template pattern, you can use predefined template variables. Variables are resolved to their concrete
value when the template is evaluated in its context. You can specify variables using simple or full syntax. If
there are multiple possible matches for a variable, they are presented as proposals to the user.
To add a variable to the template pattern, click Insert Variable and select the desired variable from the list.
You can select general and LN-specific template variables.
This table shows the general template variables:
Description
Specifies the cursor position when you leave the template edit mode. This
is useful if the cursor must jump to another place than to the end of the
template, on leaving template edit mode.
The current date.
The dollar symbol '$'. Alternatively, you can use two dollar signs: '$$'.
The content of all currently selected lines.
The current time.
The user name.
The content of the current text selection.
The current year.
Variable
${cursor}
${date}
${dollar}
${line_selection}
${time}
${user}
${word_selection}
${year}
This table shows the LN-specific template variables:
Description
The name of the function which is used above this variable
The arguments of the function which is used above this variable.
The return type of the function which is used above this variable.
Place holder
Variable
${name}
${input_arg}
${returnType}
${output_arg}
## Preferences - Launching

Use this dialog window to specify your launching preferences.
When you launch a software component, the LN Studio checks whether the release of the corresponding
application matches the package combination in which the component is executed. If they do not match,
you may encounter problems during debugging.
In this dialog, you can specify whether/how the launch should continue if release and package combination
do not match.
> [!NOTE]
- The application release is specified in the Create a new Application dialog. The release is identical to
the Base VRC on which the software development is based.
- The package combination depends on the runtime address connection points of the application's software
projects. A runtime address connection point is linked to a .bwc file. You can find the package combination
in the user data of the user account specified in this .bwc file. To view the user data, run the User Data
(ttaad2500m000) session. Alternatively, look in the Command field of the BW Configuration Properties
dialog.
Default Launch Mode
Specify how sessions are started by default.
Select an option. In the Configurations dialog, the corresponding launch mode is selected automatically.
Allowed values
- Launch in BW
- Attach to running Web UI
Continue if release does not match package combination
Use this field to specify whether/how the launch will continue if release and package combination do not
match.
Select one of the following options:
The session is launched anyway.
ways
The session is not launched.
er
Prompt A warning is displayed and you can choose whether you want to launch the session.
Al-
Nev-
The default option is Prompt.
## Preferences - Multipage

Use this dialog window to specify preferences for the Multipage Editors.
Display the TDE overview page for all editors
If this check box is selected, a TDE Documentation tab is displayed in all multipage editors. This tab shows
an XML tree with the technical information on the software component's Technical Data Entity.
The information displayed in the TDE Documentation tab is primarily intended for support and
troubleshooting purposes. Therefore it is recommended to display the tab only in case of problems.
Path for Additional File attachments
The directory where LN Studio stores the additional files that you edit in the Additional File Editor.
## Views

Preferences - Activity Explorer
Use this page to specify which additional information should be displayed in the Activity Explorer view.
Display Activity Requirement ID
If this check box is selected, the ID of the business requirement to which the activity belongs is displayed.
Requirements are usually stored in a requirement management or defect tracking system.
Display Activity Description
If this check box is selected, the description of the activity is displayed.
## Preferences - Workbench

Use this dialog window to specify whether the editor is opened automatically each time you add a new
resource to your workspace.
The script editor can start automatically, for example:
- When you use the Get command in the Component Explorer view to add a component to your workspace.
- When you use the Open Declaration (source) command in the script editor to view detailed information
on a function that is called in your source code and not present in your workspace.
- During debugging, when you step into a function that is called in your source code, but not already
present in your workspace.
Automatically open the editor for a new resource
Use this field to specify whether the corresponding editor is opened automatically for a new resource.
This table shows the available options:
The editor starts automatically each time you add a component to your workspace.
ways
The editor does not start automatically when you add a component to your workspace.
er
Al-
Nev-
Prompt
When you add a component to your workspace, the following question is displayed:
"Open editor for the new software component?"
Click Yes or No to answer the question.
Optionally, click the Remember my decision check box in the question window. Depending on
your answer to the question, this will change the Automatically open the editor for a new resource
preference setting to "Always" or "Never".
The default option is Prompt.
Automatically check components after a change
If this check box is selected, LN Studio automatically verifies software components each time a component
is saved.
If this check box is cleared, components are not verified automatically. You must start the verification manually
through the Verify Component command in the shortcut menu in the Activity Explorer view.
For details, see "Verifying software components" in the  Infor LN Studio Application Development Guide.
## Preferences - Infor LN Configuration Management

Note: This page is not located under Infor LN Studio Application preferences, but under Team preferences.
Use this dialog window to specify your Configuration Management preferences.
Checkout while editing
Indicates whether LN Studio must prompt you to checkout a software component when you edit the
component in the corresponding editor.
Select one of the following options:
You cannot check out a component while editing. To change a component, you must first check
out the component and then start the corresponding editor.
Prompt You can check out a component while editing.
If you try to change a component, which is not yet checked out, you are prompted whether you
want to check out the component.
If you click Yes, the component is checked out so you can change it.
If you click No, the component is not checked out so you cannot change it.
Never
The default option is Prompt.
Decorations
Append version information to resource name
If this check box is selected, LN Studio appends the version and release information of the application to the
resource names displayed in the Activity Explorer view.
For example: 7.6_a4
Show image decoration for dirty resources
If this check box is selected, LN Studio displays a  decorator in the Activity Explorer view for each resource
not in sync with the LN server.
A resource is dirty if the version stored in your local workspace differs from the version on the LN server.
Resources can become dirty if the Build Automatically option is turned off: When you save changes you
make to a resource, the changes are saved in your local Eclipse workspace. However, the software component
on the LN server is not updated.
You must build the component to synchronize the local resource and the LN server. The  decorator
disappears automatically.
Text decoration for dirty resources
The character entered here is displayed as a prefix to the names of dirty resources in the Activity Explorer
view.
A resource is dirty if the version stored in your local workspace differs from the version on the LN server.
Resources can become dirty if the Build Automatically option is turned off: When you save changes you
make to a resource, the changes are saved in your local Eclipse workspace. However, the software component
on the LN server is not updated.
You must build the component to synchronize the local resource and the LN server. The prefix disappears
automatically.
End Activity Behavior
By default, close the activity
If this check box is selected, the activity is ended completely when you run the End Activity command in the
Activity Explorer. The activity disappears from the Activity Explorer.
If this check box is cleared, the activity is ended partially when you run the End Activity command in the
Activity Explorer. The activity is still present in the Activity Explorer.
## Verify Software Components

### Verify Components View Filter

Use this dialog to specify a filter for the Verify Components view.
To start the dialog, click Verify Warning Filter in the Verify Components view's toolbar.
Enabled
Indicates whether the filter is enabled. You must select this check box if you want to define a filter.
Warning level
This field indicates the warning levels that are displayed. You can select multiple levels. The selected levels
are supplementary.
For example: You select High (1) and Normal (2). Warnings of level 1 and 2 are displayed.
Warning status
This field determines the warning statuses that are displayed. You can select both check boxes. The options
are supplementary.
Allowed values
Select this check box to display blocking warnings.
Exclude accept- Select this check box to exclude accepted warnings from the
list.
Only blocking
ed
Note: The selections in the filter are supplementary.
For example, in the filter properties you select the Normal (2) warning level and the Only blocking status.
As a result the following is displayed:
- All "Normal" warnings, regardless of their warning status.
- All blocking warnings, regardless of their warning level.
Resources
This field determines the resources, for which warnings are displayed.
Allowed values
LN Studio displays warnings for all resources in the Activity Explorer.
LN Studio displays warnings for the resource that you selected in the Activity Explorer, and for all resources that belong to the same project.
LN Studio only displays warnings for the resource that you selected in
the Activity Explorer.
On any resource
On any resource in same
project
On selected resource only
### Verify Warning Details

Use this dialog box to perform these actions:
- View the details of warnings generated when you verify software components.
- Accept warnings.
This dialog box is important in the procedure to handle warnings.
See Verifying software components on page 56.
VSC Warning
Warning Id
The unique code that identifies the message assigned to the warning.
For example: the message ID for a warning is 5053. The corresponding message text is Function 'sleep' is
not supported by Web UI .
Note: This field corresponds with the VSC ID column in the Verify Components view.
Message
The text of the message assigned to the warning.
For example: Function 'sleep' is not supported by Web UI
Detailed Information
Resource
The LN Studio resource that represents the software component for which the warning is generated.
For example:
- tfgld1101m000.ses (session)
- tfgld1101m000.sessrc (program script)
Project
The software project to which the software component belongs.
VSC Verification Code
The verification code for which the warning was generated.
Component name
The code that identifies the software component for which the warning was generated.
Component type
The type of the main component for which the warning was generated.
For example:
A warning is generated because of an error in a session's UI script:
- The component type is "session".
- The component subtype is "script".
Component subtype
The subcomponent type for which the warning was generated. Each software component type has its own
types of subcomponents.
Some examples of subcomponents are:
- A form command in a form.
- A field in a form.
- An index in a table.
- A text field in a table.
- A field section in a UI script.
- A choice section in a UI script.
Component location
The location in the software component where the problem occurs.
For example:
- A line number in a script or library.
- A form or report in a session.
Component element
The component element that causes the problem.
For example:
A warning is generated because an expired label is used in a form:
- The component type is "session".
- The component subtype is "form".
- The component element is the expired label, such as ttadv4122sDF1.
VSC Status
Priority
The priority of the warning: high, normal, suspicious, or low.
Priorities are automatically assigned by the verification process:
- The priorities for warnings generated based on source analyze codes, are defined in the Source Analyze
Codes (tlvsc3511m000) session.
- The priorities for warnings generated based on all other types of checks are hard coded in the VSC
software on the LN server.
Blocking
This field indicates whether the warning blocks the check in of a component.
If a warning is "blocking", either solve or accept the warning immediately.
See Verifying software components on page 56.
Accepted
This field indicates whether the warning is accepted.
Accept
Acceptance allowed
This field indicates whether it is allowed to accept the warning.
Allowed values
True It is allowed to accept the warning. The Accept Warning field is enabled.
False You cannot accept the warning. The Accept Warning field is disabled.
Note: This field is read-only. The value is determined by the rules used by VSC.
Accept Warning
To accept the warning, select this check box. In the Accept Text field, enter the reason for acceptance.
To solve the warning, clear this check box.
For example, the following warning is generated: "Possible missing break in case statement".
- If this break is not missing, but left out on purpose, select this check box and accept the warning.
- If this break was left out accidentally, clear this check box and solve the warning.
See Verifying software components on page 56.
Accept Text
If you select the Accept Warning check box to accept a warning, enter the reason in this field.
Help
Starts the Verify Warning Help dialog box, which shows information to solve the warning.
### Verify Warning Help

This dialog box shows help for the selected VSC warning.
You can start the dialog box from the Verify Warning Details dialog box.
This table shows the information that is usually displayed:
Type of information
Short Description
Description
A short description of the error.
For example:
Presence of goto statements
Type
Severity
Description
The warning type, such as Error or Warning.
The severity of the warning, such as High or Medium.
A more detailed description of the error.
For example:
The use of 'goto' statement is forbidden.
Exception: within #defines it is allowed. Sometimes it is required (for
example exception handling)
Motivation
The reason why the situation indicated in the error message is not correct.
For example:
'Goto' statements reduce the readability of script code dramatically.
Possible Solution
A hint for a possible solution.
For example:
Implement structured code (early return or if-then-else statements)
Examples
Examples to understand and solve the error.
This dialog box is important in the procedure to handle warnings.
See Verifying software components on page 56.
## Miscellaneous

### Check In comment

Use this dialog to enter check in comments for software components.
The dialog starts automatically when you check in one or more components.
Click OK to save the comment and to check in the component.
Click Cancel to cancel the check in. The comment is not saved.
Note: The revision text is stored in the configuration management system on the server. A single text is used
for all revisions of a component. This text is displayed each time you check in a new revision of the component,
so you can modify or extend it.
Use this comment for all selected components
This check box is only displayed if you check in multiple components in one go.
If this check box is selected, the revision text entered is used for all components you selected in the Activity
Explorer.
If this check box is cleared, you must enter a separate revision text for each component.
## Configuration Management

Use this dialog box to view the configuration management properties of an LN Studio resource.
Configuration Management Information
Type
The type of configuration management system used for the resource.
There is only one type of configuration management: LN Configuration Management (BaanSCM), which is
based on the Software Configuration Management (SCM) module in Enterprise Server. A more extensive CM
solution will be offered in a future release.
See Activity based development on page 37.
General Information
Checked Out
Indicates whether the resource is checked out.
Dirty
Indicates whether the resource is dirty. A resource is dirty if the version stored in your local workspace differs
from the version on the LN server.
A resource can get dirty, for example, if you do not create a new build after you have modified the resource.
To avoid dirty resources, select the Build Automatically option on the Project menu.
General Information
Type
The type of resource, such as session or library.
Component Name
The name of the resource.
Version
The VRC ( Version - Release - Customer) to which the component belongs.
Expired
Indicates whether the resource is expired.
### Configurations

Use the Run Configurations and Debug Configurations dialog boxes to create, run, or debug configurations.
To add a configuration:
1 Complete one of these steps:
- To add a run configuration, select Run > Run Configurations.
- To add a debug configuration, select Run > Debug Configurations.
2 In the left pane of the Run Configurations or Debug Configurations dialog box, right-click Infor LN
Session and select New. These tabs are displayed:
- Sessions
- BFlow
- Profiling
- Environment
- Common
3 Specify the configuration settings in these tabs and click Apply.
For details on the tabs mentioned, see the field help.
Sessions
Use this tab to specify the session you want to start, and the company in which the session must run.
## Activity

Select an activity from the list.
Session
Select the session you want to run. The name of the configuration is automatically filled with the name of
the selected session.
To select a session, perform one of these actions:
- Select a session linked to your activity from the list.
- Click Browse. The Browse session dialog starts. In this dialog you can select a session on the LN server.
The session does not have to be linked to your activity.
- Specify a session code. The session does not have to be linked to your activity.
Note: You can only select sessions that belong to the packages displayed in the Component Explorer
Launch Mode
Specify how the session is started.
Allowed values
The session is launched by BW ( BW Configuration).
BW
Web UIWeb UI
See the Web UI About screen for the currently used port number.
Launch in
Note: If you run a session in Web UI, any new or changed labels are only displayed if the session is compiled
and linked to your activity.
Company
Select a company in which the session must be started.
Perform one of these actions:
- Select Start session in company of connection point and specify the company linked to your project's
Runtime Address connection point. To find out the corresponding company number:
1 Select Windows > Preferences. The Preferences dialog is displayed.
2 In the tree that is displayed in the left pane of the dialog, select Infor LN JCA Connectivity. The
Infor LN JCA Connectivity dialog appears.
3 Select the Runtime Address connection point and click Edit. The company number is displayed.
- Select Start session in company and specify another company.
BFlow
Use this tab to specify the BFlow test script you want to start, and the company in which the script must run.
## Activity

Select an activity from the list.
Test Script
Select the test script you want to run.
Company
Select a company in which the test script must be started.
See the description of the Company field on the Sessions tab.
BFlow events log level
Select the log level for BFlow events. Use this setting to control the type and amount of log events received
from the server that are displayed in the console.
To improve the performance when running BFlow cases that have many steps, select a log level that generates
fewer log messages.
This table shows, per log level, the log messages that are received.
Log Levels
Minimal
Medium
Full
Debug
Log Messages
ENVIRONMENT
STATE
NOTICE
WARNING
ERROR
SESSION
CONNECTION
STEP
INFO
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔
Profiling
Optionally, use this tab to specify profiling parameters.
Profiling is used to display performance statistics for a session. For details, see "The Call Graph Profiler" in
the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
Enable profile mode
If this check box is selected, you can specify profiling parameters.
When you run the session, a Call Graph Profile is generated.
Sorted by runtime
Select this check box to add information that is sorted by runtime to the Call Graph Profile.
Filter
Use this field to specify a filter. If this check box is selected, you can, for example, enter the name of an object.
The generated profile contains only statistics for the specified object.
This field corresponds with the value of the PROFILE_ALL variable. See "The Call Graph Profiler" in the Infor
ES Programmers Guide (Infor Customer Portal KB2924522).
Alternative directory on Infor LN Server
If this check box is selected, you can specify a directory on the LN server to store the Call Graph Profile files.
The default value is $BSE_TMP.
This field corresponds with the PROF_DIR variable. See "The Call Graph Profiler" in the Infor ES Programmers
Guide (Infor Customer Portal KB2924522).
Attach toSave profile results on local client
If this check box is selected, you can specify a directory on your client PC to store the Call Graph Profile files.
See the description of the PROF_CLIENT variable in the Infor ES Programmers Guide (Infor Customer Portal
KB2924522).
Start default browser
If this check box is selected, the generated profile is automatically displayed in your default Web browser.
See the description of the PROF_CLIENT variable in the Infor ES Programmers Guide (Infor Customer Portal
KB2924522).
Environment
Use this tab to specify environment variables.
Environment
Append environment to native environment
Select this option to append the environment variables to the native environment variables.
Replace native environment with specified environment
Select this option to replace the native environment variables with the specified environment variables.
Common
This tab is not used by LN Studio. It contains only standard Eclipse options. See the Workbench User Guide.
## Copy from other layouts

Use this dialog box to select report layouts you want to copy from an existing report to a new report.
You can start this dialog box from the Report Editor.
Click the desired layouts and click OK to close the dialog box.
Note: The dialog box shows the layouts of a single report. To select another report, click Browse Reports.
## Create a new Application

You can use the New Application dialog box to create a new application.
New Application window
To open the New Application dialog box, complete one of the following steps:
- Right-click the Application Explorer view of LN Studio and, on the shortcut menu, select New Application.
- Click the New Application button on the Application Explorer's toolbar.
To create a new LN Studio application, in the New Application dialog box, fill in the required fields and click
OK. The new application is created in the currently connected LN server as indicated by the Administrator
Connection Point in the Infor LN JCA Connectivity window.
The following section describes the fields of the New Application dialog box.
Note: To view or modify the properties of an existing application, use the Application Properties dialog box.
This dialog box is identical to the window described here, except for the Application name field. When you
create a new application, specify an application name. When you modify an existing application, you cannot
change the application name (read-only field).
Application
Use the upper part of the dialog to specify basic application properties.
Application name
The name of the application.
When you create a new application, it is mandatory to specify an application name.
Allowed values
The application name identifies the application. Therefore, the application name must be unique in the
context of the connected LN server. The name can be any ASCII text with a maximum length of 30 characters.
Description
The description of the application.
Specifying an application description is optional.
Allowed values
The description is a (multi byte) text with a maximum length of 50 characters.
Release
The release of the application.
For LN applications, the release is identical to the Base VRC on which the software development is based.
See Applications on page 22.
Specifying a release is mandatory.
Note: An LN Studio application is linked to the Base VRC of a PMC module. Within the PMC module, the
package VRCs are linked to the export VRC of the PMC Base VRC.
Allowed values
To specify a value for this field, select a release from the drop-down list.
Base
This field is not yet implemented.
Note: You can access the field and select a value from the list. However, this value is ignored by the LN Studio.
Therefore, you are recommended to leave this field empty.
InContext Reference Model
The application's InContext Reference Model.
Related topics
- "InContext Modeling" in the  Infor LN Studio Application Development Guide
- Infor Enterprise Server InContext Modeling Development Guide
Use SCM
If this check box is selected, the software components developed or modified in LN Studio are managed with
the Software Configuration Management (SCM) tool of the connected LN environment.
Use SCM to perform version management for packages linked to the application, or for the individual activities
of the application. To use SCM for the version management of the packages, SCM must be enabled for the
associated Project VRC on the LN server. If SCM is not enabled, you cannot add a package from this VRC to
the application.
See "Activity based development" in the  Infor LN Studio Application Development Guide.
Packages
Use this tab to link packages to the application.
Package
A package linked to the application.
In LN Studio, you can link packages to an application. These packages must have a VRC that corresponds
with the Export VRC of the Base VRC of the PMC module. This must also match the Base VRC of the application.
This Export VRC contains the application data with the linked packages. LN Studio will automatically create
such an Export VRC, if no such VRC is available.
The Packages field displays a table with the packages that have been linked to the application. These
packages have the same Base VRC as the application. The table shows the name of the packages and the
package description. An additional field indicates whether the package is used.
To link packages to the application:
1 Click Add. An empty package record is added to the Packages grid. Then, in the Package field, select a
package from the drop-down list. This list contains all the packages linked to the application's Base VRC.
After you select a package, the package name and description are displayed in the grid.
Note: To add all packages at the same time, click Add All.
2 To indicate whether a package is used in the application, select or clear the corresponding Active check
box in the grid.
Note: You require special authorization to create or modify applications linked to a Base VRC of a standard
LN release. To make a customization for a particular customer, copy the application to the customer's
application.
Description
The description of the package.
This field is read-only. The specified description is derived from the selected package.
Active
If this check box is selected, the package of the application is changed or modified in LN Studio.
Allowed values
The check box is cleared.
Languages
Use this tab to link software languages to the application.
Language
A software language linked to the application during development time.
> [!IMPORTANT]
If you use the Language Translation Support functionality, to translate labels or other user interface
components, do not add secondary software languages to an application. Only use secondary software
languages for small translations performed by a software developer, outside the framework of the LTS
export/import mechanism.
The term "software language" refers to a language used by the application to communicate with the
application user. Therefore, when you run the application, the text on the buttons, commands, menus,
messages and so on, are expressed in one of the software languages linked to the application.
You can link multiple languages to an application, depending on the language packs installed on the
application's LN environment.
An LN Studio application can have two types of languages: primary and secondary. Each application must
have only one primary language. This is the development language and used to display the editable
components throughout the user interface of LN Studio. If any references are made to another component,
this reference is expressed in the primary language. By default, the primary language is 2. If you do not specify
a primary language, English is used.
Apart from the primary language, an application can possess multiple secondary languages. These can be
considered as translations of the expressions in the primary language. You can view and modify these
translations in the editor of the concerned software component. The translations are used when running
the application in a mode for a particular secondary language, determined by the language of the user.
The Languages field displays a table with all languages linked to the application. These languages must be
installed on the LN server connected to LN Studio through the Administrator connection point. The table
shows the name of the languages and the language descriptions. An additional field indicates whether the
language is a primary or secondary language.
To link a new language to the application, complete the following steps:
1 Click Add. An empty language record is added to the Languages grid.
2 In the Language field, select a language from the drop-down list. This list contains all the packages
installed on the connected LN server. After you select a language, the language code and language
description are entered in the grid.
3 To indicate whether the language acts as primary language, select or clear the Primary check box.
Description
The description of the language.
This field is read-only. The specified description is derived from the selected language.
Primary
If this check box is selected, the current language will act as the primary language of the application. If this
check box is cleared, the current language is a secondary language.
> [!NOTE]
If you set the primary language of the application, any language that was previously the primary language
will automatically be marked as a secondary language.
Allowed values
The check box is cleared.
Documentation
Documentation
Use this field to specify additional information.
## Create a New Form Command

Use this dialog window to create a new form command.
Session
The session to which you link the form command.
Activation Type
Specifies what your form command activates. You can select the following activation types from the drop-down
list. The used type names are self explanatory.
Allowed values
- Function
- Session
- Business Method
- Menu
Function/Session/Business Method/Menu
The name of the function, session, business method, or menu the form command activates.
Note: Any session you specify must exist in the development repository of the connected LN server. The
function or business method must be part of the session's program script, or DAL script respectively.
Allowed values
If the activation object is a session, you must specify a session that already exists in the LN application,
because you cannot create new sessions in the LN Studio.
The Browse button only applies to sessions and not to other activation objects. Use the browse functionality
to select a session.
For activation objects other than Session, you do not require to select an pre-existing object. Note, however,
that any specified function or business method must be part of the session's program script, or DAL script
respectively.
Command Type
Specifies where the form command appears on the session's form. You can select the following command
types from the drop-down list:
Allowed values
For all of the session's form tabs, the form command appears on the form's appropriate
menu, and/or as a button on the form.
The form command only appears on the session's appropriate menu when a user selects
the tab that includes the group you define in the Group/Field Number field.
Form
Group
Field
Print
The form command appears as a button on the form, behind the field whose Sequence
Number you enter in the Group/Field Number field.
The form command appears as an option in the session's print menu.
Group / Field Number
This field specifies the group to which the form command belongs or the sequence number of the field that
is linked to the form command. Whether this field specifies a group or a sequence number depends on the
value you specified as the Command Type: Group or Field.
This field only applies to form commands of type 'Group' or 'Field'. The field is disabled for the other form
command types ('Form' and 'Print').
For form commands of Command Type Group, select the group to which the form command belongs. The
form command only appears in the session's appropriate menu when the user selects the group's tab.
For form commands of Command Type Field, select the field behind which the form command appears as
a field button.
The pull down list shows the numbers and label codes of the available groups or fields.
Allowed values
To specify this field, select a value from the drop-down list.
## Duplicate an Infor LN Software Component

Use this wizard to make a copy of an LN Studio component in your local workspace. The copy is an exact
duplicate, with the exception of the name of the component. In the wizard, you must specify this name. Make
sure you enter a new, unique name.
The wizard saves the copied component on the file system and, if applicable, adds it to source control.
You can only duplicate a component if you are authorized to do so:
- You cannot duplicate components that were automatically generated by LN Studio, such as a label with
the Session, Table or Report Description context when you create a new session, table or report.
- You cannot duplicate components from an LN Studio Activity that has been re-assigned to another user.
After an LN Studio Activity has been re-assigned, you loose the ownership of the activity's components.
Duplicating an LN Studio software component
1 Start the wizard for an existing component
In the Activity Explorer view, right-click the LN Studio component you want to duplicate and select
Duplicate Component. This starts the Duplicate an Infor LN Software Component wizard.
The component that is to be copied must be present in the current LN Studio Activity project.
The Duplicate an Infor LN Software Component wizard displays the following information about the
component you selected for duplication:
Description
The current LN Studio Activity in which the component is duplicated.
The LN Studio Software Project to which this activity belongs is indicated behind the
activity name, between square brackets.
Field
Project
Field
Component Type
Source Name
Description
The type of component, such as Library or Session.
The name of the original component that is duplicated. This name is the identifying
attribute of the component.
The description of the original component that is duplicated.
Source Description
All these properties of the existing component are displayed in read-only mode.
2 Specify properties for the new component
Specify the following properties for the new component:
Description
Specify a unique component name.
Name
code of the package in which the component is used. Some component names must additionally include the code of the involved module. For more information on the allowed
values, see the wizard's messages and the description of the editor of the concerned component.
After you copied a component, you cannot change the component's name anymore. For
existing components, the name is read-only, because the name forms the identifying attribute
of the component. Changing a component's name would make it another component.
Specifying a Target Description is optional. If you do not fill in a description, the component
inherits the description of the component from which it is copied. The component description
can be any ASCII text with a length of less than 60 characters.
Note: You cannot specify a Target Description for labels, because the label description is
one of the label variants and all label variants are duplicated.
This field is only displayed when you duplicate a session.
Script
Field
Target
The format of the name is component specific. Most component names must start with the
Target Description
Program
Select one of the following options:
The UI script of the original session is copied. The new UI script is
linked to the target session.
Select this option if the new session must have its own UI script.
The new session is linked, through a session reference, to the UI
script of the original session, so that both sessions share the same
UI script.
See the description of the Session reference field in the online
help of the Session Editor.
Duplicate Script
Create Reference to
Source Session
Description
DAL options These options are only displayed when you duplicate a DAL script.
The duplicate wizard copies the selected (source) DAL script to a new (target) DAL script.
In addition, the wizard also copies the table, to which the source DAL script belongs, to a
new table. The new DAL script contains references to the original table. Use the following
options to automatically update these references, so the new DAL script refers to the new
table.
If this check box is selected, the wizard automatically replaces
all references to the original table name by references to the
new table name.
If this check box is cleared, the references are not updated, so
the new DAL script still contains references to the original table
name.
Replace description '<de- If this check box is selected, the wizard automatically replaces
all references to the original table description by references to
the new table description.
If this check box is cleared, the references are not updated, so
the new DAL script still contains references to the original table
description.
Field
Replace code '<name of
the original DAL script>'
scription of the original
DAL script>'
3 Duplicate the component
To duplicate the selected component in your local workspace and to exit the wizard, click Finish. The
duplicated component appears in the Activity Explorer view of the Application perspective.
You can now edit the duplicated component through the corresponding editor. For example, you can
edit a duplicated library through the Library Editor.
Some components have dependent child components, such as forms, scripts, libraries or labels. When
you duplicate a component, these child components are copied as well (see remarks in table below).
Remarks
nent
When you duplicate a session, the session's form is also copied. If you select the Duplicate
Script option, the UI script is also copied.
When you duplicate an enumerated domain, the labels used for the enumeration are also
copied.
When you duplicate a label, all label variants are duplicated (including the label description).
Compo-
Session
Domain
Label
## Application Search

Use this dialog to find out in which LN software components an element, selected in the script editor, is used.
The search results are displayed in the Search view. Double-click a search result to open the corresponding
script or library at the line where the result occurs.
> [!NOTE]
- This dialog is only available for LN servers with Enterprise Server 8.7 or higher.
- The component you are searching for must exist. If the specified component does not exist, a message
is displayed.
You can start this dialog from the shortcut menu in the script editor.
## Activity

The activity in which you started the Application Search command.
Expression / Component Name
The expression or component name you are searching for. The element that you selected in the script editor
is automatically filled in.
Search in Scripts
If this option is selected, the expression or component name is searched in the scripts/sources of the
component types specified in the Component Types field.
You can perform the search in these component types:
- Sessions
- Functions
- Tables
- Reports
- Libraries
Search as
The component type you want to search for.
The expression or component name is searched in all parts of the component types specified in the Component
Types field.
Allowed values
Description
The search process searches only for messages.
You can perform the search in these component types:
- Sessions
- Functions
- Tables
- Reports
- Libraries
- Domains
- Report Designs
- BFlow components
- Workbenches
Value
Message
Value
Question
Session
BFlow Component
Table/Field
Library
Description
The search process searches only for questions.
You can perform the search in these component types:
- Sessions
- Functions
- Libraries
- BFlow components
The search process searches only for sessions.
You can perform the search in these component types:
- Sessions
- Functions
- Libraries
- BFlow components
- Menus
The search process searches only for BFlow components.
You can perform the search in BFlow components.
The search process searches for tables or table fields. The type of search depends on the length of the component name you specify in the Expression /
Component Name field:
- If you specify 8 characters or less, the search process searches for tables.
- If you specify more than 8 characters, the search process searches for table
fields.
You can perform the search in these component types:
- Sessions
- Functions
- Tables
- Reports
- Libraries
- BFlow components
The search process searches only for libraries. You can perform the search in
these component types:
- Sessions
- Reports
- Functions
- Libraries
- Report Designs
- Menus
This option is only available if it is supported by the LN server.
Value
Label
Description
The search process searches only for labels. You can perform the search in
these component types:
- Sessions
- Reports
- Functions
- Libraries
- Report Designs
- Workbenches
- Menus
- Domains
This option is only available if it is supported by the LN server.
The search process performs the same search actions as the "Print Where Used" sessions on the LN server.
The search results are displayed in the Search view.
Note: This option is only available for LN servers with Enterprise Server 10.3 or higher.
Component Types
The component types in which the search is performed.
Package Selection
The packages in whose components the search must be performed.
Options
Extended regular expression
If this check box is selected, the search will use the specified regular expression.
A regular expression is a pattern used to match or find specific text in a string. The following special characters
can be used in regular expressions to define patterns for text matching:
Description
The end of the line
Any character
Takes the previous character 0 or more times
Takes the following special character literally
One of the characters between [ ]
Any character except the characters after ^
The previous character exactly m times
Special character
^
.
*
\\
[]
[^]
{m}
Case sensitive
If this check box is selected, the search will distinguish uppercase from lowercase letters.
Include expired components
If this check box is selected, the search process will also search in expired components.
Exclude comment lines
If this check box is selected, the search process will not search in comment lines.
Range
From/To
The range of components in which the search must be performed.
The package code must be omitted. The specified code must start with a module code. For example, you
want to search in components in the com module in the tc package. Select tc in the Package Selection field,
and specify this range:
To
comzzzzzzzzzzzzzzzzz
From
com
## Generate Library from WSDL file

Use this dialog box to generate LN 4GL code for a general library. To generate the library, you must select a
Web Services Description Language (WSDL) file or a URL.
Note: This dialog is only available for LN servers with Enterprise Server 8.7 or higher.
You can start this dialog from the shortcut menu in the script editor, when you edit the source code of a
general library.
Note: For information on how to use the generated LN code, see "Web Services from LN " in the Infor ES
Programmers Guide (Infor Customer Portal KB2924522).
WSDL File
The absolute path name of the WSDL file to be imported.
> [!NOTE]
Click Browse to start a dialog where you can locate and select the WSDL file.
WSDL URL
The URL that is used to generate the library code.
Add library code prefix to function names
If this check box is selected, the code of the library is added as a prefix to the names of all functions that are
imported from the file or URL.
## Field Dependencies

Use this dialog box to specify field dependencies.
Fields without relations are deleted after relations have been found.
Import Relations
Use this check box to enable or disable the import of field relations.
Analyze pre conditions in Function Usage
Table fields might be present in the pre condition part of the DLLUsage / FunctionUsage. If this check box is
selected, those fields are taken into account.
Example 1:
function extern void whina310.qord.update()
{
DllUsage
Expl:   The purpose of this function is to set a default value
for whina310.qord.
Pre:    Fields that are used to set the default are:
- whina310.item
- whina310.oqan
  Post:   whina310.qord could be filled or modified
  Input:  N.A.
  Output: N.A.
  Return: N.A.
  EndDllUsage
Example 2:
function extern void tfcmg204.ctdm.update()
{
DllUsage
Expl:   The purpose of this function is to set a default value
for tfcmg204.ctdm.
Pre:    Fields that are used to set the default are:
- tfcmg204.ctdm(1)    |* dimension 1
- tfcmg204.ctdm(2)    |* dimension 2
- tfcmg204.ctdm(x)    |* all possible dimensions
- tfcmg204.ctdm(*)    |* all possible dimensions
  Post:   whina310.qord could be filled or modified
  Input:  N.A.
  Output: N.A.
  Return: N.A.
  EndDllUsage
Analyze Implemented field hooks
If this check box is selected, the field hooks in the DAL script are analyzed for relations.
Analyze Depth
Allowed values:
- 1 or higher: if it is possible to find relations in sub-functions in other scripts, structured searching is
performed for finding relations.
The depth here is the depth of scripts.
- 0: only the content of the hook itself is taken into account for finding relations.
The default value is 1.
Ignore Arguments of dal.set.message… calls
If this check box is selected, arguments of these functions are not taken into account for finding relations:
- dal.set.message
- dal.set.info.message
- dal.set.error.message
Analyze existing dependencies (field.depends.on statements)
If this check box is selected, the previously defined field dependencies are taken into account. Only new
dependencies are added.
Update DAL Script
This check box determines whether the DAL script should be updated.
## Create Tables

Use this dialog box to create tables for a range of companies and packages. Before you can create tables, you
must define these components:
- A company in the Companies (ttaad1100m000) session
- Database definitions for that company in the Database Definitions (ttaad4510m000) and Tables by
Database (ttaad4111m000) sessions
- Optional: logical table definitions in the Logical Tables (ttaad4120m000) session
See also "To define database information" in the Enterprise Server online help.
Company
The range of company numbers in which the tables are created.
Package
The range of packages for which the tables are created.
Table
The range of table codes of the tables that are created.
## Convert To Runtime

Use this dialog box to convert the changed software components to the runtime data dictionary. The conversion
is performed by a range of package combinations and packages.
Note: The procedure to perform a conversion to runtime depends on how LN is deployed:
- If LN runs in the cloud, follow this procedure: Performing a conversion to runtime - Cloud on page 148
- If LN runs on-premises, follow this procedure: Performing a conversion to runtime - On-premises on page
Domains
If this check box is selected, the domains are converted to the runtime data dictionary.
Tables
If this check box is selected, the tables are converted to the runtime data dictionary.
Reconfigure Tables
If this check box is selected, the tables are reconfigured.
Reconfiguration means that a new table definition is created on the basis of the table and domain definitions
in the data dictionary. The reconfiguration is only performed if the definitions have been changed in the
development environment.
The reconfiguration of the tables is only possible if tables or domains have been created in the runtime data
dictionary.
Package Combination
The package combinations whose data is to be converted to the runtime data dictionary.
Package
The packages for which the tables and domains must be converted to the runtime data dictionary.
Table
The changed tables that must be converted to the data dictionary.
Runtime Directories
If this check box is selected, the file definition fd6.2 file of the defined package combination is dumped to
the runtime data dictionary. The runtime directories are located in the file definition and contain the runtime
objects.
Note: During this action the user files of the LN user are also dumped to the runtime data dictionary of the
defined package combination.
Performing a conversion to runtime - Cloud
1 Before you convert domains or tables, or reconfigure tables, ensure the environment is in Admin only
mode.
See the online help of the Manage Operational Status (ttmtm3501m000) session.
2 Perform the conversion.
a Start the Convert To Runtime dialog box.
b Specify the appropriate ranges and indicate which components must be converted.
> [!NOTE]
- If the Tables check box is selected, only the table definitions are created, not the tables
themselves. To create the tables, use the Create Tables dialog box.
- If the Reconfigure Tables check box is selected, the system reconfigures all changed tables.
The range of tables is not taken into account. Tables are reconfigured for the companies linked
to the specified range of package combinations.
c Click Convert to Runtime.
If the conversion is successful, you must bring the system online. See the next step.
If the reconfiguration of the tables is not successful, for example because of lock errors, this question
is displayed: Error during file configuration; try again?. In that situation, complete these steps
to resolve the problem:
1 To stop the process, click No in the message box.
2 Ensure that everybody has signed out from LN.
3 Start the Application Locks (ttadv9598m000) session and remove the application locks that
start with "ttadv502" and contain the code of your package combination.
4 Restart the Convert To Runtime dialog box and restart the reconfiguration of the tables.
5 If the process completes successfully, you must bring the system online. See the next step.
3 After the conversion of domains or tables and the reconfiguration of tables is completed successfully,
you can bring the environment online again.
See the online help of the Manage Operational Status (ttmtm3501m000) session.
Performing a conversion to runtime - On-premises
1 To avoid problems with locked tables, ensure that all users have signed out from LN before the conversion
starts.
2 Perform the conversion.
a Start the Convert To Runtime dialog box.
b Specify the appropriate ranges and indicate which components must be converted.
> [!NOTE]
- If the Tables check box is selected, only the table definitions are created, not the tables
themselves. To create the tables, use the Create Tables dialog box.
- If the Reconfigure Tables check box is selected, the system reconfigures all changed tables.
The range of tables is not taken into account. Tables are reconfigured for the companies linked
to the specified range of package combinations.
c Click Convert to Runtime.
The output of the reconfiguring process is logged in the $BSE/log/log.reconfig file.
If the reconfiguration of the tables is not successful, for example because of lock errors, this question
is displayed: Error during file configuration; try again?. In that situation, complete these steps
to resolve the problem:
1 To stop the process, click No in the message box.
2 Ensure that everybody has signed out from LN.
3 Start the Application Locks (ttadv9598m000) session and remove the application locks that
start with "ttadv502" and contain the code of your package combination.
4 Restart the Convert To Runtime dialog box and restart the reconfiguration of the tables.
5 After the conversion has been finished, ensure that all users restart their bshells. This is to avoid
errors within those bshells.
