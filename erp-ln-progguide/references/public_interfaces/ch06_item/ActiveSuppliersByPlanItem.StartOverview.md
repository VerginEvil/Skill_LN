# ActiveSuppliersByPlanItem.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ActiveSuppliersByPlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 237-238

```baan
DLL:   cpextrpdapi
This function is available from     2024.10 (KB3501642  ).
Syntax: long ActiveSuppliersByPlanItem.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpitem           iPlanItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Active Suppliers By Plan Item
(cprpd1500m000) in overview mode.
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
iSessionIndex           Not Used.
iQueryExtend            A specific query to be used when zooming
to this session.
iPlanItem               Plan Item.
Output:
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

## Public Interfaces for ActiveSupplySource

The following functions are available: ActiveSupplySources.StartOverview
