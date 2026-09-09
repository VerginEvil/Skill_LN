# BRA.TaxForecast.Calculate

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for BRA.TaxForecast
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1931-1936

```baan
DLL:   btexttaxapi
This function is available from 2026.05 (KB3655446).
Syntax: long BRA.TaxForecast.Calculate(
domain  btncmp           iLogisticCompany,
domain  btmcs.tror       iTransactionOrigin,
long             iProcessingOptionSet,
ref             long             oTaxForecastJson,
ref     domain  btmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will calculate the tax forecast and save the
results in a JSON format.
JSON structure:
{
"transactionOrigin": enumerated,
"establishment": string,
"establishmentAddress": string,
"shipFromBusinessPartner": string,
"shipFromBusinessPartnerAddress": string,
"shipToBusinessPartner": string,
"shipToBusinessPartnerAddress": string,
"invoiceFromBusinessPartner": string,
"invoiceFromBusinessPartnerAddress": string,
"invoiceToBusinessPartner": string,
"invoiceToBusinessPartnerAddress": string,
"countryFrom": string,
"stateFrom": string,
"cityFrom": string,
"countryTo": string,
"stateTo": string,
"cityTo": string,
"fiscalDocumentTypeCode": string,
"receiptFiscalDocumentType": enumerated,
"invoicingFiscalDocumentType": enumerated,
"currency": string,
"UTCExecutionDate": string representation of the UTC in
ISO 8601 format.
"item": string,
"warehouse": string,
"itemQuantity": double,
"itemUnit": string,
"itemTotalPrice": double,
"freight": double,
"insurance": double,
"generalExpenses": double,
"customsExpenses": double,
"additionsDiscounts": double,
"paymentTerms": string,
"itemType": enumerated,
"itemGroup": string,
"itemFiscalData": string,
"itemUtilization": enumerated,
"goodsOrigin": enumerated,
"groupingCode": string,
"CFOP": string,
"NCM": string,
"CEST": string,
"taxGroupCode": string,
"projectCode": string,
"projectElement": string,
"projectActivity": string,
"projectExtension": string,
"projectCostComponent": string,
"goodsAmount": double,
"costPrice": double,
"taxDiscount": double,
"financialIncrease": double,
"totalAmount": double,
"numberOfTaxes": long,
"taxLines": [
{
"taxType": enumerated,
"taxCode": string,
"calculationBaseFormulaCode": string,
"fiscalBenefit": enumerated,
"taxBase": double,
"taxRate": double,
"taxAmount": double,
"taxAmountRecovery": double,
"amountIncidenceOnGoods": double,
"amountIncidenceOnTotal": double,
"reducedRate": double,
"taxDiscount": double,
"deferredAmount": double,
"reductionTaxBasePercentage": double,
"reductionTaxRatePercentage": double,
"reductionTaxAmountPercentage": double,
"recoveryAmountPercentage": double,
"profitMarginPercentage": double,
"adjustedProfitMarginPercentage": double,
"incidenceOnGoodsAmountPercentage": double,
"incidenceOnTotalAmountPercentage": double,
"taxDiscountPercentage": double,
"partitionPercentage": double,
"paymentOwner": enumerated,
"adjustedProfitMarginIndicator": enumerated,
"fiscalText": string,
}
This will repeat for the number of "taxLines".
]
}
This function is very flexible, allowing the user to use as many
optional arguments as possible. Therefore, the more optional
input arguments are provided, the more detailed the search will
be, and consequently the more accurate the results will be.
For this reason, use the optional arguments according to
availability.
To correctly determine taxes, the function needs to know the
origin and destination of the goods and, consequently, the
invoice. Therefore, the use of the optional arguments
"establishment" and "business partner" (from or to) is
recommended. If it is not possible to use them, the variables
for city, state, and country from/to can be used.
Note that when the "establishment" and "business partner" data
are used, they will have priority over the city, state, and
country variables. The city, state, and country variables
will only be used if the establishment and/or business partner
fields are empty.
The program will use the following hierarchy according to the
transaction origin:
If the transaction origin is inbound (btmcs.tror.input), this
means that the establishment is receiving the invoice.
The establishment will then be the "ship-to" and "invoice-to"
business partner. In this case, the user must provide the
"ship-from" and "invoice-from" data to inform the program of the
origin of the invoice.
If the transaction origin is outbound (btmcs.tror.output), this
means that the establishment is issuing the invoice. Then the
establishment will be the "ship-from" and "invoice-from"
business partner. In this case, the user must provide the
"ship-to" and "invoice-to" data to inform the program of the
destination of the invoice.
The item data is also important and should be used as several
tax parameters are determined from the item code. There are
types of Brazilian invoices which does not have an item. For
this reason, the item code and its data are optional.
Pre:    n.a.
Post:   This function won't set the tax forecast tables, all
the data will be set in the output JSON.
Other public interfaces can be called to get the values from the
tax forecast JSON.
Input:  iLogisticCompany        - Logistic company. This is a mandatory
argument.
iTransactionOrigin      - Transaction origin. This is a
mandatory argument.
iProcessingOptionSet    - Processing option have a direct
impact of the calculation results.
The more data is set, the more
accurate the calculation will be.
This is a mandatory field.
A processing option set can  be
created via a call to
ProcessingOptionSet.Create().
optional arguments:
paymentTerms            - Payment terms
establishment           - Establishment
fiscalDocumentTypeCode  - Fiscal document type code
shipFromBp              - Ship-from Business Partner
shipFromBpAddress       - Ship-from Business Partner Address
shipToBp                - Ship-to Business Partner
shipToBpAddress         - Ship-to Business Partner Address
invoiceFromBp           - Invoice-from Business Partner
invoiceFromBpAddress    - Invoice-from Business Partner Address
invoiceToBp             - Invoice-to Business Partner
invoiceToBpAddress      - Invoice-to Business Partner Address
countryFrom             - Country-from
stateFrom               - State-from
cityFrom                - City-from
countryTo               - Country-to
stateTo                 - State-to
cityTo                  - City-to
item                    - Item code
itemUnit                - Item unit
itemQuantity            - Item quantity
itemTotalPrice          - Total price of the item
goodsAmount             - Goods amount
totalAmount             - Total amount
freight                 - Freight
insurance               - Insurance
generalExpenses         - General expenses
customsExpenses         - Customs expenses
additionsDiscounts      - Additions/discounts
taxDiscount             - Tax discount
itemType                - Item type
itemGroup               - Item group
itemFiscalData          - Item fiscal data
warehouse               - Warehouse
itemUtilization         - Item utilization
goodsOrigin             - Goods origin
ncmFiscalClassification - NCM fiscal classification
cest                    - CEST
lineType                - Line type
project                 - Project code
element                 - Project element
activity                - Project activity
extension               - Project extension
projectCostComponent    - Project cost component
useInputItemData        - If "yes" the function will use
the item data from the optional
arguments. If "no" the function will
determine the item data from the item
table and will ignore the arguments:
* itemType
* itemGroup
* itemFiscalData
* itemUtilization
* goodsOrigin
* ncmFiscalClassification
* cest
useInputBpLocationData  - If "yes" the function will use
the business partner location data
from the optional arguments. If "no"
the function will determine the
location data from the business
partner table and will ignore the
arguments:
* countryFrom
* stateFrom
* cityFrom
* countryTo
* stateTo
* cityTo
NAME                            TYPE                    DEFAULT
paymentTerms                    domain  btcpay          ""
establishment                   domain  btcwoc          ""
fiscalDocumentTypeCode          domain  btmcs.fdtc      ""
shipFromBp                      domain  btcom.bpid      ""
shipFromBpAddress               domain  btcom.cadr      ""
shipToBp                        domain  btcom.bpid      ""
shipToBpAddress                 domain  btcom.cadr      ""
invoiceFromBp                   domain  btcom.bpid      ""
invoiceFromBpAddress            domain  btcom.cadr      ""
invoiceToBp                     domain  btcom.bpid      ""
invoiceToBpAddress              domain  btcom.cadr      ""
countryFrom                     domain  btccty          ""
stateFrom                       domain  btmcs.cste      ""
cityFrom                        domain  btcity          ""
countryTo                       domain  btccty          ""
stateTo                         domain  btmcs.cste      ""
cityTo                          domain  btcity          ""
item                            domain  btitem          ""
itemUnit                        domain  btcuni          ""
itemQuantity                    domain  btamtf          1.0
itemTotalPrice                  domain  btamtf          0.0
goodsAmount                     domain  btamtf          0.0
totalAmount                     domain  btamtf          0.0
freight                         domain  btamtf          0.0
insurance                       domain  btamtf          0.0
generalExpenses                 domain  btamtf          0.0
customsExpenses                 domain  btamtf          0.0
additionsDiscounts              domain  btamtf          0.0
taxDiscount                     domain  btamtf          0.0
itemType                        domain  btkitm          btkitm.product
itemGroup                       domain  btcitg          ""
itemFiscalData                  domain  btifgc          ""
warehouse                       domain  btcwar          ""
itemUtilization                 domain  btitmu          btitmu.not.appl
goodsOrigin                     domain  btsour          btsour.not.appl
ncmFiscalClassification         domain  btfrat          ""
cest                            domain  btcest          ""
lineType                        domain  btcom.tpln      btcom.tpln.standard
project                         domain  btcprj          ""
element                         domain  btpdm.cspa      ""
activity                        domain  btpdm.cact      ""
extension                       domain  btptc.cstl      ""
projectCostComponent            domain  tccpcp          ""
useInputItemData                domain  btyesno         btyesno.no
useInputBpLocationData          domain  btyesno         btyesno.no
Output: oTaxForecastJson        - JSON containing all the tax forecast
calculation details.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```
