# SourcingStrategy.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for SourcingStrategy
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 234-235

```baan
DLL:   cpextrpdapi
This function is available from     2024.07 (KB2329980  ).
Syntax: long SourcingStrategy.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iPlanningScenario,
domain  cpcom.plvl       iPlanLevel,
domain  tcemm.clus       iPlanningCluster,
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tcpono           iPositionNumber,
domain  tcdate           iEffectivityDate,
ref     domain  cpcom.plnc       oPlanningScenario,
ref     domain  cpcom.plvl       oPlanLevel,
ref     domain  tcemm.clus       oPlanningCluster,
ref     domain  tccitg           oItemGroup,
ref     domain  tcitem           oItem,
ref     domain  tcpono           oPositionNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Sourcing Strategy
(cprpd7110m000) in overview mode.
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
iSessionIndex           Specifies the table                      -index that is to be
used.
Standard supported values:
1: sort by Scenario, Level, Planning
Cluster, Item Group, Item, Position
Number (default).
5: sort by Scenario, Level, Planning
Cluster, Item Group, Item, Date.
iQueryExtend            A specific query to be used when zooming
to this session.
iPlanningScenario       Planning Scenario
iPlanLevel              Plan Level
iPlanningCluster        Planning Cluster
iItemGroup              Item Group
iItem                   Item
iPositionNumber         Position Number
iEffectivityDate        Effectivity Date
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlanningScenario       Planning Scenario
oPlanLevel              Plan Level
oPlanningCluster        Planning Cluster
oItemGroup              Item Group
oItem                   Item
oPositionNumber         Position Number
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```

## Public Interfaces for SupplyStrategy

The following functions are available: SupplyStrategy.StartOverview
