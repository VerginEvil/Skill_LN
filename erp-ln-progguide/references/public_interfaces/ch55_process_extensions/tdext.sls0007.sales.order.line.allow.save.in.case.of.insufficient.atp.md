# tdext.sls0007.sales.order.line.allow.save.in.case.of.insufficient.atp

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2235-2236

```baan
Syntax: boolean tdext.sls0007.sales.order.line.allow.save.in.case.of.insufficient.atp(
domain  tcorno           i.sales.order,
domain  tcpono           i.sales.order.line,
domain  tcpono           i.sales.order.line.sequence )
Usage:        Expl.:  This function can be implemented to allow saving a sales order line
in case of insufficient ATP.
The standard logic of LN only allows this in case the sales order
(line) is created or updated through EDI. With this function it is
possible to also allow this for non EDI orders.
When this function is called from the standard, the following
applies:
-                       i.sales.order is filled
-                       i.sales.order.line is filled
-                       i.sales.order.line sequence is filled (can be zero)
-                       A record of tdsls401 is current
Input:  i.sales.order                         - Sales Order
i.sales.order.line                            - Sales Order Line
i.sales.order.line.sequence
-                                               Sales Order Line Sequence
Output: Not Applicable
Return: true                                  - The extension has determined that it is
allowed to save the order line when there
is insufficient ATP.
false                                         - The extension has determined that it is
not allowed to save the order line when
there is insufficient ATP.
This reflects the standard LN logic for
non EDI orders.
```
