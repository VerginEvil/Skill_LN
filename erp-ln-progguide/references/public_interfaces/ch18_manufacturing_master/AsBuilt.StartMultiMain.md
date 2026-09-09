# AsBuilt.StartMultiMain

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for AsBuilt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 634-635

```baan
DLL:   tiextmfcapi
This function is available from 2024.01 (KB2304915).
Syntax: long AsBuilt.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  timfc.ord        iOrderType,
domain  tcpdno           iOrderNumber,
domain  tcponl           iSchedulePosition,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Multi Main session As-Built
(timfc0610m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used.
iSessionIndex           Not used
iQueryExtend            A specific query to be used when zooming
to this session. Optional.
iOrderType              Order Number can be either Production
Order or Assembly Order - Optional
iOrderNumber            Order Number - Optional
iSchedulePosition       SchedulePosition - Optional
iItem                   Item - Optional
iSerialNumber           SerialNumber - Optional
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Error Occurred.
```
