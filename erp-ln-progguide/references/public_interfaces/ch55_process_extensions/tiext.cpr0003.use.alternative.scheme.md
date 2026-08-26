# tiext.cpr0003.use.alternative.scheme

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StandardCost
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2255-2256

```baan
Syntax: long tiext.cpr0003.use.alternative.scheme(
domain  tccpcc           i.calculation.code,
ref             boolean          o.use.alternative.scheme )
Usage:        Expl:   This method is called in the process of Standard Cost
Calculation, in order to decide if the calculation must be
executed with an alternative Cost Calculation Scheme.
When this method is called all fields of table:
-                       Cost Calculation Code (ticpr100) for the given Calculation
Code are read and current.
Implementation Example:
Intention:
For certain calculation codes the use of Cost
Calculation Scheme with many components is
required. In order to allow different users to perform
calculations independently, the Cost Calculation Code
table (ticpr100) is extended with a Customer Defined
Field (alts) with Data Type Checkbox having domain
tcyesno.
Hook Declarations:
table tticpr100
Hook :
function extern long tiext.cpr0003.use.alternative.scheme(
...)
{
o.use.alternative.scheme =
(ticpr100.cdf_alts = tcyesno.yes)
return(0)
}
Pre:    NA
Post:   NA
Input:  i.calculation.code                     - calculation code
Output: o.use.alternative.scheme               - to indicate whether or not
an alternative scheme may
be used.
Return: 0                                      -  success
```

## Process Extensions for Statement

The following process extension(s) is/are available: Statement.SkipPrintStatements
