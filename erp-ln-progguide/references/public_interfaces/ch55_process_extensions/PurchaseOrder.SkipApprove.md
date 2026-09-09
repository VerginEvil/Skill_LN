# PurchaseOrder.SkipApprove

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2194-2194

```baan
Skips Purchase Order when Approving.
This process extension is available from 2019.09 (KB2076283).
To implement this process extension, you can use the information below:
Usage:        Process Extension PurchaseOrder.SkipApprove can be used
to skip Purchase Orders when Approving the Purchase Order.
Sessions where this Process Extension can be implemented:
- Approve Purchase Orders (tdpur4210m100)
- All sessions and processes that trigger the Approve.
Fields that are available to be used in this Process Extension:
- All fields of table Purchase Order (tdpur400).
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
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
