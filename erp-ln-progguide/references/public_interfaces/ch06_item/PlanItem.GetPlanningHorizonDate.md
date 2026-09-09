# PlanItem.GetPlanningHorizonDate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 221-222

```baan
DLL:   cpextrpdapi
This function is available from 2026.11 (KB3700208).
Syntax: long PlanItem.GetPlanningHorizonDate(
domain  tcncmp           iCompany,
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
ref     domain  cpcom.date       oPlanningHorizonDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines and returns the Planning Horizon Date
for a plan item. The date is calculated using LN's
standard horizon logic (calendar resolution based on enterprise
unit/company calendar, scenario, working-day/holiday logic,
and shift to end of plan period).
The function reads the Planning Horizon (cprpd100.ptmf) setting
for the plan item and calculates the resulting calendar date.
This is functionally equivalent to how the Planning Horizon date
is determined in session Items - Planning (cprpd1100m000)
Pre:    N.A.
Post:   N.A.
Input:  iCompany                - Company. When 0, the current company
is used.
iPlanningScenario       - Planning Scenario. When empty, the
Actual scenario is used.
iPlanItem               - Plan Item. Mandatory.
Output: oPlanningHorizonDate    - Planning Horizon Date.
oExceptionMessage       - The last message, if any message is
found. If more than one message is
given these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Planning horizon date determined
successfully.
<> 0                    - Otherwise.
```
