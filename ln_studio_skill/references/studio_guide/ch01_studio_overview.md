# Chapter 1: LN Studio overview

LN Studio is a development platform for LN and is implemented in the Eclipse framework.
Eclipse is a Java based development environment with many plug-ins available. LN Studio adds several
plug-ins to Eclipse that supply additional functionality such as editors, views, wizards, and perspectives.
You can use LN Studio to perform these actions:
- Create and edit LN software components through the Eclipse workbench. You create components through
the Create a New Infor LN Software Component wizard. You can edit components through various
multipage editors.
- Run and debug sessions through the Eclipse workbench.
- Create and test Infor Business Interfaces.
Caution: The Java Connector Architecture (JCA) JCAAdapter4ERPln.jar library that is embedded in this
product is copyright and proprietary to Infor and contains interfaces and/or APIs that are strictly private to
Infor. These interfaces and/or APIs cannot be used by external applications, devices, and/or software libraries.
Usage of the JCA library will be monitored and, if used illegal, will cause a non-compliancy situation.
Note: A number of screenshots in the documentation may be based on previous application releases. They
can differ slightly from your application screens. However, the described functionality is similar.
## Functions and features

This section describes some key characteristics of LN Studio.
Activity based development
The software development process in LN Studio is activity based. Each modification that is performed on the
software must be linked to an activity. Each activity is part of a software project. A software project is linked
to an application. You can create new software projects and activities from the LN Studio, or select existing
projects and activities. Administrators can create new applications.
See Activity based development on page 37 and Applications on page 22.
Configuration Management (CM)
Currently the configuration management in LN Studio is based on the Software Configuration Management
(SCM) module in Enterprise Server. SCM is based on RCS, a freeware third party tool available for the UNIX
and Windows platforms, and supports the Check out and Check in of various types of software components.
A more extensive CM solution will be offered in a future release. For details on the usage of SCM, and information
on how to set up an SCM environment on the LN server, see To use the Software Configuration Management
system (SCM).
Workbench
The LN Studio workbench is based on Eclipse.
This table shows the features of the LN Studio workbench:
Feature
Wizards
Multipage Editors
Graphical Editors
Script editor
Description
LN Studio contains various wizards that you can use to create software components, such as sessions, menus, labels, libraries and messages.
See Create a New Infor LN Software Component wizard on page 94.
You can edit the new components using component-specific Multipage Editors.
LN Studio contains various multipage editors that you can use to edit software
components, such as sessions, menus, labels, libraries and messages.
See Multipage Editors on page 150.
Editors for modeling Business Interfaces and their implementations.
An editor that supports the 4GL programming language. A content assistant is
available, supporting syntax highlighting and completion of keywords. The
editor also supports an outline of the scripts or libraries.
See Script Editor on page 267.
Feature
Activity Explorer view
Problems view
Tasks view
Description
Shows a tree view of the software components in the activity that you have
opened, and their relation to each other.
Each activity is part of a software project and is assigned to a user (software
engineer). Activities and software projects are stored on the Project Server.
The Activity Explorer shows these components:
- Additional File
- Business Object
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
The view's shortcut menu enables you to perform Configuration Management
related actions, such as check in and check out, on these components.
See Activity Explorer view on page 299.
> [!NOTE]
- To create a new software component, you must use the Create a New Infor
LN Software Component wizard.
- To link a software component, which already exists on the LN server, to
the activity that you have opened in the Activity Explorer, complete one
of these steps:
- Use the Get command in the Component Explorer view.
- Use the Select a Software Component command in the LN Studio
toolbar.
- Use the Open Declaration command in the Script Editor.
- Project Managers can create new activities through the Software Project
Explorer view.
Shows errors and warnings from a project build (compilation).
See Problems view on page 325.
Shows Eclipse tasks. Each Eclipse task represents an action that must be performed, for example modify a particular line in a script. If a task is associated
to (a line in) a script or library, you can double-click the task to edit the script
or library. The editor opens the script or library at the involved line.
You can create Eclipse tasks through the Tasks view and from the LN Studio
script editor.
See Tasks view on page 328, Source Tab on page 270, and ToDo Comments on
page 293.
Feature
Verify Components
view
Build option
Run / Debug options
Description
Shows the warnings that are generated when you verify software components.
The verification process performs various checks, based on the LN design
principles.
For more information on the verification of software components, see this
documentation:
- Verifying software components on page 56
- "Verify Software Components (VSC)" in the Web Help on the LN server.
Synchronizes the modified sources with the server, and starts the compilation
using the generators and compilers on the server. Any problems that occur
during the build process are displayed in the Problems view.
The Run command enables you to run sessions from the LN Studio.
The Debug command runs a session in debug mode. You can set breakpoints
before you start the Debug command. From the debugger you can execute
various debug commands, for example: you can suspend a running session, so
that you can inspect it more closely.
See Running LN sessions on page 60 and Debugging LN sessions on page 62.
See LN Studio workbench on page 20.
Note: To use LN Studio for customizations, such as changing reports and forms, you do not need an additional
license. However, if you want to use LN Studio for development activities, such as creating new tables, editing
UI scripts, functions, or libraries, you need a development license, and if necessary source codes.
Some LN Studio functionality depends on the Enterprise Server version of the LN server.
For an example, see Application Search on page 278.
## User roles

