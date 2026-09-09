# SalesContract.SkipPrintSalesContract

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2241-2242

```baan
Skips Sales Contract when Printing Sales Contracts.
This process extension is available from 2025.09 (KB3617247).
To implement this process extension, you can use the information below:
Usage:        Process Extension SalesContract.SkipPrintSalesContract can be used
to skip Sales Contract when printing the Sales Contracts.
Session where this Process Extension can be implemented:
- Print Sales Contract Reports (tdsls3401m000)
Fields that are available to be used in this Process Extension:
- All fields of table Sales Contracts (tdsls300)
Note: Table must also be declared in the Process Extension.
So skip conditions can be built on current tdsls300 data
as instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for sales contracts.
Hook: Declarations
table   ttdsls300       |* Sales Contracts
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls300 = true> then
return(true)
endif
return (false)
}
```
