# Chapter 8: LN Software Maintenance

## PMC introduction

To help you manage software updates to your LN system, Infor offers the Product Maintenance and
Control (PMC) Tool – an efficient, highly effective tool for managing functional software updates (Feature
Packs) and other software updates (Individual Solutions).
The PMC module manages the installation of Feature Packs and Individual Solutions. The PMC module
is delivered to all customers as part of the master CD-ROM of LN. The PMC module is used to check
software updates for completeness and customization interference.
Without a tool such as PMC, software updates could be installed irrespective of other software updates
that were already installed. Technically, an update that contains an earlier version of a software component
than the version already present on your system, could be installed. In this case, you lose the updates
contained in the original software components.
The PMC module contains two sub-modules.
- PMC distributor
- PMC recipient
## PMC Benefits

The PMC module is an easy-to-use tool that enables you to install, configure, and run new software with
confidence. The PMC module simultaneously addresses a wide range of software update challenges,
including:
- Automatic checks for updates for any previous dependencies, to ensure that these exist on
- Analysis of potential conflicts with system customizations at installation time, which enables
- Option to maintain copies of all previous software components. This feature enables the user
- Overview of all Feature Packs and Individual Solutions, that are installed.
the system on which you install the update.
the user to identify any conflicting customizations.
to roll back updates easily to any point in history.
> [!NOTE]
A customization component does not have a ‘maintenance date’ in its object. Therefore, if you deliver
customization components to a customer, whose maintenance license has expired, the customer can
still deploy the components.
## PMC overview

This chapter provides an overview of the Product Maintenance and Control (PMC) module.
This chapter contains the following sections:
- PMC Architecture
- Where to find the PMC module
- Dependencies
- Individual Solutions
- Collections
- Feature Packs and Patches
- PMC Distributor functionality
- PMC Recipient functionality
## PMC Architecture

This diagram shows the architecture of the PMC module:
The software developer creates or updates software components in the Data Dictionary of the developer’s
ERP system. Software is packaged by the PMC distributor and stored in the PMC Registry. Feature
packs are published on the Infor Download Center. Individual solutions and monthly collections are
published on an FTP server. Software can also be sent by e-mail.
The customer can download feature packs from the Infor Download Center. Through Infor Xtreme, the
customer can download individual solutions and monthly collections from the FTP Server. PMC recipient
builds or updates the PMC Registry on the customer's ERP system. Software in the customer's PMC
Registry can be imported in the customer's data dictionary.
## Where to find the PMC module

The PMC module is part of Infor Enterprise Server (Tools). The software supplier is the distributor of
the solutions, and the user or customer of the applications is the recipient. The PMC module contains
functionality and sessions for both the distributor and recipient role.
To navigate to the recipient part of the PMC module, complete these steps:

1. Log on to LN.
2. On the ERP Menu Browser, click Tools --> Software Installation --> Miscellaneous -->
Recipient.
3. Click Setup, Operational, and Miscellaneous.
Alternatively, complete these steps to navigate to the recipient part of the PMC module:

1. Log on to LN.
2. On the ERP Menu Browser, click Tools --> Application Development --> Product
Maintenance and Control --> Recipient.
3. Click Setup, Operational and Miscellaneous.
To navigate to the distributor part of the PMC module, complete these steps:

1. Log on to LN.
2. On the ERP Menu Browser, click Tools --> Application Development --> Product
Maintenance and Control --> Distributor.
3. Click Setup and Operational.
## Dependencies

When the PMC recipient installs software updates, the recipient checks the presence of the required
depending solutions.
Three dependency types exist:
- Pre-requisites
- Co-requisites
- Post-requisites
This diagram shows a pre-requisite dependency: solution 1 must be installed before solution 2.
The following section describes a customer scenario.
Example
A dependency requires you to install the previous version of a software component first. Suppose that
you installed LN from the master CD-ROM without customizations or solutions. You receive an updated
version of the Copy Sales Order (tdsls4201s000) session, which contains the session object, script, and
forms that are interdependent of each other.
You decide not to install the dump and, a few months later, you discover that a change is required in
the script to correct a problem that is keeping your sales force from selling an item. The change is sent
as a dump that contains only the session object and script. You can install this dump only if you installed
the previous version of the software component, because the dump requires the proper form of the first
solution. PMC automatically installs the previous solution.
Suppose you deliberately decided not to install a solution, for example, because you do not know if the
existing version of the Copy Sales Order (tdsls4201s000) session was customized. The PMC module
provides protection against this as well. In this case PMC informs you that the current version is
customized. You cannot overwrite software, because PMC uses update VRC levels and maintains copies
of all previous software components. This setup enables you to roll back updates easily to any point in
history.
### Individual solutions

A PMC Distributor creates and publishes individual solutions.
Individual solutions created for standard products of Infor are available for download 24 hours a day,
seven days a week, from the Infor Support Web site http://www.infor.com/inforxtreme for Infor-owned
products.
You can only download these solutions one by one.
After you download and scan a solution, the PMC recipient checks the dependencies with other solutions.
In some cases, other dependent solutions might be missing at the installation system and must be
downloaded and scanned, as well. The process to install individual solutions can take a long time if
many dependent solutions must be downloaded and scanned.
You can use the Multilevel Download functionality to download all the dependent solutions, without user
interaction, to simplify and speed up the download process.
### Collections

