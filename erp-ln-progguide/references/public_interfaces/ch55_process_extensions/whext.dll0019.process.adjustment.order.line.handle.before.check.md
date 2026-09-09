# whext.dll0019.process.adjustment.order.line.handle.before.check

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StockPointBlocking
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2282-2282

```baan
Syntax: long whext.dll0019.process.adjustment.order.line.handle.before.check(
domain  tcorno           i.order,
domain  tcpono           i.order.line )
Usage:        Expl:   This process extension allows to include customer specific
functionality before the check on available inventory.
This process extension will be called from Infor LN
standard when the adjustment order line is processed via
sessions "Adjustment Orders" (whinh5120m000), Adjustment Order
(whinh5120m100) and "Adjustment Order Lines" (whinh5121m000).
For each adjustment order line the process extension is executed
before the check on available inventory.
Following table is current when this extension is triggered:
whinh521 - Adjustment Order Line
When the process extension is executed, this done within the
current database transaction. So no new db.retry.point should be
set or abort/commit should be performed.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.order         - Order
i.order.line    - Order Line
Output: N.a.
Return: 0: Success / <> 0: Error
```
