# ConformanceDocumentationRegister.StartMultiMain

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for ConformanceDocumentationRegister
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1799-1800

```baan
DLL:   qmextptcapi
This function is available from 2024.08 (KB3501672).
Syntax: long ConformanceDocumentationRegister.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  qmptc.orgn       iOrigin,
domain  tcorno           iOrderNumber,
domain  qmptc.pono       iOrderLine,
domain  tcpono           iSequence,
domain  tcorno           iWarehouseInspectionOrder,
domain  tcpono           iWarehouseInspectionOrderLine,
domain  qmptc.iorn       iInspectionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Multi-Main session "Conformance Documentation
Register" (qmptc1650m000)
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
iOrigin
The origin of the order linked to the conformance document.
Mandatory.
Allowed Values:
- Purchase (qmptc.orgn.purchase)
- Production (JSC) (qmptc.orgn.production)
- Routing (TI) (qmptc.orgn.rou.ti)
- Purchase Schedule (qmptc.orgn.purchase.sched)
- Sales (qmptc.orgn.sales)
- Sales Schedule (qmptc.orgn.sales.sched)
- Inventory Inspection (qmptc.orgn.inv.insp)
- Warehouse Transfer (qmptc.orgn.cwar.trans)
- Warehouse Transfer (Manual) (qmptc.orgn.cwar.trans.man)
- EP Distribution (qmptc.orgn.enterprise.plan)
- Service (qmptc.orgn.service)
- Maintenance Sales (qmptc.orgn.maint.sales)
- Maintenance Work (qmptc.orgn.maint.work)
- Project Contract (qmptc.orgn.prj.contract)
iOrderNumber
Order Number. Optional.
iOrderLine
Order Line. Optional.
iSequence
Sequence Number. Optional.
iWarehouseInspectionOrder
Warehouse inspection order number. Optional.
iWarehouseInspectionOrderLine
Warehouse inspection order line corresponding to the
warehouse inspection order number. Optional.
iInspectionOrder
Inspection order linked to conformance report. Optional.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
