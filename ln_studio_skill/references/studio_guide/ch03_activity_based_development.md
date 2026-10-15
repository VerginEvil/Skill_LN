# Chapter 3: Activity based development

The software development process in LN Studio is activity based. Before a software component can be
modified, a software engineer must link the component to an activity. Each activity is part of a software project
and each software project belongs to an Application.
This diagram shows an application, software projects, and activities:
A software application is a consistent set of packages that functionally belong together. An application is
linked to a Base VRC, which determines the environment on the LN server in which the application's software
components are stored. Administrators can create applications through the Application Explorer view.
See the Infor LN Studio Administration Guide.
For each high level software requirement (business requirement), a software project is created on the Project
Server. Multiple projects can be defined per application. A software project is split up into activities. Project
managers can create software projects and activities. They can also view the modified LN software components
per activity, through the Software Project Explorer. A separate activity is created for each individual software
requirement, such as a bug fix or a new feature within the project. Each activity is assigned to a software
engineer. See "Defining a software project" in the Project Server documentation.
Software engineers can open their activities through the Activity Explorer view.
See Developing software components on page 53.
> [!NOTE]
- Components in an activity are only accessible for the software engineer to which the activity is assigned.
However, other software engineers can access these components if they put this activity in the activity
context of their own activity.
See Activity context on page 48.
- Activities can be shared over multiple software engineers when their names are added as Assignee in the
Activity properties. In this case they also can modify the components.
## Configuration Management

The configuration management in LN Studio is based on the Software Configuration Management (SCM)
module in Enterprise Server. SCM is based on RCS, a freeware third party tool available for the UNIX and
Windows platforms. SCM supports the Check out and Check in of various software components. A more
extensive CM solution will be offered in a future release. For details on the usage of SCM, and information on
how to set up an SCM environment on the LN server, see To use the Software Configuration Management
system (SCM).
Note: Due to SCM limitations, the LN Studio configuration management is only available for main component
types such as forms, sessions, table definitions, reports, and functions. The 4GL component types, such as
labels, questions, and messages, are not supported.
## Usage of SCM

The usage of SCM has an impact on the VRC structure on the LN server. It also impacts the way configuration
management actions, such as check in and check out, work.
The usage of SCM is optional. If you use SCM, you must at least activate SCM for the project VRC(s) on the LN
server. Additionally, you can enable SCM for your LN Studio application(s).
The following situations can be distinguished:
Scenario
SCM for project VRCs
and applications
Description
SCM is activated for the project VRC(s) on the LN server and for the applications
in LN Studio. This is the preferred scenario if your LN server supports SCM.
Each time you check in a component, LN Studio generates a new revision.
Other software engineers can use (not modify) your checked in components.
See Development with SCM for project VRCs and applications on page 40.
Scenario
No SCM
Description
SCM is disabled for the project VRC(s) on the LN server and applications in LN
Studio.
LN Studio does not generate any revisions.
Other software engineers can use (not modify) your checked in components and
your checked out components.
See Development without SCM on page 44.
## Activating SCM for a project VRC

1 Log on to the LN server.
2 Start the Package VRCs (ttadv1511m000) session, and create a new (SCM) VRC. The new VRC must be
derived from the project VRC.
3 Start the (De)activate SCM and Component Management by Package VRC (ttscm0501m000) session.
The session shows a list of VRCs. Select the project VRC. On the appropriate menu, select Activate SCM
(and CM). The Activate SCM and Component Management by Package VRC (ttscm0110s000) session
starts.
4 Select the new SCM VRC and click OK.
5 To make the changes effective, log off and log on again.
See "To use the Software Configuration Management system (SCM)" in the LN Web Help.
## Activating SCM for an application

Note: You can only activate SCM for an application if SCM is active for all project VRCs in the application.
To activate SCM for an application:
1 Start LN Studio. Open the Application perspective.
2 Go to the Application Explorer view.
3 Expand the correct development environment.
4 Expand the 'Applications' tree structure. Double-click the application to start the Application properties
dialog box.
5 Select Use SCM.
6 Save the changes. Close the dialog box.
## Software components

When a personal activity in the LN Studio is open, you can link software components from the LN dictionary
to the project. You can also create new components through the LN Studio.
You can link or create these components:
- Additional File
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
These software components are the starting point of development for a software project.
The LN Studio shows a tree of software components on the LN server and a tree of components in your current
activity.
For details on the layout of LN Studio, see LN Studio workbench on page 20.
## Development with SCM for project VRCs and applications

