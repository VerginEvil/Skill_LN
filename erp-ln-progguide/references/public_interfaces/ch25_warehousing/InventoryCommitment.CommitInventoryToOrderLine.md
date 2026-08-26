# InventoryCommitment.CommitInventoryToOrderLine

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 956-958

```baan
DLL:   whextinpapi
This function is available from     2023.12 (KB2310181  ).
Syntax: long InventoryCommitment.CommitInventoryToOrderLine(
domain  whinp.corg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iBillOfMaterialLine,
domain  tcitem           iItem,
domain  tcuef.effn       iOldEffectivityUnit,
domain  tcuef.effn       iEffectivityUnit,
domain  tcguid           iSpecification,
domain  tccwar           iWarehouse,
domain  tcqiv1           iCommittedInOrderUnit,
domain  tccuni           iOrderUnit,
domain  tcqiv1           iOrderQuantity,
domain  tctrns.date      iPlannedDeliveryDate,
boolean          iInventoryBuffer,
boolean          iUpdateRelatedOrderLine,
ref     domain  tcqiv1           oCommittedInInventoryUnit,
ref     domain  tcqiv1           oCommittedInOrderUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function allows to update the inventory committed
quantity to an "issue" order like: Sales Orders, Production
Orders, Service Orders, PRP Orders, Sales Schedules, Transfer
Orders.
The function checks the available to commit inventory, and the
commitment date. The committed quantity cannot exceed the
available to commit quantity, nor the order quantity.
A check is executed on the minimum commitment quantity/rate.
After commitment, the issue orders (sales orders) are updated
accordingly.
The new committed quantity becomes iCommittedInOrderUnit
(if possible)
When iCommittedInOrderUnit = 0.0, the function perform a
de                      -commitment (remove the committed quantity).
It is expected that the issue order has been read and checked
whether the commitment is allowed from the order standpoint.
Input:  iOrderOrigin                          - Order Origin (Mandatory)
iOrderNumber                                  - Order Number (Mandatory)
iOrderLine                                    - Order Line
iOrderSequence                                - Order Sequence
iBillOfMaterialLine                           - Bill of Material Line
iItem                                         - Item (Mandatory)
iOldEffectivityUnit                           - Old Effectivity Unit
iEffectivityUnit                              - Effectivity Unit
iSpecification                                - Specification
iWarehouse                                    - Warehouse (Mandatory)
iCommittedInOrderUnit                         - New committed quantity (to update the
old one) expressed in order units.
iOrderUnit                                    - Order Unit
iOrderQuantity                                - Order Quantity
iPlannedDeliveryDate                          - Planned Delivery Date (Mandatory)
iInventoryBuffer                              - To avoid the check on the available
to commit quantity.
This is used for "Consumption of
Inventory Buffers" ONLY !
true: the DLL is used for commitment
within the consumption of
inventory buffers
false: otherwise (common value)
iUpdateRelatedOrderLine                       - Update Related Order Line
-                                               true: committed quantitity is also
updated towards the related
order line (e.g. Sales line)
false: otherwise
Output: o.committed.in.inventory.unit
-                                               Committed quantity in inventory unit
o.committed.in.order.unit
-                                               Committed quantity in order unit
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No error has been detected.
<> 0                                          - An Error is detected.
```
