# MaterialToIssueForProductionOrders.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for MaterialToIssueForProductionOrders
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 822-823

```baan
DLL:   tiextsfcapi
This function is available from 2024.10 (KB3526640).
Syntax: long MaterialToIssueForProductionOrders.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcpdno           iProductionOrder,
domain  tcpono           iPosition,
domain  tcopno           iOperation,
ref     domain  tcpdno           oProductionOrder,
ref     domain  tcpono           oPosition,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Material to Issue for
Production Orders (ticst0101m100) in overview mode.
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
iSessionIndex           Specifies the table-index that is to be
used.
Standard supported values:
1: sort by Production Order,
Position (default).
2: sort by Production Order, Operation,
Position.
iQueryExtend            A specific query to be used when zooming
to this session.
iProductionOrder        Production Order
iPosition               Position
iOperation              Operation
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oProductionOrder        Production Order
oPosition               Position
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
