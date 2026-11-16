# Chapter 11: Views

> Summary treatment for this release: orientation-level coverage. The full cleaned source text is preserved below; consult the source guide for exhaustive detail.

## Activity Explorer view

The Activity Explorer view provides a hierarchical view of the activities you have opened, and the software
components linked to these activities.
You can use the Activity Explorer to perform these tasks:
- Open, close and view an activity.
- Check in, (un)checkout a software component (if Configuration Management is applicable).
- Open a component in the corresponding editor.
The Activity Explorer is part of the Application perspective.
This figure shows the Activity Explorer view:
Double-click a software component to open the component in the corresponding editor.
You can add other software components to your activity through the Component Explorer, and through the
Select a Software Component command in the LN Studio toolbar.
This table describes the different nodes in the previous figure:
Nr. in figure
Description
Name of an open activity, with the Project Name between square brackets.
LN package code, displayed in ascending order (for example: td, tf, tp).
Nr. in figure
Description
Main Component Type, displayed in ascending order. For example: domain, report, session,
or table.
LN module code, displayed in ascending order.
The module code is displayed for all component types, except domains, labels, messages,
and questions.
LN software component, with the component description between brackets, displayed in
ascending order.
To open a software component in the corresponding editor, double-click the component.
### Toolbar

The toolbar of the Activity Explorer view includes these buttons:
Toggles whether the Activity ExplorerActivity Explorer selection to the resource
being edited. selection is linked to the active editor. When this option is selected,
changing the active editor will automatically update the
Open an LN Studio Starts the Open an Activity wizard, where you can select an activity that is assigned
to you.
See Developing software components on page 53.
If this option is selected, the multipage editor directly opens the Source selection is
linked to tab (if the source code is available) when you open a component.
If this option is not selected, the editor opens the Overview tab.
See Multipage Editors on page 150.
Removes unchanged components from your activity. The command only removes
files that are not checked out, created, or modified.
See Cleaning an activity on page 49.
This command is useful when your activity contains a lot of unchanged components,
such as when you have frequently used the Open Declaration command.
Link with Editor
Activity
Directly open the
Source Tab
Clean Activity
Recover Activity
Menu
Restores the components in your activity from the Configuration Management System
on the server to your local workspace. Optionally, unchanged components are removed from the workspace.
See Recovering an activity on page 50.
Provides, among other things, menu items that allow you to do the following:
- Open, deselect and change working sets. See "Working sets" in the Workbench
User Guide.
- Sort the items in the view by full name, or by type/extension.
- Apply a filter.
- Toggle whether the view selection is linked to the active editor.
- Show Checked Out/Modified components only. This option is useful if your
workspace contains a lot of components not checked out, such as when you
have frequently used the Open Declaration command.
See the Workbench User Guide.
Note: The remaining buttons are standard Eclipse commands. For details on these buttons, see "User interface
information" in the Workbench User Guide.
### Shortcut menu

