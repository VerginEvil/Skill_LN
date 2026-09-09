# PlannedOrder.SkipTransfer

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2130-2130

```baan
Skips transfer of Planned Orders.
This process extension is available from 2022.12 (KB2236258).
Technical information for this process extension:
Usage:        Process Extension PlannedOrder.SkipTransfer can be used to skip
the transfer of certain Planned Orders when transferring Planned Orders
from Enterprise Planning to the execution level.
Extender may specify a message, to present information about the skip
decision on the report.
Sessions where this Process Extension can be implemented:
- Transfer Order Planning (cppat1210m000).
Fields that are available to be used in this Process Extension:
- cprrp100.plnc (Scenario)
- cprrp100.type (Planned Order Type)
- cprrp100.orno (Planned Order)
Note: Tables & messages must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table tcprrp100
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if <condition on cprrp100 = true> then
o.reason = "Transfer skipped because ..."
return(true)
endif
return(false)
}
```
