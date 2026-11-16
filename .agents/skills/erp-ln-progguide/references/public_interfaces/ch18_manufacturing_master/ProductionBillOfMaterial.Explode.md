# ProductionBillOfMaterial.Explode

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 627-629

```baan
DLL:   tiextmfcapi
This function is available from 2026.01 (KB3573290).
Syntax: long ProductionBillOfMaterial.Explode(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tcuef.effn       iEffectivityUnit,
domain  tcdate           iReferenceDate,
long             iExplosionDepth,
boolean          iApplyScrapYield,
boolean          iMergeComponents,
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
- direct non-phantom children of iProduct
- non-phantom children of phantom children (multi-level;
maximum number of levels: iExplosionDepth)
The found children (= materials) are added to the
output arrays. The output arrays will have a length of 3000.
In case the concept Job Shop by Site is active, then the
Production Bom (table timfc310) is searched else the 'classic'
Bom (table tibom010) is searched.
Phantoms on iExplosionDepth are not exploded but are included in
the output arrays, unless iExplodeLowestPhantoms = true: then
the explosion of the phantom child's continues.
Only BOM lines that are valid on iReferenceDate and that are
valid for iEffectivityUnit are read. Other BOM lines are skipped
E.g. if iEffectivityUnit = 0, then BOM lines that are  not
'standard configuration' will be skipped.
A warning is also given when the output arrays are completely
filled, as that may mean that the output is not complete.
Pre:    Output arrays must be based.
Post:   NA
Input:  iSite
Site.
iProduct
Product.
iEffectivityUnit
Effectivity Unit.
iReferenceDate
Reference Date.
iExplosionDepth
Explosion Depth. Default value is 1. if user option as
zero then, use default value.
iApplyScrapYield
Apply Scrap Yield.
iMergeComponents
Merge Components.
iExplodeLowestPhantoms
Explode Lowest Phantoms.
Output: oProject        - Array of Projects, must be a based array.
oWarehouse      - Array of Warehouses, must be a based array.
oItem           - Array of Items, must be a based array.
oCustomizable   - Array of Customizable flags, must be a based
array.
oPositionNumber - Array of Position numbers, must be a based
array.
oBomQuantity    - Array of BOM Quantities, must be a based
array.
oNumberOfMaterials
- Number of materials.
oExceptionMessage
- The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID
- An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0 -     Function is executed successfully.
<> 0 -  An error occurred. The Production Bill of Material could
not be exploded.
```