To open the shortcut menu, right-click a resource in the view.
This menu provides, among other things, the following commands:
New
Open
Open With
Copy
Allows you to open a new activity in the root node, or to create a new component in
the current activity.
To open an activity, on the submenu, select Infor LN Studio Application Project (Open
Activity). The Open an Activity wizard starts.
When you open an activity, the following occurs:
- The activity is automatically placed under the control of configuration management.
- The content of the associated development repository is displayed in the Component Explorer. This view is refreshed and a (closed) tree with the LN packages is
displayed for the Application linked to the software project to which the activity
belongs.
To create a new component, on the submenu, select Infor LN Component. The Create
a New Infor LN Software Component wizard starts.
Opens the selected software component in the LN Studio in the corresponding multipage editor.
You can use this command to open the selected software component in an editor
other than the component's default editor. Select the desired editor from the submenu.
Copies the selected resource to the clipboard.
Pastes resources on the clipboard into the selected project or folder. The resource is
not added to the Revision Control System. If a resource is selected, the resources on
the clipboard are pasted as siblings of the selected resource.
Deletes the selected resource from the workspace.
Note: This command can only delete components that are not checked out, created,
or modified in the current activity. These components have a  decorator in the bottom
right corner of the software component image.
Moves the selected resource to another location. A dialog is displayed, requesting the
location to which the resource must be moved.
Allows you to specify a new name for the selected resource.
Opens the import wizard and allows you to select resources to import into the Workbench.
Opens the export wizard and allows you to export resources to an external location.
Refreshes the Workbench's view of the selected resource and its children. For example,
when you create a new file for an existing project outside the Workbench and want
the file to appear in the Activity Explorer view.
Duplicate Compo- Starts the Duplicate an Infor LN Software Component wizard, where you can duplicate
the selected component.
Performs quality control on the selected software component(s). The command executes various checks based on the Infor LN design principles.
When you verify software components, a list of warnings is generated. You can decide
to accept each warning, or to solve the problem.
See Verifying software components on page 56.
Link Run Configu- Starts a dialog where you can link existing run configurations to the selected activity.
rations
This command is only displayed if you select an activity.
This menu contains these commands:
- Infor LN Session Alt+Shift+X, L
Starts the selected session and automatically generates a run configuration for
the session.
This option is only displayed if you right-click a session in the view.
- BFlow Test
See Running BFlow tests on page 72.
- Run Configurations
Starts the Configurations dialog. Use this dialog to create or modify run configurations.
See Running LN sessions on page 60.
Paste
Delete
Move
Rename
Import
Export
Refresh
nent
Verify Component
See Linking run configurations to an activity on page 51.
Run As
Debug As
Team
Compare With
Replace With
Restore from Local History
Properties
Refactor
This menu contains these commands:
- Infor LN Session Alt+Shift+D, L
Starts the selected session in debug mode and automatically generates a run
configuration for the session.
This option is only displayed if you right-click a session in the view.
- Debug Configurations
Starts the Configurations dialog. Use this dialog to create or modify run configurations.
See Debugging LN sessions on page 62.
This menu provides various Configuration Management functions.
See "The Team submenu".
Provides a mechanism to compare the selected software component with other versions
of that component in the workspaces’ local history.
Provides a mechanism to replace the selected software component with other versions
of that component in the workspaces’ local history.
Restores deleted Workbench resources with a state from the local history. See
"Restoring deleted resources from local history" in the Workbench User Guide.
Starts the property page of the selected item.
If you select an InContext Table Model, the Dependent InContext Models command
is available.
This command starts the Dependent InContext Models view. You can use that view
to refactor the table model's dependent models.
Related topics:
- Dependent InContext Models view on page 316
- InContext Modeling on page 73
- Infor Enterprise Server InContext Modeling Development Guide
- Table InContext Model Editor on page 262
> [!NOTE]
- Some commands in the shortcut menu, such as Checkout and Run as, are also available as buttons in
the toolbar in the Application perspective.
See Application perspective on page 296.
- The previous list does not describe all commands in the shortcut menu. The remaining commands are
standard Eclipse commands. For details on these commands, see "User interface information" in the
Workbench User Guide.
The Team submenu
The Team submenu provides various Configuration Management functions.
If you select an activity, these commands are available:
- Reassign Activity
Starts the Reassign Activity dialog, where you can assign the activity to another user.
- Cancel Activity
Use this command to undo all changes in an activity.
- End Activity
Closes the activity and releases the changed components to the Project VRC.
In the Preferences - Infor LN Configuration Management dialog, you can set the default behavior for
this command.
If you select a software component, these commands are available:
- Recover
Restores the selected component, which was saved on the LN server, to your local workspace.
See Recovering an activity on page 50.
- Checkout
You must lock (check out) a component before it can be changed. When a check out is performed, the
latest version of the software component is retrieved from the development repository. It is then made
editable in the workspace.
Note: This option is not available for components already checked out.
- Checkin
Use this command when you finished editing a component, to unlock a component and store the changes
in the development repository.
1 You are prompted to save any outstanding changes in the component.
Note: If you cancel the “modified source” dialog, the check in is canceled.
2 Then, you are asked to specify a revision text: The updated version of the component is sent to the
development repository and the component is made read-only in the workspace.
Note: This option is unavailable for components not checked out.
- Uncheckout
Use this command when you have finished editing the component, and you do not want to send the
changes to the development repository.
1 The component is unlocked (and changes are discarded).
2 You are prompted to confirm the command: If the command is confirmed, then the current local
representation of the software component is replaced by the latest remote representation.
> [!NOTE]
- If you check out a component for the first time and then perform an uncheckout, the component is
considered as unchanged. The component has a  decorator in the bottom right corner of the
software component image.
- You cannot perform an uncheckout in the following situations:
- If SCM is disabled.
- If the component does not support SCM, for example if the component is a label, message,
question, domain, or additional file.
You must perform a checkin because the changes cannot be rolled back.
- Compare
Starts the Compare Package VRC's (ttadv6450m000) session. The session prints the differences between
the latest version and the previous version of the component.
The differences can be printed in detail, if required.
See the session help.
- Show Revisions
Starts the History view. This view shows all revisions of the selected component, which are present in
the derivation path of your Activity VRC.
See History view on page 320.
- Expire
Performs a check out of the component, sets the Expired flag, and performs a check in. A  decorator is
displayed over the component image.
Note: A session can only be expired if there is no reference to it from another not-expired session.
See Session Editor on page 203.
- Unexpire
Performs a check out of the component, unsets the Expired flag, and performs a check in. The  decorator
disappears.
Note: A session cannot be unexpired if it has a session reference to an expired session.
See Session Editor on page 203.
- Delete
Removes the selected component.
Note: This command can only delete components that are created or modified in the current activity.
These components have a  decorator in the bottom right corner of the software component image.
See Activity based development on page 37.
### Icons and decorators

### Icons

