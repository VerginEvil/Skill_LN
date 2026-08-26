# CorrectiveActionPlan.StartOverview

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for CorrectiveActionPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1767-1768

```baan
DLL:   qmextcplapi
This function is available from     2025.02 (KB3541502  ).
Syntax: long CorrectiveActionPlan.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
ref     domain  tccono           oCorrectiveActionPlan,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Overview session "Corrective Action
Plan"(qmcpl1100m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
Not Used
Output: For i.start.mode MODAL:
oCorrectiveActionPlan                                 - Corrective Action Plan
selected byuser.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - An error occurred
```

## Public Interfaces for CorrectiveActionPlanTask

The following functions are available: CorrectiveActionPlanTask.SetStatus
