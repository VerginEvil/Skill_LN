# whext.dll0012.create.new.warehouse.order

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2314-2314

```baan
Syntax: long whext.dll0012.create.new.warehouse.order(
domain  tckoor           i.found.order.origin,
domain  tcorno           i.found.order,
domain  tcwset           i.found.order.set,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence,
ref             boolean          o.line.can.be.added.to.found.order )
Usage:        Expl:   This process extension allows to include customer specific
functionality during the process of releasing an order to
Warehousing. When an order line is released to Warehousing, the
standard process is searching for an existing warehouse order
header for the new order line and if found uses that warehouse
order header. This process extension will be called when the
process will find a warehouse order header to put the new line
onto, to allow 'custom' logic which should prevent the line from
being added to the warehouse order header.
The input arguments i.found.order.origin, i.found.order and
i.found.order.set are referring to the header that is found. The
i.order.line and i.order sequence refer to the line that is to
created and can be used to retrieve additional data from the
originating calling process. The determination of the source and
target data should be handled by the extender, so based on the
found order header and the order line + sequence the originating
line can be read and used to determine if this warehouse order
header can be used.
Pre:    N.a.
Post:   N.a.
Input:  i.found.order.origin    - Order Origin
i.found.order           - Order Number
i.found.order.set       - Order Set
i.order.line            - Order Line
i.order.sequence        - Order Sequence
Output: o.line.can.be.added.to.found.order - Can the line be added to
the order header that is found.
Return: 0: Success / <> 0: Error
```