The following icons are displayed in the Activity Explorer view:
Decorators
CM decorators
The following decorators are used to show Configuration Management related status information, which is
mutually exclusive. The decorators are displayed in the bottom right corner of the software component image.
Compiler decorators
The following decorators are used to indicate errors and warnings. The decorators are displayed in the bottom
left corner of the images of the involved nodes.
The decorators are displayed for the involved software component and for all parent nodes.
For example, if a library contains invalid code, error decorators are displayed for the library itself, and also
for the module, the main component type, the package, and the activity to which the library belongs. See the
following figure:
VSC decorators
The following decorators are used to indicate the VSC status of a software component. The decorators are
displayed in the upper right corner of the software component image.
For details on VSC, see Verifying software components on page 56.
"Expired" decorator
The following decorator is used to indicate a software component is expired. The decorator is displayed over
the software component image.
## Breakpoints view

The Breakpoints view shows a list of all available breakpoints and their state (enabled, disabled, resolved,
and invalidated).
In this view, you can perform these actions:
- Double-click a breakpoint, or use the Go to File command, to display its location in the Script Editor.
- Enable or disable breakpoints.
- View or modify the properties of a breakpoint.
- Delete breakpoints.
Note: You cannot add new breakpoints in this view. New breakpoints are added via the Script Editor and via
the Outline view.
For information on adding breakpoints, see Using breakpoints on page 68.
### Toolbar

The toolbar of the Breakpoints view contains these buttons:
Show Breakpoints Supported When you use multiple programming languages within the Eclipse workbench such as Infor 4GL and Java, you can define different types of
breakpoints per language.
If this option is toggled on, only breakpoints applicable to the selected
debug target are displayed, such as the following:
- You debug an LN session, only the LN specific breakpoints are displayed.
- You debug a Java program, only the Java specific breakpoints are
displayed.
Displays the source code and the line associated with the selected breakpoint in the Editor area. Double-clicking a breakpoint has the same effect.
Disables all breakpoints.
When this option is toggled on, the breakpoints hit by the debugger are
automatically highlighted in the Breakpoints view.
by Selected Target
Go to File for Breakpoint
Skip All Breakpoints
Link with Debug View
Add Java Exception Breakpoint
Starts the Add Java Exception Breakpoint dialog box. See the online help
of the dialog box.
### Shortcut menu

Right-click on any breakpoint in the view to open a shortcut menu. The menu contains these commands:
- Go to File
- Enable
- Disable
- Remove
- Remove All
- Select All Ctrl + A
- Copy Ctrl + Insert
- Paste Shift+Insert
- Export Breakpoints
- Import Breakpoints
- Properties
Use the shortcut menu to enable and disable breakpoints. Alternatively, select or clear the check boxes
displayed in front of the breakpoints.
When you run the Properties command, a dialog box is started where you can view and modify the properties
of the selected breakpoint. In this dialog box you can, for example, enable or disable a breakpoint. See these
sections:
- Line Breakpoint properties on page 113
- Method Breakpoint properties on page 113
- Watchpoint properties on page 114
### Icons and decorators

### Icons

These icons are displayed in the Breakpoints view:
Decorators
The following decorators are used to indicate whether a breakpoint is installed or invalidated. They are
displayed in the bottom left corner of the breakpoint icon.
Note: The "Invalidated" decorator is not applicable for method breakpoints.
## BFlow Palette view

This view shows the actions you can use in BFlow tests.
Use the buttons in the title bar to change the way the actions are displayed. The actions can be displayed in
these ways:
- As a list, in alphabetical order
- Grouped by category
To add an action to a Bflow test, drag the action to the tree in the Actions tab in the BFlow Editor. Alternatively,
use the shortcut menu of the tree.
## Component Explorer view

This view provides a hierarchical view of the software components on the LN server.
Use this view to add these software components to your personal activity in the LN Studio:
- Additional Files
- Domains
- Functions
- Labels
- Libraries
- Menus
- Messages
- Questions
- Reports
- Sessions
- Tables
The following table describes the different nodes in the previous figure.
Nr. in figure
Description
Application that determines the development repository to be used.
LN package code displayed in ascending order (for example: td, tf, tp).
Main Component Type. For example: Domain, report, session, or table.
LN module code displayed in ascending order.
The module code is displayed for all component types, except domains and labels.
Nr. in figure
Description
LN software component displayed in ascending order.
Double-click a software component to add the component to your personal activity.
To find a particular software component, perform one of these actions:
- Expand the relevant folders in the Component Explorer view. For example, to find the Employees -
General (tccom0101m000) session, expand the following folders: tc (Common), Sessions, and com
(Common Data).
- On the LN Studio toolbar, click Select a Software Component, or press ALT+Q. The Select Component(s)
dialog starts. Use this dialog to find components and link them to your current activity.
Note: Labels are not sorted by module, but by search key. They are divided into subgroups.
Messages and questions are sorted by module. If a message or question code does not start with a valid
module code, the message/question is categorized in the "other" subgroup.
### Toolbar

The toolbar of the Component Explorer view includes the following buttons:
Refresh
Hide expired components
Hide checked out components
Refreshes the contents of the view. For example, use this command when
you have created a new session on the LN server and want the session to
appear in the Component Explorer view.
Hides components with the Expired status.
Hides components already checked out.
### Shortcut menu

