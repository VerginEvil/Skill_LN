# SalesOrderLine.ConfirmSalesDelivery

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 340-341

```baan
DLL:   tdextslsapi
This function is available from     2020.11 (KB2148537  ).
Syntax: long SalesOrderLine.ConfirmSalesDelivery(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcpono           iSalesDeliverySequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This functions handles the confirmation of the
Sales Delivery Line.
iSalesDeliverySequence is the sequence from that comes from the
Sales Delivery (tdsls426) record. This record must be present
and allowed to be confirmed.
Pre:    Caller must set retry              -point.
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                                   - Sales Order (Mandatory)
iSalesOrderLine                                       - Sales Order Line (Mandatory)
iSalesOrderSequence                                   - Sales Sequence number
(must be >= 0)
iSalesDeliverySequence                                - Sales Delivery Sequence number
(must be >= 1)
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Confirm successful
<> 0                    Error during confirm occurred.
```
