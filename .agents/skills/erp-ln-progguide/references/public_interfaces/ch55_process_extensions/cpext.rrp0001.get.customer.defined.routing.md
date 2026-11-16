# cpext.rrp0001.get.customer.defined.routing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for OrderPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2111-2112

```baan
Syntax: long cpext.rrp0001.get.customer.defined.routing(
domain  tirou.opro       i.routing,
domain  tcqiv2           i.order.quantity,
domain  tcitem           i.item,
domain  tcuef.effn       i.effectivity.unit,
ref     domain  tirou.opro       o.routing )
Usage:        Expl:   Use this method to get a customer defined routing from
an extension. This custom routing will override the routing
while Generate Order Planning(cprrp1210m000).
This process extension only works when Sites concept
is not active.
Note:
1)      If this function returns an empty string in o.routing,
then LN will use the standard routing(i.routing).
External variables available for use by this process extension
function:
- proc_ext_ord_plan_rou_cluster
[type: domain tcemm.clus]
Planning cluster for which the routing is determined.
Example:
o.routing = ""
|* Read custom routing based on item, routing, quantity
custom.routing = get.alternative.routing(
i.item,
i.routing,
i.order.quantity)
if not isspacce(custom.routing) then
o.routing = custom.routing
endif
return(0)
Pre:    NA
Post:   NA
Input:  i.routing               - Routing
i.order.quantity        - Order Quantity
i.item                  - Item
i.effectivity.unit      - Effectivity Unit
Output: o.routing               - Custom Routing
Return: 0                       - Success
```
