# ShipmentLine.Confirm

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1172-1173

```baan
DLL:   whextinhapi
This function is available from 2022.06 (KB2245586).
Syntax: long ShipmentLine.Confirm(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will confirm the given shipment line.
When successful, also the automatic outbound process is started
for this shipment line.
Be aware that transaction management is handled within this
function.
Pre:    Not applicable
Post:   Not applicable
Input:  iShipment               - Mandatory
iShipmentLine           - Mandatory
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
