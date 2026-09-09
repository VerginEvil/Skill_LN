# GenericAssemblyBillOfMaterial.CreateNewVersion

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for GenericAssemblyBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 833-834

```baan
DLL:   tiextpcfapi
This function is available from 2026.11 (KB3684740).
Syntax: long GenericAssemblyBillOfMaterial.CreateNewVersion(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmrv           iCurrentVersion,
ref     domain  tibmrv           oNewVersion,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface creates a new version of Generic
Assembly Bill of Material record for the input assembly
Bill of Material version.
Pre:    A db.retry.point should be set.
Post:   Commit or abort the transaction.
Input:  iSite                   - Site (Mandatory).
iProduct                - Product (Mandatory).
iCurrentVersion         - Current Version for which the new
version has to be created (Mandatory).
Output: oNewVersion             - The new version which is created.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success. New Version is created
successfully.
<> 0                    - Error occurred during creating of
new version.
```
