# CorrectiveActionPlanTask.SetStatus

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for CorrectiveActionPlanTask
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1787-1788

```baan
DLL:   qmextcplapi
This function is available from 2022.08 (KB2226027).
Syntax: long CorrectiveActionPlanTask.SetStatus(
domain  tcorno           iCorrectiveActionPlan,
domain  tcpono           iCorrectiveActionPlanTask,
domain  qmcpl.tsks       iCorrectiveActionPlanTaskStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will set Corrective Action Plan Task status.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iCorrectiveActionPlan
- Corrective Action Plan; Mandatory
iCorrectiveActionPlanTask
- Corrective Action Plan Task; Mandatory
iCorrectiveActionPlanTaskStatus
- Corrective Action Plan Task Status ; Mandatory
qmcpl.tsks.inprogress   - In Progress
qmcpl.tsks.completed    - Completed
qmcpl.tsks.closed       - Closed
qmcpl.tsks.cancelled    - Canceled
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Corrective Action Plan Task Status changed to given status.
<> 0    - Corrective Action Plan Task Status could not be changed.
```
