# Chapter 7: Version and Release Management

## Version and release management introduction

This section describes LN ’s version and release management, which manages the various versions of
the LN packages, their corresponding releases, and customizations.
## An overview of version and release management

Software is constantly changing. Therefore, you must manage various versions of packages,
corresponding releases, and all the various customizations on the standard software. Infor Enterprise
Server offers a comprehensive solution with a version and release management concept.
Advantages of the version and release concept are the following:
- A flexible development environment
- Flexible management of the following:
- New versions of the software
- Patches on the software
- Customizations on the software
- Localizations for the software
- Developers can create and test the customizations on the standard software in a separate
- Operational users will not see new or customized software components until the components
development environment.
are fully tested and released in their own run-time environment.
### Package combinations

A package combination is a collection of various LN packages. Every package combination has a unique
VRC. The package combination links users to a specific version of the LN software. A package
combination can be linked to one or more users and to one or more companies. However, a package
combination can contain only one version of a package, which is identified by a package VRC.
The following figure shows an example of a standard package combination:
Example of a software environment with a standard package combination
This figure shows an example of a standard package combination, which contains a number of standard
package VRCs, such as the standard version of LN Financials.
### Package VRCs

Each LN package is distributed as a package VRC, which represents a specific version of that package.
VRC stands for version release customer code, and it identifies the development stage of the LN software.
A VRC consists of the following:
- A version code that identifies a major LN software modification
- A release code that identifies a minor LN software modification
- A customer extension code that identifies LN software for a specific customer
A package, for example, LN Financials, can have more than one version. Each version is identified by
a specific package VRC. For example, LN Financials can have a package VRC that contains the standard
software of LN Financials and a package VRC that contains the customizations on the standard software
of LN Financials.
As a rule, a new package VRC is derived from a previous package VRC. To avoid duplication of software
components, a new VRC only contains those software components that have changed compared to
previous VRCs.
The following figure shows an example of the VRC derivation structure:
An example of a VRC derivation structure
In this example, B61_a is the VRC that contains the standard software. The following two new VRCs
are derived from this VRC:
- The VRC B61C_a_cus1 contains a customized version of the standard software
- The VRC B61_b contains a new version of the standard software. From this new standard
- B61C_b_cus1
- B61C_b_cus2.
VRC, two new customized versions are derived:
The VRCs B61C_b_cus1 and B61C_b_cus2 contain several customizations on the B61_b
standard version.
### Package VRC code

A unique identifier identifies package VRCs in LN. LN uses the following format to identify package
VRCs, the codes of which are described in the following table:
pp vvvt_rr_gggn
Code
Description
pp
Package code
vvv
Version code
t
Type code.
Denotes customizations on standard software. This
field is not filled for the standard software. Possible
type codes include the following:
- L Localizations: Customizations for a specific
- B Branch: Customizations for a specific line
- C Customer: Customizations ordered by the
- O Own: Customizations developed by the
country.
of business.
customer, developed by a dealer or partner.
customer.
rr
Release code
ggg
Customer code: This field is not filled for the standard software.
n
Sequence code
For example, for the Strangely Brown Chicken company (SBC), the package VRC tc B61O_b_sbc1
represents the first customization on the standard software in the B61_b VRC of LN Common.
> [!NOTE]
Customers can only create new VRCs for their own customizations from the standard software. Infor or
a partner delivers all other VRC types.
## LN software environment

To create specific software environments, you can use package combinations.
A software environment consists of:
- A package combination
- At least one company
You can create a special package combination to customize software components or to create new
software components.
This table shows the software environments in LN:

Software environmen tDescription
### Standard environment

A package combination that contains the standard version of all LN packages.
### Runtime environment

A package combination that contains the package VRCs that normal users
use at runtime.
### Development environment

A package combination that contains package VRCs in which developers
can create customizations.
### Standard environment

