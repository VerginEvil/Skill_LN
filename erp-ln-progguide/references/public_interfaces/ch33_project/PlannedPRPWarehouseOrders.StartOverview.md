# PlannedPRPWarehouseOrders.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for PlannedPRPWarehouseOrders
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1727-1729

```baan
DLL:   tpextpssapi
This function is available from     2024.11 (KB3522428  ).
Syntax: long PlannedPRPWarehouseOrders.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccprj           iProject,
domain  tppdm.cspa       iElement,
domain  tppdm.cact       iActivity,
domain  tcitem           iItemInProject,
domain  tcitem           iItemInWarehousing,
domain  tccwar           iWarehouse,
domain  tppss.delt       iWarehouseDeliveryType,
domain  tcorno           iWarehouseOrder,
ref     domain  tcorno           oWarehouseOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session
Planned PRP Warehouse Order (tppss6115m000) in overview mode.
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
Not Used.
iSessionIndex
Specifies the session index that is to be used. Please be
aware that iStartFilter will overrule the index passed in
this argument. So when not using start filter the session
index will match the value of this variable.
Allowed values:
1: sort by Project, Planned PRP Warehouse Order
View fields                                          - Project, Project Status
2: sort by Project, Project Item, Planned PRP Warehouse
Order
View fields                                          - Project, Project Status
3: sort by Warehouse Item, Project, Planned PRP Warehouse
Order
View fields                                          - Project, Project Status
4: sort by Warehouse, Delivery Type, Project, Planned
Order
View fields                                          - Warehouse, Delivery Type, Project,
Project Status
5: sort by Planned PRP Warehouse Order
6: sort by Project, Element, Planned PRP Warehouse Order
View fields                                          - Project, Element, Project Status
7: sort by Project, Activity, Planned PRP Warehouse Order
View fields                                          - Project, Activity, Project Status
iQueryExtend
A specific query to be used when zooming to this session.
iProject
Project. Optional
iElement
Element. Optional
iActivity
iActivity. Optional
iItemInProject
Item In Project. Optional
iItemInWarehousing
Item In Warehousing. Optional
iWarehouse
Warehouse. Optional
iWarehouseDeliveryType
Warehouse Delivery Type
Allowed Values:
tppss.delt.wp                                       -  Wrh->Project
tppss.delt.pw                                       -  Project->Wrh
tppss.delt.ww                                       -  Wrh->Wrh
tppss.delt.wb                                       -  Wrh->BP
tppss.delt.pwb                                       - Proj->Wrh->BP
tppss.delt.bw                                       -  BP->Wrh
iWarehouseOrder
Warehouse Order. Optional
Output:
oWarehouseOrder                               - The selected Warehouse Order.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - An error occurred
```
