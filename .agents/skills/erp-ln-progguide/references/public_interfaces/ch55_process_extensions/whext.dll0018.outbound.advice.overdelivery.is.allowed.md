# whext.dll0018.outbound.advice.overdelivery.is.allowed

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2113-2113

```baan
Syntax: boolean whext.dll0018.outbound.advice.overdelivery.is.allowed(
domain  whinh.oorg       i.order.origin,
domain  tcorno           i.order.number,
domain  tcwset           i.order.set,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence )
Usage:        Expl:   This function allows to override the overdelivery check for
internal orders during the generation of outbound advice.
When this function returns true, the overdelivery is
considered allowed.
This process extension is only applicable for internal
orders and not for actual sales orders.
Following tables are current when this extension is triggered:
whinh220 - Outbound Order Line
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.order.origin          - Order Origin
i.order.number          - Order Number
i.order.set             - Order Set
i.order.line            - Order Line
i.order.sequence        - Order Sequence
Output: N.a.
Return: true:  Overdelivery is allowed
false: Overdelivery is not allowed (standard behavior)
```
