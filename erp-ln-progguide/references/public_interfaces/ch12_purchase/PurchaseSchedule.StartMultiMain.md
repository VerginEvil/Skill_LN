# PurchaseSchedule.StartMultiMain

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseSchedule
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 439-440

```baan
DLL:   tdextpurapi
This function is available from     2025.11 (KB3632431  ).
Syntax: long PurchaseSchedule.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcorno           iPurchaseSchedule,
domain  tdstyp           iScheduleType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Purchase Schedule
(tdpur3610m000).
Input:  iStartMode              Specifies the start mode for the session
(mandatory).
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used
iQueryExtend            A specific query to be used when zooming
to this session (optional).
iPurchaseSchedule       Purchase schedule (mandatory).
iScheduleType           Schedule Type (mandatory)
Values are: Push, Pull Forecast and Pull Call                                              -off.
Output: oExceptionMessage       The last message if any message is
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
