# Project.Start360

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for Project
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1693-1694

```baan
DLL:   tpextpdmapi
This function is available from 2022.01 (KB2224590).
Syntax: long Project.Start360(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcyesno          iSetFilterFields,
domain  tcemno           iProjectManager,
domain  tccwoc           iProjectManagementOffice,
domain  tccprj           iProject,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the Project 360 session (tppdm6500m100).
Input:  iStartMode
Specifies the start mode for the session (Mandatory).
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"AllProjects":  All projects are displayed
"OpenProjects": Only open projects are displayed
iSessionIndex
Specifies the session index that is to be used.
iQueryExtend
A specific query to be used when zooming to this session.
iSetFilterFields:
Used to set a filter on the projects for a Project
Manager or a Project Management Office.
Possible values are:
Yes:    A filter on the projects for a Project Manager
or a Project Management Office can be applied.
No:     No filter for Project Manager or Project
Management Office will be applied.
Empty:  If not set, the saved session defaults will be
used and applied for these filter fields.
iProjectManager:
The Project Manager to be used with iSetFilterFields.
iProjectManagementOffice:
The Project Management Office to be used with
iSetFilterFields.
i.project:
To filter on a specific Project. Make sure that the
project is inrange of the iStartFilter, iQueryExtend and
SetFilterFields selections.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
