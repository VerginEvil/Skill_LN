# SalesOrder.Rush

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 328-329

```baan
DLL:   tdextslsapi
This function is available from     2026.01 (KB3644594  ).
Syntax: long SalesOrder.Rush(
domain  tcorno           iSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to rush a sales order. It behaves
similar to the functionality provided through the 'Rush'
form command in session 'Sales Orders' (tdsls4100m000).
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales Order (mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - The rush was executed successfully
<> 0                                          - An error occurred
```
