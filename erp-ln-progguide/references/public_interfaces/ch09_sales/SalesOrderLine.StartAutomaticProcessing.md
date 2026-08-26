# SalesOrderLine.StartAutomaticProcessing

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 357-358

```baan
DLL:   tdextslsapi
This function is available from     2021.03 (KB2173890  ).
Syntax: long SalesOrderLine.StartAutomaticProcessing(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts processing the next sales order line
activity that is set to execute automatically.
This public interface will stop the automatic process when the
next activity is not set to automatic.
This function must not be called within a logical transaction
as this function will have its own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSalesOrder                           - Sales Order (mandatory)
iSalesOrderLine                               - Sales Order Line (mandatory)
iSalesOrderSequence                           - Sales Sequence number
(must be >= 0)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Automatic Processing finished or
next activity is not automatic.
<> 0                                          - Not all mandatory input arguments are
filled.
```
