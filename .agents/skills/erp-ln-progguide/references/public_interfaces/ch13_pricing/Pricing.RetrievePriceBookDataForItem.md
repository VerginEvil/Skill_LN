# Pricing.RetrievePriceBookDataForItem

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 503-507

```baan
DLL:   tdextpcgapi
This function is available from 2019.12 (KB2079838).
Syntax: long Pricing.RetrievePriceBookDataForItem(
domain  tdpcg.prbk       iPriceBook,
domain  tdpcg.prit       iPriceType,
domain  tcdate           iPriceDate,
domain  tcitem           iItem,
domain  tcmpnr           iManufacturerPartNumber,
domain  tcmcs.cmnf       iManufacturer,
domain  tcqsl1           iOrderQuantity,
domain  tccuni           iQuantityUnit,
domain  tcconv           iQuantityUnitConversionFactor,
domain  tdpcg.prpc       iPricePercentage,
domain  tccuni           iPriceUnit,
domain  tcccur           iOrderCurrency,
domain  tcccur           iHomeCurrency,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcyesno          iHighPrio,
domain  tdpcg.tyor       iTypeOfOrder,
domain  tccwoc           iOffice,
boolean          iIgnoreQuantityBreaks,
ref     domain  tdpcg.prbk       oPriceBook,
ref     domain  tcmcs.long       oPriceBookLine,
ref     domain  tdpcg.prit       oPriceType,
ref     domain  tcrefa           oReference mb,
ref     domain  tcrefa           oSource mb,
ref     domain  tcyesno          oUsedForQuotations,
ref     domain  tctrns.date      oEntryDate,
ref     domain  tcefex.date      oEffectiveDate,
ref     domain  tcefex.date      oExpiryDate,
ref     domain  tcitem           oItem,
ref     domain  tcmpnr           oManufacturerPartNumber,
ref     domain  tcmcs.cmnf       oManufacturer,
ref     domain  tdpcg.brty       oBreakType,
ref     domain  tcqsl1           oBreakQuantityValue,
ref     domain  tccuni           oQuantityUnit,
ref     domain  tdpcg.prpc       oPricePercentage,
ref     domain  tcpric           oPrice,
ref     domain  tccuni           oPriceUnit,
ref     domain  tcccur           oCurrency,
ref     domain  tcyesno          oBasePrice,
ref     domain  tcprsg           oPriceStage,
ref     domain  tcyesno          oUpdateOrderLinesWithPriceUnitFromPriceBook,
ref     domain  tcperc           oPercentage,
ref     domain  tdpcg.dssc       oDiscountSchedule,
ref     domain  tccom.bpid       oBuyFromBusinessPartner,
ref     domain  tccom.bpid       oShipFromBusinessPartner,
ref     domain  tcyesno          oHighPriority,
ref             boolean          oValidPriceFound,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This public interface searches the proper price book record for
the given input. If a price book record was found, its price data
is returned in the output variables.
The price book instances that are found during
searching will be rated according to the search
mechanism. The valid price book instance having the
highest rate will be applied.
When determining the rate, the following price-book fields are
considered. Fields that are mentioned first in this list will
contribute more to the rate than fields that are lower in the list.
1. Manufacturer Part Number and Manufacturer are filled.
2. Buy-from and ship-from Business Partner are filled.
3. Search on order currency, then on home currency,
then on any currency.
4. Search on order unit, then on base unit, then on
price unit.
Pre:    NA
Post:   NA
Input:  iPriceBook              - Price Book; Mandatory
iPriceType              - Price Type; indicates the procurement
- scenario:
- Buying
- Item Subcontracting
- Operation Subcontracting
- Service Subcontracting
- Not Applicable.
iPriceDate              - Date of the Order, Contract,
RFQ, etc.
iItem                   - Item; Mandatory
iManufacturerPartNumber
- Manufacturer Part Number
iManufacturer           - Manufacturer
iOrderQuantity          - Order Quantity
iQuantityUnit           - Order Quantity Unit
iQuantityUnitConversionFactor
- Conversion factor for the Order Quantity
Unit
iPricePercentage        - Indicates the kind of price book record
that is retrieved.
Price: A price book record is
retrieved for which the field
'Price / Percentage' (tdpcg031.perc)
has the value 'Price'.
Percentage:
A price book record is
retrieved for which the field
'Price / Percentage' (tdpcg031.perc)
has the value 'Percentage'.
iPriceUnit              - Price Unit
iOrderCurrency          - Order Currency
iHomeCurrency           - Home Currency
iBuyFromBusinessPartner
- Buy-from BP
iShipFromBusinessPartner
- Ship-from BP
iHighPrio               - High Priority (Yes/No)
Search for price record that have
the High Priority flag set to the
given value.
iTypeOfOrder            - Indicates the type of order for which
a price book record is searched.
Allowed values include (but not limited
to):
Sales Order
Sales Contract
Sales Quotation
Purchase Order
Purchase Contract
Request for Quotation
General (Sales)
General (Purchase)
iOffice                 - Office
iIgnorePriceBreaks      - True/False
Indicates if quantity breaks must be
ignored.
Output: Data found on the price-book record:
oPriceBook              - Price Book
oPriceBookLine          - Price Book Line
oPriceType              - Price Type; indicates the procurement
scenario:
- Buying
- Item Subcontracting
- Operation Subcontracting
- Service Subcontracting
- Not Applicable.
oReference              - Any informative description field used
to refer to, for example:
* The person or department with
authorization to perform a specific
task.
* The business partner's contact.
* The original invoice number.
oSource                 - The LN component in which the price is
created, or the means by which the price
is created.
oUsedForQuotations      - Yes/No
If this field is set to Yes, the
price book line is allocated to quotations.
oEntryDate              - The entry date of the price book line
oEffectiveDate          - The date and time from which the price
book is valid
oExpiryDate             - The expiry date and time of the price book.
If this field is not filled, the price
book is infinitely valid.
oItem                   - Item
oManufacturerPartNumber
- The manufacturer part number (MPN)
linked to the price book line.
oManufacturer           - The code of the manufacturer linked to
the price book line.
oBreakType              - An entity used to specify how breaks
between ranges of entities such as
distances, amounts, or ordered quantities
of items are defined. A break, in this
case, is the first or the last number
of a range. A break type has either of
the following values:
* Minimum: The break is the
lowest number of a range.
* Up To:   The break is the
highest number of a range.
oBreakQuantityValue     - The minimum or maximum order quantity
or value to which the price book applies.
oQuantityUnit           - Quantity Unit
oPricePercentage        - Defines, for a cost or service item,
whether you can enter a price or a percentage.
oPrice                  - Price
oPriceUnit              - Price Unit
oCurrency               - Currency
oBasePrice              - Yes/No
If this field is Yes, the default sales
or purchase price book from the Pricing
Parameters session is used to store the
item's prices and discounts.
oPriceStage             - Price Stage
oUpdateOrderLinesWithPriceUnitFromPriceBook
- Yes/No
If this field is Yes, and an order line
is entered, the price unit on the order
line is similar to the price book's Price Unit.
oPercentage             - The additional cost item's percentage,
based on which an additional cost amount
is calculated.
oDiscountSchedule       - Discount Schedule
oBuyFromBusinessPartner
- Buy From Business Partner
oShipFromBusinessPartner
- Ship From Business Partner
oHighPriority           - Yes/No
If this field is Yes, the price of the
buy-from business partner/ship-from
business partner/item combination has
priority over the prices stored under
the normal matrix priority structure.
oValidPriceFound        - Price book retrieved (True/False)
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function was executed successfull.
<> 0                    - An error occurred.
```
