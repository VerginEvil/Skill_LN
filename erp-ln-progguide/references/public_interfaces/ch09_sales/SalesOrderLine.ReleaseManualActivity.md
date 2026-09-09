# SalesOrderLine.ReleaseManualActivity

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 357-357

```baan
DLL:   tdextslsapi
This function is available from 2025.12 (KB3638043).
Syntax: long SalesOrderLine.ReleaseManualActivity(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
ref     domain  tcmcs.st20m      oActivity mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function releases a manual activity for a sales order line.
Note: This function does not trigger any automatic processing
afterwards, if applicable.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales order (mandatory)
iSalesOrderLine         - Sales order line (mandatory)
iSalesOrderLineSequence - Sales order line sequence
Output: oActivity               - The released manual activity, if applicable
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The manual activity is released
<> 0                    - An error occurred
```
