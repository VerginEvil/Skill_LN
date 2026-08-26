# AssemblyProductVariant.CalculateStandardCost

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 861-863

```baan
DLL:   tiextascapi
This function is available from     2022.11 (KB2253167  ).
Syntax: long AssemblyProductVariant.CalculateStandardCost(
domain  tccpva           iProductVariant,
domain  tccpcc           iCalculationCode,
domain  tiutcs           iEffectiveDate,
domain  tcyesno          iActualizeCostForProductVariant,
domain  tcyesno          iUpdateNotStartedFrozenOrders,
domain  tcorno           iAssemblyOrderToUpdateFrom,
domain  tcorno           iAssemblyOrderToUpdateTo,
domain  tiutcs           iAssemblyOrderStartDateFrom,
domain  tiutcs           iAssemblyOrderStartDateTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to calculate the Standard Cost for a
specific Product Variant in Assembly. Calculation will be
performed after updating the product variant structures. The
result of the calculation may be used to update a specific set of
Assembly Orders based on the new calculations.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process; that is handled within
the function.
Input:  iProductVariant
-                               (Mandatory) Product Variant
iCalculationCode
-                               (Mandatory) Calculation Code
iEffectiveDate
-                               (Mandatory) Effective Date of Calculated Standard Cost.
iActualizeCostForProductVariant
-                               If set to YES,  the Current Standard Cost field in the
Product Variant (Assembly) is updated with the total
current value of the roll                                -off line taken from the Product
Variant Standard Costs by Calculation Code (tiapl3540m000)
session.If set to NO, only the new effective date and new
cost component details are updated in the Product Variant
Standard Costs by Calculation Code (tiapl3540m000).
iUpdateNotStartedFrozenOrders
-                               If set to YES, all assembly orders on which production
has not yet started are updated. On assembly orders with
WIP estimates already available and the status Sequenced,
the WIP estimates are updated with the new product
variant standard cost.
iAssemblyOrderToUpdateFrom
-                               Applies when iUpdateNotStartedFrozenOrders is YES.
Defines the FROM assembly order in the range of assembly
orders for which cost is actualized and not started
frozen orders are updated.
iAssemblyOrderToUpdateTo
-                               Applies when iUpdateNotStartedFrozenOrders is YES.
Defines the TO assembly order in the range of assembly
orders for which cost is actualized and not started
frozen orders are updated.
iAssemblyOrderStartDateFrom
-                               Applies when iUpdateNotStartedFrozenOrders is YES.
Defines the FROM START date to select planned assembly
orders for which cost is actualized and not started
frozen orders are updated.
iAssemblyOrderStartDateTo
-                               Applies when iUpdateNotStartedFrozenOrders is YES.
Defines the TO start date to select planned assembly
orders for which cost is actualized and not started
frozen orders are updated.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Calculation was successful.
<> 0                          - Calculation was not successful.
```
