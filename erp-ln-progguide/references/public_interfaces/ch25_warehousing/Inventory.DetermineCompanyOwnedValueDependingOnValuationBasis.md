# Inventory.DetermineCompanyOwnedValueDependingOnValuationBasis

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 936-939

```baan
DLL:   whextinaapi
This function is available from     2026.01 (KB3544552  ).
Syntax: long Inventory.DetermineCompanyOwnedValueDependingOnValuationBasis(
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
boolean          iSpecificAttributeSet,
domain  tcatse           iAttributeSet,
domain  tcqiv1           iCompanyOwnedInventory,
domain  whina.valb       iValuationBasis,
boolean          iByAttributeSet,
domain  whina.prap       iLevelMarketPrice,
domain  whina.prap       iLevelPurchasePrice,
domain  tcprus           iPriceToBeUsed,
domain  tcdate           iValuationDate,
boolean          iIncludeAntedated,
domain  tcccur           iCurrency,
domain  tcrtyp           iRateType,
ref             long             oNumberOfCostComponents,
ref     domain  tccpcp           oCostComponents() fixed,
ref     domain  tcamnt           oCompanyOwnedInventoryValue(),
ref     domain  tcamnt           oCompanyOwnedInventoryTotalValue,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will determine the inventory value
on a certain date, based on a defined valuation basis
(so not based on actual Inventory Valuation Method).
It is only meant for company owned inventory.
Pre:    N.A.
Post:   oCostComponents and oCompanyOwnedInventoryValue will be
allocated, so a free.mem() must be used to free the memory which
is used by these arrays.
Input:  iItem
The item for which inventory value needs to be
determined.
This is mandatory to fill.
iWarehouse
The warehouse for which inventory value needs to be
determined.
This is mandatory to fill.
iSpecificAttributeSet
Indicator (True/False) if inventory value needs to be
determined for a specific attribute set.
This indicator can only be set when iItem is
dimension controlled.
This is mandatory to fill.
iAttributeSet
The attribute set for which inventory value needs
to be determined.
This is mandatory to fill if iSpecificAttributeSet is
set to True.
iCompanyOwnedInventory
The company owned inventory (quantity) on specific
date (iValuationDate). This is the quantity as returned
by public interface Inventory.DetermineQuantityAndValue
(any version) and/or Inventory.DetermineQuantity.
iValuationBasis
The Valuation Basis against which the inventory value
should be reported.
Possible options:
* MAUC by Warehouse (whina.valb.mauc)
* Standard Cost (whina.valb.ftp)
* Market Value Including Surcharges
(whina.valb.market.incl.sur)
* Market Value Excluding Surcharges
(whina.valb.market.excl.sur)
* Average Purchase Price Including Surcharges
(whina.valb.aver.incl.sur)
* Average Purchase Price Excluding Surcharges
(whina.valb.aver.excl.sur)
This is mandatory to fill
iByAttributeSet
Indicator (True/False) if valuation basis should be
based on Attribute Set Level if applicable, else
Item Level is used.
This indicator can only be set to True when:
-                               iItem is dimension controlled.
-                               iSpecificAttributeSet is True
This is mandatory to fill
iLevelMarketPrice
The Level Market Price should be used to indicate at
which level the market price is searched.
Possible options:
* Item (whina.prpa.item)
Price search is done within iItem.
* Item/Warehouse (whina.prpa.itwh)
Price search is done within iItem and
iWarehouse.
* Item/Warehouse Valuation Group (whina.prpa.itwv)
Price search is done within iItem and the
valuation group of iWarehouse.
* Item/Site (whina.prpa.itsi)
Price search is done within iItem and the
site of iWarehouse.
This is mandatory to fill if iValuationBasis is
Market Value Including Surcharges or
Market Value Excluding Surcharges
iLevelPurchasePrice
The Level Purchase Price should be used to indicate
at which level the purchase price is searched.
Possible options:
* Item (whina.prpa.item)
Price search is done within iItem.
* Item/Site (whina.prpa.itsi)
Price search is done within iItem and the
valuation group of iWarehouse.
This is mandatory to fill if iValuationBasis is
Average Purchase Price Including Surcharges or
Average Purchase Price Excluding Surcharges
iPriceToBeUsed
Price Used if purchase receipts exist after the
last Market Value.
Possible options:
* Last Available Market Price (tcprus.market)
The price is taken from the market values.
* Last Available Order Price (tcprus.order)
The price is taken from the receipt
transactions.
This is mandatory to fill if iValuationBasis is
Market Value Including Surcharges or
Market Value Excluding Surcharges
iValuationDate
The date for which inventory value needs to be
determined.
This is optional to fill.
When leaving this empty the current date will be used.
iIncludeAntedated
Indicator (True/False) if antedated transactions should
be included or not.
Antedated transactions are transactions having
transaction date before the valuation date and actual
log date after the valuation date.
This is mandatory to fill.
iCurrency
The currency in which the inventory value needs to be
expressed. This is mandatory to fill.
iRateType
The rate type for which inventory value needs to be
determined.
This is optional to fill.
If empty the internal rate type is used.
Output: oNumberOfCostComponents
The number of cost components.
oCostComponents
Array with the found cost components.
oCompanyOwnedInventoryValue,
Array with the found inventory values by cost component.
oCompanyOwnedInventoryTotalValue,
The total inventory value.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0               - The inventory and inventory value have been found
successfully.
<> 0                       - Error. The inventory and inventory value could not be
determined.
```
