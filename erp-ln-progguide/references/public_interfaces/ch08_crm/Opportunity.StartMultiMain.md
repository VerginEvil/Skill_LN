# Opportunity.StartMultiMain

> Chapter: Chapter 8 Public Interfaces for CRM
>
> Group: Public Interfaces for Opportunity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 269-271

```baan
DLL:   tdextsmiapi
This function is available from     2020.06 (KB2127961  ).
Syntax: long Opportunity.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcopty           iOpportunity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Opportunity
(tdsmi1610m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iQueryExtend            A specific query to be used when zooming
to this session.
iOpportunity            Opportunity
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

## Chapter 9 Public Interfaces for Sales

## Public Interfaces for Sales

The following functions are available: Sales.CalculatePlannedDeliveryDate Sales.CalculatePlannedReceiptDate Sales.GenerateRetrobilledPriceChangeAdvices Sales.GetContractSettings Sales.GetGeneralSettings Sales.GetOrderSettings Sales.GetQuoteSettings Sales.GetScheduleSettings Sales.StartProcessProFormaInvoices