To open the shortcut menu, select one or more software components in the view. Then right-click.
The shortcut menu contains the Get command. Use this command to link the selected software components
to your current activity.
The components are now displayed in the Activity Explorer view. You can now check out and edit the
components.
See Developing software components on page 53.
Note: When you use the Get command, the editor can automatically start for the selected components.
However, this depends on your workbench preference settings.
See Preferences - Workbench on page 123.
### Icons and decorators

### Icons

The following icons are displayed in the Activity Explorer view:
Note: The Loading node is displayed when information is retrieved from the server. For example, this happens
when you open a node for the first time.
Such a load process is time-consuming. Therefore the information is gathered in the background.
## Debug view

You can use the Debug view to manage the debugging or running of Infor LN sessions in the workbench. The
view shows a list of sessions, either started normally (in run mode) or started in debug mode. The view also
shows related information (stack frames) and state information (terminated, running or suspended).
If you suspend a session, the view shows the stack frames for the suspended session. A session is displayed
as a node in the tree. The corresponding stack frames are displayed as child elements.
> [!NOTE]
- In a multi-tenant environment you cannot debug with LN Studio. You can use the Debug Workbench, see
the Debug and Profile 4GL (ttadv1123m000) session.
- In a multi-tenant environment you cannot debug BFlows with LN Studio. You can run BFlows in the LN
UI to see the result.
### Toolbar

The toolbar of the Debug view contains the following buttons:
Remove All Terminated
Launches
Resume
Removes all terminated sessions from the Debug view.
Suspend
Terminate
Disconnect
Step Into
Resumes a suspended session. The session resumes its execution and stack
frames are no longer displayed for the session. The Variables view is cleared.
Requests to suspend a running session. The session is suspended when the next
debugable line is hit.
See Suspending sessions on page 66.
Terminates the session related to the selected item.
This command is not supported by LN Studio.
Steps into the current statement. This command invokes the next instruction
to be executed. The execution suspends at the next executable line.
Note: Ensure the Reuse editor when displaying source code option in the
Run/Debug preferences dialog is disabled. If this option is enabled, and you
use the Step Into command while the script is not in the workspace, an error
page is displayed in some situations.
Step Over
Step Return
Steps over the current statement. This command executes the next instruction.
The execution suspends on the next executable line.
Continues the execution until the end of the current function.
Note: This command is equivalent to the return action in the classic 4GL Debugger.
This command is not supported by LN Studio.
This command is not supported by LN Studio.
Drop to Frame
Use Step Filters / Step
Debug
Menu
Contains the View Management command. This command starts a preference
page where you can configure the debugger to open debug-related views, such
as the Variables view and the Breakpoints view, in non-debug perspectives.
> [!NOTE]
- Most of these commands are also available in the Run menu in the Eclipse Workbench.
- The Run menu contains an additional command: Run to Line (CTRL+R). This command moves the
execution pointer, without executing code, to the line you selected in the Script Editor. Run to Line is
equivalent to the Go to Line action in the classic 4GL Debugger.
- For more information, see Debugging LN sessions on page 62.
### Shortcut menu

Right-click on any resource in the view to open a shortcut menu. This table shows commands in the menu:
Copy Stack
Find
Copies the selected stack of suspended sessions and the state of the running
sessions to the clipboard. You can paste the information from the clipboard into
various applications, such as MS Word and Notepad.
Starts a dialog where you can enter a search expression to find items in the Debug
view.
Terminates the session related to the selected item and relaunches the session.
Terminate and Relaunch
Remove All Terminated Removes all terminated sessions from the Debug view.
Re-launches the session related to the selected item.
This command is not supported by LN Studio.
Terminate and Remove Terminates the session related to the selected item and removes the session from
the Debug view.
Terminates all sessions.
Starts a property page with process information for the session you selected in
the Debug view.
Relaunch
Edit <session name>
Terminate All
Properties
For information on shortcut menu commands that are not mentioned in the previous table, see the descriptions
of the Toolbar commands.
### Icons

These icons are displayed in the Debug view:
> [!NOTE]
- You can only suspend sessions started in debug mode. If a session was started normally (in run mode),
you cannot suspend the session, but only terminate it.
- Stack frames are only available when the session is suspended.
## Limitations

Exit value not displayed
The exit value of an LN process is not displayed in the Debug view.
“An error has occurred. See error log for more details” error message
While debugging, the message "An error has occurred. See error log for more details" may be given by
Eclipse. This is not a fatal error. Click the OK button and resume debugging.
## Dependent InContext Models view

This view shows the dependent InContext Models of a selected InContext Table Model.
After you modified an InContext Table model, you can use this view to refactor all dependent models. To
open this view, click the Dependent InContext Models link in the Table InContext Model Editor.
In this view, you can select one or more InContext Models and then use toolbar buttons or shortcut menu
options to refactor these models.
To refactor the dependent models:
1 Select the dependent models in the view.
2 Check out the selected models.
3 Refresh context messages for the selected models.
4 Regenerate libraries for the selected session models.
5 Check in the selected models.
### Toolbar

This table shows the descriptions of the toolbar buttons:
Button
Description
Refreshes the contents of the view.
Checks out the selected InContext models.
Checks in the selected InContext models.
Refreshes the context messages for the selected InContext models. Only checked-out models are
processed.
(Re)generates the libraries for the selected InContext session models.
### Shortcut menu

