# tdext.pcg0001.get.customer.determined.price.and.discounts

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2118-2123

```baan
Syntax: long tdext.pcg0001.get.customer.determined.price.and.discounts(
domain  tdpcg.tyor       i.type.of.order,
domain  tcorno           i.number,
domain  tccono           i.contract,
domain  tcpono           i.contract.line,
domain  tccwoc           i.contract.office,
domain  tcpono           i.contract.sequence,
domain  tcitem           i.item,
domain  tccwoc           i.office,
domain  tcsite           i.site,
domain  tcncmp           i.logistic.company,
domain  tcyesno          i.subcontracted,
domain  tcuef.effn       i.effectivity.unit,
domain  tccpva           i.product.variant,
domain  tcolid           i.option.list.id,
domain  tccom.bpid       i.buy.sell.bp,
domain  tccom.bpid       i.ship.bp,
domain  tccom.bpid       i.pricing.bp,
domain  tcmcs.cpcl       i.product.class,
domain  tcmcs.cpln       i.product.line,
domain  tcmpnr           i.manufacturer.part.number,
domain  tcmcs.cmnf       i.manufacturer,
domain  tcdate           i.order.date,
domain  tcdate           i.planned.delivery.date,
domain  tcqsl1           i.order.quantity,
domain  tcqsl1           i.original.order.quantity,
domain  tcqsl1           i.price.group.quantity,
domain  tccuni           i.quantity.unit,
domain  tcconv           i.quantity.unit.conversion.factor,
boolean          i.delete.manual.discount,
boolean          i.delete.pricebook.discount,
domain  tdpcg.prds       i.apply.price.discount.both,
domain  tdpcg.prpc       i.price.percentage,
boolean          i.update.uef,
boolean          i.update.pcf,
domain  tcncmp           i.financial.company,
domain  tcccur           i.transaction.currency,
ref     domain  tcratc           i.rate(),
ref     domain  tcratf           i.rate.factor(),
domain  tcdate           i.rate.date,
domain  tcrtyp           i.rate.type,
domain  tdpcg.prit       i.price.type,
domain  tcorno           i.production.order,
domain  tcorno           i.maintenance.work.order,
domain  tcorno           i.service.order,
domain  tcmcs.chan       i.channel,
domain  tccdec           i.delivery.terms,
domain  tdpcg.pror       i.default.price.book,
domain  tccuni           i.price.unit.from.standard.logic,
domain  tcconv           i.price.unit.conv.factor.from.standard.logic,
domain  tcpric           i.price.from.standard.logic,
domain  tcperc           i.percentage.from.standard.logic,
boolean          i.derived.item.used.from.standard.logic,
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
ref     domain  tcperc           o.percentage,
ref             boolean          o.derived.item.used,
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
from an extension, if applicable.
The price and discounts are only retrieved and used if:
-                       Process Extension Pricing.RetrievePriceAndDiscounts
(tdpcg.retrieve.price.and.disc) is implemented;
-                       No errors are found during executing the extension.
If the extension returns a zero price and/or zero discounts,
these will be treated as valid prices and discounts. If that's
not desired, then the extension should return an error in those
cases.
Pre:    NA
Post:   NA
Input:
i.type.of.order
-                               The type of order being processed. Possible values:
tdpcg.tyor.so:          Sales Orders
tdpcg.tyor.sq:          Quotations
tdpcg.tyor.po:          Purchase Orders
tdpcg.tyor.pq:          RFQ's
tdpcg.tyor.gs:          General Sales
tdpcg.tyor.gp:          General Purchase
tdpcg.tyor.sr:          General Service
tdpcg.tyor.sr.quote:    Service Quote
tdpcg.tyor.sr.msc:      Maintenance Sales Order
tdpcg.tyor.sr.soc:      Service Order
i.number
-                               The "Order Number".
This depends on the Type of Order (i.type.of.order):
tdpcg.tyor.so:          Sales Order
tdpcg.tyor.sq:          Quotation Number
tdpcg.tyor.po:          Purchase Order
tdpcg.tyor.pq:          RFQ
tdpcg.tyor.gs:          "" (empty string)
tdpcg.tyor.gp:          "" (empty string)
tdpcg.tyor.sr:          "" (empty string)
tdpcg.tyor.sr.quote:    Service Quote
tdpcg.tyor.sr.msc:      Maintenance Sales Order
tdpcg.tyor.sr.soc:      Service Order
i.contract                      The contract that is linked to
the purchase or sales order line
i.contract.line                 The contract line that is linked
to the purchase or sales order line
i.contract.office               The contract office
i.contract.sequence             The contract sequence to which
the purchase order line is linked
i.item                          Item
i.office                        The office used for e.g. reading
Office specific settings
i.site                          Site
i.logistic company              Logistic Company
i.subcontracted                 Subcontracted order line (Yes/No).
Only for Purchase Order Lines
i.effectivity.unit              Effectivity unit
i.product.variant               Product Variant from the order line
i.option.list.id                Option list id from the order line
i.buy.sell.bp                   Purchase: buy                      -from business partner
Sales: sold                                                      -to business partner
i.ship.bp                       Purchase: ship                      -from business partner
Sales: ship                                                      -to business partner
i.pricing.bp                    Parent Business Partner for
Prices and Discounts.
i.product.class                 Product Class
i.product.line                  Product Line
i.manufacturer.part.number      Manufacturer Part Number
i.manufacturer                  Manufacturer
i.order.date                    Order date from the line.
i.planned.delivery.date         Planned delivery date from line
i.order.quantity                Total order quantity from line.
i.original.order.quantity       Original order quantity of line.
In add mode, this is zero. In
edit mode this is set to the
quantity before the line was
edited.
i.price.group.quantity          Quantity used to apply
discounts for 'like' price
groups.
i.quantity.unit                 Unit in which the quantity is
expressed
i.quantity.unit.conversion.factor
Conversion factor from quantity
units to inventory unit
i.delete.manual.discount        Delete manual discounts (True/
False).
i.delete.pricebook.discount     Delete discount applied from
the price book (True/False).
i.apply.price.discount.both     Apply a price, apply the
discounts or both.
i.price.percentage              Retrieve a price or a
percentage
i.update.uef                    Update Total Upgrade Price in
UEF or retrieve UEF Total
Upgrade Price.
i.update.pcf                    Update Price Structure in PCF or
retrieve PCF price.
i.financial.company             Financial company (Belongs to
sales / purchase office.
i.transaction.currency          Transaction currency.
i.rate                          Exchange rate array.
i.rate.factor                   Rate factor array.
i.rate.date                     Rate date
i.rate.type                     Rate type
i.price.type                    Price Type; possible values:
Not Applicable
Buying
Item Subcontracting
Operation Subcontracting
Service Subcontracting
i.production.order              Linked production order
i.maintenance.work.order        Linked work order
i.service.order                 Linked service order
i.channel                       Channel (Sales order only)
i.delivery.terms                Delivery Terms (Sales order only)
i.default.price.book            Default Price Book; possible values:
Sales
Service
i.price.unit.from.standard.logic                As determined under
standard logic
i.price.unit.conv.factor.from.standard.logic    As determined under
standard logic
i.price.from.standard.logic                     As determined under
standard logic
i.percentage.from.standard.logic                As determined under
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
Output:
o.price.unit                    Price Unit
o.price.unit.conv.factor        Conversion factor from Price Unit
to inventory unit
o.price                         Unit Price
o.percentage                    Percentage
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
o.disc.matrix.type(11)          Discount Matrix Type array
o.discount.origin(11)           Discount Origin array
o.disc.matrix.definition(11)    Discount Matrix Definition array
o.disc.matrix.sequence(11)      Discount Matrix Sequence array
o.discount.percentage(11)       Discount Percentage array
o.discount.amount(11)           Discount Amount array
o.discount.code(11)             Discount Code array
o.discount.method(11)           Discount Method array
o.discount.schedule(11)         Discount Schedule array
o.determining                   Determining (Yes/No)
o.eligible                      Eligible (Yes/No)
o.fallback.to.standard.logic.in.case.of.errors
True:   When an error is returned
by the extension, then LN
will use the outcome of
the LN standard logic.
False:  Errors in the extension
are returned as                                                            -  is to LN.
Output variables are
initialized to 0/empty/""
Return: 0                               Success
<> 0                            An error occurred
```
