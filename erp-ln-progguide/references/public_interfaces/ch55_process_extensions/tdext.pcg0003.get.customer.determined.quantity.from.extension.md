# tdext.pcg0003.get.customer.determined.quantity.from.extension

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2117-2118

```baan
Syntax: long tdext.pcg0003.get.customer.determined.quantity.from.extension(
domain  tdpcg.tyor       i.type.of.order,
domain  tcqsl1           i.ordered.quantity,
domain  tccuni           i.quantity.unit,
domain  tcconv           i.conv.factor,
domain  tcqsl1           i.original.ordered.quantity,
ref     domain  tcqsl1           o.quantity.based.on.extension )
Usage:        Expl:   This function gets the customer determined order quantity
from an extension, if applicable.
The order quantity from extension is only retrieved and used if:
-                       Process Extension Pricing.HandleInputOverruling
(tdpcg.pricing.handle.input) is implemented;
-                       No errors are found during executing the extension.
Pre:    Not applicable
Post:   Not applicable
Input:  i.type.of.order                                       - The type of order for which
pricing is called
i.ordered.quantity                                            - As defaulted under the
standard logic
i.quantity.unit                                               - Quantity Unit
i.conv.factor                                                 - Conversion Factor
i.original.ordered.quantity                                   - Original Ordered Quantity
Output: o.quantity.based.on.extension                         - The order quantity
determined by the extension
Return: 0                                                     - Success
DALHOOKERROR                                                  - When an error occurs in the
determination of the
order quantity
```
