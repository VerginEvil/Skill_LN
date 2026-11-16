# tdext.pcg0002.get.customer.determined.sales.price.date.type.parameter

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2136-2137

```baan
Syntax: long tdext.pcg0002.get.customer.determined.sales.price.date.type.parameter(
domain  tdpur.pric       i.sales.price.date.type.from.standard.logic,
domain  tcncmp           i.logistic.company,
ref     domain  tdpur.pric       o.sales.price.date.type.from.extension )
Usage:        Expl:   Use this method to get a customer determined sales price date type
from an extension for sales parameter. This price date type will
be used in Sales.
Using this process extension, the sales price date type from
standard logic can be changed to another value.
The sales price date type from extension is only retrieved and used if:
- Process Extension Pricing.DefaultPriceDateType
(tdpcg.pric.def.pric.date.type) is implemented;
- The sales price date type from extension is valid (and not empty);
- No errors are found during executing the extension.
Pre:    Not applicable
Post:   Not applicable
Input:  i.sales.price.date.type.from.standard.logic     - As defaulted under the
standard logic
i.logistic.company                              - Logistic company
Output: o.sales.price.date.type.from.extension          - The price date type
determined by
the extension
Return: 0                                               - Success
DALHOOKERROR                                    - When an error occurs in
the deter-
mination of the price
date type
from extension
```
