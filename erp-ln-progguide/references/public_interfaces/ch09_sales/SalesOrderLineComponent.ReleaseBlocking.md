# SalesOrderLineComponent.ReleaseBlocking

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLineComponent
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 361-362

```baan
DLL:   tdextslsapi
This function is available from     2022.05 (KB2223400  ).
Syntax: long SalesOrderLineComponent.ReleaseBlocking(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcpono           iComponentSequence,
domain  tcmcs.hrea       iHoldReason,
domain  tdsls.rlty       iReleaseType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to release (delete) a sales order line
component blocking.
Note: This function should not be used for blockings which
are caused by Trade Compliance related checks.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales Order (mandatory)
iSalesOrderLine                               - Sales Order Line (mandatory)
iSalesOrderSequence                           - Sales Sequence number
iComponentSequence                            - Component Sequence (Mandatory)
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

## Public Interfaces for SalesOrderActualDeliveryLine

The following functions are available: SalesOrderActualDeliveryLine.ReadWarehousingStatusDescription
