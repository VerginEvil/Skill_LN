# AdjustmentOrderLine.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for AdjustmentOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 901-902

```baan
DLL:   whextinhapi
This function is available from     2022.01 (KB2223343  ).
Syntax: long AdjustmentOrderLine.Process(
domain  tcorno           iAdjustmentOrder,
domain  tcpono           iAdjustmentOrderLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will process a given adjustment order
line.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iAdjustmentOrder               - The Adjustment Order which needs to
be processed; Mandatory
iAdjustmentOrderLine                       - The Adjustment Order Line which needs to
be processed; Mandatory
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0               - Adjustment Order Line has been processed successfully
<> 0                       - Error.
```
