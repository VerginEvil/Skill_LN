# ServiceOrderActivity.SkipComplete

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ServiceOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2265-2266

```baan
Skips Service Order Activity when setting Status to Completed.
This process extension is available from 2021.04 (KB2181351).
To implement this process extension, you can use the information below:
Usage:        Process Extension ServiceOrderActivity.SkipComplete can be used
to skip service order activities when setting to status Completed.
Sessions where this Process Extension can be implemented:
- Complete Service Order Activities (tssoc2206m000)
- All sessions and processes that trigger a Service Order Activity to be
set to status Completed.
Fields that are available to be used in this Process Extension:
- Key fields of tssoc210        - tssoc210.orno (Service Order)
- tssoc210.acln (Activity Line)
These fields can be used to read e.g. tables tssoc200 and tssoc210.
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table   ttssoc200       |* Service Orders
table   ttssoc210       |* Service Order Activities
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tssoc200 = true> then
return(true)
endif
if <condition on tssoc210 = true> then
return(true)
endif
return (false)
}
```
