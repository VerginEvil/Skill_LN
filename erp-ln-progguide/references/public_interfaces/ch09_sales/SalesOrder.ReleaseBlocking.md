# SalesOrder.ReleaseBlocking

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 330-330

```baan
DLL:   tdextslsapi
This function is available from 2022.05 (KB2223400).
Syntax: long SalesOrder.ReleaseBlocking(
domain  tcorno           iSalesOrder,
domain  tcmcs.hrea       iHoldReason,
domain  tdsls.rlty       iReleaseType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to release (delete) a sales order blocking.
Note that this function will only release blockings that are
linked on header level. Blockings that are done on line level or
component level must be released separately, using function
SalesOrderLine.ReleaseBlocking and
SalesOrderLineComponent.ReleaseBlocking respectively.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales Order (mandatory)
iHoldReason             - Hold Reason (Mandatory)
iReleaseType            - Release Type (Soft / Firm)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Release successful
<> 0                    - Error during release occurred
```
