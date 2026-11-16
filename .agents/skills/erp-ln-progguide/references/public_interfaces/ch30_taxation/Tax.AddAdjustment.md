# Tax.AddAdjustment

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1632-1635

```baan
DLL:   tcexttaxapi
This function is available from 2025.04 (KB3557291).
Syntax: long Tax.AddAdjustment(
domain  tcncmp           iFinancialCompany,
domain  tcinvn           iInvoiceNumber,
domain  tcmcs.long       iInvoiceLine,
domain  tcgld.ttyp       iTransactionType,
domain  tcdate           iInvoiceDate,
domain  tcmcs.long       iNumberOfItems,
domain  tccom.bpid       iBusinessPartner,
domain  tcficu           iFinancialBusinessPartnerGroup,
domain  tccwoc           iWarehouseOrOffice,
domain  tcmcs.st30m      iCustomerOrderReference mb,
domain  tccdec           iDeliveryTerms,
domain  tcptpa           iPointOfTitlePassage,
domain  tctxin           iSalesServiceRentalUsage,
domain  tcpcat           iProduct,
domain  tcpcat           iProductClass,
domain  tcccty           iShipFromCountry,
domain  tcpstc           iShipFromZipCode mb,
domain  tccadr.namc      iShipFromStreet mb,
domain  tcmcs.cste       iShipFromState,
domain  tccadr.name      iShipFromCounty mb,
domain  tcdsca           iShipFromCityName mb,
domain  tcgeoc           iShipFromGeoCode,
domain  tcglat           iShipFromLatitude,
domain  tcglon           iShipFromLongitude,
domain  tcict2           iShipFromIsoCode2,
domain  tcccty           iShipToCountry,
domain  tcpstc           iShipToZipCode mb,
domain  tccadr.namc      iShipToStreet mb,
domain  tcmcs.cste       iShipToState,
domain  tccadr.name      iShipToCounty mb,
domain  tcdsca           iShipToCityName mb,
domain  tcgeoc           iShipToGeoCode,
domain  tcglat           iShipToLatitude,
domain  tcglon           iShipToLongitude,
domain  tcict2           iShipToIsoCode2,
domain  tcccty           iAdminShipFromCountry,
domain  tcpstc           iAdminShipFromZipCode mb,
domain  tccadr.namc      iAdminShipFromStreet mb,
domain  tcmcs.cste       iAdminShipFromState,
domain  tccadr.name      iAdminShipFromCounty mb,
domain  tcdsca           iAdminShipFromCityName mb,
domain  tcgeoc           iAdminShipFromGeoCode,
domain  tcglat           iAdminShipFromLatitude,
domain  tcglon           iAdminShipFromLongitude,
domain  tcict2           iAdminShipFromIsoCode2,
domain  tcccty           iAdminShipToCountry,
domain  tcpstc           iAdminShipToZipCode mb,
domain  tccadr.namc      iAdminShipToStreet mb,
domain  tcmcs.cste       iAdminShipToState,
domain  tccadr.name      iAdminShipToCounty mb,
domain  tcdsca           iAdminShipToCityName mb,
domain  tcgeoc           iAdminShipToGeoCode,
domain  tcglat           iAdminShipToLatitude,
domain  tcglon           iAdminShipToLongitude,
domain  tcict2           iAdminShipToIsoCode2,
domain  tcfovn           iExemptCertificate,
domain  tccdis           iExemptReason,
domain  tcccur           iCurrency,
domain  tcamnt           iTaxableAmount,
boolean          iTaxIncluded,
domain  tcmcs.str100     iAdjustmentReason,
domain  tcamnt           iTaxAmountToAdjust,
ref     domain  tcamnt           oTaxCountryAmount,
ref     domain  tcamnt           oTaxStateAmount,
ref     domain  tcamnt           oTaxCountyAmount,
ref     domain  tcamnt           oTaxCityAmount,
ref     domain  tcamnt           oTaxDistrictAmount,
ref     domain  tcpvat           oTaxCountryPercentage,
ref     domain  tcpvat           oTaxStatePercentage,
ref     domain  tcpvat           oTaxCountyPercentage,
ref     domain  tcpvat           oTaxCityPercentage,
ref     domain  tcpvat           oTaxDistrictPercentage,
ref     domain  tcamnt           oTaxAmount,
ref     domain  tcpvat           oTaxPercentage,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Process a tax-only credit or debit to reconcile an underpayment
or overpayment of tax, by means of an external tax provider.
Pre:    na
Post:   na
Input:  iFinancialCompany       - Financial Company (mandatory)
iInvoiceNumber          - Invoice Number
iInvoiceLine            - Invoice Line
iTransactionType        - Transaction Type
iInvoiceDate            - Invoice Date
iNumberOfItems          - Number Of Items
iBusinessPartner        - Business Partner
iFinancialBusinessPartnerGroup
- Financial Business Partner Group
iWarehouseOrOffice      - Warehouse Or Office
iCustomerOrderReference - Customer Order Reference
iDeliveryTerms          - Delivery Terms
iPointOfTitlePassage    - Point Of Title Passage
iSalesServiceRentalUsage- Sales Service Rental Usage
iProduct                - Product
iProductClass           - Product Class
iShipFromCountry        - Ship From Country
iShipFromZipCode        - Ship From Zip Code
iShipFromStreet         - Ship From Street
iShipFromState          - Ship From State
iShipFromCounty         - Ship From County
iShipFromCityName       - Ship From City Name
iShipFromGeoCode        - Ship From Geo Code
iShipFromLatitude       - Ship From Latitude
iShipFromLongitude      - Ship From Longitude
iShipFromIsoCode2       - Ship From Iso Code2
iShipToCountry          - Ship To Country
iShipToZipCode          - Ship To Zip Code
iShipToStreet           - Ship To Street
iShipToState            - Ship To State
iShipToCounty           - Ship To County
iShipToCityName         - Ship To City Name
iShipToGeoCode          - Ship To Geo Code
iShipToLatitude         - Ship To Latitude
iShipToLongitude        - Ship To Longitude
iShipToIsoCode2         - Ship To Iso Code2
iAdminShipFromCountry   - Admin Ship From Country
iAdminShipFromZipCode   - Admin Ship From Zip Code
iAdminShipFromStreet    - Admin Ship From Street
iAdminShipFromState     - Admin Ship From State
iAdminShipFromCounty    - Admin Ship From County
iAdminShipFromCityName  - Admin Ship From City Name
iAdminShipFromGeoCode   - Admin Ship From Geo Code
iAdminShipFromLatitude  - Admin Ship From Latitude
iAdminShipFromLongitude - Admin Ship From Longitude
iAdminShipFromIsoCode2  - Admin Ship From Iso Code2
iAdminShipToCountry     - Admin Ship To Country
iAdminShipToZipCode     - Admin Ship To Zip Code
iAdminShipToStreet      - Admin Ship To Street
iAdminShipToState       - Admin Ship To State
iAdminShipToCounty      - Admin Ship To County
iAdminShipToCityName    - Admin Ship To City Name
iAdminShipToGeoCode     - Admin Ship To Geo Code
iAdminShipToLatitude    - Admin Ship To Latitude
iAdminShipToLongitude   - Admin Ship To Longitude
iAdminShipToIsoCode2    - Admin Ship To Iso Code2
iExemptCertificate      - Exempt Certificate
iExemptReason           - Exempt Reason
iCurrency               - Currency
iTaxableAmount          - Taxable Amount
iTaxIncluded            - Tax Included
iAdjustmentReason       - Adjustment Reason
iTaxAmountToAdjust      - Tax Amount To Adjust
Output: oTaxCountryAmount       - Tax Country Amount
oTaxStateAmount         - Tax State Amount
oTaxCountyAmount        - Tax County Amount
oTaxCityAmount          - Tax City Amount
oTaxDistrictAmount      - Tax District Amount
oTaxCountryPercentage   - Tax Country Percentage
oTaxStatePercentage     - Tax State Percentage
oTaxCountyPercentage    - Tax County Percentage
oTaxCityPercentage      - Tax City Percentage
oTaxDistrictPercentage  - Tax District Percentage
oTaxAmount              - Tax Amount
oTaxPercentage          - Tax Percentage
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - succes
<> 0                    - otherwise
```
