# SalesOrder.StartMultiMain

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 332-333

```baan
DLL:   tdextslsapi
This function is available from 2020.04 (KB2114020).
Syntax: long SalesOrder.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcorno           iSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Sales Order
(tdsls4100m900).
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
iSalesOrder             Sales Order
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
