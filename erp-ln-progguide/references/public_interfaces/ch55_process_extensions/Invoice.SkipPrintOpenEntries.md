# Invoice.SkipPrintOpenEntries

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2081-2082

```baan
Skips Invoices when Printing Open Entries.
This process extension is available from 2024.08 (KB3501274).
To implement this process extension, you can use the information below:
Usage:        Process Extension Invoice.SkipPrintOpenEntries can be used
to skip certain Invoices when Printing Open Entries
Sessions where this Process Extension can be implemented:
- Print Invoice-From Business Partner Open Entries. (tfacp2421m000)
- Print Invoice-to Business Partner Open Entries. (tfacr2421m000)
External variables that are available to be used in the Process
Extension:
- proc_ext_called_from [type: string(13) ] : this variable is filled
with one of next values:
- "tfacp2421m000"
- "tfacr2421m000"
- proc_ext_acp_or_acr [type: string(3) ] : this variable is filled
with one of next values:
- "acp" --> Purchase invoice is current
- "acr" --> Sales Invoice is current
Fields that are available to be used in this Process Extension:
- All fields of table tfacp200 are available if proc_ext_acp_or_acr
reads "acp"
- All fields of table tfacr200 are available if proc_ext_acp_or_acr
reads "acr"
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfacp200       |* Open Items (Purchase Invoices and Payments)
table   ttfacr200       |* Open Items (Sales Invoices & Receipts)
extern          string          proc_ext_called_from(13)
extern          string          proc_ext_acp_or_acr(3)
Hook: ext.skip
function extern boolean ext.skip()
{
if proc_ext_called_from = "tfacp2421m000" and
proc_ext_acp_or_acr = "acp" and
<condition on tfacp200 = true> then
return(true)
endif
if proc_ext_called_from = "tfacp2421m000" and
proc_ext_acp_or_acr = "acr" and
<condition on tfacr200 = true> then
return(true)
endif
return (false)
}
```
