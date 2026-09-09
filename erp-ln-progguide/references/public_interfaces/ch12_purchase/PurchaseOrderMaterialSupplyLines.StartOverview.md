# PurchaseOrderMaterialSupplyLines.StartOverview

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderMaterialSupplyLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 479-480

```baan
DLL:   tdextpurapi
This function is available from 2025.07 (KB3605556).
Syntax: long PurchaseOrderMaterialSupplyLines.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iPurchaseOrder,
domain  tcpono           iPurchaseOrderLine,
domain  tcpono           iPurchaseOrderLineSequence,
domain  tcpono           iMaterialSequence,
domain  tcitem           iItem,
domain  tcorno           iSupplyOrder,
domain  tcpono           iSupplyOrderLine,
ref     domain  tcorno           oPurchaseOrder,
ref     domain  tcpono           oPurchaseOrderLine,
ref     domain  tcpono           oPurchaseOrderLineSequence,
ref     domain  tcpono           oMaterialSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Purchase Order Material Supply Lines
Overview (tdpur4116m000).
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
Not Used
iSessionIndex
Specifies the session-index that is to be used.
Supported values:
1: sort by Purchase Order, Line, Sequence, Material Sequence
(default)
2: sort by Item
3: sort by Supply Order, Supply Order Line
iQueryExtend
A specific query to be used when zooming to this session.
iPurchaseOrder
Purchase Order
Mandatory if iStartMode = MODELESS and session-index 1 is used.
iPurchaseOrderLine
Purchase Order Line
iPurchaseOrderLineSequence
Purchase Order Line Sequence
iMaterialSequence
Material Sequence
iItem
Item
Mandatory if iStartMode = MODELESS and session-index 2 is used.
iSupplyOrder
Supply Order
iSupplyOrderLine
Supply Order Line
Output: for iStartMode MODAL:
oPurchaseOrder  The selected Purchase Order
oPurchaseOrderLine
The selected Purchase Order Line
oPurchaseOrderLineSequence
The selected Purchase Order Line Sequence
oMaterialSequence
The selected Material Sequence
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
