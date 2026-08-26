# PurchaseOrderLine.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2186-2186

Skips Purchase Order Lines when Printing. This process extension is available from 2026.09 ( KB3692686 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PurchaseOrderLine.SkipPrint can be used to skip Purchase
Order Lines when Printing the Purchase Order.
Sessions where this Process Extension can be implemented:
-               Print Purchase Orders (tdpur4405m000)
-               Print Purchase Order Lines (tdpur4409m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Purchase Order Lines (tdpur401)
Note: The table must also be declared in the Process Extension.
So skip conditions can be built on current tdpur401
data as instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for purchase
order lines.
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
