# Chapter 12: Infor LN Project Server

> Summary treatment for this release: orientation-level coverage. The full cleaned source text is preserved below; consult the source guide for exhaustive detail.

Infor LN Project Server is used to maintain Software Projects and Activities for Software Engineers that develop
software in LN Studio.
Project Server functionality is available in the Project Server perspective in LN Studio.
Note: A number of screenshots in the documentation may be based on previous application releases. They
can differ slightly from your application screens. However, the described functionality is similar.
## Procedures

## Defining a software project

This topic describes how to define software projects and activities. The projects and activities are stored in
Project Server.
To define a software project:
1 Start LN Studio
2 Open the Software Project Explorer view
On the Windows menu, select Open Perspective, and then click Project Server.
The Software Project Explorer view is displayed in the Eclipse workbench.
3 Specify the project data
Complete these steps:
a On the view's toolbar, or on the shortcut menu, select New Software Project. The Create a Software
Project dialog box is displayed.
b Specify the project properties. See the online help of the dialog box.
c Save the project and close the dialog box.
4 Add one or more activities to the new project
Complete these steps:
a In the Software Project Explorer view, right-click the new project and select New Activity. The
Create a new Activity dialog box is displayed.
b Specify the activity properties. See the online help of the dialog box.
c Save the activity and close the dialog box.
The users, to which the activities are assigned, can now start developing software in the new project. They
can select the assigned activities in the Application perspective in the LN Studio workbench.
## Delivering software components

This topic describes how to deliver the components after you end a development activity.
After you end a development activity, you can distribute the corresponding components through PMC.
If the Integration With PMC
- Generate and deliver a solution in one go. This is the fastest way to deliver components. check box is
selected in the properties of the project to which the activity belongs, use one of these procedures to
deliver the components.
- Manually create and deliver a solution. This procedure contains more manual actions, and therefore
offers more flexibility.
If the Integration With PMC check box is not selected, manually create and release a solution though the
PMC sessions on the LN server.
Note: The following procedures describe how to release a PMC solution from Infor LN Project Server. Only
the steps to perform the procedure are described. No background information on PMC is included. For details
on the PMC terminology and PMC-specific actions, such as Generate Dependencies, Export Solution, and
Release Solution, see the  Infor LN Development Tools Development Guide.
Manually creating and delivering a solution
1 Choose to perform a manual delivery.
If you end an activity that belongs to a project for which the integration with PMC is enabled, this question
is displayed.
check boxDo you want to deliver this Activity and create a Solution?
To perform a manual delivery, click No.
2 Create a delivery activity.
Complete these steps:
a In the Software Project Explorer view, click New Activity. The Create a new Activity dialog is
displayed.
b Create an activity of type "Delivery". See the online help of the dialog.
c Save the activity and close the dialog.
3 Place the delivery activity in the delivery explorer.
In the Software Project Explorer view, select the delivery activity and drag it to the Delivery Explorer.
Alternatively, use the Open a Delivery Activity command in the Delivery Explorer.
4 Add software development activities to the delivery activity.
Add the software development activities, whose components you want to deliver, to the delivery activity.
To do this, drag these activities to the Delivery Explorer and drop them on the delivery activity.
Alternatively, use the Add Development Activity command in the shortcut menu in the Delivery Explorer.
5 Add a solution.
In the Delivery Explorer, right-click the delivery activity and, on the shortcut menu, select Create Solution.
The Create a Solution wizard starts. Specify a code and description for the solution and click Finish. The
Solution Editor starts.
6 Edit the solution.
Use the Solution Editor to modify the solution.
For example, you can perform these actions:
- Add components to the solution.
- Add installation instructions.
- Define additional dependencies.
See Solution Editor on page 351.
When finished, save the changes and close the editor.
7 Generate dependencies.
To regenerate dependencies after you added or deleted components to/from the solution:
a In the Delivery Explorer, right-click the solution.
b On the shortcut menu, select Generate Dependencies.
The solution status changes to "Dependencies defined".
8 Export the solution.
In the Delivery Explorer, right-click the solution and, on the shortcut menu, select Export Solution.
The solution status changes to "Exported".
9 Release the solution.
In the Delivery Explorer, right-click the solution and, on the shortcut menu, select Release Solution.
The solution status changes to "Released".
You are prompted to finalize the delivery activity and remove the activity from the Delivery Explorer.
10 Finalize the delivery.
In the question window, click Yes. The delivery activity disappears from the Delivery Explorer and its
status is set to "Finalized".
This step does not change anything to the solution.
Note: If you click No, you must complete these steps to manually finalize the delivery activity:
a In the Delivery Explorer, right-click the delivery activity.
b Select Finalize Delivery.
Generating and delivering a solution in one go
1 Choose to generate and deliver a solution in one go.
If you end an activity that belongs to a project for which the integration with PMC is enabled, the following
question is displayed.
Do you want to deliver this Activity and create a Solution?
To generate and deliver a solution in one go, click Yes. The Create a Solution wizard starts.
2 Create and release a solution.
In the Create a Solution wizard:
a Specify the name and description of the delivery activity to be generated, or accept the defaults.
b Specify the code and description of the solution to be generated, or accept the defaults.
c Select Export and release solution without editing.
d Click Finish.
The wizard performs these actions:
- Generates a delivery activity.
- Generates a solution.
- Exports the solution.
- Releases the solution.
- Finalizes the delivery activity.
Note: If you want to edit the solution before the release, select Edit solution before export and release
instead of Export and release solution without editing. When you click Finish, the Solution Editor
starts. In this editor you can, among other things, add components to the solution and define
dependencies. See the editor's online help. After you have edited the solution, you must manually perform
these actions:
- Generate Dependencies.
- Export the solution.
- Release the solution.
- Finalize the delivery activity.
## Dialogs

