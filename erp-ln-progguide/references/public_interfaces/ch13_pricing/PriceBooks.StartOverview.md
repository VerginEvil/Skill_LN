# PriceBooks.StartOverview

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for PriceBook
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 525-526

```baan
DLL:   tdextpcgapi
This function is available from     2026.05 (KB3664998  ).
Syntax: long PriceBooks.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tdpcg.prbk       iPriceBook,
ref     domain  tdpcg.prbk       oPriceBook,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Price Books Overview (tdpcg0111m000).
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS        Parent and child are parallel sessions
that can be manipulated simultaneously.
iStartFilter            Start filter (Not used).
iSessionIndex           Session index (Not used).
iQueryExtend            A specific query to be used when zooming
to this session (Optional).
iPriceBook              Price Book (Optional).
Output: for iStartMode MODAL:
oPriceBook      The selected Price Book
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

## Public Interfaces for PriceBookLine

The following functions are available: PriceBookLines.StartDetail PriceBookLines.StartOverview
