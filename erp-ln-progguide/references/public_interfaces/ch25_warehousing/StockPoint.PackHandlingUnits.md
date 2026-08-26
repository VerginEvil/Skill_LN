# StockPoint.PackHandlingUnits

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StockPoint
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 987-989

```baan
DLL:   whextinrapi
This function is available from     2022.03 (KB2224782  ).
Syntax: long StockPoint.PackHandlingUnits(
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tcinvt.date      iInventoryDate,
domain  tccuni           iStorageUnit,
domain  tcqst1           iQuantityInStorageUnit,
domain  whwmd.pkdf       iPackageDefinition,
domain  whhuid           iHandlingUnit,
domain  tcuef.mask       iMask,
domain  tcyesno          iSSCC,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
ref     domain  tcmcs.long       oNumberOfHandlingUnits,
ref     domain  whhuid           oHandlingUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will pack the anonymous stock in one or
more handling units.
This public interface can be used only when for the iItem and
iWarehouse combination handling units are used in stock.
Pre:    db.retry.point()
Post:   commit/abort transaction
Input:  iWarehouse                            - Warehouse - Mandatory
iLocation                                     - Location - Mandatory when iWarehouse
and iItem are location controlled.
iItem                                         - Item - Mandatory.
iLot                                          - Lot (in inventory) - Mandatory when
for the iItem the lots are registered
in inventory.
iSerial                                       - Serial (in inventory) - Mandatory when
the iItem is serialized in inventory
iInventoryDate                                - Inventory Date - Mandatory when the
iItem has outbound method FIFO
or LIFO.
iStorageUnit                                  - Storage Unit - Mandatory when iSerial
is empty.
iQuantityInStorageUnit                        - Quantity in Storage Unit - Mandatory
when iSerial is empty.
iPackageDefinition                            - Package Definition - Optional
Package definition must be of type
Variable.
iHandlingUnit                                 - Handling Unit with this Id will be
generated                                                 - Optional
iMask                                         - Handling Unit Mask - Optional if
empty default mask will be used.
iSSCC                                         - iMask is with SSCC standard.
iOrderOrigin                                  - Order Origin - can be used when iMask
contains a segment with this field                                                 -
Optional.
iOrder                                        - Order Number - can be used when iMask
contains a segment with this field                                                 -
Optional.
iOrderSet                                     - Order Set - can be used when iMask
contains a segment with this field                                                 -
Optional.
Output: oNumberHandlingUnits                  - Number of handling units in array.
oHandlingUnitArray                            - Array with generated handling units.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```

## Public Interfaces for StockPointInventory

The following functions are available: StockPointInventory.StartDetail StockPointInventory.StartOverview