The standard environment contains the standard software of all LN package VRCs of all LN packages.
You can use the standard environment to compare customized software with standard software.
This diagram shows an example of the standard environment.
### Standard environment

This diagram shows an example of a user who is linked to a specific package combination. Use the
User Data (ttaad2500m000) details session to link the user to a package combination.
### Runtime environment

A runtime package combination can contain some package VRCs that are derived from standard package
VRCs. However, not all packages in the package combination have to have the same package VRC. If
no customizations exist for a certain package, the standard VRC of this package is used in the run-time
package combination. For example, the Service and Maintenance package (tsB61_a) in the following
figure is not customized. The other packages are customized and for these the derived package VRC
is used in the package combination.
To specify that the package combination is customer defined, make sure you add not only the customer
extension (cus) but also the extension O. This letter indicates that the package combination is the
customer’s own.
This diagram shows an example of a runtime environment.
Run-time environment
### Development environment

As in the run-time environment, a package combination in a development environment contains package
VRCs that are derived from standard package VRCs. Also, not all packages in the package combination
must have the same package VRC. If no customizations exist for a certain package, the standard VRC
of this package is used in the run-time package combination.
Developers use a development environment to develop new software components or to change existing
components.
This diagram shows an example of a development environment:
The development environment
The name of this package combination, such as the previous one, contains the character O. In this case,
the customer extension is replaced by the extension dev, which stands for development.
### VRC derivation

If a user starts a software component, for example a session, the Virtual Machine (VM) searches from
the outside to the inside, as shown in the following figure. The Virtual Machine (VM) searches for any
customizations on the component made by the customer in the own customization. If no own
customizations exist, the Virtual Machine (VM) searches for a customer-specific customization, and so
on.
The following figure shows how the Virtual Machine (VM) navigates through the customizations on a
component.
Navigation of the Virtual Machine (VM) through the VRC structure
The search path also depends on the package combination and company to which the user is linked.
For example, the package VRCs in a development package combination are derived from the VRCs in
the run-time package combination, these run-time package combinations were, in turn, derived from
standard package VRCs.
The following figure shows the derivation structure of the development package combination.
Package VRC derivation structure
In this previous figure, the VRCs with customer extension dev are derived from the VRCs with the cus
extension, which themselves are derived from standard VRCs. If a user works with package combination
b61O_a_cus and starts a software component, the Virtual Machine (VM) searches for a customization
in the VRC with the cus extension. If such a customization is found, this customized component is started.
If no such customization exists, the component in the standard VRC is started.
If a user works with package combination b61O_a_dev and starts a software component, the Virtual
Machine (VM) searches for a customization in the VRC with the dev extension. If no such customization
is found, the Virtual Machine (VM) continues the search in the cus VRC. If this VRC also does not contain
a customized version of the component, the Virtual Machine (VM) starts the component in the standard
VRC.
If you create many package VRCs, derived from each other, the derivation structure can get complicated.
The consequences of a cluttered and complicated VRC derivation structure are:
- A decrease in system performance due to the longer derivation structure
- A cluttered directory structure due to a large number of newly-created package VRCs
For this reason, you must regularly purge the VRC derivation structure. Before you can purge a package
VRC, you must make sure that the VRC is not connected to a package combination. You can disconnect
the package VRC from a package combination with the Packages by Package Combination
(ttaad1121m000) session.
> [!NOTE]
If you purge a package VRC, the derived-from structure changes. The user files and fd6.2 files, for the
involved users and package combinations, are automatically regenerated so that they contain the new
derived-from structure.
The following figure provides an example of a package VRC derivation structure before and after the
purge:
Package VRC derivation structure before and after the purge procedure
Typically, only customer-defined VRCs are purged that contain customized software components that
do not belong to a package combination. However, you can also purge the package VRCs that contain
the standard software.
For example, the following figure shows the derivation structure of the package VRCs that contain the
standard software of the LN Common package. A new standard can contain new functionality, feature
packs, bug fixes, and so on.
A new standard is put on top of its predecessor, so software components can be duplicated. Therefore,
you must purge the standard package VRCs regularly to remove the duplications.
Derivation structure of the LN Common package
The maximum VRC depth, in other words, the number of VRC that you can stack on top of each other,
is 40 VRCs. However, for best results, keep the maximum VRC depth as low as possible.
## Contents of a software environment

