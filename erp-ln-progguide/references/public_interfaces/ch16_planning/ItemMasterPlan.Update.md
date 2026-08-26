# ItemMasterPlan.Update

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemMasterPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 542-543

```baan
DLL:   cpextrmpapi
This function is available from     2021.06 (KB2171483  ).
Syntax: long ItemMasterPlan.Update(
domain  tcncmp           iCompany,
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  tcmcs.chan       iChannel,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Update the item master plan data for the given Planning Scenario
and Plan Item.
Pre:    Retry point must be set.
Post:   Abort or commit the transaction.
Input:  iCompany                Company (mandatory).
iPlanningScenario       Scenario (mandatory).
iPlanItem               Plan Item (mandatory).
iChannel                Channel (optional).
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Function has completed.
<> 0                    A fatal problem occurred.
```

## Public Interfaces for ItemOrderPlan

The following functions are available: ItemOrderPlan.Generate ItemOrderPlan.Get ItemOrderPlan.GetV2 ItemOrderPlan.StartPlan ItemOrderPlan.StartPlanForProject ItemOrderPlan.StartPlanForProjectPeg ItemOrderPlan.StartSessionForOrder
