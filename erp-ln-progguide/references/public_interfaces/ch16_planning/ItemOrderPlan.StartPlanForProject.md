# ItemOrderPlan.StartPlanForProject

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 553-554

```baan
DLL:   cpextrrpapi
This function is available from 2020.06 (KB2127795).
Syntax: long ItemOrderPlan.StartPlanForProject(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  tccprj           iProject,
domain  cprrp.perl       iPeriodLength,
domain  cpcom.date       iStartDate,
domain  tcyesno          iSkipEmptyDays,
domain  tcyesno          iShowDistribution,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Item Order Plan (cprrp0520m000),
but only if Planning and if Project Pegging is implemented.
The Item Order Plan is started in the Item - Project View.
Input:  iStartMode              Not used. Session is always
started MODELESS (Parent and child are
parallel sessions that can be manipulated
simultaneously).
iStartFilter            Not Used.
iSessionIndex           Not Used.
iQueryExtend            Not Used
iPlanningScenario       When empty, the Actual Scenario will
be used.
iPlanItem               Plan Item, Mandatory
iProject                Project (used in Project Pegging)
Mandatory
iPeriodLength           When empty, then Detail is used
iStartDate              When zero, then current date is used
iSkipEmptyDays          When empty, then Yes is used
iShowDistribution       When empty, then Yes is used
Output: No information of selected records is returned.
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
