# Pricing.GlobalUpdateOfPricesViaPriceBooks

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 501-503

```baan
DLL:   tdextpcgapi
This function is available from 2023.11 (KB2306213).
Syntax: long Pricing.GlobalUpdateOfPricesViaPriceBooks(
domain  tdpcg.mous       iFromPriceBookType,
domain  tdpcg.prbk       iFromPriceBook,
domain  tcccur           iFromCurrency,
domain  tccom.bpid       iFromBuyFromBp,
domain  tccom.bpid       iFromShipFromBp,
domain  tccuni           iFromQuantityUnit,
domain  tcqsl1           iFromBreakValue,
domain  tdpcg.prit       iFromPriceType,
domain  tcmpnr           iFromManufacturerPartNumber,
domain  tcmcs.cmnf       iFromManufacturer,
domain  tcefex.date      iFromEffectiveDate,
domain  tcefex.date      iFromExpiryDate,
domain  tcitem           iFromItem,
domain  tccitg           iFromItemGroup,
domain  tcctyp           iFromProductType,
domain  tcmcs.cpcl       iFromProductClass,
domain  tcmcs.cpln       iFromProductLine,
domain  tcmcs.cmnf       iFromItemManufacturer,
domain  tdpcg.mous       iToPriceBookType,
domain  tdpcg.prbk       iToPriceBook,
domain  tcccur           iToCurrency,
domain  tccom.bpid       iToBuyFromBp,
domain  tccom.bpid       iToShipFromBp,
domain  tccuni           iToQuantityUnit,
domain  tcqsl1           iToBreakValue,
domain  tdpcg.prit       iToPriceType,
domain  tcmpnr           iToManufacturerPartNumber,
domain  tcmcs.cmnf       iToManufacturer,
domain  tcefex.date      iToEffectiveDate,
domain  tcefex.date      iToExpiryDate,
domain  tcitem           iToItem,
domain  tccitg           iToItemGroup,
domain  tcctyp           iToProductType,
domain  tcmcs.cpcl       iToProductClass,
domain  tcmcs.cpln       iToProductLine,
domain  tcmcs.cmnf       iToItemManufacturer,
domain  tdpcg.ampe       iUpdatePriceBy,
domain  tcpric           iValueToChangeBy,
domain  tcdisc           iPercentageToChangeBy,
domain  tccrou           iRoundingCode,
domain  tcccur           iCurrency,
domain  tcefex.date      iNewEffectiveDate,
domain  tcefex.date      iNewExpiryDate,
ref             boolean          oPriceBookLineProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function updates the prices for a range of Price Books.
It is using the same logic and transaction handling as the
LN session 'Global Update of Prices via Price Books'
(tdpcg0231m000).
Pre:    LN Application sets retry-point, so not by caller
Post:   LN Application sets commit/abort transaction, so not by caller
Input:  iFromPriceBookType      - Selection field.
Mandatory to be filled.
iFromPriceBook          - Selection field.
iFromCurrency           - Selection field.
iFromBuyFromBp          - Selection field.
iFromShipFromBp         - Selection field.
iFromQuantityUnit       - Selection field.
iFromBreakValue         - Selection field.
iFromPriceType          - Selection field.
Mandatory to be filled.
iFromManufacturerPartNumber - Selection field.
iFromManufacturer       - Selection field.
iFromEffectiveDate      - Selection field.
iFromExpiryDate         - Selection field.
iFromItem               - Selection field.
iFromItemGroup          - Selection field.
iFromProductType        - Selection field.
iFromItemManufacturer   - Selection field.
iFromProductLine        - Selection field.
iFromProductClass       - Selection field.
iToPriceBookType        - Selection field.
Mandatory to be filled.
iToPriceBook            - Selection field.
iToCurrency             - Selection field.
iToBuyFromBp            - Selection field.
iToShipFromBp           - Selection field.
iToQuantityUnit         - Selection field.
iToBreakValue           - Selection field.
iToPriceType            - Selection field.
Mandatory to be filled.
iToManufacturerPartNumber - Selection field.
iToManufacturer         - Selection field.
iToEffectiveDate        - Selection field.
iToExpiryDate           - Selection field.
iToItem                 - Selection field.
iToItemGroup            - Selection field.
iToProductType          - Selection field.
iToItemManufacturer     - Selection field.
iToProductLine          - Selection field.
iToProductClass         - Selection field.
iUpdatePriceBy          - Update Price by Percentage or by
Value. Mandatory to be filled.
iValueToChangeBy        - Value with which the price book
price is to be updated. Expressed in
the Currency. Only to be filled in
case Update Price By is By Value.
iPercentageToChangeBy   - Percentage with which the price book
price is to be updated. Only to be
filled in case Update Price By is By
Percentage.
iRoundingCode           - Rounding Code used in case
Value To Change By is Percentage.
Only allowed to be filled in case
Update Price By is By Percentage.
iCurrency               - Currency in which the Value To
Change By is expressed. Only allowed
to be filled in case Update Price By
is By Value. Then it is mandatory.
iNewEffectiveDate       - Effective Date of the updated price.
iNewExpiryDate          - Expiry Date of the updated price.
Output: oPriceBookLineProcessed - At least one price book line is
processed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function executed successfully
<> 0                    - An error occurred
```
