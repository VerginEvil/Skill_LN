# SalesOrderLine.CreateSalesDelivery

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 348-348

```baan
DLL:   tdextslsapi
This function is available from 2023.04 (KB2285765).
Syntax: long SalesOrderLine.CreateSalesDelivery(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
boolean          iConfirm,
ref     domain  tcpono           oSalesDeliverySequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This functions handles the creation of a Sales Delivery Line.
Pre:    Caller must set retry-point.
Post:   * Caller must commit/abort transaction
* Function SalesOrder.FinalizeBlocking must be called
afterwards, in a new transaction, because a Blocking record
may need to be created for Price Stage blocking.
Input:  iSalesOrder                     - Sales Order (Mandatory)
iSalesOrderLine                 - Sales Order Line (Mandatory)
iSalesOrderSequence             - Sales Sequence
(must be >= 0)
iConfirm                true: The created sales delivery line
will also be confirmed.
false:
The created sales delivery line
will not be confirmed.
Output: oSalesDeliverySequence  Sales Delivery Sequence that has been
created.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Creation was successful
<> 0                    Error during creation occurred.
```
