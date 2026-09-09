# SimulatedPurchasePrices.StartOverview

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for SimulatedPurchasePrices
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 600-601

```baan
DLL:   tiextcprapi
This function is available from 2020.03 (KB2111387).
Syntax: long SimulatedPurchasePrices.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccpcc           iCostCalculationCode,
domain  tcitem           iItem,
domain  tcsite           iSite,
ref     domain  tccpcc           oCostCalculationCode,
ref     domain  tcitem           oItem,
ref     domain  tcsite           oSite,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Simulated Purchase Prices
in overview mode (ticpr1170m000).
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
iSessionIndex           The index that will be used.
Supported values:
1: sort by Cost Calculation Code/Item/Site
iQueryExtend            A specific query to be used when zooming
to this session.
iCostCalculationCode    Cost Calculation Code
iItem                   Item
iSite                   Site
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oCostCalculationCode
Cost Calculation Code
oItem           Item
oSite           Site
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
