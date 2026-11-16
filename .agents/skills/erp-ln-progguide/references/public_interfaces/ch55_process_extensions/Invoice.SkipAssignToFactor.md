# Invoice.SkipAssignToFactor

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2079-2079

```baan
Skips assignment of Invoice to Factor.
This process extension is available from 2026.06 (KB3673548).
To implement this process extension, you can use the information below:
Usage:        Process Extension Invoice.SkipAssignToFactor can be used to skip an
invoice during assignment to a factor.
Sessions where this Process Extension can be implemented:
- Assign Factor to Documents (tfacr2210m000)
Fields that are available to be used in this Process Extension:
- Open Items (Sales Invoices & Receipts) (tfacr200)
Pseudocode: In the code below,
if the extender defined expression evaluates to true
then the invoice from tfacr200 is skipped
during assignment to a factor.
Hook: Declarations
table   tfacr200
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tfacr200 = true> then
return(true)
endif
return(false)
}
```
