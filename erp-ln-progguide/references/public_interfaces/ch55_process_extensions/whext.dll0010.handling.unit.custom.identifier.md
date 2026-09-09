# whext.dll0010.handling.unit.custom.identifier

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2049-2050

```baan
Syntax: long whext.dll0010.handling.unit.custom.identifier(
domain  whinh.shpm       i.receipt,
domain  tcpono           i.receipt.line,
domain  whinh.shpm       i.shipment,
domain  tcpono           i.shipment.line,
domain  tcitem           i.item,
domain  tcclot           i.lot,
domain  tcibd.sern       i.serial,
domain  tcinvt.date      i.inventory.date,
domain  tccwar           i.warehouse,
domain  whloca           i.location,
ref     domain  whhuid           o.handling.unit.id )
Usage:        Expl:   This function can be implemented to use a custom handling
unit identifier based on the specified fields.
Pre:    NA
Post:   A check should be done to see if the handling unit identifier
already exists.
Input:  i.receipt
i.receipt.line
i.shipment
i.shipment.line
i.item
i.lot
i.serial
i.inventory.date
i.warehouse
i.location
Output: o.handling.unit.id
Return: 0/DALHOOKERROR
```
