# ProductionBillOfMaterial.CreateNewRevision

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 623-624

```baan
DLL:   tiextmfcapi
This function is available from     2024.07 (KB2318528  ).
Syntax: long ProductionBillOfMaterial.CreateNewRevision(
domain  tcitem           iItem,
domain  tibmrv           iOldRevision,
boolean          iLinkRevision,
ref     domain  tibmrv           oNewRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a new Revision for a
Production Bill of Material.
Pre:    Multi Site setting 'Job Shop by Site' must be In Preparation or
Active.
Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iItem                   Item (Mandatory).
iOldRevision            Old Production Bill of Material Revision
(Mandatory).
iLinkRevision           Link new revision to old revision.
Output: oNewRevision                          - Created Revision.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - PBOM Revision has succesfully
been created.
<> 0                                          - PBOM Revision has not been
created.
```
