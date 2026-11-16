# HandlingUnit.MoveToLoad

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1052-1052

```baan
DLL:   whextinhapi
This function is available from 2021.11 (KB2211254).
Syntax: long HandlingUnit.MoveToLoad(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  whhuid           iHandlingUnit,
domain  whinh.load       iDestinationLoad,
domain  tccdis           iReason,
ref     domain  whinh.shpm       oDestinationShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports moving a staged or projecetd
handling unit to the destination load.
If handling unit quantity is less than shipment line quantity,
shipment line will be split; otherwise shipment line will be
moved to other load and shipment.
Pre:    db.retry.point().
Post:   abort/commit transaction.
Input:  iShipment               - Shipment; Mandatory
iShipmentLine           - Shipment Line; Mandatory
iHandlingUnit           - Handling Unit; Mandatory
Only handling units with status
Staged and Projected are allowed.
iDestinationLoad        - Destination Load; Mandatory
iReason                 - Compose Reason; Mandatory if
destination load is planned by FM.
Output: oDestinationShipment    - Destiantion Shipment
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
