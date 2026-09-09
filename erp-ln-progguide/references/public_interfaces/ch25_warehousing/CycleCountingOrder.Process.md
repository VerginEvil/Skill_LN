# CycleCountingOrder.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for CycleCountingOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 918-919

```baan
DLL:   whextinhapi
This function is available from 2022.10 (KB2261934).
Syntax: long CycleCountingOrder.Process(
domain  tcorno           iOrder,
domain  tcsern           iCountNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will process a given cycle counting order.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iOrder - The Cycle Counting Order which needs to be
processed; Mandatory
iCountNumber - The Count Number of the Cycle Counting Order
which needs to be processed; Mandatory
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0 - Cycle Counting Order has been processed successfully
<> 0 - Error.
```
