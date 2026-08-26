# AdvanceInstallment.SkipPrintZ5Reporting

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for AdvanceInstallment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1948-1949

Skip Advance Installment during Z5 reporting. This process extension is available from 2026.03 ( KB3655880 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension AdvanceInstallment.SkipPrintZ5Reporting
can be used to skip advance installment during Z5 reporting.
Sessions where this Process Extension can be implemented:
-                       Print Z5 Report (tfcmg3455m000)
Fields that are available to be used in this Process Extension:
-                       Open Items (Sales Invoices & Receipts) (tfacr200)
Pseudocode: In the code below,
if the extender defined expression evaluates to true
then the advance installment from tfacr200 is skipped
during Z5 reporting.
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

## Process Extensions for AssemblyOrder

The following process extension(s) is/are available: AssemblyOrder.SkipDelete AssemblyOrder.SkipGenerate
