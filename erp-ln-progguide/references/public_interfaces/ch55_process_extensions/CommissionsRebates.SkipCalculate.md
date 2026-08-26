# CommissionsRebates.SkipCalculate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for CommissionsRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1985-1987

Skips Commissions/Rebates when Calculating. This process extension is available from 2025.11 ( KB3620998 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension CommissionsRebates.SkipCalculate can be used
to skip Commissions/Rebates when calculating the Commissions/Rebates.
Session where this Process Extension can be implemented:
-               Calculate Commissions and Rebates (tdcms0240m000)
Fields that are available to be used in this Process Extension:
-               All fields of table "Commissions/Rebates" (tdcms050) when removing non
paid commissions and rebates.
-               Primary key fields of table "Sales Order Line History" (tdsls451) when
calculation method 'Sales Order' is used.
-               Primary key fields of table "Sales Order Actual Delivery Line History"
(tdsls456) when calculation method 'Sales Invoice' or 'Paid Sales Invoice'
is used.
External variable that is available to be used in this Process Extension:
-               proc_ext_skip_commissions_rebates_based_on [ type: string(40) ].
Supported values are:
-                       remove_non_paid_commissions_rebates (for table tdcms050)
-                       calculate_by_sales_order (for table tdsls451)
-                       calculate_by_sales_invoice (for table tdsls456)
Note: tables and external variable must also be declared in the
Process Extension.
The process extension must be applied to these three tables.
Pseudocode:
Below you can find an example how to handle the conditions for
commissions/rebates,
sales order history lines and sales order actual delivery history lines.
Hook: Declarations
table   ttdcms050       |* Commissions/Rebates
table   ttdsls451       |* Sales Order Line History
table   ttdsls456       |* Sales Order Actual Delivery Lines History
extern          string  proc_ext_skip_commissions_rebates_based_on(40)
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_skip_commissions_rebates_based_on
case "remove_non_paid_commissions_rebates":
if <condition on tdcms050 = true> then
return(true)
endif
So in case of remove_non_paid_commissions_rebates
commissions/rebates can be skipped based on
tdcms050 data.
break
case "calculate_by_sales_order":
if <condition on tdsls451 = true> then
return(true)
endif
So in case of calculate_by_sales_order sales order
history lines can be skipped based on tdsls451
primary key data.
break
case "calculate_by_sales_invoice":
if <condition on tdsls456 = true> then
return(true)
endif
So in case of calculate_by_sales_invoice sales order
actual delivery history lines can be skipped based
on tdsls456 primary key data.
break
default:
break
endcase
return (false)
}
```

## Process Extensions for Common

The following process extension(s) is/are available: Common.DeterminePurchaseType Common.GetItemSignalInfo
