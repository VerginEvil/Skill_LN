# WarehouseItemInventory.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseItemInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 980-981

```baan
DLL:   whextwmdapi
This function is available from 2020.03 (KB2111387).
Syntax: long WarehouseItemInventory.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
ref     domain  tccwar           oWarehouse,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Warehouse - Item
Inventory (whwmd2515m000).
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
"byWarehouse":
data is displayed by Warehouse
session will be started on index 1
view field: Warehouse
"byItem":
data is displayed by Item
session will be started on index 2
view fields: Item
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iWarehouse
Mandatory when iStartFilter "byWarehouse" is used or
iSessionIndex = 1 and iStartMode is MODELESS.
iItem
Mandatory when iStartFilter "byItem" is used or
iSessionIndex = 2 and iStartMode is MODELESS.
Output: for iStartMode MODAL:
oWarehouse              - Warehouse of selected inventory.
oItem                   - Item of selected inventory.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
