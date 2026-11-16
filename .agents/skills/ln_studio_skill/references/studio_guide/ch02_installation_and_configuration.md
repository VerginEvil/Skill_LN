# Chapter 2: Installation and configuration

## First installation

### Prerequisites

This section describes the prerequisites to run LN Studio.
Licenses
To use LN Studio, you need these licenses:
- A license for the Adapter for LN. Take care of the following:
- If you already have an Adapter for LN license for product ID 7013, you do not need a new license.
- If you do not have a license yet, obtain a license for product ID 7056.
- An LN Development license, product ID 10146. This is required if you want to create or modify tables,
domains, UI scripts, functions, or libraries. This license is also required if you want to modify and generate
Business Interface implementations.
To obtain a license, add the corresponding product ID in the Infor Solution License Manager (SLM) and request
a license for it.
Prerequisites for the LN server(s)
For the LN server the following is required:
- Infor Enterprise Server 8.5 or later.
- Infor Enterprise Server AddOn 8.5 or later.
Note: The development repository and the development projects and activities, that are defined in Project
Server, can reside on the same LN server. However, you can also configure a dedicated server to store the
project data. The prerequisites for such a dedicated project server are:
- Infor Enterprise Server 8.5 or later.
- Infor Enterprise Server AddOn 8.5 or later.
Note: On the LN server(s), the FGL_STUDIO_ENABLED environment variable must be set to 1.
Prerequisites for the client PC
Prerequisites for the client PC are as follows:
- 2 GB RAM memory (recommended)
- Microsoft Windows 7 or later
- Java Runtime Environment (JRE) 11 (Java 11), 64-bits
You can download the JRE software from the https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/
downloads-list.html website.
## Installing LN Studio

This section describes how you can install LN Studio.
> [!NOTE]
- For information on the prerequisites for the installation of LN Studio, see Prerequisites on page 25.
- Before you can install LN Studio, the system administrator must give you access to the zip file with the
LN Studio software.
To install LN Studio:
1 Create an installation folder.
Create a new folder on your machine.
The recommended installation directory is: C:\Infor\LN\LNStudio.
Note: On Windows 7 or later, do not install LN Studio in a Windows protected folder, such as C:\Program
Files or C:\Program Files (x86).
2 Open the InforLNStudio_<version number>.nnn-x86_64.zip file, which contains the LN Studio software,
and extract all contents of the file to the new installation folder.
nnn represents a build number, such as "0023".
Post installation steps
1 Select the workspace.
See Selecting the workspace on page 27.
2 Configure static connection points.
When you have installed LN Studio, you must configure these static Connection Points:
- Project Server
- Debug
See Defining connectivity settings on page 28.
3 Configure dynamic connection points.
For each LN server, on which you want to perform administrative tasks, you must configure the following
dynamic connection point:
Administrator
For each software project you develop software in, you must configure these dynamic connection points:
- Development Address
- Runtime Address
Note: You cannot define these connection points in advance. When working in LN Studio, a prompt is
displayed whenever such a connection is required, but not yet configured. At that moment a wizard to
configure the required connection point is started.
4 Configure connection points for Business Interface development.
To use interface projects, configure these connection points:
- RuntimeRepositoryConnection
- TestServerConnection
See Defining connectivity settings on page 28.
Note: These connection points are not required if the interface project is using "related software projects".
5 Define LN Studio preferences for Application development.
a Select Window > Preferences.
b In the left pane of the Preferences window, select Infor LN Studio Application. For details about
the preferences, see the "Application Preferences" section in this guide or the dialog's online help.
6 Define LN Studio preferences for Business Interface development.
a Select Window > Preferences.
b In the left pane of the Preferences window, select Infor LN Studio Integration. For details about
the preferences, see the "Integration Preferences" section in this guide or the preference page's
online help.
## Selecting the workspace

