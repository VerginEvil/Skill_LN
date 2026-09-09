# tdext.sls0006.sales.order.determine.supplier.for.direct.delivery

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2244-2245

```baan
Syntax: long tdext.sls0006.sales.order.determine.supplier.for.direct.delivery(
domain  tccwoc           i.sales.office,
domain  tccom.bpid       i.sold.to.bp,
domain  tccom.bpid       i.ship.to.bp,
domain  tcitem           i.item,
domain  tcdate           i.search.date,
domain  tccom.bpid       i.buy.from.bp.from.standard.logic,
domain  tccom.bpid       i.ship.from.bp.from.standard.logic,
ref     domain  tccom.bpid       o.buy.from.bp,
ref     domain  tccom.bpid       o.ship.from.bp )
Usage:        Expl:   This method allows for custom logic to be implemented when
determining the supplier for a sales order in a direct delivery
scenario.
The method is invoked at various stages, not just during the
generation of the direct delivery purchase order line. For
example, it is also called when inserting or modifying a sales
order line to ensure that the correct tax values are applied.
The method provides flexibility in how business partners are
determined:
* If only a buy-from business partner is returned, then LN
will attempt to find a default ship-from business partner
associated with that buy-from business partner.
* If only a ship-from business partner is returned, LN will
try to locate a default buy-from business partner linked to
that ship-from business partner.
If no default was found in either of the 2 situations above, LN
will revert to its standard logic to determine the supplier.
In cases where:
* The extension returns a non-zero return-value, or
* Both the buy-from and ship-from fields are left empty, or
* One of the business partners is not present in the database,
LN will automatically fall back to the standard supplier
determination logic.
Pre:    Not Applicable.
Post:   Not Applicable.
Input:  i.sales.office          - Sales Office
i.sold.to.bp            - Sold-to Business Partner
i.ship.to.bp            - Ship-to Business Partner
i.item                  - Item
i.search.date           - Search Date
i.buy.from.bp.from.standard.logic
- The Buy-from Business Partner as
determined under standard logic.
i.ship.from.bp.from.standard.logic
- The Ship-from Business Partner as
determined under standard logic.
Output: o.buy.from.bp           - The Buy-from Business Partner as
determined by the extension.
* non-empty:
if the given buy-from business
partner does not exist, then LN
will use standard logic to
determine the supplier.
* empty:
If only a ship-from business
partner is returned, LN will
try to locate a default buy-from
business partner linked to
that ship-from business partner.
o.ship.from.bp          - The Ship-from Business Partner as
determined by the extension.
* non-empty:
if the given ship-from business
partner does not exist, then LN
will use standard logic to
determine the supplier.
* empty:
If only a buy-from business
partner is returned, then LN
will attempt to find a default
ship-from business partner
associated with that buy-from
business partner.
Return: 0                       - Success
<> 0                    - When an error occurs in the
determination of the supplier.
LN will use the standard logic
to determine the supplier.
```
