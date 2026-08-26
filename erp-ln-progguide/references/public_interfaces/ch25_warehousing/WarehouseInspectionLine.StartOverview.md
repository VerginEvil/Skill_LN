# WarehouseInspectionLine.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspectionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1273-1275

```baan
DLL:   whextinhapi
This function is available from     2022.05 (KB2240600  ).
Syntax: long WarehouseInspectionLine.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
long             iInspectionLine,
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
ref     domain  tcorno           oInspection,
ref     domain  tcpono           oInspectionSequence,
ref             long             oInspectionLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts session Warehouse Inspection Lines
(whinh2131m000) in Overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, in case of a
multi                                              -occurrence the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byInspectionLine"
Data is displayed by Inspection Line
session will be started on index 1
view fields: Inspection, Inspection Sequence
"byReceiptLine"
Data is displayed by Receipt Line
session will be started on index 2
view fields: Receipt, Receipt Line
"byOrder"
Data is displayed by Warehousing Order
session will be started on index 3
view fields: Order Origin, Order, Order Set
"byItem"
Data is displayed by Item
session will be started on index 4
view fields: Item
"byWarehouseLocation"
Data is displayed by Warehouse Location
session will be started on index 5
view fields: Warehouse, Location
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session
iInspection
The Inspection Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byInspectionLine")
iInspectionSequence
The Inspection Sequence to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byInspectionLine")
iInspectionLine
The Inspection Line to be started. Optional.
iReceipt
Optional
iReceiptLine
Optional
iOrderOrigin
Mandatory if iStartMode = MODELESS and
iSessionIndex = 3 (or iStartFilter = "byOrder")
iOrder
Optional
iOrderSet
Optional
iItem
Optional
iWarehouse
Optional
iLocation
Optional
Output: oInspection                           - Inspection Number of selected record
oInspectionSequence                           - Inspection Sequence of selected record
oInspectionLine                               - Inspection Line of selected record
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

## Public Interfaces for InventoryInspection

The following functions are available: InventoryInspection.Generate
