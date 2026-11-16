# WarehouseInspection.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1278-1280

```baan
DLL:   whextinhapi
This function is available from 2025.08 (KB3615530).
Syntax: long WarehouseInspection.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  whinh.shpm       iReceipt,
domain  tcmcs.st20m      iActivity mb,
domain  whinh.kofr       iInspectionType,
ref     domain  tcorno           oInspection,
ref     domain  tcpono           oInspectionSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Warehouse Inspection
(whinh3122m000).
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
"byInspection":
data is displayed by Inspection
session will be started on index 1
view fields: None
"byOrder":
data is displayed by Order
session will be started on index 2
view fields: Order Origin,
Order Number,
Order Set
"byItem":
data is displayed by Item
session will be started on index 3
view field: Item
"byWarehouse":
data is displayed by Warehouse
session will be started on index 4
view field: None
"byReceipt":
data is displayed by Receipt
session will be started on index 5
view field: Receipt
"byActivity":
data is displayed by Activity
session will be started on index 6
view field: Activity
"byInspectionType":
data is displayed by Inspection Type
session will be started on index 7
view field: Inspection Type
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
Optional.
A specific query to be used when starting the session.
Use this to specify a filter, e.g.
"whinh211.apst = whinh.apst.in.process"
Using the query extend may lead to a
"data not found, session not started" situation.
iInspection
The Inpection Number to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byInspection")
iInspectionSequence
The Inpection Sequence to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byInspection")
iOrderOrigin
The Order Origin to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byOrder")
iOrderNumber
The Order Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byOrder")
iOrderSet
The Order Set to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byOrder")
iItem
The Item to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 3 (or iStartFilter = "byItem")
iWarehouse
The Warehouse to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 4 (or iStartFilter = "byWarehouse")
iReceipt
The Receipt Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 5 (or iStartFilter = "byReceipt")
iActivity
The Activity to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 6 (or iStartFilter = "byActivity")
iInspectionType
The Inspection Type to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 7 (or iStartFilter = "byInspectionType")
Output: for iStartMode MODAL:
oInspection          - Inspection Number of selected record
oInspectionSequence  - Inspection Sequence of selected record
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
