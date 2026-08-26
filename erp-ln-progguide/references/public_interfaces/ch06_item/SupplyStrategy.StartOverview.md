# SupplyStrategy.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for SupplyStrategy
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 235-237

```baan
DLL:   cpextrpdapi
This function is available from     2024.07 (KB2329980  ).
Syntax: long SupplyStrategy.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iPlanningScenario,
domain  cpcom.plvl       iPlanLevel,
domain  tcemm.clus       iPlanningCluster,
domain  cpitem           iPlanItem,
domain  cpcom.soty       iSupplyType,
domain  tccitg           iItemGroup,
domain  tcpono           iPositionNumber,
ref     domain  cpcom.plnc       oPlanningScenario,
ref     domain  cpcom.plvl       oPlanLevel,
ref     domain  tcemm.clus       oPlanningCluster,
ref     domain  cpitem           oPlanItem,
ref     domain  cpcom.soty       oSupplyType,
ref     domain  tccitg           oItemGroup,
ref     domain  tcpono           oPositionNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Supply Strategy in overview
mode (cprpd7120m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Specifies the table                      -index that is to
be used.
Standard supported values:
1: sort by Scenario, Level, Planning
Cluster, Group, Item, Supply Type,
Position Number.
2: sort by Scenario, Level, Planning
Cluster, Item, Supply Type, Item
Group, Position Number (default).
iQueryExtend            A specific query to be used when zooming
to this session.
iPlanningScenario       Planning Scenario
iPlanLevel              Plan Level
iPlanningCluster        Planning Cluster
iPlanItem               Plan Item
iSupplyType             Supply Type could be either Distribution
or Purchase.
iItemGroup              Item Group
iPositionNumber         Position Number
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlanningScenario       Planning Scenario
oPlanLevel              Plan Level
oPlanningCluster        Planning Cluster
oPlanItem               Plan Item
oSupplyType             Supply Type could be either Distribution
or Purchase.
oItemGroup              Item Group
oPositionNumber         Position Number
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```

## Public Interfaces for ActiveSuppliersByPlanItem

The following functions are available: ActiveSuppliersByPlanItem.StartOverview
