# CommissionsAndRebates.EvaluateAgreementGrades

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for CommissionsAndRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 376-380

```baan
DLL:   tdextcmsapi
This function is available from     2020.10 (KB2134632  ).
Syntax: long CommissionsAndRebates.EvaluateAgreementGrades(
domain  tdcms.type       iCommissionRebateType,
domain  tdcms.prty       iAgreementSearchPriority,
domain  tcitem           iAgreementItem,
domain  tckogr           iAgreementGradebyQuantityAmount,
domain  tcccur           iAgreementCurrency,
domain  tccuni           iAgreementGradeUnit,
domain  tcconv           iGradeUnitConversionFactor,
domain  tcgnpr           iAgreementGradeCalculation,
domain  tdcms.fagu       iAgreementFixedAmountOn,
domain  tdcms.grtl       iAgreementCommissionRebateOver,
domain  tdcms.grtl       iAgreementGrowCommissionRebateOver,
domain  tdcms.pyrs       iAgreementInvoiceDirectReserve,
domain  tccdsc           iAgreementDiscountCode,
domain  tcqanp           iAgreementGradeUpToQuantityAmount,
domain  tdcms.cmpr       iAgreementGrossProfitPercentage,
domain  tdcms.cmpr       iAgreementCommissionRebatePercentage,
domain  tdcms.cmpr       iAgreementGrowPercentage,
domain  tcamnt           iAgreementFixedAmount,
domain  tcamnt           iAgreementMaximumLimit,
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcpono           iSalesOrderDeliverySequence,
domain  tcpono           iSalesOrderInvoiceLine,
domain  tcncmp           iSalesOrderInvoiceCompany,
domain  tcttyp           iSalesOrderTransactionType,
domain  tcinvn           iSalesOrderInvoiceNumber,
domain  tcdate           iSalesOrderInvoiceDate,
domain  tccwoc           iSalesOrderOffice,
domain  tccwoc           iSalesOrderFinancialDepartment,
domain  tcamnt           iSalesOrderAmount,
domain  tcccur           iSalesOrderCurrency,
domain  tcqiv1           iSalesOrderQuantity,
domain  tccuni           iSalesOrderUnit,
domain  tcconv           iSalesOrderUnitConversionFactor,
domain  tcdate           iSalesOrderRateDate,
domain  tcrtyp           iSalesOrderRateType,
ref     domain  tcratc           iSalesOrderRate(),
ref     domain  tcratf           iSalesOrderRateFactor(),
domain  tdcms.cmpr       iSalesOrderGrossProfitPercentage,
domain  tcqiv1           iSalesOrderAccumulatedOrderQuantity,
domain  tcamnt           iSalesOrderAccumulatedOrderAmount,
domain  tccom.bpid       iRelation,
domain  tdcms.rtyp       iRelationType,
domain  tcpono           iRelationSequence,
domain  tdcms.cupf       iRelationCurrencyForInvoicing,
domain  tccom.bpid       iRelationBuyFromBusinessPartner,
domain  tccom.bpid       iRelationSoldToBusinessPartner,
ref     domain  tcccur           oCommissionRebateInvoiceCurrency,
ref     domain  tdcms.cmpr       oCommissionRebatePercentage,
ref     domain  tdcms.cmpr       oCommissionRebateGrowPercentage,
ref     domain  tcamnt           oCommissionRebateGrowAmount,
ref     domain  tcamnt           oCommissionRebateFixedAmountInOrderCurrency,
ref     domain  tcamnt           oCommissionRebateSalesOrderAmountInOrderCurrency,
ref     domain  tcamnt           oCommissionRebateAmountInOrderCurrency,
ref             boolean          oSkipCommissionRebateAgreement,
ref             boolean          oStopSearchingAgreement,
ref             boolean          ioInitializeStatics,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function searches and applies agreements based on the search
priority which is used to calculate the commissions and rebates.
Pre:    None
Post:   None
Input:  iCommissionRebateType                         - Type Commission or Rebate
iAgreementSearchPriority                              - Agreement search priority
as defined in Commissions and
Rebates parameters
|**************************************************************
|* Input arguments as defined in Commissions/Rebates Agreements
|**************************************************************
iAgreementItem                                        - Agreement Item
iAgreementGradeByQuantityAmount
-                                                       Agreement Grade by Quantity/
Amount
iAgreementCurrency                                    - Agreement Currency
iAgreementGradeUnit                                   - Agreement Grade Unit
iGradeUnitConversionFactor                            - Conversion factor between
inventory unit of item and
Commission/Rebate Agreement
Grade Unit Only applicable
in case Agreement Grade by
Quantity/Amount is set to
Quantity
iAgreementGradeCalculation                            - Agreement Grade Calculation
Gross/Net
iAgreementFixedAmountOn                               - Agreement Fixed Amount on
Grade/Total
iAgreementCommissionRebateOver
-                                                       Agreement Commission/Rebate
Over Grade/Total
iAgreementGrowCommissionRebateOver
-                                                       Agreement Grow Commission/
Rebate Over Grade/Total
iAgreementInvoiceDirectReserve
-                                                       Agreement Invoice/Reserve
iAgreementDiscountCode                                - Agreement Discount Code
iAgreementGradeUpToQuantityAmount
-                                                       Agreement Grade Upto Quantity/
Amount. In case Agreement
Grade by Quantity/Amount is
set to 'Amount' then Agreement
Grade is Upto Amount
otherwise it is Upto Quantity
iAgreementGrossProfitPercentage
-                                                       Agreement Grade Gross Profit
Percentage
iAgreementCommissionRebatePercentage
-                                                       Agreement Grade
Commission/Rebate Percentage
iAgreementGrowPercentage                              - Agreement Grade Growing
Percentage
iAgreementFixedAmount                                 - Agreement Grade Fixed Amount
iAgreementMaximumLimit                                - Agreement Grade Maximum Limit
|**************************************************************
|* Sales order (line) related arguments based on Sales Order
|* (Line) History (tdsls451/tdsls456)
|**************************************************************
iSalesOrder                                   - Sales Order
iSalesOrderLine                               - Sales Order Line
iSalesOrderSequence                           - Sales Sequence Number, it is 0 in case
the Commission/Rebate Parameter
'Linking of Relations On' is set to
Sales Order
iSalesOrderDeliverySequence
-                                               Sales Order Delivery Sequence Line
iSalesOrderInvoiceLine                        - Sales Order Invoice Line
iSalesOrderInvoiceCompany
-                                               Sales Order Line Invoice Company
iSalesOrderTransactionType
-                                               Sales Order Line Transaction Type
iSalesOrderInvoiceNumber
-                                               Sales Order Line Invoice Number
iSalesOrderInvoiceDate                        - Sales Order Line Invoice Date
iSalesOrderOffice                             - Sales Order Line Sales Office
iSalesOrderFinancialDepartment
-                                               Sales Order Line Financial Department
iSalesOrderAmount                             - Sales Order Line amount in order
currency
iSalesOrderCurrency                           - Sales Order Currency
iSalesOrderQuantity                           - Sales Order Line quantity in
sales Order Line unit
iSalesOrderUnit                               - Sales Order Line Unit
iSalesOrderUnitConversionFactor
-                                               Conversion Factor Sales to Inventory
Unit
iSalesOrderRateDate                           - Sales Order Line Rate Date
iSalesOrderRateType                           - Sales Order Line Rate Type
iSalesOrderRate                               - Sales Order Line Rate
iSalesOrderRateFactor                         - Sales Order Line Rate Factor
iSalesOrderGrossProfitPercentage
-                                               Sales Order Line Gross Profit
percentage
iSalesOrderAccumulatedOrderQuantity
-                                               Accumulated Sales Order (lines)
quantity. Sum of all quantities in
order unit.
iSalesOrderAccumulatedOrderAmount
-                                               Accumulated Sales Order (lines) amount
in order currency
iRelation                                     - Relation by sales order line
iRelationType                                 - Relation Type: Employee/Supplier
/Customer
iRelationSequence                             - Relation sequence by order line
iRelationCurrencyForInvoicing
-                                               Relation Currency for Invoicing
Relation/Company/N.A./Sales Order
/Agreement
iRelationBuyFromBusinessPartner
-                                               Relation Buy-from BP, only applicable
in case the Relation type is
'Supplier'
iRelationSoldToBusinessPartner
-                                               Relation Buy-from BP, only applicable
in case the relation type is set to
'Customer'
Output: oCommissionRebateInvoiceCurrency
-                                               Commissions/Rebates Invoice Currency
based on invoice currency for relation
oCommissionRebatePercentage
-                                               Commissions/Rebates according
Commissions/Rebates Agreement Grades
oCommissionRebateGrowPercentage
-                                               Commissions/Rebates Grow Percentage
according Commissions/Rebates
Agreement Grades
oCommissionRebateGrowAmount
-                                               Commissions/Rebates Grow Amount based
on Commissions/Rebates Agreement
Grades Grow Percentage
oCommissionRebateFixedAmountInOrderCurrency
-                                               Commissions/Rebates Fixed Amount
according Commissions/Rebates
Agreement Grades
oCommissionRebateSalesOrderAmountInOrderCurrency
-                                               Sales Order (Line) Amount in sales
order line currency
oCommissionRebateAmountInOrderCurrency
-                                               Commissions/Rebates Amount in order
currency based on Commissions/Rebates
Agreement Grades Commission/Rebate
Percentage
oSkipCommissionRebateAgreement
-                                               True/False. Indicates that the
Commission/Rebate agreement grade is
not applicable to sales order (line)
oStopSearchIngAgreement                       - True/False. Indicates that all
agreement grade quantity/amounts have
been fit
ioInitializeStatics                           - True/False. Indicates that
variables used for determining
agreement grades need to be
initialized.
oExceptionMessage                             - The last message if any message is
found. If more than one  message is
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Evaluation of commission/rebate amount
was successfull
<> 0                    An error occurred
```
