# SalesContracts.StartOverview

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 303-304

```baan
DLL:   tdextslsapi
This function is available from 2023.04 (KB2286306).
Syntax: long SalesContracts.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccono           iSalesContract,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tcmcs.st30m      iCustomerOrder mb,
domain  tccwoc           iSalesOffice,
domain  tcemno           iInternalSalesRepresentative,
ref     domain  tccono           oSalesContract,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Sales Contracts in overview mode
(tdsls3500m000).
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
1: sort by Sales Contract (default)
2: sort by Sold-to Business Partner, Customer Order
3: sort by Description, Contract
4: sort by Sales Office, Sold-to Business Partner, Contract
6: sort by Internal Sales Rep, Sold-to Business Partner
iQueryExtend
A specific query to be used when zooming to this session.
(Optional)
iSalesContract
Sales Contract (Optional)
iSoldToBusinessPartner
Sold-to Business Partner (Optional)
iCustomerOrder
Customer Order (Optional)
iSalesOffice
Sales Office (Optional)
iInternalSalesRepresentative
Internal Sales Representative (Optional)
Output: for iStartMode MODAL:
oSalesContract  The selected Sales Contract
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
