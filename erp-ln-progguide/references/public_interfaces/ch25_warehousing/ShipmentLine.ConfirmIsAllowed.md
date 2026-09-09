# ShipmentLine.ConfirmIsAllowed

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1173-1173

```baan
DLL:   whextinhapi
This function is available from 2024.06 (KB2329564).
Syntax: long ShipmentLine.ConfirmIsAllowed(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
boolean          iReadShipmentLine,
ref             boolean          oConfirmationAllowed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will determine if the given
shipment line is allowed to be confirmed or not.
Pre:    Not applicable
Post:   Not applicable
Input:  iShipment               - Mandatory
iShipmentLine           - Mandatory
iReadShipmentLine       - Mandatory
True -> Shipment Line will be read.
False-> Shipment Line is expected to
be current.
Output: oConfirmationAllowed
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
