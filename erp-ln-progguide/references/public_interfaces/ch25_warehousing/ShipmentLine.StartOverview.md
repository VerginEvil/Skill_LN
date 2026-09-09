# ShipmentLine.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1181-1182

```baan
DLL:   whextinhapi
This function is available from 2023.02 (KB2280147).
Syntax: long ShipmentLine.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  whinh.shst       iStatus,
domain  tcitem           iItem,
domain  tcrefs           iShipmentReference mb,
domain  tccorn           iCustomerOrder mb,
ref     domain  whinh.shpm       oShipment,
ref     domain  tcpono           oShipmentLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Shipment Lines
(whinh4131m000).
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
started MULTI_OCC session.
Possible values are:
"byShipment":
data is displayed by Shipment
session will be started on index 1
view field: Shipment
"byOrder":
data is displayed by Order
session will be started on index 2
view field: Order Origin, Order
"byActivity":
data is displayed by Activity
session will be started on index 3
view field: None
"byOrderSet":
data is displayed by Order Set
session will be started on index 4
view field: Order Origin, Order, Order Set
"byItem":
data is displayed by Item
session will be started on index 5
view field: Item
"byShipmentReference":
data is displayed by Shipment Reference
session will be started on index 6
view field: Shipment Reference
"byCustomerOrder":
data is displayed by Customer Order
session will be started on index 7
view field: Customer Order
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iShipment
The Shipment to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byShipment")
iShipmentLine
Optional
iOrderOrigin
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 or 4
(or iStartFilter = "byOrder"   or
or iStartFilter = "byOrderSet"  )
iOrder
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 or 4
(or iStartFilter = "byOrder"   or
or iStartFilter = "byOrderSet"  )
iOrderSet
Mandatory if iStartMode = MODELESS and
iSessionIndex = 4 (or iStartFilter = "byOrderSet")
iOrderLine
Optional
iOrderSequence
Optional
iStatus
Optional
iItem
Mandatory if iStartMode = MODELESS and
iSessionIndex = 5 (or iStartFilter = "byItem")
iShipmentReference
Optional
iCustomerOrder
Optional
Output: for iStartMode MODAL:
oShipment               - selected shipment
oShipmentLine           - selected shipment line
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
