# WarehouseOrderLine.Activate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1284-1284

```baan
DLL:   whextinhapi
This function is available from     2022.05 (KB2237106  ).
Syntax: long WarehouseOrderLine.Activate(
domain  whinh.oorg       iWarehouseOrderOrigin,
domain  tcorno           iWarehouseOrder,
domain  tcpono           iWarehouseOrderLine,
domain  tcpono           iWarehouseOrderSequence,
domain  whinh.ittp       iTransactionType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will activate a given warehouse order line.
It must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before
calling this function.
Post:   No need to commit or abort the process, that is handled
within the function.
Input:  iWarehouseOrderOrigin
The Order origin to be activated. This is mandatory to
fill.
iWarehouseOrder
Order number to be activated. This is mandatory to fill.
iWarehouseOrderLine
Order line number to be activated. Optional to
fill. A warehouse order line can have line number 0.
iWarehouseOrderSequence
Order line sequence to be activated. Optional to
fill. A warehouse order sequence can have sequence 0.
iTransactionType
Indicator for what type of order line has to be
activated. This is mandatory to fill.
Possible values are:
Receipt (1)                               -   An inbound order line will be activated.
Issue (2)                               -     An outbound order line will be activated.
Transfer (3)                               -  An outbound order line will be activated.
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0               - Warehouse Order Line has been activated successfully
<> 0                       - Error.
```
