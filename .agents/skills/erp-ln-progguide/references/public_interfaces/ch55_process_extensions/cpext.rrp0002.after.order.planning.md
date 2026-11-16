# cpext.rrp0002.after.order.planning

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2096-2096

```baan
Syntax: long cpext.rrp0002.after.order.planning(
domain  tcncmp           i.company,
domain  cpcom.plnc       i.scenario )
Usage:        Expl:   This function is called in the context of order planning, just
after the planning process has completed.
It will only be called when order planning is started from session
Generate Order Planning (cprrp1210m000).
Implementation example:
function extern long cpext.rrp0002.after.order.planning(
domain  tcncmp          i.company,
domain  cpcom.plnc      i.scenario)
{
|* Process results
process.custom.results(i.company, i.scenario)
|* Send notification
if notification.required() then
send.notification(i.scenario)
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.company       - Company
i.scenario      - Scenario
Output: N.A
Return: 0               - Success
```