## Create a Software Project

Use this dialog box to create a Software Project.
Project
Project name
The project name.
Description
The project description.
Requirement ID
The ID of the business requirement to which the project belongs (requirements are usually stored in a
requirement management or defect tracking system).
Partial End Allowed
If this check box is selected, you can partially end the activities linked to the project. When you end an activity,
you can select the components for which the activity is ended. These components are checked in to the
project VRC, while the other components stay available in the activity VRC.
See Developing software components on page 53.
If this check box is cleared, you can only end activities in their entirety.
Sharing Activities Allowed
If this check box is selected, each activity linked to the project can be assigned to multiple users.
If this check box is cleared, each activity can be assigned to only one user.
> [!NOTE]
When you open a shared activity, the components developed by other users are not displayed automatically.
To display these components, recover the activity. See the online help of the Recover activity dialog.
If sharing activities is used in combination with activity context, all assignees of an activity must use the same
context. Otherwise, the assignees will get different results when they recover an activity, or when they launch
or debug a session.
Integration With PMC
If this check box is selected, you can create delivery activities in the project, and deliver components from
Project Server. When you end a development activity, you are prompted to deliver the activity and create a
PMC solution.
See Delivering software components on page 340.
If this check box is cleared, the PMC integration is disabled. You cannot deliver the components from Project
Server. You can perform the PMC delivery from the LN server instead.
Repository
Development Environment
The LN environment in which the software for the project is developed. Select the environment from a
drop-down list.
Application
The application to which the project belongs. Select the application from a drop-down list.
Documentation
Use this field to enter additional documentation about the project.
## Create a new Activity

