# tiext.pcf0001.adjust.variant.price

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2149-2150

```baan
Syntax: long tiext.pcf0001.adjust.variant.price(
ref     domain  tipcf.pric       io.price )
Usage:        Expl:
This method is called at the end of the sales or purchase
price calculation for a certain line of the generic price
list, just before rounding the final result. So when a
generic price list has multiple lines, this method is
called during processing of each of these lines.
With this method, the value of calculated sales or purchase
price can be adjusted.
When this method is called, the Generic Price List record
(tipcf400) is read and and all tipfc400 fields are current
(inclusing the Customer Defined Fields) and can be
used in this method.
EXAMPLE:
Assume that ticpf400.acst (Administration Cost) is a CDF on
table tipcf400, and must be applied during the sales price
calculation. The following logic could be added to
adjust the calculated price
if tipcf400.kopl = tckopl.sales then
io.price = io.price + tipfc400.acst
endif
Pre:    when ticpf400 fields are used: include
table   ttipcf400
in the global variable section of the extension.
Post:   N.A.
Input:  io.price
Output: io.price
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in the
added logic
```
