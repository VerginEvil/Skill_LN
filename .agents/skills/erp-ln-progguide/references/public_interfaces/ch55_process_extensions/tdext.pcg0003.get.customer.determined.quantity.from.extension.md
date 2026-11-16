# tdext.pcg0003.get.customer.determined.quantity.from.extension

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2140-2141

```baan
Syntax: long tdext.pcg0003.get.customer.determined.quantity.from.extension(
domain  tdpcg.tyor       i.type.of.order,
domain  tcqsl1           i.ordered.quantity,
domain  tccuni           i.quantity.unit,
domain  tcconv           i.conv.factor,
domain  tcqsl1           i.original.ordered.quantity,
ref     domain  tcqsl1           o.quantity.based.on.extension )
Usage:        Expl:   This function sets the customer determined order quantity.
Pre:    Not applicable
Post:   Not applicable
Input:  i.type.of.order                         - The type of order for which
pricing is called
i.ordered.quantity                      - As defaulted under the
standard logic
i.quantity.unit                         - Quantity Unit
i.conv.factor                           - Conversion Factor
i.original.ordered.quantity             - Original Ordered Quantity
Output: o.quantity.based.on.extension           - The order quantity
determined by the extension
Return: 0                                       - Success
DALHOOKERROR                            - When an error occurs in the
determination of the
order quantity, the
LN flow will use the
original quantity.
```
