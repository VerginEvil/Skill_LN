# GenericAssemblyBillOfMaterial.ActualizeVersion

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for GenericAssemblyBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 833-833

```baan
DLL:   tiextpcfapi
This function is available from 2026.11 (KB3684740).
Syntax: long GenericAssemblyBillOfMaterial.ActualizeVersion(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmrv           iVersion,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface actualizes the input version of
Generic Assembly Bill of Material record.
Pre:    A db.retry.point should be set.
Post:   Commit or abort the transaction.
Input:  iSite                   - Site (Mandatory).
iProduct                - Product (Mandatory).
iVersion                - The version to be actualized
(Mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success. Version is actualized
successfully.
<> 0                    - Error occurred during actualization
of version.
```
