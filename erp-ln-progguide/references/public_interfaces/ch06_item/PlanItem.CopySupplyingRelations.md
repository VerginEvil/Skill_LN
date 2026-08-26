# PlanItem.CopySupplyingRelations

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 216-217

```baan
DLL:   cpextrpdapi
This function is available from     2024.03 (KB2303603  ).
Syntax: long PlanItem.CopySupplyingRelations(
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  cpitem           iTargetPlanItem,
domain  tcdate           iReferenceDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Copy the Plan Item's Supplying Relations for the Planning
Scenario to the Target Plan Item.
The Target Plan Item must exist.
Pre:    Retry point must be set.
Post:   Abort or commit the transaction.
Input:  iPlanItem               The plan item to copy from (mandatory).
iTargetPlanItem         The target plan item to copy to
(mandatory).
iReferenceDate          Copy supplying relations effective on
the given reference date and those that
will be effective later. (mandatory).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The Plan Item's Supplying Relations were
succesfully copied.
<> 0                    Errors occurred.
```
