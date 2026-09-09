# WarehouseLocation.StartRecalculateOccupation

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseLocation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1009-1009

```baan
DLL:   whextwmdapi
This function is available from 2024.07 (KB3502697).
Syntax: long WarehouseLocation.StartRecalculateOccupation(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tccwar           iFromWarehouse,
domain  whloca           iFromLocation,
domain  tccwar           iToWarehouse,
domain  whloca           iToLocation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Recalculate Occupation of
Location (whwmd3201m000). Depending on the main table of the
calling session, Non-Consecutive Record Selection (NCRS) is
used.
When the main table is:
Locations (whwmd300) or
Location Capacity (whwmd301) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iFromWarehouse
From Warehouse selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromLocation
From Location selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToWarehouse
To Warehouse selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS is not
applicable)
iToLocation
To Location selection field is filled with this
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
