# SourcingStrategy.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for SourcingStrategy
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 235-235

```baan
DLL:   cpextrpdapi
This function is available from 2024.07 (KB2329980).
Syntax: long SourcingStrategy.StartDetail(
long             iStartMode,
domain  cpcom.plnc       iPlanningScenario,
domain  cpcom.plvl       iPlanLevel,
domain  tcemm.clus       iPlanningCluster,
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tcpono           iPositionNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Sourcing Strategy
(cprpd7110m000) in detail mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Primary Key Fields:
iPlanningScenario       Planning Scenario
iPlanLevel              Plan Level
iPlanningCluster        Planning Cluster
iItemGroup              Item Group
iItem                   Item
iPositionNumber         Position Number
Output: oExceptionMessage       The last message if any message is
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
