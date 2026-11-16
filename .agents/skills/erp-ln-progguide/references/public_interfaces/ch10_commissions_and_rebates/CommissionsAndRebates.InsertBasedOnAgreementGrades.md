# CommissionsAndRebates.InsertBasedOnAgreementGrades

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for CommissionsAndRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 382-384

```baan
DLL:   tdextcmsapi
This function is available from 2020.10 (KB2134632).
Syntax: long CommissionsAndRebates.InsertBasedOnAgreementGrades(
domain  tdcms.type       iCommissionRebateType,
domain  tdcms.prty       iAgreementSearchPriority,
domain  tdcms.pyrs       iAgreementInvoiceDirectReserve,
domain  tccdsc           iAgreementDiscountCode,
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcpono           iSalesOrderDeliverySequence,
domain  tcpono           iSalesOrderInvoiceLine,
domain  tcttyp           iSalesOrderTransactionType,
domain  tcinvn           iSalesOrderInvoiceNumber,
domain  tcdate           iSalesOrderInvoiceDate,
domain  tccwoc           iSalesOrderOffice,
domain  tccwoc           iSalesOrderFinancialDepartment,
domain  tcccur           iSalesOrderCurrency,
domain  tcdate           iSalesOrderRateDate,
domain  tcrtyp           iSalesOrderRateType,
ref     domain  tcratc           iSalesOrderRate(),
ref     domain  tcratf           iSalesOrderRateFactor(),
domain  tccom.bpid       iRelation,
domain  tdcms.rtyp       iRelationType,
domain  tcpono           iRelationSequence,
domain  tdcms.cmpr       iCommissionRebatePercentage,
domain  tdcms.cmpr       iCommissionRebateGrowPercentage,
domain  tcamnt           iCommissionRebateGrowAmount,
domain  tcamnt           iCommissionRebateFixedAmountInOrderCurrency,
domain  tcamnt           iCommissionRebateSalesOrderAmountInOrderCurrency,
domain  tcamnt           iCommissionRebateAmountInOrderCurrency,
domain  tcccur           iCommissionRebateInvoiceCurrency,
ref             boolean          oCommissionRebateAdded,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function generates a commission/rebate line for
commissions/rebates which are calculated for a sales order
(line) based on Agreement Grades
Before adding new commission/rebate lines, a counter posting is
created for existing commission/rebate commissions/rebates that
are already processed.
Pre:    Retry point must be set
Post:   Transaction must be committed or aborted.
Input:  iCommissionRebateType   - Type Commission or Rebate
iAgreementSearchPriority
- Agreement search priority as defined
in Commissions and Rebates parameters
iAgreementInvoiceDirectReserve
- Agreement Invoice/Reserve
iAgreementDiscountCode  - Agreement Discount Code
iSalesOrder             - Sales Order
iSalesOrderLine         - Sales Order Line
iSalesOrderSequence     - Sales Sequence Number, it is 0 in case
the Commission/Rebate Parameter
'Linking of Relations On' is set to
Sales Order
iSalesOrderDeliverySequence
- Sales Order Delivery Sequence Line
iSalesOrderInvoiceLine  - Sales Order Invoice Line
iSalesOrderTransactionType
- Sales Order Line Transaction Type
iSalesOrderInvoiceNumber
- Sales Order Line Invoice Number
iSalesOrderInvoiceDate  - Sales Order Line Invoice Date
iSalesOrderOffice       - Sales Order Line Sales Office
iSalesOrderFinancialDepartment
- Sales Order Line Financial Department
iSalesOrderCurrency     - Sales Order Currency
iSalesOrderRatedate     - Sales Order Line Rate Date
iSalesOrderRatetype     - Sales Order Line Rate Type
iSalesOrderRate         - Sales Order Line Rate
iSalesOrderRateFactor   - Sales Order Line Rate Factor
iRelation               - Relation by sales order line
iRelationType           - Relation Type: Employee/Supplier
/Customer
iRelationSequence       - Relation sequence by order line
iCommissionRebatePercentage
- Commissions/Rebates according
Commissions/Rebates Agreement Grades
iCommissionRebateGrowPercentage
- Commissions/Rebates Grow Percentage
according Commissions/Rebates
Agreement Grades
iCommissionRebateGrowAmount
- Commissions/Rebates Grow Amount based
on Commissions/Rebates Agreement
Grades Grow Percentage
iCommissionRebateFixedAmountInOrderCurrency
- Commissions/Rebates Fixed Amount
according Commissions/Rebates
Agreement Grades
iCommissionRebateSalesOrderAmountInOrderCurrency
- Sales Order (Line) Amount in sales
order line currency
iCommissionRebateAmountInOrderCurrency
- Commissions/Rebates Amount in order
currency based on Commissions/Rebates
Agreement Grades Commission/Rebate
Percentage
iCommissionRebateInvoiceCurrency
- Commissions/Rebates Invoice Currency
based on invoice currency for relation
Output: oCommissionRebateAdded  - True/False. Indicates that Commission/
Rebate line has been inserted
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Insert of commission/rebate amount
was successfull
<> 0                    An error occurred.
```
