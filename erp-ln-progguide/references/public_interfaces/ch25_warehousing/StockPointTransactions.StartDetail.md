# StockPointTransactions.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StockPointTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 992-993

```baan
DLL:   whextinrapi
This function is available from     2024.01 (KB2314707  ).
Syntax: long StockPointTransactions.StartDetail(
long             iStartMode,
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tcinvt.date      iInventoryDate,
domain  tcdate           iTransactionDate,
domain  tcpono           iSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session
Stock Point Transactions (whinr1500m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Primary Key Fields:
iWarehouse      Warehouse (mandatory)
iLocation       Location (optional)
iItem           Item (mandatory)
iLot            Lot (optional)
iSerial         Serial (optional)
iInventoryDate  Inventory Date (optional)
iTransactionDate Transaction Date (mandatory)
iSequence       Sequence (mandatory)
Output:
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
