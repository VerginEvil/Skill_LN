# ProductionWarehouseOrders.StartDetail

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionWarehouseOrders
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 632-633

```baan
DLL:   tiextmfcapi
This function is available from 2023.06 (KB2286048).
Syntax: long ProductionWarehouseOrders.StartDetail(
long             iStartMode,
domain  tiinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcpono           iPosition,
domain  tcpono           iSequenceNumber,
domain  tcinh.ittp       iTransactionType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Production Warehouse Orders
(timfc0101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iOrderOrigin
Order Origin - Mandatory. The Order Origin must have one
of the following values:
tiinh.oorg.production           - JSC Production
tiinh.oorg.product.sched        - Production Schedule
iOrder
Order - Mandatory.
iPosition
Position
iSequenceNumber
Sequence Number - Mandatory.
iTransactionType
Transaction Type - Mandatory. The Transaction Type must
have one of the following values:
tcinh.ittp.receipt      - Receipt
tcinh.ittp.issue        - Issue
tcinh.ittp.transfer     - Transfer
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
