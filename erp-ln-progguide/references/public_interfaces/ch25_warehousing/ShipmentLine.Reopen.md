# ShipmentLine.Reopen

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1166-1167

```baan
DLL:   whextinhapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long ShipmentLine.Reopen(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
ref             boolean          oShipmentLineReopened,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface reopens the given frozen shipment line.
Pre:    db.retry.point()
Post:   abort/commit transaction
Input:  iShipment                             - Shipment (Mandatory)
iShipmentLine                                 - Shipment Line (Mandatory)
Output: oShipmentLineReopened                 - Shipment Line is reopened.
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
