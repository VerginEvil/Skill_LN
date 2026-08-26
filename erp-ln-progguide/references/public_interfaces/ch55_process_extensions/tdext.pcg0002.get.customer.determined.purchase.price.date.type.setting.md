# tdext.pcg0002.get.customer.determined.purchase.price.date.type.setting

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2113-2113

```baan
Syntax: long tdext.pcg0002.get.customer.determined.purchase.price.date.type.setting(
domain  tdpur.pric       i.purchase.price.date.type.from.standard.logic,
domain  tcncmp           i.logistic.company,
domain  tccwoc           i.purchase.office,
ref     domain  tdpur.pric       o.purchase.price.date.type.from.extension )
Usage:        Expl:   Use this method to get a customer determined purchase price date type
from an extension for purchase office setting. This price date type
will be used in Procurement.
Using this process extension, the purchase price date type from
standard logic can be changed to another value.
Note: The purchase office can be used to determine the price date type.
The purchase price date type from extension is only retrieved and used if:
-                       Process Extension Pricing.DefaultPriceDateType
(tdpcg.pric.def.pric.date.type) is implemented;
-                       The purchase price date type from extension is valid (and not empty);
-                       No errors are found during executing the extension.
Pre:    Not applicable
Post:   Not applicable
Input:  i.purchase.price.date.type.from.standard.logic                - As defaulted under the
standard logic
i.logistic.company                                                    - Logistic company
i.purchase.office                                                     - Purchase office
Output: o.purchase.price.date.type.from.extension                     - The price date type
determined by
the extension
Return: 0                                                            -  Success
DALHOOKERROR                                                          - When an error occurs in
the deter      -
mination of the price
date type
from extension
```
