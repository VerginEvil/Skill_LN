# FreightPlanning.MoveShipmentLine

> Chapter: Chapter 26 Public Interfaces for Freight
>
> Group: Public Interfaces for FreightPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1333-1334

```baan
DLL:   fmextlbdapi
This function is available from 2026.04 (KB3665487).
Syntax: long FreightPlanning.MoveShipmentLine(
domain  tcorno           iSourcePlan,
domain  tcorno           iSourceLoad,
domain  tcorno           iSourceShipment,
domain  tcpono           iSourceShipmentLine,
domain  tcorno           iDestinationPlan,
domain  tcorno           iDestinationLoad,
domain  tcorno           iDestinationShipment,
boolean          iMergeShipmentLines,
boolean          iDeleteEmptyLoad,
boolean          iDeleteEmptyShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function moves as shipment line to a different plan, load
and/or shipment. When the load or shipment are empty, new load
and/or shipments are created based on the source shipment line.
If destination load/shipment is given, it must belong to the
destination plan/load.
Pre:    db.retry.point() is set
Post:   transaction handling (abort/commit)
exception handling can be done when applicable
Input:  iSourcePlan             - Plan from which shipment line must be
moved (mandatory)
iSourceLoad             - Load from which shipment line must be
moved (mandatory)
iSourceShipment         - Shipment from which shipment line must
be moved (mandatory)
iSourceShipmentLine     - Shipment Line to be moved (mandatory)
iDestinationPlan        - Plan to which shipment line must be
moved (mandatory)
iDestinationLoad        - Load to which shipment line must be
moved (optional)
iDestinationShipment    - Shipment to which shipment line must
be moved (optional)
iMergeShipmentLines     - If there are shipment lines in the
destination load for the same freight
order line, these lines must be merged
iDeleteEmptyLoad        - If there are no lines left, the source
load can be deleted
iDeleteEmptyShipment    - If there are no lines left, the source
shipment can be deleted
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
