# ItemPlanning.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 212-213

```baan
DLL:   cpextrpdapi
This function is available from 2023.10 (KB2303593).
Syntax: long ItemPlanning.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpitem           iPlanItem,
domain  cpcom.plvl       iPlanLevel,
domain  tccprj           iProject,
domain  tcemm.clus       iCluster,
domain  tcitem           iItem,
ref     domain  cpitem           oPlanItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Items Planning (cprpd1100m000)
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
iSessionIndex           Specifies the table-index that is to be
used. Optional.
Standard supported values:
1: sort by Plan Item (default)
2: sort by Plan Level, Plan Item
7: sort by Project, Plan Level, Plan Item
8: sort by Planning Cluster, Item
9: sort by Item, Planning Cluster
iQueryExtend            A specific query to be used when zooming
to this session.(Optional)
iPlanItem               Plan Item - Optional, used when Session
Index is 1.
iPlanLevel              Plan Level - Optional, used when Session
Index is 2.
iProject                Project - Optional, used when Session
Index is 7.
iCluster                Cluster - Optional, used when Session
Index is 8.
iItem                   Item - Optional, used when Session
Index is 9.
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlanItem               Plan Item
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
