# tdext.pur0003.determine.purchase.order.for.combining.order.lines.during.generation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2199-2201

```baan
Syntax: long tdext.pur0003.determine.purchase.order.for.combining.order.lines.during.generation(
domain  tcorno           i.purchase.order,
domain  tcpono           i.purchase.order.line,
domain  tdpur.corg       i.purchase.order.origin,
long             i.source.generating.process,
ref     domain  tcorno           o.purchase.order )
Usage:        Expl:   Use this method to get a customer determined purchase order that
will be used when generating purchase order lines. If this
extension returns a purchase order, then that purchase order
will be used to add the new purchase order line to.
Note that after calling this method, LN will also consider
the method
tdext.pur0003.suppress.combining.of.purchase.order.lines.to.existing.order.during.generati
on
If implemented, that extension could prevent combining the
order line.
If the extension returns a purchase order that is closed or
cancelled, then LN will create a new order. The same happens if
attributes on the returned purchase order do not match with the
attributes that are actually required.
If the extension returns a purchase order that is not updatable,
then an error is returned during generation.
This extension is implemented for multiple purchase order generation
processes. See below.
Input:  i.purchase.order        - Purchase Order
If filled, this refers to the purchase
order that would be used by the
standard logic.
If empty, LN standard logic would
generate a new purchase order.
i.purchase.order.line   - Purchase Order Line (Optional)
If filled, this refers to the purchase
order line that would be used by
standard logic; LN would create a new
detail-line.
i.purchase.order.origin - The Purchase Order Origin from / for
which the purchase order is generated.
i.source.generating.process
- Indicates the source process from /
for which the purchase order is
generated and where an order header
can be created.
Possible Values:
0           Undefined - Use
i.purchase.order.origin
to determine the source
process
1           Sales Order Components
(Kitting)
2           Return Rejected
The following generation sources can support creation of
multiple order headers and can be affected by the process
extension. These processes are either identified by the origin
(i.purchase.order.origin) or by the value of
i.source.generating.process.
Source Process                  Value of i.purchase.order.origin
- Unexpected Warehouse Receipts         tdpur.corg.wh.receipt
- RFQ                                   tdpur.corg.inquiries
- Subcontracting Purchase Order         tdpur.corg.subc.pur.order
- Subcontracting Purchase Schedule      tdpur.corg.subc.pur.sched
- Production                            tdpur.corg.sfc
- Planning                              tdpur.corg.mrp
- Purchase Payment (Pay on Use)         tdpur.corg.payment
- Price Calculation                     tdpur.corg.price.calc
- Sales                                 tdpur.corg.sls
- Warehousing                           tdpur.corg.inv
- Contract Delivery Scheme              tdpur.corg.contracts
- Service Material Cost Lines           tdpur.corg.sma
- Maintenance Work Order                tdpur.corg.wcs
Source Process                  Value of i.source.generating.process
- Sales Order Components (Kitting)      1
- Return Rejected                       2
Other generation sources can support creation of order headers
but cannot be affected by the process extension and will not
invoke the process extension because:
- LN standard creates one order and line (hard coded)
- Multiple orders may cause conflicts with current
standard behavior or maybe unwanted.
These are:
- Price Calculator
- Assembly
- List items
- Net Prices per Buy-from Business Partner
- Copy BOM
- Project (PRP Orders)
- Service Customer Claim
- Requisition
- Orders generated through external integrations: BOD/BDE/...
Output: o.purchase.order        - The purchase Order as determined
by the extension.
* non-empty:
The purchase order line will be
added to the given purchase order.
if the given purchase order does
not exist, then LN will create
a new purchase order.
* empty:
Standard logic from LN will be
used to decide which existing
purchase order (if any) will be
used to add the purchase order line
to.
Return: 0                       - Success
<> 0                    - When an error occurs in the
determination of the purchase order.
The standard logic for combining will
be applied.
```