Use this dialog box to create an activity.
Project
Project name
The software project to which the activity belongs. Select a project from the drop-down list.
Description
The description of the selected project.
Activity
Name
Specify an activity name.
Description
Specify an activity description.
Type
Select an activity type from the drop-down list.
If the activity is intended for software development, select one of the following types:
- Enhancement
- Change request
- Miscellaneous
- Defect (intern)
- Defect (extern)
If the activity is intended for software delivery through PMC, select the "Delivery" type.
Note: You can only select the "Delivery" type if the Integration With PMC check box is selected in the
properties of the project to which the activity belongs.
Requirement ID
The ID of the business requirement to which the activity belongs (requirements are usually stored in a
requirement management or defect tracking system).
Owner
The software engineer who owns the activity. Select a software engineer from the drop-down list.
The owner can open the activity, develop components in the activity, reassign the activity, and end the
activity.
Assignees
Assignee
The software engineers to which the activity is assigned. The assignees can open the activity and develop
components in the activity. However, only the owner can end the activity.
To add an assignee, click Add and select a software engineer from the drop-down list.
The Assignees grid is only available if the Sharing Activities Allowed check box in the software project's
properties is selected.
If sharing activities is not allowed, the Add button is disabled, and the system automatically adds the owner
of the activity as assignee. This change is displayed only after you re-open the dialog box.
Documentation
Specify documentation about the activity.
Finish
Saves the new activity and closes the dialog box.
Finish and Open
Saves the new activity and closes the dialog box. Automatically switches to the Application perspective and
opens the new activity in the Activity Explorer view.
## Compile activity overview

This dialog box shows an overview of the components that were compiled, for example when you closed an
activity.
## Open a Delivery Activity

Use this wizard to open a delivery activity.
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
For details on the other fields, see Create a Software Project on page 342.
Select Activity
Use this page to select the activity you want to open.
All fields, except Activity name, are read-only.
Activity name
The activity you want to open.
You can select the activity name from a drop-down list.
All other fields
For details on the other fields, see Create a new Activity on page 343.
## Create a Solution

Use this wizard to create and deliver a new PMC solution.
Project
Name
The software project to which the solution belongs.
Description
The project description.
Delivery Activity
Name
The name of the delivery Activity to which the solution belongs.
The wizard generates this activity and links it to your development activity.
Description
The activity description.
Solution
Name
The name of the solution to be generated.
Description
The description of the solution.
Edit or Release Solution
Edit solution before export and release
If this option is selected, you can edit the solution before it is exported and released. When you click Finish,
the Solution Editor starts.
After you have edited the solution, you must manually perform these actions:
- Generate Dependencies (if you defined dependencies).
- Export the solution.
- Release the Solution.
- Finalize the delivery activity.
See Delivering software components on page 340.
Export and release solution without editing
If this option is selected, you cannot edit the solution before it is exported and released.
When you click Finish, the wizard automatically performs these actions:
- Exports the solution.
- Releases the Solution.
- Finalizes the delivery activity.
## Add development activity

Use this dialog to add an existing development activity to a delivery activity.
You can start this dialog from the Delivery Explorer.
To add an existing development activity to a delivery activity:
1 In the Name field, select a development activity from the list.
2 Press Finish.
The development activity is displayed, under the delivery activity, in the Delivery Explorer.
Project
Project name
The software project to which the delivery activity belongs.
Description
The description of the selected project.
Delivery Activity
Name
The delivery activity to which the development activity is added.
Description
The description of the delivery activity.
Development Activity
Name
The name of the development activity. Select a development activity from the drop-down list.
## Browse Solutions

