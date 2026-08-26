# JobShopBillOfMaterial.GetSourceEngineeringRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 646-646

```baan
DLL:   tiextbomapi
This function is available from     2025.10 (KB3629872  ).
Syntax: long JobShopBillOfMaterial.GetSourceEngineeringRevision(
domain  tcsite           iSite,
domain  tcitem           iItem,
domain  tibmdl           iBomModel,
domain  tibmrv           iModelRevision,
ref     domain  tiedm.revi       oSourceEngineeringRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to read the Source Engineering Revision
for a given Job Shop Bill of Material.
Input:
iSite                   Site (Mandatory)
iItem                   Item (Mandatory)
iBomModel               Bom Model (Mandatory)
iModelRevision          Model Revision (Mandatory)
Output:
oSourceEngineeringRevision
The found Source Engineering Revision.
Can be empty.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
Return: 0                       Function is executed successfully.
<> 0                    Errors occurred.
```
