# CycleCountingOrderLine.SkipGenerate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for CycleCountingOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1997-1998

Skips generating cycle counting lines. This process extension is available from 2025.11 ( KB3624525 ). Technical information for this process extension:

```baan
Usage:        Process Extension CycleCountingOrderLine.SkipGenerate can be
used to skip generating cycle counting order lines.
Sessions where this Process Extension can be implemented:
-               Generate Cycle Counting Orders (whinh5200m000)
Fields that are available to be used in this Process Extension:
-               All fields of tables
Cycle Counting Order Lines (whinh501)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table twhinh501
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if <condition on whinh501 = true> then
o.reason = "Cycle Counting Line skipped because ..."
return(true)
endif
return (false)
}
```

## Process Extensions for Dataset

The following process extension(s) is/are available: Dataset.CustomOutputFormat
