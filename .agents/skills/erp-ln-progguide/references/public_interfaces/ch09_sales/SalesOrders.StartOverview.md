# SalesOrders.StartOverview

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 335-336

```baan
DLL:   tdextslsapi
This function is available from 2022.12 (KB2268796).
Syntax: long SalesOrders.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iSalesOrder,
domain  tccom.bpid       iSoldToBp,
domain  tcemno           iInternalSalesRepresentative,
domain  tccwoc           iSalesOffice,
ref     domain  tcorno           oSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Sales Orders Overview
(tdsls4100m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used
iSessionIndex
Specifies the table-index that is to be used. Optional.
Supported values:
1: sort by Sales Order (default)
2: sort by Sold-to Business Partner
3: sort by Internal Sales Rep
4: sort by Customer Order
5: sort by Sales Office, Sold-to Business Partner
6: sort by Shipment
iQueryExtend
A specific query to be used when zooming to this session.
iSalesOrder
Sales Order (Optional)
iSoldToBp
Sold-to Business Partner
Mandatory if iStartMode = MODELESS and session-index 2
or 5 is used.
iInternalSalesRepresentative
Internal Sales Representative (Optional)
iSalesOffice
Sales Office
Mandatory if iStartMode = MODELESS and session-index 5
is used.
Output: for iStartMode MODAL:
oSalesOrder     The selected Sales Order
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
