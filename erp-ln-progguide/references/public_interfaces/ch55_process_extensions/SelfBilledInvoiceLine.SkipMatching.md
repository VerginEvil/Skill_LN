# SelfBilledInvoiceLine.SkipMatching

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SelfBilledInvoiceLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2264-2265

```baan
Skip Self-Billed Invoice Lines when Matching.
This process extension is available from 2021.11 (KB2214870).
To implement this process extension, you can use the information below:
Usage:        Process Extension SelfBilledInvoiceLine.SkipMatching can be used
to skip Matching of Self-Billed Invoice Line.
Sessions where this Process Extension can be implemented:
- Match Self-Billed Invoices (cisli5200m000)
Fields that are available to be used in this Process Extension:
- Self-Billed Invoice Header (cisli500)
- Self-Billed Invoice Lines (cisli505)
Note:- This method is not applicable for Manual Matching Process
Pseudocode: In the code below, the Self-Billed Invoice line from
cisli505 which have Self-Billed Invoice Type(cisli505.type)
as "Price Variation" will be skipped during the matching
process.
Hook: Declarations
table   tcisli500
table   tcisli505
Hook: ext.skip
function extern boolean ext.skip()
{
if cisli505.type = tcsli.intp.price.variation then
|* If Self-Billed Invoice Type is Price
|* Variation then skip matching of the
|* Self-Billed Invoice Line.
return(true)
endif
return (false)
}
```
