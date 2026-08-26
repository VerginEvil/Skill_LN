# tiext.cpr0003.get.alternative.scheme

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StandardCost
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2254-2255

```baan
Syntax: long tiext.cpr0003.get.alternative.scheme(
domain  tccpcc           i.calculation.code,
domain  tcitem           i.item,
domain  tcemm.grid       i.enterprise.unit,
ref     domain  ticpr.chrt       o.alternative.scheme )
Usage:        Expl:   This method is called in the process of Standard Cost
Calculation. It must return the Alternative Cost
Calculation Scheme to be used for the calculation.
When this method is called all fields of table:
-                       Items - Costing (ticpr007) for the given Item and
Enterprise Unit are current.
Implementation Example:
Intention:
For certain calculation codes the use of Cost
Calculation Scheme with many components is
required. The Items                               - Costing table (ticpr007)
is extended with a Customer Defined Field (altc)
with Data Type String having domain ticpr.chrt
Hook Declarations:
table tticpr007
Hook :
function extern long tiext.cpr0003.get.alternative.scheme(
...)
{
o.alternative.scheme = ticpr007.cdf_altc
return(0)
}
Pre:    NA
Post:   NA
Input:  i.calculation.code                    - calculation code
i.item                                        - item for calculation
i.enterprise.unit                             - enterprise unit
Output: o.alternative.scheme                  - the alternative cost calculation
scheme to be used in the calculation.
Return: 0                                     - success
```