To select the workspace:
1 To start LN Studio, run the eclipse.exe executable in the LN Studio installation folder.
The Workspace Launcher dialog box is displayed.
2 Specify this information:
Workspace
The location of the workspace. The workspace is the directory, usually on your own PC, where your work
is stored.
It is discouraged to locate the workspace in the directory where the LN Studio software or the Eclipse
software is installed. It is better to select a different directory, for example under C:\data. This results
in a better overview of the directory structure on your desktop, and makes the workspace independent
of the versions of the LN Studio and Eclipse software.
Use this as the default and do not ask again
Select this check box to prevent that the Workspace Launcher dialog box is displayed again.
3 Click OK.
4 Allow installation of BW and Dynamic Form Editor.
LN Studio requires Infor BW activation for the development and runtime addresses. LN Studio also
requires the Infor LN Dynamic Form Editor (DFE) to develop session forms.
If BW and DFE are not installed on your computer, or older versions are installed, an automatic installation
of these components is performed when you start LN Studio for the first time.
If User Account Control (UAC) is enabled, confirmation dialog boxes are displayed during the BW and DFE
installations: you are prompted to allow the BW and DFE setup programs to make changes to your
computer.
Click Yes in both dialog boxes.
A single Workbench window is displayed.
Note: If you want to select another workspace after the Workbench is started, select File > Switch Workspace
> Other.
## Defining connectivity settings

This section describes the procedure to define connectivity settings for the LN Studio.
Infor LN Studio uses Connection Points to connect to the LN server that contains the LN applications and the
development repository, and to the server on which the software projects are stored.
This table shows the static connection points you must configure to define the connectivity settings:
Connection
Description
This connection point is used to connect to the Project Server. The Project Server contains
projects and activities that are used in the Infor LN Studio.
The Project Server connection point is used, for example:
- When a project manager creates a new project, or a new activity in the Software Project
Explorer view. When a software engineer starts the Open an Activity wizard from the
Activity Explorer view.
Debug When a software engineer debugs a session from the LN Studio, the debugger on the
LN server uses this connection point to send messages to the LN Studio on the client PC.
RuntimeRepositoryConnection This connection point is used for exchanging business
metadata with the application server. This connection is not required if the interface project
is using "related software projects". TestServerConnection This connection point is used
when testing Business Interface implementations. This connection is not required if the interface project is using "related software projects".
point
ProjectServer
Configuring static connection points
To configure the connection points:
1 Display the standard connection points
a On the Eclipse Windows menu, select Preferences. The Preferences dialog appears.
b In the tree that is displayed in the left pane of the dialog, select Infor LN JCA Connectivity. The Infor
LN JCA Connectivity dialog is displayed. The dialog shows the standard Debug and Project Server
connection points, which were defined by LN Studio by default.
The Infor LN JCA Connectivity dialog is part of the connectivity plug-in. For details, see the dialog's
online help and to the online help of the Infor Connectivity plug-in.
2 Configure the connection points
To configure a connection point, select the connection point and click Edit. The Configure Connection
point wizard starts. Specify the properties for the connection points and close the wizard.
This table shows points of attention per static connection point:
Points of attention
Select the appropriate activation type:
- To connect to an on-premises installation of LN, select the BW, Rexec, or Baan-
Login activation type, and specify the corresponding settings.
- To connect to a multi-tenant cloud installation of LN, specify the HTTP-OAuth2
activation type after setting up a "Cloud Environment".
To connect to a single-tenant cloud installation of LN, specify the HTTP-Basic
activation type.
See "Specifying additional settings for cloud development".
The company number for this connection point must be 000.
The application and project data accessed through these connection points can
reside in the same LN environment. If so, you can share these connection points.
As a result, only one bshell is used to connect to the server, instead of two, which
improves the performance.
Debug
Select a free local port number, such as 10100.
RuntimeRepositoryConnection
The company number for this connection point must be 000.
TestServerConnection
Connection point
ProjectServer
Select the Socket-In activation type.
Select the BaanLogin (recommended), Rexec, or BW activation type, and specify the
corresponding settings.
Select the BaanLogin (recommended), Rexec, or BW activation type, and specify the
corresponding settings.
The Configure Connection point wizard is part of the connectivity plug-in. For details, see the wizard's
online help and the online help of the Infor Connectivity plug-in.
> [!NOTE]
- You can use the Preferences dialog box to set various other user preferences for the LN Studio workbench.
See "Application preferences", "Integration preferences", and "Connectivity preferences" in the  Infor
LN Studio Administration Guide.
- To run or debug sessions after creating or modifying the Debug connection point, you must restart LN
Studio.
- In a multi-tenant environment you cannot debug with LN Studio. You can use the Debug Workbench, see
the Debug and Profile 4GL (ttadv1123m000) session.
- In a multi-tenant environment you cannot run or debug BFlows with LN Studio. You can run BFlows in
the LN UI to see the result.
## Defining dynamic connection points

