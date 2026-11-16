# JobShopBillOfMaterial.ExpireRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 646-647

```baan
DLL:   tiextbomapi
This function is available from 2021.08 (KB2201787).
Syntax: long JobShopBillOfMaterial.ExpireRevision(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function expires the specified revision. If the revision is
already expired or not allowed, a failure message will be
returned.
It is not allowed to expire a revision if it is used by active
Production Orders.
Pre:    Job Shop by Site must be In Preparation or Active.
Retry point has been set.
Input JSBOM is not yet expired.
Post:   Transaction is aborted or committed.
Input:  iSite                   Site (Mandatory).
iProduct                Product (Mandatory).
iBillOfMaterialCode     BOM Model (Mandatory).
iRevision               Revision (Mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Specified JS BOM Revision has
successfully been expired.
<> 0                    - Specified JS BOM Revision has not been
expired.
```
