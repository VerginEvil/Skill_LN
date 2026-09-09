# ProductionOrder.SkipWarehouseForMaterialShortage

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2166-2166

```baan
Skips Warehouses when Calculating Shortage.
This process extension is available from 2026.01 (KB3628424).
To implement this process extension, you can use the information below:
Usage:        Process Extension ProductionOrder.SkipWarehouseForMaterialShortage can
be used to skip considering certain warehouses for available material
inventory during the shortage calculation.
Sessions where this Process Extension can be implemented:
- Print Material Shortages by Production Order (tisfc0419m000)
- Release Production Orders (tisfc0204m000)
External variables made available to be used in this Process Extension:
- proc_ext_skip_warehouse_for_mat_shortage_warehouse (Warehouse) (domain
tccwar)
- proc_ext_skip_warehouse_for_mat_shortage_cluster (Cluster) (domain
tcemm.clus)
- proc_ext_skip_warehouse_for_mat_shortage_material (Material) (domain
tcitem)
- proc_ext_skip_warehouse_for_mat_shortage_production_order (Production
Order) (domain tcpdno)
Pseudocode:
Below you can find an example.
Hook: Declarations
Hook: ext.skip
function extern boolean ext.skip()
{
if      <condition on
proc_ext_skip_warehouse_for_mat_shortage_warehouse >
then
return(true)
endif
return (false)
}
```
