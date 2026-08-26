# OrderInventoryTransaction.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OrderInventoryTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 917-919

```baan
DLL:   whextinrapi
This function is available from     2023.02 (KB2274419  ).
Syntax: long OrderInventoryTransaction.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcncmp           iOrderCompany,
domain  tckoor           iTypeOfOrder,
domain  tcorno           iOrder,
domain  tcpono           iOrderLine,
domain  tcdate           iTransactionDate,
domain  tcmcs.long       iSequence,
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
ref     domain  tcncmp           oOrderCompany,
ref     domain  tckoor           oTypeOfOrder,
ref     domain  tcorno           oOrder,
ref     domain  tcpono           oOrderLine,
ref     domain  tcdate           oTransactionDate,
ref     domain  tcmcs.long       oSequence,
ref     domain  tcitem           oItem,
ref     domain  tccwar           oWarehouse,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Order - Inventory Transactions
(whinr1511m000).
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
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
iOrderCompany
Mandatory when iStartMode is MODELESS
iTypeOfOrder
Mandatory when iStartMode is MODELESS
iOrder
Mandatory when iStartMode is MODELESS
iOrderLine
Optional.
iTransactionDate
Optional.
iSequence
Optional.
iItem
Optional.
iWarehouse
Optional.
Output: for iStartMode MODAL:
oOrderCompany                                 - order company of selected transaction
oTypeOfOrder                                  - type of orderd of selected transaction
oOrder                                        - order of selected transaction
oOrderLine                                    - order line of selected transaction
oTransactionDate                               - transaction date of selected
transaction
oSequence                                     - sequence of selected transaction
oItem                                         - item of selected transaction
oWarehouse                                    - warehouse of selected transaction
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for ItemIssueByPeriod

The following functions are available: ItemIssueByPeriod.StartDetail ItemIssueByPeriod.StartOverview
