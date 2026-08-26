# tdext.pur0006.suppress.combining.of.supply.order.lines.to.existing.supply.order

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for MaterialSupplyLines
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2085-2087

```baan
Syntax: boolean tdext.pur0006.suppress.combining.of.supply.order.lines.to.existing.supply.order(
domain  tcorno           i.previous.order,
domain  tcpono           i.previous.line,
domain  tcpono           i.previous.sequence,
domain  tcpono           i.previous.material.sequence,
domain  tcorno           i.purchase.order,
domain  tcpono           i.purchase.order.line,
domain  tcpono           i.purchase.order.line.sequence,
domain  tcpono           i.purchase.order.material.sequence,
domain  tcorno           i.target.sales.order,
domain  tcorno           i.target.sales.schedule,
domain  tcorno           i.target.warehouse.order,
domain  tcorno           i.target.purchase.order,
domain  tcorno           i.target.purchase.schedule )
Usage:        Expl.:  When generating supply orders for Material Supply Lines, use
this method to suppress combining new supply order lines with
existing supply orders.
When combining supply orders must be suppressed, a new supply
order will be generated instead of merging with an existing one.
The standard logic in LN first determines whether combining
supply orders is allowed. If combining is permitted, this method
is then called to decide whether combining should be suppressed
for the current operation.
When this method is called, the following applies:
-                               i.purchase.order is always filled;
-                               i.purchase.order.line is always filled
-                               i.purchase.order.line.sequence can be zero or > zero
-                               i.purchase.order.material.sequence is always filled
Pre:    Not Applicable.
Post:   Not Applicable.
Input:  i.previous.order        The previous purchase order for which
a supply                                              -order was generated in this
process.
i.previous.line         The previous purchase order line for
which a supply                                              -order was generated in
this process.
i.previous.sequence     The previous purchase order sequence
for which a supply                                              -order was generated
in this process.
i.previous.material.sequence
The previous purchase order material
sequence for which a supply                                              -order was
generated in this process.
i.purchase.order        Purchase Order. Always filled.
i.purchase.order.line   Purchase Order Line. Always filled.
i.purchase.order.line.sequence
Purchase Order Line Sequence. Can be
zero or > zero.
i.purchase.order.material.sequence
Purchase Order Material Sequence.
Always filled.
i.target.sales.order    For Material Supply Lines with the
Transfer Type set to
'Sales Order Transfer', this
variable contains the supply                                              -order that
would be used by LN in case of the
standard logic.
If empty, LN standard logic would
generate a new supply                                              -order.
i.target.sales.schedule For Material Supply Lines with the
Transfer Type set to
'Sales Schedule Transfer', this
variable contains the supply                                              -order that
would be used by LN in case of the
standard logic.
If empty, LN standard logic would
generate a new supply                                              -order.
i.target.warehouse.order
For Material Supply Lines with the
Transfer Type set to
'Warehouse Transfer', this
variable contains the supply                                              -order that
would be used by LN in case of the
standard logic.
If empty, LN standard logic would
generate a new supply                                              -order.
i.target.purchase.order
For Material Supply Lines with
Supply Type set to 'Supplier' and
configured to generate a purchase order,
this variable contains the supply                                              -order
that would be used by LN in case of the
standard logic.
If empty, LN standard logic would
generate a new supply                                              -order.
i.target.purchase.schedule
For Material Supply Lines with
Supply Type set to 'Supplier' and
configured to generate a purchase
schedule, this variable contains the
supply                                              -order that would be used by LN in
case of the standard logic.
If empty, LN standard logic would
generate a new supply                                              -order.
Output: Not Applicable.
Return: True                    Suppress adding the supply order line
to the existing supply order.
False                   Do not suppress adding the supply
order line to the existing supply
order.
This is the default value from the
extension, so by default, the
extension does not affect standard
combination logic.
```

## Process Extensions for OpenItem

The following process extension(s) is/are available: OpenItem.SkipSelectForInterestInvoices
