# ShipmentLine.Split

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1168-1170

```baan
DLL:   whextinhapi
This function is available from     2021.11 (KB2211254  ).
Syntax: long ShipmentLine.Split(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  tcpono           iBomLine,
domain  tcqiv1           iSplitQuantity,
long             iNumberStockPoints,
ref     domain  tcibd.sern       iSerialArray() fixed,
ref     domain  tcclot           iLotArray() fixed,
ref     domain  tcinvt.date      iInventoryDateArray(),
ref     domain  tcuef.effn       iEffectivityUnitArray(),
ref     domain  tcqst1           iSplitQuantityArray(),
ref     domain  tccuni           iSplitUnitArray() fixed,
ref     domain  whinh.shpm       ioDestinationShipment,
ref     domain  whinh.load       ioDestinationLoad,
domain  tccdis           iReason,
boolean          iAcceptWarnings,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports splitting of a shipment line and
moving of the splitted stock points.
Split quantity followed by storage unit must be passed for all
shipment line                       - stock point details records, which must be
split.
Total split quantity iSplitQuantity in inventory units must
be equal to the sum of the split quantities in stock point
details.
Based on combiantion of ioDestinationShipment and
ioDestinationLoad the following actions will be executed:
|                      --------------------------------------------------------------
|ioDestShipment | ioDestLoad    | Action
| Filled        | Empty         | Splitted part of shipment line
|               |               | moved to the shipment
| Filled        | Filled        | Check whether shipment matches
|               |               | the load.
|               |               | Splitted part of shipment line
|               |               | moved to the shipment
| Empty         | Filled        | New shipment generated for the
|               |               | Load.
|               |               | Splitted part of shipment line
|               |               | moved to the generated
|               |               | shipment.
| Empty         | Empty         | New shipment and load will be
|               |               | generated.
|                      -------------------------------------------------------------
If parameter iAcceptWarnings is set to True and destination
shipment or destination load is passed to the public interface a
mismatch between the source shipment and the destination
shipment or destination load will be ignored;
otherwise error message will be returned.
Note that in standard LN a mismatch can be ignored by the user
in interactive mode.
Example 1:
Shipment line contains 10 pieces of item A which are distributed
over lots LA1 (4 pieces) and LA2 (6 pieces).
The user wants to split 2 pieces of the lot LA1 to the new
shipment line.
Public Interface must be called as follows:
iSplitQuantity = 2
iNumberStockPoints = 1
iLotArray(1) = LA1
iSplitQuantityArray(1) = 2
Result: 2 pieces of lot LA1 are moved to the new Shipment line.
Example 2:
Shipment line contains 10 pieces of item A which are distributed
over lots LA1 (4 pieces) and LA2 (6 pieces).
The user wants to split 2 pieces of the lot LA1 and 3 pieces of
the lot LA2 to the new shipment line.
Public Interface must be called as follows:
iSplitQuantity = 5
iNumberStockPoints = 2
iLotArray(1) = LA1
iSplitQuantityArray(1) = 2
iLotArray(2) = LA2
iSplitQuantityArray(2) = 3
Result: 2 pieces of lot LA1 and 3 pieces of lot LA2 are moved to
the new Shipment line.
NOTE: Athough some of input parameters are marked as "optional",
they may still be mandatory if they are applicable in a certain
situation.
Example: if an Item has Outbound Method "By Location", then it
is not needed to fill iInventoryDateArray.
But if an Item has Outbound Method "FIFO"/"LIFO", then
Inventory Date is applicable and stockpoint record has
Inventory Date filled. In this case iInventoryDateArray should
be filled.
Pre:    db.retry.point()
Split quantities in the shipment line stock point details are
zero.
Post:   abort/commit transaction
Input:  iShipment                             - Shipment (mandatory)
iShipmentLine                                 - Shipment Line (mandatory)
iBomLine                                      - BOM line (optional)
iSplitQuantity                                - Split Quantity in Inventory Units
(mandatory)
iNumberStockPoints                            - Number of Shipment Line stock point
details to be split (mandatory)
iSerialArray                                  - Array of serials (optional)
iLotArray                                     - Array of lots (optional)
iInventoryDateArray                           - Array of inventory dates (optional)
iEffectivityUnitArray                         - Array of effectivity units (optional)
iSplitQuantityArray                           - Array of split quantities (mandatory)
iSplitUnitArray                               - Array of storage units (mandatory)
ioDestinationShipment                         - Destination Shipment (optional)
ioDestinationLoad                             - Destination Load (optional)
iReason                                       - Compose Reason; Mandatory if
destination load is planned by FM.
iAcceptWarnings                               - Accept warnings; (mandatory)
Output: ioDestinationShipment                 - Shipment, Split quanity is moved to.
ioDestinationLoad                             - Load, Split quanity is moved to.
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
