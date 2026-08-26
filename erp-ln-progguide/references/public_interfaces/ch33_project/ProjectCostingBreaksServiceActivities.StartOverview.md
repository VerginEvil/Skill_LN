# ProjectCostingBreaksServiceActivities.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectCostingBreaksServiceActivities
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1715-1716

```baan
DLL:   tpextpdmapi
This function is available from     2024.03 (KB2301398  ).
Syntax: long ProjectCostingBreaksServiceActivities.StartOverview(
long             iStartMode,
domain  tccprj           iProject,
ref     domain  tccprj           oProject,
ref     domain  tppdm.serf       oLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session
Costing Breaks                       - Service Activities(tppdm3106m000) in overview mode.
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
iProject                              - Project; Optional
Output: oProject                              - Project of selected transaction
oLine                                         - Line of selected transaction
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

## Public Interfaces for ProjectCostTransactions

The following functions are available: ProjectCostTransactions.StartOverview