VRC structure
If SCM is enabled for project VRCs and applications, LN Studio generates two VRCs on the LN server for each
activity: an Activity VRC and a Private VRC. In these VRCs, a software engineer can modify software components
without disturbing other software engineers.
This diagram shows an example:
These VRCs are used:
- The 'old' VRC contains software components developed in a previous project.
- The Project VRC contains all finished software components for the project. From here, deliveries to
customers are performed, once the project is completed.
Note: The project VRC is the Export VRC linked to the Base VRC of the Application to which the project
belongs. Therefore, the project VRC contains finished software components for other projects defined
for the same application.
- The SCM Project VRC is derived from the project VRC. It is used to store checked out software components.
- The Activity VRC contains checked in software components for an activity. The activity VRC is generated
automatically when you open the activity for the first time. The components in this VRC are only accessible
for the software engineer to which the activity is assigned. However, other software engineers can access
these components if they put this activity in the activity context of their own activity.
See Activity context on page 48.
- The Private VRC is derived from the activity VRC. It contains the checked out components the software
engineer is working on. The components in this VRC are only accessible by the software engineer to which
the activity is assigned. The private VRC is generated automatically when you open the activity for the
first time.
Note: Various software engineers can work at the same activity. In that case, multiple private VRCs exist for
the same activity VRC.
## VRC numbering

The numbers in the customer extension of the activity and private VRCs are generated automatically:
- Activity VRCs: Numbering starts with 0001. The number is increased for each new activity VRC. The
maximum number is 4999.
- Private VRCs: Numbering starts with 9999. The number is decreased for each new private VRC. The
minimum number is 5000.
Example
LN Studio generates these VRCs:
- For the first activity: activity VRC B61_a3_0001 and private VRC B61_a3_9999.
- For the second activity: activity VRC B61_a3_0002 and private VRC B61_a3_9998.
- For the third activity: activity VRC B61_a3_0003 and private VRC B61_a3_9997.
Note: The numbers of an activity VRC and the corresponding private VRC do not always have to be
complementary. This is because multiple private VRCs can exist for the same activity.
When you end an activity, LN Studio performs a roll-up of all component revisions and revision texts. The
resulting components and texts are moved to the project VRC. The empty activity VRC and private VRC are
released, allowing these VRCs to be reused in the future.
## CM actions

