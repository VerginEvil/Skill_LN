# InvoiceFromBP.SkipCalculateAgingAnalysis

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InvoiceFromBP
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2088-2088

```baan
Skips Invoice-from Business Partner when Calculating Aging Analysis.
This process extension is available from 2024.11 (KB3508117).
To implement this process extension, you can use the information below:
Usage:        Process Extension InvoiceFromBP.SkipCalculateAgingAnalysis can be used
to skip certain Invoice-from Business Partner when Calculating Aging Analysis.
Sessions where this Process Extension can be implemented:
- Calculate Payables Aging Analysis. (tfacp3525m000)
Fields that are available to be used in this Process Extension:
- Primary key fields of tccom122:       tccom122.ifbp (Invoice-from Business
Partner)
tccom122.cofc (Department)
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttccom122       |* Invoice-from Business Partners
Hook: ext.skip
function extern boolean ext.skip()
{
|* read data using tccom122.ifbp, tccom122.cofc
if <condition on the data read = true> then
return(true)
endif
return (false)
}
```