Collection dumps enable customers to update their system with the latest software.
Collections are groups of all individual solutions that are released in a particular period.
These individual solutions are gathered at the PMC distributor side in a single dump file.
Collections for standard products of Infor are published on an FTP server.
You can scan collections in a single action. While you scan the collection with the Scan Solution/Patch
File (ttpmc2200s000) session, the dump file is split into all individual solutions that were included in the
collection.
Afterwards, you can install the individual solutions.
You can use collection dumps in two ways: for pro-active installation or corrective installation.
- Pro-active installation
- Corrective installation
The user installs all individual solutions of the collection. The user runs the most up-to-date
version of the software, including the latest released fixes.
The individual solutions of the collection are not installed. The solutions have status Available
in the PMC registry. If the user runs into a problem, and a solution is advised for this problem,
the user can install that solution immediately. All dependent solutions will be installed
automatically.
### Feature Packs and patches

Periodically, individual solutions can be bundled into Feature Packs or patches. In general, these types
of updates contain solutions created in a larger time period than a collection. In the PMC Tool, the term
‘patch’ is used both for Feature Packs and patches. The patch entity is known at both the PMC distributor
and PMC recipient side. Feature Packs and patches are an indivisible set of solutions. You cannot install
or uninstall individual solutions that belong to a Feature Pack or a patch by the PMC recipient. You can
only install or uninstall entire Feature Packs and patches. Dependencies between Feature Packs and
patches can exist.
The subsequent sections describe the justification, characteristics, and differences of Feature Packs
and patches.
## Justification of Feature Packs and patches

During the life cycle of a product, in general, two types of changes are implemented in the product:
- Corrective fixes for defects
- Functional enhancements to further enrich the product
Functional enhancements are often accompanied by changes in the data model, changes in the user
interface, and changes in the behavior of the application. In general, functional enhancements require
a careful preparation before installation in an operational environment. PMC generates dependencies
between solutions, that contain the same components to guarantee that the solutions are installed in
the correct order and no necessary solutions are skipped. In some cases, users must first install a
number of functional enhancements before the users can install a corrective fix for a relative small defect.
Installation of the functional enhancements can be required at unexpected and undesirable moments.
Feature Packs enable you to separate functional enhancements from the flow of corrective fixes. This
separation enables users to adopt and implement functional enhancements in a more controlled way.
Patches do not offer this possibility.
### Feature Packs

Feature Packs enable you to separate corrective fixes from functional enhancements. Multiple parallel
maintenance baselines exist for the product. Every new baseline is linked to a unique base VRC.
Functional enhancements are, in principle, only implemented at the start of a new baseline.
This diagram shows the Feature Packs mechanism:
Feature Pack 1 is linked to base VRC A1. The Feature Pack contains a number of corrective fixes and
some functional enhancements. Corrective maintenance is performed for this Feature Pack, which
results in solutions 1, 2, and 3 in the previous diagram.
In parallel, the software distributor develops Feature Pack 2, which is linked to base VRC A2. Whenever
possible, the distributor immediately ports and includes corrective solutions created on top of Feature
Pack 1 in Feature Pack 2. Refer to solution 1 and the dashed arrow in the previous diagram. These
ported solutions are registered in Feature Pack 2 as so-called obsolete solutions.
The same process repeats when the distributor develops Feature Pack 3, which is linked to base VRC
A3.
After the release of Feature Pack 2 and 3, the distributor also creates corrective solutions on top of these
Feature Packs.
When Feature Pack 2 is being installed at a recipient, the PMC Tool checks whether all solutions that
were installed on top of Feature Pack 1 are also available for Feature Pack 2.
These solutions can be available in two different shapes for Feature Pack 2:
- As an obsolete solution
Included in Feature Pack 2. Refer to solution 1 and the dashed arrow in the previous diagram.
These obsolete solutions are integrated in Feature Pack 2 and do not have a separate physical
solution dump.
- As an individual solution
Available on top of Feature Pack. Refer to solutions 2’ and 3’ in the previous diagram. These
so-called missing solutions are not included in Feature Pack 2 and do have a physical solution
dump.
Note: If Feature Pack 1 is installed in multiple update VRCs, the PMC Tool performs the
missing solution check in all update VRCs, that contain Feature Pack 1.
By default, the PMC Tools will refuse to install Feature Pack 2 if not all solutions installed on top of
Feature Pack 1 are also available for Feature Pack 2. Otherwise, old defects would come back after
you install Feature Pack 2. The distributor is responsible for ensuring that all solutions of the preceding
Feature Pack are also available for the subsequent Feature Pack before publishing the subsequent
Feature Pack.
> [!NOTE]
You can change this default behavior, so that you can install Feature Pack updates without additional
individual solutions. For details, refer to To install a 'clean' Feature Pack.
Feature Packs are cumulative. Every new Feature Pack also includes all preceding Feature Packs. This
enables you to skip the installation of Feature Packs at the PMC recipient. For example, you can
immediately upgrade from Feature Pack 1 to Feature Pack 3 without installing Feature Pack 2 in between.
The installation process is optimized in such a way that only components that are changed as compared
to the current installed Feature Pack will be installed.
You can install Feature Packs in an existing update VRC. Therefore, creating a new update VRC is
unnecessary. As a result, the VRC structure at a recipient system can remain unchanged. However,
the base VRC linked to the update VRC will change. If desired, you can, of course, also install a new
Feature Pack in a new update VRC.
## To install a 'clean' Feature Pack

