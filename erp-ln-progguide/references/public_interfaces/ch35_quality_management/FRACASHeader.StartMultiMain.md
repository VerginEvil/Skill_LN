# FRACASHeader.StartMultiMain

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for FRACASHeader
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1769-1770

```baan
DLL:   qmextpqmapi
This function is available from     2022.08 (KB2226027  ).
Syntax: long FRACASHeader.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iFRACASNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session
"Failure Reporting Analysis and Corrective Action System Header"
(qmpqm2600m100).
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
Not Used
iSessionIndex
Not Used
iQueryExtend
Not Used
iFRACASNumber
FRACAS Number, Mandatory
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

## Public Interfaces for TestingCombination

The following functions are available: TestingCombinations.StartOverview
