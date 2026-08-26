# cpext.rrp0002.after.phase.number

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2075-2076

```baan
Syntax: long cpext.rrp0002.after.phase.number(
domain  tcncmp           i.company,
domain  cpcom.plnc       i.scenario,
domain  cpcom.phnu       i.phase.number )
Usage:        Expl:   This function is called in the context of Generate Order Planning,
just after the execution completes for a specific order phase number.
It can be called from session Generate Order Planning (cprrp1210m000),
Generate Order Planning (Item) (cprrp1220m000) and Public Interface
"ItemOrderPlan.Generate".
Implementation example:
function extern long cpext.rrp0002.after.phase.number(
domain  tcncmp          i.company,
domain  cpcom.plnc      i.scenario,
domain  cpcom.phnu      i.phase.number)
{
|* Validate phase results
if not validate.phase(i.phase.number) then
log.validation.error(i.phase.number)
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.company                     - Company
i.scenario                            - Scenario
i.phase.number                        - Phase Number
Output: N.A
Return: 0                             - Success
```
