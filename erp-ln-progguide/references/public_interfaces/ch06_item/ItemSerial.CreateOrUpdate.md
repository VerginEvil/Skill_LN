# ItemSerial.CreateOrUpdate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemSerial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 222-223

```baan
DLL:   tcextibdapi
This function is available from     2025.12 (KB3628975  ).
Syntax: long ItemSerial.CreateOrUpdate(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcclot           iLot,
domain  tcuef.effn       iEffectivityUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface updates an exiting item serial number with
the lot and effectivity unit. Only items with item type Product
and Rental Product can be updated.
If the serial does not exist it will be created.
Pre:    db.retry.point()
Post:   abort or commit transaction
iItem                                         - Item (Mandatory).
iSerialNumber                                 - Serial Number (Mandatory).
iLot                                          - Lot (Optional).
iEffectivityUnit                              - Effectivity Unit (Optional).
If Item is lot controlled, Effectivity
Unit will be taken from Lot. In this
case the value must be 0 (zero).
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Successfully updated.
<> 0                                          - Otherwise.
```
