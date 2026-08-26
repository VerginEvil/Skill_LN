# cpext.rrp0002.before.order.planning

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2077-2077

```baan
Syntax: long cpext.rrp0002.before.order.planning(
domain  tcncmp           i.company,
domain  cpcom.plnc       i.scenario )
Usage:        Expl:   This function is called in the context of order planning, just
before the planning process is actually started.
It will only be called when order planning is started from session
Generate Order Planning (cprrp1210m000).
Implementation example:
function extern long cpext.rrp0002.before.order.planning(
domain  tcncmp          i.company,
domain  cpcom.plnc      i.scenario)
{
|* Check scenario and prepare data
if i.scenario = "MAIN" then
prepare.custom.data(i.company)
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.company                     - Company
i.scenario                            - Scenario
Output: N.A
Return: 0                             - Success
```
