# ItemOrderPlan.CustomActions

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2074-2075

Executes Custom Process for Order Planning. This process extension is available from 2026.07 ( KB3612975 ). Technical information for this process extension:

```baan
Usage:    This Process Extension allows users to define custom actions at different
stages of the Order Planning process. The extender can implement the
following functions:
-             cpext.rrp0002.before.order.planning() - Executed at the beginning of
order planning for a scenario in a company.
-             cpext.rrp0002.after.order.planning() - Executed at the conclusion of
order planning for a scenario in a company.
-             cpext.rrp0002.before.phase.number() - Executed at the start of
planning items for a specific phase number.
-             cpext.rrp0002.after.phase.number() - Executed at the end of
planning items for a specific phase number.
-             cpext.rrp0002.before.plan.item() - Executed at the initiation of
order planning for a plan item.
-             cpext.rrp0002.after.plan.item() - Executed at the completion of
order planning for a plan item.
```

To implement this process extension, you need to implement the following method(s):
