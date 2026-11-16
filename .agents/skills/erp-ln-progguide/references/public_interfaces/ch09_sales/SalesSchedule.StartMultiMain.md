# SalesSchedule.StartMultiMain

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesSchedule
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 308-309

```baan
DLL:   tdextslsapi
This function is available from 2024.02 (KB2318770).
Syntax: long SalesSchedule.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iSalesSchedule,
domain  tdsls.reltype    iSalesScheduleType,
domain  tcpono           iSalesScheduleRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Sales Schedule
(tdsls3611m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Not Used.
iQueryExtend            A specific query to be used when zooming
to this session; Optional
iSalesSchedule          Sales Schedule; Optional
iSalesScheduleType      Sales Schedule Type; Optional
iSalesScheduleRevision  Sales Schedule Revision; Optional
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
