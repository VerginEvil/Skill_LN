# WarehouseOrderLine.UpdatePlannedDates

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1297-1297

```baan
DLL:   whextinhapi
This function is available from 2023.11 (KB2308224).
Syntax: long WarehouseOrderLine.UpdatePlannedDates(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcdate           iPlannedDeliveryDate,
domain  tcdate           iPlannedReceiptDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function updates the planned dates of a warehouse order
line
Pre:    db.retry.point must be set
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
Input:  iOrderOrigin - Order Origin; Mandatory
iOrderNumber - Order Number; Mandatory
iOrderLine - Order Line
iOrderSequence - Order Sequence
iPlannedDeliveryDate - Planned Delivery Date; Mandatory
iPlannedReceiptDate - Planned Receipt Date; Mandatory
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0 - Planned Dates updated succesfully
DALHOOKERROR - An error occured when updating Planned Dates
```
