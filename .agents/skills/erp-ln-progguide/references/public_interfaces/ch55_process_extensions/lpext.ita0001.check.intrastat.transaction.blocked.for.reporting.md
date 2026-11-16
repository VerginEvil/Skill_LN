# lpext.ita0001.check.intrastat.transaction.blocked.for.reporting

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for IntrastatTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2060-2061

```baan
Syntax: long lpext.ita0001.check.intrastat.transaction.blocked.for.reporting(
ref             boolean          o.blocked.for.reporting )
Usage:        Expl:
Use this method to check whether, at adding Intrastat Transaction
record, the status must be set to "Blocked for Reporting".
At moment of adding an Intrastat Transaction, LN will do checks
first. Only if the Intrastat Transaction status is not set to
"Blocked for Reporting" according to the standard logic in LN,
this method in the Process Extension is called.
In this method, own checks can be implemented and the variable
o.blocked.for.reporting can be set. If the variable is
set to false, the Intrastat Transaction status will not be changed.
Otherwise, the status will be set to "Blocked for Reporting".
Fields that can be used in this process extension:
Although the Intrastat Transaction is about to be added and not
yet committed, the Intrastat Transaction fields from lpita360 table
are already available.
Note that dal messages set in this function will be ignored by
the standard.
----------------------------------------------------------------
Start of Example of Implementation
Pseudocode:
Hook: Declarations
table   tlpita360       |* Intrastat Transactions
Hook: lpext.ita0001.get.intrastat.transaction.blocked.for.reporting
function extern long
lpext.ita0001.get.intrastat.transaction.blocked.for.reporting(
ref boolean o.blocked.for.reporting)
{
domain  <domain>        field.value
|* Default value is set to False.
o.blocked.for.reporting = false
select  cisli310.<field>:field.value
from    cisli310
where   cisli310._index1 = {
:lpita360.fcmp,
:lpita360.tran,
:lpita360.idoc,
:lpita360.line}
as set with 1 rows
selectdo
|**************************************
|* If customized criteria are met
|* so the Intrastat transaction status
|* is set to "Blocked for Reporting".
|**************************************
if field.value = <customized criteria> then
o.blocked.for.reporting = true
endif
endselect
return(0)
}
End of Example of Implementation
----------------------------------------------------------------
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.blocked.for.reporting - Indicates whether the Intrastat
Transaction record status must be set
to "Blocked for Reporting".
Return: 0                       - Success
<> 0                    - Returning a value <> 0 will abort the
creation of Intrastat Transactions.
```
