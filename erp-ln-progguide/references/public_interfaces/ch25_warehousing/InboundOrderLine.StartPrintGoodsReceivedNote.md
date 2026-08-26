# InboundOrderLine.StartPrintGoodsReceivedNote

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1084-1086

```baan
DLL:   whextinhapi
This function is available from     2024.02 (KB2314556  ).
Syntax: long InboundOrderLine.StartPrintGoodsReceivedNote(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tcdate           iFromPlannedReceiptDate,
domain  whinh.oorg       iFromOrderOrigin,
domain  tcorno           iFromOrderNumber,
domain  tcpono           iFromOrderLine,
domain  whinh.shpm       iFromReceipt,
domain  tcdate           iToPlannedReceiptDate,
domain  whinh.oorg       iToOrderOrigin,
domain  tcorno           iToOrderNumber,
domain  tcpono           iToOrderLine,
domain  whinh.shpm       iToReceipt,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Print Goods Received Note
(whinh3412m100). Depending on the main table of the calling
session, Non                      -Consecutive Record Selection (NCRS) is used.
When the main table is:
Warehouse Orders (whinh200) or
Inbound Order Lines (whinh210) or
Handling Unit Process Inbound (whinh213") or
Receipt Lines (whinh312) or
Handling Units (whwmd530) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iFromPlannedReceiptDate
From Planned Receipt Date selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable)
iFromOrderOrigin
From Order Origin selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderNumber
From Order Number selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderLine
From Order Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromReceipt
From Receipt selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToPlannedReceiptDate
To Planned Receipt Date selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable)
iToOrderOrigin
To Order Origin selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderNumber
To Order Number selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderLine
To Order Line selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToReceipt
To Receipt selection field is filled with this
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

## Public Interfaces for InboundRun

The following functions are available: InboundRun.GenerateStorageList InboundRun.StartAutomaticInboundProcessing
