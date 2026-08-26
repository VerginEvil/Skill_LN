# SalesOrderLine.ExecuteTradeComplianceCheck

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 347-347

```baan
DLL:   tdextslsapi
This function is available from     2023.09 (KB2301023  ).
Syntax: long SalesOrderLine.ExecuteTradeComplianceCheck(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Function can be used to execute the sales trade compliance
check and log the related consumption  for the given
sales order line.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales Order (mandatory)
iSalesOrderLine                               - Sales Order Line (mandatory)
iSalesOrderSequence                           - Sales Sequence number
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - The trade compliance check was
executed successfully
<> 0                                          - An error occurred
```
