# PurchaseRequisitionLine.ConvertToPurchaseOrder

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseRequisitionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 419-420

```baan
DLL:   tdextpurapi
This function is available from     2021.05 (KB2185794  ).
Syntax: long PurchaseRequisitionLine.ConvertToPurchaseOrder(
domain  tcrqno           iPurchaseRequisition,
domain  tcpono           iRequisitionLine,
domain  tcseri           iOrderSeries,
domain  tccotp           iOrderType,
domain  tcseri           iSubcontractingOrderSeries,
domain  tccotp           iSubcontractingOrderType,
domain  tcseri           iServiceSubcontractingOrderSeries,
domain  tccotp           iServiceSubcontractingOrderType,
domain  tcyesno          iCalculateNewPriceAndDiscounts,
domain  tcyesno          iCurrencyFromBusinessPartner,
domain  tcorno           iPreviousPurchaseOrder,
domain  tcpono           iPreviousPurchaseOrderLine,
ref     domain  tcorno           oGeneratedOrder,
ref     domain  tcpono           oGeneratedOrderLine,
ref     domain  tcpono           oGeneratedOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts the given requisition line to a purchase
order. Conversion is only allowed if the requisition header has
the proper status (i.e. Approved or In Process), and the
requisition line is not rejected. The Conversion Type of the
requisition line must be 'Purchase Order'.
When input argument iPreviousPurchaseOrder is filled, this
function tries to add a line to that order. If the requisition
line does not match with the given order, then a new purchase
order will be generated. If maximal commingling must be obtained,
then the order in which the requisition lines are converted is
important.
When input argument iPreviousPurchaseOrderLine is filled, the
function tries to add another sequence to that order line.
Pre:    Caller must set a retry              -point
Post:   Caller must commit or abort the transaction.
Input:  iPurchaseRequisition                  - Requisition; Mandatory
iRequisitionLine                              - Requisition Line; Mandatory
iOrderSeries                                  - Order Series that will be used to
generate the purchase order. Depending
on the setup, this can be empty.
iOrderType                                    - Order Type that will be used to
generate the purchase order. Depending
on the setup, this can be empty.
iSubcontractingOrderSeries                            - Order Series for subcontracting
purchase orders.
iSubcontractingOrderType                              - Order Type for subcontracting
purchase orders.
iServiceSubcontractingOrderSeries
-                                                       Order Series for service
subcontracting purchase orders.
iServiceSubcontractingOrderType                       - Order Type for service
subcontracting purchase orders.
iCalculateNewPriceAndDiscounts
-                                               Yes:  LN calculates new prices and
discounts when converting
requisitions to purchase orders.
No:   The prices defined in the
requisition are transferred to
the purchase order.
iCurrencyFromBusinessPartner
-                                               Yes:  LN uses the business partner's
currency on the purchase order.
The requisition's price and
amount are converted to this
currency.
No:   LN uses the currency of the
requisition on the purchase order.
iPreviousPurchaseOrder
-                                               If filled, the function tries to add
a line to that order. Mandatory if
iPreviousPurchaseOrderLine is filled.
iPreviousPurchaseOrderLine
-                                               If filled, the function tries to add
another sequence to that order line.
Output: oGeneratedOrder               - The generated purchase order
oGeneratedOrderLine                           - The generated purchase order line
oGeneratedOrderSequence                       - The generated purchase order
line sequence
Return: 0                                     - The requisition line is converted
<> 0                                          - An error occurred
```
