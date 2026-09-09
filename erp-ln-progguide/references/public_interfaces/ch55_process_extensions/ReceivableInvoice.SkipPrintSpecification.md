# ReceivableInvoice.SkipPrintSpecification

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ReceivableInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2221-2222

```baan
Skip Print Receivable Invoice Specification.
This process extension is available from 2024.07 (KB2329986).
To implement this process extension, you can use the information below:
Usage:        Process Extension ReceivableInvoice.SkipPrintSpecification can be used
to skip Printing Receivable Invoice Specification.
Sessions where this Process Extension can be implemented:
- Print Receivable Invoice Specifications (tfacp1432m000).
- Checklist Reconciliation Goods Received Not Invoiced (tfgld4495m200)
- Print Receivable Invoices Up to Period (tfacp1439m000)
Note: For sessions tfgld4495m200 and tfacp1439m000,
PurchaseOrder.SkipPrintReceivableInvoice is available to skip printing
based on table: Purchase Order History (tdpur450)
Fields that are available to be used in this Process Extension:
- All fields of table: Order Data for Approval (tfacp240)
External variables that are available to be used in the Process
Extension:
- proc_ext_called_from [type: string(13) ] : this variable is filled
with one of next values:
- "tfacp1432m000"
- "tfgld4495m200"
- "tfacp1439m000
Note: Tables and external variables must also be declared in the
Process Extension.
Pseudocode: Below you can find an example:
Hook: Declarations
table   ttfacp240       |* Order Data for Approval
extern          string          proc_ext_called_from(13)
Hook: ext.skip
function extern boolean ext.skip()
{
if proc_ext_called_from = "tfacp1439m000" and
<condition on tfacp240 = true> then
return(true)
endif
return (false)
}
```
