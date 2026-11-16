# LotInventoryByWarehouseAndItem.StartMultiMain

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for LotInventoryByWarehouseAndItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1121-1122

```baan
DLL:   whextltcapi
This function is available from 2023.02 (KB2280148).
Syntax: long LotInventoryByWarehouseAndItem.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcclot           iLot,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the multi main table session Warehouse -
Item - Lots Inventory (whltc1605m000).
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
iQueryExtend
A specific query to be used when zooming to this session.
Primary Key Fields:
iWarehouse
iItem
iLot
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
