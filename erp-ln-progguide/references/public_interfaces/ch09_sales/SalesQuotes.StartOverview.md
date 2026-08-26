# SalesQuotes.StartOverview

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 294-295

```baan
DLL:   tdextslsapi
This function is available from     2023.08 (KB2301528  ).
Syntax: long SalesQuotes.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcqono           iSalesQuote,
domain  tcemno           iInternalSalesRepresentative,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tcdate           iExpiryDate,
domain  tccwoc           iSalesOffice,
ref     domain  tcqono           oSalesQuote,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Sales Quotations Overview
(tdsls1500m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used
iSessionIndex
Specifies the table                              -index that is to be used.
Supported values:
1: sort by Sales Quotation (default)
2: sort by Internal Sales Representative, Sold                              -to Business Partner
3: sort by Sold                              -to Business Partner
4: sort by Expiry Date, Sold                              -to Business Partner
5: sort by Sales Office, Sold                              -to Business Partner
iQueryExtend
A specific query to be used when zooming to this session.
iSalesQuote
Sales Quotation (Optional)
iInternalSalesRepresentative
Internal Sales Representative (Optional)
iSoldToBusinessPartner
Sold                              -to Business Partner
Mandatory if iStartMode = MODELESS and session                              -index 3
or 5 is used.
iExpiryDate
Expiry Date (Optional)
iSalesOffice
Sales Office
Mandatory if iStartMode = MODELESS and session                              -index 5
is used.
Output: for iStartMode MODAL:
oSalesQuote     The selected Sales Quotation
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

## Public Interfaces for SalesQuoteLine

The following functions are available: SalesQuoteLine.DetermineAmounts SalesQuoteLine.RecalculatePriceAndDiscounts SalesQuoteLine.StartDetail
