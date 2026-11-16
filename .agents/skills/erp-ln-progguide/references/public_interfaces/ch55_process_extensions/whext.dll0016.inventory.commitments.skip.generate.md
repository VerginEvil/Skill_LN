# whext.dll0016.inventory.commitments.skip.generate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InventoryCommitments
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2064-2064

```baan
Syntax: long whext.dll0016.inventory.commitments.skip.generate(
domain  whinp.corg       i.order.origin,
domain  tcorno           i.order.number,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence,
domain  tcpono           i.bom.line,
domain  tccwar           i.warehouse,
domain  tcncmp           i.rental.owner.company,
domain  tccwoc           i.rental.owner,
domain  tcitem           i.item,
domain  tcatse           i.attribute.set,
domain  tcuef.effn       i.effectivity.unit,
ref             boolean          o.generate.inventory.commitment )
Usage:        Expl:   This function allows you to skip the generation of an inventory
commitment by setting the output variable
o.generate.inventory.commitment to false.
Pre:    NA
Post:   NA
Input:  i.order.origin
i.order.number
i.order.line
i.order.sequence
i.bom.line
i.warehouse
i.rental.owner.company
i.rental.owner
i.item
i.attribute.set
i.effectivity.unit
Output: o.generate.inventory.commitment
Return: 0/DALHOOKERROR
```
