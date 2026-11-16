# Tax.Calculate

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1635-1639

```baan
DLL:   tcexttaxapi
This function is available from 2020.12 (KB2155860).
Syntax: long Tax.Calculate(
domain  tcncmp           iFinancialCompany,
domain  tcccty           iTaxCountry,
domain  tccvat           iTaxCode,
domain  tcccur           iCurrency,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcficu           iFinancialBPGroup,
domain  tccwar           iWarehouse,
domain  tccwoc           iDepartment,
domain  tcmcs.st30m      iCustomerOrderReference mb,
domain  tccdec           iDeliveryTerms,
domain  tcptpa           iPointOfTitlePassage,
domain  tcfovn           iExemptCertificate,
domain  tccdis           iExemptReason,
domain  tctax.toam       iTypeOfAmount,
domain  tcamnt           iTaxableOrderLineAmount,
domain  tcamnt           iCustomsValue,
domain  tcdate           iOrderDate,
domain  tcdate           iInvoiceDate,
domain  tcdate           iDeliveryDate,
domain  tcdate           iTaxDate,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcinvn           iInvoiceNumber,
domain  tcmcs.long       iInvoiceLine,
boolean          iLastInvoiceLine,
domain  tcgld.ttyp       iTransactionType,
domain  tcqdhc           iOrderQuantity,
domain  tctxin           iSalesServiceRentalUsage,
domain  tcprel           iRelationType,
domain  tcitem           iItem,
domain  tccitg           iItemGroup,
domain  tclct.type       iLandedCostType,
domain  tccprj           iProject,
domain  tctano           iStandardLabor,
domain  tctano           iProjectLabor,
domain  tctax.cico       iStandardSundryCosts,
domain  tctax.cico       iProjectSundryCosts,
domain  tccom.sctp       iServiceCostType,
domain  tctax.ctpc       iContractType,
domain  tctax.cstp       iServiceType,
domain  tcgld.leac       iAccountNumber,
domain  tccom.cadr       iShipFromAddress,
domain  tccom.cadr       iShipToAddress,
domain  tccom.cadr       iAdminShipFromAddress,
domain  tccom.cadr       iAdminShipToAddress,
domain  tcyesno          iRoundTaxAmount,
domain  tcyesno          iUpdateTaxRegister,
boolean          iUseAmountEnteredInFinancials,
domain  tcyesno          iPerceptionTax,
ref     domain  tcamnt           oTotalTaxAmount,
ref     domain  tcpvat           oTotalTaxPercentage,
ref     domain  tcmcs.xml        oTaxCalcResultsNode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   This Public Interface calculates the tax amount of a logistic
or financial transaction.
Pre:    not applicable
Post:   not applicable
Input:
In the description below an indicator has been given for every
input field to make clear where it is used:
I : used in Internal Tax calculation
E : used in External Tax calculation
PT: used in Perception Tax (for Argentina) calculation
iFinancialCompany       - Financial Company
(I/E/PT (mandatory))
iTaxCountry             - Tax Country
(I/E/PT(mandatory))
iTaxCode                - Tax Code. In case of a Notax tax code,
an early return is done
(I/E(mandatory))
iCurrency               - Transaction Currency, the currency
in which the amount is expressed.
(I/PT (mandatory))
iInvoiceToBusinessPartner
- Invoice-to Business Partner
(PT)
iSoldToBusinessPartner  - Sold-to Business Partner
(I/E)
iBuyFromBusinessPartner - Buy-From BP; fill this field only in
case of Purchase Tax Origins.
(I/E)
iFinancialBPGroup       - Financial BP Group
(E)
iWarehouse              - Warehouse
(E)
iDepartment             - Department, fill this field only if the
Warehouse
is not available (e.g. Manual Sales Invoice)
(E)
iCustomerOrderReference - Customer Order Reference
(E)
iDeliveryTerms          - Delivery Terms
(E)
iPointOfTitlePassage    - Point of Title Passage
(E)
iExemptCertificate      - Exempt certificate
(I/E)
iExemptReason           - Exempt reason
(I/E)
iTypeOfAmount           - Specification of the characteristics
of variable 'iTaxableOrderLineAmount'.
* Gross: Amount includes tax
* Net: Amount is without tax; true for
calls from TD.
* Gross over Hundred
(I)
iTaxableOrderLineAmount
- Taxable amount, the order line amount
minus discounts (if applicable).
(I/E/PT)
iCustomsValue           - Customs Value
(I)
iOrderDate              - Order Date
(I)
iInvoiceDate            - Invoice Date
(I/PT)
iDeliveryDate           - Delivery Date
One of these dates is used for
determining the date for which the tax
rates apply.
If the invoice date is present, then
this date is used. Else, if the
delivery date is present, then this
date is used. Else the order date is
used.
(I)
iTaxDate                - Tax Date
(E/PT)
iOrderNumber            - Order Number
(E)
iOrderLine              - Order Line
(E)
iInvoiceNumber          - Invoice Number
(E)
iInvoiceLine            - Invoice Line
(E)
iLastInvoiceLine        - Indication if the current invoice line
is the last one of the invoices.
Only applicable if 'Update Tax
Register' is set to 'Yes'.
(E)
iTransactionType        - Transaction Type (currently not used)
(E)
iOrderQuantity          - Order Quantity
(E)
iSalesServiceRentalUsage
- Options are 'Sales', 'Service',
'Rental' or 'Purchase'
(E)
iRelationType           - Product Relation. The field determines
which of the following field must be
taken into account for determination
of the product category.
(E)
iItem                   - Item (for determining the product
category)
(E)
iItemGroup              - Item Group (for determining the
product category)
(E)
iLandedCostType         - Landed Cost Type (for determining the
product category)
(E)
iProject                - Project (for determining the product
category)
(E)
iStandardLabor          - Standard Labor (for determining the
product category)
(E)
iProjectLabor           - Project Labor (for determining the
product category)
(E)
iStandardSundryCosts    - Standard Sundry Costs (for determining
the product category)
(E)
iProjectSundryCosts     - Project Sundry Costs (for determining
the product category)
(E)
iServiceCostType        - Service Cost Type (for determining the
product category)
(E)
iContractType           - Contract Type (for determining the
product category)
(E)
iServiceType            - Service Type (for determining the
product category)
(E)
iAccountNumber          - Ledger Account (for determining the
product category)
(E)
iShipFromAddress        - Ship-from Address
(E)
iShipToAddress          - Ship-to Address
(E)
iAdminShipFromAddress   -Point of Acceptance Address. This is
the place where the business is
actually agreed / signed. Normally
this is the buy-from address.
(E)
iAdminShipToAddress     -Point of Order Origin. Normally this
is the sold-to address, but it might
differ due to the point of title
passage.
(E)
iRoundTaxAmount         - If 'Yes', then the output tax amount
is rounded.
If 'No', then the output tax amount is
not rounded
(I)
iUpdateTaxRegister      - If 'Yes' then the Vertex database is
updated with new rates.
If 'No' then the Vertex database is
only used for retrieval of rates.
(E)
iUseAmountEnteredInFinancials
- This value only applies to Financials.
Integrations from other packages will
have this field set to false.
If the value is set, then the gross/
net indicator of the tax code must be
used when calculating the tax amount.
(E)
iPerceptionTax          - If 'Yes', the tax calculation is done
for Perception Tax (in Argentina).
Perception Taxes are tax amounts that
are applied to documents at header
level. Therefore, the input variable
iTaxableOrderLineAmount must be
filled with the total net invoice
amount.
The Tax Result Node will contain the
Perception Tax Codes that are applied.
Mandatory input of this function:
- iFinancialCompany
- iTaxCountry
- iCurrency
- iInvoiceToBp
- iTypeOfAmount must be tctax.toam.net
- iTaxableOrderLineAmount
- iInvoiceDate
- iTaxDate
If 'No' the regular tax retrieval
applies.
(PT)
Output:
oTotalTaxAmount         - Total tax amount
oTotalTaxPercentage     - Total tax percentage
oTaxCalcResultsNode     - XML node which stores the calculation
details.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                         Succes
<> 0                      Error
```
