# PerformInventoryValuation.SkipItem

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PerformInventoryValuation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2103-2104

Skips Items during Perform Inventory Valuation. This process extension is available from 2023.10 ( KB2308375 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PerformInventoryValuation.SkipItem can be used
to skip Items during Perform Inventory Valuation.
Sessions where this Process Extension can be implemented:
-               Perform Inventory Valuation (whina1210m000)
Fields that are available to be used in this Process Extension:
-               All fields of tables
Items (tcibd001)
Warehouses (tcmcs003)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table ttcibd001
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tcibd001 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for PickingMission

The following process extension(s) is/are available: PickingMission.HandleAfterGenerate
