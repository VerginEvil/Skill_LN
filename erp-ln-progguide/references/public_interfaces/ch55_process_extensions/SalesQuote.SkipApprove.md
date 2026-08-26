# SalesQuote.SkipApprove

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2238-2239

Skips Sales Quote when Approving. This process extension is available from 2026.08 ( KB3686564 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesQuote.SkipApprove can be used
to skip Sales Quotations when Approving the Sales Quotations.
Session where this Process Extension can be implemented:
-               Approve Sales Quotations (tdsls1211m000)
Fields that are available to be used in this Process Extension:
-               All fields of table "Sales Quotations" (tdsls100)
Note: Table must also be declared in the Process Extension.
Skip conditions can be built on current tdsls100 data
as instructed below.
Pseudocode:
Below you can find an example how to handle the conditions for sales
quotations.
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