When you update an existing environment with a Feature Pack via PMC or via the Installation Wizard,
PMC requires that all solutions, that were installed on top of a previous Feature Pack, are installed for
the new Feature Pack as well. PMC requires these additional solutions to prevent that old problems
come back after installation of the Feature Pack. This also applies if you install the Feature Pack in
another, or even in a new, Update VRC. This is because you can upgrade your companies to the Package
Combination of that Update VRC and subsequently you might see old problems again.
In some situations this functionality is too strict, for example when you want to develop customizations
for different customers on different Feature Pack levels.
To change this default behavior, you must set the PMC_IGNORE_SOL environment variable to 1. You
can now install a 'clean' Feature Pack, without taking care of the content of already installed Feature
Packs and additional solutions.
You can specify the environment variable in different ways:
- In the command field of the BW configuration file (-set PMC_IGNORE_SOL=1). In this way
- In the $BSE/lib/bse_vars file (add the line PMC_IGNORE_SOL=1). If you use the Installation
the setting only applies to the user that uses this configuration.
Wizard you can add this line when you are prompted to change the bse_vars configuration
file. In this way the setting applies to all users.
> [!NOTE]
- It is recommended to remove the PMC_IGNORE_SOL setting after each Feature Pack
- If you install the Feature Pack in an already existing Update VRC, the solutions that were
installation.
installed in that Update VRC for the previous Feature Pack, will also be installed for the new
Feature Pack. So, the possibility to ignore additional solutions only applies to solutions of other
Update VRCs.
Example
You want to install Feature Pack 2, which includes solutions 133, 146 and 154 as obsolete solutions
already.
The following table shows, for some Update VRCs with different Feature Packs and additional solutions
installed:
- what happens if PMC_IGNORE_SOL is not set.
- what happens if PMC_IGNORE_SOL is set.
Update VRC

B61U_a_stnd
B61U_a_fp1
B61U_a_fp2
Feature Pack installed
-
FP1 including obsolet e-
solutions 133 and 146
Solutions installed
133
146
154
168
154
168
172
-
Action
Install FP2 in an Updat eInstall FP2 in a new Up-
Update VRC with som eVRC with FP1 and som edate VRC.
additional solutions installed.
Install FP2 in an 'FP0'
individual solutions installed.
SOL is not set
Fails unless additional
solutions 168 and 172
are present.
Reason for failure:
Solution 168 was alread yBoth solutions were al -Solutions 168 and 172
were installed on top of
Update VRC.
was installed on top of
FP1 in Update VRC
B61U_a_fp1.
Result if PMC_IGNORE _Fails unless additional
solutions 168 and 172
are present.
Reason for failure:
Fails unless additional
solutions 168 and 172
are present.
Reason for failure:
installed in this Update
VRC, and solution 172
ready installed in this
FP1 in Update VRC
B61U_a_fp1.
Succeeds.
Reason for success:
PMC can ignore all solutions, because it is a new
Both solutions were in -Update VRC.
VRC, so it is needed o nstalled in this Update
top of FP2.
ignored.
Solution 172 can be ignored now.
Fails unless additional
solution 168 is present .solutions 168 and 172
are present.
Reason for failure:
Reason for failure:
Solution 168 was installed in this Update
Result if PMC_IGNORE _Fails unless additional
SOL is set to 1
VRC, so they cannot be
> [!IMPORTANT]
Do not set PMC_IGNORE_SOL to 1 if you install the Feature Pack in an Update VRC and Package
Combination, and you plan to upgrade your companies to this Package Combination. This can result in
old problems coming back or, even worse, loss of data if additional solutions on top of the previous
Feature Pack introduced new table fields.
### Patches

Patches do not enable you to separate corrective fixes from functional enhancements. Only one
maintenance baseline of the product exists. Changes are always implemented in the latest version of
a software component. The base VRC remains the same. Functional enhancements will be included in
the chain of depending corrective solutions.
This diagram shows the Patch mechanism:
To install solution 3 in this diagram, you must first install solution 2, which contains a functional
enhancement.
Patches are not cumulative, which means you cannot skip the installation of Patches at a recipient's
location. For example, before you install Patch 3, you always must install Patch 2 in advance. You cannot
immediately upgrade from Patch 1 to Patch 3.
## Distributor’s Policy

The software distributor decides if Feature Packs or Patches are being applied. A mix of both types is
also possible:
- When applying Feature Packs, the distributor can decide to release a functional enhancement
- When applying Feature Packs, the distributor can decide to periodically also release Patches
as an individual PMC solution on top of one of the released Feature Packs.
on top of the Feature Pack.
When applying Feature Packs, the distributor’s policy determines how many base VRCs are maintained
in parallel and how long the base VRCs are maintained.
### PMC Distributor functionality

