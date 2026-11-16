# PlannedOrderDistribution.StartOverview

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedOrderDistribution
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 583-584

```baan
DLL:   cpextrrpapi
This function is available from 2024.06 (KB2329991).
Syntax: long PlannedOrderDistribution.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iPlanningScenario,
domain  tckoor           iOrderType,
domain  cprrp.orno       iPlannedOrder,
domain  tcpono           iLinePositionNumber,
domain  tcguid           iSpecification,
ref     domain  cpcom.plnc       oPlanningScenario,
ref     domain  tckoor           oOrderType,
ref     domain  cprrp.orno       oPlannedOrder,
ref     domain  tcpono           oLinePositionNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Planned Order Distribution in
overview mode (cprrp1105m000).
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
iSessionIndex           Specifies the table-index that is to
be used.
Standard supported values:
1: sort by Scenario, Order Type,
Planned Order, Position (default).
iQueryExtend            A specific query to be used when zooming
to this session.
iPlanningScenario       Planning Scenario
iOrderType              Order Type
iPlannedOrder           Planned Order
iLinePositionNumber     Line Position Number
iSpecification          Specification
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlanningScenario       Planning Scenario
oOrderType              Order Type
oPlannedOrder           Planned Order
oLinePositionNumber     Line Position Number
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
