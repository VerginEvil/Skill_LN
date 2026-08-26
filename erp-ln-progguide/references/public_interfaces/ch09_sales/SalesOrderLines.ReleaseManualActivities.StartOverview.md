# SalesOrderLines.ReleaseManualActivities.StartOverview

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 359-360

```baan
DLL:   tdextslsapi
This function is available from     2025.03 (KB3557009  ).
Syntax: long SalesOrderLines.ReleaseManualActivities.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcmcs.st20m      iActivity mb,
ref     domain  tcorno           oSalesOrder,
ref     domain  tcpono           oSalesOrderLine,
ref     domain  tcpono           oSalesOrderLineSequence,
ref     domain  tcmcs.st20m      oActivity mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Release Manual Activities Sales Order
Lines (tdsls4501m150).
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
Specifies the session index that is to be used.
Supported values:
1: sort by "Order Lines by Activity" (default)
2: sort by "Execution Sequence of Activity by Order Line"
3: sort by "Activities by Order Line"
iQueryExtend
A specific query to be used when zooming to this session.
iSalesOrder
Sales Order
Mandatory if iStartMode = MODELESS and session index 2 is used.
iSalesOrderLine
Sales Order Line
iSalesOrderLineSequence
Sales Order Line Sequence
iActivity
Activity
Mandatory if iStartMode = MODELESS and session index 1 is used.
Output: for iStartMode MODAL:
oSalesOrder     The selected Sales Order
oSalesOrderLine The selected Sales Order Line
oSalesOrderLineSequence
The selected Sales Order Line Sequence
oActivity       The selected Activity
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

## Public Interfaces for SalesOrderLineComponent

The following functions are available: SalesOrderLineComponent.Block SalesOrderLineComponent.ReleaseBlocking