The software developer generates additional software and makes software changes on the existing LN
software packages.
The supplier of the LN software uses the PMC Distributor functionality to manage the software updates
and prepares those updates for delivery to the customers.
The following is a process overview of the PMC Distributor module.
- Create individual solutions
a. Define a unique identifier for the solution and a brief description.
b. Link one or more software components to the solution.
c. Define or generate the dependencies on other solutions.
d. Export the solution, the software dumps are now created.
e. Release the solution, the solution is now ready for delivery.
- Create collections
a. Define a unique identifier for the collection and a brief description.
b. Link one or more individual solutions to the collection.
c. Export the collection.
d. Release the collection.
- Create patches
a. Define a unique identifier for the patch and a brief description.
b. Link one or more individual solutions to the patch.
c. Define or generate the dependencies on other patches.
d. Validate the patch.
e. Export the patch.
f. Release the patch.
- Create Feature Packs
a. Define a new base VRC for the Feature Pack.
b. Define a unique identifier for the Feature Pack and a brief description.
c. Define the dependency on previous Feature Packs.
d. Generate the Feature Pack, in other words, link all components in a specified VRC to the
Feature Pack.
e. Validate the Feature Pack.
f. Export the Feature Pack.
g. Release the Feature Pack.
- Additional distributor functionality
- Mutilevel export.
- SCM integration.
- Maintenance History.
### PMC Recipient functionality

Customers use the PMC Recipient module to install the LN software updates on their ERP system.
The following is an overview of the PMC Recipient module.
- Download solutions
You can download solutions from the FTP server or copy the solutions from a medium such
as a CD-ROM.
- Scan and connect solutions
The downloaded solution files can be scanned. In other words, the user must extract and store
the solutions into the PMC registry. The extracted solutions are also connected to an update
VRC.
- Process solutions
a. Check to install. Report the following: Pre- and post-installation instructions, customized
components, and missing dependent solutions.
b. Install the solutions: Store the software components in the data dictionary, report additional
post-installation instructions.
- Additional recipient functionality
- Uninstall
- Mutilevel download
- Compare installed solutions
- Solution History
- PMC cleanup
- Copy PMC registry
- View installation runs.
## PMC distributor procedure

This chapter describes the PMC distributor procedures. This chapter contains the following sections:
- Setup
- To create updates
- Feature Pack development
- Customizations
### Setup

The procedures for the update distributor to set up the PMC administration.
The setup consists of these sections:
- Setup procedure
- Parameters
- Base VRCs
- Base VRC combinations
### Setup procedure

To perform the setup procedure, run these sessions:

1. Parameters (ttpmc0100s000)
2. Base VRC's (ttpmc0110m000)
3. Base VRC Combinations (ttpmc0111m000)
The subsequent sections provide a detailed explanation of the procedure.
### Parameters

The very first step in the distributor set-up procedure is to define the PMC parameters.
The following two group boxes are available:
- Recipient
Even if you do not use the PMC recipient part of the PMC module, for technical reasons, you
must fill in the parameters in this group box.
- Distributor
The PMC distributor part of the PMC module uses these parameters, and therefore you must
fill in these parameters.
Most of the parameters are directories on the operating system on which the solution dumps
will be stored.
For details, refer to the Parameters (ttpmc0100s000) session.
> [!NOTE]
Because the definition of the parameters is a once only step, you must be aware of the impact if you
change the parameters afterwards.
If you change the directories on the operating system, you must move the directories and files according
to the new directory specifications.
### base VRCs

You must define a base VRC before you can create and link solutions, collections, patches, and Feature
Packs to the base VRC.
A base VRC is an administrative identifier for a software product and is not a physical VRC, but must
always be connected to a physical VRC, which contains the software components.
The PMC distributor should connect a base VRC to an export VRC, the PMC recipient should connect
a base VRC to an update VRC.
> [!NOTE]
A Feature Pack always starts a new base VRC.
For details, refer to the Base VRC's (ttpmc0110m000) session.
### base VRC combinations

Base VRC combinations are required to define relations between base VRCs.
Any base VRC must always be a member of a base VRC combination, even if no relations to other base
VRCs exist.
If you have not linked a base VRC to a base VRC combination, you cannot create updates.
The following example shows a base VRC combination with two base VRCs with a relation:
For details refer to the Base VRC Combinations (ttpmc0111m000) session.
## To create updates

PMC distributor procedures to create software updates:
- To create solutions
- To create collections
- To create patches
- To create Feature Packs
## To create solutions

To create solutions:

1. Create the solution.
Create or maintain solutions in the Solutions (ttpmc1100m000) session.
This session is the central session from which you can maintain all aspects of solutions.
The initial status of a solution after creation is In Progress.
2. Optionally, create defects and connect defects to the solution.
You can create and connect the defects in the Defects by Solution (ttpmc1110m000) session.
3. Connect software components to the solution.
To connect software components to the solution, use the Components by Solution
(ttpmc1520m000) session and the Component by Solution (ttpmc1120s000) session.
You can also connect software components to a solution in the Connect Components to PMC
Solution (ttpmc1221m000) session.
4. Define dependencies between the solutions.
To define dependencies between solutions, run the Dependencies (ttpmc1140m000) session.
5. Validate the solution.
To validate a solution, select Validate Solution on the appropriate menu in the Solutions
(ttpmc1100m000) session. This option starts the Validate Solution (ttpmc1404s000) session.
This session checks, for example, if components are available, or if components are not
compiled in debug mode, and so on.
6. Export the solution.
To export a solution, use the Export Solution/Patch (ttpmc1200s000) session.
7. Release the solution.
To release a solution, you must change the Status from Exported to Released in the Solutions
(ttpmc1100m000) session.
You can only release a solution if the Status of the solution is Exported.
8. Optionally, publish the solution.
To publish a solution, select the Published check box in the Solutions (ttpmc1100m000)
session.
You can only publish a solution if the Status of the solution is Released.
Optionally, complete these steps:
- View or print solutions
To view solutions, use the Components by solution (ttpmc1521m000) session.
To print solutions, use the Print Components by Solution (ttpmc1420m000) session.
- View the solution history.
To view the solution history, use the Maintenance History (ttpmc1560m000) session.
## To create collections

