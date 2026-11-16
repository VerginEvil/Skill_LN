# EngineeringItemRevision.GenerateEBomCopyData

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItemRevision
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 254-256

```baan
DLL:   tiextedmapi
This function is available from 2024.03 (KB2298929).
Syntax: long EngineeringItemRevision.GenerateEBomCopyData(
domain  tcitem           iEngineeringItem,
domain  tiedm.revi       iRevision,
domain  tcitem           iTargetItem,
boolean          iOverwriteExistingEBomCopyData,
boolean          iCreateRelationships,
boolean          iIncludeJobShopComponents,
boolean          iOverwriteItemInProduction,
boolean          iOverwriteItemDescription,
boolean          iCopyAttachedDocuments,
boolean          iCopyDocumentLinks,
boolean          iIncludeAlternatives,
boolean          iIncludeUseUpMaterials,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to generate copy data for a
multilevel EBOM. It will not generate copy data for the lower
levels of the EBOM if copy data already exists.
It will not generate copy data of a E-item revision if:
- The revision does not have the status Approved by Production.
- The E-item revision's unit is different from the item's unit.
- The E-Item type is different from production item type.
- There is no valid revision of a component E-item of the EBOM
with the status Approved by Production.
Create Relationships is related with Overwrite Item in
Production:
- If Create Relationships is true and Overwrite Item in
Production is false, the relation is created with the same
code as that of the E-item only if an item with that code
does not exist in production.
- If Create Relationships is true and Overwrite Item in
Production is true, the relation is created with the same
code as that of the E-item. If an item with that code
already exists in production, it is overwritten.
- If Create Relationships is false and Overwrite Item in
Production is true, the generation of copy data is stopped
when the relations are not defined.
Pre:    N.A.
Post:   N.A.
Input:  iEngineeringItem        - Engineering Item (Mandatory).
iRevision               - Revision (Mandatory).
iTargetItem             - Target Item (Mandatory).
iOverwriteExistingEBomCopyData
- Control for overwriting existing EBOM
copy data.
iCreateRelationships    - Control for creating relationships.
iIncludeJobShopComponents
- Control for including components
already present on job shop in the
EBOM copy.
iOverwriteItemInProduction
- Control for overwriting Item in
Production.
iOverwriteItemDescription
- Control for overwriting Item
Description and Search Keys.
iCopyAttachedDocuments  - Control for copying Attached
Documents.
iCopyDocumentLinks      - Control for copying Document Links.
iIncludeAlternatives    - Control for including Alternative
Materials.
iIncludeUseUpMaterials  - Control for including Use-Up
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Generate EBOM Copy Data is successful.
<> 0                    - Generate EBOM Copy Data is not
successful.
```
