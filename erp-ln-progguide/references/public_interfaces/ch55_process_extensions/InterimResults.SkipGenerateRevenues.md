# InterimResults.SkipGenerateRevenues

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InterimResults
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2058-2059

```baan
Skips Generation of Revenues for Interim Results.
This process extension is available from 2026.03 (KB3635960).
To implement this process extension, you can use the information below:
Usage:        Process Extension InterimResults.SkipGenerateRevenues can be used to
skip generating interim results for selected Revenue Transactions
of a Project, Contract, or Contract and Contract Line that use the
Revenue Recognition Method as Actual Revenues or Percentage of Completion.
Sessions where this Process Extension can be implemented:
- Generate Interim Results (tpppc3250m000)
Fields that are available to be used in this Process Extension:
- tpppc305.cprj (Project)
- tpppc305.cspa (Element)
- tpppc305.cpro (Revenue Code)
- tpppc305.sern (Sequence Number)
Note: Tables must also be declared in the Process Extension.
Pseudocode:
The Generate Interim Results session creates interim results by
Contract or Project for both Revenue Transactions (tpppc305) and
Cost Transactions (tpppc200). This process extension can been applied to
the Revenue Transactions (tpppc305) table using the table fields mentioned above.
Below you can find an example.
Hook: Declarations
table   ttpppc305       |* Revenue Transactions
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tpppc305 = true> then
return(true)
endif
return (false)
}
```
