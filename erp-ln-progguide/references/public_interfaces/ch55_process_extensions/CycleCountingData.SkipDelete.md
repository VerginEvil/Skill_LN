# CycleCountingData.SkipDelete

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for CycleCountingData
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2015-2016

```baan
Skips deleting unused cycle counting data.
This process extension is available from 2025.03 (KB3539935).
To implement this process extension, you can use the information below:
Usage:        Process Extension CycleCountingData.SkipDelete can be
used to skip deleting unused cycle counting data.
Sessions where this Process Extension can be implemented:
- Remove Unused Cycle Counting Data (whinh5240m000)
Fields that are available to be used in this Process Extension:
- All fields of tables
Cycle Counting Data (whinh540)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table twhinh540
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on whinh540 = true> then
return(true)
endif
return (false)
}
```
