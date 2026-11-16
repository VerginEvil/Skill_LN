# HandlingUnit.StartPrintLabels

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1066-1067

```baan
DLL:   whextwmdapi
This function is available from 2025.07 (KB3571649).
Syntax: long HandlingUnit.StartPrintLabels(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  whhuid           iFromHandlingUnit,
domain  whhuid           iToHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Print Labels (whwmd5430m100).
Depending on the main table of the calling session,
Non-Consecutive Record Selection (NCRS) is used.
When the main table is:
Handling Units (whwmd530) or
Prepacking Advice (whwmd540) or
Inventory Ownership Change Orders (whinh100) or
Inventory Ownership Change Order Lines (whinh110) or
Inventory Ownership Change Order - Inventory Movement (whinh115) or
Allocation Change Orders (whinh120) or
Allocation Change Order Lines (whinh130) or
Warehousing Orders (whinh200) or
Inbound Order Lines (whinh210) or
Warehouse Inspections (whinh211) or
Inbound Advice (whinh215) or
Outbound Order Lines (whinh220) or
Outbound Advice (whinh225) or
Warehouse Inspection Handling Units (whinh234) or
ASN Headers (whinh300) or
ASN Lines (whinh301) or
Receipt Headers (whinh310) or
Receipt Lines (whinh312) or
Shipping Containers (whinh425) or
Shipments (whinh430) or
Shipment Lines (whinh431) or
Cycle Counting Orders (whinh500) or
Cycle Counting Order Lines (whinh501) or
Adjustment Orders (whinh520) or
Adjustment Order Lines (whinh521) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iFromHandlingUnit
From HandlingUnit selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToHandlingUnit
To HandlingUnit selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
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
