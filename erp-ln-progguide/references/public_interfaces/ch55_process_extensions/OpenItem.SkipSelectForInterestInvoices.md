# OpenItem.SkipSelectForInterestInvoices

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for OpenItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2110-2111

```baan
Skips selection for Interest Invoice.
This process extension is available from 2023.09 (KB2300368).
Technical information for this process extension:
Usage:        OpenItem.SkipSelectForInterestInvoices can be used to skip an
Opem Item for Interest Invoice selection.
A message may be filled, to present information about the skip
decision on the report. This message can have max 70 characters.
Session where this Process Extension can be implemented:
- Select Inv.-to BP Receipts for Interest Invoices (tfacr5210m000)
Fields that are available to be used in this Process Extension:
- Primary key fields of tfacr500        tfacr500.fcom (financial company)
tfacr500.ttyp (Transaction Type)
tfacr500.ninv (Document)
tfacr500.line (Line)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfacr500       |* Open Items A/R
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
read tfacr500 (binded!)
if <condition on tfacr500 = true> then
o.reason = "Open Item Skipped because ....."
return(true)
endif
return (false)
}
```
