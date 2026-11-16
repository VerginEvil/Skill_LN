# PlannedOrders.StartOverview

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 564-565

```baan
DLL:   cpextrrpapi
This function is available from 2020.03 (KB2111387).
Syntax: long PlannedOrders.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iPlanningScenario,
domain  tckoor           iOrderType,
domain  cprrp.orno       iPlannedOrder,
domain  tcemm.clus       iPlanningCluster,
domain  tcsite           iSite,
domain  tcemno           iPlanner,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcemno           iBuyer,
ref     domain  cpcom.plnc       oPlanningScenario,
ref     domain  tckoor           oOrderType,
ref     domain  cprrp.orno       oPlannedOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Planned Orders (cprrp1100m000)
in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The index that will be used.
Supported values:
1: sort by order type
2: sort by cluster / Site
3: sort by Start Date
4: sort by Required Date
5: sort by Planner / Start Date
6: sort by Planner / Order Type
7: sort by Supplier
8: sort by Buyer
iQueryExtend            A specific query to be used when zooming
to this session.
iPlanningScenario       Planning Scenario (Mandatory if iStartMode
is MODELESS)
iOrderType              Order Type (Mandatory if iStartMode is
MODELESS and iSessionIndex is 1 or 6).
iPlannedOrder           Planned Order
iPlanningCluster        Planning Cluster
iSite                   Site
iPlanner                Planner
iBuyFromBusinessPartner
Buy-from Business Partner
iBuyer                  Buyer
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlanningScenario    Planning Scenario
oOrderType           Order Type
oPlannedOrder        Planned Order
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
