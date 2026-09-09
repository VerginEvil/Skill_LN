# InvoiceFromBP.SkipPrintOpenEntries

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InvoiceFromBP
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2089-2090

```baan
Skips Invoice-from Business Partner when Printing Open Entries.
This process extension is available from 2021.08 (KB2191481).
To implement this process extension, you can use the information below:
Usage:        Process Extension InvoiceFromBP.SkipPrintOpenEntries can be used
to skip certain Invoice-from Business Partner when Printing Open Entries
from Print Invoice-From Business Partner Open Entries.
Sessions where this Process Extension can be implemented:
- Print Invoice-From Business Partner Open Entries. (tfacp2421m000)
Fields that are available to be used in this Process Extension:
- All fields of table tccom122 are available.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttccom122       |* Invoice-from Business Partners
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on the data read = true> then
return(true)
endif
return (false)
}
```
