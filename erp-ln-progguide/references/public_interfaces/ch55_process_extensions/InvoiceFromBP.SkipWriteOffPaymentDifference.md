# InvoiceFromBP.SkipWriteOffPaymentDifference

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InvoiceFromBP
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2090-2090

```baan
Skips Invoice-from Business Partner when Writing Off Payment Difference.
This process extension is available from 2022.05 (KB2236314).
To implement this process extension, you can use the information below:
Usage:        InvoiceFromBP.SkipWriteOffPaymentDifference can be used to skip
Invoice-from Business Partner when Writing Off Payment Difference
from Write Off Payment Difference (tfacp2230m000).
Fields that are available to be used in this Process Extension:
- All fields of table tfacp500 are available.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfacp500       |* Open Items A/P
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on the data read = true> then
return(true)
endif
return (false)
}
```
