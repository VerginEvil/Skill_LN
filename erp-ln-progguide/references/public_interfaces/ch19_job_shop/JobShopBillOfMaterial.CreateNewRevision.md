# JobShopBillOfMaterial.CreateNewRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 645-646

```baan
DLL:   tiextbomapi
This function is available from 2021.11 (KB2216214).
Syntax: long JobShopBillOfMaterial.CreateNewRevision(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
ref     domain  tibmrv           oNewRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to create a new Revision based on
an existing Job Shop Bill of Material.
The BOM lines of the original Bill of Material are copied to the
new Revision.
Pre:    Retry point has been set.
Post:   Abort or commit the transaction.
Input:  iSite
Site (Mandatory).
iProduct
Product (Mandatory).
iBillOfMaterialCode
BOM Model (Mandatory).
iRevision
Revision (Mandatory).
Output: oNewRevision
Created new Job Shop BOM revision.
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
Return: 0       - Function is executed successfully.
<> 0    - An error occurred. A new revision could not be created.
```
