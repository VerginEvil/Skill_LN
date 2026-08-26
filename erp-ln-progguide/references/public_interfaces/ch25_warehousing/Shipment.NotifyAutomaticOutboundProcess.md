# Shipment.NotifyAutomaticOutboundProcess

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1144-1145

```baan
DLL:   whextinhapi
This function is available from     2025.12 (KB3628999  ).
Syntax: long Shipment.NotifyAutomaticOutboundProcess(
domain  whinh.shpm       iShipment,
ref             boolean          oArrayElementAdded,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface stores the Shipments that must be
processed automatically.
Pre:    N.A.
Post:   Start Warehousing.StartAutomaticOutboundProcessing()
Input:  iShipment                             - Shipment. Must be in status Confirmed
or Frozen
Output: oArrayElementAdded                    - True if the iShipment has been added
to array
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```
