# JobShopTasks.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopTask
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 811-812

```baan
DLL:   tiextrouapi
This function is available from     2023.04 (KB2274111  ).
Syntax: long JobShopTasks.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tctano           iTask,
domain  tcseak           iSearchKey mb,
ref     domain  tctano           oTask,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Tasks(Reference Operations) in
overview mode (tirou0103m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           1                       - The session will start with
the first session index: Task
2                                               - The session will start with
the second session index:
Search Key, Task.
iQueryExtend            A specific query to be used when zooming
to this session.
Primary Key fields:
iTask                 Task
iSearchKey            Search Key
(Mandatory if iSessionIndex = 2)
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oTask                   Task
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```

## Public Interfaces for UtilizationByWeek

The following functions are available: UtilizationByWeek.StartOverview
