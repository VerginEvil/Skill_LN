# cpext.rrp0002.before.plan.item

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2099-2099

```baan
Syntax: long cpext.rrp0002.before.plan.item(
domain  tcncmp           i.company,
domain  cpcom.plnc       i.scenario,
domain  cpcom.phnu       i.phase.number,
domain  cpitem           i.plan.item )
Usage:        Expl:   This function is called in the context of Generate Order Planning,
just before the execution starts for a plan item.
It can be called from session Generate Order Planning (cprrp1210m000),
Generate Order Planning (Item) (cprrp1220m000) and Public Interface
"ItemOrderPlan.Generate".
Implementation example:
function extern long cpext.rrp0002.before.plan.item(
domain  tcncmp          i.company,
domain  cpcom.plnc      i.scenario,
domain  cpcom.phnu      i.phase.number,
domain  cpitem          i.plan.item)
{
|* Check if custom processing is needed
if requires.custom.processing(i.plan.item) then
prepare.item.data(i.company, i.plan.item)
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.company       - Company
i.scenario      - Scenario
i.phase.number  - Phase Number
i.plan.item     - Plan Item
Output: N.A
Return: 0               - Success
```