You can start this dialog box from the Solution Editor.
Use the dialog box to link another solution to the solution you are editing.
The dialog box consists of two tabs, that you can use to search in two different ways:
- Select on code
- Search on description
Select on code
Use this tab to search on the first part of the solution code.
Linking a solution to the solution you are editing
Complete these steps:
1 Optionally: In the upper right part of the tab, click the drop-down menu button. The Browse Solution
Types dialog box starts. In this dialog box you can specify additional settings for the search process.
2 In the Solution Code field, enter the first part of the solution code.
3 Click the ellipsis button, or press CTRL+SPACE. A list of solutions, which match the pattern, is displayed.
4 Select the desired solution and click OK.
Sorting search results
- To sort the search results by code or description, click the corresponding column header.
- To toggle between ascending and descending sort mode, click the involved column header.
Fields
Solution Code
Specify the (first part of the) solution code you are searching for.
To display a list of solutions, which match the pattern, click the ellipsis button, or press CTRL+SPACE.
Code
The solution code.
Description
The description of the solution.
Search on description
Use this tab to search on a part of the solution's description.
To link a solution to the solution you are editing:
1 Optionally: In the upper right part of the tab, click the drop-down menu button. The Browse Solution
Types dialog box starts. In this dialog box you can specify additional settings for the search process.
2 In the Description field, enter the search pattern.
3 Click the ellipsis button. A list of solutions that match the search pattern is displayed.
4 Select the desired solution and click OK.
Fields
Description
Specify the search pattern.
To display a list of solutions, which match the pattern, click the ellipsis button.
Name
The solution code
Description
The description of the solution.
## Browse Solution Types

Use this dialog to specify additional settings for the search process that you want to start in the Browse
Solutions dialog.
Max number of solutions
Specify a maximum number of solutions to be displayed per search.
Reset Defaults
Restores the default settings for this dialog.
## Select Component(s) for delivery

Use this dialog box to link components to a solution.
You can start the dialog box from the Solution Editor.
The dialog box consists of two tabs, that you can use to search in two different ways:
- Select on code
- Search on description
Select on code
Use this tab to search on the first part of the component code.
To add a component to the solution you are editing:
1 Optionally: In the upper right part of the tab, click the drop-down menu button. A dialog box, where you
can specify additional settings for the search process, starts.
2 In the Component Code field, specify the first part of the component code. For example: tdsls0.
3 Click the ellipsis button, or press CTRL+SPACE. A list of components, which match the pattern, is displayed.
If you type additional characters, The dialog box automatically updates this list.
4 Select the desired component and click OK.
To sort search results:
- To sort the search results by type, name, or description, click the corresponding column header.
- To toggle between ascending and descending sort mode, click the involved column header.
Note: As you type the package code and the module code (the first five characters of the component code),
The dialog box automatically shows a list of matching packages and modules, and updates this list after each
character typed. For example:
Component
Code
t
td
tdr
Search results displayed
All packages starting with t.
Package td and all its modules.
All modules of package td that start with r. For example, tdrec and tdrpl.
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
Search on description
Use this tab to search on a part of the component's description.
To add a component to the selected activity:
1 Optionally: In the upper right part of the tab, click the drop-down menu button. A dialog box, where you
can specify additional settings for the search process, starts.
2 In the Package field, select a package from the list.
3 Specify the search pattern, and click the binoculars button. A list of components that match the search
pattern is displayed.
4 Select the desired component and click OK.
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
### Project Server View Filter

Use this dialog box to specify filter criteria for the Software Project Explorer view. To apply the filter, click
OK. The filter criteria are stored. The next time you open the view, the filter is applied automatically.
Show Projects with status
Select one or more project statuses. The view only shows projects that have one of these statuses.
Show empty projects
Use this field to easily recognize empty projects in the view.
If this check box is cleared, a + sign is displayed before all projects in the view.
If this check box is selected, the + sign is not displayed before empty projects.
Show Activities with status
Select one or more activity statuses. The view only shows activities that have one of these statuses.
Show Activities of all users
If this check box is selected, the view shows activities of all users. If this check box is cleared, the view only
shows your own activities.
Name starts with
If you select the check box, you can specify one or more characters. The view shows activities whose names
start with the specified characters.
Note: The filter is case sensitive.
## Multipage Editors

## Solution Editor

