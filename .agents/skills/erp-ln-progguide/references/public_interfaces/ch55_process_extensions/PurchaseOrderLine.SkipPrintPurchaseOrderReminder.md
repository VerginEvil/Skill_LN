# PurchaseOrderLine.SkipPrintPurchaseOrderReminder

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2211-2211

```baan
Skips Purchase Order Line when Printing Purchase Order Reminders.
This process extension is available from 2021.12 (KB2215353).
To implement this process extension, you can use the information below:
Usage:        Process Extension PurchaseOrderLine.SkipPrintPurchaseOrderReminder can
be used to skip specific Purchase Order Lines when printing Purchase
Order Reminders.
Sessions where this Process Extension can be implemented:
- Print Purchase Order Reminders (tdpur4403m000)
Fields that are available to be used in this Process Extension:
- All fields of table Purchase Order Lines (tdpur401)
Pseudocode:
Below you can find an example:
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
