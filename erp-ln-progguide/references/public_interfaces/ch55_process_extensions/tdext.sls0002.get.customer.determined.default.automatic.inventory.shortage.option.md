# tdext.sls0002.get.customer.determined.default.automatic.inventory.shortage.option

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesCheckInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2215-2216

```baan
Syntax: long tdext.sls0002.get.customer.determined.default.automatic.inventory.shortage.option(
domain  tdsls.koor       i.document.type,
domain  tcorno           i.document,
domain  tcpono           i.line,
domain  tcpono           i.sequence,
domain  tcpono           i.component.sequence,
domain  tccotp           i.order.type,
domain  tcitem           i.item,
boolean          i.recheck.inventory.promised.line,
domain  tdsls.ssop
i.automatic.inventory.shortage.option.from.master.data,
ref     domain  tdsls.ssop       o.automatic.inventory.shortage.option )
Usage:        Expl:   Use this method to get a customer determined default automatic
inventory handling option from an extension. This option will be
used in 'Check Inventory for Sales Orders' (tdsls4217m000) and
any other process triggering the automatic inventory handling in
Sales.
The standard logic in LN determines the automatic inventory
shortage handling option (enumerated value of domain
tdsls.ssop) from the sales order type and is also
determined by the item and if inventory is rechecked.
Using this process extension, the defaulted value can be
changed to another option of the existing options of the domain.
As an example: the option defaulted by standard LN may be
'ATP                       - When Available' (tdsls.ssop.atp.fixed.wh). Based on logic
in the extension, this value may be overruled for specific
order lines by 'ATP                       - When Available - Single Delivery'
(tdsls.ssop.del.date).
Note:
1. The input arguments can be used to determine the option.
2. Only values from domain tdsls.ssop can be used.
3. Run time errors occur when non                      -existing enumumerated options
of domain tdsls.ssop are provided; an empty value is not
overruling the default value from the master data.
4. Standard LN logic may overrule the selected option, otherwise
standard logic may fail.
Pre:    NA
Post:   NA
Input:  i.document.type                       -       Sales Quote Line or
Sales Order Line or
Sales Order Line Component
i.document                                    -       Sales Quote or Sales Order
i.line                                        -       Sales Quote Line or
Sales Order Line
i.sequence                                    -       Sales Quote Alternative or
Sales Order Sequence
i.component.sequence                          -       Sales Order Component Line
i.order.type                                  -       Sales Order Type
i.item                                        -       Sales Quote Line Item or
Sales Order Line Item or
Sales Order Component Item
i.recheck.inventory.promised.line
-                                                     If inventory is being rechecked
(True/False)
i.automatic.inventory.shortage.option.from.master.data
-                                                     The option determined by
standard LN.
Output: o.automatic.inventory.shortage.option
-                                                     The option determined by the
extension.
Return: 0                                     -       Success
DALHOOKERROR                                  -       When an error occurs in the
determination of the inventory
option.
```
