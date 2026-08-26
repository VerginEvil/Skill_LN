# InvoiceToBP.SkipCalculateAgingAnalysis

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InvoiceToBP
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2070-2070

Skips Invoice - to Business Partner when Calculating Aging Analysis. This process extension is available from 2024.11 ( KB3508117 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension InvoiceToBP.SkipCalculateAgingAnalysis can be used
to skip Invoice              -to Business Partner when Calculating Aging Analysis.
Sessions where this Process Extension can be implemented:
-               Calculate Receivables Aging Analyses. (tfacr2511m000)
Fields that are available to be used in this Process Extension:
-               Primary key fields of tccom112:       tccom112.itbp (Invoice-to Business
Partner)
tccom112.cofc (Department)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttccom112       |* Invoice              -to Business Partners
Hook: ext.skip
function extern boolean ext.skip()
{
|* read data using tccom112.itbp, tccom112.cofc
if <condition on the data read = true> then
return(true)
endif
return (false)
}
```
