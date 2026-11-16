# WarehouseOrder.Activate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1020-1021

```baan
DLL:   whextinhapi
This function is available from 2026.08 (KB3683531).
Syntax: long WarehouseOrder.Activate(
domain  whinh.oorg       iWarehouseOrderOrigin,
domain  tcorno           iWarehouseOrder,
domain  tcwset           iWarehouseOrderSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will activate a given warehouse order.
All order lines within the specified order and order set
will be activated.
This function must not be called within a logical transaction
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
iWarehouseOrderSet
Order set to be activated. This is mandatory to fill.
Output: oExceptionMessage - The last message if any message is found. If
more than one message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0 - Warehouse Order has been activated successfully
<> 0 - Error.
```
