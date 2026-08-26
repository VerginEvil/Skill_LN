# SerialsByWarehouse.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for SerialsByWarehouse
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1115-1118

```baan
DLL:   whextltcapi
This function is available from     2021.04 (KB2179943  ).
Syntax: long SerialsByWarehouse.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tccwar           iWarehouse,
domain  tcclot           iLot,
domain  whloca           iLocation,
domain  tcinvt.date      iInventoryDate,
domain  tccom.bpid       iBusinessPartner,
ref     domain  tcitem           oItem,
ref     domain  tcibd.sern       oSerialNumber,
ref     domain  tccwar           oWarehouse,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Item - Serials and
Warehouses (whltc5100m000).
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
"byItem":
data is displayed by:
Item
Serial Number
Warehouse
session will be started on index 1
view field:
Item
"byItemLot":
data is displayed by:
Item
Lot
Serial Number
Warehouse
session will be started on index 2
view fields:
Item
Lot
"byItemWarehouse":
data is displayed by:
Item
Warehouse
Serial Number
session will be started on index 3
view fields:
Item
Warehouse
"byWarehouseItemLocation":
data is displayed by:
Warehouse
Item
Location
Serial Number
session will be started on index 4
view fields:
Warehouse
Item
Location
"byWarehouseLocationItem":
data is displayed by:
Warehouse
Location
Item
Lot
Inventory Date
Serial Number
session will be started on index 5
view fields:
Warehouse
Location
Item
Lot
Inventory Date
"byItemBusinessPartner":
data is displayed by:
Item
Business Partner
Serial Number
Warehouse
session will be started on index 6
view fields:
Item
Business Partner
"byItemWarehouseBusinessPartner":
data is displayed by:
Item
Warehouse
Business Partner
Serial Number
session will be started on index 7
view fields:
Item
Warehouse
Business Partner
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
i.item
Mandatory when startfilter "byItem",
"byItemLot", "byItemWarehouse",
"byWarehouseLocationItem", "byItemBusinessPartner" or
"byItemWarehouseBusinessPartner" is used and the session
is started in overview mode with start mode MODELESS
i.serial.number
i.warehouse
Mandatory when startfilter "byItemWarehouse",
"byWarehouseItemLocation", "byWarehouseLocationItem" or
"byItemWarehouseBusinessPartner" is used and the session
is started in overview mode with start mode MODELESS
i.lot
i.warehouse
Mandatory when startfilter "byItemLot" or
"byWarehouseLocationItem" is used and the session
is started in overview mode with start mode MODELESS
i.location
Mandatory when startfilter "byWarehouseItemLocation" or
"byWarehouseLocationItem" is used and the session
is started in overview mode with start mode MODELESS
i.inventory.date
Mandatory when startfilter "byWarehouseItemLocation" is
used and the session is started in overview mode with
start mode MODELESS
i.business.partner
Mandatory when startfilter "byItemBusinessPartner" or
"byItemWarehouseBusinessPartner" is used and the session
is started in overview mode with start mode MODELESS
Output: for iStartMode MODAL:
oItem                                         - Selected Item.
oSerialNumber                                 - Selected Serial Number.
oWarehouse                                    - Selected Warehouse.
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

## Public Interfaces for ItemLotSerialTransaction

The following functions are available: ItemLotSerialTransaction.GetData ItemLotSerialTransactions.Get ItemLotSerialTransactions.StartOverview
