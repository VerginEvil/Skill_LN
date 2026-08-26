# PickingList.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PickingList
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1260-1261

```baan
DLL:   whextinhapi
This function is available from     2026.08 (KB3681970  ).
Syntax: long PickingList.StartDetail(
long             iStartMode,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdvice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Picking List
(whinh4525m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, in case of a
multi                                              -occurrence the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Following input variable form the primary key, these fields
are mandatory, if the primary key cannot be found an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iOrderOrigin
iOrderNumber
iOrderSet
iOrderLine
iOrderSequence
iAdvice                                       - The primary key fields must refer to
an existing Outbound Advice
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```
