# StockPointTransactions.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StockPointTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1003-1004

```baan
DLL:   whextinrapi
This function is available from 2024.01 (KB2314707).
Syntax: long StockPointTransactions.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tcinvt.date      iInventoryDate,
domain  tcdate           iTransactionDate,
domain  tcpono           iSequence,
ref     domain  tccwar           oWarehouse,
ref     domain  whloca           oLocation,
ref     domain  tcitem           oItem,
ref     domain  tcclot           oLot,
ref     domain  tcibd.sern       oSerial,
ref     domain  tcinvt.date      oInventoryDate,
ref     domain  tcdate           oTransactionDate,
ref     domain  tcpono           oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session
Stock Point Transactions (whinr1500m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Session Index.
iQueryExtend
A specific query to be used when zooming to this session.
Primary Key Fields:
iWarehouse      Warehouse (mandatory)
iLocation       Location (optional)
iItem           Item (mandatory)
iLot            Lot (optional)
iSerial         Serial (optional)
iInventoryDate  Inventory Date (optional)
iTransactionDate Transaction Date (optional)
iSequence       Sequence (optional)
Output: for iStartMode MODAL:
oWarehouse
oLocation
oItem
oLot
oSerial
oInventoryDate
oTransactionDate
oSequence
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
