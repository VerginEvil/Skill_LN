# JobShopBillOfMaterial.ApproveRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 643-644

```baan
DLL:   tiextbomapi
This function is available from 2020.11 (KB2151944).
Syntax: long JobShopBillOfMaterial.ApproveRevision(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to approve the specified Job Shop
Bill of Material Revision.
In case Electronic Signature is required, this function
cannot be not be used for standard items; it can then only be
used for customized items.
Pre:    Job Shop by Site must be In Preparation or Active.
Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory).
iProduct                Main item (mandatory).
iBillOfMaterialCode     BOM Model (mandatory).
iRevision               Revision (mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - JS BOM Revision is set to Approved
<> 0                    - JS BOM Revision could not be Approved
```
