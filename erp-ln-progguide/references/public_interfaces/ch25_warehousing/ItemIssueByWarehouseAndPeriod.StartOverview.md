# ItemIssueByWarehouseAndPeriod.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemIssueByWarehouseAndPeriod
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 922-923

```baan
DLL:   whextinrapi
This function is available from     2025.06 (KB3564424  ).
Syntax: long ItemIssueByWarehouseAndPeriod.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcyrno           iYear,
domain  tcccp.peri       iPeriod,
ref     domain  tccwar           oWarehouse,
ref     domain  tcitem           oItem,
ref     domain  tcyrno           oYear,
ref     domain  tcccp.peri       oPeriod,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Item Issue by
Warehouse and Period (whinr1530m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used
iSessionIndex
Not Used
iQueryExtend
Not Used
iWarehouse
Mandatory
iItem
Mandatory
iYear
Mandatory
iPeriod
Mandatory
Output: for iStartMode MODAL:
oWarehouse                                    - Warehouse of selected record
oItem                                         - Item of selected record
oYear                                         - Year of selected record
oPeriod                                       - Period of selected record
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```

## Public Interfaces for PlannedInventoryTransaction

The following functions are available: PlannedInventoryTransaction.Rebuild PlannedInventoryTransaction.StartDetail PlannedInventoryTransaction.StartOverview
