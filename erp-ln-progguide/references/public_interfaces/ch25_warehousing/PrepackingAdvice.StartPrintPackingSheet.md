# PrepackingAdvice.StartPrintPackingSheet

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PrepackingAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1312-1314

```baan
DLL:   whextwmdapi
This function is available from     2026.05 (KB3663694  ).
Syntax: long PrepackingAdvice.StartPrintPackingSheet(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  whinh.shpm       iFromShipment,
domain  tcpono           iFromShipmentLine,
domain  tcpono           iFromReferenceSequence,
domain  whwmd.past       iFromPrepackingAdviceStatus,
domain  whinh.shpm       iToShipment,
domain  tcpono           iToShipmentLine,
domain  tcpono           iToReferenceSequence,
domain  whwmd.past       iToPrepackingAdviceStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Print Packing Sheet
(whwmd5440m000). Depending on the main table of the calling
session, Non                      -Consecutive Record Selection (NCRS) is used.
When the main table is:
Prepacking Advice(whwmd540) or
Prepacking Advice Lines (whwmd545) or
Prepacking Advice Proposed Stock Points (whwmd547) or
Prepacking Advice Actual Stock Points (whwmd548) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iFromShipment
From Shipment selection field is filled with this value.
(when iIgnoreSelectionFields is false
and NCRS is not applicable). Optional.
iFromShipmentLine
From Shipment Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable). Optional
iFromReferenceSequence
From Reference Sequence selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable). Optional
iFromPrepackingAdviceStatus
From Prepacking Advice Status selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable). Optional
iToShipment
To Shipment selection field is filled with this value.
(when iIgnoreSelectionFields is false
and NCRS is not applicable). Optional.
iToShipmentLine
To Shipment Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable). Optional.
iToReferenceSequence
To Reference Sequence selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable). Optional
iToPrepackingAdviceStatus
To Prepacking Advice Status selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable). Optional
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

## Public Interfaces for ShipmentPlanning

The following functions are available: ShipmentPlanning.StartOverview ShipmentPlanning.StartOverviewV2
