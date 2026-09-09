# Invoice.SkipSelectInvoiceForReminding

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2085-2085

```baan
Skips selection of an invoice for reminding.
This process extension is available from 2023.09 (KB2300371).
To implement this process extension, you can use the information below:
Usage:        Invoice.SkipSelectInvoiceForReminding can be used to skip
selecting of an Invoice For reminding.
Session where this Process Extension can be implemented:
- Select Invoices for Reminding (tfacr3205m000)
Fields that are available to be used in this Process Extension:
- All fields of "Open Items"  (tfacr500)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfacr500       |* Open Items A/R
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tfacr500 = true> then
return(true)
endif
return (false)
}
```
