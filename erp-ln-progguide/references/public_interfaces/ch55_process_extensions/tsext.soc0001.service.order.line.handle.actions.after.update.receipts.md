# tsext.soc0001.service.order.line.handle.actions.after.update.receipts

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ServiceOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2266-2267

```baan
Syntax: long tsext.soc0001.service.order.line.handle.actions.after.update.receipts(
domain  tcorno           i.service.order,
domain  tcpono           i.service.order.line )
Usage:        Expl.:  This function can be implemented to define additional actions
to the update of the direct delivery receipt in service.
For example: addition of Other Cost Lines.
When this function is called from the standard, the following
applies:
- i.service.order is filled
- i.service.order.line is filled
It is not allowed to do transaction management. This is
handled by the update receipt flow.
Pre:    -
Post:   -
Input:  i.service.order         - Service Order
i.service.order.line    - Service Order Line
Output: -
Return: 0/DALHOOKERROR
```
