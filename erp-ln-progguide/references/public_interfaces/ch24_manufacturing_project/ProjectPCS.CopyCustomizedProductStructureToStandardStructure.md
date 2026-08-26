# ProjectPCS.CopyCustomizedProductStructureToStandardStructure

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 882-883

```baan
DLL:   tiextpcsapi
This function is available from     2024.04 (KB2299641  ).
Syntax: long ProjectPCS.CopyCustomizedProductStructureToStandardStructure(
domain  tcsite           iSite,
domain  tcitem           iStandardItem,
domain  tcitem           iCustomizedItem,
domain  tcyesno          iCopyAllComponentsAndEffectiveUnits,
domain  tcuef.effn       iUnit,
domain  tcdate           iReferenceDate,
domain  ticpst           iCopyMethod,
domain  tcyesno          iCopyEitemRelationships,
domain  tcyesno          iIncludeAlternatives,
domain  tcyesno          iIncludeUseUpMaterials,
domain  tcyesno          iGenerateNewItemCodes,
domain  tcyesno          iApproveConversionFactors,
domain  tcyesno          iCopyToStandardItemConfiguration,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Copy a customized product structure to a standard structure.
Pre:    Retry point must be set.
Post:   Abort or commit the transaction.
Input:  iSite   Site (Mandatory when the Site concept
is active).
iStandardItem
Standard Item to copy (Mandatory).
iCustomizedItem
Customized Item to copy to (Mandatory).
The project segment determines the Project.
iCopyAllComponentsAndEffectiveUnits
To specify whether or not effectivity unit in the
product structure must be copied.
Mandatory if Unit Effectivity is YES in common parameters.
iUnit   Effectivity Unit (Optional). When provided,
only the effective components are copied.
Not applicable when iCopyAllComponentsAndEffectiveUnits
is set to YES.
iReferenceDate
Reference date to determine which
components must be included. (Mandatory).
iCopyMethod
Copy method (Mandatory). Possible options are:
Single Level:  Only the first level of the
product structure is copied
If standard item and Customized item
are equal then Single level is
not applicable
Multilevel: All levels of the product structure
are copied.
Interactive is not applicable.
iCopyEitemRelationships
To specify whether the E                              -item relationships of a
customized structure is copied to the
standard structure.
Mandatory when Site is not active.
iIncludeAlternatives
To specify whether or not alternative
items in the product structure must be copied.
Mandatory if Alternative materials is YES in
common parameters.
iIncludeUseUpMaterials
To specify whether or not use up materials
in the product structure must be copied.
Mandatory if Alternative materials is YES in
common parameters.
iGenerateNewItemCodes
To specify whether or not new item codes
must be generated when the target customized
item already exist.
iApproveConversionFactors
To specify whether or not for the created
customized items, conversion factors need
to be approved automatically (Mandatory).
iCopyToStandardItemConfiguration
To specify whether product structure of a
customized structure is copied to standard structure.
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
