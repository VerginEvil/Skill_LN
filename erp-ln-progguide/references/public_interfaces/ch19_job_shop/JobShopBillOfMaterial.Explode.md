# JobShopBillOfMaterial.Explode

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 644-646

```baan
DLL:   tiextbomapi
This function is available from     2022.03 (KB2221191  ).
Syntax: long JobShopBillOfMaterial.Explode(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
domain  tcuef.effn       iEffectivityUnit,
domain  tcdate           iReferenceDate,
long             iExplosionDepth,
boolean          iMergeComponents,
boolean          iApplyScrapYield,
boolean          iExplodeLowestPhantoms,
ref     domain  tccprj           oProject() fixed,
ref     domain  tccwar           oWarehouse() fixed,
ref     domain  tcitem           oItem() fixed,
ref     domain  tcyesno          oCustomizable(),
ref     domain  tcpono           oPositionNumber(),
ref     domain  tcqiv1           oBomQuantity(),
ref             long             oNumberOfMaterials,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to get "exploded" Bill of Material
information in output arrays.
The BOM tree is searched for:
-                       direct non-phantom children of iProduct
-                       non-phantom children of phantom children (multi-level;
maximum number of levels: iExplosionDepth)
The found children (= materials) are added to the
output arrays. The output arrays will have a length of 3000.
In case the concept Job Shop by Site is active, then
the Job Shop BOM is searched else the 'classic' BOM is searched.
When Job Shop by Site is active, then iSite must be filled and
iBillOfMaterialCode / iRevision can be filled optionally. When
iBillOfMaterialCode and iRevision are both filled, then the Job
Shop BOM is read for the specified Model and Revision, else
the 'Use for Planning' Job Shop BOM is read.
When Job Shop by Site is not active, then iSite,
iBillOfMaterialCode and iRevision are not used.
Phantoms on iExplosionDepth are not exploded but
are included in the output arrays. But if
iExplodeLowestPhantoms = true, then the phantom children
on iExplosionDepth are exploded anyway.
iExplosionDepth = 0 is handled as if iExplosionDepth = 1.
Only BOM lines that are valid on iReferenceDate and that
are valid for iEffectivityUnit are read. Other BOM lines
are skipped.
E.g. if iEffectivityUnit = 0, then BOM lines that are
not 'standard configuration' will be skipped.
Note that if the concept Job Shop by Site is In Preperation and
the Site is empty, a warning instead of an error is given in the
returned ExceptionID structure. The function still returns 0 in
this case.
A warning is also given when the output arrays are completely
filled, as that may mean that the output is not complete.
Pre:    Output arrays must be based.
Post:   NA
Input:  iSite
Site (Mandatory when concept Job Shop by Site is active).
iProduct
Product (Mandatory).
iBillOfMaterialCode
BOM Model  (Optional).
iRevision
Source Revision  (Optional).
iEffectivityUnit
Effectivity Unit (Optional).
iReferenceDate
Reference Date for filtering the BOM lines (Mandatory).
iExplosionDepth
Maximum dept (1 is direct children).
iMergeComponents
Merge the same components on different levels.
iApplyScrapYield
Apply defined scrap and yield to determine the quantity.
iExplodeLowestPhantoms
Continue exploding Phantoms when iExplosionDepth is
reached.
Output: oProject                      - Array of projects, must be a based array.
oWarehouse                            - Array of warehouses, must be a based array.
oItem                                 - Array of Items, must be a based array.
oCustomizable                         - Array of Customizable flags, must be a based
array.
oPositionNumber                       - Array of Position numbers, must be a based
array.
oBomQuantity                          - Array of BOM Quantities, must be a based
array.
oNumberOfMaterials
-                                       The number of materials found and filled in
the arrays.
oExceptionMessage
-                                       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID
-                                       An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               -     Function is executed successfully.
<> 0                       -  An error occurred. The Job Shop Bill of Material could
not be exploded.
```
