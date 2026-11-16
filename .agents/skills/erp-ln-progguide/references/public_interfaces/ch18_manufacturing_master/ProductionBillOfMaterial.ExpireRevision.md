# ProductionBillOfMaterial.ExpireRevision

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 627-627

```baan
DLL:   tiextmfcapi
This function is available from 2021.08 (KB2202931).
Syntax: long ProductionBillOfMaterial.ExpireRevision(
domain  tcitem           iProduct,
domain  tibmrv           iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function expires the specified revision. If the revision is
already expired an Exception message will be returned.
Pre:    Multi Site setting 'Job Shop by Site' must be In Preparation or
Active.
Retry point has been set.
Specified Production Bill of Material is not yet expired.
Post:   Transaction is aborted or committed.
Input:  iProduct                - Product (Mandatory).
iRevision               - Revision (Mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Specified PBOM Revision has succesfully
been expired.
<> 0                    - Specified PBOM Revision has not been
expired.
```
