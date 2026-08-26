# ShipmentLine.Cancel

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1162-1162

```baan
DLL:   whextinhapi
This function is available from     2023.09 (KB2304375  ).
Syntax: long ShipmentLine.Cancel(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  tcyesno          iFinalizeOrderLine,
domain  tcyesno          iReturnToStock,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will cancel the given shipment line.
Not shipped goods can be returned to the stock if required.
Be aware that transaction management is handled within this
function.
Pre:    Not applicable
Post:   Not applicable
Input:  iShipment                             - Shipment (Mandatory)
iShipmentLine                                 - Shipment Line (Mandatory)
iFinalizeOrderLine                            - Finalize order line if tolerances are
met and no unprocessed advice lines or
shipment lines are present (Mandatory)
iReturnToStock                                - Return not shipped goods to stock
(Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```
