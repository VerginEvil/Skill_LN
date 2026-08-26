# Task.StartMultiMain

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Task
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 143-144

```baan
DLL:   tcextcomapi
This function is available from     2025.09 (KB3607361  ).
Syntax: long Task.StartMultiMain(
long             iStartMode,
long             iSessionIndex,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tccom.acty       iTask,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session 'Task' (tccom6600m300).
Input:
iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                                         - The parent session is blocked until
the child session exits. The session
will be started as a zoom session.
MODELESS                                      - Parent and child are parallel sessions
that can be manipulated simultaneously.
iSessionIndex                                 - The index that will be used.
Supported value:
1: sort by Activity.
iStartFilter                                  - Not Used.
iQueryExtend                                  - A specific query to be used when
zooming to this session.
iTask                                         - Task; this is an Activity of type Task.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started.
<> 0                                          - Error.
```

## Public Interfaces for Activities

The following functions are available: Activities.StartOverview