Right-click in the view to open a shortcut menu. The commands in the menu are also present in the toolbar.
See the description of the toolbar buttons.
## Expressions view

The Expressions view contains a list of watch expressions. Only variables are supported. These watch
expressions are evaluated each time a session suspends. The expressions are evaluated in the context of the
currently selected stack frame.
The left part of the screenshot shows the Debug view with the selected stack frame. The right part shows the
Expressions view with the watch expressions. In the screenshot, the Expressions view consists of an overview
pane (left) and a details pane (right).
The details pane shows this information:
- Value of primitive variables.
- Hexadecimal value of variables of type string.
- XML structure of variables of type XML.
Expressions that cannot be evaluated in the context of the current stack frame are indicated as “cannot be
resolved”.
You can determine the amount of information displayed in the Expressions view. For example, you can show
/ hide the following:
- Data type information.
- The details pane.
See the description of the toolbar and shortcut menu commands.
Note: Try to keep the list of expressions limited. This is, because all expressions are evaluated each time a
session suspends, which can affect the performance adversely.
If an array variable contains more than 10 dimensions, the variable is divided into partitions of 10 dimensions.
### Toolbar

The toolbar of the Expressions view contains these buttons:
Show Type Names
You can toggle this option to show or hide data type names. The data type names
are displayed in front of the expression names.
Show Logical Structure
Collapse All
Menu
Displays certain complex data structures in a more compact and meaningful form.
For example, elements of a list are displayed as an ordered collection. Therefore,
you can easier navigate complex data structures in terms of their logical structure,
than in terms of their implementation.
Collapses all expanded expressions.
Contains these layout options:
- Vertical View Orientation: The details pane is displayed below the overview
pane.
- Horizontal View Orientation: The details pane is displayed next to the overview
pane.
- Expressions View Only: The details pane is not displayed.
### Shortcut menu

Use the shortcut menu to add, remove, and edit watch expressions. If you right-click a watch expression when
the debugger is active, the shortcut menu also contains the Reevaluate Watch Expression command. This
command evaluates the watch expression again, which is useful after editing a watch expression.
Note: To define an expression that must be executed only once, click Execute Assignment Expression. The
Execute Assignment Expression dialog box starts. See the dialog box's online help.
To create a watch expression that is executed each time you step through the execution, click Add Watch
Expression. The Add Watch Expression dialog box starts. In this dialog box, specify the expression in this
format: <variable>:=<value>. Then, select the Enable check box and click OK.
### Icons and decorators

### Icons

These icons are displayed in the Expressions view:
Decorators
The following decorators are used to indicate whether a variable is fixed and / or based. Decorators are
displayed in the upper right corner of the variable icon.
## Limitations

Limited to variables
Currently, it is only possible to evaluate expressions that are actually variables. It is not possible to evaluate
other expressions, such as I=0.
Changing values not reflected in UI
The value of an expression is not updated, when the value of the contained variable is changed. To solve this,
use the Reevaluate Watch Expression command on the expression.
## History view

This view shows all revisions of the selected component, which are present in the derivation path of your
Activity VRC.
This figure shows the revisions of a session that was selected in the Activity Explorer:
Revisions can exist for these components:
- Domain
- Function
- Label
- Library
- Menu
- Message
- Question
- Report
- Session
- Table
## Columns

This table shows the columns in the view:
Column
VRC
Revision
User
Check In Date/Time
Revision Text
Description
A tree structure that shows this information:
- The Package VRC to which the revision belongs.
- The component type.
For sessions and tables, separate revision numbers
are stored for the session or table itself and for the
corresponding UI script or DAL script. You can expand the component type node to view the corresponding script revisions. See the previous figure.
The other components have only one revision
number.
If you expanded a session or table node, the shortcut
menu items are only enabled if a script is selected.
The number of the revision.
The user that created the revision.
The date the revision was created.
The revision text that describes the functionality of
the changed software component.
If the text in a column does not fit in the column, hover over the text. A tooltip with the complete text is
displayed. Click inside the tooltip, or press F2, to view the text in a dialog box.
### Toolbar

This table shows the most important toolbar buttons:
Button
Description
Refresh
Refreshes the contents of the view.
Link with Editor and Selection
When enabled, the view shows the history for the resource of the active editor or of
the active selection.
Pin this History View
When enabled, pins the view and its contents. Any new requests for history open a
new instance of the History View.
Show Previous Histories
When enabled, you can select a resource, for which a history has been viewed in the
past, from a drop-down menu. This button is disabled when the History view is
opened for the first time.
Expand All
Expands all categories.
Collapse All
Collapses all categories.
Checkout to current
Checks out the component and updates it to the selected revision.
Compare
This button is only enabled if two items are selected. Opens the Compare view where
you can view the differences between both revisions.
Compare To Local
This button is only enabled if one item is selected. Opens the Compare view where
you can view the differences between the selected revision and the local version.
Show revision details
Opens the selected item.
Double-clicking an item has the same effect as this command.
### Shortcut menu

