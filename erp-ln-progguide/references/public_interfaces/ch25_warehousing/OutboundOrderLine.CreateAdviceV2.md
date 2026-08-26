# OutboundOrderLine.CreateAdviceV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1228-1230

```baan
DLL:   whextinhapi
This function is available from     2026.01 (KB3643788  ).
Syntax: long OutboundOrderLine.CreateAdviceV2(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcpono           ioAdviceLine,
domain  whhuid           iHandlingUnit,
domain  tcmcs.long       iHandlingUnitStpSequence,
domain  whhuid           iToShipmentHandlingUnit,
domain  whwmd.pkdf       iPackageDefinition,
domain  whloca           iFromLocation,
domain  whloca           iToLocation,
ref     domain  whinh.btno       ioRun,
domain  tcqst1           iAdvisedQuantityISU,
domain  tccuni           iUnit,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tcuef.effn       iEffectivityUnit,
domain  tcinvt.date      iInventoryDate,
domain  tcpono           iBomLine,
domain  tcguid           iSpecification,
domain  whinh.load       iLoad,
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  tcpono           iShipmentLineReferenceDist,
boolean          iAdviseNegativeInventory,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate an outbound advice for the
given input.
Pre:    db.retry.point().
Post:   abort/commit transaction.
Input:  iOrderOrigin                                  - Mandatory
iOrderNumber                                          - Mandatory
iOrderLine                                            - Mandatory
iOrderSequence                                        - Mandatory
ioAdviceLine                                          - Optional, when input is 0 a
new advice line will be
generated
iHandlingUnit                                         - Mandatory when ownership
registration is by physical item
or allocation registration is by
physical item.
iHandlingUnitStpSequence                              - Optional
iToShipmentHandlingUnit                               - Optional
iPackageDefinition                                    - Optional
iFromLocation                                         - Mandatory when item and
warehouse are location
controlled and Handling Unit is
empty.
iToLocation                                           - Optional
ioRun                                                 - Optional, when left empty a
new run will be generated
iAdvisedQuantityISU                                   - Mandatory
iUnit                                                 - Mandatory
iLot                                                  - Mandatory if the item is lot
controlled in inventory and
handling unit is empty
iSerial                                               - Mandatory if the item is
serial controlled in inventory
and handling unit is empty
iEffectivityUnit                                      - Mandatory if lot is filled and
item is unit effective and
handling unit is empty
iInventoryDate                                        - Mandatory if the item uses
FIFO or LIFO as its outbound
method and handling unit is
empty
iBomLine                                              - Mandatory if outbound line is
issued by material
iSpecification                                        - Optional. When left empty
specification will be copied
from outbound line or handling
unit if applicable
iLoad                                                 - Optional
iShipment                                             - Optional
iShipmentLine                                         - Optional
iShipmentLineReferenceDist                            - Optional
iAdviseNegativeInventory                              - Mandatory
Boolean indicating whether, in case of a shortage, an
advice must be created which can result in negative
inventory.
-                               true: in case of a shortage, LN tries to create an
outbound advice for the total iAdvisedQuantityISU.
-                               false: in case of a shortage, LN only creates an
outbound advice for the available quantity.
Output: ioAdviceLine                                  - Advice Line
ioRun                                                 - Run
oExceptionMessage                                     - The last message if any
message is found. If more than
one message is given, these are
present in the oExceptionID.
oExceptionID                                          - An ID that refers to the
exception information. Use the
functions in Exception to get
all relevant information.
Return: 0: OK, <> 0: Error
```
