# ShipmentLine.MoveToLoad

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1164-1164

```baan
DLL:   whextinhapi
This function is available from     2021.11 (KB2211254  ).
Syntax: long ShipmentLine.MoveToLoad(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  whinh.load       iDestinationLoad,
domain  tccdis           iReason,
boolean          iAcceptWarnings,
ref     domain  whinh.shpm       oDestinationShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports moving a shipment line to the
destination load.
If parameter iAcceptWarnings is set to True a mismatch between
the source shipment and the destination load will be ignored;
otherwise error message will be returned.
Note that in standard LN a mismatch can be ignored by the user
in interactive mode.
New shipment will be generated and returned to the calling
function.
Pre:    db.retry.point()
Post:   abort/commit transactions.
Input:  iShipment                             - Shipment; Mandatory
iShipmentLine                                 - Shipment Line; Mandatory
iDestinationLoad                              - Destination Load; Mandatory
iReason                                       - Compose Reason; Mandatory if
destination Load is planned by FM.
iAcceptWarnings                               - Accept warnings; Mandatory
Output: oDestinationShipment                  - Generated shipment
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
