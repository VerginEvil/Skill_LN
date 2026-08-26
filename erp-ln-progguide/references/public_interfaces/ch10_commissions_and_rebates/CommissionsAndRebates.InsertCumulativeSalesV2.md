# CommissionsAndRebates.InsertCumulativeSalesV2

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for CommissionsAndRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 384-387

```baan
DLL:   tdextcmsapi
This function is available from     2021.03 (KB2168763  ).
Syntax: long CommissionsAndRebates.InsertCumulativeSalesV2(
domain  tdcms.type       iCommissionRebateType,
domain  tdcms.prty       iAgreementSearchPriority,
domain  tccom.bpid       iAgreementSoldToBusinessPartner,
domain  tccom.bpid       iAgreementRelation,
domain  tdcms.agrp       iAgreementGroup,
domain  tccprj           iAgreementProject,
domain  tcitem           iAgreementItem,
domain  tdcms.cmgp       iAgreementCommissionRebateGroup,
domain  tcccur           iAgreementCurrency,
domain  tcdate           iAgreementEffectiveDate,
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesSequence,
domain  tcpono           iSalesDeliverySequence,
domain  tcpono           iSalesInvoiceLine,
domain  tccwoc           iSalesOffice,
domain  tccwoc           iSalesOrderFinancialDepartment,
domain  tcccur           iSalesOrderCurrency,
ref     domain  tcratc           iSalesOrderCurrencyRate(),
ref     domain  tcratf           iSalesOrderCurrencyRateFactor(),
domain  tcdate           iSalesOrderCurrencyRateDate,
domain  tcrtyp           iSalesOrderCurrencyRateType,
domain  tdcms.stat       iRelationByStatus,
domain  tcpono           iRelationSequence,
domain  tdcms.cmcm       iRelationCalculationMethod,
domain  tdcms.ruci       iRelationRateUsedForCalculating,
domain  tdcms.exrt       iRelationRateType,
domain  tcrtyp           iRelationRateTypeUsed,
domain  tdcms.cupf       iRelationCurrencyForInvoicing,
domain  tdcms.rtyp       iRelationType,
domain  tccom.bpid       iRelationBuyFromBusinessPartner,
domain  tccom.bpid       iRelationSoldToBusinessPartner,
domain  tcccp.cpdt       iRelationPeriodTable,
domain  tcdate           iSearchDate,
domain  tcyesno          iFullUpdate,
ref             boolean          oCumulativeSalesAdded,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function evaluates whether commissions rebates cumulative sales
should be added either by order or order line and inserts
cumulative sales lines.
This logic is executed after calculating commissions and
rebates for those cumulative agreements.
Pre:    Retry point must be set
Post:   Transaction must be committed or aborted.
Input:  iCommissionRebatetype                 - Type Commission or Rebate (Mandatory)
iAgreementsearchPriority
-                                               Agreement search priority as defined
in Commissions and Rebates parameters
(Mandatory)
iAgreementSoldToBusinessPartner
-                                               Agreement Sold-to Business Partner
iAgreementRelation                            - Agreement Relation
iAgreementGroup                               - Agreement Group
iAgreementProject                             - Agreement Project
iAgreementItem                                - Agreement Item
iAgreementCommissionRebateGroup
-                                               Agreement Commission/Rebate Group
iAgreementCurrency                            - Agreement Currency
iAgreementEffectiveDate                       - Agreement Effective Date
iSalesOrder                                   - Sales Order (Mandatory)
iSalesOrderLine                               - Sales Order Line
iSalesOrderSequence                           - Sales Sequence Number, it is 0 in case
the Commission/Rebate Parameter
'Linking of Relations On' is set to
Sales Order
iSalesOrderDeliverySequence
-                                               Sales Order Delivery Sequence Line
iSalesOrderInvoiceLine                        - Sales Order Invoice Line
iSalesOffice                                  - Sales Order Sales Office
iSalesOrderFinancialDepartment
-                                               Sales Order Line Financial Department
iSalesOrderCurrency                           - Sales Order Currency
iSalesOrderCurrencyRate                       - Sales Order Currency Rate
iSalesOrderCurrencyRateFactor
-                                               Sales Order Currency Rate Factor
iSalesOrderCurrencyRateDate
-                                               Sales Order Currency Rate Date
iSalesOrderCurrencyRateType
-                                               Sales Order Currency Rate Type
iRelationByStatus                             - The status of the relation linked to
sales order (line)
iRelationSequence                             - Relation sequence by order line
iRelationCalculationMethod
-                                               Relation Calculation Method
-                                                 Order
-                                                 Invoice
-                                                 Paid Sales Invoice
iRelationRateUsedForCalculating
-                                               Relation Rate used for
Calculating/Invoicing
-                                                 Sales Order Date
-                                                 Sales Invoice Rate
-                                                 Sales Invoice Date
-                                                 Calculation Date
iRelationRateType                             - Relation Rate Type
-                                                 Sales Order
-                                                 Commissions/Rebates Parameter
-                                                 User Defined
-                                                 Not Applicable
iRelationRateTypeUsed                         - Relation Rate Type Used
iRelationCurrencyForInvoicing
-                                               Relation Currency for Invoicing
iRelationType                                 - Relation Type: Employee/Supplier/
Customer
iRelationBuyFromBusinessPartner
-                                               Relation Buy-from BP, only applicable
in case the relation type is
'Supplier'
iRelationSoldToBusinessPartner
-                                               Relation Buy-from BP, only applicable
in case the relation type is
'Customer'
iRelationPeriodTable                          - Relation Period Table (Mandatory)
iSearchDate                                   - Search date based on Commissions/
Rebates parameter 'Search for
Commission Based on Date'
(Mandatory)
iFullUpdate                                   - Yes/No. Yes: Indicates if previous
calculated Cumulative Commissions and
Rebates needs to be removed and
calculated again (Mandatory)
Output: oCumulativeSalesAdded                 - True/False. Indicates that Cumulative
Sales Commission/Rebate line has been
inserted.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Insert of commission/rebate amount
was successfull
<> 0                    An error occurred
```

## Public Interfaces for Rebate

The following functions are available: Rebates.StartOverview
