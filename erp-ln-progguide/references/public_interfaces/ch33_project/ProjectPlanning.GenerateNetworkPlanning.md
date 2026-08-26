# ProjectPlanning.GenerateNetworkPlanning

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1703-1704

```baan
DLL:   tpextpssapi
This function is available from     2024.02 (KB2304907  ).
Syntax: long ProjectPlanning.GenerateNetworkPlanning(
domain  tccprj           iProject,
domain  tcyesno          iUpdateProjectPlanningDates,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to generate network planning
for a project and calculate the critical path for work and
planning packages of the project. It uses the planning method
as specified in the project and also the actual dates and
constraints on the activities. It calculates early start and
finish dates and late start and finish dates. It can establish
which activities have float. This function offers
similar functionality as
session (tppss2240m000                       - Generate Network Planning).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iProject                              - Project. Mandatory
iUpdateProjectPlanningDates                           -
Update Project Planning Dates (Yes/No).
Mandatory.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Successful
<> 0                                          - An error occurred
```

## Public Interfaces for ProjectActivity

The following functions are available: ProjectActivities.StartOverview ProjectActivity.SetInsertMode
