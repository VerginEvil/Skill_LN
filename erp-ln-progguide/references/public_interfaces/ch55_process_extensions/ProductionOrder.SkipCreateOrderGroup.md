# ProductionOrder.SkipCreateOrderGroup

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2140-2141

Skips Creating a Production Order Group. This process extension is available from 2025.09 ( KB3548856 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension ProductionOrder.SkipCreateOrderGroup can be used
to skip production order grouping.
Sessions where this Process Extension can be implemented:
-                       Create Production Order Group(tisfc3250m000)
Field that is available to be used in this Process Extension:
-               All fields of table Production Orders (tisfc001)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table ttisfc001
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tisfc001 = true> then
return(true)
endif
return (false)
}
```
