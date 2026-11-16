# ReservedApprovedCommissionsRebates.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ReservedApprovedCommissionsRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2226-2227

```baan
Skips Reserved and Approved Commissions/Rebates when Printing.
This process extension is available from 2023.09 (KB2302057).
To implement this process extension, you can use the information below:
Usage:        Process Extension ReservedApprovedCommissionsRebates.SkipPrint can be used
to skip Reserved and Approved Commissions/Rebates when Printing the Reserved
Commissions/Rebates and Approved Commissions/Rebates.
Session where this Process Extension can be implemented:
- Print Approved Commissions/Rebates (tdcms2402m000)
- Print Reserved Commissions/Rebates (tdcms2403m000)
Fields that are available to be used in this Process Extension:
- All fields of table Commissions/Rebates (tdcms050)
Note: Table must also be declared in the Process Extension.
So skip conditions can be built on current tdcms050 data
as instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for reserved
commissions/rebates and approved commissions/rebates.
Hook: Declarations
table   ttdcms050       |* Commissions/Rebates
Hook: ext.skip
function extern boolean ext.skip()
{
on case tdcms050.resv
case tcyesno.yes:
if <condition on tdcms050 = true> then
return(true)
endif
So in case of field Reserve (tdcms050.resv) = "Yes",
Reserved Commissions/Rebates can be skipped based
on tdcms050 data.
break
case tcyesno.no:
if <condition on tdcms050 = true> then
return(true)
endif
So in case of field Reserve (tdcms050.resv) = "No",
Approved Commissions/Rebates can be skipped based
on tdcms050 data.
break
endcase
return (false)
}
```