After you create a software environment, you must fill the environment with software components. In a
single-system environment, you can copy the software components from another environment to your
new environment. In a multisystem environment, you can use LN ’s export/import tool.
## Copy software components concept

You can copy software components from one software environment to another. For example, you can
customize software components in a dedicated development environment and then copy the components
to a new run-time environment or to an environment that is already in use.
If you copy the software components into another environment, you must compile the components in
the new environment and then convert the components to the new environment’s run-time data dictionary.
The result of this example is that normal users can use the released software components without the
need to create new package VRCs or package combinations. Developers can continue to create
customizations on the standard software components in their dedicated development VRC.
The components that are copied into a new runtime environment are positioned at a higher level. For
example, components that are copied from the package VRC tfB60O_b1 into the new run-time
environment are placed in the package VRC tfB60O_b2.
For more information, refer to the Copy software components procedure (p. 148) .
## Export/import software components concept

You can export software components of a package VRC to sequential files. You can import these files
into a package VRC in another environment. If you have imported the software components into another
environment, you must convert them to the runtime data dictionary of the new environment.
The following figure shows an example of the export/import procedure:
Example of the export/import procedure
Use the export/import method to fill an environment in a multisystem environment. The sequential files
that contain the exported software components are sent from one system to another by means of File
Transfer Protocol (FTP), a CD-ROM or by e-mail.
The following figure shows the import/ export concept in a multi-system environment:
Import/export procedure in a multi-system environment
FTP is a protocol used to copy files to and from remote computer systems on a network using TCP/IP,
such as the Internet. This protocol also enables you to use FTP commands to work with files, such as
listing files and directories on the remote system.
For more information, refer to the Export and import procedure (p. 149) .
To use the Software Configuration Management system
(SCM)
Developers can use the Software Configuration Management System (SCM) to make a copy of the
software component and place the component into a dedicated development VRC. The component can
then be modified, for example, to fix a bug. If the component is finished and tested, the component can
be placed back into the run-time environment. This process is called the check-out and check-in process.
The component can still have the same VRC code, but it has a different revision number. Older revisions
of the component are still retrievable.
During the check-out period:
- the original version is still available for the regular users in the run-time environment.
- other users cannot modify or check-out the original version.
- other users can test the checked out component. Refer to SCM Groups for details.
The following figure shows LN ’s Software Control Management (SCM) concept:
LN ’s Software Configuration Management (SCM) concept
SCM controls only the revisions of components in one VRC. If a component is copied to another VRC,
the revision information is no longer available.
> [!NOTE]
There is a fundamental difference between copying software components in a new run-time environment
and copying components into a development VRC with LN ’s SCM tool. The components, which are
copied into a development VRC with the SCM tool, are positioned at the same level as the original and
have the development extension code, for example, tfB60O_b1_dev. This process is known as the
check-in and check-out process.
The following figure shows the relation between the SCM procedure and the copy procedure.
Relation between the SCM procedure and the copy procedure
> [!NOTE]
SCM only supports configuration management for the main component types such as Forms, Sessions,
Table Definitions, Reports, and Functions. The 4GL component types, such as Labels, Questions, and
Messages, are not supported.
SCM makes use of the RCS software on the LN Server. Revision Control System (RCS) is freeware
software. For more information on SCM, refer to Software Configuration Management in the Infor
Enterprise Server Web Help. For details on RCS, refer to http://www.gnu.org/software/rcs/rcs.html .
In earlier versions of Infor Enterprise Server, SCM is only available on UNIX platforms. From version
8.4.2 you can also activate SCM on Windows platforms. For details, refer to solution 230630.
## SCM Groups

