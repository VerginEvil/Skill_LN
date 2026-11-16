# ItemMasterPlan.StartPlan

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemMasterPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 545-545

```baan
DLL:   cpextrmpapi
This function is available from 2020.03 (KB2111387).
Syntax: long ItemMasterPlan.StartPlan(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  cpcom.sern       iPeriodNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Item Master Plan (cprmp2101m000)
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The index that will be used.
Supported values:
1: sort by Scenario/Plan Item/Period
2: sort by Plan Item/Scenario/Period
iQueryExtend            Not Used.
iPlanningScenario       Planning Scenario
iPlanItem               Plan Item
iPeriodNumber           Period Number
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
