# LotInventoryByWarehouseAndItem.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for LotInventoryByWarehouseAndItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1112-1114

```baan
DLL:   whextltcapi
This function is available from     2023.02 (KB2280148  ).
Syntax: long LotInventoryByWarehouseAndItem.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcclot           iLot,
ref     domain  tccwar           oWarehouse,
ref     domain  tcitem           oItem,
ref     domain  tcclot           oLot,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Warehouse - Item -
Lots Inventory (whltc1505m000).
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
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byWarehouseItem":
data is displayed by Warehouse, Item
session will be started on index 1
view field: Warehouse, Item
"byItem":
data is displayed by Item, Lot
session will be started on index 2
view field: Item, Lot
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iWarehouse
Mandatory when startfilter "byWarehouseItem" is used and
the session is started in overview mode with start mode
MODELESS
iItem
Mandatory when startfilter "byItem" and the session
is started in overview mode with start mode MODELESS
iLot
Mandatory when startfilter "byItem" and the session
is started in overview mode with start mode MODELESS
Output: for iStartMode MODAL:
oWarehouse                                    - Selected Warehouse.
oItem                                         - Selected Item.
oLot                                          - Selected Lot.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for SerialsByWarehouse

The following functions are available: SerialsByWarehouse.StartDetail SerialsByWarehouse.StartOverview
