# ItemWarehouseFixedLocation.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemWarehouseFixedLocation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 922-923

```baan
DLL:   whextwmdapi
This function is available from 2020.03 (KB2111387).
Syntax: long ItemWarehouseFixedLocation.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
ref     domain  tcitem           oItem,
ref     domain  tccwar           oWarehouse,
ref     domain  whloca           oLocation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Fixed Locations
(whwmd3502m000).
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
"byWarehouseLocation":
data is displayed by Warehouse
session will be started on index 2
view field: Warehouse
"byItemWarehousePriority":
data is displayed by Item and Warehouse
session will be started on index 3
view field: Item, Warehouse
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iItem
Mandatory when iStartFilter "byItemWarehouse" or
"byItemWarehousePriority" is used or iSessionIndex is
1 or 3, and iStartMode is MODELESS.
iWarehouse
Mandatory when iStartFilter "byItemWarehouse" or
"byItemWarehousePriority" or "byWarehouseLocation" is
used or iSessionIndex 1 or 3 and iStartMode
is MODELESS.
Output: for iStartMode MODAL:
oWarehouse              - Warehouse of selected fixed location.
oItem                   - Item of selected fixed location.
oLocation               - Location of selected fixed location.
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
