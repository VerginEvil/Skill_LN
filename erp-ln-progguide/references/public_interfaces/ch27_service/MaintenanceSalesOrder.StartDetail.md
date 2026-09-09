# MaintenanceSalesOrder.StartDetail

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceSalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1489-1490

```baan
DLL:   tsextmscapi
This function is available from 2026.05 (KB3663572).
Syntax: long MaintenanceSalesOrder.StartDetail(
long             iStartMode,
domain  tcorno           iMaintenanceSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Maintenance Sales Orders
in Details (tsmsc1100m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iMaintenanceSalesOrder
The Maintenance Sales Order to display at the top of the
grid if present in the chosen view. (Optional)
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    An error occurred
```
