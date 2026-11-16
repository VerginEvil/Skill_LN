# MaintenanceSalesOrder.StartMultiMain

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceSalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1490-1491

```baan
DLL:   tsextmscapi
This function is available from 2026.05 (KB3663572).
Syntax: long MaintenanceSalesOrder.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcorno           iMaintenanceSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Maintenance Sales
Order (tsmsc1100m100).
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
iQueryExtend            A specific query to be used when zooming
to this session.
iMaintenanceSalesOrder  Maintenance Sales Order
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
