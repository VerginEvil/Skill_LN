# HandlingUnit.CommitInventory

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1033-1034

```baan
DLL:   whextinhapi
This function is available from     2026.09 (KB3693739  ).
Syntax: long HandlingUnit.CommitInventory(
domain  whhuid           iHandlingUnit,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iBomLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function commits a Handling Unit for an Order Line.
The handling unit is always committed in full.
Before committing, the function verifies:
-                       The handling unit exists and is In Stock.
-                       The handling unit is compatible with the order line
(warehouse, item, lot, serial, unit, specification).
-                       The available quantity to commit for the order line is
sufficient to commit the full handling unit.
Inventory Commitments can be generated via public interface
InventoryCommitment.Generate(...)
Pre:    db.retry.point should be set.
Inventory Commitments (whinp200) exists for order line.
Post:   commit or abort transaction depending on the return value.
Input:  iHandlingUnit                         - Handling Unit (Mandatory)
iOrderOrigin                                  - Order Origin (Mandatory)
iOrderNumber                                  - Order Number (Mandatory)
iOrderLine                                    - Order Line (Optional)
iOrderSequence                                - Order Sequence (Optional)
iBomLine                                      - BOM Line (Optional)
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
