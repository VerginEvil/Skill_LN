# Shipment.MoveToLoad

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1144-1144

```baan
DLL:   whextinhapi
This function is available from     2022.08 (KB2248918  ).
Syntax: long Shipment.MoveToLoad(
domain  whinh.shpm       iShipment,
domain  whinh.load       iDestinationLoad,
domain  tccdis           iReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports moving a shipment to the
destination load.
Pre:    db.retry.point()
Post:   abort/commit transactions.
Input:  iShipment                             - Shipment; Mandatory
iDestinationLoad                              - Destination Load; Mandatory
iReason                                       - Compose Reason; Mandatory if
destination Load is planned by FM.
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
