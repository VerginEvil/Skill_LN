# SalesQuoteLine.StartDetail

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuoteLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 299-300

```baan
DLL:   tdextslsapi
This function is available from 2020.10 (KB2151929).
Syntax: long SalesQuoteLine.StartDetail(
long             iStartMode,
domain  tcqono           iSalesQuote,
domain  tcpono           iSalesQuoteLine,
domain  tdsls.altn       iAlternative,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Sales Quotation Lines
(tdsls1501m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSalesQuote             Sales Quote (Mandatory)
iSalesQuoteLine         Sales Quote Line (Mandatory)
iAlternative            Alternative( must be >= 0)
Note that the given sales quote line
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
