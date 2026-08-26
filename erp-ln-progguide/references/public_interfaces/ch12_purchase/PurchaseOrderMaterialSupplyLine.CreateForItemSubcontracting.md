# PurchaseOrderMaterialSupplyLine.CreateForItemSubcontracting

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderMaterialSupplyLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 473-474

```baan
DLL:   tdextpurapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long PurchaseOrderMaterialSupplyLine.CreateForItemSubcontracting(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tcguid           iSpecification,
domain  tclsel           iLotSelection,
domain  tcqrd1           iRequiredQuantity,
domain  tcdate           iPlannedReceiptDate,
domain  tcpric           iCustomsValue,
domain  tcccur           iCustomsValueCurrency,
domain  tccwar           iSupplyFromWarehouse,
domain  tccwar           iSupplyToWarehouse,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to create a material supply line in
an item subcontracting scenario for a subcontracted purchase
order line.
In the item subcontracting scenario the whole production of an
end item is subcontracted, materials that must be supplied to
the subcontractor can be added as material supply lines to
the order line of the end item.
This function does not support the operation subcontracting
scenario where only one or more operations of the production of
an end item are subcontracted. In that scenario, the material
supply lines can only be maintained from the production order.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder          Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iOrderLineSequence      Purchase Order Line Sequence (Mandatory)
iItem                   Item (Mandatory)
The item that must be supplied to the
subcontractor.
iEffectivityUnit        Effectivity Unit
iSpecification          Specification GUID
iLotSelection           Lot Selection
This field is mandatory when the concept
'Lot Control in Use' is implemented.
If not implemented it can be set to 0.
iRequiredQuantity       Required Material Quantity in inventory
unit (Mandatory)
iPlannedReceiptDate     Planned Receipt Date
iCustomsValue           Customs Value
iCustomsValueCurrency   Customs Value Currency (Mandatory if
iCustomsValue is not 0)
iSupplyFromWarehouse    Supply                      -from Warehouse
iSupplyToWarehouse      Supply                      -to Warehouse
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
