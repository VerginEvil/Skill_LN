# PlannedPRPOrder.SkipGenerate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PlannedPRPOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2108-2109

Skips Generation of Planned PRP Orders. This process extension is available from 2026.03 ( KB3651167 ). To implement this process extension, you can use the information below:

```baan
Usage:                Process Extension PlannedPRPOrder.SkipGenerate can be used to
skip the generation of the Planned PRP Order for Material,
Equipment and Subcontracting.
Session where this Process Extension can be implemented:
-               Generate Planned PRP Orders (tppss6200m000)
Fields that are available to be used in this Process Extension:
|***          - All fields of table: Control Data Material Lines (tpptc127)
-               All fields of table: Control Data Equipment Lines(tpptc147)
-               All fields of table: Control Data Subcontracting Lines(tpptc157)
External variables that are available to be used in this Process
Extension:
-               proc_ext_cost_type [ type: string(20) ]
Note: tables and external variables must also be declared in the
Process Extension.
Pseudocode
The session Generate Planned PRP Orders can generate Planned PRP Orders
based on Project and Control data. Each process has its own table,
so the process extension must be applied on these tables.
Available table fields and external variables
(proc_ext_cost_type) value :
Control Data Material Lines               - tpptc127 (Control Data Material Lines)
variable proc_ext_cost_type = "material"
Control Data Equipment Lines               - tpptc147 (Control Data Equipment Lines)
variable proc_ext_cost_type = "equipment"
Control Data Subcontracting Lines               -
tpptc157 (Control Data Subcontracting Lines)
variable proc_ext_cost_type = "subcontracting"
Below you can find an example how to handle the conditions.
Hook: Declarations
table   ttpptc127       |* Control Data Material Lines
table   ttpptc147       |* Control Data Equipment Lines
table   ttpptc157       |* Control Data Subcontracting Lines
extern          string          proc_ext_cost_type(20)
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_cost_type
case "material":
if <condition on ttpptc127 = true> then
return(true)
endif
break
case "equipment":
if <condition on ttpptc147 = true> then
return(true)
endif
break
case "subcontracting":
if <condition on ttpptc157 = true> then
return(true)
endif
break
default:
break
endcase
return (false)
}
```

## Process Extensions for PlannedServiceActivity

The following process extension(s) is/are available: PlannedServiceActivity.SkipSwitchStatus
