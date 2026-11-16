# StockPointInventory.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StockPointInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 999-1000

```baan
DLL:   whextinrapi
This function is available from 2023.09 (KB2297960).
Syntax: long StockPointInventory.StartDetail(
long             iStartMode,
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tctrns.date      iInventoryDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Stock Point Inventory
(whinr1540m000).
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
Following input variable form the primary key, these fields
are mandatory, if the primary key cannot be found an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iWarehouse
iLocation
iItem
iLot
iInventoryDate
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
