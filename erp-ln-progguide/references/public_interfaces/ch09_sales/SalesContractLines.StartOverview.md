# SalesContractLines.StartOverview

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesContractLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 303-305

```baan
DLL:   tdextslsapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long SalesContractLines.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccono           iSalesContract,
domain  tcpono           iSalesContractLine,
domain  tccwoc           iSalesOffice,
domain  tccprg           iSalesPriceGroup,
domain  tcitem           iItem,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tcaitm           iCustomerItem mb,
ref     domain  tccono           oSalesContract,
ref     domain  tcpono           oSalesContractLine,
ref     domain  tccwoc           oSalesOffice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Sales Contract Lines in overview
mode (tdsls3501m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used
iSessionIndex
Specifies the table                              -index that is to be used. Optional.
Supported values:
1: sort by Contract, Contract Line, Sales Office (default)
2: sort by Price Group, Item, Contract, Contract Line,
Sales Office
4: sort by Sold                              -to BP, Ship-to BP, Price Group, Item,
Contract, Contract Line, Sales Office
5: sort by Sold                              -to BP, Ship-to BP, Customer Item
iQueryExtend
A specific query to be used when zooming to this session.
(Optional)
iSalesContract
Sales Contract
Mandatory if iStartMode is MODELESS and session                              -index is 1
iSalesContractLine
Sales Contract Line (Optional)
iSalesOffice
Sales Office (Optional)
iSalesPriceGroup
Sales Price Group (Optional)
iItem   Item
Mandatory if iStartMode is MODELESS and session                              -index is 2
iSoldToBusinessPartner
Sold                              -to Business Partner (Optional)
iShipToBusinessPartner
Ship                              -to Business Partner (Optional)
iCustomerItem
Customer Item (Optional)
Output: for iStartMode MODAL:
oSalesContract  The selected Sales Contract
oSalesContractLine
The selected Sales Contract Line
oSalesOffice    The selected Sales Office
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

## Public Interfaces for SalesSchedule

The following functions are available: SalesSchedule.GetForecastQuantity SalesSchedule.StartMultiMain
