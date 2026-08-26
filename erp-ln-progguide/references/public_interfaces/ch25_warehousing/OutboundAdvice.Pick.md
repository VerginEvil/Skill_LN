# OutboundAdvice.Pick

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1182-1184

```baan
DLL:   whextinhapi
This function is available from     2026.07 (KB3668952  ).
Syntax: long OutboundAdvice.Pick(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdviceLine,
domain  whhuid           iFromHandlingUnit,
domain  whhuid           iToHandlingUnit,
domain  tcibd.sern       iSerial,
domain  tcclot           iLot,
domain  tcinvt.date      iInventoryDate,
domain  tcqst1           iQuantityPicked,
domain  tccuni           iStorageUnit,
domain  tccwar           iWarehouse,
domain  whloca           iFromLocation,
domain  whloca           iToLocation,
boolean          iFinalPick,
long             iNoLotsSerials,
ref     domain  tcpono           iBomLineArray(),
ref     domain  tcmcs.long       iLotSerialSequenceArray(),
ref     domain  tcclot           iLotArray() fixed,
ref     domain  tcibd.sern       iSerialArray() fixed,
ref     domain  tcqst1           iLotSerialQuantityPickedArray(),
ref     domain  tccuni           iLotSerialStorageUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface has functionality to handle modifications
of the actual picked stock point to reflect the reality of the
picked inventory as opposed to the planned stock point to pick.
This is of course only possible when the inventory is available.
Next to the modification of the picked stock point, it also
allows to handle partial picking for a picking list line. When
this occurs the logic will split the picking list line, by
applying the following logic:
The current picking list is decreased with the quantity that is
to be picked, for the actual picked inventory a new picking list
line is created which will then be picked. When the i.final.pick
is set to yes the process of partial picking is not done, when
the quantity to be picked is less than the remaining quantity
there will be no split, the quantity will be overwritten by the
given i.quantity.picked and the picking list line will be set to
picked.
It will also be possible to provide the high volume lots and/or
serials for items which require this registration during the
picking process. This only applies to items which are having
lots and/or serials not in inventory.
When picking is not part of the procedure, this process applies
to the outbound advice, as that is eventually also picked.
Pre:    db.retry.point()
Post:   commit/abort transaction.
Input:  iOrderOrigin                          - Order Origin (Mandatory)
iOrderNumber                                  - Order Number (Mandatory)
iOrderSet                                     - Order Set (Mandatory)
iOrderLine                                    - Order Line (Mandatory)
iOrderSequence                                - Order Sequence (Optional)
iAdviceLine                                   - Advice Line (Mandatory)
iFromHandlingUnit                             - From Handling Unit (Optional)
iToHandlingUnit                               - To Handling Unit (Optional)
iSerial                                       - Serial Number (Optional)
iLot                                          - Lot Code (Optional)
iInventoryDate                                - Inventory Date (Optional)
iQuantityPicked                               - Quantity Picked (Mandatory)
iStorageUnit                                  - Storage Unit (Mandatory)
iWarehouse                                    - Warehouse (Optional)
iFromLocation                                 - From Location (Optional)
iToLocation                                   - To Location (Optional)
iFinalPick                                    - Final Pick (True/False)
iNoLotsSerials                                - Number of Lots/Serials in arrays
iBomLineArray                                 - BOM Line Array
iLotSerialSequenceArray                       - Lot/Serial Sequence Array
iLotArray                                     - Lot Array
iSerialArray                                  - Serial Array
iLotSerialQuantityPickedArray                       - Lot/Serial Quantity Picked
iLotSerialStorageUnitArray                       - Lot/Serial Storage Unit
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     - Outbound Advice picked successfully
<> 0                          - Picking failed
```
