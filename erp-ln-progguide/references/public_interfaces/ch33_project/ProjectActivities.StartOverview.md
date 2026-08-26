# ProjectActivities.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1704-1705

```baan
DLL:   tpextpssapi
This function is available from     2024.10 (KB3532922  ).
Syntax: long ProjectActivities.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccprj           iProject,
domain  tppss.cpla       iPlan,
domain  tppdm.cact       iActivity,
domain  tppdm.seak       iSearchKey mb,
domain  tppdm.cact       iParentActivity,
domain  tppdm.tact       iActivityType,
domain  tppdm.sern       iLevel,
domain  tppdm.long       iActivityPosition,
ref     domain  tppdm.cact       oActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Activities (tppss2100m000) in
overview mode.
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
1: sort by Project, Plan, Activity
View fields                                          - Project, Plan
2: sort by Project, Plan, Search Key
View fields                                          - Project, Plan
3: sort by Project, Plan, Parent Activity
View fields                                          - Project, Plan
4: sort by Project, Plan, Activity Type
View fields                                          - Project, Plan, Activity Type
5: sort by Project, Plan, Level
View fields                                          - Project, Plan
6: sort by Project, Plan, Activity Position
View fields                                          - Project, Plan
iQueryExtend
A specific query to be used when zooming to this session.
iProject                              - Project. Optional
iPlan                                 - Plan linked to project. Optional
iActivity                             - Activity. Optional
iSearchKey                            - Search Key. Optional
iParentActivity                       - Parent Activity. Optional
iActivityType                         - Activity type. Optional
iLevel                                - Level Number. Optional
iActivityPosition                      - Activity Position. Optional
Output: for iStartMode MODAL :
oActivity                                     - Activity of the selected record.
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
