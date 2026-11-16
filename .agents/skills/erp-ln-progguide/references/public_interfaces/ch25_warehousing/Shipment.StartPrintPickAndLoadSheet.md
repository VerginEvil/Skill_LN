# Shipment.StartPrintPickAndLoadSheet

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1169-1171

```baan
DLL:   whextinhapi
This function is available from 2023.01 (KB2272718).
Syntax: long Shipment.StartPrintPickAndLoadSheet(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  whinh.load       iFromLoad,
domain  whinh.shpm       iFromShipment,
domain  tcdate           iFromPlannedDeliveryDate,
domain  whinh.oorg       iFromOrderOrigin,
domain  tcorno           iFromOrderNumber,
domain  tcpono           iFromOrderLine,
domain  whinh.load       iToLoad,
domain  whinh.shpm       iToShipment,
domain  tcdate           iToPlannedDeliveryDate,
domain  whinh.oorg       iToOrderOrigin,
domain  tcorno           iToOrderNumber,
domain  tcpono           iToOrderLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Print Pick and Load Sheet
(whinh4430m200). Depending on the main table of the calling
session, Non-Consecutive Record Selection (NCRS) is used.
When the main table is:
Shipments       (whinh430) or
Loads           (whinh440) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iFromLoad
From Load selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromShipment
From Shipment selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromPlannedDeliveryDate
From Planned Delivery Date selection field is filled
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
iToLoad
To Load selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToShipment
To Shipment selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToPlannedDeliveryDate
To Planned Delivery Date selection field is filled
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
