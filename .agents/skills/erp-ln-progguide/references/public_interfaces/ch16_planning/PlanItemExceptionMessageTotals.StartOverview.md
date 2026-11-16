# PlanItemExceptionMessageTotals.StartOverview

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlanItemExceptionMessageTotal
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 559-560

```baan
DLL:   cpextraoapi
This function is available from 2020.06 (KB2128476).
Syntax: long PlanItemExceptionMessageTotals.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcemno           iPlannerID,
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  tcdate           iReferenceDateFrom,
domain  tcdate           iReferenceDateTo,
domain  cprao.prio       iPriorityFrom,
domain  cprao.prio       iPriorityTo,
const           string           iSortBy(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Exception Messages by Planner
overview session (cprao1120m000).
Input:  iStartMode: Not used. Session will always be started modeless.
MODELESS:       Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Not Used.
iQueryExtend            Not Used.
iPlannerID              The employee number of the planner,
or empty (for unlinked messages)
iPlanningScenario       The Planning Scenario.
When empty, the Actual Scenario will
be used.
iPlanItem               Filter field. Optional. When empty:
all items are shown, when filled:
only items matching the filter string are
shown. Eg. "CL1PCS000123" will display
only cluster CL1 plan items for
project PCS000123.
iReferenceDateFrom      Filter field. Optional. Default: 0
iReferenceDateTo        Filter field. Optional. Default: 31-12-9999
iPriorityFrom           Filter field. Optional. Default: 0
iPriorityTo             Filter field. Optional. Default: 100
iSortBy                 Possible values:
"item" (= plan item),
"number" (= number of messages"),
"priority" (= highest priority),
"date" (= reference date).
Optional. When empty, the sort order
is undefined.
Output: As cprao1120m000 displays aggregated data, no information about
selected records is returned.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
