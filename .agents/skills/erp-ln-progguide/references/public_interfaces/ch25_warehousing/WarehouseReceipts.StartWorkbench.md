# WarehouseReceipts.StartWorkbench

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 987-987

```baan
DLL:   whextinhapi
This function is available from 2020.03 (KB2111387).
Syntax: long WarehouseReceipts.StartWorkbench(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
const           string           iInboundLineFilter(),
domain  tccwar           iWarehouse,
domain  tccom.bpid       iBusinessPartner,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the workbench session Warehouse Receipts
(whinh2610m100).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
Not Used.
iInboundLineFilter
A specific query to be used when zooming to the
Inbound Lines session.
Following input variables form the filtering fields, these
fields are optional.
iWarehouse
iBusinessPartner
Output: oExceptionMessage       - The last message if any message is
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
