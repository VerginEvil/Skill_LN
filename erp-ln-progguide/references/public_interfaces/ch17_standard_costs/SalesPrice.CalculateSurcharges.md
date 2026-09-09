# SalesPrice.CalculateSurcharges

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for SalesPrice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 617-618

```baan
DLL:   tiextcprapi
This function is available from 2024.10 (KB2312058).
Syntax: long SalesPrice.CalculateSurcharges(
domain  tcitem           iItem,
domain  tccpcc           iSalesPriceCalculationCode,
domain  tiutcs           iCalculationDate,
domain  tccwoc           iSalesOffice,
ref     domain  tcccur           oCurrency,
ref             long             oNumberOfSurcharges,
ref     domain  tccpcp           oCostComponents() fixed,
ref     domain  tccopr           oVariableSurcharges(),
ref     domain  tccopr           oFixedSurcharges(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface calculates sales price surcharges.
Pre:    N.A.
Post:   N.A.
Input:  iItem                   Item for which the surcharges
are calculated (Mandatory).
iSalesPriceCalculationCode
The Calculation Code for the
Sales Price (Mandatory).
iCalculationDate        The Calculation Date, to get the
Currency rates (Mandatory).
iSalesOffice            Sales Office (Mandatory).
Output: oCurrency               Currency
oNumberOfSurcharges     Number of rows in output arrays.
oCostComponents()       Array with the Cost Components
oVariableSurcharges()   Array with the calculated variable
project surcharges.
oFixedSurcharges()      Array with the calculated fixed project
surcharges.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Sales price surcharges are calculated.
<> 0                    Errors occurred.
```
