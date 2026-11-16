# PrepackingAdvice.Create

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PrepackingAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1320-1320

```baan
DLL:   whextwmdapi
This function is available from 2026.07 (KB3679984).
Syntax: long PrepackingAdvice.Create(
domain  tcmcs.long       iNumberOfShipments,
ref     domain  whinh.shpm       iShipmentArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will create Prepacking Advices for
the given array of Projected Shipments.
For each shipment in the array, a Prepacking Advice header
and lines will be created and the shipment will be set to
not allow changes.
Note: Shipmnets must be in status Projected.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iNumberOfShipments      - Number of shipments in the array
(Mandatory). Must be greater
than zero.
iShipmentArray          - Array of Shipments for which
Prepacking Advices must be created
(Mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               - Prepacking Advices created successfully
<> 0            - Error
```
