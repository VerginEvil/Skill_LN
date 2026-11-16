# tdext.pcg0003.get.customer.determined.price.date.from.extension

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2140-2140

```baan
Syntax: long tdext.pcg0003.get.customer.determined.price.date.from.extension(
domain  tdpcg.tyor       i.type.of.order,
domain  tcdate           i.price.date.from.standard.logic,
ref     domain  tcdate           o.price.date.based.on.extension )
Usage:        Expl:   This function sets the customer determined price date.
Pre:    Not applicable
Post:   Not applicable
Input:  i.type.of.order                         - The type of order for which
pricing is called
i.price.date.from.standard.logic        - As defaulted under the
standard logic
Output: o.price.date.based.on.extension         - The price date
determined by the extension
Return: 0                                       - Success
DALHOOKERROR                            - When an error occurs in the
determination of the
price date, the
LN flow will use the
original price date.
```
