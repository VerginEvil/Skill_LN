# Shipment.RecalculateWeight

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1164-1164

```baan
DLL:   whextinhapi
This function is available from 2025.04 (KB3568308).
Syntax: long Shipment.RecalculateWeight(
domain  whinh.shpm       iShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function recaluclates the weight of the shipment header
and each shipment line
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
Input:  iShipment               - Shipment (Mandatory)
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
