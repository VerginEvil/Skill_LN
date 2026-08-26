# ProjectPhysicalProgress.CopyToActivityOrCostObject

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectPhysicalProgress
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1741-1741

```baan
DLL:   tpextppcapi
This function is available from     2025.01 (KB3509112  ).
Syntax: long ProjectPhysicalProgress.CopyToActivityOrCostObject(
domain  tccprj           iProject,
domain  tpdate           iDateFrom,
domain  tpdate           iDateTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function offers similar functionality as session
Copy Activity Physical Progress to Activity/Cost Object (tpppc1245m000).
Be aware that transaction management is handled within this function.
Pre:    None.
Post:   None.
Input:  iProject                      - The Project to be copied, Mandatory
iDateFrom                             - The Date range to be copied, Optional
iDateTo                               - The Date range to be copied, Optional
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Activity Progress was copied.
<> 0                                          - Otherwise.
```

## Public Interfaces for ProjectActivityBudgetOverview

The following functions are available: ProjectActivityBudgetOverview.StartOverview
