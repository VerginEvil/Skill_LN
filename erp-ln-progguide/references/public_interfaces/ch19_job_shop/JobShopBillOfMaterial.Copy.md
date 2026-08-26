# JobShopBillOfMaterial.Copy

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 641-642

```baan
DLL:   tiextbomapi
This function is available from     2021.05 (KB2156270  ).
Syntax: long JobShopBillOfMaterial.Copy(
domain  tcsite           iSourceSite,
domain  tcitem           iSourceProduct,
domain  tibmdl           iSourceBillOfMaterialCode,
domain  tibmrv           iSourceRevision,
domain  tcsite           iTargetSite,
domain  tcitem           iTargetProduct,
domain  tibmdl           iTargetBillOfMaterialCode,
domain  tibmrv           iTargetRevision,
boolean          iCopyExceptions,
boolean          iCopyReferenceDesignators,
boolean          iCopyMaterialsRoutingRelationships,
boolean          iCopyBomText,
boolean          iCopyPhantomRoutingRelationships,
boolean          iCopyAlternativeMaterials,
ref     domain  tibmdl           oNewBillOfMaterialCode,
ref     domain  tibmrv           oNewRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to copy a Job Shop Bill of Material to
the target Job Shop Bill of Material where related data is
copied based on input options.
If the target model code does not exist, the target revision is
ignored as a new Model code and revision are created by the
system.
If target model code does exist but revision number is missing,
A new revision is created by the system.
Pre:    Job Shop by Site must be In Preparation or Active.
Retry point has been set.
Post:   abort or commit the transaction
Input:  iSourceSite
Source Site (Mandatory).
iSourceProduct
Source Product (Mandatory).
iSourceBillOfMaterialCode
Source BOM Model (Mandatory).
iSourceRevision
Source Revision (Mandatory).
iTargetSite
Target Site (Mandatory).
iTargetProduct
Target Product (Mandatory).
iTargetBillOfMaterialCode
Target Bill Of Material Code (Optional).
iTargetRevision
Target Revision (Optional).
iCopyExceptions
Copy Exceptions
iCopyReferenceDesignators
Copy Reference Designators
iCopyMaterialRoutingRelationships
Copy Material Routing Relationships
iCopyBomText
Copy BOM Text
iCopyPhantomRoutingRelationships
Copy Phantom Routing Relationships
iCopyAlternativeMaterials
Copy Alternative Materials
Output: oNewBillOfMaterialCode
New Job Shop BOM model.
oNewRevision
New Job Shop BOM revision.
oExceptionMessage
The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               - Function is executed successfully.
<> 0                       - An error occurred. The Job Shop Bill of Material could not
be copied.
```
