# CorrectiveActionPlan.SetStatus

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for CorrectiveActionPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1785-1785

```baan
DLL:   qmextcplapi
This function is available from 2022.08 (KB2226027).
Syntax: long CorrectiveActionPlan.SetStatus(
domain  tcorno           iCorrectiveActionPlan,
domain  qmcpl.caps       iCorrectiveActionPlanStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will set Corrective Action Plan status.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iCorrectiveActionPlan
- Corrective Action Plan; Mandatory
iCorrectiveActionPlanStatus
- Corrective Action Plan Status; Mandatory
qmcpl.caps.open         - Open (Reset)
qmcpl.caps.submitted    - Submitted
qmcpl.caps.approved     - Approved
qmcpl.caps.complete     - Completed
qmcpl.caps.cancelled    - Canceled
qmcpl.caps.closed       - Closed
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Corrective Action Plan Status changed to given status.
<> 0    - Corrective Action Plan Status could not be changed.
```
