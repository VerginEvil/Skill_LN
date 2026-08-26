# ExceptionMessages.StartOverview

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ExceptionMessages
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 590-592

```baan
DLL:   cpextraoapi
This function is available from     2024.09 (KB3501698  ).
Syntax: long ExceptionMessages.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcemno           iPlannerID,
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
domain  tckoor           iOrderType,
domain  cporno           iOrderNumber,
domain  cpcom.date       iReferenceDate,
domain  cprao.sign       iPlanItemExceptionMessage,
domain  tcponl           iPositionNumber,
domain  tcpono           iSequenceNumber,
ref     domain  tcemno           oPlannerID,
ref     domain  cpcom.plnc       oScenario,
ref     domain  cpitem           oPlanItem,
ref     domain  tckoor           oOrderType,
ref     domain  cporno           oOrderNumber,
ref     domain  cpcom.date       oReferenceDate,
ref     domain  cprao.sign       oPlanItemExceptionMessage,
ref     domain  tcponl           oPositionNumber,
ref     domain  tcpono           oSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Exception Messages
(cprao1125m000) in overview mode.
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
1: sort by Plan Item, Order
(default).
2: sort by Plan Item, Priority
4: sort by Planner, Message
5: Scenario
iQueryExtend            A specific query to be used when zooming
to this session.
iPlannerID              Planner ID
iScenario               Scenario
iPlanItem               Plan Item
iOrderType              Order Type
iOrderNumber            Order Number
iReferenceDate          Reference Date
iPlanItemExceptionMessage Exception Message
iPositionNumber         Position Number
iSequenceNumber         Sequence Number
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlannerID              Planner ID
oScenario               Scenario
oPlanItem               Plan Item
oOrderType              Order Type
oOrderNumber            Order Number
oReferenceDate          Reference Date
oPlanItemExceptionMessage Exception Message
oPositionNumber         Position Number
oSequenceNumber         Sequence Number
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

## Public Interfaces for OrderPegging

The following functions are available: OrderPegging.StartOrderDetails OrderPegging.StartSelect
