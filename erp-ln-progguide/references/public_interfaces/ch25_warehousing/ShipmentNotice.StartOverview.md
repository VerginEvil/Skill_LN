# ShipmentNotice.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentNotice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1006-1007

```baan
DLL:   whextinhapi
This function is available from     2020.04 (KB2115522  ).
Syntax: long ShipmentNotice.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iShipFromBusinessParter,
domain  whinh.shpm       iShipment,
domain  whinh.stat       iStatus,
domain  whinh.load       iFreightLoad,
domain  tcaref           iSuppliersASN mb,
ref     domain  tccom.bpid       oShipFromBusinessParter,
ref     domain  whinh.shpm       oShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Shipment Notices
(whinh3100m000).
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
"byShipFromBusinessPartnerShipment":
session will be started on index 1
view field: None
"byStatus":
session will be started on index 2
view field: Status
"byFreightLoad":
session will be started on index 3
view field: Freight Load
"byShipFromBusinessPartnerSuppliersASN":
session will be started on index 4
view fields:
ShipFromBusinessPartner
SuppliersASN
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iShipFromBusinessParter
Mandatory when iStartFilter
"byShipFromBusinessPartnerShipment" or
"byShipFromBusinessPartnerSuppliersASN" is used and
the session is started in overview mode with start
mode MODELESS
iShipment
Mandatory when iStartFilter
"byShipFromBusinessPartnerShipment" is used and the
session is started in overview mode with start mode
MODELESS
iStatus
Mandatory when iStartFilter "byStatus"
is used and the session is started in overview mode
with start mode MODELESS
iFreightLoad
iSuppliersASN
Output: for iStartMode MODAL:
oShipFromBusinessParter                       - Ship-from Business Partner of
selected ASN.
oShipment                                     - Shipment of selected ASN.
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

## Public Interfaces for ShipmentNoticeLine

The following functions are available: ShipmentNoticeLine.GenerateHandlingUnit ShipmentNoticeLine.Receive ShipmentNoticeLine.RemoveHandlingUnit
