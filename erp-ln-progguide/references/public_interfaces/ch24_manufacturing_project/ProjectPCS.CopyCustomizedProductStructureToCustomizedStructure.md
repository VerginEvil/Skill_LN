# ProjectPCS.CopyCustomizedProductStructureToCustomizedStructure

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 880-882

```baan
DLL:   tiextpcsapi
This function is available from     2024.04 (KB2299641  ).
Syntax: long ProjectPCS.CopyCustomizedProductStructureToCustomizedStructure(
domain  tcsite           iSite,
domain  tcitem           iSourceCustomizedItem,
domain  tcitem           iTargetCustomizedItem,
domain  tcyesno          iUseProjectReferenceDate,
domain  tcdate           iReferenceDate,
domain  tcyesno          iCopyAllComponentsAndEffectiveUnits,
domain  tcuef.effn       iUnit,
domain  ticpst           iCopyMethod,
domain  tcyesno          iCopyEitemRelationships,
domain  tcyesno          iCopyProductVariantStructure,
domain  tcyesno          iIncludeAlternatives,
domain  tcyesno          iIncludeUseUpMaterials,
domain  tcyesno          iGenerateNewItemCodes,
domain  tcyesno          iApproveConversionFactors,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Copy a customized product structure to a customized structure
linked to a PCS project. The project segment of given
Customized Item determines which PCS Project the
customized structure is created for.
Pre:    Retry point must be set.
Post:   Abort or commit the transaction.
Input:  iSite   Site (Mandatory when the Site concept is active).
iSourceCustomizedItem
Source Customized Item to copy (Mandatory).
The project segment determines the Project.
iTargetCustomizedItem
Target Customized Item to copy to (Mandatory).
The project segment determines the Project.
iUseProjectReferenceDate
Indicates if the reference date of the target PCS
project must be used (Mandatory).
If the project does not have a reference
date, the current date is used.
iReferenceDate
Reference date to determine which
components must be included. Not applicable when
iUseProjectReferenceDate is set to YES.
iCopyAllComponentsAndEffectiveUnits
To specify whether or not effectivity unit in the
product structure must be copied.
Mandatory if Unit Effectivity is YES in
common parameters.
iUnit   Effectivity Unit (Optional). When provided,
only the effective components are copied.
Not applicable when iCopyAllComponentsAndEffectiveUnits
is set to YES.
iCopyMethod
Copy method (Mandatory). Possible options are:
Single Level:  Only the first level of the
product structure is copied
Multilevel: All levels of the product structure
are copied.
Interactive is not applicable.
iCopyEitemRelationships
To specify whether the E                              -item relationships are copied
to the customized structure.
Mandatory when Site is not active.
iCopyProductVariantStructure
To specify whether the product variant structure of the
customized source item is copied to customized
target item. (Mandatory).
iIncludeAlternatives
To specify whether or not alternative
items in the product structure must be
copied.
Mandatory if Alternative materials is YES in
common parameters.
iIncludeUseUpMaterials
To specify whether or not use up materials
in the product structure must be
copied.
Mandatory if Alternative materials is YES in
common parameters.
iGenerateNewItemCodes
To specify whether or not new item codes
must be generated when the customized
item already exist.
iApproveConversionFactors
To specify whether or not for the created
customized items, conversion factors need
to be approved automatically (Mandatory).
Output:
oExceptionMessage
The last message if any message is found.If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information.
Use the functions in Exception to get all relevant
information.
Return: 0       Successfully copied.
<> 0    Failed to copy.
```
