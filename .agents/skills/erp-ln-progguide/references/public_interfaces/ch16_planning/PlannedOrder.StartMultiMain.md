# PlannedOrder.StartMultiMain

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 562-563

```baan
DLL:   cpextrrpapi
This function is available from 2024.04 (KB2327965).
Syntax: long PlannedOrder.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iScenario,
domain  tckoor           iOrderType,
domain  cprrp.orno       iPlannedOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Planned Order (cprrp1600m000).
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
iSessionIndex           Not Used.
iQueryExtend            Not Used.
iScenario               Planning Scenario. optional, if not
provided starts with previous.
iOrderType              Order Type. optional, if not
provided starts with previous.
iPlannedOrder           Planned Order. optional, if not
provided starts with previous.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
