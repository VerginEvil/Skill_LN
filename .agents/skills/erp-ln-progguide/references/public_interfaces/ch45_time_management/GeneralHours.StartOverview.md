# GeneralHours.StartOverview

> Chapter: Chapter 45 Public Interfaces for Time Management
>
> Group: Public Interfaces for GeneralHours
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1919-1921

```baan
DLL:   bpexttmmapi
This function is available from 2023.02 (KB2274132).
Syntax: long GeneralHours.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcemno           iEmployee,
domain  tcccp.yrno       iYear,
domain  tcccp.peri       iPeriod,
domain  tcppl.cgrp       iTeam,
ref     domain  tcemno           oEmployee,
ref     domain  tcccp.yrno       oYear,
ref     domain  tcccp.peri       oPeriod,
ref     domain  bptmm.type       oTransactionType,
ref     domain  bpmdm.serd       oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session General Hours -
bptmm1111m200 (Overview).
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
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"" (Session has no start filter)
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
Note: - Session starts on Index 1.
If specific session index is to be used, below Indices
are only applicable:
Index 1
Index 4
iQueryExtend
Optional
A specific query to be used when zooming to this session.
iEmployee               - Employee          (Not Mandatory)
iYear                   - Year              (Not Mandatory)
iPeriod                 - Period            (Not Mandatory)
iTeam                   - Team              (Not Mandatory)
Output: for iStartMode MODAL:
oEmployee               - Selected Employee
oYear                   - Selected Year
oPeriod                 - Selected Period
oTransactionType        - Selected Transaction Type
oSequence               - Selected Sequence
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
