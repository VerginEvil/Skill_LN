# QuarantineInventory.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1216-1218

```baan
DLL:   whextwmdapi
This function is available from 2022.07 (KB2247580).
Syntax: long QuarantineInventory.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iQuarantineIdentifier,
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcorno           oQuarantineIdentifier,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts session Quarantine Inventory
(whwmd2171m000) in Overview Mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byQuarantineId":
data is displayed by Quarantine ID
session will be started on index 1
view fields: Quarantine ID
"byWarehouseLocation":
data is displayed by Warehouse and Location
session will be started on index 2
view fields: Warehouse, Location
"byItemWarehouseLocation":
data is displayed by Item, Warehouse and Location
session will be started on index 3
view fields: Item, Warehouse, Location
"byOrderLine":
data is displayed by Order Line
session will be started on index 4
view fields: Order Origin, Order, Order Set,
Order Line, Order Sequence
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iQuarantineIdentifier
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byQuarantineId")
iWarehouse
Optional
iLocation
Optional
iItem
Optional
iOrderOrigin
Mandatory if iStartMode = MODELESS and
iSessionIndex = 4 (or iStartFilter = "byOrderLine")
iOrder
Optional
iOrderSet
Optional
iOrderLine
Optional
iOrderSequence
Optional
Output: oQuarantineIdentifier   - Quarantine ID of the selected record,
if iStartMode = MODAL.
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
