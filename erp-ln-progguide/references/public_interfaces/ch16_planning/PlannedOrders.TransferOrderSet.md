# PlannedOrders.TransferOrderSet

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 565-566

```baan
DLL:   cpextrrpapi
This function is available from 2022.05 (KB2239777).
Syntax: long PlannedOrders.TransferOrderSet(
long             iStartMode,
long             iNumberOfOrders,
ref     domain  cprrp.orno       iPlannedOrder() fixed,
ref     domain  tckoor           iOrderType(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the process session Transfer Order Planning
(cppat1210m000).
The session will be started to process the planned orders given
in the input arrays.
If i.number.of.orders is 0, the session will be started without
a preselection and the Planned Orders can be selected using the
standard selection ranges.
Pre:    -
Post:   -
Input:  iStartMode
Specifies the start mode for the session.
The following start modes are allowed for this Public
Interface:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS.ALWAYS -
The parent and child are parallel
sessions that can be manipulated
simultaneously.
iNumberOfOrders         Number of Planned Orders to be
transferred.
iPlannedOrder           Array with the planned orders that will
be attempted to be transferred (Mandatory).
iOrderType              Array with the order types of the orders
in the iPlannedOrder array (Mandatory).
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Transfer Order Session started.
<> 0                    Otherwise.
```
