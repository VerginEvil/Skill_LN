# ShipmentNotice.SetToScheduledManually

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentNotice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1003-1004

```baan
DLL:   whextinhapi
This function is available from     2026.09 (KB3687302  ).
Syntax: long ShipmentNotice.SetToScheduledManually(
domain  tccom.bpid       iShipFromBusinessPartner,
domain  whinh.shpm       iShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function updates the status of the given Shipment
Notice (ASN) to Scheduled Manually.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iShipFromBusinessPartner              - Ship-from Business Partner (Mandatory)
iShipment                                     - Shipment (Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: Status is updated, <> 0: Error
```
