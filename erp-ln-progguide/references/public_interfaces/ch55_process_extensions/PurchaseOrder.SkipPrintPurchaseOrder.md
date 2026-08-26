# PurchaseOrder.SkipPrintPurchaseOrder

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2173-2173

Skips Purchase Order when Printing Purchase Order. This process extension is available from 2019.09 ( KB2076283 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PurchaseOrder.SkipPrintPurchaseOrder can be used
to skip Purchase Orders when printing the Purchase Order.
Sessions where this Process Extension can be implemented:
-               Print Purchase Orders (tdpur4401m000)
-               All sessions and processes that trigger the printing of the
Purchase Order (like automatic processing logic).
Fields that are available to be used in this Process Extension:
-               All fields of table Purchase Order (tdpur400)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdpur400       |* Purchase Orders
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdpur400 = true> then
return(true)
endif
return (false)
}
```
