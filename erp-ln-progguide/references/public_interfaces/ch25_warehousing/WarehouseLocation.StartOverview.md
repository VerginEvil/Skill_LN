# WarehouseLocation.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseLocation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1007-1008

```baan
DLL:   whextwmdapi
This function is available from 2024.07 (KB3502697).
Syntax: long WarehouseLocation.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
ref     domain  tccwar           oWarehouse,
ref     domain  whloca           oLocation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Warehouse Locations
(whwmd3500m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byWarehouseLocation":
data is displayed by Warehouse and Location
session will be started on index 1
view field: Warehouse
"byWarehouseFixedLocation":
data is displayed by Warehouse and Fixed Location
session will be started on index 2
view fields: Warehouse, Fixed Location
"byWarehouseLocationOccupied":
data is displayed by Warehouse and Location Occupied
session will be started on index 3
view fields: Warehouse, Location Occupied
"byWarehouseZone":
data is displayed by Warehouse and Zone
session will be started on index 4
view fields: Warehouse, Zone
"byWarehouseSearchArgument":
data is displayed by Warehouse and Search Argument
session will be started on index 5
view field: Warehouse
"byWarehouseOwnerOfInventory":
data is displayed by Warehouse and Owner
session will be started on index 6
view fields: Warehouse, Owner
"byWarehouseLocationType":
data is displayed by Warehouse and Location Type
session will be started on index 7
view field: Warehouse
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iWarehouse
Mandatory when iStartFilter is used or iStartMode =
MODELESS and started in MULTI_OCC mode.
iLocation
Optional
Output: for iStartMode MODAL:
oWarehouse              - Selected Warehouse.
oLocation               - Selected Location.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
