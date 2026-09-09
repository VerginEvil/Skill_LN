# ProductionOrder.SkipCalculateIntermediateResults

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2162-2162

```baan
Skips Production Orders when executing Calculate Intermediate Results.
This process extension is available from 2023.06 (KB2294561).
Technical information for this process extension:
Usage:        Process Extension ProductionOrder.SkipCalculateIntermediateResults can be used
to skip intermediate result calculation for specific Production Orders.
A message may be filled, to present information about the skip
decision on the report. This message can have max 300 characters.
Sessions where this Process Extension can be implemented:
- Calculate Intermediate Results (ticst0201m100)
Fields that are available to be used in this Process Extension:
- All fields of table: Production Orders (tisfc001)
Pseudocode:
Below you can find an example.
Hook: Declarations
table tisfc001
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if <condition on tisfc001 = true> then
o.reason = "Production Order skipped because ..."
return(true)
endif
return(false)
}
```
