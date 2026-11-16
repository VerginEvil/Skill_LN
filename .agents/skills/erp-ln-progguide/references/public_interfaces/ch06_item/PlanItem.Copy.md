# PlanItem.Copy

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 215-216

```baan
DLL:   cpextrpdapi
This function is available from 2024.03 (KB2303603).
Syntax: long PlanItem.Copy(
domain  cpitem           iPlanItem,
domain  cpitem           iTargetPlanItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Copy a Plan Item to the Target Plan Item. The Target Item must
exist.
The Target Plan Item must not exist.
Pre:    Retry point must be set.
Post:   Abort or commit the transaction.
Input:  iPlanItem               The plan item to copy (mandatory).
iTargetPlanItem         The target plan item. (mandatory).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The Plan Item was succesfully copied.
<> 0                    Errors occurred.
```
