# SalesOrder.Block

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 313-314

```baan
DLL:   tdextslsapi
This function is available from 2022.11 (KB2257724).
Syntax: long SalesOrder.Block(
domain  tcorno           iSalesOrder,
domain  tcmcs.hrea       iHoldReason,
domain  tctrns.date      iExpectedReleaseDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to block a sales order. It behaves
similar to the functionality provided through session
'Sales Order (Line) Blocking' (tdsls4120s000).
Note: This function should not be used for blockings which
are related to Trade Compliance.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales Order (mandatory)
iHoldReason             - Hold Reason (Mandatory)
* Hold Reasons with a Trade Compliance
related category are not allowed.
* A Hold Reason that is used as
'Credit Limit Hold Reason' in Sales
Order Parameters/Sales Office Settings
is not allowed.
iExpectedReleaseDate    - Expected Release Date. Optional; if
the value zero (0) is passed, then
the system will determine the expected
release date based on the maximum
holding days as defined for the
business partner type and hold reason.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The block was executed successfully
<> 0                    - An error occurred
```
