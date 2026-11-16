# tdext.sls0003.suppress.combining.sales.order.lines.during.generation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2254-2255

```baan
Syntax: boolean tdext.sls0003.suppress.combining.sales.order.lines.during.generation(
domain  tcorno           i.sales.order,
domain  tcpono           i.sales.order.line,
domain  tdsls.corg       i.sales.order.origin,
long             i.source.generating.process )
Usage:        Expl.:  This method can be implemented to suppress combining sales
order lines on the same sales order during generation.
The standard logic in LN will first determine whether combining
is allowed at all. If so, this process extension will then be
called to decide whether combining must be suppressed.
When this method is called, the following applies:
- i.sales.order is always filled;
- i.sales.order.line can be zero or > zero
- A record of tdsls400 is current.
Input:  i.sales.order           - Sales Order
i.sales.order.line      - Sales Order Line
Note that the sequence cannot be input
for the order generation process.
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
Output: Not Applicable.
Return: True                    - The extension has determined that
combining must be suppressed for the
given input.
False                   - The standard logic for combining
applies.
```