Introduction
Use this editor to define and edit PMC solutions.
In PMC, a solution is the smallest, indivisible type of update. A solution is identified both at the distributor
and recipient side by a unique solution code. The term individual solution is also frequently used and has the
same meaning.
Overview
Use this page to perform these actions:
- Maintain the basic data of a solution.
- Specify pre- and post-installation instructions.
- Link additional components to the solution.
- Define dependencies between the current solution and other solutions.
General Information
Name
A unique identification of the solution in a Base VRC.
The solution code has these characteristics:
- Datatype: alpha-numerical string.
- Maximum length: 14 characters.
- Forbidden characters: All characters that have a special meaning in UNIX, such as $, *, and so on. If you
enter a forbidden character, the code will not be accepted.
Description
The description of the solution.
Base VRC
Base VRC
Status
Solution status distributor
Published
If this check box is selected, the solution is published immediately upon release. If a solution is published,
the solution is copied to the directory specified in the Path for Published Solutions field in the Parameters
(ttpmc0100s000) session.
Note: If the Copy Published Solutions check box in the Parameters (ttpmc0100s000) session is cleared,
the solution cannot be published, regardless of the selection of the current check box.
Installation Instructions
Pre
The pre-installation instructions. The instructions are added to the solution text.
For example: Before you install this solution, ensure there are no open integration transactions.
Post
The post-installation instructions. The instructions are added to the solution text.
For example: After you install this solution, generate MRP orders again.
Components
Components
Use the grid to link components to the solution.
Add / remove components
- To add a component, click Add and fill out the fields in the grid.
- To remove a component, right-click a component and, on the shortcut menu, select Remove.
Type
The type of software component, such as session, message, or label.
Name
The component identification, such as a session code.
To add a component:
1 Press CTRL+SPACE. The Select Component(s) for delivery dialog box is displayed. The dialog box only
shows components of the selected type.
2 Select one or more components and close the dialog box. See the dialog box's online help.
Dependencies
Dependencies
Use the grids to define dependencies between the current solution and other solutions.
If not all dependencies that would be generated are present, you receive a warning during the export of the
solution or patch.
After you define all the dependencies, you can change the solution status to Dependencies defined and the
solution is ready to be exported. You can change the status in the Delivery Explorer.
If the status of the solution was Exported, and you change the dependencies, then the solution status is reset
to Dependencies defined.
Add / remove dependencies
- Use the upper grid, to enter dependencies of type Co-requisite and Pre-requisite.
- Use the lower grid to indicate the solution is a Post-requisite of another solution.
- To add a dependency, click the relevant Add button and fill out the fields in the grid.
- To remove a dependency, right-click a dependency and, on the shortcut menu, select Remove.
Type
The type of dependency: Co-requisite or Pre-requisite.
Related VRC
The Base VRC of the solution or Patch to which the current solution or patch is related.
The related VRC can be a different base VRC if the dependency type is Co-requisite or a Pre-requisite from a
Feature Pack to the previous Feature Pack.
Solution
The solution or Patch with which a Dependency relation exists.
To add a solution:
1 Press CTRL+SPACE. The Browse Solutions dialog box is displayed.
2 Select a solution and close the dialog box. See the dialog box's online help.
Description
The solution description.
Manual
If this check box is selected, the dependency was not generated, but defined manually.
This solution is post-requisite of:
Related VRC
The Base VRC of the solution or Patch to which the current solution or patch is related.
Solution
The solution or Patch with which a Dependency relation exists.
To add a solution:
1 Press CTRL+SPACE. The Browse Solutions dialog box is displayed.
2 Select a solution and close the dialog box. See the dialog box's online help.
Description
The solution description.
History
Use this page to display the status changes to a solution for a Base VRC.
Every status change of a solution or patch status is recorded. This page shows all these recorded changes. If
you delete a solution, this fact is recorded with the new status as blank.
The page shows the maintenance history for the relevant solution or patch up until the specified time.
Maintenance History
Date
The date on which the status of the solution was changed.
Time
The time when the status of the solution was changed.
Serial
Number to make the key unique.
User
The name of the user who changed the solution.
Status
The new status of the solution.
## Perspectives

## Project Server perspective

