# ProjectPCS.Start360

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 899-901

```baan
DLL:   tiextpcsapi
This function is available from 2022.02 (KB2226609).
Syntax: long ProjectPCS.Start360(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccprj           iProject,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Project 360 (tipcs0320m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session. Optional.
Possible values are:
"ShowAllProjects":
All Projects are displayed.
"ShowBudgets":
Only Budgets are shown.
"ShowOpenProjects":
Only open Projects are shown.
"ShowActiveProjects":
Only active Projects are shown.
"ShowSimulatedProjects":
Only simulated Projects are shown.
"ShowFreeProjects":
Only free Projects are shown.
"ShowCanceledProjects":
Only canceled Projects are shown.
"ShowFinishedProjects":
Only finished Projects are shown.
"ShowToBeClosedProjects":
Only to be closed Projects are shown.
"ShowClosedProjects":
Only closed Projects are shown.
"ShowArchivedProjects":
Only archived Projects are shown.
"ShowOneProject":
Only iProject is shown.
iSessionIndex
The index that will be used.
Supported values:
1: sort by Project.
2: sort by Search Key/Project.
3: sort by Kind Of Project/Project.
4: sort by Calculation Group/Project.
5: sort by Sold-to BP/Project.
iQueryExtend            Not used.
iProject                Project. Only used if iStartFilter
"ShowOneProject" is used.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
