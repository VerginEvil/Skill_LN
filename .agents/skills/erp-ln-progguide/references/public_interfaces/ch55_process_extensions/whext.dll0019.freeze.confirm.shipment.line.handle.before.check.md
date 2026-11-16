# whext.dll0019.freeze.confirm.shipment.line.handle.before.check

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StockPointBlocking
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2281-2282

```baan
Syntax: long whext.dll0019.freeze.confirm.shipment.line.handle.before.check(
domain  whinh.shpm       i.shipment,
domain  tcpono           i.shipment.line )
Usage:        Expl:   This process extension allows to include customer specific
functionality before the check on stock point blocking.
This process extension will be called from Infor LN
standard when the shipment line is frozen or confirmed via
sessions "Shipments" (whinh4630m000), Shipment Lines
(whinh4131m000), session "Freeze/Confirm Shipments/Loads"
(whinh4275m000), or when Freeze/Confirm Shipments/Loadsis an
automatic order step.
For each shipment line the process extension is executed before
the check on stock point blocking.
Following table is current when this extension is triggered:
whinh431 - Shipment Line
When the process extension is executed, this done within the
current database transaction. So no new db.retry.point should be
set or abort/commit should be performed.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.shipment      - Shipment
i.shipment.line - Shipment Line
Output: N.a.
Return: 0: Success / <> 0: Error
```
