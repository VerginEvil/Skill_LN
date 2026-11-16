# cpext.rrp0002.before.phase.number

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2098-2099

```baan
Syntax: long cpext.rrp0002.before.phase.number(
domain  tcncmp           i.company,
domain  cpcom.plnc       i.scenario,
domain  cpcom.phnu       i.phase.number )
Usage:        Expl:   This function is called in the context of Generate Order Planning,
just before the execution starts for a specific order phase number.
It can be called from session Generate Order Planning (cprrp1210m000),
Generate Order Planning (Item) (cprrp1220m000) and Public Interface
"ItemOrderPlan.Generate".
Implementation example:
function extern long cpext.rrp0002.before.phase.number(
domain  tcncmp          i.company,
domain  cpcom.plnc      i.scenario,
domain  cpcom.phnu      i.phase.number)
{
|* Apply phase-specific logic
if i.phase.number = 1 then
set.phase.parameters(i.company, i.scenario)
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.company       - Company
i.scenario      - Scenario
i.phase.number  - Phase Number
Output: N.A
Return: 0               - Success
```
