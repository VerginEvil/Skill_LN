# StandardCost.UseAlternativeScheme

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StandardCost
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2254-2254

Standard Cost Calculation using Alternative Cost Component Scheme. This process extension is available from 2026.09 ( KB3641489 ). Technical information for this process extension:

```baan
Usage:        With this process extension, the Standard Cost Calculation can be
controlled to use an alternative Cost Component Scheme.
This behavior can only be applied for a Cost Calculation Code
that is used for simulation purposes. A Calculation Code is not for
simulation when it is defined as the Standard Cost Calculation Code
in Standard Cost Calculation Parameters (ticpr0100m000), or, when
calculating in a PCS Project context, it is defined as the project's
Cost Calculation Code in Projects (tipcs2101m000).
Two cooperating extension points are defined to allow efficient
control during the calculation.
First method (tiext.cpr0003.use.alternative.scheme) allows the extender
to control whether or not for the simulation code, an alternative
Cost Component Scheme must be considered during the calculations.
If the outcome indicates that the alternative scheme must be considered
then during the calculations, for each item/enterprise unit combination,
the second extension point method (tiext.cpr0003.get.alternative.scheme)
is called to obtain the alternative Cost Component Scheme.
```

To implement this process extension, you need to implement the following method(s):
