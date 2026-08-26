# cpext.pat0002.get.custom.defined.production.order.series

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TransferOrderPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2282-2282

```baan
Syntax: long cpext.pat0002.get.custom.defined.production.order.series(
domain  tcseri           i.order.series,
ref     domain  tcseri           o.order.series )
Usage:        Expl:   This method is called prior to the transfer of a Planned
Production Order, to get a custom Order Series.
This custom order series will override the Production Order
Series given on session 'Transfer Order Planning'
(cppat1210m000) or session Transfer Planned
Production Orders (cppat1211m000).
Note:
1)      Attributes of table cprrp100 including customer defined
fields are made current and can be used.
2)      If this function returns an empty string in o.order.series,
then LN will use the standard order.series.
Example:
o.order.series = ""
if custom.order.series is filled then
o.order.series is filled with custom.order.series
endif
Pre:    NA
Post:   NA
Input:  i.order.series                - the order series from the standard session
Output: o.order.series                - the order series to use for this transfer.
may be left empty, in that case the input Order
series will be used for the transfer
Return: 0                             - Success
```
