# tdext.sls0004.determine.sales.order.for.combining.order.lines.during.generation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2252-2254

```baan
Syntax: long tdext.sls0004.determine.sales.order.for.combining.order.lines.during.generation(
domain  tcorno           i.sales.order,
domain  tcpono           i.sales.order.line,
domain  tdsls.corg       i.sales.order.origin,
long             i.source.generating.process,
ref     domain  tcorno           o.sales.order )
Usage:        Expl:   This method can be implemented to get a customer determined
sales order that will be used when generating sales order lines.
If this extension returns a sales order, then that sales order
will be used to add the new sales order line to.
Note that after calling this extension, LN will also consider
the extension SalesOrderGenerate.SuppressCombiningOrderLines.
If implemented, that extension could prevent combining the
order line.
If the extension returns a sales order that is cancelled, closed
or not updatable, then an error is returned during generation.
This extension is implemented for multiple sales order generation
processes. See below.
Input:  i.sales.order           - Sales Order (Optional)
If filled, this can refer to either
the sales order that would be used by
the standard logic, or it refers to a
sales order series. In the latter case,
LN would generate a new sales order.
If empty, LN standard logic would
generate a new sales order.
i.sales.order.line      - Sales Order Line (Optional)
If filled, this refers to the sales order
line that would be used by standard
logic; LN would create a new detail-
line.
i.sales.order.origin    - Sales Order Origin (tdsls400.corg)
i.source.generating.process
- Indicates the source process from /
for which the sales order is generated
and where an order header can be
created.
The following generation sources can support creation of
multiple order headers and can be affected by the process
extension:
Source Process                  Value of
i.source.generating.process
- Quote                                 1
- Retro-Billing                         10
- Contract Delivery Scheme              12
- Template                              14
- Subcontracting Purchase Order         15
- Sales Transfer                        17
- Price Calculation                     30
- Received Customer Order               31
Other generation sources can support creation of order headers
but cannot be affected by the process extension and will not
invoke the process extension because:
- LN standard creates one order and line (hard coded)
- Multiple orders may cause conflicts with current
standard behavior or maybe unwanted.
These are:
- Return Rejected
- Direct Delivery from Procurement
- Consumption (Cons. Inv.)
- Copy Template
- Schedule Return
- Price Calculator
- Shipment Additional Costs
Output: o.sales.order           - The sales Order as determined
by the extension.
* non-empty:
The sales order line will be
added to the given sales order.
if the given sales order does
not exist, then LN will create
a new sales order.
* empty:
Standard logic from LN will be
used to decide which existing
sales order (if any) will be
used to add the sales order line
to.
Return: 0                       - Success
<> 0                    - When an error occurs in the
determination of the sales order.
The standard logic for combining will
be applied.
```
