# lpext.bra0002.get.wh.order.business.partners

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BRA.WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1994-1995

```baan
Syntax: long lpext.bra0002.get.wh.order.business.partners(
domain  whinh.oorg       i.order.origin,
domain  tcorno           i.order,
domain  tcwset           i.order.set,
domain  whinh.ittp       i.transaction.type,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence,
domain  tccom.bpid       i.ship.to.business.partner,
domain  tccom.bpid       i.invoice.to.business.partner,
ref     domain  tccom.bpid       o.custom.ship.to.business.partner,
ref     domain  tccom.bpid       o.custom.invoice.to.business.partner )
Usage:        Expl:   Use this method to get a ship-to and invoice-to business
partners from a warehouse order. These business partners
are used to check if shipment or receipt generates a
fiscal document or fiscal receipt respectively.
Some warehouse order order origin can set ship-to business
partner in warehouse order header. Other order types are
searched. Business partner can be set by the following
scenarios:
1 - Ship-to business partner is set in warehouse order header.
2 - It is search ship-to and invoice-to business partner
based on order origin.
3 - The custom business partner search is defined by this process
extension.
In standard, the business partners are retrieved from the
warehouse order header or other search logic.
Those found business partners can be overruled by the
business partners returned in this process extension.
----------------------------------------------------------------
Start of Example of Implementation
Pseudocode:
In code below it will get a business partner from
Order Origin equal project or project (manual) and
Transaction Type Issue or Receipt.
Hook: Declarations
boolean         found.set
tt.init.vars(   o.custom.ship.to.business.partner,
o.custom.invoice.to.business.partner)
found.set = false
on case i.order.origin
case whinh.oorg.project:
case whinh.oorg.project.man:
on case i.transaction.type
case whinh.ittp.issue:
| Set o.custom.ship.to.business.partner and
| o.custom.invoice.to.business.partner for
| Project or Project (manual) Issue.
break
case whinh.ittp.receipt:
| Set o.custom.ship.to.business.partner and
| o.custom.invoice.to.business.partner for
| Project or Project (manual) Receipt.
break
endcase
if not isspace(o.custom.ship.to.business.partner) and
not isspace(o.custom.invoice.to.business.partner) then
found.set = true
endif
break
endcase
if found.set then
return(0)
endif
End of Example of Implementation
----------------------------------------------------------------
Pre:    n.a.
Post:   n.a.
Input:  i.order.origin                  - Order Origin
i.order                         - Order number
i.order.set                     - Order header set
i.order.line                    - Order line
i.order.sequence                - Order line sequence
i.ship.to.business.partner      - Ship-to BP retrieved by
Standard.
i.invoice.to.business.partner   - Invoice-to BP retrieved by
Standard.
Output: o.ship.to.business.partner
o.invoice.to.business.partner
Return: long                            - If not zero, the results of
this process extension
will not be used.
```
