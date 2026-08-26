# PurchaseOrderLine.SkipPrintPurchaseInvoice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2186-2187

Skips Purchase Order Line when Printing Purchase Invoices. This process extension is available from 2020.08 ( KB2142810 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PurchaseOrderLine.SkipPrintPurchaseInvoice can be used
to skip specific Purchase Order Lines when printing Purchase Invoices.
Sessions where this Process Extension can be implemented:
-               Print Purchase Invoices (tdpur4404m000)
-               All sessions and processes that trigger the printing of the
Purchase Invoices (like automatic processing logic).
Fields that are available to be used in this Process Extension:
-               All fields of table Purchase Orders (tdpur400)
-               All fields of table Purchase Order Lines (tdpur401)
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
