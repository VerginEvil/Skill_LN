# AllocationChangeOrder.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for AllocationChangeOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1112-1113

```baan
DLL:   whextinhapi
This function is available from 2024.09 (KB3516844).
Syntax: long AllocationChangeOrder.Process(
domain  tcorno           iAllocationChangeOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes the given Allocation Change Order.
Only allowed when the Demand Pegging concept is enabled in
Implemented Software Components (tccom0500m000).
This function does not print labels.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iAllocationChangeOrder
The allocation change order number (mandatory).
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0: OK
<> 0: Error
```