In SCM groups, developers can share their checked-out runtime components, so they can test each
other's components, but they cannot change them.
When you start using SCM, the system automatically generates an SCM group for you. The name of
your SCM group is identical to your user name.
Normally, you can only access components that belong to your own SCM group.
To test a component that belongs to another SCM group (a component that was checked-out by another
developer), you must modify your login configuration:

1. Open you Windows Client configuration (.bwc file).
2. In the Command field of the BW Configuration Properties dialog box, fill the
BAAN_SCM_GRP variable with the name of the desired SCM group. For example, specify
-- -set BAAN_SCM_GRP = peter to test software components that belong to SCM group
"peter".
3. Log in using the new configuration.
To return to your own SCM group: log off, remove the -- -set BAAN_SCM_GRP = .... setting from your
Windows client configuration, and log in again.
## To set up the SCM environment

Take the following steps to activate SCM for a VRC:

1. Start the Package VRCs (ttadv1511m000) session, and create a development VRC. The new
VRC must be derived from the original VRC. See the previous figure for an example: the
tfB60O_b1_dev development VRC is derived from the tfB60O_b1 original VRC.
2. Start the (De)activate SCM and Component Management by Package VRC (ttscm0501m000)
session. Select the original VRC (e.g. tfB60O_b1) and click Activate SCM (and CM) on the
context menu.
3. The Activate SCM and Component Management by Package VRC (ttscm0110s000) session
is started automatically. Select the desired development VRC and click OK.
4. Log off and log in again to make the changes effective.
Repeat these steps for each VRC for which you want to activate SCM.
## Sessions

The following sessions can be started from the Software Configuration Management (SCM) menu:
- (De)activate SCM and Component Management by Package VRC (ttscm0501m000)
- Global Check-In of Components (ttscm1200m000)
- Delete Component Revisions (ttscm1201m000)
- Global Undo Check-Out of Components (ttscm1202m000)
- Copy/Move Checked Out Components (ttscm1203m000)
## To use the SCM check-in and check-out procedure

This topic describes how to maintain software components if SCM (Software Configuration Management)
is activated. For details on SCM, refer to To use the Software Configuration Management system (SCM)
(p. 142) .
## Procedure

To maintain a software component:

1. check out the software component from the original VRC to a development VRC. To do this,
on the appropriate menu click Check-Out, or click the corresponding button.
2. If the changes on the software component are tested and completed, check-in the component,
so that the changes are made available to other users. To do this, on the appropriate menu
click Check-In, or click the corresponding button.
> [!NOTE]
This procedure only applies to the main component types such as Program Scripts/Libraries, Forms,
Sessions, Table Definitions, Reports and Functions. SCM does not support the 4GL component types
such as Labels, Questions, and Messages.
The Check-Out and Check-In commands are available in the sessions that are used to maintain these
main components, such as Reports (ttadv3530m000) and Sessions (ttadv2500m000).
On the appropriate menu of these sessions, you can select Revisions to start the Component Revisions
(ttscm1501m000) session, to view and maintain a component's revisions.
If necessary the procedure can be reversed by using the undo check-out procedure. To do this, on the
appropriate menu click undo check-out.
> [!IMPORTANT]
- You can only check-out components that are stored in the original VRC, that is: the VRC from
- Make sure that the original VRC is selected as your current VRC, not the development VRC.
- If the component is not present in the original VRC, you must first copy it to the original VRC.
which the development VRC is derived.
Select Change Current package VRC of User in the appropriate menu to change the current
VRC.
## Standard software environment procedure

### Procedure aim

In this procedure, a software environment is created that you can use to create your own customized
software for LN. The environment contains a dedicated package combination and package VRCs for a
customization department.
### Procedure result and prerequisites

#### Result

A new software environment with package combinations and package VRCs.
#### Prerequisites

