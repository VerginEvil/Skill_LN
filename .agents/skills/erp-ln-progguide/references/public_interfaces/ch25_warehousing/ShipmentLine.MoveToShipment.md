# ShipmentLine.MoveToShipment

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1174-1175

```baan
DLL:   whextinhapi
This function is available from 2021.11 (KB2211254).
Syntax: long ShipmentLine.MoveToShipment(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
ref     domain  whinh.shpm       ioDestinationShipment,
domain  tccdis           iReason,
boolean          iAcceptWarnings,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports moving a shipment line from one
shipment to another.
If parameter iAcceptWarnings is set to True a mismatch between
the source shipment and the destination shipment will be ignored;
otherwise error message will be returned.
Note that in standard LN a mismatch can be ignored by the user
in interactive mode.
If no destination shipment is passed a new shipment will be
generated and returned to the calling function.
Pre:    db.retry.point()
Post:   abort/commit transaction
Input:  iShipment               - Shipment; Mandatory
iShipmentLine           - Shipment Line; Mandatory
ioDestinationShipment   - Destination Shipment; Optional
If empty new shipment will be created.
iReason                 - Compose Reason; Mandatory if Shipment
is planned by FM.
iReason                 - Compose Reason; Mandatory if
destination shipment belongs to the load which is planned by FM.
iAcceptWarnings         - Accept warnings; Mandatory
Output: ioDestinationShipment   - Destination Shipment
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
