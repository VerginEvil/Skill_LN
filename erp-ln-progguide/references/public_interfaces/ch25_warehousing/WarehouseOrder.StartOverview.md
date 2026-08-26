# WarehouseOrder.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1025-1028

```baan
DLL:   whextinhapi
This function is available from     2020.03 (KB2112548  ).
Syntax: long WarehouseOrder.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tccfrw           iCarrier,
domain  tcncmp           iShipFromCompany,
domain  tcsite           iShipFromSite,
domain  tctyps           iShipFromType,
domain  tccshp           iShipFromCode,
domain  tcncmp           iShipToCompany,
domain  tcsite           iShipToSite,
domain  tctyps           iShipToType,
domain  tccshp           iShipToCode,
domain  tcitem           iItem,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcorno           oOrder,
ref     domain  tcwset           oOrderSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session
Warehousing Orders (whinh2100m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byOrderOrigin":
data is filtered for order origin
order by can be set with iSessionIndex
"byOrder":
data is filtered for order
order by can be set with iSessionIndex
"byCarrier":
data is displayed by Carrier
session will be started on index 3
view field: Carrier
"byShipFrom":
data is displayed by:
iShipFromSite
iShipFromCompany
iShipFromType
iShipFromCode
session will be started on index 4
view fields:
ShipFromSite (if sites applicable)
ShipFromType
"byShipTo":
data is displayed by:
iShipToSite
iShipToCompany
iShipToType
iShipToCode
session will be started on index 5
view fields:
ShipToSite (if sites applicable)
ShipToType
"byItem":
data is filtered for:
iItem (Mandatory)
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iOrderOrigin
Mandatory when iStartFilter "byOrderOrigin" or "byOrder"
is used and the session is started with start mode MODELESS
iOrder
Mandatory when iStartFilter "byOrder" is used
and the session is started with start mode MODELESS
iOrderSet
Optional.
iCarrier
Optional.
iShipFromCompany
Optional.
iShipFromType
Optional.
iShipFromCode
Optional.
iShipFromSite
Optional.
iShipToCompany
Optional.
iShipToType
Optional.
iShipToCode
Optional.
iShipToSite
Optional.
iItem
Mandatory when iStartFilter "byItem" is used and the
session is started in with start mode MODELESS
Output: for iStartMode MODAL:
oOrderOrigin
oOrder
oOrderSet
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for PackageDefinition

The following functions are available: PackageDefinition.DetermineMultipleOfQuantity PackageDefinition.Validate