Check out
You must check out a component before it can be modified. LN Studio checks whether the component is
already present in your activity VRC (for example because of an earlier check out and check in action).
- LN Studio does not support parallel development for applications. Therefore, if the component is not
present in your activity VRC, LN Studio locks the component in the Project VRC, so that other software
engineers cannot check out the component, and copies the component to your private VRC where it can
be modified. The component stays locked until you end your activity.
- If the component is already present in the Activity VRC, LN Studio copies the component from your activity
VRC to your Private VRC. The component in the project VRC stays locked.
To check out a software component in LN Studio:
1 Right-click the component in the Activity Explorer view.
2 Select Team > Checkout.
Note: If you try to change a component which is not checked out, you are prompted whether you want to
check out the component.
Check in
You can check in a component when you finish the changes to the component.
LN Studio moves the checked out component from your private VRC to your activity VRC. A historical version
(revision) is generated, for which you must enter a revision text.
> [!NOTE]
- The checked in component stays in the activity VRC. The component is not copied to the project VRC.
The component in the project VRC stays locked and not accessible to all software engineers. To unlock
the component in the project VRC and to make it accessible for other software engineers, end or cancel
the activity, or delete the component from the activity.
- Other software engineers can use (not modify) your checked in components. This is possible if your
activity is inserted into the activity context of their own activity.
See Activity context on page 48.
To check in a software component in LN Studio:
1 Right-click the component in the Activity Explorer view.
2 Select Team > Checkin. The Check In comment dialog box starts. Specify a comment and click OK to
check in the component.
> [!NOTE]
- The revision text is stored in the configuration management system on the server. A single text is used
for all revisions of a component. This text is displayed each time you check in a new revision of the
component, so you can modify or extend it. If you check in multiple components together, you can use
the same revision text for all components.
See Check In comment on page 130.
- If Verify Software Components (VSC) is active and blocking VSC warnings are present, Check in is not
possible.
Undo checkout
You can undo the check out of a component. LN Studio removes the component from your private VRC and
cancels all changes you made since the last check in of the component. The component in the activity VRC
is not removed.
Note: The component in the project VRC stays locked and is not accessible for other software engineers. To
unlock the component in the project VRC and to make it accessible for other software engineers, end or cancel
the activity, or delete the component from the activity.
To undo the check out of a software component in LN Studio:
1 Right-click the component in the Activity Explorer view.
2 Select Team > Uncheckout.
End Activity
When you finish all changes in an activity, you can end the activity so the changed components are released
to the project VRC.
When you end an activity, LN Studio performs these actions:
- Creates a roll-up of all component revisions and revision texts in the activity VRC.
- Moves the resulting software components and texts from the activity VRC to the project VRC. Therefore,
components become available to other software engineers.
- Unlocks the components in the project VRC.
- Releases the private VRC and the activity VRC, so they can be reused in the future.
- Disconnects the corresponding run configurations from the activity. You can link these configurations
to another activity.
See Linking run configurations to an activity on page 51.
Note: You can only end an activity if all components in that activity are checked in.
To end an activity in LN Studio:
1 Right-click the activity in the Activity Explorer view.
2 Select Team > End activity.
Note: If not all components are checked in and the Partial End Allowed check box in the software project
properties is selected, you can partially end the activity. To do this, in the Activity Overview, End Activity
dialog box, select a subset of the components and click OK. See the dialog box's online help.
Cancel Activity
To undo all changes in an activity, cancel the activity.
LN Studio performs these actions:
- Removes all components from the activity.
- Unlocks the components in the project VRC.
- Releases the private VRC and the activity VRC, so they can be reused in the future.
To cancel an activity in LN Studio:
1 Right-click the activity in the Activity Explorer view.
2 Select Team > Cancel Activity.
Cancel a range of activities
To undo all changes in a range of activities, run the Global Cancel Activity (ttadv1223m000) session on the
LN server.
Note: This session does not update the status of the canceled activities in the Project Server. See the session
help.
## Development without SCM

VRC structure
If SCM is disabled for an application, LN Studio generates an Activity VRC on the LN server for each activity.
In this VRC a software engineer can modify software components without disturbing other software engineers.
This diagram shows an example:
These VRCs are used:
- The 'old' VRC contains software components developed in a previous project.
- The Project VRC contains all finished software components for the project. From this VRC, deliveries to
customers are carried out, once the project is completed.
Note: The project VRC is the Export VRC linked to the Base VRC of the Application to which the project
belongs. Therefore, the project VRC contains finished software components for other projects defined
for the same application.
- Activity VRC. Contains checked in and checked out software components for an activity. The activity VRC
is generated automatically when you open the activity for the first time. The components in this VRC are
only accessible for the software engineer to which the activity is assigned. However, other software
engineers can access these components if they put this activity in the activity context of their own activity.
See Activity context on page 48.
## VRC numbering

The numbers in the customer extension of the activity VRCs are generated automatically. The numbering
starts with 0001 and increases for each new activity VRC. The maximum number is 4999.
Example
LN Studio generates these VRCs:
- First activity: activity VRC B61_a3_0001.
- Second activity: activity VRC B61_a3_0002.
- Third activity: activity VRC B61_a3_0003.
Note: When you end an activity, the corresponding components are moved to the project VRC. The empty
activity VRC is released, so it can be reused.
## CM actions

