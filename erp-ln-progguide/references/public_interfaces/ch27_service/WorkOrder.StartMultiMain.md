# WorkOrder.StartMultiMain

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1498-1499

```baan
DLL:   tsextwcsapi
This function is available from     2022.01 (KB2219389  ).
Syntax: long WorkOrder.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcorno           iWorkOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Work Order
(tswcs2100m100).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -
The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -
Parent and child are parallel sessions that
can be manipulated simultaneously.
MODAL+START.WITH.ADD.SET                               -
Session is started in Add                                      -mode, so a new
work order can be entered directly.
The parent session is blocked until the
child session exits.
MODELESS+START.WITH.ADD.SET                               -
Session is started in Add                                      -mode, so a new
work order can be entered directly.
Parent and child are parallel sessions that
can be manipulated simultaneously.
iStartFilter
Not Used.
iQueryExtend
A specific query to be used when zooming
to this session.
This argument is ignored when started in Add                              -mode.
iWorkOrder
Work Order
This argument is ignored when started in Add                              -mode.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
