# StockPointInventory.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StockPointInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1000-1001

```baan
DLL:   whextinrapi
This function is available from 2023.09 (KB2297960).
Syntax: long StockPointInventory.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tctrns.date      iInventoryDate,
ref     domain  tccwar           oWarehouse,
ref     domain  whloca           oLocation,
ref     domain  tcitem           oItem,
ref     domain  tcclot           oLot,
ref     domain  tctrns.date      oInventoryDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Stock Point Inventory
(whinr1540m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byItemWarehouse":
data is displayed by Item and Warehouse
session will be started on index 1
view fields: Item, Warehouse
"byWarehouse":
data is displayed by Warehouse
session will be started on index 2
view field: Warehouse
"byWarehouseItem":
data is displayed by Warehouse and Item
session will be started on index 3
view fields: Warehouse, Item
"byWarehouseLocation":
data is displayed by Warehouse, Location and
Item
session will be started on index 4
view fields: Warehouse, Location, Item
"byItemLot":
data is displayed by Item and Lot
session will be started on index 5
view fields: Item, Lot
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iWarehouse
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1,2,3 or 4
(or iStartFilter = "byItemWarehouse"
or iStartFilter = "byWarehouse"
or iStartFilter = "byWarehouseItem"
or iStartFilter = "byWarehouseLocation")
iLocation
Optional
iItem
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1,3,4 or 5
(or iStartFilter = "byItemWarehouse"
or iStartFilter = "byWarehouseItem"
or iStartFilter = "byWarehouseLocation"
or iStartFilter = "byItemLot")
iLot
Optional
iInventoryDate
Optional
Output: for iStartMode MODAL:
oWarehouse      - Warehouse of selected record
oLocation       - Location of selected record
oItem           - Item of selected record
oLot            - Lot of selected record
oInventoryDate  - Inventory Date of selected record
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
