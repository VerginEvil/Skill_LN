# InvoiceToBP.SkipPrintOpenEntries

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InvoiceToBP
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2071-2072

Skips Invoice - to Business Partner when Printing Open Entries. This process extension is available from 2021.08 ( KB2191481 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension InvoiceToBP.SkipPrintOpenEntries can be used
to skip Invoice              -to Business Partner when Printing Open Entries from Print
Invoice              -to Business Partner Open Entries.
Sessions where this Process Extension can be implemented:
-               Print Invoice-to Business Partner Open Entries. (tfacr2421m000)
Fields that are available to be used in this Process Extension:
-               All fields of table tccom112 are available.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttccom112       |* Invoice              -to Business Partners
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on the data read = true> then
return(true)
endif
return (false)
}
```
