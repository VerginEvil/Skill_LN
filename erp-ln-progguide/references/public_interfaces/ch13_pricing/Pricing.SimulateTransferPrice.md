# Pricing.SimulateTransferPrice

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 517-518

```baan
DLL:   tdextpcgapi
This function is available from     2024.03 (KB2319624  ).
Syntax: long Pricing.SimulateTransferPrice(
domain  tcncmp           iLogisticCompany,
domain  tcncmp           iFinancialCompany,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tcccur           iCurrency,
domain  tcitem           iItem,
domain  tccom.bpid       iInvoiceFromBusinessPartner,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tccwoc           iFinancialDepartment,
domain  tcsite           iSite,
domain  tcmpnr           iManufacturerPartNumber,
domain  tcmcs.cmnf       iManufacturer,
domain  tccprg           iPriceGroup,
domain  tcdate           iRateDate,
domain  tcrtyp           iRateType,
domain  tcqst1           iQuantity,
domain  tccuni           iQuantityUnit,
domain  tcconv           iQuantityUnitConversionFactor,
domain  tcyesno          iRepairPrice,
domain  tcyesno          iSubcontracted,
domain  tdpcg.prit       iPriceType,
domain  tcefex.date      iPriceDate,
ref     domain  tcpric           oPrice,
ref     domain  tccuni           oPriceUnit,
ref     domain  tcconv           oPriceUnitConversionFactor,
ref     domain  tcpcg.made       oMatrixDefinition,
ref     domain  tcpcg.prse       oMatrixSequence,
ref     domain  tdpcg.prbk       oPriceBook,
ref     domain  tdgen.porg       oPriceOrigin,
ref             boolean          oPriceRetrieved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface simulates transfer price retrieval. Price
retrieval is according to standard LN logic, searching through
the hierarchical price structure.
Pre:    NA
Post:   NA
Input:
|***************************************************************
|* Mandatory input arguments
|***************************************************************
iLogisticCompany                                      - Logictic Company
iFinancialCompany                                     - Financial Company
iBuyFromBusinessPartner                               - Buy-from Business Partner
iSoldToBusinessPartner                                - Sold-to Business Partner
iCurrency                                             - Currency
iItem                                                 - Item
iPriceType                                            - Price Type
iRepairPrice                                          - Repair Price
iSubcontracted                                        - Subcontracted
|***************************************************************
|* Optional input arguments; if not filled, defaults are
|* retrieved
|***************************************************************
iInvoiceFromBusinessPartner                           - Invoice-from Business Partner
iInvoiceToBusinessPartner                             - Invoice-to Business Partner
iFinancialDepartment                                  - Financial Department
iSite                                                 - Site
iManufacturerPartNumber                               - Manufacturer Part Number
iManufacturer                                         - Manufacturer
iPriceGroup                                           - Price group
iRateDate                                             - Rate Date; if zero, then Price
Date is used.
iRateType                                             - Exchange Rate Type
iQuantity                                             - Quantity
iQuantityUnit                                         - Quantity Unit
iQuantityUnitConversionFactor                         - Quantity Unit Conversion
Factor
iPriceDate                                            - Price Date; if zero, then
current date and time is used
Output:
|***************************************************************
|* Price Output
|***************************************************************
oPrice                                                - Price
oPriceUnit                                            - Price Unit
oPriceUnitConversionFactor                            - Price Unit Conversion Factor
oPriceMatrixDefinition                                - Price Matrix Definition
oPriceMatrixSequence                                  - Price Matrix Sequence
oPriceBook                                            - Price Book
oPriceOrigin                                          - Price Origin
oPriceRetrieved                                       - Price Retrieved
|***************************************************************
|* Technical Output
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
