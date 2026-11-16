# SalesQuote.StartMultiMain

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 295-295

```baan
DLL:   tdextslsapi
This function is available from 2020.06 (KB2127961).
Syntax: long SalesQuote.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcqono           iSalesQuote,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Sales Quotation
(tdsls1600m000).
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
iSalesQuote             Sales Quote
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
