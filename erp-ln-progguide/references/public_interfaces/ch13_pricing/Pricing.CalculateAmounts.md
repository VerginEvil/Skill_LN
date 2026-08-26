# Pricing.CalculateAmounts

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 490-494

```baan
DLL:   tdextpcgapi
This function is available from     2021.09 (KB2204530  ).
Syntax: long Pricing.CalculateAmounts(
domain  tdpcg.tyor       iTypeOfOrder,
domain  tcitem           iItem,
domain  tcmpnr           iManufacturerPartNumber,
domain  tcmcs.cmnf       iManufacturer,
domain  tcqsl1           iQuantity,
domain  tccuni           iQuantityUnit,
domain  tcconv           iQuantityUnitConversionFactor,
domain  tcpric           iPrice,
domain  tccuni           iPriceUnit,
domain  tcconv           iPriceUnitConversionFactor,
domain  tdpcg.prbk       iPriceBook,
domain  tcccur           iTransactionCurrency,
domain  tccrnd           iRoundingMethod,
const   domain  tcdisc           iDiscountPercentage(),
const   domain  tddiam           iDiscountAmount(),
const   domain  tddmth           iDiscountMethod(),
const   domain  tdgen.dorg       iDiscountOrigin(),
const   domain  tdpcg.dssc       iDiscountSchedule() fixed,
domain  tcdate           iPriceDate,
domain  tccwoc           iOffice,
boolean          iRoundAmounts,
ref     domain  tcamnt           oNetAmount,
ref     domain  tcamnt           oGrossAmount,
ref     domain  tcamnt           oTotalDiscountAmount,
ref     domain  tcdisc           oStructureDiscountPercentage,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface calculates the Net Amount, Gross Amount,
the Discount Amount, and the Structure Discount Percentage.
Definitions:
1) Structure Discount Amount is the sum of all Discount Amounts
that are not Manual.
2) Total discount Amount is the sum of all Discount Amounts.
Calculations:
1) Gross Amount = Quantity (in inv.unit) x Price (in inv.unit)
2) Total Discount Amount is based upon the Discount Arrays
3) Net Amount = Gross Amount                       - Total Discount Amount
4) Structure Discount Percentage =
Structure Discount Amount / Gross Amount x 100%
In case the Type of Order is Purchase Contract (tdpcg.tyor.pc),
Sales Contract (tdpcg.tyor.sc) or Request for Quotation
(tdpcg.tyor.pq), then it is possible to retrieve the Price from
the Contract/RFQ Price Book and the Discounts from the Contract/
RFQ Discount Schedules. In that case no Price and Discounts must
be passed along. This is illustrated in the tables below.
legend:
'x' means: mandatory
'                              -' means: leave empty
_______________________________________________________________
PRICES:
_______________________________________________________________
Type of Order = tdpcg.tyor.pc (Purchase Contract)
-----------------------------------------------------------
iPrice                          x                                     -
iPriceUnit                      x                                     -
iPriceUnitConversionFactor      x                                     -
iPriceBook                                            -               x
Explanation for the table above:
Either iPrice, iPriceUnit and iPriceUnitConversionFactor must be
filled (and iPriceBook must then be empty), OR
iPrice, iPriceUnit and iPriceUnitConversionFactor must be EMPTY
(and iPriceBook must then be filled).
Type of Order = tdpcg.tyor.sc (Sales Contract)
-----------------------------------------------------------
iPrice                          x                                     -
iPriceUnit                      x                                     -
iPriceUnitConversionFactor      x                                     -
iPriceBook                                            -               x
Type of Order = tdpcg.tyor.pq (RFQ)
-----------------------------------------------------------
iPrice                          x                                     -
iPriceUnit                      x                                     -
iPriceUnitConversionFactor      x                                     -
iPriceBook                                            -               x
Type of Order = tdpcg.tyor.so/sq/po/tr/sr/gs/gp
-----------------------------------------------------------
iPrice                          x
iPriceUnit                      x
iPriceUnitConversionFactor      x
iPriceBook                                            -
-----------------------------------------------------------
_______________________________________________________________
DISCOUNTS:
_______________________________________________________________
Type of Order = tdpcg.tyor.pc (Purchase Contract)
-----------------------------------------------------------
iDiscountPercentage     x                                     -
iDiscountAmount         x                                     -
iDiscountMethod         x                                     -
iDiscountOrigin         x               tdgen.dorg.not.applicable
iDiscountSchedule                             -               x
Type of Order = tdpcg.tyor.sc (Sales Contract)
-----------------------------------------------------------
iDiscountPercentage     x                                     -
iDiscountAmount         x                                     -
iDiscountMethod         x                                     -
iDiscountOrigin         x               tdgen.dorg.not.applicable
iDiscountSchedule                             -               x
Type of Order = tdpcg.tyor.pq (RFQ)
-----------------------------------------------------------
iDiscountPercentage     x                                     -
iDiscountAmount         x                                     -
iDiscountMethod         x                                     -
iDiscountOrigin         x               tdgen.dorg.not.applicable
iDiscountSchedule                             -               x
Type of Order = tdpcg.tyor.so/sq/po/tr/sr/gs/gp
-----------------------------------------------------------
iDiscountPercentage     x
iDiscountAmount         x
iDiscountMethod         x
iDiscountOrigin         x
iDiscountSchedule                             -
Pre:    NA
Post:   NA
Input:  iTypeOfOrder                                  - Mandatory
All enum values are allowed:
tdpcg.tyor.so                                   - Sales Order
tdpcg.tyor.sc                                   - Sales Contract
tdpcg.tyor.sq                                   - Sales Quotation
tdpcg.tyor.po                                   - Purchase Order
tdpcg.tyor.pc                                   - Purchase Contract
tdpcg.tyor.pq                                   - Request for Quotation
tdpcg.tyor.tr                                   - Transfer
tdpcg.tyor.sr                                   - General Service
tdpcg.tyor.gs                                   - General Sales
tdpcg.tyor.gp                                   - General Purchase
tdpcg.tyor.fm                                   - Freight Management
tdpcg.tyor.sr.soc                                   - Service Order
tdpcg.tyor.sr.msc                                   - Maintenance Sales Order
tdpcg.tyor.sr.quote                                   - Service Quote
iItem                                                 - Item; Mandatory
iManufacturerPartNumber                               - Manufacturer Part Number; Optional
This field is only used when
iPrice is zero and the price
is to be found using the given
price book.
iManufacturer                                         - Manufacturer; Optional
This field is only used when
iPrice is zero and the price
is to be found using the given
price book.
iQuantity                                             - Quantity; (zero is allowed)
iQuantityUnit                                         - Quantity Unit; Mandatory
iQuantityUnitConversionFactor                         - Conversion Factor of the Quantity
Unit; Mandatory
iPrice                                                - Price; Optional
iPriceUnit                                            - Price Unit; Mandatory if iPrice <> 0
iPriceUnitConversionFactor                            - Conversion Factor of the Price
Unit; Mandatory if iPrice <> 0
iPriceBook                                            - Price Book; Optional
iTransactionCurrency                                  - Transaction Currency; Mandatory
iRoundingMethod                                       - Rounding Method; Optional
iDiscountPercentage                                   - Discount Percentage; Optional
iDiscountAmount                                       - Discount Amount; Optional
iDiscountMethod                                       - Discount Method; Optional
iDiscountOrigin                                       - Discount Origin; Optional
iDiscountSchedule                                     - Discount Schedule; Optional
iPriceDate                                            - Date of the Order, Contract,
RFQ, etc; Mandatory
iOffice                                               - Sales Office, Purchase Office,
Contract Office, etc. Optional
This field is only used when
iPrice is zero and the price
is to be found using the given
price book.
iRoundAmounts                                         - true:  The amounts will be
rounded according
to the given currency
and rounding method.
-                                                       false: The amounts will not be
rounded.
Output: oNetAmount                                    - Net Amount
oGrossAmount                                          - Gross Amount
oTotalDiscountAmount                                  - Total Discount Amount
oStructureDiscountPercentage                          - Structure Discount Percentage
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Function was executed successfull.
<> 0                                          - An error occurred.
```
