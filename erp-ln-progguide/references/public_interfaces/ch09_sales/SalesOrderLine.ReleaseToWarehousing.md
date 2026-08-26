# SalesOrderLine.ReleaseToWarehousing

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 355-356

```baan
DLL:   tdextslsapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long SalesOrderLine.ReleaseToWarehousing(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
ref     domain  tcyesno          oReleased,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the release of a sales order line
to Warehousing.
Pre:    Caller must set retry              -point
Post:   * Caller must commit/abort transaction
* Function SalesOrder.FinalizeBlocking must be called
* If desired, function SalesOrderLine.StartAutomaticProcessing
can be called to start any automatic order steps for the given
order (line).
Input:  iSalesOrder                           - Sales Order (Mandatory)
iSalesOrderLine                               - Sales Order Line (Mandatory)
iSalesOrderLineSequence                       - Sales Sequence number (must be >= 0)
Output: oReleased               Yes: The order line has been released to
warehousing
No:  The order line has not been released
to warehousing. Error or
information messages may be present
in oExceptionID.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Release successful
<> 0                                          - Error during release occurred
```
