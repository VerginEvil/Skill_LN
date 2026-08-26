# SalesOrderLine.ReleaseBlocking

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 354-355

```baan
DLL:   tdextslsapi
This function is available from     2022.05 (KB2223400  ).
Syntax: long SalesOrderLine.ReleaseBlocking(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcmcs.hrea       iHoldReason,
domain  tdsls.rlty       iReleaseType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to release (delete) a sales order line
blocking.
Note: This function should not be used for blockings which
are caused by Trade Compliance related checks.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales Order (mandatory)
iSalesOrderLine                               - Sales Order Line (mandatory)
iSalesOrderSequence                           - Sales Sequence number
(must be >= 0)
iHoldReason                                   - Hold Reason (Mandatory)
iReleaseType                                  - Release Type (Soft / Firm)
Output: oExceptionMessage                     - The last message if any message is
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
