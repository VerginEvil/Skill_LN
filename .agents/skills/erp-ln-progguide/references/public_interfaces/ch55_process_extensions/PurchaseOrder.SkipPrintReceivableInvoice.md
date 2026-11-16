# PurchaseOrder.SkipPrintReceivableInvoice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2196-2197

```baan
Skips Purchase Order when Printing Receivable Invoices.
This process extension is available from 2024.06 (KB2327957).
To implement this process extension, you can use the information below:
Usage:        Process Extension PurchaseOrder.SkipPrintReceivableInvoice can be used
to skip Purchase Orders when printing receivable invoices.
Sessions where this Process Extension can be implemented:
- Print Receivable Invoices Up to Period (tfacp1439m000)
- Checklist Reconciliation Goods Received Not Invoiced (tfgld4495m200)
Note: For the same sessions, ReceivableInvoice.SkipPrintSpecification()
is available to skip printing based on "Order Data for Approval" (tfacp240)
Fields that are available to be used in this Process Extension:
- All fields of table Purchase Order History (tdpur450)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdpur450       |* Purchase Order History
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdpur450 = true> then
return(true)
endif
return (false)
}
```
