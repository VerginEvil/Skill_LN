# ProjectPCS.CopyProject

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 893-894

```baan
DLL:   tiextpcsapi
This function is available from 2022.06 (KB2244721).
Syntax: long ProjectPCS.CopyProject(
domain  tccprj           iSourceProject,
domain  tccprj           iTargetProjectCode,
domain  tckopr           iTargetProjectType,
domain  tipcs.ccgr       iTargetCalculationGroup,
domain  tcsite           iSourceSiteItemRelatedData,
boolean          iCopyItemData,
boolean          iCopyBillsOfMaterial,
boolean          iCopyRoutings,
boolean          iCopyCostingData,
boolean          iCopyPlanning,
boolean          iCopyProductVariantStructure,
domain  tcynna           iApproveConversionFactors,
ref     domain  tccprj           oGeneratedProject,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will copy a PCS Project.
If iTargetProjectCode is empty, the created Project Code will be
generated using the First Free Number of the default Project
Series.
If iTargetProjectCode is only filled with a Project Series, then
the created Project Code will be generated using the First Free
Number of the given Project Series.
Pre:    Retry point has been set.
Post:   Abort or commit the transaction.
Input:  iSourceProject          Source Project (Mandatory).
iTargetProjectCode      Target Project Code (Optional).
iTargetProjectType      Target Project Type (Mandatory).
iTargetCalculationGroup Target Calculation Group (Optional).
iSourceSiteItemRelatedData
The source Site for the BOM, Routing,
Subcontracting Model to be copied with
the Project (Optional).
iCopyItemData           Copy Item Data.
iCopyBillsOfMaterial    Copy Bill of Material and Subcontracting
models.
iCopyRoutings           Copy Routings.
iCopyCostingData        Copy Costing Data.
iCopyPlanning           Copy Planning.
iCopyProductVariantStructure
Copy Product Variant Structure.
iApproveConversionFactors
Approve the Conversion Factors of the
copied Project.
Output:
oGeneratedProject       The created Project code.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Project Copied succesfully.
<> 0                    Project has not been copied.
```
