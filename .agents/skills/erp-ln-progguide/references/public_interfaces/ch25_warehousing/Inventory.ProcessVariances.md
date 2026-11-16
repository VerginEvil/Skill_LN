# Inventory.ProcessVariances

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 959-959

```baan
DLL:   whextinaapi
This function is available from 2026.07 (KB3665122).
Syntax: long Inventory.ProcessVariances(
domain  tckoor           iKindOfOrder,
domain  tcorno           iOrder,
domain  tcpono           iOrderLine,
boolean          iAutomatic,
boolean          iWithCommit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface processes inventory variances manually
and automatically for a specified order or order line.
The function searches for unprocessed inventory variances and
processes them if automatic processing is enabled for the
warehouse/item combination.
Pre:    If iWithCommit is false db.retry.point() must be set.
Otherwise there should be no pending logical transaction before
calling this function.
Post:   If iWithCommit is false commit.transaction() or
abort.transaction() must be done.
If true - no need to commit or abort the process, that is handled
within the function.
Input:  iKindOfOrder
The kind of order for which variances need to be
processed. This is mandatory to fill.
iOrder
The order number for which variances need to be
processed. This is mandatory to fill.
iOrderLine
The order line for which variances need to be
processed. Optional.
If 0, processes all lines of the order.
iAutomatic
If true the function processes inventory variances of
the given order/line automatically.
Process Inventory Variances Automatically option
must be set in session Inventory Analysis Parameters
(whina0100m000).
The not processed inventory variances are searched.
If automatic processing of variances is enabled
for the warehouse and item combination (whwmd2110s000),
the variance is processed.
iWithCommit
Determines whether transaction handling is performed
by this function itself.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0 - The variances have been processed successfully.
<> 0 - Error. The variances could not be processed.
```
