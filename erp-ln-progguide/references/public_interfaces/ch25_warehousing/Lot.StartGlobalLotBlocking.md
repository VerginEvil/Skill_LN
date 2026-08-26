# Lot.StartGlobalLotBlocking

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Lot
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1107-1108

```baan
DLL:   whextwmdapi
This function is available from     2023.02 (KB2280149  ).
Syntax: long Lot.StartGlobalLotBlocking(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tcclot           iFromLot,
domain  tcitem           iFromItem,
domain  tcclot           iToLot,
domain  tcitem           iToItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Global Lot Blocking
(whwmd6220m000). Depending on the main table of the calling
session, Non                      -Consecutive Record Selection (NCRS) is used.
When the main table is:
Lots            (whltc100) or
Lot Blocking    (whwmd620) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not used
Session is always started in MODAL mode.
iIgnoreSelectionFields
If true, (empty) From/To selection fields will not be
filled in the session.
iFromLot
From Lot selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromItem
From Item selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToLot
To Lot selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToItem
To Item selection field is filled with this
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
