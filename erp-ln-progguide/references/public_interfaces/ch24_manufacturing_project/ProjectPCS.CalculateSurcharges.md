# ProjectPCS.CalculateSurcharges

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 878-880

```baan
DLL:   tiextpcsapi
This function is available from     2024.08 (KB2319474  ).
Syntax: long ProjectPCS.CalculateSurcharges(
domain  tccprj           iProject,
domain  tcccur           iCurrency,
domain  tcncmp           iFinancialCompany,
domain  tckoch           iSurchargeType,
long             iNumberOfRows,
const   domain  tccpcp           iCostComponents() fixed,
const           double           iAmounts(,),
ref             long             oNumberOfRows,
ref     domain  tccpcp           oCostComponents() fixed,
ref             double           oFixedSurcharges(,),
ref             double           oVariableSurcharges(,),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:                This function calculates the Project Surcharges based on
the given set of amounts in the input arrays.
The output arrays are allocated by this function and must be
declared as based.
The output arrays will contain the calculation results,
separated out into fixed cost                       - and variable cost project
surcharges.
Pre:    N.A.
Post:   N.A.
Input:  iProject
The project for which surcharges need to be
calculated (Mandatory).
iCurrency       The input Currency applies when the currency
system is Dependent or Single. It defines the
currency of the input and output amounts.
iFinancialCompany
The input Financial Company applies when the
currency system Standard. It defines the currency
setup of the input and output amounts.
iSurchargeType
Surcharge Type to defines which type of surcharges
are selected from the Project Surcharges (Mandatory).
Possible options are:
tckoch.est.charge: Estimated Surcharge
tckoch.act.charge: Actual Surcharge
iNumberOfRows
Number of rows in input arrays. if this value
is zero, then still fixed amount surcharges may
be applied, which are independent of the input set.
iCostComponents
Array with input cost components.
iAmounts
Array with currency amounts, per cost component,
a maximum of three (3) currency amounts can be given.
Output: oNumberOfRows
Number of rows in output arrays.
will match the allocation of the output arrays
oCostComponents
Array with the output cost components.
oFixedSurcharges
Array with the calculated fixed project surcharges
Note: when the parameter Include Fixed
Costs in Project Valuation (tipcs000.fciv) is
set to No, then fixed surcharges should not
be designated as actual project cost.
oVariableSurcharges
Array with the calculated variable project surcharges.
oExceptionMessage
The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               Successfull.
<> 0            Not successfull.
```