Dynamic connection points
LN Studio uses the following dynamic Connection Points:
Dynamic connection point
Administrator
dress
Runtime Address
Configuration
Enables you to perform administrative tasks on the LN Configure this connection
point for each LN server, on
which you want to perform
administrative tasks or devel-
- When an administrator defines a new application
opment tasks.
from the Application Explorer.
- When a Project Manager links a project to the corresponding application (through the Project
Properties dialog).
Configure these connection
points for each software
project, in which you develop software.
- checks out, or checks in a software component.
- edits a script or library.
- builds (compiles) a session.
Sends information to the LN server when you run or
debug a session from the LN Studio.
Description
server.
The connection point is used, for example:
Development Ad- Is used to connect to the development repository on
the LN server.
This connection point is used, for example, when a
software engineer:
You are prompted to configure these connection points, the first time you open an activity linked to the
software project. See the following section.
Configuring dynamic connection points
To configure the dynamic connection points mentioned, complete the following steps:
1 Select the project
Complete these steps:
a Open the Application perspective: On the Windows menu, select Open Perspective, and
subsequently click Other. Select Application from the list and click OK.
b In the Activity Explorer view, click Open an Infor LN Studio Activity. The Open an Activity dialog
box is displayed.
c Select the software project from the list. A question window is displayed: you are prompted to
configure the corresponding Administrator connection point.
Note: This question is displayed only the first time you open an activity for the project.
2 Configure the Administrator connection point
Complete these steps:
a In the question window, click Yes. The Configure Connection point wizard starts.
b Specify the properties for the connection point.
Points of attention:
- To connect to an on-premises installation of LN, select the BW, Rexec, or BaanLogin activation
type, and specify the corresponding settings.
To connect to a multi-tenant cloud installation of LN, specify the HTTP-OAuth2 activation type.
To connect to a single-tenant cloud installation of LN, specify the HTTP-Basic activation type.
- Select company number 000.
- The application and project data can reside in the same LN environment. If so, you can share
the Administrator and ProjectServer connection points. As a result, only one bshell is used to
connect to the server, instead of two. This improves the performance.
See the wizard's online help.
c To save the connection point and to close the wizard, click Finish. A question window is displayed:
you are prompted to configure the Development Address and Runtime Address connection points.
3 Configure the Development Address and Runtime Address connection points
Complete these steps:
a In the question window, click Yes. The Configure Connection point wizard starts and automatically
generates these connection points:
- <project name>_dev (Development Address)
- <project name>_rt (Runtime Address)
b Specify the properties for these connection points.
Points of attention:
- Development Address
- To connect to an on-premises installation of LN, select the BW activation type and specify
the corresponding settings.
To connect to a multi-tenant cloud installation of LN, specify the HTTP-OAuth2 activation
type.
To connect to a single-tenant cloud installation of LN, specify the HTTP-Basic activation
type.
- The company number for this connection point must be 000.
- Runtime Address
- To connect to an on-premises installation of LN, select the BW activation type and specify
the corresponding settings.
To connect to a multi-tenant cloud installation of LN, specify the HTTP-OAuth2 activation
type.
To connect to a single-tenant cloud installation of LN, specify the HTTP-Basic activation
type.
- A runtime address is always linked to a particular company number, such as company 100,
on the LN server.
If the development repository and the application data accessed through these connection points
reside in the same LN environment, you can share these connection points. As a result, only one
bshell is used to connect to the server, instead of two. This improves the performance.
See the wizard's online help.
c To save the connection point and to close the wizard, click Finish.
You can now open an activity for the project.
Modifying existing connection points
To modify the configuration properties of existing connection points:
1 Select Windows > Preferences. The Preferences dialog box is displayed.
2 In the tree in the left pane of the dialog box, select Infor LN JCA Connectivity. The Infor LN JCA
Connectivity dialog box is displayed. The dialog box shows the connection points. See the dialog box's
online help.
3 To configure a connection point, select the connection point and click Edit. The Configure Connection
point wizard starts. Modify the properties for the connection point and close the wizard.
## Setting user preferences

