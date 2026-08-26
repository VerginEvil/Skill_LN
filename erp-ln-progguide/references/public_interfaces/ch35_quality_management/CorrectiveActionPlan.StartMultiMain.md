# CorrectiveActionPlan.StartMultiMain

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for CorrectiveActionPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1766-1767

```baan
DLL:   qmextcplapi
This function is available from     2022.08 (KB2226027  ).
Syntax: long CorrectiveActionPlan.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccono           iCorrectiveActionPlan,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session "Corrective Action Plan"
(qmcpl1100m900).
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
iCorrectiveActionPlan
Corrective Action Plan, Mandatory
Output:
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
