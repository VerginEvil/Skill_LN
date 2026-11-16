# Invoice.SkipCreditNoteLinking

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2079-2080

```baan
Skip Credit Note Linking to the original invoice at the time of posting of invoice.
This process extension is available from 2025.02 (KB3551578).
To implement this process extension, you can use the information below:
Usage:        When an Invoice is being posted, as per LN Standard logic, if Credit
Note is allowed to be linked to the original invoice, then it will be
automatically linked.
Process Extension Invoice.SkipCreditNoteLinking can be used to skip the
automatic linking of credit note to the original invoice at the time of
posting of invoice.
Fields that are available to be used in this Process Extension:
- Invoice Header (cisli305)
Pseudocode:
Hook: Declarations
table   tcisli305
Hook: ext.skip
function extern boolean ext.skip()
{
if cisli305.itbp = "BP0000001" then
|* In case of Invoice-to BP is equal to above
|* Skip automatic linking of Credit Note at the
|* time of posting of Invoice.
return(true)
endif
|* Automatically link the Credit Note if applicable at
|* the time of posting of Invoice.
return (false)
}
```
