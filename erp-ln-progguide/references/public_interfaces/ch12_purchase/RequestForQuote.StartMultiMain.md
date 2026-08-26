# RequestForQuote.StartMultiMain

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for RequestForQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 411-412

```baan
DLL:   tdextpurapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long RequestForQuote.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcqono           iRequestForQuote,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Request for
Quotation (tdpur1600m000).
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS        Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iQueryExtend            A specific query to be used when zooming
to this session (Optional).
iRequestForQuote        Request for Quote (Mandatory).
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

## Public Interfaces for RequestForQuoteLine

The following functions are available: RequestForQuoteLines.StartOverview
