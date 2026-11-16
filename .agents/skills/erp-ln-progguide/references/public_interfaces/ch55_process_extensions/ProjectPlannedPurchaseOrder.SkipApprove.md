# ProjectPlannedPurchaseOrder.SkipApprove

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProjectPlannedPurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2186-2187

```baan
Skips Planned Purchase Orders in Project for Material, Equipment and Subcontracting when
Approving.
This process extension is available from 2019.09 (KB2076283).
To implement this process extension, you can use the information below:
Usage:        Process Extension ProjectPlannedPurchaseOrder.SkipApprove can be used
to skip Planned Purchase Orders in Project for cost types Material,
Equipment and Subcontracting when Approving.
Sessions where this Process Extension can be implemented:
- Approve Planned PRP Purchase Orders (tppss6220m000)
Fields that are available to be used in this Process Extension:
- All fields of table: Planned PRP Purchase Orders - Material (tppss610)
- All fields of table: Planned PRP Purchase Orders - Equipment (tppss611)
- All fields of table: Planned PRP Purchase Orders - Subcontracting (tppss612)
External variables that are available to be used in this Process
Extension:
- proc_ext_cost_type [ type: string(20) ]
Note: tables and external variables must also be declared in the
Process Extension.
Pseudocode
The session Approve Planned PRP Purchase Orders can approve planned
orders for 3 cost types: Material, Equipment and Subcontracting. Each
cost type has its own table, so the process extension must be applied
on these 3 tables. Available table fields per cost type:
- Material       - tppss610 (variable proc_ext_cost_type = "material")
- Equipment      - tppss611 (variable proc_ext_cost_type = "equipment")
- Subcontracting - tppss612 (variable proc_ext_cost_type = "subcontracting")
Below you can find an example how to handle the conditions per cost
type.
Hook: Declarations
table   ttppss610       |* Planned PRP Purchase Orders (Material)
table   ttppss611       |* Planned PRP Purchase Orders (Equipment)
table   ttppss612       |* Planned PRP Purchase Orders (Subcontracting)
extern          string          proc_ext_cost_type(20)
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_cost_type
case "material":
if <condition on tppss610 = true> then
return(true)
endif
break
case "equipment":
if <condition on tppss611 = true> then
return(true)
endif
break
case "subcontracting":
if <condition on tppss612 = true> then
return(true)
endif
break
default:
break
endcase
return (false)
}
```
