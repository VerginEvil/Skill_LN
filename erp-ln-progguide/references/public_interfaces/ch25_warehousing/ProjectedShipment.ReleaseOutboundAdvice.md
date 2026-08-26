# ProjectedShipment.ReleaseOutboundAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectedShipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1178-1178

```baan
DLL:   whextinhapi
This function is available from     2023.10 (KB2302540  ).
Syntax: long ProjectedShipment.ReleaseOutboundAdvice(
domain  whinh.shpm       iShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will release the outbound advice for the
projected shipment.
No data is printed.
No automatic outbound process is triggered.
Be aware that transaction management is handled within this
function.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iShipment                             - Shipment (Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