Make sure that you have at least 10 MB free disk space and 40 MB database space available.
This section describes only the most important steps in the standard software environment procedure.
For detailed instructions on how to enter data in the sessions that are mentioned in the procedure steps,
refer to the session help.
> [!NOTE]
You can use the procedure on both UNIX and Windows platforms. You can use the ${BSE} notation for
both platforms, as well as for the slash (/) and backslash (\) characters.
Points of attention
Points of attention for the package combination:
- The new package combination must contain a VRC for each package, except Tools (tt) and
- The Data Director (da), OpenWorld Middleware-enabling (tm), and New Technology (nt) must
Tools Add-on (tl):
not be customized. Therefore, you must include existing (not your own!) VRCs for these
packages. For example, include the highest update or localization VRC in the derivation
structure.
- For the remaining packages (except tt and tl) you must include your own VRCs.
### Procedure summary

The following list shows the procedure steps and the corresponding sessions.

1. Create new package VRCs - Package VRCs (ttadv1511m000)
2. Create new directories for the software components of the new package VRCs - Directories
of Software Components (ttadv1115m000)
3. Create a new package combination - Package Combinations (ttaad1520m000)
4. Link package VRCs to the new package combination - Packages by Package Combination
(ttaad1121m000)
5. Link companies to the new package combination - Change Package Combination by Company
(ttaad1101m000)
6. Link users to new package combination - Change Package Combinations for Users
(ttaad2200m000)
7. Change the authorizations for the developers - Developer Authorization Template
(ttams1151m000)
8. Optionally: Initialize Test tool for Business Data Entities (BDEs) - Initialize Tools
(tlcom0200m000)
9. Authorize normal users for a new or other environment - User Data (ttaad2500m000)
## One-step software environment procedure

### Procedure aim

In this procedure, a software environment is created that you can use to create your own customized
software for LN. The environment contains a dedicated package combination and package VRCs for a
customization department.
You cannot use this procedure to maintain existing environments. To maintain existing environments,
you must use the sessions discussed in the Standard software environment procedure (p. 145) . The
prerequisites for and result of this procedure are identical to those of the Standard software environment
procedure.
### Procedure result and prerequisites

#### Result

A new software environment with package combinations and package VRCs.
#### Prerequisites

Make sure that you have at least 10 MB free disk space and 40 MB database space available.
This section describes only the most important steps in the one-step procedure. For detailed instructions
on how to enter data in the sessions that are mentioned in the procedure steps, refer to the session
help.
> [!NOTE]
You can use the procedure on both UNIX and Windows platforms. You can use the ${BSE} notation for
both platforms, as well as for the slash (/) and backslash (\) characters.
Points of attention
Points of attention for the package combination:
- The new package combination must contain a VRC for each package, except Tools (tt) and
- The Data Director (da), OpenWorld Middleware-enabling (tm), and New Technology (nt) must
Tools Add-on (tl):
not be customized. Therefore, you must include existing (not your own!) VRCs for these
packages. For example, include the highest update or localization VRC in the derivation
structure.
- For the remaining packages (except tt and tl) you must include your own VRCs.
### Procedure summary

The following list shows the procedure steps and the corresponding sessions.

1. Create the software environment - Create New Package Combination / VRCs (One Step)
(ttaad1222m000)
2. Optionally: Initialize Test tool for Business Data Entities (BDEs) - Initialize Tools
(tlcom0200m000)
## Copy software components procedure

### Procedure aim

An environment must be filled with software components. To fill a new environment with software
components, you can select components from an already existing environment and copy them into the
new one.
### Procedure result and prerequisites

#### Result

Normal users, for example, can use the new environment as a run-time environment. Developers can
also use this environment as a development environment to create new components or to customize
existing components.
#### Prerequisites

Make sure that the environment is created successfully. You can create an environment through the
Standard software environment procedure (p. 145) , or through the One-step software environment
procedure (p. 147) .
The copy software components procedure is usually used for a single system environment. If you use
more systems, use the Export and import procedure (p. 149) .
### Procedure summary

