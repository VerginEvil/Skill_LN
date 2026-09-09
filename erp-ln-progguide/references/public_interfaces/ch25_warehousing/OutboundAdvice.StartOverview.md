# OutboundAdvice.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1202-1205

```baan
DLL:   whextinhapi
This function is available from 2022.07 (KB2243668).
Syntax: long OutboundAdvice.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdvice,
domain  whinh.btno       iRun,
domain  tcmcs.st20m      iActivity mb,
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcclot           iLot,
domain  tcinvt.date      iInventoryDate,
domain  tcyesno          iPicked,
domain  tccuni           iUnit,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcorno           oOrderNumber,
ref     domain  tcwset           oOrderSet,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderSequence,
ref     domain  tcpono           oAdvice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Outbound Advice
(whinh4525m000).
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
"byOrder":
data is displayed by Order
session will be started on index 1
view field: None
"byRun":
data is displayed by Run
session will be started on index 4
view field: Run
"byActivity":
data is displayed by Activity
session will be started on index 6
view field: Activity
"byItem":
data is displayed by Item
session will be started on index 5
view field: Item
"byWarehouse":
data is displayed by Warehouse
session will be started on index 2
view field: Warehouse
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iOrderOrigin
The Order Origin to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrder")
iOrderNumber
The Order Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrder")
iOrderSet
The Order Set to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrder")
iOrderLine
The Order Line to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrder")
iOrderSequence
The Order Sequence to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrder")
iAdvice
The Advice to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrder")
iRun
The Run to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 4 (or iStartFilter = "byRun")
iActivity
The Activity to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 6 (or iStartFilter = "byActivity")
iItem
The Item to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 5 (or iStartFilter = "byItem")
iWarehouse
The Warehouse to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byWarehouse")
iLocation
Optional
iLot
Optional
iInventoryDate
Optional
iPicked
Optional
iUnit
Optional
Output: for iStartMode MODAL:
oOrderOrigin    - Order Origin of selected record
oOrderNumber    - Order Number of selected record
oOrderSet       - Order Set of selected record
oOrderLine      - Order Line of selected record
oOrderSequence  - Order Sequence of selected record
oAdvice         - Advice of selected record
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