Right-click on a selected item to open a shortcut menu. The commands in the menu are also present in the
toolbar. See the description of the toolbar buttons.
## Outline view

This view displays an outline of a script or library currently open in the script editor, and lists the main structural
elements.
The contents of the outline depend on the type of library or script. For example:
- For a library, the Outline view displays the corresponding functions.
- For a UI script, the outline consists of functions (if any) and script sections, such as:
- Program sections.
- Form sections.
- Group sections.
- Choice sections.
- Field sections.
- ZoomFrom sections.
- Main Table sections.
This figure shows the outline of a UI script:
When you select a structural element in the Outline view, the cursor will move to the corresponding line in
the script editor.
The Outline view is updated automatically when you edit a script or library.
### Toolbar

The toolbar of the Outline view includes the following buttons:
Sort Outline
Hide return type
and arguments
Menu
Sorts the displayed folders and their contents alphabetically.
Hides return types and arguments of functions.
Contains these options:
- Link With Editor: Toggles whether the contents of the Outline view are linked
to the active editor. When this option is selected, changing the active editor will
automatically update the contents of the Outline view to the resource being
edited.
- Hide return type and arguments: Hides return types and arguments of functions.
- Hide local functions: Hides local functions, so only external functions are displayed.
- Hide sections: Hides sections, so only functions are displayed.
- Show external functions first (in sorted list): if you sort the displayed folders
and their contents, external functions are displayed at the top of the list.
### Shortcut menu

The Outline view contains a shortcut menu. This enables you to define method breakpoints.
This table shows the commands in the shortcut menu:
Toggle Method
Breakpoint
Adds or removes a method breakpoint for the selected function. When started in
debug mode, the session suspends when the execution reaches a function for which
a method breakpoint was set.
This command is only available for functions and not for other structural elements.
For more information on breakpoints, see Using breakpoints on page 68.
### Icons

The following table explains the icons used to identify the structural elements.
For details on the 4GL components mentioned in the previous table, see the Infor ES Programmers Guide (Infor
Customer Portal KB2924522).
## Problems view

The Problems view displays system-generated errors, warnings, or information associated with a resource.
These are typically produced by builders/compilers. For example, if you build a source file that contains syntax
errors, the errors are automatically logged in this view.
Note: If a problem is associated to (a line within) a component, double-click the problem to edit the component.
The script editor opens the component at the involved line.
The problems are grouped into the following severity categories: Errors, Warnings, and Information.
This table shows the columns in the view:
A description of the problem. Also indicates the severity of the problem: Error, Warning or Info.
Description
Resource The name of the resource associated with the problem.
Path
Location
Type
The folder in your workspace where the resource is stored.
The line number of the problem within its associated resource.
The type of problem, such as "Script Problem".
### Toolbar

This table shows the buttons in the toolbar of the view:
Provides commands to sort and filter the contents of the view, and to define preferences.
Menu The Configure Contents command in the menu starts a dialog box where you can specify filters.
You can filter items according to which resource or group of resources they are associated with. The
filtering is performed by text string within the Description field, or by problem severity.
Note: To view problems and warnings related to the following, select the appropriate check box in
the Configure Contents dialog box:
- Configuration management: select the SCM Problem check box.
- The source code in your scripts and libraries: select the Script Problem check box.
Known limits
The filter does not work properly if the Link with Editor option in the Activity Explorer is selected. For
example, if you filter “On selected element only”, the compilation errors and warnings belonging to the source
file are not displayed properly.
### Shortcut menu

To open the shortcut menu, right-click on a resource in the view.
This menu provides various commands, such as a Properties command to view the properties of the selected
problem.
For details on the other commands, see "User interface information" in the Workbench User Guide.
### Icons

These icons are used by the Problems view:
## Progress view

The Progress view shows the progress of background processes. For example, it is used when the following
occurs:
- You open an activity.
- CM (Configuration Management) information is loaded from the LN server. This can occur when you start
LN Studio, or the first time you open a node in the Component Explorer view. In both situations, the
requested data is retrieved by a background process. When the process is finished, the data is displayed
in the Component Explorer view.
- You build a software component or a project.
- You verify a software component.
This figure shows an example:
The progress of these processes is displayed in the Progress view, and indicated in the bottom-right corner
of the workbench window. See the previous figure.
### Toolbar

The toolbar of the Progress view includes these buttons:
Remove All Finished Opera- Removes all finished operations from the Progress view.
tions
Menu
The menu contains these options:
- Remove All Finished Operations.
- Preferences: Starts a dialog box where you can indicate whether the
view must display sleeping and system operations.
### Icons

The following icons are used in the Progress view
## Tasks view

The Tasks view displays Eclipse Tasks you add manually.
Each Eclipse task represents an action that needs to be carried out, such as to modify a particular line in a
script. You can associate a task with a resource in the Workbench, but this is not required.
The Tasks view enables you to add new tasks, and to maintain and remove existing tasks.
The second and third task in the screenshot are associated to a line in a script. The first task is not associated.
> [!NOTE]
- If a task is associated to (a line in) a script or library, double-click the task to edit the script or library. The
editor opens the script or library at the involved line.
- You can add new tasks from the LN Studio script editor.
For more information, see Source Tab on page 270.
This table shows the columns in the view:
The first column
Indicates whether the task is completed. You can manually select or clear the check
box.
Indicates whether the task is high, normal, or low priority.
The second column
Description
Resource
Path
Location
Type
A description of the line item.
The name of the resource associated with each line item.
The folder in your workspace where the resource is stored.
The line number of the line item within its associated resource.
The type of task, such as "Task" or "Java Task".
You can edit the first three columns directly in the grid, and via the Properties command in the shortcut
menu.
### Toolbar