To create collections:

1. Create the collection.
Create or maintain collections in the Collections (ttpmc1503m000) session.
This session is the central session from which you can maintain all aspects of collections.
The initial status of a collection after creation is In Progress.
2. Connect solutions to the collection.
You can connect solutions to a collection in the Solutions by Collection (ttpmc1151m000)
session.
3. Validate the collection.
Validate collections in the Validate Collection (ttpmc1402s000) session.
4. Export the collection.
Export a collection in the Export Collection (ttpmc1210s000) session.
5. Release the collection.
To release a collection, change the Collection Status from Exported to Released in the
Collections (ttpmc1101s000) session.
You can only release a collection if the Collection Status is Exported.
6. Optionally, publish the collection.
To publish a collection, select the Published check box in the Collections (ttpmc1101s000)
session.
You can only publish a collection if the Collection Status is Released.
Optionally, view the collection history. To view the collection history, use the Maintenance History
(ttpmc1560m000) session.
## To create patches

To create patches:

1. Create the patch.
Create or maintain patches in the Patches (ttpmc1501m000) session.
This session is the central session from which you can maintain all aspects of patches.
Clear the New Base VRC check box. Otherwise, the patch is a Feature Pack.
The initial status of a patch after creation is In Progress.
2. Connect solutions to the patch.
To connect solutions to a patch, you must use either the Solutions (ttpmc1100m000) session
or the Generate Patch (ttpmc1250s000) session.
3. Define dependencies between the patches.
To define dependencies between patches, you must use the Dependencies (ttpmc1140m000)
session.
4. Set a password on the patch.
To set or change the password of a patch, you must use the Password by Patch
(ttpmc1105s000) session.
5. Validate the patch.
To validate a patch, you must use the Validate Patch (ttpmc1401s000) session.
6. Export the patch.
To export a patch, you must use the Export Solution/Patch (ttpmc1200s000) session.
7. Release the patch.
To release a patch, you must change the Status from Exported to Released in the Patches
(ttpmc1501m000) session.
You can only release a patch if the Status is Exported.
8. Optionally, publish the patch.
To publish a patch, select the Published check box in the Patches (ttpmc1501m000) session.
Publish a patch if the Status of the patch is Released.
Optionally, view the patch history. You can view the patch history in the Maintenance History
(ttpmc1560m000) session.
## To create Feature Packs

> [!NOTE]
The process to create Feature Packs requires a specific setup of your development environment.
The Feature Pack development section describes in detail how the setup must look.
To create Feature Packs:

1. Create the Feature Pack.
You can create or maintain Feature Packs in the Patches (ttpmc1501m000) session.
This session is the central session from which you maintain all aspects of Feature Packs.
You must select the New Base VRC check box, otherwise, the patch is not a Feature Pack.
The initial status of a Feature Pack after creation is In progress.
2. Define dependencies between the Feature Packs.
Define dependencies between Feature Packs in the Dependencies (ttpmc1140m000) session.
3. Create the header for the Feature Pack.
Create the Feature Pack header in the Patch Header (ttpmc1106m000) session.
4. Generate obsolete solutions for the Feature Pack.
Generate obsolete solutions for the Feature Pack in the Generate Obsolete Solutions
(ttpmc1252s000) session.
5. Generate the Feature Pack.
Generate a Feature Pack in the Generate Patch for New Base VRC (ttpmc1253s000) session.
6. Validate the Feature Pack.
Validate a Feature Pack in the Validate Patch (ttpmc1401s000) session.
7. Export the Feature Pack.
Export a Feature Pack in the Export Solution/Patch (ttpmc1200s000) session.
8. Release the Feature Pack.
To release a Feature Pack, change the Status from Exported to Released in the Patches
(ttpmc1501m000) session.
You can only release a Feature Pack if the Status of the Feature Pack is Exported.
9. Optionally, publish the Feature Pack.
To publish a Feature Pack, you must select the Published check box in the Patches
(ttpmc1501m000) session.
You can only publish a Feature Pack if the Status of the Feature Pack is Release.
Optionally, view the Feature Pack history. You can view the Feature Pack history in the Maintenance
History (ttpmc1560m000) session.
## Feature Pack development

This section describes various aspects applicable to the Feature Pack development and build process.
This section describes the following topics:
- System setup for standard products
- System setup for derived products
- Rules for upgrading derived products
- To build Feature Packs and the Infor Installation Wizard
## System setup for standard products

The subsequent setup assumes that the distributor side includes a combined development/maintenance
environment. This combined environment supports the maintenance of already released Feature Packs,
development of a new Feature Pack, and the physical creation of solutions and Feature Packs.
> [!NOTE]
The following examples use the following conventions for VRC naming:
- Version: B61<X>
- Release: a<Y>
- Customer: <zzzz>
X = M aintenance, D evelopment
Y = Feature Pack number
zzzz = extension/localization code
The following diagrams illustrate the results over time:
As soon as the initial master product, B61_a, which for the sake of simplicity is referred to simply as
Feature Pack 0 in the remainder of this document, is released, the maintenance starts for B61_a in the
maintenance VRC B61M_a. The development of the new Feature Pack is carried out in B61D_a1. All
fixes in B61M_a are ported to B61D_a1. In the PMC registry of B61D_a1, these fixes are registered as
obsolete solutions. After B61D_a1 is frozen, a final Feature Pack is created for the Feature Pack and
installed in the same environment to enable you to perform maintenance on the Feature Pack.
> [!NOTE]
The SCM revision data is not available in the Feature Pack VRC B61_a1, because the export/import
software does not support the transfer of revisions. Because the original development VRC B61D_a1
is still present, you can still view revisions.
Currently, you can maintain B61M_a and B61M_a1, Feature Pack 0 and Feature Pack 1, in parallel.
You must port bug fixes that are created for Feature Pack 0 between the freeze moment and the time
of installation of Feature Pack 1 first. Feature Pack 2, B61D_a2, is currently in development.
You can repeat this cycle unlimited times for each new Feature Pack.
## System setup for derived products

