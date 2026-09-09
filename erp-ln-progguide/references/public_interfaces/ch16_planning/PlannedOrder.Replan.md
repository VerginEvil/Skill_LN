# PlannedOrder.Replan

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 562-562

```baan
DLL:   cpextrrpapi
This function is available from 2024.05 (KB2313534).
Syntax: long PlannedOrder.Replan(
domain  cpcom.plnc       iScenario,
domain  tckoor           iOrderType,
domain  cprrp.orno       iPlannedOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function is used to replan planned order.
Pre     : Retry point must be set.
Post    : Commit or abort the transaction.
Input   : iScenario             Planning Scenario (Mandatory).
iOrderType            Order Type (Mandatory).
iPlannedOrder         Planned Order (Mandatory).
Output  : oExceptionMessage     The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID          An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return  : 0                     Planned Order is Replanned successfully.
<> 0                  Otherwise.
```
