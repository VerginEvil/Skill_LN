# PlanItem.GetHorizonDate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 218-219

```baan
DLL:   cpextrpdapi
This function is available from 2026.07 (KB3643775).
Syntax: long PlanItem.GetHorizonDate(
domain  tcncmp           iCompany,
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
ref     domain  cpcom.date       oHorizonDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface determines the order horizon date for a
specific company and plan item.
Pre:    N.A.
Post:   N.A.
Input:  iCompany                - Company.
iScenario               - Scenario. Mandatory.
iPlanItem               - Plan Item. Mandatory.
Output: oHorizonDate            - Horizon Date.
oExceptionMessage       - The last message, if any message is
found. If more than one message is
given these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Horizon date of a plan item determined
successfully.
<> 0                    - Otherwise.
```
