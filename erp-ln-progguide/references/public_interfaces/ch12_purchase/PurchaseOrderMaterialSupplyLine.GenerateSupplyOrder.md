# PurchaseOrderMaterialSupplyLine.GenerateSupplyOrder

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderMaterialSupplyLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 475-477

```baan
DLL:   tdextpurapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long PurchaseOrderMaterialSupplyLine.GenerateSupplyOrder(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcpono           iMaterialSupplyLineSequence,
domain  tcorno           iProposedSalesOrder,
domain  tcorno           iProposedSalesSchedule,
domain  tcorno           iProposedWarehouseOrder,
domain  tcorno           iProposedPurchaseOrder,
domain  tcorno           iProposedPurchaseSchedule,
ref     domain  tcorno           oSalesOrder,
ref     domain  tcorno           oSalesSchedule,
ref     domain  tcorno           oWarehouseOrder,
ref     domain  tcorno           oPurchaseOrder,
ref     domain  tcorno           oPurchaseSchedule,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to generate a supply order for the given
purchase order material supply line.
The function allows to pass proposed values for the supply order
to be generated with input arguments:
iProposedSalesOrder
iProposedSalesSchedule
iProposedWarehouseOrder
iProposedPurchaseOrder
iProposedPurchaseSchedule
The existing LN logic determines if these proposed order numbers
can be used. With these proposed order numbers it is possible
to combine the supply for different material supply lines in a
single supply order.
The generated/used supply order is returned in one of the output
arguments:
oSalesOrder
oSalesSchedule
oWarehouseOrder
oPurchaseOrder
oPurchaseSchedule
Note:
This function does not start the execution of automatic
order steps. A separate Public Interface can be used to
start automatic order steps if necessary:
'PurchaseOrder.StartAutomaticProcessing'.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder          Purchase Order (Mandatory)
The purchase order of the material supply
line for which a supply order must be
generated.
iOrderLine              Purchase Order Line (Mandatory)
The purchase order line of the material
supply line for which a supply order must
be generated.
iOrderLineSequence      Purchase Order Line Sequence (Mandatory)
The purchase order line sequence number
of the material supply line for which a
supply order must be generated.
iMaterialSupplyLineSequence
Material Supply Line Sequence (mandatory)
The sequence number of the material supply
line for which a supply order must be
generated.
iProposedSalesOrder     Proposed Sales Order (Optional)
The proposed sales order number for the
supply order to be generated.
iProposedSalesSchedule  Proposed Sales Schedule (Optional)
The proposed sales schedule number for
the supply order to be generated.
iProposedWarehouseOrder Proposed Warehouse Order (Optional)
The proposed warehouse order number for
the supply order to be generated.
iProposedPurchaseOrder  Proposed Purchase Order (Optional)
The proposed purchase order number for
the supply order to be generated.
iProposedPurchaseSchedule
Proposed Purchase Schedule (Optional)
The proposed purchase schedule number
for the supply order to be generated.
Output:
oSalesOrder             Sales Order
The sales order generated/used for the
given material supply line.
oSalesSchedule          Sales Schedule
The sales schedule generated/used for the
given material supply line.
oWarehouseOrder         Warehouse Order
The warehouse order generated/used for
the given material supply line.
oPurchaseOrder          Purchase Order
The purchase order generated/used for the
given material supply line.
oPurchaseSchedule       Purchase Schedule
The purchase schedule generated/used for
the given material supply line.
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
