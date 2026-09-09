# PurchaseOrder.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2194-2195

```baan
Skips Purchase Order when Printing.
This process extension is available from 2026.09 (KB3692686).
To implement this process extension, you can use the information below:
Usage:        Process Extension PurchaseOrder.SkipPrint can be used to skip Purchase
Orders when Printing the Purchase Order.
Sessions where this Process Extension can be implemented:
- Print Purchase Orders (tdpur4405m000)
- Print Purchase Order Lines (tdpur4409m000)
Fields that are available to be used in this Process Extension:
- All fields of table Purchase Orders (tdpur400)
Note: Table must also be declared in the Process Extension.
So skip conditions can be built on current tdpur400 data as
instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for purchase
orders.
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