The Project Server perspective provides functionality for project managers and administrators.
This table shows the views in the perspective:
Software Project Explorer Project managers use this view to maintain software projects and activities
on the Project Server.
For details on the procedure to define projects and activities, see Defining a
software project on page 339.
Application Explorer view Administrators use this view to create and maintain the applications for
which the software projects are defined.
For more information on the administrator's tasks, see the  Infor LN Studio
Administration Guide.
view
## Views

## Software Project Explorer view

The Software Project Explorer view provides a hierarchical view of the projects, activities, and modified
software components in the Project Server. See the following figure for an example.
This table describes the different nodes in the previous figure:
Nr. in figure
Description
Project
Development Activity
Modified LN software component
Nr. in figure
Description
Delivery Activity
Toolbar
The toolbar of the Software Project Explorer view contains the following buttons:
Properties
New Software Project
New Activity
Compile closed activity at development system
Shows the properties of the selected project or activity.
For details on the project and activity properties, see the description
of the Create a Software Project and Create a new Activity dialog
boxes.
Adds a project on the project server.
Adds a new activity to the selected project.
Compiles the software components in the selected closed activity.
Use this command if the automatic compilation during the ending of
the activity has failed, and the problem that caused the compilation
error is solved.
Example:
- Activity B is part of the context of activity A. A UI script in activity
A calls a DLL that belongs to activity B. The DLL is not compiled
yet.
- Activity A is ended by its owner. The compilation of the UI script
fails, because the DLL in activity B is not compiled. Activity A is
closed anyway.
- Activity B is ended by its owner. The DLL is compiled automatically
and the activity is closed.
- The owner of activity A can now use the Compile closed activity
at development system option to compile the UI script in the
closed activity A.
Delete selected item
Menu
Deletes the selected project or activity.
> [!NOTE]
- You cannot delete a project, if the project status is Created or Act
ive.
- This option does not undo the software modifications performed
within the project or activity that are already checked in.
Contains these menu items:
- New Software Project
- New Activity
- Compile closed activity
- Filters
This command starts a dialog box where you can specify filter
criteria for the Software Project Explorer view.
See Project Server View Filter on page 351.
Note: The remaining buttons are standard Eclipse commands. For details on these buttons, see "User interface
information" in the Workbench User Guide.
Shortcut menu
To open the shortcut menu, right-click on a resource in the view.
This menu contains most of the toolbar commands.
Icons
The following icons are displayed in the Software Project Explorer view:
## Delivery Explorer view

The Delivery Explorer view provides a hierarchical view of the delivery activities, and the corresponding
development activities and solutions.
This figure shows an example:
This table describes the different nodes in the previous figure:
Nr. in figure
Description
Delivery Activity
Development Activity
Solution
Toolbar
The toolbar of the Delivery Explorer view contains these buttons:
## Open a Delivery Activity

Compile Delivery Activity at development system
Delete
Menu
Starts the Open a Delivery Activity wizard, where you can select
an activity that is assigned to you.
Compiles the software components in the selected delivery activity.
Deletes the selected item.
Contains the Open a Delivery Activity command.
Note: The remaining buttons are standard Eclipse commands. For details on these buttons, see "User interface
information" in the Workbench User Guide.
Shortcut menu
To open the shortcut menu, right-click a resource in the view.
This menu provides the following Project Server-specific commands:
Add Development Activ- Starts the Add development activity dialog, where you can link a development
activity to the selected delivery activity.
Compile Delivery Activi- Compiles the software components in the selected delivery activity.
ty
Starts the Create a Solution dialog, where you can create a PMC solution.
Generate Dependencies Generates the dependencies defined in the selected solution.
For details on the PMC terminology and PMC specific actions, such as Generate
Dependencies, Export Solution, and Release Solution, see the Infor LN Development Tools Development Guide.
Exports the solution.
Releases the solution.
Sets the status of the selected delivery activity to Finalized. The delivery activity disappears from the Delivery Explorer.
ity
Create Solution
Export Solution
Release Solution
Finalize Delivery
Icons
These icons are displayed in the Delivery Explorer view:
