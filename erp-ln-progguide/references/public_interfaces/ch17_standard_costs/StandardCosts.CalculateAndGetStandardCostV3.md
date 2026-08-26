# StandardCosts.CalculateAndGetStandardCostV3

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 607-608

```baan
DLL:   tiextcprapi
This function is available from     2026.02 (KB3647993  ).
Syntax: long StandardCosts.CalculateAndGetStandardCostV3(
domain  tccpcc           iCalculationCode,
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
domain  tcuef.effn       iEffectivityUnit,
domain  tcdate           iStandardCostDate,
boolean          iUseSpecifiedOrderQuantity,
domain  tiqep1           iOrderQuantity,
boolean          iUseCalculatedOrderQuantityComponents,
boolean          iRecalculateStandardParts,
domain  tccpcc           iCalculationCodeStandardParts,
ref             long             oNumberOfCurrencies,
ref     domain  tcccur           oCurrencies() fixed,
ref             long             oNumberOfCostComponents,
ref     domain  tccpcp           oCostComponents() fixed,
ref     domain  tcqnu1           oCostNumberOfUnits(),
ref     domain  tccopr           oCostTotal(,),
ref     domain  tccopr           oCostFixed(,),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates standard costs for the given Calculation
Code, Item and Enterprise Unit. The calculated standard cost is
returned in the output arrays.
NOTE: The calculated standard cost is not stored in the
standard cost records for the item.
Input:  iCalculationCode        Calculation Code (Mandatory)
iItem                   Item (Mandatory)
iEnterpriseUnit         Enterprise Unit (mandatory filled when
the concept Standard Cost per EU
is active, otherwise empty)
iEffectivityUnit        Effectivity Unit, use 0 when not used.
iStandardCostDate       Reference Date for calculation.
iUseSpecifiedOrderQuantity
When true: Calculate standard cost based
on the given order quantity
iOrderQuantity          Order Quantity
iUseCalculatedOrderQuantityComponents
When true: Calculation of the standard
cost for components in the product
structure, will use the calculated
order quantity.
When false: the calculation will use
the predefined order quantity.
iRecalculateStandardParts
When true: if the top level item is
configured, the standard parts that
are encountered in the product structure
are recalculated.
iCalculationCodeStandardParts
When reading or re                                              -calculating the
standard parts in the product structure,
of a configured item, they are
calculated using the given calculation
code. In case this input is left empty,
the Standard Cost Calculation Code
as defined in Standard Cost Calculation
Parameters (ticpr0100m000) is used.
Output:
oNumberOfCurrencies     Number of currencies
oCurrencies             Currencies in CostTotal/CostFixed arrays
Array of Home Currencies, allocated by
caller.
oNumberOfCostComponents Number of cost components in the output
arrays.
oCostComponents         Cost Component arrays
(allocated by function)
oCostNumberOfUnits      Cost number of units for cost component
(allocation by function)
oCostTotal              Cost total for cost component
(allocation by function)
oCostFixed              Fixed Cost for cost component
(allocation by function)
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Standard Cost calculated and stored in
ouput arrays
<> 0                    failure
```
