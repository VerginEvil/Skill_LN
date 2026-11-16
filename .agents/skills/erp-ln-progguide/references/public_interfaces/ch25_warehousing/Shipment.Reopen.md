# Shipment.Reopen

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1164-1165

```baan
DLL:   whextinhapi
This function is available from 2021.11 (KB2210929).
Syntax: long Shipment.Reopen(
domain  whinh.shpm       iShipment,
ref             boolean          oShipmentReopened,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface reopens the frozen Shipment.
Pre:    db.retry.point()
Post:   abort/commit transaction
Input:  iShipment               - Mandatory
Output: oShipmentReopened       - Shipment is reopened.
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
