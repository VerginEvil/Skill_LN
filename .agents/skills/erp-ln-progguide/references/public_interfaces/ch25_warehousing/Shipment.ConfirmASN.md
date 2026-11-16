# Shipment.ConfirmASN

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1152-1152

```baan
DLL:   whextinhapi
This function is available from 2026.04 (KB3665487).
Syntax: long Shipment.ConfirmASN(
domain  whinh.shpm       iShipment,
domain  tcyesno          iCancelMessage,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function confirms ASN by shipment.
Pre:    db.retry.point must be set
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
Input:  iShipment               - Shipment (Mandatory)
iCancelMessage          - Cancel Message (Mandatory)
Shipment EDI status will be set to Confirmed when
iCancelMessage reads No or to Cancelled when
iCancelMessage reads Yes.
Cancellation is only allowed when Shipment EDI status
is Sent.
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