The setup becomes a bit more complex if derived products such as localizations or extensions enter
the scope.
> [!NOTE]
Customizations are also a type of derived products. For customizations, the situation differs somewhat.
The section Customizations describes how to deal with customizations.
Suppose you must create a localization on top of Feature Pack 1.
A new VRC is created on top of Feature Pack 1, B61D_a1_loc1:
The localization is built on top of the standard Feature Pack and is delivered as a Feature Pack in PMC.
Therefore, you must not create master media for derived products. As soon as Feature Pack 0 for the
localization is available, the Feature Pack is installed in the maintenance VRC, B61M_a1_loc1.
The localization is also copied to a development VRC B61D_a2_loc1:
The first action that you must perform is to merge all bug-fixes of the standard VRC B61M_a1 into the
localization maintenance VRC B61M_a1_loc1 and to create PMC solutions for the localization.
In addition, you must merge the B61D_a2 functional enhancements to B61D_a2_loc1.
From this moment on, the localization follows the same Feature Pack cycle as the standard software.
Repeat the same approach for Feature Pack 2.
The physical Feature Packs for the standard software and the localization are created and installed in
a separate VRC tree B61_a2 and B61L_a2_loc1. New maintenance and development VRCs are created.
The maintenance and development VRC for the localization are populated with the components from
the installed Feature Pack B61L_a2_loc1.
## Rules to upgrade derived products

The following rules apply with respect to the creation of Feature Packs for derived products:
- You must only build Feature Packs for derived products on top of Feature Packs of the parent
product. Do not build Feature Packs on top of a Feature Pack plus a number of individual
solutions of the parent product. The reason for this is because you can only define PMC
dependencies between the Feature Pack of the standard and the derived products. You cannot
define PMC dependencies from the Feature Pack of the derived product to individual solutions
of the parent product.
- The Feature Pack frequency of derived products can be greater than the Feature Pack
- The Feature Pack frequency of derived products cannot be lower than the Feature Pack
frequency of the parent product. Therefore, you can build multiple derived Feature Packs on
top of a single Feature Pack of the parent product.
frequency of the parent product. If you do not update a derived product in time, you will most
likely face various compatibility issues between the parent and the derived product.
## Building Feature Packs and the Infor Installation Wizard

PMC Feature Packs are installable units that you can install by means of the Infor Installation Wizard.
Metadata that is included in a Feature Pack controls the behavior of the Infor Installation Wizard. The
following aspects are relevant if you want to make your Feature Pack suitable for installation with the
Infor Installation Wizard:
- Before you build a Feature Pack, be sure to fill in the installable unit key, name, and version
are filled at your PMC base VRC. If you do not fill in these values, the Infor Installation Wizard
will not recognize the installable unit. For more details, refer to the Base VRC's
(ttpmc0110m000) session.
- Before you export a Feature Pack, be sure that the Feature Pack header contains the correct
properties. Based on the properties defined in the Feature Pack header, the Infor Installation
Wizard can automatically perform particular actions at a recipient system, such as create new
package combinations, create new update VRCs, and link new update VRCs to an existing
or new package combination. For more details, refer to the Patch Header (ttpmc1106m000)
session.
### Customizations

This section describes various aspects relevant to the development and maintenance process of
customizations.
Customizations are, in most cases, built by organizations other than the producer of the related parent
standard product.
The vendor who builds customizations installs the standard parent product in an update VRC.
The customization is built on top of the installed parent standard product.
This situation is specific in the sense that PMC serves both as recipient and distributor in such a
development environment.
The following sections describe best practices how to develop and maintain customizations.
- Patches and customizations
- Feature Packs and customizations
- Dependencies for customizations
- Other
## Patches and customizations

