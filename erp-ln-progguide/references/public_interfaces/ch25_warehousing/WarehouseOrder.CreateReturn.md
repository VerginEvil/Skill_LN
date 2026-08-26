# WarehouseOrder.CreateReturn

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1013-1016

```baan
DLL:   whextinhapi
This function is available from     2020.11 (KB2152623  ).
Syntax: long WarehouseOrder.CreateReturn(
domain  whinh.oorg       iSourceOrderOrigin,
domain  tcorno           iSourceOrder,
domain  tcwset           iSourceOrderSet,
domain  tcorno           iTargetOrder,
domain  tcseri           iTargetSeries,
domain  tccotp           iOrderType,
domain  tcdate           iDeliveryDate,
domain  tccwoc           iOffice,
domain  tcyesno          iCopyText,
domain  whqty.based.on   iBasedOnQuantity,
domain  tcyesno          iAllOrderLines,
long             iNumberOfReceiptLines,
ref     domain  whinh.shpm       iReceiptArray() fixed,
ref     domain  tcpono           iReceiptLineArray(),
long             iNumberOfShipmentLines,
ref     domain  whinh.shpm       iShipmentArray() fixed,
ref     domain  tcpono           iShipmentLineArray(),
long             iNumberOfOrderLines,
ref     domain  tcpono           iOrderLineArray(),
ref     domain  tcpono           iOrderSequenceArray(),
ref     domain  whinh.oorg       oTargetOrderOrigin,
ref     domain  tcorno           oTargetOrder,
ref     domain  tcwset           oTargetOrderSet,
ref             long             oCreatedNumberOfOrderLines,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a return order for a specified warehouse
order header.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iSourceOrderOrigin
The Order origin to be copied from. This is mandatory to
fill.
iSourceOrder
Order number to be copied from. This is mandatory to
fill.
iSourceOrderSet
Order set to be copied from. This is mandatory to fill.
iTargetOrder
iTargetSeries
There are two options. Specify the order number
(iTargetOrder) to copy to or the series (iTargetSeries)
to be used to create an order number.
iOrderType
The order type for the created order. Optional to
fill.
iDeliveryDate
The delivery date for the created order. Mandatory to
fill.
iOffice
The office for the created order. Optional to fill.
iCopyText
Copy text indicator (Yes/No). Mandatory to fill.
iBasedOnQuantity
Specify which quantity should be used to create the
return order.
-                               whqty.based.on.received: Based on received quantity
-                               whqty.based.on.shipped: Based on shipped quantity
-                               whqty.based.on.ordered: Based on ordered quantity
iAllOrderLines
Return all lines indicator (Yes/No). Mandatory to fill.
When not returning all lines then you have to specify
the (receipt, shipment or order) lines to be copied.
This needs to be done according your iBasedOnQuantity
value.
iNumberOfReceiptLines
Specify the number of receipt lines. This is mandatory
when iAllOrderLines is No and iBasedOnQuantity is
received quantity.
iReceiptArray
Specify the receipts which need to be returned. This is
mandatory when iAllOrderLines is No and iBasedOnQuantity
is received quantity.
iReceiptLineArray
Specify the receipt lines which need to be returned.
This is mandatory when iAllOrderLines is No and
iBasedOnQuantity is received quantity. The receipt of
receipt line should match with the receipt on the same
position of the iReceiptArray.
iNumberOfShipmentLines
Specify the number of shipment lines. This is mandatory
when iAllOrderLines is No and iBasedOnQuantity is
shipped quantity.
iShipmentArray
Specify the shipments which need to be returned. This is
mandatory when iAllOrderLines is No and iBasedOnQuantity
is shipped quantity.
iShipmentLineArray
Specify the shipment lines which need to be returned.
This is mandatory when iAllOrderLines is No and
iBasedOnQuantity is shipped quantity. The shipment of
shipment line should match with the shipment on the same
position of the iShipmentArray.
iNumberOfOrderLines
Specify the number of order lines. This is mandatory
when iAllOrderLines is No and iBasedOnQuantity is
ordered quantity.
iOrderLineArray
Specify the order lines which need to be returned. This
is mandatory when iAllOrderLines is No and
iBasedOnQuantity is ordered quantity.
iOrderSequenceArray
Specify the order line sequences which need to be
returned. This is mandatory when iAllOrderLines is No
and iBasedOnQuantity is ordered quantity. The line
number of the sequence should match with the line on the
same position of the iOrderLineArray.
Output: oTargetOrderOrigin
Origin of the created order.
oTargetOrder
Order number of the created order.
oTargetOrderSet
Order set of the created order.
oCreatedNumberOfOrderLines
Number of order lines which are created.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0               - Success - Return order has been created successfully.
<> 0                       - Error - Return order could not be created. r
```
