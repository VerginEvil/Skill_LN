# PlannedOrders.StartGenerate

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 563-564

```baan
DLL:   cpextrrpapi
This function is available from 2022.07 (KB2248039).
Syntax: long PlannedOrders.StartGenerate(
long             iStartMode,
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the process session
Generate Order Planning (Item) (cprrp1220m000).
Pre:    -
Post:   -
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS -
Parent and child are parallel
sessions that can be manipulated
simultaneously.
iPlanningScenario       The Planning Scenario (Mandatory).
iPlanItem               Plan Item.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Generate Order Planning (Item) Session
started.
<> 0                    Otherwise.
```