In some cases, the vendor of the standard parent product applies patches rather than Feature Packs
as a method to provide incremental updates to the market. As opposed to Feature Packs, patches are
not cumulative. The installation of a patch in an update VRC requires that you also install all preceding
update VRCs in the same update VRC. This issue has consequences for the VRC setup at the distributor.
In most cases, you use a single environment to develop and to maintain multiple customizations. You
build every customization on a specific patch. In addition, you must periodically upgrade existing
customizations to a newer patch. As a result, you must have multiple Feature Packs of the standard
parent product installed in separate VRCs. The following method is the best way to achieve this:
Install patch 1 of the standard parent product in update VRC P10U_a1_stnd. When patch 2 is available,
install the patch in a new, separate update VRC P10U_a2_stnd, which is derived from P10U_a1_stnd.
Patch 2 will have patch 1 as a prerequisite. You cannot install patch 2 in the new update VRC
P10U_a2_stnd because patch 1 is not installed in this new update VRC. Therefore, run the Copy Solution
Registry to Derived Update VRC (ttpmc2290m000) session and copy the registry of update VRC
P10_a1_stnd into P10_a2_stnd. After you perform this step, you can install patch 2 directly in the
P10U_a2_stnd update VRC. You can then repeat this same process for subsequent patches. The
P10U_a<n>_stnd VRCs must only contain net patches. No additional solutions must be installed in
these VRCs that do not belong to the relevant patch.
At this point, you have a VRC tree in which the net patches are installed in separate VRCs. In general,
customizations are developed based on a net patch. However, in some cases customizations are not
derived from a net patch, or a customer might want to install parent standard product solutions that have
components which overlap with the customization. As a result, the customer must have the option to
derive the customization VRC from any possible maintenance stage of the parent standard product.
The P10U_a<n>_std update VRCs are introduced to achieve this. For every customization an intermediate
VRC layer is introduced in which standard solutions can be installed that do not belong to the underlying
patch. You can again use the Copy Solution Registry to Derived Update VRC (ttpmc2290m000) session
to populate the PMC registry for the P10U_a<n>_std update VRCs.
The customization VRCs P10C_a_cusA, P10C_a_cusB, and P10C_a_cusC represent various
customizations that are derived from various patches. Suppose customization P10C_a_cusA is developed
based on the net patch 1. During development of the customization, the P10U_a1_stdA VRC will still
be empty. After the customization is released and the customer installs the customization, the customer
might want to install solutions of the standard parent product that also require an update of the
customization. In this case, the customization vendor can install the solutions of the parent standard
product in the P10U_a1_stdA VRC, port the solution to the P10C_a_cusA and provide a corresponding
solution for the customization VRC. Installation of solutions in the P10U_a1_stdA VRC will only have
impact on the P10C_a_cusA customization and will not impact the other customizations in the
environment.
## Feature Packs and Customizations

To a certain extent, the system setup is comparable to the setup described for localizations and extensions
described in the section Feature Pack development. The main difference lies in the fact that Feature
Packs for the parent standard product are now installed in an update VRC by means of PMC. Another
differentiator is the fact that Feature Packs are cumulative, which means that Feature Packs also contain
all preceding Feature Packs. To upgrade a customization to a higher Feature Pack level, having a VRC
available that only contains the net changes of a Feature Pack of the standard parent product can be
useful. Suppose you must create a customization on top of Feature Pack 1 for a parent standard product.
Feature Pack 1 is installed in the B61U_a1_stnd update VRC and a new VRC B61W_a1_cusA is
developed on top of the Feature Pack.
The customization is built on top of the standard Feature Pack and will be delivered as a Feature Pack
in PMC, so no master media must be created for the customization. As soon as Feature Pack 0 for the
customization is available, the Feature Pack is installed in the maintenance VRC B61M_a1_cusA.
> [!NOTE]
In theory, you can also skip the installation of the FP in the B61M_a1_cus1 VRC and start maintenance
immediately in the B61D_a1_cus1 VRC. However, best practice is to install and maintain the official
build that customers also receive.
Solutions for Feature Pack 1 of the parent standard product will be installed in the B61U_a1_stnd VRC.
When you scan solutions for the parent standard product, you can also print a customization report. The
customization report provides an overview of which components must be updated in the B61M_a1_cusA
VRC. As soon as you install the standard solution, you can merge the changes to the B61M_a1_cusA
VRC and create a corresponding PMC solution for the customization.
The approach for subsequent Feature Packs is as follows: Install Feature Pack 2 for the parent standard
product in the B61U_a2_stnd VRC, which is derived from B61_a VRC. Copy the contents of the
B61M_a1_cusA VRC to the B61W_a2_cusA VRC. As a result, all maintenance changes you create on
top of Feature Pack 0 of the customization until the moment of the copy action immediately become
available in the B61W_a2_cusA VRC. After the copy, you must also port all maintenance changes in
the B61M_a1_cusA VRC to the B61W_a2_cusA VRC. Feature Pack 2 for the standard product is
cumulative, which means that all changes implemented in Feature Pack 1 are also present in Feature
Pack 2. Therefore, you must create an overview of all components that were changed in Feature Pack
2 as compared to Feature Pack 1, and these components also must be present in the customization.
To achieve this, you can use the Compare Package VRC's (ttadv6450m000) session. In this session,
specify values in the following fields as follows:

VRC 1
B61U_a1_stnd
VRC 2
B61U_a2_stnd
Where Software Components presen tB61W_a2_cusA
in VRC
Using these settings enable you to create a net overview of customized components that must be
updated to be compatible with the Feature Pack 2 of the parent standard product. You can then merge
all changes implemented in Feature Pack 2 of the standard product from the B61U_2_stnd VRC into
the B61W_a2_cusA VRC. You can then build Feature Pack 1 for the customization, based on the
contents of the B61D_a2_cusA VRC.
You can repeat this procedure for an unlimited number of Feature Packs. In addition, you can develop
and maintain multiple customizations in parallel on various levels of the standard parent product.
If multiple customization VRCs are derived from, for example, the B61U_a1_stnd VRC, then for every
customization, an additional update VRC layer B61U_a1_std is required between the customization
VRC and the B61U_a2_stnd VRC. You can use the additional update VRC layer to install additional
solutions of the parent product, which you must port to the customization. You must use the Copy
Solution Registry to Derived Update VRC (ttpmc2290m000) session to populate the PMC registry for
the B61U_a1_std update VRCs. Installation of additional solutions in the B61U_a1_stdA update VRC
only impacts the B61M_a_cusA VRC and does not influence the B61M_a1_cusB VRC.
## Dependencies for customizations

