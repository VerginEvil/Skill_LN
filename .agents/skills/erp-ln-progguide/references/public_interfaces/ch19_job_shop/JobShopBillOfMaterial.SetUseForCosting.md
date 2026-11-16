# JobShopBillOfMaterial.SetUseForCosting

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 650-651

```baan
DLL:   tiextbomapi
This function is available from 2021.05 (KB2156270).
Syntax: long JobShopBillOfMaterial.SetUseForCosting(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function sets the Use For Costing flag to true for a Job
Shop Bill of Material.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   - Site (Mandatory).
iProduct                - Product (Mandatory).
iBillOfMaterialCode     - Bill Of Material Model (Mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Use for Costing set to true.
<> 0                    - Otherwise.
```
