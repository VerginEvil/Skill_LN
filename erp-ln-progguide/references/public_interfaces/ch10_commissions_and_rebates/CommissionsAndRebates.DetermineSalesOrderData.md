# CommissionsAndRebates.DetermineSalesOrderData

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for CommissionsAndRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 374-376

```baan
DLL:   tdextcmsapi
This function is available from     2020.10 (KB2134632  ).
Syntax: long CommissionsAndRebates.DetermineSalesOrderData(
domain  tdcms.type       iCommissionRebateType,
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcpono           iSalesOrderDeliverySequence,
domain  tcpono           iSalesOrderInvoiceLine,
domain  tccom.bpid       iRelation,
domain  tdcms.cmcm       iCalculationMethod,
domain  tdcms.cmac       iCalculationMethodForDeliveries,
ref     domain  tcitem           oSalesOrderItem,
ref     domain  tccuni           oSalesOrderUnit,
ref     domain  tcconv           oSalesOrderUnitConversionFactor,
ref     domain  tccprj           oSalesOrderProject,
ref     domain  tcdate           oSalesOrderOrderDate,
ref     domain  tcdate           oSalesOrderRateDate,
ref     domain  tcrtyp           oSalesOrderRateType,
ref     domain  tcratc           oSalesOrderRate(),
ref     domain  tcratf           oSalesOrderRateFactor(),
ref     domain  tcdate           oSalesOrderDeliveryDate,
ref     domain  tcttyp           oSalesOrderTransactionType,
ref     domain  tcinvn           oSalesOrderInvoiceNumber,
ref     domain  tcdate           oSalesOrderInvoiceDate,
ref     domain  tcncmp           oSalesOrderInvoiceCompany,
ref     domain  tcqiv1           oSalesOrderTotalQuantity,
ref     domain  tcamnt           oSalesOrderTotalNetAmount,
ref     domain  tcqiv1           oSalesOrderAccumulatedOrderQuantity,
ref     domain  tcamnt           oSalesOrderAccumulatedOrderAmount,
ref     domain  tdcms.cmpr       oSalesOrderGrossProfit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function determines sales order (line) data based on history,
including accumulated quantity and amount.
Sales order gross profit is also calculated which is used while
searching commission and rebate agreements.
Depending on the Calculation Method (tdcms010.calm) the intake
and cancellation records (tdsls451) are taken or the turnover
records (tdsls456).
Basically, total and accumulated quantity and amount are
calculated as follows:
Linking of Relations On: Sales Order
Calculation Method: Sales Order
-                               Total amount = sum of all sales order history lines
(tdsls451)
-                               Accumulated amount = sum of all sales order history
lines (tdsls451)
Calculation Method: Sales Invoice / Paid Sales Invoice
-                               Total amount = sum of all sales order delivery history
lines (tdsls456)
-                               Accumulated amount = sum of all sales order delivery
history lines (tdsls456)
Linking of Relations On: Sales Order Line
Calculation Method: Sales Order
-                               Total amount = sum of all sales order history lines
(tdsls451), intake and cancellation
based on sales order/line/sequence
Calculation method for deliveries: Separately
-                               Accumulated amount = sum of all sales order history
lines (tdsls451), intake and
cancellation based on
sales order/line/sequence
Calculation method for deliveries: Accumulate, Ordered
-                               Accumulated amount = sum of all sales order history
lines (tdsls451), intake and
cancellation based on
sales order/line
Calculation Method: Sales Invoice / Paid Sales Invoice
-                               Total amount = sum of all sales order delivery history
lines (tdsls456), based on sales order/
line/sequence/delivery sequence/invoice
line
Calculation method for deliveries: Separately
-                               Accumulated amount = sum of all sales order delivery
history lines (tdsls456),
based on sales order/line/
sequence/delivery sequence/
invoice line
Calculation method for deliveries:
Accumulate/Fully Invoiced Line
Accumulate/Partial Invoiced Line
-                               Accumulated amount = sum of all sales order delivery
history lines (tdsls456),
based on sales order/line/
sequence
Pre:    None
Post:   None
Input:  iCommissionRebateType                         - Type Commission or Rebate
|**************************************************************
|* Sales order (line) related arguments based on Sales Order
|* (Line) History (tdsls451/tdsls456)
|**************************************************************
iSalesOrder                                           - Sales Order (Mandatory)
iSalesOrderLine                                       - Sales Order Line
iSalesOrderSequence                                   - Sales Sequence Number, it is 0
in case the Commission/Rebate
Parameter 'Linking of
Relations On' is set to Sales
Order
iSalesOrderDeliverySequence                           - Sales Order Delivery Sequence
Line
iSalesOrderInvoiceLine                        - Sales Order Invoice Line
iRelation                                             - Relation by sales order line
iCalculationMethod                                    - Calculation Method defined
in Relations, used to control
when the commissions and
rebates are calculated
iCalculationMethodForDeliveries
-                                                       Calculation Method for
Deliveries defined in
Relations, used to control how
the commissions and rebates
are calculated after sales
order deliveries are executed.
Output: oSalesOrderItem                               - Sales order line item
oSalesOrderUnit                                       - Sales order unit
oSalesOrderUnitConversionFactor
-                                                       Conversion Factor Sales to
Inventory Unit
oSalesOrderProject                                    - Sales order line project
oSalesOrderDate                                       - Sales order date
oSalesOrderRateDate                                   - Sales order rate date
oSalesOrderRateType                                   - Sales order rate type
oSalesOrderRate                                       - Sales order rates
oSalesOrderRateFactor                                 - Sales order rate factor
oSalesOrderDeliveryDate                               - Sales order delivery date
oSalesOrderTransactionType                            - Sales order transaction type
oSalesOrderInvoiceNumber                              - Sales order invoice number
oSalesOrderInvoiceDate                                - Sales order invoice date
oSalesOrderInvoiceCompany                             - Sales order invoice company
oSalesOrderTotalQuantity                              - Sum of all quantities in sales
order unit.
oSalesOrderTotalNetAmount                             - Sum of all amounts in sales
order currency
oSalesOrderAccumulatedOrderQuantity
-                                                       Accumulated quantity in sales
order unit. See explanation
above.
oSalesOrderAccumulatedOrderAmount
-                                                       Accumulated net amount in sales
order currency. See explanation
above.
oSalesOrderGrossProfit                                - Sales order gross profit
oExceptionMessage       The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               Sales order history records exist and
quantities/amounts could be calculated
<> 0            Sales order history records do not exist or
quantity/amounts could not be calculated.
```