This table shows the buttons in the toolbar of the view:
Provides commands to sort and filter the contents of the view, and to define preferences.
Menu The Configure Contents command in the menu starts a dialog box where you can specify filters.
You can filter items according to which resource or group of resources they are associated with. The
filtering is performed by text string within the Description field, by task priority, or by task status.
Note: You can define a specific filter for TODO reminders.
See ToDo Comments on page 293.
### Shortcut menu

To open the shortcut menu, right-click on a resource in the view:
This menu provides various commands, for example:
- Commands to add or delete tasks
- A command to change the properties of the selected task
- A command to delete completed tasks
See "User interface information" in the Workbench User Guide.
### Icons

The following icons are used by the Tasks view:
## Variables view

The Variables view is part of the Debug perspective.
The Variables view displays a list of variables that exists in the scope of the selected Stack frame. The values
of primitive variables are displayed. To examine a complex variable, expand the variable to show its members.
XML nodes are displayed in an XML tree, which you can collapse and expand.
The view is usually empty. However, it is automatically filled when a session in debug mode is suspended,
and a stack frame is selected in the Debug view.
This figure shows an example:
The left part of the screenshot shows the Debug view with the selected stack frame. The right part shows the
Variables view with the stack frame's variables. In the screenshot, the Variables view consists of an overview
pane (top) and a details pane (bottom).
The details pane shows this information:
- The value of primitive variables.
- The hexadecimal value of variables of type string.
- The XML structure of variables of type XML.
You can determine the amount of information displayed in the Variables view. For example, you can show /
hide the following:
- Data type information.
- The details pane.
See the description of the toolbar and shortcut menu commands.
Note: The Variables view displays all variables that are in scope. If a session contains a lot of variables, the
performance can be affected. To boost the performance, close the Variables view and use the Expressions
view.
### Toolbar

The toolbar of the Variables view contains the following buttons:
You can toggle this option to show or hide data type names. The data type names
are displayed in front of the variable names.
Show Logical Struc- Displays certain complex data structures in a more compact and meaningful form.
For example, the elements of a list are displayed as an ordered collection.
Collapses all expanded variables.
Contains these menu items:
- Layout: Opens a menu with the following options:
- Vertical View Orientation: The details pane is displayed below the overview
pane.
- Horizontal View Orientation: The details pane is displayed next to the
overview pane.
- Variables View Only: The details pane is not displayed.
- Show Columns: The overview pane displays columns with, for example,
the names and values of the variables.
- Select Columns: Starts a dialog box where you can select the columns to
be displayed.
- Show Global Variables
- Show Local Variables
Show Type Names
ture
Collapse All
Menu
### Shortcut menu

To open the shortcut menu, right-click on a variable in the view. The menu contains these commands:
- Select All Ctrl+A
- Copy Variables Ctrl+Insert
- Find Ctrl+F
- Change Value
- Create Watch Expression
Use the Create Watch Expression command to define a watch expression. The selected variable is copied
to the Expressions view. Watch expressions are evaluated each time a session suspends.
### Icons and decorators

### Icons

The following icons are displayed in the Variables view:
Decorators
The following decorators are used to indicate whether a variable is fixed and / or based. The decorators are
displayed in the upper right corner of the variable icon.
This figure shows an example:
## Limitations

Filters not correctly initialized
The filters in the Variables view ( Show Global Variables and Show Local Variables) are not correctly
initialized. To correct the settings, click the stack frame twice or select a variable in the Variables view.
## Verify Components view

This view shows the warnings generated when you verify software components. The verification process
performs various checks based on the LN design principles.
For more information on the verification of software components, see these sections:
- Verifying software components on page 56
- "Verify Software Components (VSC)" in the Web Help on the LN server.
You can view the generated warnings and the corresponding details and decide to accept each warning
individually, or solve the problem.
Note: When you double-click a warning, the appropriate editor for the software component starts automatically
at the location where the error occurs.
Severi- The view displays a warning icon with a number that indicates the priority of the warning:
ty
- 2 - Normal
- 3 - Suspicious
- 4 - Low
These priorities are automatically assigned by the verification process:
- The priorities for warnings that are generated based on source analyze codes are defined in
the Source Analyze Codes (tlvsc3111m000) session.
- The priorities for warnings that are generated based on all other types of checks are hard
coded in the VSC software on the LN server.
Note: If a warning blocks the check in of a component, an error icon is displayed instead of a
warning icon.
Accept- Shows a check mark if the warning is accepted.
ed
The unique code that identifies the message assigned to the warning.
For example: the message ID for a warning is 5053. The corresponding message text is Function
'sleep' is not supported by        Web UI                                .
Note: This column corresponds with the Warning Id field in the Verify Warning Details dialog
box.
- 1 - High
VSC ID
The text of the message that is assigned to the warning.
For example: Function 'sleep' is not supported by        Web UI
The location in the software component where the error occurs.
For example:
- A line number in a script or library.
- A form or report in a session.
The LN Studio resource that represents the software component for which the warning is generated.
For example:
- tfgld1101m000.ses (session)
- tfgld1101m000.sessrc (program script)
Project The software project to which the software components belong.
Message
Location
Resource
### Toolbar

