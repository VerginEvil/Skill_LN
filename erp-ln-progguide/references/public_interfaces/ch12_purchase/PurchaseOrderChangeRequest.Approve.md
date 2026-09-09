# PurchaseOrderChangeRequest.Approve

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderChangeRequest
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 480-481

```baan
DLL:   tdextpurapi
This function is available from 2024.04 (KB2323365).
Syntax: long PurchaseOrderChangeRequest.Approve(
domain  tcorno           iChangeRequest,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function approves a modified purchase order change request.
If Change Requests are setup to be processed automatically after
approval, then processing the Change Request will be done as
well.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iChangeRequest          - Purchase Order Change Request (mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       -> The change request has been approved
<> 0    -> An error occurred
```