This table shows the user roles that can be distinguished in LN Studio:
Role
Administrator
Project Manager
Description
The administrator creates and maintains the applications for which the software
projects are defined.
See the  Infor LN Studio Administration Guide.
Project managers create and maintain the software projects and activities in which
the software components are developed. The Project manager assigns each activity
to a Software Engineer.
The projects and activities are stored on the Project Server.
See Defining a software project on page 339.
Role
Software Engineer
Description
Software engineers develop software components through the LN Studio. Before
editing a component, an engineer must first open an activity that the Project Manager
assigned to him/her.
See Developing software components on page 53.
## Current scope and limitations

Currently the configuration management in LN Studio is based on the SCM module in Enterprise Server.
In future versions, the configuration management will be enhanced. In addition, database modeler and
Workflow tools will be added.
For detailed information on the limitations of the LN Studio, see LN Studio Limitations on page 75.
## Architecture

The LN Studio is implemented in the Eclipse framework.
The LN Studio workbench runs on the user's client PC (desktop).
The software components, and the Package VRCs to which they belong, reside on the LN server. The
development projects, to which the components are linked, can reside on the same LN server. However, you
can also configure a dedicated server to store the project data.
The connection between the client PC and the server(s) is based on JCA: the LN Studio connects through a
JCA connectivity plug-in on the client PC to the server.
For details on Eclipse, see the Eclipse online help and http://www.eclipse.org/.
## Troubleshooting

If you encounter any error messages, for example on connectivity, read these log files for detailed information:
- The Eclipse log files in your local workspace. To find the location of your workspace, select File > Switch
Workspace in the Eclipse workbench. The Eclipse log file is located in the .workspace\.log file in the
workspace. If LN Studio is running, you can also view the log messages in the Error Log view in LN Studio.
- The log file of the Connectivity plug-in. To find the location of this log file:
1 Select Windows > Preferences. The Preferences dialog box is displayed.
2 In the tree that is displayed in the left pane of the dialog box, expand the Infor LN JCA Connectivity
node. Then, click Log configuration. The log file location is displayed.
## LN Studio workbench

