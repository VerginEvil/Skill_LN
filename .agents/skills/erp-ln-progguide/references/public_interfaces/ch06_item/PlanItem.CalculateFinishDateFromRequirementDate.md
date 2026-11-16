# PlanItem.CalculateFinishDateFromRequirementDate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 214-215

```baan
DLL:   cpextrpdapi
This function is available from 2024.10 (KB3514340).
Syntax: long PlanItem.CalculateFinishDateFromRequirementDate(
domain  tcncmp           iCompany,
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
domain  tcdate           iRequirementDate,
ref     domain  tcdate           oFinishDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to calculate the finish date
for a plan item. Given a Requirement Date, planning the additional
lead time backwards yields the returned Finish Date (completion
of production).
Input:
iCompany                Company Number (Mandatory)
iScenario               Planning Scenario (Mandatory)
iPlanItem               Plan Item (Mandatory)
iRequirementDate        Requirement Date is the date of
availability for external or internal
delivery (Mandatory)
Output:
oFinishDate             Finish Date
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Calculated the Finish date successfully.
<> 0                    An error occurred.
```
