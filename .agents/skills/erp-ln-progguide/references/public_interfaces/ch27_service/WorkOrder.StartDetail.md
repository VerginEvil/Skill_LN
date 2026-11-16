# WorkOrder.StartDetail

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1512-1512

```baan
DLL:   tsextwcsapi
This function is available from 2025.01 (KB3543185).
Syntax: long WorkOrder.StartDetail(
long             iStartMode,
domain  tcorno           iWorkOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Work Orders
(tswcs2100m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iWorkOrder
Work Order (Mandatory)
Note that the given work order must exist.
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                       Session started
<> 0                    An error occurred
```
