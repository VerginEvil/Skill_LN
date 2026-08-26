# ProjectActivityBudgetOverview.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectActivityBudgetOverview
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1741-1743

```baan
DLL:   tpextptcapi
This function is available from     2025.12 (KB3625106  ).
Syntax: long ProjectActivityBudgetOverview.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccprj           iProject,
domain  tppss.cpla       iPlan,
domain  tppdm.cact       iActivity,
ref     domain  tccprj           oProject,
ref     domain  tppdm.cact       oActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Activity Budget Overview(tpptc2100m000)
in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, in case of a
multi                                              -occurrence the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the session index that is to be used. Please be
aware that iStartFilter will overrule the index passed in
this argument. So when not using start filter the session
index will match the value of this variable.
Allowed values:
1: sort by Project,Plan,Activity
2: sort by Project
iQueryExtend
A specific query to be used when zooming to this session.
iProject                              - Project. Mandatory
iPlan                                 - Plan linked to project. Optional
iActivity                             - Activity. Optional
Output: for iStartMode MODAL :
oProject                                      - Project
oActivity                                     - Activity
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

## Public Interfaces for ProjectOrderLineBalance

The following functions are available: ProjectOrderLineBalance.StartOverview
