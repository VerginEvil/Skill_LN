# BillableLine.SkipComposing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BillableLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1974-1975

```baan
Skip Billable Line when composing.
This process extension is available from 2024.09 (KB3520951).
To implement this process extension, you can use the information below:
Usage:        Process Extension BillableLine.SkipComposing can be used to skip
billable line when it is being composed.
Sessions where this Process Extension can be implemented:
- Compose/Print/Post (cisli2200m000)
- Billable Lines (cisli8110m000)
Fields that are available to be used in this Process Extension:
- Billable Line (cisli810)
Pseudocode: In the code below, the billable line from cisli810 whose
Billable Amount (cisli810.amti) is greater than 1000.00
will be skipped during the composing process.
Hook: Declarations
table   tcisli810
Hook: ext.skip
function extern boolean ext.skip()
{
if cisli810.amti > 1000.00  then
|* If Billable line amount is greater than
|* 1000.00 then skip this billable line during
|* the composing.
return(true)
endif
return (false)
}
```
