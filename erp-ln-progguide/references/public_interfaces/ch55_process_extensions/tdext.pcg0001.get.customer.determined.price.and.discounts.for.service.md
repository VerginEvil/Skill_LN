# tdext.pcg0001.get.customer.determined.price.and.discounts.for.service

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2146-2151

```baan
Syntax: long tdext.pcg0001.get.customer.determined.price.and.discounts.for.service(
domain  tdpcg.tyor       i.type.of.order,
domain  tcorno           i.number,
long             i.price.search.method,
domain  tccwoc           i.office,
domain  tcsite           i.site,
domain  tcqrd1           i.quantity.in.piece.unit,
domain  tccuni           i.piece.unit,
domain  tcconv           i.piece.unit.conv.factor,
domain  tcitem           i.item,
domain  tcatse           i.attribute.set,
domain  tccom.bpid       i.sold.to.bp,
domain  tccom.bpid       i.ship.to.bp,
domain  tccom.bpid       i.invoice.to.bp,
domain  tccom.bpid       i.invoice.from.bp,
domain  tccom.bpid       i.pricing.bp,
domain  tdsls.corg       i.sales.order.origin,
domain  tccwoc           i.service.office,
domain  tccplt           i.price.list,
domain  tcpaym           i.payment.method,
domain  tccdec           i.terms.of.delivery,
domain  tcmcs.chan       i.bp.channel,
domain  tcctyp           i.product.type,
domain  tcmcs.cpln       i.product.line,
domain  tcmcs.cpcl       i.product.class,
domain  tcmcs.cmnf       i.manufacturer,
domain  tccprg           i.price.group,
domain  tccitg           i.item.group,
domain  tdpcg.pror       i.price.origin,
domain  tcmcs.cbtp       i.sold.to.type,
domain  tccreg           i.area,
domain  tccotp           i.service.type,
domain  tcbsc.clst       i.service.installation.group,
domain  tcitem           i.service.maintained.item,
domain  tcibd.sern       i.service.maintained.serial,
domain  tccreg           i.service.area,
domain  tcacm.cact       i.service.reference.activity,
domain  tcacm.cact       i.service.master.routing,
domain  tcacm.cact       i.service.routing.option,
domain  tccitg           i.service.item.group,
domain  tccitg           i.service.serialized.item.group,
domain  tcmdm.cotp       i.service.cost.type,
domain  tcorno           i.service.contract,
domain  tcpono           i.service.contract.change,
domain  tcpono           i.service.configuration.line,
domain  tcdate           i.service.coverage.time,
domain  tccotp           i.service.coverage.type,
domain  tccpcp           i.service.cost.component,
domain  tccom.bpid       i.service.subcontractor,
domain  tcccur           i.currency,
domain  tcncmp           i.financial.company,
ref     domain  tcratc           i.rate(),
ref     domain  tcratf           i.rate.factor(),
domain  tcdate           i.rate.date,
domain  tcrtyp           i.rate.type,
boolean          i.delete.manual.discount,
boolean          i.delete.pricebook.discount,
domain  tdpcg.prds       i.apply.price.disc.both,
domain  tcdate           i.order.date,
domain  tcdate           i.delivery.date,
domain  tcqsl1           i.order.quantity,
domain  tcqsl1           i.price.group.quantity,
domain  tccuni           i.quantity.unit,
domain  tcconv           i.quan.unit.conv.factor,
domain  tccuni           i.price.unit.from.standard.logic,
domain  tcconv           i.price.unit.conv.factor.from.standard.logic,
domain  tcpric           i.price.from.standard.logic,
domain  tcbool           i.derived.item.used.from.standard.logic,
domain  tdpcg.prbk       i.price.book.from.standard.logic,
domain  tcprsg           i.price.stage.from.standard.logic,
domain  tdgen.porg       i.price.origin.from.standard.logic,
domain  tdpcg.made       i.price.matrix.definition.from.standard.logic,
domain  tdpcg.prse       i.price.matrix.sequence.from.standard.logic,
const   domain  tdpcg.maty       i.disc.matrix.type.from.standard.logic(),
const   domain  tdgen.dorg       i.discount.origin.from.standard.logic(),
const   domain  tdpcg.made       i.disc.matrix.definition.from.standard.logic()
fixed,
const   domain  tdpcg.prse       i.disc.matrix.sequence.from.standard.logic(),
const   domain  tcdisc           i.discount.percentage.from.standard.logic(),
const   domain  tddiam           i.discount.amount.from.standard.logic(),
const   domain  tccdsc           i.discount.code.from.standard.logic() fixed,
const   domain  tddmth           i.discount.method.from.standard.logic(),
const   domain  tdpcg.dssc       i.discount.schedule.from.standard.logic() fixed,
domain  tcyesno          i.determining.from.standard.logic,
domain  tcyesno          i.eligible.from.standard.logic,
ref     domain  tccuni           o.price.unit,
ref     domain  tcconv           o.price.unit.conv.factor,
ref     domain  tcpric           o.price,
ref     domain  tcbool           o.derived.item.used,
ref     domain  tdpcg.prbk       o.price.book,
ref     domain  tcprsg           o.price.stage,
ref     domain  tdgen.porg       o.price.origin,
ref     domain  tdpcg.made       o.price.matrix.definition,
ref     domain  tdpcg.prse       o.price.matrix.sequence,
ref     domain  tdpcg.maty       o.disc.matrix.type(),
ref     domain  tdgen.dorg       o.discount.origin(),
ref     domain  tdpcg.made       o.disc.matrix.definition() fixed,
ref     domain  tdpcg.prse       o.disc.matrix.sequence(),
ref     domain  tcdisc           o.discount.percentage(),
ref     domain  tddiam           o.discount.amount(),
ref     domain  tccdsc           o.discount.code() fixed,
ref     domain  tddmth           o.discount.method(),
ref     domain  tdpcg.dssc       o.discount.schedule() fixed,
ref     domain  tcyesno          o.determining,
ref     domain  tcyesno          o.eligible,
ref             boolean          o.fallback.to.standard.logic.in.case.of.errors )
Usage:        Expl:   This function gets the customer determined price and discounts
from an extension, if applicable. The function is called in
some flows where price-retrieval is initiated from the Service
package.
The price and discounts are only retrieved and used if:
- Method
'tdext.pcg0001.get.customer.determined.price.and.discounts.for.service'
is implemented for Process Extension
Pricing.RetrievePriceAndDiscounts (tdpcg.retrieve.price.and.disc).
- No errors are found during executing the extension.
If the extension returns a zero price and/or zero discounts,
these will be treated as valid prices and discounts. If that's
not desired, then the extension should return an error in those
cases.
Pre:    NA
Post:   NA
Input:  i.type.of.order
- The type of order being processed. Possible values:
tdpcg.tyor.sr:          General Service
tdpcg.tyor.sr.quote:    Service Quote
tdpcg.tyor.sr.msc:      Maintenance Sales Order
tdpcg.tyor.sr.soc:      Service Order
i.number
- The "Order Number".
This depends on the Type of Order (i.type.of.order):
tdpcg.tyor.sr:          "" (empty string)
tdpcg.tyor.sr.quote:    Service Quote
tdpcg.tyor.sr.msc:      Maintenance Sales Order
tdpcg.tyor.sr.soc:      Service Order
i.price.search.method   -
- The Search Method. Possible values:
1:                      Price Books Service
2:                      Price Books Service/Sales
3:                      Item Service Prices
4:                      Price Books Sales/Service
i.office                        The office used for e.g. reading
Office specific settings
i.site  -                       Site
i.quantity.in.piece.unit        The quantity in Piece Unit.
Only used in Dimension Controlled
scenarios.
i.piece.unit                    Unit in which the quantity
is expressed.
i.piece.unit.conv.factor        Conversion factor from quantity
units to inventory unit
i.item                          Item (Mandatory)
i.attribute.set                 Attribute Set
i.sold.to.bp                    Sold-to Business Partner (Mandatory)
i.ship.to.bp                    Ship-to Business Partner (Mandatory)
i.invoice.to.bp                 Invoice-to Business Partner
(Mandatory)
i.invoice.from.bp               Invoice-from Business Partner
i.pricing.bp                    Parent Business Partner for
Prices and Discounts
i.sales.order.origin            Sales Order Origin.
Value: tdsls.corg.service
i.service.office                Service Office (Mandatory)
i.price.list                    Price List (Mandatory)
i.payment.method                Payment Method
i.terms.of.delivery             Terms of Delivery
i.bp.channel                    BP Channel
i.product.type                  Product Type
i.product.line                  Product Line
i.product.class                 Product Class
i.manufacturer                  Manufacturer
i.price.group                   Price Group (Mandatory)
i.item.group                    Item Group (Mandatory)
i.price.origin                  Price Origin
Value: empty
i.sold.to.type                  Sold-to business partner type
i.area                          Area
i.service.type                  Service Type
i.service.installation.group    Maintained Installation Group
i.service.maintained.item       Maintained Item
i.service.maintained.serial     Maintained Serial
i.service.area                  Service Area
i.service.reference.activity    Reference Activity
i.service.master.routing        Master Routing
i.service.routing.option        Routing Option
i.service.item.group            The service item group of the
material line item
i.service.serialized.item.group The serialized item group of the
material line item
i.service.cost.type             Cost Type. Possible values:
tcmdm.cotp.material     Material
tcmdm.cotp.other        Other
tcmdm.cotp.subcon       Subcontracting
i.service.contract              Service Pricing Contract
i.service.contract.change       Contract Change
i.service.configuration.line    Contract Line
i.service.coverage.time         Coverage Time
i.service.coverage.type         Coverage Type
i.service.cost.component        Cost Component
i.service.subcontractor         Subcontractor
i.currency                      Currency (Mandatory)
i.financial.company             Financial Company of the
Department
i.rate                          Exchange Rate
i.rate.factor                   Exchange Rate Factor
i.rate.date                     Rate Date
i.rate.type                     Rate Type
i.delete.manual.discount        Delete Manual Discounts.
This parameter decides whether
the manual discounts will be
removed before retrieving
structure discounts
i.delete.pricebook.discount     Delete Price Book Discount.
This parameter decides whether
the discount derived from a Price
Book Discount Schedule will be
removed before retrieving
structure discounts.
i.apply.price.disc.both         Price/Discount/Both: this
decides whether to search
a Price only, Discounts only, or
both Price and Discounts.
Possible values:
tdpcg.prds.prc          Pricing Only
tdpcg.prds.dsc          Discounting Only
tdpcg.prds.both         Both
i.order.date                    Order Date
i.delivery.date                 Delivery Date
i.order.quantity                Ordered Quantity
i.price.group.quantity          Price Group Quantity: This
quantity is filled with the
aggregated quantities of the
Order Lines with Items that have
the same Price Group. It is used
to apply Cumulative Price Group
Discounts.
i.quantity.unit                 Quantity Unit
i.quan.unit.conv.factor         Quantity Unit Conversion Factor
i.price.unit.from.standard.logic                As determined under
standard logic
i.price.unit.conv.factor.from.standard.logic    As determined under
standard logic
i.price.from.standard.logic                     As determined under
standard logic
i.derived.item.used.from.standard.logic         As determined under
standard logic
i.price.book.from.standard.logic                As determined under
standard logic
i.price.stage.from.standard.logic               As determined under
standard logic
i.price.origin.from.standard.logic              As determined under
standard logic
i.price.matrix.definition.from.standard.logic   As determined under
standard logic
i.price.matrix.sequence.from.standard.logic     As determined under
standard logic
Arrays below have been
allocated
with 11 elements.
i.disc.matrix.type.from.standard.logic(11)      As determined under
standard logic
i.discount.origin.from.standard.logic(11)       As determined under
standard logic
i.disc.matrix.definition.from.standard.logic(11) As determined under
standard logic
i.disc.matrix.sequence.from.standard.logic(11)  As determined under
standard logic
i.discount.percentage.from.standard.logic(11)   As determined under
standard logic
i.discount.amount.from.standard.logic(11)       As determined under
standard logic
i.discount.code.from.standard.logic(11)         As determined under
standard logic
i.discount.method.from.standard.logic(11)       As determined under
standard logic
i.discount.schedule.from.standard.logic(11)     As determined under
standard logic
i.determining.from.standard.logic               As determined under
standard logic
i.eligible.from.standard.logic                  As determined under
standard logic
Output: o.price.unit                    Price Unit
o.price.unit.conv.factor        Conversion factor from Price Unit
to inventory unit
o.price                         Unit Price
o.derived.item.used             The derived from item was used
to retrieve the price (True/
False).
o.price.book                    Price Book
o.price.stage                   Price Stage
o.price.origin                  Price Origin
o.price.matrix.definition       Price Matrix Definition
o.price.matrix.sequence         Price Matrix Sequence
Arrays below have been allocated
with 11 elements.
o.disc.matrix.type              Discount Matrix Type array
o.discount.origin               Discount Origin array
o.disc.matrix.definition        Discount Matrix Definition array
o.disc.matrix.sequence          Discount Matrix Sequence array
o.discount.percentage           Discount Percentage array
o.discount.amount               Discount Amount array
o.discount.code                 Discount Code array
o.discount.method               Discount Method array
o.discount.schedule             Discount Schedule array
o.determining                   Determining (Yes/No)
o.eligible                      Eligible (Yes/No)
o.fallback.to.standard.logic.in.case.of.errors
True:   When an error is returned
by the extension, then LN
will use the outcome of
the LN standard logic.
False:  Errors in the extension
are returned as-is to LN.
Output variables are
initialized to 0/empty/""
Return: 0                               Success
<> 0                            An error occurred
```
