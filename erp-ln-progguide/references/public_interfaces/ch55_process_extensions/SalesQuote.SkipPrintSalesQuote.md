# SalesQuote.SkipPrintSalesQuote

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2239-2240

Skips Sales Quote when Printing Sales Quote. This process extension is available from 2020.06 ( KB2127961 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesQuote.SkipPrintSalesQuote can be used
to skip Sales Quotes when printing the Sales Quote.
Sessions where this Process Extension can be implemented:
-               Print Sales Quotation (tdsls1401m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Sales Quotation (tdsls100)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdsls100       |* Sales Quotations
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls100 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for SalesQuoteLine

The following process extension(s) is/are available: SalesQuoteLine.SkipPrintSalesQuote
