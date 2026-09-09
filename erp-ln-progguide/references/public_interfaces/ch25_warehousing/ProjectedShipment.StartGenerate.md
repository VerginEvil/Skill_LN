# ProjectedShipment.StartGenerate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectedShipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1188-1190

```baan
DLL:   whextinhapi
This function is available from 2023.07 (KB2293617).
Syntax: long ProjectedShipment.StartGenerate(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  whinh.oorg       iFromOrderOrigin,
domain  tcorno           iFromOrderNumber,
domain  tcwset           iFromOrderSet,
domain  tcpono           iFromOrderLine,
domain  tcpono           iFromOrderSequence,
domain  tcmcs.long       iFromDistributionSequence,
domain  whinh.oorg       iToOrderOrigin,
domain  tcorno           iToOrderNumber,
domain  tcwset           iToOrderSet,
domain  tcpono           iToOrderLine,
domain  tcpono           iToOrderSequence,
domain  tcmcs.long       iToDistributionSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Generate Projected Shipments
(whinh4230m200). Depending on the main table of the calling
session, Non-Consecutive Record Selection (NCRS) is used.
When the main table is:
Warehousing Orders      (whinh200) or
Outbound Order Lines    (whinh220) or
Outbound Order Line - Planned Shipment Requirements
(whinh483) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iFromOrderOrigin
From Order Origin selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderNumber
From Order Number selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderSet
From Order Set selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderLine
From Order Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderSequence
From Sequence selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromDistributionSequence
From Distribution Sequence selection field is filled
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
iToOrderSet
To Order Set selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderLine
To Order Line selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable)
iTomOrderSequence
To Sequence selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToDistributionSequence
To Distribution Sequence selection field is filled
with this value. (when iIgnoreSelectionFields is false
and NCRS is not applicable)
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
