# SalesQuoteLine.SkipPrintSalesQuote

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesQuoteLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2240-2241

Skips Sales Quote Lines when Printing Sales Quote. This process extension is available from 2024.06 ( KB2330719 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesQuoteLine.SkipPrintSalesQuote can be used
to skip Sales Quote Lines when printing the Sales Quote.
Sessions where this Process Extension can be implemented:
-               Print Sales Quotation (tdsls1401m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Sales Quotation (tdsls100)
-               All fields of table Sales Quotation Lines (tdsls101)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdsls101       |* Sales Quotation Lines
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls101 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for SelfBilledInvoiceLine

The following process extension(s) is/are available: SelfBilledInvoiceLine.SkipMatching
