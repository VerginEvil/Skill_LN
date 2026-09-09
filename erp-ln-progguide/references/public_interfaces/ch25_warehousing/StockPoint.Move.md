# StockPoint.Move

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StockPoint
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 996-997

```baan
DLL:   whextinrapi
This function is available from 2020.03 (KB2111387).
Syntax: long StockPoint.Move(
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  whloca           iOriginatingLocation,
domain  whhuid           iHandlingUnit,
domain  tcclot           iLot,
domain  tcinvt.date      iInventoryDate,
domain  whwmd.pkdf       iPackageDefinition,
domain  tcyesno          iFullStockPoint,
domain  tcqst1           iQuantityToMove,
domain  tccuni           iStorageUnit,
ref     domain  tcibd.sern       iSerialArray() fixed,
boolean          iMoveBlockedStockPoint,
domain  whloca           iDestinationLocation,
ref             boolean          oStockPointMoved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will move inventory from the originating stock
point to the destination stock point.
Pre:    db.retry.point() must be set
Post:   abort/commit transaction
Input:  iWarehouse              - Warehouse - Mandatory
iItem                   - Item - Mandatory
iOriginatingLocation    - Originating Location - Mandatory
iHandlingUnit           - Handling Unit - Optional
When the stock point is packed inside
a handling unit, the handling unit
should be passed.
iLot                    - Lot (in inventory)
Mandatory when iItem is lot
controlled in inventory, and the
iHandlingUnit is empty. If
iHandlingUnit is filled the
handling unit will determine the
lot itself, as the lot is stored in
the handling unit stock point details.
iInventoryDate          - Inventory Date
Mandatory when iItem has outbound
method FIFO or LIFO and the
iHandlingUnit is empty. If
iHandlingUnit is filled the handling
unit will determine the inventory date
itself, as the inventory date is
stored in the handling unit stock
point details.
iPackageDefinition      - Fixed Package Definition
Mandatory when the stock point
has inventory structure which uses
a fixed package definition. Otherwise
the inventory structure cannot be
updated properly. Input will not be
validated, if no inventory can be
found the stock point cannot be moved.
iFullStockPoint         - Full Stock Point - Optional
When set to tcyesno.yes, the
iQuantitytoMove is not mandatory
anymore, because the complete stock
point must be moved to the
iDestinationLocation.
iQuantityToMove         - Quantity to Move
Mandatory when iHandlingUnit is empty
and iFullStockPoint is set to
tcyesno.no.
Should be greater than zero when
iHandlingUnit is empty and
iFullStockPoint is set to tcyesno.no.
iStorageUnit            - Storage Unit
Mandatory when iHandlingUnit is empty
and iFullStockPoint is set to
tcyesno.no.
iSerialArray            - Serial Array
Can be passed to indicate which
serials must be moved, if empty the
logic will pick serials from the stock
point which is to be moved.
If iHandlingUnit is passed as empty
the memory should be allocated for the
array, if no inventory allocation is
done, an API error will be given.
iMoveBlockedStockPoint  - Move Blocked Inventory - Mandatory
Value should be true or false.
iDestinationLocation    - Destination Location - Mandatory
Output: oStockPointMoved        - Stock Point Moved, true/false.
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
