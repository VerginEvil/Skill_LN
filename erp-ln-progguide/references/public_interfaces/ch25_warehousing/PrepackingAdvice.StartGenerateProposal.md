# PrepackingAdvice.StartGenerateProposal

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PrepackingAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1321-1322

```baan
DLL:   whextwmdapi
This function is available from 2026.05 (KB3663670).
Syntax: long PrepackingAdvice.StartGenerateProposal(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  whinh.shpm       iShipment,
domain  tcpono           iFromShipmentLine,
domain  tcpono           iFromReferenceSequence,
domain  tcpono           iToShipmentLine,
domain  tcpono           iToReferenceSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Generate Proposed Stock Points
(whwmd5247m000). Depending on the main table of the calling
session, Non-Consecutive Record Selection (NCRS) is used.
When the main table is:
Prepacking Advice(whwmd540) or
Prepacking Advice Lines (whwmd545) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iShipment
Shipment selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable). Optional
iFromShipmentLine
From Shipment Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable). Optional
iFromReferenceSequence
From Reference Sequence selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable). Optional
iToShipmentLine
To Shipment Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable). Optional.
iToReferenceSequence
To Reference Sequence selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable). Optional
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
