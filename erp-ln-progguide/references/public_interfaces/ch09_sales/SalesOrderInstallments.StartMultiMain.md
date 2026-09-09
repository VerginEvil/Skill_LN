# SalesOrderInstallments.StartMultiMain

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderInstallment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 372-373

```baan
DLL:   tdextslsapi
This function is available from 2025.12 (KB3634823).
Syntax: long SalesOrderInstallments.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcorno           iSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Sales Order - Installments
(tdsls4600m100).
Input:  iStartMode              Specifies the start mode for the session
(mandatory).
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used
iQueryExtend            A specific query to be used when zooming
to this session (optional).
iSalesOrder             Sales order (mandatory).
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
