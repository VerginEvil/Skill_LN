# WorkOrder.GetActualRepairCosts

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1493-1495

```baan
DLL:   tsextwcsapi
This function is available from     2021.07 (KB2195953  ).
Syntax: long WorkOrder.GetActualRepairCosts(
domain  tcorno           iWorkOrder,
ref             long             oNumberOfHomeCurrencies,
ref     domain  tcccur           oHomeCurrencies() fixed,
ref     domain  tcamnt           oMaterialCosts(),
ref     domain  tcamnt           oLaborCosts(),
ref     domain  tcamnt           oOtherCosts(),
ref     domain  tcamnt           oTotalCosts(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this function the actual material, labor and other costs
for a work order can be determined.
The cost arrays are expressed in the home currencies which
relate to the financial company of the service department of
the work order (tswcs200.cwoc).
Note:
The output arrays should already have been allocated at the
calling side with a depth of 3!
Important: the cost arrays are always filled on the first
array element position, which represents the local currency.
However the costs are not always filled on the reporting
currency amount positions, which are the element positions 2
and 3 in the arrays. Only in an independent currency system, or
in a standard currency system with the usage of functional
currencies switched on, the costs are present on all the used
home currency positions.
So suppose we have a dependent currency system which uses 3
home currencies, i.e. [EUR, USD, YEN].
This means that the output argument oNumberOfHomeCurrencies
is filled with 3 and the array oHomeCurrencies is
filled with [EUR, USD, YEN].
However, the arrays with the costs are only filled on the first
(local currency) position, so i.e. oMaterialCosts =
[100.0, 0.0, 0.0] etc.
Suppose we have an independent currency system which uses
2 home currencies, i.e. [BRL, USD], then the
oNumberOfHomeCurrencies is filled with 2 and the array
oHomeCurrencies is filled with [BRL, USD].
The array with costs is filled on all home currency positions,
so i.e. oMaterialCosts = [100, 10].
Pre:    The output arrrays should have been allocated three elements
deep.
Post:   N.A.
Input:  iWorkOrder
The work order  (mandatory input). The system will
generate an error if the work order does not exist.
Output: oNumberOfHomeCurrencies
The number of home currencies of the financial company
of the work order department.
oHomeCurrencies
The array (3 deep) with the home currencies of the
financial company of the work order department.
oMaterialCosts
The array (3 deep) with the material costs.
oLaborCosts
The array (3 deep) with the labor costs.
oOtherCosts
The array (3 deep) with the other costs.
oTotalCosts
The array (3 deep) with the total costs. The sum of
material, labor and other costs.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - The work order actual repair costs could be determined.
<> 0                          - Error while determining the work order actual repair
costs.
```
