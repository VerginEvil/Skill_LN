# tdext.sls0009.determine.additional.cost.set

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2209-2212

```baan
Syntax: long tdext.sls0009.determine.additional.cost.set(
const           long             i.input.option.set,
domain  tdsls.ccos       i.additional.cost.set.from.standard.logic,
ref     domain  tdsls.ccos       o.additional.cost.set )
Usage:        Expl:   Use this process extension to determine the additional cost set
that must be used in the sales process.
The extension is invoked after the standard logic has determined
the additional cost set. The standard result is passed via
i.additional.cost.set.from.standard.logic, allowing the
extension to inspect it and either accept, modify, or replace it.
The context of the call (sales order, shipment, or price
calculation) is passed via the Processing Option Set
i.input.option.set. Read it using ProcessingOptionSet.Read()
in DLL tcextextapi.
Pseudocode:
|* Read the context
ret = ProcessingOptionSet.Read(
i.input.option.set,
my.exception.message,
my.exception.id,
|* option name                          option                      -variable
default
"SalesOrder",                           sales.order,
"",
"Shipment",                             shipment,
"",
"PriceCalculation",                     price.calculation,
"",
"Line",                                 line,                           0,
"Sequence",                             sequence,                       0,
"SalesOffice",                          sales.office,
"",
"PriceList",                            price.list,
"",
"SoldToBusinessPartner",                sold.to.bp,
"",
"ShipToBusinessPartner",                ship.to.bp,
"",
"Item",                                 item,
"",
"Site",                                 site,
"",
"CollectOrder",                         collect.order,
tcyesno.no,
"UserInteractionAllowed",               user.interaction.allowed,
false,
"EDIBatch",                             edi.batch,
false)
if <some.condition> then
|* Return the standard result unchanged
o.additional.cost.set =
i.additional.cost.set.from.standard.logic
return(0)
endif
|* Return a customer                              -determined cost set
o.additional.cost.set = <customer.determined.cost.set>
return(0)
Pre:    N.A.
Post:   N.A.
Input:  i.input.option.set                    - Processing Option Set containing the
context in which the additional cost
set is being determined.
Read via ProcessingOptionSet.Read()
in DLL tcextextapi.
Supported Processing Options and their type:
NAME                            TYPE
SalesOrder                      domain  tcorno
Shipment                        domain  tcshpm
PriceCalculation                domain  tcorno
Line                            domain  tcpono
Sequence                        domain  tcpono
SalesOffice                     domain  tccwoc
PriceList                       domain  tccplt
SoldToBusinessPartner           domain  tccom.bpid
ShipToBusinessPartner           domain  tccom.bpid
Item                            domain  tcitem
Site                            domain  tcsite
CollectOrder                    domain  tcyesno
UserInteractionAllowed                  boolean
EDIBatch                                boolean
Explanation for some of the supported Processing Options:
Line
-                                               The meaning depends on the context
in which the additional cost set is
retrieved:
* Sales Order context:
Line refers to the sales order line.
* Shipment context:
Line refers to the shipment line.
* Price Calculation context:
Line refers to the price calculation
line.
See also Sequence.
Sequence
-                                               Belongs to the same context as Line.
CollectOrder
-                                               Can only be Yes in Sales Order
context.
UserInteractionAllowed
-                                               true:  questions may be asked.
-                                               false: no user interaction allowed.
EDIBatch
-                                               true:  triggered from an EDI batch
process.
-                                               false: not an EDI batch process.
i.additional.cost.set.from.standard.logic
-                                               The additional cost set as determined
by the standard logic.
Empty if standard logic did not find
a cost set.
Note: This argument is passed directly,
not via the Processing Option Set.
Output: o.additional.cost.set                 - The additional cost set as determined
by the extension.
* non                                                -empty:
The returned cost set will be used.
* empty:
No cost set will be used, even if
the standard logic yielded a
non                                                  -empty cost set.
Return: 0                                     - Success.
<> 0                                          - When an error occurs.
LN will fall back to standard logic.
```
