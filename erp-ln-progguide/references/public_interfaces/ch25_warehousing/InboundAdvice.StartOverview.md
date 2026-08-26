# InboundAdvice.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1073-1076

```baan
DLL:   whextinhapi
This function is available from     2025.04 (KB3566675  ).
Syntax: long InboundAdvice.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iAdvice,
domain  tcpono           iAdviceLine,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
domain  tcmcs.st20m      iActivity mb,
domain  whinh.btno       iRun,
domain  whhuid           iToHandlingUnit,
domain  tcitem           iItem,
domain  tcorno           iQuarantineInventory,
ref     domain  tcorno           oAdvice,
ref     domain  tcpono           oAdviceLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Inbound Advice
(whinh3525m000).
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
"byOrder":
data is displayed by Order
session will be started on index 2
view fields: Order Origin,
Order Number,
Order Set
"byAdvice":
data is displayed by Advice
session will be started on index 1
view field: None
"byReceipt":
data is displayed by Receipt
session will be started on index 6
view field: Receipt
"byInspection":
data is displayed by Inspection
session will be started on index 7
view field: Inspection
"byActivity":
data is displayed by Activity
session will be started on index 3
view field: Activity
"byRun":
data is displayed by Run
session will be started on index 4
view field: Run
"byHandlingUnit":
data is displayed by To Handling Unit
session will be started on index 8
view field: None
"byItem":
data is displayed by Item
session will be started on index 5
view field: Item
"byRejection":
data is displayed by Rejection
session will be started on index 9
view field: Rejection
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
Optional.
A specific query to be used when starting the session.
Use this to specify a filter, e.g.
"whinh215.puta = tcyesno.no"
Using the query extend may lead to a
"data not found, session not started" situation.
iAdvice
The Advice Number to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byAdvice")
iAdviceLine
The Advice Line to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byAdvice")
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
iOrderLine
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byOrder")
iOrderSequence
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byOrder")
iReceipt
The Receipt Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 6 (or iStartFilter = "byReceipt")
iReceiptLine
The Receipt Line to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 6 (or iStartFilter = "byReceipt")
iInspection
The Inspection Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 7 (or iStartFilter = "byInspection")
iInspectionSequence
The Inspection Sequence to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 7 (or iStartFilter = "byInspection")
iActivity
The Activity to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 3 (or iStartFilter = "byActivity")
iRun
The Run to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 4 (or iStartFilter = "byRun")
iHandlingUnit
The To Handling Unit to be started
Optional. Can be used when iStartMode = MODELESS and
iSessionIndex = 8 (or iStartFilter = "byHandlingUnit")
iItem
The Item to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 5 (or iStartFilter = "byItem")
iQuarantineInventory
The Quarantine ID to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 9 (or iStartFilter = "byRejection")
Output: for iStartMode MODAL:
oAdvice                                       - Advice Number of selected record
oAdviceLine                                   - Advice Line of selected record
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

## Public Interfaces for InboundInspection

The following functions are available: InboundInspection.StartAutomaticInboundProcessing