The LN Studio workbench is a desktop development environment that is based on the Eclipse framework.
You can use the workbench to perform these tasks:
- Define software projects and activities in Project Server.  Open an activity in the Activity Explorer view.
Edit components such as Sessions, Reports, and DAL scripts.  Run software components. For example, run
a session after you changed the corresponding UI script. Debug software components. Edit Business
Interfaces. Generate runtime code for Business Interfaces. Test Business Interfaces.
Perspectives, editors and views
You can open multiple Workbench windows simultaneously.
This figure shows a sample Workbench window:
In a Workbench window, you can open multiple perspectives, and you can switch between the perspectives
that you have opened. The name of the active perspective is displayed in the title of the window. See the
previous figure for an example.
A perspective contains editors and views, and controls what appears in certain menus and tool bars.
An editor is a visual component within the LN Studio workbench that is typically used to edit or browse
a resource, such as a session or a library. Modifications made in an editor follow an open-save-close life
cycle model. Multiple instances of an editor type may exist within an LN Studio workbench window.
A view is a visual component within the LN Studio workbench. It is typically used to perform these actions:
- Navigate a hierarchy of information. For example, browse the resources in the development repository.
- Open an editor.
- Show properties for the active editor.
Modifications made in a view are saved immediately. Normally, only one instance of a particular type of
view may exist within a workbench window.
These views are examples of typical LN Studio views:
- Activity Explorer
- Software Project Explorer
- Component Explorer
- Verify Components
In LN Studio, these perspectives are used:
- Application
- Debug
- Project Server
- Integration
- Integration Test
Each perspective provides a set of functionality aimed at accomplishing a specific type of task or works
with specific types of resources. For example, the Application perspective combines views that you
would commonly use while editing scripts and libraries. The Debug perspective contains the views that
you would use while debugging programs. The Integration perspective is used when developing Business
Interfaces. As you work in the workbench, you will probably switch perspectives frequently.
For details on these perspectives, see this documentation:
- Application perspective on page 296
- Debug perspective on page 297
- Project Server perspective on page 355
- Infor LN Studio Integration online help
- Infor LN Studio Integration Development Guide
Opening and switching perspectives
You can open a new perspective through the Open Perspective command on the Windows menu.
Alternatively you can use the shortcut bar in the top right corner of the window. See the following figure.
This shortcut bar allows you to open new perspectives and switch between ones already open.
The name of the active perspective is shown in the title of the window and its item in the shortcut bar is
highlighted. In this example, the LN Studio perspective is in use.
Running sessions
From the Run menu, you can run any session on the LN server.
See Running LN sessions on page 60.
Preferences
You can set various user preferences for the LN Studio workbench. For example: connectivity settings,
preferences for the editor, and label decorations.
See Setting user preferences on page 32.
More information
The LN Studio workbench is based on Eclipse.
For details on the standard Eclipse functionality, see the Workbench User Guide in the Eclipse online help.
This guide contains useful information and tutorials on various topics.
For information on the extra functionality developed by Infor, see LN Studio overview on page 15.
To access the Workbench User Guide and the LN Studio online help, select Help > Help Contents.
## Applications

This topic describes the concept of applications.
LN Studio uses applications to group software components created or modified during a software development
project. This is performed by bundling one or more LN packages.
An LN Studio application comprises a consistent set of packages that functionally belong together. Each
application is linked to a Base VRC. This determines the environment on the LN server in which the application's
software components are stored.
For each application, you can define one or more projects, in which the software engineers can develop their
software components.
The Base VRC of an LN Studio application corresponds with the Base VRC of a PMC module. Within the PMC
module, the package VRCs are linked to the Export VRC of the PMC Base VRC. Therefore, all packages assigned
to an application are linked to the Export VRC of the Base VRC of the PMC module and the other way around.
Therefore, all packages that have the same VRC as the PMC Export VRC represent one application.
This diagram illustrates the relationships between applications, packages, and VRCs:
Note: You can only delete, modify or create components belonging to the packages linked to the application.
Therefore, the Component Explorer shows the components from the packages linked to the application.
The Create a New Infor LN Software Component wizards only allow you to create new components in these
packages. This restriction also applies to the Duplicate an Infor LN Software Component wizard.
## Cloud-specific differences

In the cloud, some features may work differently or may not be available.
These are the cloud-specific differences:
- In a multi-tenant environment you cannot debug with LN Studio. You can use the Debug Workbench, see
the Debug and Profile 4GL (ttadv1123m000) session.
- You cannot start the old report layout editor because it requires an OLE connection. Instead, you must
use the report designer workbench.
- You cannot start sessions from LN Studio. Instead, you must start the sessions from LN UI.
- In a multi-tenant environment you cannot run or debug BFlows with LN Studio. You can run BFlows in
the LN UI to see the result.
