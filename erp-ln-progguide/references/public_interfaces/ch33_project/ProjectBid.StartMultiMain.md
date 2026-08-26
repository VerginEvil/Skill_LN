# ProjectBid.StartMultiMain

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectBid
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1684-1685

```baan
DLL:   tpextestapi
This function is available from     2020.09 (KB2143379  ).
Syntax: long ProjectBid.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccprj           iProject,
domain  tpest.vers       iVersion,
domain  tpest.bnum       iBidNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Project Multi-Main session "Bid"
(tpest3600m000).
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
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
iProject
Project
iVersion
Version
iBidNumber
Bid Number
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

## Public Interfaces for ProjectEstimate

The following functions are available: ProjectEstimate.GenerateStructuralElements
