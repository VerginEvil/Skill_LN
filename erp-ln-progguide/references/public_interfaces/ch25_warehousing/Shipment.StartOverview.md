# Shipment.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1158-1159

```baan
DLL:   whextinhapi
This function is available from     2022.08 (KB2252307  ).
Syntax: long Shipment.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iShipment,
domain  whinh.load       iLoad,
domain  tcpono           iLoadingListSequence,
domain  whinh.shpm       iDeliveryNote,
domain  whinh.cntr       iShippingContainer,
domain  tcrefs           iShipmentReference mb,
domain  tccorn           iCustomerOrder mb,
ref     domain  whinh.shpm       oShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Shipments
(whinh4130m000).
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
"byShipment":
data is displayed by Shipment
session will be started on index 1
view field: None
"byLoad":
data is displayed by Load
session will be started on index 2
view field: Load
"byLoadingList":
data is displayed by Loading List
session will be started on index 3
view field: Load
"byDeliveryNote":
data is displayed by Delivery Note
session will be started on index 4
view field: Preliminary Delivery Note
"byShippingContainer":
data is displayed by Shipping Container
session will be started on index 5
view field: Load, Shipping Container
"byShipmentReference":
data is displayed by Shipment Reference
session will be started on index 6
view field: Shipment Reference
"byCustomerOrder":
data is displayed by Customer Order
session will be started on index 7
view field: Customer Order
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iShipment
The Shipment to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byShipment")
iLoad
Optional
iLoadingListSequence
Optional
iDeliveryNote
Optional
iShippingContainer
Optional
iShipmentReference
Optional
iCustomerOrder
Optional
Output: for iStartMode MODAL:
oShipment                                     - selected shipment
oExceptionMessage                             - The last message if any message is
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
