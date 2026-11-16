# tdext.pur0003.suppress.combining.of.purchase.order.lines.to.existing.order.during.generation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2201-2202

```baan
Syntax: boolean
tdext.pur0003.suppress.combining.of.purchase.order.lines.to.existing.order.during.generati
on(
domain  tcorno           i.purchase.order,
domain  tcpono           i.purchase.order.line,
domain  tdpur.corg       i.purchase.order.origin,
long             i.source.generating.process )
Usage:        Expl.:  Use this method to suppress combining purchase order lines on
the same purchase order during generation.
The standard logic in LN will first determine whether combining
is allowed at all. If so, this method will then be called to
decide whether combining must be suppressed.
When this method is called, the following applies:
- i.purchase.order is always filled;
- i.purchase.order.line can be zero or > zero
- A record of tdpur400 is current.
Input:  i.purchase.order        - Purchase Order
This refers to the purchase
order that would be used by the
standard logic.
i.purchase.order.line   - Purchase Order Line
Note that the sequence cannot be input
for the order generation process.
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
Output: Not Applicable.
Return: True                    - The extension has determined that
combining must be suppressed for the
given input.
False                   - The standard logic for combining
applies.
```
