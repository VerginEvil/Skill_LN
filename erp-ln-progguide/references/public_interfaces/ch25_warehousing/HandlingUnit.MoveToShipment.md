# HandlingUnit.MoveToShipment

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1042-1043

```baan
DLL:   whextinhapi
This function is available from     2021.11 (KB2211254  ).
Syntax: long HandlingUnit.MoveToShipment(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  whhuid           iHandlingUnit,
ref     domain  whinh.shpm       ioDestinationShipment,
domain  tccdis           iReason,
boolean          iAcceptWarnings,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports moving a staged or projected
handling unit to the destination shipment.
If handling unit quantity is less than shipment line quantity,
shipment line will be split;
otherwise complete shipment line will be moved to the
destination shipment.
Pre:    db.retry.point().
Post:   abort/commit transaction.
Input:  iShipment                             - Shipment; Mandatory
iShipmentLine                                 - Shipment Line; Mandatory
iHandlingUnit                                 - Handling Unit; Mandatory
Only handling units with status
Staged or Projected are allowed.
ioDestinationShipment                         - Destination Shipment; Optional
If empty new shipment will be created.
iReason                                       - Compose Reason; Mandatory if
destination shipment belongs to the load which is planned by FM.
iAcceptWarnings                               - Accept Warnings; Mandatory
Output: ioDestinationShipment                 - Destination Shipment
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
