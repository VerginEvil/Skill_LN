# ReservedCommissionsRebates.SkipReservationApproval

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ReservedCommissionsRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2228-2228

```baan
Skips Reserved Commissions/Rebates when Reserving and Approving.
This process extension is available from 2025.09 (KB3598645).
To implement this process extension, you can use the information below:
Usage:        Process Extension ReservedCommissionsRebates.SkipReservationApproval can be used
to skip Reserved Commissions/Rebates when Reserving and Approving the Reserved
Commissions/Rebates.
Session where this Process Extension can be implemented:
- Reservation and Approval of Reserved Commissions/Rebates (tdcms2202m000)
Fields that are available to be used in this Process Extension:
- All fields of table Commissions/Rebates (tdcms050)
Note: Table must also be declared in the Process Extension.
So skip conditions can be built on current tdcms050 data
as instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for reserved
commissions/rebates.
Hook: Declarations
table   ttdcms050       |* Commissions/Rebates
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdcms050 = true> then
return(true)
endif
return (false)
}
```
