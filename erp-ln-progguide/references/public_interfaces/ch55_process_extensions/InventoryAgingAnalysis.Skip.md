# InventoryAgingAnalysis.Skip

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InventoryAgingAnalysis
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2043-2044

Skips Inventory during Inventory Aging Analysis. This process extension is available from 2024.09 ( KB3514346 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension InventoryAgingAnalysis.Skip can be
used to skip Inventory during Inventory Aging Analysis.
Sessions where this Process Extension can be implemented:
-               Perform Inventory Aging Analysis (whina1440m000)
Fields that are available to be used in this Process Extension:
-               All fields of tables
Inventory Receipt Transactions (whina112)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table twhina112
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on whina112 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for InventoryCommitments

The following process extension(s) is/are available: InventoryCommitments.SkipGenerate
