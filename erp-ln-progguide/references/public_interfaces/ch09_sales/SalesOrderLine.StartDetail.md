# SalesOrderLine.StartDetail

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 358-359

```baan
DLL:   tdextslsapi
This function is available from     2020.10 (KB2151929  ).
Syntax: long SalesOrderLine.StartDetail(
long             iStartMode,
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Sales Order Lines
(tdsls4101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSalesOrder             Sales Order (Mandatory)
iSalesOrderLine         Sales Order Line (Mandatory)
iSalesOrderLineSequence Sales Order Line Sequence number
( must be >= 0)
Note that the given sales order line
must exist.
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
