# SubcontractingModel.Explode

> Chapter: Chapter 20 Public Interfaces for Subcontracting
>
> Group: Public Interfaces for SubcontractingModel
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 842-843

```baan
DLL:   tiextsubapi
This function is available from 2024.08 (KB2328603).
Syntax: long SubcontractingModel.Explode(
domain  tcsite           iSite,
domain  tcitem           iProduct,
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
Usage:        Expl:   Use this Public Interface to get "exploded" Product
Subucontractor Bill of Material.
The product structure in Product Subcontractor Bill of Material
is searched for:
- direct non-phantom children of iProduct (single level)
- non-phantom children of the phantom children (multi-level;
maximum number of levels: iExplosionDepth)
The child items (materials/sub items) found are added to the
output arrays.
Phantoms on iExplosionDepth are not exploded but are included
in the output arrays, unless iExplodeLowestPhantoms is true,
then the explosion of the phantom childs continues.
iExplosionDepth = 0 is handled as iExplosionDepth = 1
Only BOM lines that are valid on iReferenceDate are read.
BOM lines that are not 'standard configuration' will be skipped.
Note : A warning is given when the output arrays are completely
filled, as that may mean that the output is not complete.
Pre:    N.A.
Post:   N.A.
Input:  iSite                   Site (mandatory when concept Job Shop by
Site is active).
iProduct                Product (mandatory).
iReferenceDate          Reference Date (mandatory).
iExplosionDepth         Control for Max Depth of explosion
(1 is direct children).
iMergeComponents        Control for merging same components on
different levels.
iApplyScrapYield        Control for applying defined scrap and
yield to determine the quantity.
iExplodeLowestPhantoms  Control for continuing exploding
Phantoms when iExplosionDepth is
reached.
Output: oProject                Array of projects, must be a
based array.
oWarehouse              Array of warehouses, must be a
based array.
oItem                   Array of Items, must be a based array.
oCustomizable           Array of Customizable flags, must be a
based array.
oPositionNumber         Array of Position numbers, must be a
based array.
oBomQuantity            Array of BOM Quantities, must be a
based array.
oNumberOfMaterials      The number of materials found and
filled in the arrays.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Function is executed successfully.
<> 0                    An error occurred. Product Subcontractor
Bill of Material could not be exploded.
```
