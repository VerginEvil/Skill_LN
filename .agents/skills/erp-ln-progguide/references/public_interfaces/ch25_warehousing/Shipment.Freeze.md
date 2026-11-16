# Shipment.Freeze

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1152-1153

```baan
DLL:   whextinhapi
This function is available from 2021.01 (KB2166276).
Syntax: long Shipment.Freeze(
domain  whinh.shpm       iShipment,
domain  tcyesno          iCalculateAdditionalCosts,
ref             boolean          oShipmentLinesFrozen,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will freeze the given Shipment.
When successful, also the automatic outbound process for
printing of shipping documents is started for this shipment.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iShipment               - Mandatory
iCalculateAdditionalCosts
- Mandatory
When this is set to Yes, the existing
additional cost lines will first be
removed, and a new calculation of the
additional cost lines will be
performed.
This excludes the manually created
additional cost lines.
Output: oShipmentLinesFrozen    - One or more Shipment Lines are
frozen
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
