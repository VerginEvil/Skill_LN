# Pricing.SimulateServicePrice

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 513-518

```baan
DLL:   tdextpcgapi
This function is available from 2024.12 (KB3527699).
Syntax: long Pricing.SimulateServicePrice(
long             iProcessingOptionSet,
ref     domain  tcpric           oPrice,
ref     domain  tccuni           oPriceUnit,
ref     domain  tcconv           oPriceUnitConversionFactor,
ref     domain  tdpcg.made       oPriceMatrixDefinition,
ref     domain  tdpcg.prse       oPriceMatrixSequence,
ref     domain  tstdm.porg       oPriceOrigin,
ref     domain  tcprsg           oPriceStage,
ref     domain  tcdisc           oDiscount,
ref     domain  tcdisc           oDiscountPercentage(),
ref     domain  tcamnt           oDiscountAmount(),
ref     domain  tccdsc           oDiscountCode() fixed,
ref     domain  tddmth           oDiscountMethod(),
ref     domain  tdpcg.maty       oDiscountType(),
ref     domain  tdpcg.made       oDiscountDefinition() fixed,
ref     domain  tdpcg.prse       oDiscountSequence(),
ref     domain  tdgen.dorg       oDiscountOrigin(),
ref     domain  tcyesno          oDetermining,
ref     domain  tcyesno          oEligible,
ref             boolean          oDerivedItemUsed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface simulates service price and discounts
retrieval.
Price and discount retrieval is according to standard LN logic,
searching through the hierarchical price structure.
Via the Processing Option Set all details surrounding the price
defaulting request, such as the type of order, the Item,
Business Partners and original price data can be passed to this
Public Interface.
Pre:    Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iProcessingOptionSet
Processing Option Set: Mandatory, a processing option
set number referring to the processing option set
created through ProcessingOptionSet.Create().
NAME                    TYPE                    DEFAULT
================================================================
TypeOfOrder             domain  tdpcg.tyor      tdpcg.tyor.sr
The type of order to find a default price for.
Allowed values:
- tdpcg.tyor.sr         General Service
- tdpcg.tyor.sr.msc     Maintenance Sales
- tdpcg.tyor.sr.quote   Service Quote
- tdpcg.tyor.sr.soc     (Field) Service
OrderNumber             domain  tcorno          ""
The Order- or Quote number of the order to find a
default price for. This is only applicable and mandatory
if TypeOfOrder is tdpcg.tyor.sr.msc, tdpcg.tyor.sr.quote
or tdpcg.tyor.sr.soc.
UseDiscountsFromPriceBooks
domain  tcyesno         tcyesno.no
Whether or not to search for default discounts.
Item                    domain  tcitem          ""
Mandatory.
The Cost Line Item to find a default price for.
RentalSerialNumber      domain  tcibd.sern      ""
The Serial Number of the Rental Product/Equipment to
find a default price for. This is only applicable for
Rental Orders.
Site                    domain  tcsite          ""
The Site to find a default price for.
SoldToBusinessPartner   domain  tccom.bpid      ""
Mandatory.
The Sold-to Business Partner to find a default price
for.
ShipToBusinessPartner   domain  tccom.bpid      ""
The Ship-to Business Partner to find a default price
for.
InvoiceToBusinessPartner
domain  tccom.bpid      ""
Optional*
The Invoice-to Business Partner to find a default price
for.
PricingBusinessPartner  domain  tccom.bpid      ""
The Pricing Business Partner to find a default price
for.
ServiceOffice           domain  tccwoc          ""
The Service Office to find a default price for.
FinancialDepartment     domain  tccwoc          ""
The Financial Department to find a default price for.
SalesPriceList          domain  tccplt          ""
The Sales Price List to find a default price for.
SalesArea               domain  tccreg          ""
The Sales Area to find a default price for.
PaymentMethod           domain  tcpaym          ""
The Payment Method to find a default price for.
TermsOfDelivery         domain  tccdec          ""
The Terms of Delivery to find a default price for.
ServiceType             domain  tsmdm.cstp      ""
The Service Type to find a default price for.
InstallationGroup       domain  tsbsc.clst      ""
The Installation Group to find a default price for.
MaintainedItem          domain  tcitem          ""
The maintained Item to find a default price for.
MaintainedSerial        domain  tcibd.sern      ""
The Serial Number of the maintained Item to find a
default price for.
ServiceArea             domain  tsmdm.csar      ""
The Service Area to find a default price for.
ReferenceActivity       domain  tsacm.cact      ""
The Reference Activity to find a default price for.
MasterRouting           domain  tsacm.cact      ""
The Master Routing to find a default price for.
RoutingOption           domain  tsacm.cact      ""
The Routing Option to find a default price for.
Quantity                domain  tsmdm.qmat      0
The Quantity of the cost line to find a default price
for.
QuantityUnit            domain  tccuni          ""
Optional*
The Quantity Unit of the cost line to find a default
price for.
QuantityUnitConversionFactor
domain  tcconv          0.0
Optional*
The Quantity Unit Conversion Factor of the cost line to
find a default price for.
Currency                domain  tcccur          ""
Optional*
The Currency to find a default price in.
CurrencyRate1           domain  tcratc          0.0
The Currency Rate from the local currency to the
reference currency or given currency.
CurrencyRate2           domain  tcratc          0.0
The Currency Rate from reporting currency 1 to the
reference currency or given currency.
CurrencyRate3           domain  tcratc          0.0
The Currency Rate from reporting currency 2 to the
reference currency or given currency.
CurrencyRateFactor1     domain  tcratf          0
The Currency Rate Factor from the local currency to the
reference currency or given currency.
CurrencyRateFactor2     domain  tcratf          0
The Currency Rate Factor from reporting currency 1 to
the reference currency or given currency.
CurrencyRateFactor3     domain  tcratf          0
The Currency Rate Factor from reporting currency 2 to
the reference currency or given currency.
CurrencyRateDate        domain  tcdate          0
The Rate Date of the given Currency Rates and Factors.
CurrencyRateType        domain  tcrtyp          ""
The Rate Type of the given Currency Rates and Factors.
DeliveryDate            domain  tcdate          0
The Delivery Date to find a default price for.
OrderDate               domain  tcdate          0
The Order Date to find a default price for.
CostType                domain  tsmdm.cotp      tsmdm.cotp.material
The Cost Type to find a default price for.
Contract                domain  tcorno          ""
The Contract to find a default price for.
ContractChange          domain  tsctm.cchn      0
The Contract Change to find a default price for.
ConfigurationLine       domain  tsmdm.seqn      0
The Contract Configuration Line to find a default price
for.
CoverageTime            domain  tsmdm.trdt      0
The Coverage Time to find a default price for.
CoverageType            domain  tsmdm.cctp      ""
The Coverage Type to find a default price for.
CostComponent           domain  tccpcp          ""
The Cost Component to find a default price for.
Subcontractor           domain  tccom.bpid      ""
The Subcontractor to find a default price for.
* These fields will be defaulted if not provided.
Output: oPrice
The default Price found.
oPriceUnit
The default Price Unit found.
oPriceUnitConversionFactor
The default Price Unit Conversion Factor found.
oPriceMatrixDefinition
The default Price Matrix Definition found.
oPriceMatrixSequence
The default Price Matrix Sequence found.
oPriceOrigin
The Price Origin from which the default Price was
obtained if any.
oPriceStage
The default Price Stage found.
oDiscount
The default Discount found.
oDiscountPercentage
The array of default Discount Percentages found.
oDiscountAmount
The array of default Discount Amounts found.
oDiscountCode
The array of default Discount Codes found.
oDiscountMethod
The array of default Discount Methods found.
oDiscountType
The array of default Discount Types found.
oDiscountDefinition
The array of default Discount Definitions found.
oDiscountSequence
The array of default Discount Sequences found.
oDiscountOrigin
The array of default Discount Origins found.
oDetermining
The default Determining flag found.
oEligible
The default Eligible flag found.
oDerivedItemUsed
Whether or not a derived Item was used.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - No Error
<> 0    - Error
```
