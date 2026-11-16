# whext.dll0021.overrule.qty.to.advise

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InventorySearchEngine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2069-2069

```baan
Syntax: long whext.dll0021.overrule.qty.to.advise(
domain  whinh.oorg       i.order.origin,
domain  tcorno           i.order.number,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence,
ref     domain  tcqiv1           io.quantity.to.advise )
Usage:        Expl:   This function allows to override the quantity to advise
during the outbound advice inventory allocation process.
Advised quantity must correspond to ordered quantity.
This process extension is called from the outbound advice
generation, during the inventory allocation loop.
Following tables are current when this extension is
triggered:
whinh200 - Warehouse Order Header
whinh220 - Outbound Order Line
Note: If you execute queries on the standard Infor LN
tables, bind the table fields to local variables to
prevent disturbing the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.order.origin          - Order Origin
i.order.number          - Order Number
i.order.line            - Order Line
i.order.sequence        - Order Sequence
io.quantity.to.advise   - Quantity to Advise
Output: io.quantity.to.advise   - Quantity to Advise (overruled)
Return: 0: Success / <> 0: Error
```
