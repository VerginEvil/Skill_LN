# ShipmentLine.ReturnNotShippedGoods

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1177-1177

```baan
DLL:   whextinhapi
This function is available from 2026.10 (KB3684110).
Syntax: long ShipmentLine.ReturnNotShippedGoods(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
long             iProcessingOptionSet,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcorno           oOrderNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns not shipped goods for the shipment line.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iShipment               - Shipment (Mandatory)
iShipmentLine           - Shipment Line (Mandatory)
iProcessingOptionSet Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Return not Shipped Goods (whinh4231m500) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
NAME                    TYPE            DEFAULT
Series                  domain tcseri   Similar to session default
OrderType               domain tccotp   Similar to session default
ActivateOrder           domain tcyesno  tcyesno.no
ProcessOrder            domain tcyesno  tcyesno.no
Output: oOrderOrigin            Order Origin of created order
oOrderNumber            Order Number of created order
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
