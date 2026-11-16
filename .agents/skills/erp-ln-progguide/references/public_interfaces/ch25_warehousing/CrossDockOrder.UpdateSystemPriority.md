# CrossDockOrder.UpdateSystemPriority

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for CrossDockOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1314-1315

```baan
DLL:   whextinhapi
This function is available from 2026.09 (KB3694657).
Syntax: long CrossDockOrder.UpdateSystemPriority(
domain  tccwar           iWarehouseFrom,
domain  tccwar           iWarehouseTo,
domain  tcitem           iItemFrom,
domain  tcitem           iItemTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will update the system priority of all
cross-dock orders for the given item and warehouse range.
It will only do this for cross-dock orders that have status
Open, Planned, In Process or Staged.
When errors occur during the process the errors are visible
in the oExceptionID and the last message is present in
oExceptionMessage.
Pre:    db.retry.point() must have been set.
Post:   Commit or abort the transaction
Input:  iWarehouseFrom          - Warehouse from (Optional)
iWarehouseTo            - Warehouse to (Optional)
iItemFrom               - Item from (Optional)
iItemTo                 - Item to (Optional)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
