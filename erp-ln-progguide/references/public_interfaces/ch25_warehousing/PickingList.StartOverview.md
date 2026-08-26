# PickingList.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PickingList
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1261-1262

```baan
DLL:   whextinhapi
This function is available from     2026.08 (KB3681970  ).
Syntax: long PickingList.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.btno       iRun,
domain  tccwar           iWarehouse,
domain  whinh.picm       iPickingMission,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcorno           oOrderNumber,
ref     domain  tcwset           oOrderSet,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderSequence,
ref     domain  tcpono           oAdvice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Picking List
(whinh4525m100).
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
Not used
iSessionIndex
Not used
iQueryExtend
A specific query to be used when zooming to this session.
iRun
The Run to be started
Mandatory if iStartMode = MODELESS
iWarehouse
The Warehouse to be started
iPickingMission
The Picking Mission to be started
Output: for iStartMode MODAL:
oOrderOrigin                                  - Order Origin of selected record
oOrderNumber                                  - Order Number of selected record
oOrderSet                                     - Order Set of selected record
oOrderLine                                    - Order Line of selected record
oOrderSequence                                - Order Sequence of selected record
oAdvice                                       - Advice of selected record
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

## Public Interfaces for WarehouseInspection

The following functions are available: WarehouseInspection.CopyImage WarehouseInspection.LinkHandlingUnit WarehouseInspection.Print WarehouseInspection.Process WarehouseInspection.StartDetail WarehouseInspection.StartMultiMain WarehouseInspection.StartOverview
