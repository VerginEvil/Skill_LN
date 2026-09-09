# CommissionsAndRebates.InsertCumulativeSales

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for CommissionsAndRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 384-386

```baan
DLL:   tdextcmsapi
This function is available from 2020.10 (KB2134632).
Syntax: long CommissionsAndRebates.InsertCumulativeSales(
domain  tdcms.type       iCommissionRebateType,
domain  tdcms.prty       iAgreementSearchPriority,
domain  tccom.bpid       iAgreementSoldToBusinessPartner,
domain  tccom.bpid       iAgreementRelation,
domain  tdcms.agrp       iAgreementGroup,
domain  tccprj           iAgreementProject,
domain  tcitem           iAgreementItem,
domain  tdcms.cmgp       iAgreementCommissionRebateGroup,
domain  tcccur           iAgreementCurrency,
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesSequence,
domain  tcpono           iSalesDeliverySequence,
domain  tcpono           iSalesInvoiceLine,
domain  tccwoc           iSalesOrderFinancialDepartment,
domain  tcccur           iSalesOrderCurrency,
domain  tdcms.stat       iRelationByStatus,
domain  tcpono           iRelationSequence,
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
Usage:        Expl.:
*** Warning ***
This public interface is deprecated and will be obsolete from
LN Cloud 2021.04 onwards; use:
CommissionsAndRebates.InsertCumulativeSalesV2
Function evaluates whether commissions rebates cumulative sales
should be added either by order or order line and inserts
cumulative sales lines.
This logic is executed after calculating commissions and
rebates for those cumulative agreements.
Pre:    Retry point must be set
Post:   Transaction must be committed or aborted.
Input:  iCommissionRebatetype   - Type Commission or Rebate
iAgreementsearchPriority
- Agreement search priority as defined
in Commissions and Rebates parameters
iAgreementSoldToBusinessPartner
- Agreement Sold-to Business Partner
iAgreementRelation      - Agreement Relation
iAgreementGroup         - Agreement Group
iAgreementProject       - Agreement Project
iAgreementItem          - Agreement Item
iAgreementCommissionRebateGroup
- Agreement Commission/Rebate Group
iAgreementCurrency      - Agreement Currency
iSalesOrder             - Sales Order
iSalesOrderLine         - Sales Order Line
iSalesOrderSequence     - Sales Sequence Number, it is 0 in case
the Commission/Rebate Parameter
'Linking of Relations On' is set to
Sales Order
iSalesOrderDeliverySequence
- Sales Order Delivery Sequence Line
iSalesOrderInvoiceLine  - Sales Order Invoice Line
iSalesOrderFinancialDepartment
- Sales Order Line Financial Department
iSalesOrderCurrency     - Sales Order Currency
iRelationByStatus       - The status of the relation linked to
sales order (line)
iRelationSequence       - Relation sequence by order line
iRelationCurrencyForInvoicing
- Relation Currency for Invoicing
iRelationType           - Relation Type: Employee/Supplier/
Customer
iRelationBuyFromBusinessPartner
- Relation Buy-from BP, only applicable
in case the relation type is
'Supplier'
iRelationSoldToBusinessPartner
- Relation Buy-from BP, only applicable
in case the relation type is
'Customer'
iRelationPeriodTable    - Relation Period Table
iSearchDate             - Search date based on Commissions/
Rebates parameter 'Search for
Commission Based on Date'
iFullUpdate             - Yes/No. Indicate if previous
calculated Cumulative Commissions and
Rebates need to be removed and
calculated again
Output: oCumulativeSalesAdded   - True/False. Indicates that Cumulative
Sales Commission/Rebate line has been
inserted.
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
<> 0                    An error occurred
```