The toolbar of the Tasks view includes the following buttons:
Verify Warning Fil- Starts the Verify Components View Filter dialog box. You can, for example, define a
filter that displays only warnings with a particular warning level.
See Verify Components View Filter on page 125.
ter
### Shortcut menu

Right-click on any resource in the view to open a menu that contains the View Details command. This
command starts the Verify Warning Details dialog box. In this dialog box, you can view the warning details,
and change the warning status to "Accepted". See the dialog box's help.
### Icons

These icons are used in the view:
## Table Fields view

This view responds to the Session Editor; it shows the table fields of the main table of the opened session,
including any references to other tables.
Use this view to drag and drop table fields on the tree within the session editor's Form Definition tab.
To expand or collapse all nodes of the tree, click the icons above the tree.
Specify text in the filter text box to only show these fields and elements:
- Fields with names that contain the specified text
- Elements with child elements that have names that contain the specified text
### Shortcut menu

To view the table field's details, right-click the field and select Open. The Table Editor starts, with the
appropriate table field selected.
Copy is also enabled.
## Call Hierarchy view

The function-call hierarchy view provides a view in tree format of the calls to and from a selected function,
thus providing a clear overview of the interrelated function calls, which can grow into large, elaborately
intertwined call hierarchies.
Prerequisite
The Call Hierarchy functionality is dependent on the Source Analyzer Tools. Therefore, you must initially
create the Source Analyzer Data in theUpdate Scripts for analysis (tlanl1201m000) session and in the BSE
Services (ttaad8110m000) session, select the Automatic Start check box for the Queue Service
(ttaad8020m000) session to ensure that the data is automatically updated.
Starting the Calls Hierarchy view
To view the calls related to a function, select and right-click a function and on the context menu, select Call
Hierarchy.
You can select a function in any of these locations:
- In the script code opened from an open activity. The script code can belong to any component, such as
a session, table, or library.
- The Outline view.
- A function node, at any level, within the call hierarchy of a function. If you right-click a node, the context
menu shows these options:
- Show Caller Hierarchy
- Show Callee Hierarchy
See the next section for a description of the Show Caller Hierarchy and Show Callee Hierarchy options.
You can also open the Call Hierarchy View on the LN Studio menu:
Window -> Show View -> Other -> Infor LN Studio Application -> Call Hierarchy.
Using the Call Hierarchy View
The Call Hierarchy View shows the function calls of the selected function in a tree structure. The selected
function is the parent, that is, the top node in the tree structure.
The parent function can have calls to multiple other functions displayed as child functions in the tree structure.
In turn, a child function can have multiple child and parent functions, that is, calls to and from other functions.
To operate the Call Hierarchy View, you can use these toolbar buttons:
Toolbar button
Show Caller Hierarchy
Show Callee Hierarchy
Description
Shows the functions that call the selected function.
If you double-click a selected child function, the line
number where the parent function call is made is
opened. The file of the parent call is downloaded
and opened if it was not already available in the
workspace.
Shows the functions that the selected function calls.
If you double-click a selected child function, the selected function is opened. The file of the call is
downloaded and opened if it was not already available in the workspace.
Toolbar button
Show History List
History
Clear History
Expand 'n' level
Collapse
Open Call Hierarchy Preference Page
Description
Show History List is a combination of a toolbar button and a drop-down list. The drop-down list is displayed as a small black triangle.
If you click the toolbar button, a pop-up window
opens showing all previously browsed functions.
If you click the drop-down list icon, the 10 most recently browsed functions are displayed.
After selecting a function from the drop-down list
or the pop-up window, the call hierarchy of the selected function is displayed in the Call Hierarchy
view according to the Show Caller Hierarchy or the
Show Callee Hierarchy toolbar button selected previously.
Identical to Show History List.
Removes the list of the browsed functions.
Expands the selected function with the number of
levels specified in the Preferences window, which is
opened on the LN Studio menu by selecting Window
- > Preferences.
The configured number of levels is also shown as
tooltip of the Expand ‘n’ level button.
Collapses a function node.
Opens the Preferences window, in which you can
specify the number of nodes with which the selected
function node is to be expanded. You can specify up
to five nodes.
Filtering
In the text box in the upper right corner of the Call Hierarchy View, you can use these anchors to specify criteria
with which you can filter the list of functions:
Anchor
^
$
.
*
|
\
Description
The start of a line.
The end of a line.
Any character.
Zero or more characters.
Or
The next character.
For example, you can use ^td.*sales to retrieve functions related to sales in the TD package.
