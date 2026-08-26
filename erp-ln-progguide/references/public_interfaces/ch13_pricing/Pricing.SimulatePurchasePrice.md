# Pricing.SimulatePurchasePrice

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 505-508

```baan
DLL:   tdextpcgapi
This function is available from     2019.04 (KB2042557  ).
Syntax: long Pricing.SimulatePurchasePrice(
domain  tcncmp           iLogisticCompany,
domain  tcncmp           iFinancialCompany,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcccur           iCurrency,
domain  tcitem           iItem,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tccom.bpid       iInvoiceFromBusinessPartner,
domain  tccom.bpid       iPricingBusinessPartner,
domain  tccwoc           iPurchaseOffice,
domain  tcrtyp           iRateType,
domain  tcdate           iRateDate,
const   domain  tcratc           iRate(),
const   domain  tcratf           iRateFactor(),
domain  tccplt           iPriceList,
domain  tccotp           iOrderType,
domain  tccreg           iArea,
domain  tccdec           iDeliveryTerms,
domain  tcpaym           iPaymentMethod,
domain  tcolid           iOptionListID,
domain  tccpva           iProductVariant,
domain  tcuef.effn       iEffectivityUnit,
domain  tcguid           iSpecification,
domain  tcmpnr           iManufacturerPartNumber,
domain  tcmcs.cmnf       iManufacturer,
domain  tcyesno          iSubcontracted,
domain  tcsite           iSite,
domain  tcefex.date      iPriceDate,
domain  tdpcg.prit       iPriceType,
domain  tcqsl1           iOrderQuantity,
domain  tccuni           iOrderQuantityUnit,
domain  tcconv           iOrderQuantityUnitConversionFactor,
domain  tccono           iContract,
domain  tcpono           iContractLine,
domain  tccwoc           iContractOffice,
domain  tcpono           iContractSequence,
ref     domain  tcpric           oPrice,
ref     domain  tccuni           oPriceUnit,
ref     domain  tcconv           oPriceUnitConversionFactor,
ref             boolean          oDerivedItemUsed,
ref     domain  tdpcg.prbk       oPriceBook,
ref     domain  tcprsg           oPriceStage,
ref     domain  tdgen.porg       oPriceOrigin,
ref     domain  tdpcg.made       oPriceMatrixDefinition,
ref     domain  tdpcg.prse       oPriceMatrixSequence,
ref     domain  tdpcg.maty       oDiscountMatrixType(),
ref     domain  tdgen.dorg       oDiscountOrigin(),
ref     domain  tdpcg.made       oDiscountMatrixDefinition() fixed,
ref     domain  tdpcg.prse       oDiscountMatrixSequence(),
ref     domain  tcdisc           oDiscountPercentage(),
ref     domain  tddiam           oDiscountAmount(),
ref     domain  tccdsc           oDiscountCode() fixed,
ref     domain  tddmth           oDiscountMethod(),
ref     domain  tdpcg.dssc       oDiscountSchedule() fixed,
ref     domain  tccono           oContract,
ref     domain  tcpono           oContractLine,
ref     domain  tccwoc           oContractOffice,
ref     domain  tcpono           oContractSequence,
ref     domain  tcmpr.pagr       oMaterialPriceAgreement,
ref     domain  tcprip           oTotalMaterialPriceSurcharges,
ref     domain  tcprip           oTotalMaterialPrice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface simulates purchase price and discounts
retrieval, including material price surcharge information.
Price and discount retrieval is according to standard LN logic,
searching through the hierarchical price structure. The output
indicates from which level the information is retrieved.
Pre:    NA
Post:   NA
Input:
|***************************************************************
|* Mandatory input arguments.
|***************************************************************
iLogisticCompany                                      - Logictic Company
iFinancialCompany                                     - Financial Company
iBuyFromBusinessPartner                               - Buy-from Business Partner
iCurrency                                             - Currency
iItem                                                 - Item
|***************************************************************
|* Optional input arguments; if not filled, defaults are
|* retrieved.
|***************************************************************
iShipFromBusinessPartner                              - Ship-from Business Partner
iInvoiceFromBusinessPartner                           - Invoice-from Business Partner
iPricingBusinessPartner                               - Pricing Business Partner
iPurchaseOffice                                       - Purchase Office
iRateType                                             - Exchange Rate Type
iRateDate                                             - Rate Date; if zero, then Price
Date is used.
iRate                                                 - Rate; if first element zero,
rate and rate factor are
defaulted.
iRateFactor                                           - Rate Factor; if first element
is zero, rate and rate factor
are defaulted.
iPriceList                                            - Price List
iOrderType                                            - Order Type
iArea                                                 - Area
iDeliveryTerms                                        - Delivery Terms
iPaymentMethod                                        - Payment Method
iOptionListID                                         - Option List ID
iProductVariant                                       - Product Variant
iEffectivityUnit                                      - Effectivity Unit
iSpecification                                        - Specification
iManufacturerPartNumber                               - ManufacturerPartNumber
iManufacturer                                         - Manufacturer
iSubcontracted                                        - Subcontracted; if empty, 'no'
is used
iSite                                                 - Site
iPriceDate                                            - Price Date; of zero, then
current date and time is used.
iPriceType                                            - Price Type; if empty, 'buying'
is used
iOrderQuantity                                        - Order Quantity
iOrderQuantityUnit                                    - Order Quantity Unit
iOrderQuantityUnitConversionFactor
-                                                       Order Quantity Unit Conversion
Factor
iContract                                             - Contract; if not filled,
Contract, Contract Line and
Contract Office are defaulted
(if applicable) without user
interaction.
iContractLine                                         - Contract Line; see Contract
iContractOffice                                       - Contract Office; see Contract
iContractSequence                                     - Contract Sequence
Output:
|***************************************************************
|* Price Output.
|***************************************************************
oPrice                                                - Price
oPriceUnit                                            - Price Unit
oPriceUnitConversionFactor                            - Price Unit Conversion Factor
oDerivedItemUsed                                      - Derived Item Used
oPriceBook                                            - Price Book
oPriceStage                                           - Price Stage
oPriceOrigin                                          - Price Origin
oPriceMatrixDefinition                                - Price Matrix Definition
oPriceMatrixSequence                                  - Price Matrix Sequence
|***************************************************************
|* Discount Output; memory allocation (11 levels) for arrays
|* needed.
|***************************************************************
oDiscountMatrixType                                   - Discount Matrix Type (array)
oDiscountOrigin                                       - Discount Origin (array)
oDiscountMatrixDefinition                             - Discount Matrix Definition
(array)
oDiscountMatrixSequence                               - Discount Matrix Sequence
(array)
oDiscountPercentage                                   - Discount Percentage (array)
oDiscountAmount                                       - Discount Amount (array)
oDiscountCode                                         - Discount Code (array)
oDiscountMethod                                       - Discount Method (array)
oDiscountSchedule                                     - Discount Schedule (array)
|***************************************************************
|* Contract Output.
|***************************************************************
oContract                                             - Contract; filled if price /
discount origin is 'contract'
oContractLine                                         - Contract Line; see Contract
oContractOffice                                       - Contract Office; see Contract
|***************************************************************
|* Material Price Output.
|***************************************************************
oMaterialPriceAgreement                               - Material Price Agreement
oTotalMaterialPriceSurcharges                         - Material Price Surcharges
oTotalMaterialPrice                                   - Total Material Price
|***************************************************************
|* Technical Output.
|***************************************************************
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - Price could be determined.
<> 0                                                  - Error occurred.
```