Individual solutions, patches and/or Feature Packs for customizations must have dependencies to
corresponding updates of the parent standard product. Not having these types of dependencies can
result in runtime compatibility problems if only a solution for the standard parent product is installed,
while installation of an update for the customizations was also required.
The best way to establish these dependencies is to define co-requisite dependencies between the
updates of the parent product and the corresponding updates for the customized product. The co-requisite
dependencies are generated automatically if the customization uses the same solution numbers that
were also used in the parent standard product. Of course this method only works if the base VRC of the
customization, together with the base VRC of the standard parent product, are part of the same base
VRC combination at the distributor side. At the recipient side, the update VRCs for the parent standard
product and the customization must also be included in a VRC combination.
The co-requisite relationship will only be in one direction: from the customization to the standard parent
product. This one-directional co-requisite makes it impossible to install a solution for the customization
without simultaneously installing the corresponding standard solution for the parent product. However,
as long as you have not scanned the customized solution, you can still install a solution for the standard
parent product without simultaneously installing the corresponding solution of the customization. This
can result in run time compatibility problems. The customization report solves this problem. When you
check standard solutions in a customized environment, you can optionally print a customization report,
which signals customized components and informs the recipient that, together with the standard solution,
an update for the customization must also be installed.
### Other

The facts described in the sections Rules to upgrade derived products and Building Feature Packs and
the Infor Installation Wizard are also applicable to the development and maintenance of customizations.
## PMC distributor session summary

## PMC distributor sessions

Title
Description
Parameters (ttpmc0100s000)
Maintain the parameters for the PMC module.
Base VRC's (ttpmc0110m000)
Maintain the relation between base VRCs and
export VRCs.
Base VRC Combinations (ttpmc0111m000)
Display the base VRC combinations.
Base VRC Combinations (ttpmc0111m100)
Maintain the base VRC combinations.
Base VRCs by Base VRC Combination
(ttpmc0112m000)
Link the base VRCs to a base VRC combination.
Solutions (ttpmc1100m000)
Maintain solutions.
Collections (ttpmc1101s000)
Maintain collections.
Password by Patch (ttpmc1105s000)
Enter a password for a patch. A patch is meant
to be installed as a whole. If you want to break up
a patch to install the solutions it contains separately, a password is required.
Patch Header (ttpmc1106m000)
Maintain patch headers.
Packages by Patch Header (ttpmc1107m000)
Link packages to a patch header.
Defects by Solution (ttpmc1110m000)
Specify which defects are solved by a solution.
Component by Solution (ttpmc1120s000)
Link a component to a solution.
Sessions by Component (ttpmc1125m000)
Display the sessions that use a component that
is linked to a solution.
Dependencies (ttpmc1140m000)
Define the dependencies between solutions or
patches.
Solutions by Collection (ttpmc1151m000)
Add solutions to a collection.
Export Solution/Patch (ttpmc1200s000)
Create the export dump for a solution or a patch.
Export Solution Multi-level (ttpmc1202s000)
Create a multilevel export dump for a released
solution.
Export Collection (ttpmc1210s000)
Export a collection, which means that a dump of
the collection is made.
Connect Components to PMC Solution
(ttpmc1221m000)
Connect software components in the export VRC
to a PMC solution.
Generate Dependencies (ttpmc1240s000)
Generate the dependency relations between solutions which must be installed together at a customer system.
Generate Patch (ttpmc1250s000)
Generate a patch.
Generate Collection (ttpmc1251s000)
Add a range of solutions to a collection.
Generate Obsolete Solutions (ttpmc1252s000)
Generate obsolete solutions.
Generate Patch for New Base VRC (ttpmc1253s000 )Generate patch for New Base VRC.
Select "In Progress" Solution (ttpmc1299m000)
Link a component to an In progress solution.
Print Solution/Patch (ttpmc1400m000)
Print solutions and patches.
Validate Patch (ttpmc1401s000)
Validate a patch.
Validate Collection (ttpmc1402s000)
Validate a collection.
Print Collection (ttpmc1403m000)
Print the contents of a collection.
Validate Solution (ttpmc1404s000)
Validate a solution.
Print Components by Solution (ttpmc1420m000)
Print components connected to a solution.
Print Dependencies (Multi-level) (ttpmc1440m000 )Print the dependencies.
Print Maintenance History (ttpmc1460m000)
Print the history of changes for a solution or patch.
Patches (ttpmc1501m000)
Maintain patches.
Patches (ttpmc1501m100)
Maintain patches
Collections (ttpmc1503m000)
Maintain collections.
Components by Solution (ttpmc1520m000)
Connect the modified components to a solution.
Components by solution (ttpmc1521m000)
View the components that are linked to a solution.
Dependencies (ttpmc1541m000)
View the dependencies between solutions or
patches.
Solutions by Collection (ttpmc1551m000)
View the solutions that are part of a collection.
Maintenance History (ttpmc1560m000)
Display the status changes of a solution or patch
for a base VRC.
General Maintenance History (ttpmc1561m000)
Display the status changes of a all solutions and
patches.
Specify Another Solution (ttpmc1821s000)
Specify another solution.