Check out
You must check out a component before it can be modified. LN Studio checks whether the component is
already present in your activity VRC (for example because of an earlier check out and check in action).
- If the component is not yet present in your activity VRC, LN Studio locks the component in the Project
VRC, so that other software engineers cannot check out the component, and copies the component to
your activity VRC where it can be modified. The component in the project VRC stays locked until you end
your activity.
- If the component is already present in the activity VRC, the component gets the "checked out" status, so
that it can be modified. Note: The component in the project VRC stays locked until you end your activity.
To check out a software component in LN Studio:
1 Right-click the component in the Activity Explorer view.
2 Select Team > Checkout.
Check in
You can check in a component when you finish the changes to the component.
LN Studio changes the status of the component in the activity VRC to "checked in". To modify the component,
perform a new check out.
Note: The checked in component stays in the activity VRC. The component is not copied to the project VRC.
The component in the project VRC stays locked. Therefore, it is not accessible for all software engineers. To
unlock the component in the project VRC and to make it accessible for other software engineers, end your
activity, or cancel the activity or the component.
To check in a software component in LN Studio:
1 Right-click the component in the Activity Explorer view.
2 Select Team > Checkin.
Note: If Verify Software Components (VSC) is active and blocking VSC warnings are present, Check in is not
possible.
Undo checkout
You can undo the check out of a component. LN Studio cancels all changes made since the last check in of
the component. The component stays in the activity VRC.
Note: The component in the project VRC stays locked. Therefore it is not accessible for other software
engineers. To unlock the component in the project VRC and make it accessible for all software engineers, end
your activity.
To undo the check out of a software component in LN Studio:
1 Right-click the component in the Activity Explorer view.
2 Select Team > Uncheckout.
End activity
When you finish all changes in an activity, you can end the activity so the changed components are released
to the project VRC.
When you end an activity, LN Studio performs the following actions:
- Moves all software components in the activity VRC to the project VRC. Therefore, components become
available to other software engineers.
- Unlocks the components in the project VRC.
- Releases the activity VRC, so it can be reused.
- Disconnects the corresponding run configurations from the activity. You can link these configurations
to another activity.
See Linking run configurations to an activity on page 51.
Note: You can only end an activity if all components in that activity are checked in.
To end an activity in LN Studio:
1 Right-click the activity in the Activity Explorer view.
2 Select Team > End activity.
Note: If not all components are checked in and the Partial End Allowed check box in the software project
properties is selected, you can partially end the activity. To do this, in the Activity Overview, End Activity
dialog box, select a subset of the components and click OK. See the dialog box's online help.
Cancel Activity
To undo all changes in an activity, cancel the activity.
LN Studio performs these actions:
- Removes all components from the activity.
- Unlocks the components in the project VRC.
- Releases the activity VRC, so it can be reused.
To cancel an activity in LN Studio:
1 Right-click the activity in the Activity Explorer view.
2 Select Team > Cancel Activity.
Cancel a range of activities
To undo all changes in a range of activities, run the Global Cancel Activity (ttadv1223m000) session on the
LN development server.
Note: This session does not update the status of the canceled activities in the Project Server. See the session
help.
## Activity context

The components in an Activity VRC are only accessible for the software engineer to which the activity is
assigned.
Sometimes, it is necessary to use components developed by another software engineer.
For example:
- In your UI script, you want to use a new DLL developed by another software engineer.
- You want to open components from another software engineer through the Open Declaration command
in the Script Editor.
To access software components developed by another software engineer, put the activity that contains the
desired components in the activity context of your own activity.
To add an activity to the activity context of your own activity:
1 Right-click your activity in the Activity Explorer, and select Properties.
2 In the left pane in the properties dialog box, select LN Studio Activity Information.
3 Click the Context tab.
4 Click Add and select the project to which the desired activity belongs.
5 Click Add Activity and select the desired activity from the list.
6 Click OK.
Note: When you add multiple activities, use the Up and Down buttons to change the order in which the
activity VRCs are searched at runtime. The activity at the top of the list is searched immediately after your
own activity. Subsequently, the second activity in the list is searched, and so on.
To delete a project or an activity from the activity context, right-click the project or activity and select Delete.
Example- search order
Activity 1 has activity 4 in its activity context.
The search order for activity 1 is as follows:
1 Activity 1 private VRC (only if SCM is active)
2 Activity 1 activity VRC
3 Activity 4 activity VRC
4 Project VRC
5 Lower VRCs
This diagram shows an example:
The context of your activity can change. The context changes, for example, in these situations:
- You add another activity to the context of your activity.
- A new component is added in an activity that is in the context of your activity.
- An existing component is modified and compiled in an activity that is in the context of your activity.
If your activity context changes, complete the following steps to incorporate the changes in your activity:
1 Select Project > Clean. The Clean dialog box starts.
2 Use this dialog box to invoke a full build for your activity. All previous build results are discarded.
Note: Ensure the Build Automatically option in the Project menu is selected.
3 Recover your activity.
See Recovering an activity on page 50.
## Cleaning an activity

