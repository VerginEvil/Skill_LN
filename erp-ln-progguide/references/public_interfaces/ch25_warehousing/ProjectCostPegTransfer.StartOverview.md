# ProjectCostPegTransfer.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectCostPegTransfer
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1104-1105

```baan
DLL:   whextinhapi
This function is available from 2023.08 (KB2296399).
Syntax: long ProjectCostPegTransfer.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iProjectCostPegTransfer,
ref     domain  tcorno           oProjectCostPegTransfer,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Project Cost Peg
Transfer (whinh1140m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
iProjectCostPegTransfer
The Project Cost Peg Transfer to be started
Mandatory if iStartMode = MODELESS
Output: for iStartMode MODAL:
oProjectCostPegTransfer
- Project Cost Peg Transfer of selected
record
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
