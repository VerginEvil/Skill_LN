# StockPoint.CheckBlocking

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StockPoint
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 994-996

```baan
DLL:   whextinrapi
This function is available from 2022.02 (KB2228439).
Syntax: long StockPoint.CheckBlocking(
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  whhuid           iHandlingUnit,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tctrns.date      iInventoryDate,
domain  whwmd.pkdf       iPackageDefinition,
domain  tccuni           iStorageUnit,
domain  tcqst1           iQuantityInStorageUnit,
domain  tcqiv1           iQuantityInInventoryUnit,
boolean          iInterWarehouseTransfer,
boolean          iIntraWarehouseTransfer,
boolean          iIssueFromQuarantine,
boolean          iProcessingPickOutboundAdvice,
boolean          iProcessingShipment,
boolean          iCheckManualBlock,
ref             boolean          oStockPointBlocked,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function detects whether inventory is blocked which
prevents the inventory from being used.
Manual Blockings are never checked for serials and only
evaluated in case one of the following variables is true:
- iProcessingPickOutboundAdvice
- iProcessingShipment
- iCheckManualBlock
Input:  iWarehouse              - Warehouse - Mandatory
iLocation               - Location - Mandatory when warehouse
and item are location controlled.
iItem                   - Item - Mandatory when iHandlingUnit is
empty.
iHandlingUnit           - Handling Unit - Mandatory when iItem
is empty.
iLot                    - Lot (in inventory) - Mandatory when
for the item the lots are registered
in inventory and iHandlingUnit is
empty.
iSerial                 - Serial (in inventory) - Mandatory
when for the item, the serials are
registered in inventory and
iHandlingUnit is empty.
iInventoryDate          - Inventory Date - Mandatory when the
item has outbound method FIFO
or LIFO and iHandlingUnit is empty.
iPackageDefinition      - Package Definition - Optional
iStorageUnit            - Storage Unit - Mandatory when iSerial
is empty.
iQuantityInStorageUnit  - Quantity in Storage Unit - Mandatory
when iSerial is empty.
iQuantityInInventoryUnit
- Quantity in Inventory Unit - Mandatory
when Handling Unit is empty.
iInterWarehouseTransfer
- Intra Warehouse Transfer - Mandatory
Movement between warehouses.
Value should be true or false.
iIntraWarehouseTransfer
- Inter Warehouse Transfer - Mandatory
Movement within a warehouse between
locations.
Value should be true or false.
iIssueFromQuarantine    - Issue from Quarantine Inventory
- Mandatory
Value should be true or false.
iProcessingPickOutboundAdvice
- Processing step is Pick Outbound
Advice - Mandatory
Value should be true or false.
iProcessingShipment     - Processing step is Shipping
- Mandatory
Overrules processing step Pick
Outbound Advice when both are true.
Value should be true or false.
iCheckManualBlock       - Check on Manual Block is performed.
- Mandatory
Value should be true or false.
Output: oStockPointBlocked      - Stock Point Blocked, true/false.
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
