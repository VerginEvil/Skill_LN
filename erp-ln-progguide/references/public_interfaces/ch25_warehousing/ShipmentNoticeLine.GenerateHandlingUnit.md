# ShipmentNoticeLine.GenerateHandlingUnit

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentNoticeLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1007-1008

```baan
DLL:   whextinhapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long ShipmentNoticeLine.GenerateHandlingUnit(
domain  tccom.bpid       iShipFromBusinessPartner,
domain  whinh.shpm       iShipmentNotice,
domain  tcpono           iShipmentNoticeLine,
ref     domain  whhuid           oHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates Handling Unit Structure for the given
Shipment Notice Line.
Pre:    db.retry.point must be set
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
Input:  iShipFromBusinessPartner              - Ship-from Business Partner - Mandatory
iShipmentNotice                               - Shipment Notice - Mandatory
iShipmentNoticeLine                           - Shipment Notice Line - Mandatory
Output: oHandlingUnit                         - Generated Handling Unit
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
