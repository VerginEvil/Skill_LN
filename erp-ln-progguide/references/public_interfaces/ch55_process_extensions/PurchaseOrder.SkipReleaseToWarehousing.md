# PurchaseOrder.SkipReleaseToWarehousing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2174-2175

Skips Purchase Order Lines when Releasing to Warehousing. This process extension is available from 2019.09 ( KB2076283 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PurchaseOrder.SkipReleaseToWarehousing can be used
to skip Purchase Order Lines when Releasing to Warehousing.
Sessions where this Process Extension can be implemented:
-               Release Purchase Orders to Warehousing (tdpur4246m000)
-               All sessions and processes that trigger the release of lines to
Warehousing (like automatic processing logic).
Fields that are available to be used in this Process Extension:
-               All fields of table Purchase Order Lines (tdpur401) when releasing
order lines.
Note: tables must also be declared in the Process Extension.
The Purchase order release to warehousing process releases Purchase order
lines.
Pseudocode:
Below you can find an example.
Hook: Declarations
table   ttdpur401       |* Purchase Order Lines
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdpur401 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for PurchaseOrderGenerate

The following process extension(s) is/are available: PurchaseOrderGenerate.HandleCombining PurchaseOrderGenerate.InputOverruling PurchaseOrderGenerate.SuppressCommingleLine