The following list shows the procedure steps and the corresponding sessions.

1. Copy components in a software environment - Copy Software Components to New Package
VRC (ttadv6265m000)
2. Create the run-time data dictionary for labels- Compile Labels (ttadv1243m000)
3. Create the run-time data dictionary of the components in the target package combination-
Create Runtime Data Dictionary (ttadv5210m000)
4. Compile the program scripts and library scripts of the copied components - Compile Program
Scripts / Libraries (ttadv2230m000)
5. Compile the reports of the copied components - Compile Reports (ttadv3240m000)
6. Create the run-time data dictionary of the forms and menus - Create Runtime Data Dictionary
(Forms and Menus) (ttadv5214m000)
7. Install Infor Web Help for the components in the target environment
## Export and import procedure

With the import/export procedure, the software components in a package VRC are exported to sequential
files and imported into a package VRC in another environment. If you import the software components
into another environment, you must convert them to the runtime data dictionary in the new environment.
### Procedure aim

An environment must be filled with software components. You can use the export/import procedure to
fill an environment with software components.
### Procedure result and prerequisites

#### Result

The process results in a new environment that normal users, for example, can use as their runtime
environment. Developers can also use this environment as a development environment to create new
components to customize existing components.
#### Prerequisites

Make sure that the environment is created successfully. You can create an environment through the
Standard software environment procedure (p. 145) , or through the One-step software environment
procedure (p. 147) .
### Procedure summary

The following list shows the procedure steps and the corresponding sessions.

1. Export components from a software environment to sequential files - Export Data Dictionary
(ttiex1280m000)
2. Only if the source and the target environments are located on different systems: transfer the
sequential files to the target system
3. Import components from the sequential files into the target environment - Import Data Dictionary
(ttiex1285m000)
4. Create the run-time data dictionary for labels- Compile Labels (ttadv1243m000)
5. Create the run-time data dictionary of the components in the target package combination-
Create Runtime Data Dictionary (ttadv5210m000)
6. Compile the program scripts and library scripts of the copied components - Compile Program
Scripts / Libraries (ttadv2230m000)
7. Compile the reports of the copied components - Compile Reports (ttadv3240m000)
8. Create the run-time data dictionary of the forms and menus - Create Runtime Data Dictionary
(Forms and Menus) (ttadv5214m000)
9. Install Infor Web Help for the components in the target environment
> [!NOTE]
The compilation of program scripts/libraries and reports, and the creation of the runtime dictionary for
forms and menus is only necessary if you did not export objects/dumps for these components.
## Purge a package VRC derivation structure procedure

### Procedure aim

If you create many own package VRCs, derived from each other, the derivation structure can get very
long.
The consequences of a cluttered VRC structure are:
- A decrease in system performance due to the longer derivation structure
- A cluttered directory structure due to a large number of newly-created package VRCs
The maximum depth of the package VRC tree is 40. Purging a package VRC reduces the depth of the
package VRC tree, which makes it possible to add a new package VRC to the tree.
When you purge a package VRC:
- software components that are no longer used, for example, because of a new customization
- The components that are still in use are copied to the package VRC that is derived from the
on the same component in a more recent package VRC, are deleted.
purged VRC.
### Procedure result and prerequisites

#### Result

As a result of this procedure, a shorter derivation structure is created and, therefore, better performance
is achieved. In addition, the directory structure on your operating system, for example, UNIX or Windows,
is more transparent.
#### Prerequisites

The status of the package VRC must be Expired.
### Procedure summary

The following list shows the procedure steps and the corresponding sessions.

1. Change the status of the package VRC to Expired - Package VRCs (ttadv1511m000)
2. Purge the package VRC - Purge Entire Package VRC (ttadv6255m000)
3. Recreate the user files - Convert to Runtime DD (ttams2201m000)
