# Shipment.Confirm

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1151-1151

```baan
DLL:   whextinhapi
This function is available from 2020.12 (KB2159758).
Syntax: long Shipment.Confirm(
domain  whinh.shpm       iShipment,
domain  tctrns.date      iInventoryAdjustmentDate,
domain  tcyesno          iCalculateAdditionalCosts,
ref             boolean          oShipmentLinesConfirmed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will confirm the given Shipment.
When successful, also the automatic outbound process is started
for this shipment.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iShipment               - Mandatory
iInventoryAdjustmentDate- Optional.
This field is used for filling of the
inventory adjustment date of the
shipment line (whinh431.iadr).
The iInventoryAdjustmentDate will only
be used when whinh431.iadr is zero.
When iInventoryAdjustmentDate has the
value zero then whinh431.iadr will be
filled with the current date
(utc.num()).
For additional cost lines the date
will remain zero.
iCalculateAdditionalCosts
- Mandatory
When this is set to Yes, the existing
additional cost lines will first be
removed, and a new calculation of the
additional cost lines will be
performed.
This excludes the manually created
additional cost lines.
Output: oShipmentLinesConfirmed - One ore more Shipment Lines are
confirmed
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
