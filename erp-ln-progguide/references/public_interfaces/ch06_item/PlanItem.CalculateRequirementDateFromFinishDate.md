# PlanItem.CalculateRequirementDateFromFinishDate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 214-214

```baan
DLL:   cpextrpdapi
This function is available from     2024.10 (KB3514340  ).
Syntax: long PlanItem.CalculateRequirementDateFromFinishDate(
domain  tcncmp           iCompany,
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
domain  tcdate           iFinishDate,
ref     domain  tcdate           oRequirementDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to calculate the requirement
date for a plan item. Given a Finish Date (completion of production),
planning the additional lead time forward yields the returned
Requirement Date
Input:
iCompany                Company Number (Mandatory)
iScenario               Planning Scenario (Mandatory)
iPlanItem               Plan Item (Mandatory)
iFinishDate             Finish Date is the completion date in
production (Mandatory)
Output:
oRequirementDate        Requirement Date.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Calculated the Requirement date successfully.
<> 0                    An error occurred.
```
