# TPOP.SkipPlannedTransaction

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TPOP
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2280-2281

Skips Order generation (TPOP) under certain circumstances. This process extension is available from 2024.05 ( KB2331666 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension TPOP.SkipPlannedTransaction can be used
to skip a planned inventory transaction during the TPOP run.
Sessions where this Process Extension can be implemented:
-               Generate Orders (TPOP) (whinh2201m000)
Fields that are available to be used in this Process Extension:
All primary keys of whinp100 are current:
whinp100.koor                               - Originating Type of Order
whinp100.orno                               - Order
whinp100.kotr                               - Transaction Type
whinp100.pono                               - Order Line
whinp100.ponb                               - Order Sequence
whinp100.boml                               - BOM Line
whinp100.dlin                               - Distribution Line
whinp100.effn                               - Effectivity Unit
Pseudocode:
Below you can find an example.
Hook: Declarations
table whinp100
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on whinp100 = true> then
return(true)
endif
return(false)
}
```

## Process Extensions for TransferOrderPlanning

The following process extension(s) is/are available: TransferOrderPlanning.CustomOrderSeries TransferOrderPlanning.CustomSorting
