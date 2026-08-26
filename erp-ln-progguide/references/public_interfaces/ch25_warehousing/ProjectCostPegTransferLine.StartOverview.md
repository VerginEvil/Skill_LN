# ProjectCostPegTransferLine.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectCostPegTransferLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1097-1099

```baan
DLL:   whextinhapi
This function is available from     2023.08 (KB2296385  ).
Syntax: long ProjectCostPegTransferLine.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iProjectCostPegTransfer,
domain  tcpono           iProjectCostPegTransferLine,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdvice,
domain  tcitem           iItem,
domain  tccprj           iFromProject,
domain  tcpdm.cspa       iFromElement,
domain  tcpdm.cact       iFromActivity,
domain  tccprj           iToProject,
domain  tcpdm.cspa       iToElement,
domain  tcpdm.cact       iToActivity,
ref     domain  tcorno           oProjectCostPegTransfer,
ref     domain  tcpono           oProjectCostPegTransferLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Project Cost Peg
Transfer Lines (whinh1145m000).
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
"byOrderLine":
Project Cost Peg Transfer Lines are displayed
by project cost peg transfer.
session will be started on index 1
view fields: Project cost peg transfer
"byRelatedOrderLine":
Project Cost Peg Transfer Lines are displayed
by related order line.
session will be started on index 2
view fields: Order Origin
Order Number
Order Set
Order Line
"byItem":
Project Cost Peg Transfer Lines are displayed
by item.
session will be started on index 3
view fields: Item
"byFromPeg":
Project Cost Peg Transfer Lines are displayed
by from peg.
session will be started on index 4
view fields: From Project
"byToPeg":
Project Cost Peg Transfer Lines are displayed
by to peg.
session will be started on index 5
view fields: To Project
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iProjectCostPegTransfer
The Project Cost Peg Transfer to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrderLine")
iProjectCostPegTransferLine
The Project Cost Peg Transfer Line to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrderLine")
iOrderOrigin
The Order Origin to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byRelatedOrderLine")
iOrderNumber
The Order Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byRelatedOrderLine")
iOrderSet
The Order Set to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byRelatedOrderLine")
iOrderLine
The Order Line to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byRelatedOrderLine")
iOrderSequence
Optional
iAdvice
Optional
iItem
The Item to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 3 (or iStartFilter = "byItem")
iFromProject
The From Project to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 4 (or iStartFilter = "byFromPeg")
iFromElement
Optional
iFromActivity
Optional
iToProject
The To Project to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 5 (or iStartFilter = "byToPeg")
iToElement
Optional
iToActivity
Optional
Output: for iStartMode MODAL:
oProjectCostPegTransfer                               -
-                                               Project Cost Peg Transfer of selected
record
oProjectCostPegTransferLine
-                                               Project Cost Peg Transfer Line of
selected record
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

## Public Interfaces for AllocationChangeOrder

The following functions are available: AllocationChangeOrder.Generate AllocationChangeOrder.Process
