# Series.StartOverview

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Series
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 142-142

```baan
DLL:   tcextmcsapi
This function is available from 2025.08 (KB3606156).
Syntax: long Series.StartOverview(
long             iStartMode,
long             iSessionIndex,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcnrgr           iNumberGroup,
ref     domain  tcseri           oSeries,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session 'First Free Numbers' (tcmcs0150m000).
Input:
iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL           - The parent session is blocked until
the child session exits. The session
will be started as a zoom session.
MODELESS        - Parent and child are parallel sessions
that can be manipulated simultaneously.
iSessionIndex           - The index that will be used.
Supported value:
1: sort by Number Group, Series.
iStartFilter            - Not Used.
iQueryExtend            - A specific query to be used when
zooming to this session.
iNumberGroup            - Number Group.
Output:
oSeries                 - Selected Series.
(For iStartMode = MODAL)
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started.
<> 0                    - Error.
```
