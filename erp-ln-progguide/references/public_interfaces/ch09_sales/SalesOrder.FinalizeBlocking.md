# SalesOrder.FinalizeBlocking

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 322-322

```baan
DLL:   tdextslsapi
This function is available from 2023.04 (KB2286306).
Syntax: long SalesOrder.FinalizeBlocking(
domain  tcorno           iSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the creation of a Blocking record if
required. This is required for instance if release to warehousing
is aborted because the credit check failed.
Pre:    - Caller must set the retry-point.
Note that if this function is called after a failing sales
order line activity (like Release to Warehousing, Confirm
Shipment), then that transaction must have been aborted and a
new transaction started prior to calling this function.
- A relevant function (like SalesOrderLine.ReleaseToWarehousing)
must have been called for the same order number, prior to
calling this function.
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales Order (mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Finalize was successful
<> 0                    - An error occurred
```
