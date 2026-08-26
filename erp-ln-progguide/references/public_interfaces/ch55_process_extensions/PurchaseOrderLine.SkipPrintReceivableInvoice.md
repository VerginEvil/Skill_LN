# PurchaseOrderLine.SkipPrintReceivableInvoice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2188-2189

Skips Purchase Order Line when Printing Receivable Invoices. This process extension is available from 2024.06 ( KB2327957 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PurchaseOrderLine.SkipPrintReceivableInvoice can be used
to skip Purchase Order Lines when printing receivable invoices.
Sessions where this Process Extension can be implemented:
-               Print Receivable Invoices Up to Period (tfacp1439m000)
-               Checklist Reconciliation Goods Received Not Invoiced (tfgld4495m200)
Note: For the same sessions, ReceivableInvoice.SkipPrintSpecification()
is available to skip printing based on "Order Data for Approval" (tfacp240)
Fields that are available to be used in this Process Extension:
-               All fields of table Purchase Orders History (tdpur450)
-               All fields of table Purchase Order Lines History (tdpur451)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdpur451       |* Purchase Order Line History
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdpur451 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for PurchaseRequisition

The following process extension(s) is/are available: PurchaseRequisition.SkipConvert
