# Item.GetPlanningTimeFenceDate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 173-174

```baan
DLL:   cpextrpdapi
This function is available from     2020.01 (KB2085127  ).
Syntax: long Item.GetPlanningTimeFenceDate(
domain  tcncmp           iLogisticCompany,
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
ref     domain  tcdate           oTimeFenceDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the time fence date for a
specific company and plan item.
Pre:    None
Post:   None
Input:  iLogisticCompany        Logistic Company (Mandatory)
iScenario               Scenario (Mandatory)
iPlanItem               Plan Item (Mandatory)
Output: oTimeFenceDate          Time Fence Date
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Function is executed successfully
<> 0                    An error occurred
```