You can use the Preferences dialog box to set various user preferences.
To set preferences:
1 Select Window > Preferences.
The Preferences dialog box is displayed. This dialog box contains several preference pages.
2 Specify your preference settings. To open a preference page, select the corresponding item in the tree
structure in the left pane of the Preferences dialog box.
This table shows the preference pages that are relevant for the Application perspective:
Item in menu structure in the left pane
Infor LN JCA Connectivity
Preference page
Infor LN JCA Connectivity
This page is part of the connectivity plug-in. See the
page's online help.
Log configuration
This page is part of the connectivity plug-in. See the
page's online help.
Item in menu structure in the left pane
Infor LN Studio Application
Team
Preference page
Preferences - Editor
Preferences - Code Assist
Preferences - Folding
Preferences - Syntax
Preferences - Templates
Preferences - Launching
Preferences - Multipage
Preferences - Workbench
Preferences - Infor LN Configuration Management
Other preferences
The Preferences dialog box also contains preference pages for the Integration perspective in LN Studio. See
the documentation for the Integration perspective.
For information on the other preference pages, see "Preferences" in the "Reference" section in the Workbench
User Guide, or use the online help function (F1) in the pages.
Specifying additional settings for multi-tenant cloud
development
You can connect to an LN installation in the cloud. To achieve this, you must set up an HTTPS connection to
an LN UI server where the LN Client Service is enabled. The required authorization settings are usually stored
in a .ionapi file. Your administrator can distribute this file in multiple ways:
- Send the file by email.
- Publish the file on a network share or on an HTTP server in your local intranet.
The settings in the .ionapi file are used to define a "Cloud Environment".
Adding a cloud environment
1 Select Window > Preferences.
2 In the tree in the left pane of the dialog box, expand Infor LN JCA Connectivity and select Cloud
Environments.
3 Click Add. The Configure Cloud Environment wizard starts.
4 If the .ionapi file is present on your file system or on a network share, select Import from file. Then click
Browse to locate the .ionapi file. Alternatively, specify the path to the .ionapi file directly in the text
box.
If the .ionapi file is published on an HTTP server, select Import from URL and specify the URL to the file.
5 Click Import. The remaining fields on the wizard page are filled with settings from the .ionapi file.
6 Optionally, change the Environment Name. Leave the rest of the settings unchanged. Tip: copy the value
of the Gateway URL to the clipboard; you need this later on.
7 Click Finish.
Adding a server certificate to the trust store
Because you are creating a Secure HTTPS connection to LN UI, LN Studio must know whether the server is
trusted. Therefore, you must register the trusted server certificates in a trust store. The trust store is a file in
"Java Key Store" format. This file contains a "global" configuration that is valid for all workspaces. Therefore,
the file is located outside of the LN Studio installation folder, and outside of the workspace folder. A good
location is your "home folder".
To add a server certificate to the trust store:
1 Select Window > Preferences.
2 In the tree in the left pane of the dialog box, expand Infor LN JCA Connectivity and select Trusted SSL
Certificates.
3 If you do not yet have a trust store, complete these steps:
a Click Browse. Browse to the folder where you want to create the trust store, such as C:\Users\<Your
Name> .
b Specify the file name. Use a .jks extension for the file name. For example, specify
LNStudioTrustStore.jks.
c To complete the browse dialog box, click Open or press Enter.
4 Optionally, specify a password for the trust store. If you leave the field blank, a default password is used.
5 Click Apply. If the trust store did not yet exist, you are prompted whether you want to create a new one.
Click Yes.
6 The certificates in the chosen trust store are listed in the Certificates table, and the Add button is enabled
now. If you have a copy of the certificate in a file, you can click Add to add that certificate. Usually, this
is not the case, so you must use another way.
7 In the Check Trusted URL field, specify the HTTPS URL of the LN UI server you want to use. You can go
back to the Cloud Environments preference page, select the configured cloud environment, click Edit,
and copy the Gateway URL. The Gateway URL is the first part of the URL to the LN UI server.
8 Click Check. Usually, a "Check failed" dialog, which suggests to import the certificate presented by the
server, is displayed. Click Yes. The Import Certificate dialog box is displayed.
9 In the Import Certificate dialog box, the Server Certificates drop-down list may contain more than one
certificate.
The HTTPS server presents a chain of certificates, starting with its own certificate. Next is the certificate
of the Certification Authority (CA) that issued the server certificate, followed by the issuer of the CA
certificate, and so on. The last certificate in the chain is usually a "root CA certificate", issued by itself.
You must import the last certificate. This certificate is already selected in the drop-down list. Details of
the selected certificate are displayed in the dialog box.
10 In the Alias field, specify a short name for the certificate. This alias is stored in lower case in the trust
store. Click Finish. The certificate is now present in the Certificates table.
11 Click Check again. A "Check succeeded" dialog box is displayed.
12 Click OK. The Preferences dialog box is closed.
Configuring connection points
You must configure these connection points:
- The static connection point for the Project Server
- The dynamic connection points for Administrator, Development Address, and Runtime Address.
These connection points must use an HTTPS connection to an LN UI server that provides access to an LN
environment in the cloud.
Example - Project Server connection point
For example, to configure the Project Server connection point:
1 Select Windows > Preferences.
2 Select Infor LN JCA Connectivity.
3 In the table with connection points, select ProjectServer and click Edit. Alternatively, double-click the
row with ProjectServer. The Configure Connection point wizard starts.
4 In the Activation Type drop-down list, select HTTP-OAuth2 and click Next.
5 Select the correct Cloud Environment from the drop-down list.
6 The Service Endpoint URL is automatically filled with the URL for the LN UI server.
7 For a project server connection, ensure the Company field contains 0.
8 To complete the configuration, click Finish.
9 To test the connection, select the connection point and click Ping. A dialog box containing a login page
is displayed. During normal usage of LN Studio, this login page is displayed the first time a connection
to the cloud is established.
Follow the instructions on the page. These instructions are provided by the authorization server of the
cloud. If everything is okay, the connection test succeeds. If the test fails, errors are reported: the
configuration is incorrect, or you specified invalid credentials on the login page.
Specifying additional settings for single-tenant cloud
development
You can connect to an LN installation in the cloud. To achieve this, you must set up an HTTPS connection to
an LN UI server where the LN Client Service is enabled.
Configuring connection points
You must configure these connection points:
- The static connection point for the Project Server
- The dynamic connection points for Administrator, Development Address, and Runtime Address
These connection points must use an HTTPS connection to an LN UI server that provides access to an LN
environment in the cloud.
Example - Project Server connection point
For example, to configure the Project Server connection point:
1 Select Windows > Preferences.
2 Select Infor LN JCA Connectivity.
3 In the table with connection points, select ProjectServer and click Edit. Alternatively, double-click the
row with ProjectServer. The Configure Connection point wizard starts.
4 In the Activation Type drop-down list, select HTTP-Basic and click Next.
5 In the Service Endpoint URL field, specify the URL for the LN UI server. Your administrator can supply
the correct value.
The LN Client Service should be enabled. For details on how to enable the LN Client Service, see the Infor
LN UI Administration Guide.
6 In the LN UI Environment field, specify the name of the environment as defined on the LN UII server.
Your administrator can supply the correct value.
7 For a project server connection, ensure the Company field contains 0.
8 Leave the Command field blank, unless your administrator has instructed otherwise.
9 In the User and Password fields, specify the correct values.
10 To complete the configuration, click Finish.
11 To test the connection, select the connection point and click Ping.
## Installing LN Studio updates

This section describes how you can install updates for LN Studio.
Note: Before you can install updates, the system administrator must provide a new LN Studio zip file.
To install updates:
1 Open the InforLNStudio_<version number>.nnn-x86_64.zip file, which contains the new software.
nnn represents a build number, such as "0023".
2 Extract all contents of the file to your existing LN Studio installation folder, such as C:\Infor\LN\LNStudio
. Ensure the Overwrite existing files check box is selected!
