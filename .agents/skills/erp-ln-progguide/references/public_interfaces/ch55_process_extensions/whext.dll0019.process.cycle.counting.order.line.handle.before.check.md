# whext.dll0019.process.cycle.counting.order.line.handle.before.check

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StockPointBlocking
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2283-2283

```baan
Syntax: long whext.dll0019.process.cycle.counting.order.line.handle.before.check(
domain  tcorno           i.order,
domain  tcsern           i.count.number,
domain  tcpono           i.order.line )
Usage:        Expl:   This process extension allows to include customer specific
functionality before the check on available inventory.
This process extension will be called from Infor LN
standard when the cycle counting order line is processed via
sessions "Cycle Counting Orders" (whinh5100m000), Cycle
Counting Order (whinh5600m000) and "Cycle Counting Order Lines"
(whinh5101m000).
For each cycle counting order order line the process extension
is executed before the check on available inventory.
Following table is current when this extension is triggered:
whinh501 - Cycle Counting Order Line
When the process extension is executed, this done within the
current database transaction. So no new db.retry.point should be
set or abort/commit should be performed.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.order         - Order
i.count.number  - Count Number
i.order.line    - Order Line
Output: N.a.
Return: 0: Success / <> 0: Error
```
