# Lot.StartPrintLotBlocking

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Lot
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1109-1111

```baan
DLL:   whextwmdapi
This function is available from     2023.02 (KB2274420  ).
Syntax: long Lot.StartPrintLotBlocking(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tcitem           iFromItem,
domain  tcclot           iFromLot,
domain  tccdis           iFromReason,
domain  tcitem           iToItem,
domain  tcclot           iToLot,
domain  tccdis           iToReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Print Lot Blocking
(whwmd6420m000). Depending on the main table of the calling
session, Non                      -Consecutive Record Selection (NCRS) is used.
When the main table is:
Lot Blocking (whwmd620) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not used
Session is always started in MODAL mode.
iIgnoreSelectionFields
If true, (empty) From/To selection fields will not be
filled in the session.
iFromItem
From Item selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromLot
From Lot selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromReason
From Reason selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToItem
To Item selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToLot
To Lot selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToReason
To Reason selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```

## Public Interfaces for

## LotInventoryByWarehouseAndItem

The following functions are available: LotInventoryByWarehouseAndItem.StartDetail LotInventoryByWarehouseAndItem.StartMultiMain LotInventoryByWarehouseAndItem.StartOverview
