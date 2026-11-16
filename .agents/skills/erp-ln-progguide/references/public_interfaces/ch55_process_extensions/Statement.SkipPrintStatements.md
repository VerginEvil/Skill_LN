# Statement.SkipPrintStatements

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Statement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2279-2279

```baan
Skip Print Statements of account.
This process extension is available from 2024.01 (KB2319017).
To implement this process extension, you can use the information below:
Usage:        Process Extension Statement.SkipPrintStatements can be used
to skip Printing Statements of Account.
Sessions where this Process Extension can be implemented:
- Print Statements (tfacr3440m000)
Fields that are available to be used in this Process Extension:
- All fields of "Open Items" (tfacr500)
Note: Tables must also be declared in the Process Extension.
Pseudocode: Below you can find an example:
Hook: Declarations
table   ttfacr500       |* Open Items A/R
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tfacr500 = true> then
return(true)
endif
return (false)
}
```