An activity can contain a lot of components that were retrieved from the server but never changed, such as
when you have frequently used the Open Declaration command.
Clean an activity to remove these unchanged components.
To clean an activity:
1 In the Activity Explorer, select the activity you want to clean.
2 Click Clean activity in the Activity Explorer 's toolbar. The Clean activity dialog starts.
3 Optionally, select Clean all activities in the dialog to clean all activities displayed in the Activity Explorer.
4 Click OK to start the cleaning process. The process removes all components that are not checked out,
created, or modified from the selected activities. All other components are ignored.
For details, see the online help of the Clean activity dialog box.
## Recovering an activity

You must recover an activity if, for some reason, the corresponding local workspace is not in sync with the
LN server.
The recovery process restores the components in the activity from the Configuration Management System
on the server to your local workspace. Optionally, unchanged components are removed from the workspace.
There are various situations in which you must recover an activity, such as:
- After a PC crash. On your new PC, you can start LN Studio, open your activity, and restore your local
workspace from the server.
- After new LN Studio software is installed on your PC and on the server. The structure of the old files in
your workspace is possibly not compatible with the new software. Recover your activity to retrieve new
files from the server.
- After an intermediate code freeze. Your local workspace is not valid anymore.
To solve this, you must recover your activity.
Note: You must select the Recover existing activity files check box in the Recover activity dialog.
- After a final code freeze. Your activities have moved to a different software project. The directory names
in your local workspace are not valid anymore.
To solve this:
1 Delete your activity from the local workspace. In the Activity Explorer, right-click the activity and,
on the shortcut menu, select Delete.
2 Open the activity again. In the Activity Explorer, click Open an Infor LN Studio Activity. The Open
an Activity - Select Project dialog appears. Select the new software project from the list and click
Next. In the second page of the dialog, select your activity from the list and click Finish.
3 Recover your activity.
Note: You must select the Recover existing activity files check box in the Recover activity dialog
box.
- After other developers checked in components you use in your components. Recover your activity to get
the latest versions of these components.
For example, you call another developer's DLL in one of your UI scripts. Recover your activity after the
other developer checked in a new version of the DLL.
Note: To use components of other developers, put the corresponding activities in the context of your
activity.
See Activity context on page 48.
- If the activity is shared with other developers. Recover the activity to display the components created
by the other developers.
- You have unchanged components in your activity. After a while, the server may contain new versions of
these components, changed by other developers. Recover your activity to get the latest versions of these
components.
Note: Recover you activity regularly to make sure the components in your workspace are up-to-date.
To recover an activity:
1 In the Activity Explorer, select the activity you want to recover.
2 Click Recover activity in the Activity Explorer 's toolbar. The Recover activity dialog starts.
3 Specify the settings for the recovery process.
See Recover activity on page 82.
4 Click OK. LN Studio shows the recovery actions that will be executed.
See Recover activity on page 83.
5 Click OK to start the recovery process. The recovery results are displayed.
6 Click OK to close the dialog.
## Reassigning an activity

To reassign an activity to another user:
1 In the Activity Explorer, right-click the activity and, on the shortcut menu, select Team. Then, click
Reassign Activity. The Reassign Activity dialog starts.
2 In the Reassign to field, select the user, to which you want to assign your activity, from the list.
3 Click OK to reassign the activity and close the dialog.
Note: After you have assigned an activity to another user:
- The other user has full permissions for the activity.
- You have only limited permissions for the activity. You can finish the components you were working at,
but you cannot check out other components, cancel the activity, or end the activity.
- You can reassign the activity to your self again.
If the other user has reassigned the activity to you, your permissions are still limited. To get full permissions,
you must refresh your activity properties. To do this:
1 In the Activity Explorer, right-click the activity and, on the shortcut menu, select Properties. A
properties dialog starts.
2 In the left pane, click Activity Information. The Activity Information dialog starts.
3 Click Refresh to update the permissions.
4 Click OK to close the dialog.
## Linking run configurations to an activity

This section describes the procedure to link one or more run configurations to an activity.
Use this procedure, for example, after you end an activity. When an activity is ended, the corresponding run
configurations are no longer linked to an activity. You can link these activities to another activity.
To link run configurations to an activity:
1 In the Activity Explorer, right-click the desired activity and select Link Run Configurations.
The Link Run Configurations dialog is displayed.
2 Select the desired run configuration(s) and click Link.
