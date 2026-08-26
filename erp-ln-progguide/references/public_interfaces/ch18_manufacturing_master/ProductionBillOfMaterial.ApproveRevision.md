# ProductionBillOfMaterial.ApproveRevision

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 621-622

```baan
DLL:   tiextmfcapi
This function is available from     2021.01 (KB2155728  ).
Syntax: long ProductionBillOfMaterial.ApproveRevision(
domain  tcitem           iProduct,
domain  tibmrv           iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to approve the specified Production
Bill of Material Revision.
In case Electronic Signature is required this function cannot
be used.
Pre:    Multi Site setting 'Job Shop by Site' must be In Preparation or
Active.
Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iProduct                              - Product ID. (mandatory).
iRevision                                     - Revision Number (mandatory).
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - PBOM Revision is set to Approved
<> 0                                          - PBOM Revision could not be Approved
```
