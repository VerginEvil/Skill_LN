# ReceiptLine.StartAwaitingDirectMaterialSupply

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1252-1253

```baan
DLL:   whextinhapi
This function is available from     2025.06 (KB3566661  ).
Syntax: long ReceiptLine.StartAwaitingDirectMaterialSupply(
long             iStartMode,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
ref     domain  whinh.shpm       oReceipt,
ref     domain  tcpono           oReceiptLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Receipt Lines Awaiting Direct
Material Supply (whinh3512m300, multi occ).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSessionIndex
Not Mandatory.
1: Receipt, Receipt Line (default)
2: Item, Warehouse, Receipt, Receipt Line
3: Warehouse, Item, Receipt, Receipt Line
iReceipt
Not Mandatory.
iReceiptLine
Not Mandatory.
iWarehouse
Not Mandatory.
iItem
Not Mandatory.
Output: for i.start.mode MODAL:
oReceipt
oReceiptLine
Return: 0 / DALHOOKERROR
```

## Public Interfaces for ReceiptLineStockPointDetail

The following functions are available: ReceiptLineStockPointDetails.StartOverview
