# PhysicalBreakdown.CreateFromProjectBreakdownStructure

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PhysicalBreakdown
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1354-1356

```baan
DLL:   tsextcfgapi
This function is available from     2023.09 (KB2305193  ).
Syntax: long PhysicalBreakdown.CreateFromProjectBreakdownStructure(
domain  tccprj           iSourceProject,
domain  tscfg.2212.01    iSourceStructure,
domain  tscfg.pelt       iSourceElementOrActivity,
domain  tsbsc.clst       iTargetInstallationGroup,
domain  tscfg.sigr       iSerialItemGroup,
domain  tsmdm.utct       iDeliveryTime,
domain  tsmdm.utct       iInstallationTime,
domain  tcyesno          iCopyMaterials,
domain  tcyesno          iGenerateDummySerials,
domain  tcyesno          iContinueWhenAlreadyCreated,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function creates a Physical Breakdown from a Project
Breakdown Structure. The same functionality is applicable
as available in session Copy Project Breakdown Structure
(tscfg2210m200).
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Input   :
iSourceProject
Project; Mandatory
iSourceStructure
Origin Structure, Element or Activity; Mandatory
iSourceElementOrActivity
Project Element/Activity; Mandatory
iTargetInstallationGroup
Target Installation Group; Not mandatory
iSerialItemGroup
Serialized Item Group; Mandatory when Configurations
parameter Serialized Item Group Usage is Yes.
iDeliveryTime
Delivery Time; Mandatory when Warranty is applicable
for Element/Activity, and Warranty Start is determined
by Delivery.
iInstallationTime
Installation Time; Mandatory when Warranty is applicable
for Element/Activity, and Warranty Start is determined
by Installation.
iCopyMaterials
Copy Materials; Mandatory
iGenerateDummySerials
Generate Dummy Serial Numbers; Mandatory
iContinueWhenAlreadyCreated
Continue when Physical Breakdown already has been
created for Project; Mandatory
Output  :
ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0                                   - No error
<> 0                                          - An error occurred
```
