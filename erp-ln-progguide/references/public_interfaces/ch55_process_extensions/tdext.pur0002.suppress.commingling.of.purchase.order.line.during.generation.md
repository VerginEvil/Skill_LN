# tdext.pur0002.suppress.commingling.of.purchase.order.line.during.generation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2184-2186

```baan
Syntax: boolean tdext.pur0002.suppress.commingling.of.purchase.order.line.during.generation(
domain  tcorno           i.previous.order,
domain  tcpono           i.previous.line,
domain  tcpono           i.previous.sequence,
domain  tdpur.corg       i.origin,
domain  tcorno           i.originating.order,
domain  tcpono           i.originating.line,
domain  tcpono           i.originating.sequence,
domain  tccom.bpid       i.buy.from.business.partner,
domain  tccom.bpid       i.ship.from.business.partner,
domain  tcitem           i.item,
domain  tcuef.effn       i.effectivity.unit,
domain  tdobid           i.product.variant,
domain  tcyesno          i.subcontracted,
domain  tccwar           i.warehouse )
Usage:        Expl.:  This method can be implemented to suppress commingling during
purchase order line generation.
The standard logic in LN will first determine whether commingling
is allowed at all. If so, this process extension will then be
called to decide whether commingling must be suppressed.
Input:
i.previous.order        The previous purchase order that was
generated in this process.
If commingling is allowed then LN will
commingle the new purchase order line to
this order.
i.previous.line         The previous purchase order line that was
generated in this process.
If commingling is allowed and it is not
suppressed, then LN will commingle the
new purchase order line to this order line.
i.previous.sequence     The previous purchase order sequence
that was generated in this process.
i.origin                The origin of the new order line.
Possible values:
tdpur.corg.mrp (EP)
tdpur.corg.wcs (Maintenance)
tdpur.corg.inv (Warehousing)
tdpur.corg.contracts (Contract)
tdpur.corg.inquiries (RFQ)
tdpur.corg.eop (EDI)
tdpur.corg.manual (Manual)
tdpur.corg.sfc (Job Shop Control)
tdpur.corg.project (Project)
tdpur.corg.sls (Sales)
tdpur.corg.sma (Service)
tdpur.corg.pmg (Process)
tdpur.corg.requisition (Requisition)
tdpur.corg.asc (Assembly)
tdpur.corg.extern (External)
tdpur.corg.wh.receipt (Warehousing Receipt)
tdpur.corg.payment (Purchase Payment)
tdpur.corg.subc.pur.order (Subcontracting
Purchase Order)
tdpur.corg.subc.pur.sched (Subcontracting
Purchase Schedule)
tdpur.corg.serv.cust.claim (Service Customer
Claim)
tdpur.corg.routing (Routing)
tdpur.corg.price.calc (Price Calculation)
i.originating.order     The originating order. This field is
guaranteed to be filled in case of the
following values for i.origin:
* tdpur.corg.sls (Sales)
* tdpur.corg.inquiries (RFQ's)
* tdpur.corg.requisition (Requisition)
* tdpur.corg.subc.pur.order
(Subcontracting Purchase Order)
* tdpur.corg.price.calc (Price Calculation)
For other origins, the originating order
may be filled or not, depending on the
scenario.
i.originating.line      Originating line. May be filled or not.
See 'i.originating.order'.
i.originating.sequence  Originating sequence May be filled or not.
See 'i.originating.order'.
i.buy.from.business.partner
Buy                                              -from business partner.
i.ship.from.business.partner
Ship                                              -from business partner.
i.item                  Item
i.effectivity.unit      Effectivity Unit
i.product.variant       Product Variant
i.subcontracted         Subcontracted (Yes/No)
i.warehouse             Warehouse
Output: N.A.
Return: true                    The extension has determined that
commingling must be suppressed for the
given input.
false                   The standard logic for commingling applies.
```

## Process Extensions for PurchaseOrderLine

The following process extension(s) is/are available: PurchaseOrderLine.SkipPrint PurchaseOrderLine.SkipPrintPurchaseInvoice PurchaseOrderLine.SkipPrintPurchaseOrder PurchaseOrderLine.SkipPrintPurchaseOrderReminder PurchaseOrderLine.SkipPrintReceivableInvoice
