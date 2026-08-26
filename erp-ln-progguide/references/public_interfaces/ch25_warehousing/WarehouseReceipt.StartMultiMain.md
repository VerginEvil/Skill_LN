# WarehouseReceipt.StartMultiMain

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 975-976

```baan
DLL:   whextinhapi
This function is available from     2023.09 (KB2301526  ).
Syntax: long WarehouseReceipt.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iReceipt,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the multi main table session
Warehouse Receipts (whinh3512m000).
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
Primary Key Fields:
iReceipt                                      - iReceipt must refer to an existing
warehouse receipt.
Output: oExceptionMessage                     - The last message if any message is
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
