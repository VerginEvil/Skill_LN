# ProductionOrder.SkipMaterialLineAggregation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2164-2165

```baan
Skip the aggregation of Estimated Material Lines.
This process extension is available from 2025.08 (KB3532174).
To implement this process extension, you can use the information below:
Usage:        Process Extension ProductionOrder.SkipMaterialLineAggregation can be
used to skip the aggregation of estimated material lines during the
creation of the production order.
Sessions where this Process Extension can be implemented:
- Production Order (tisfc0101m100)
Fields that are available to be used in this Process Extension:
Extern Variables used in this process extension:
|* For control of aggregation based on BOM (model or classic)
proc_ext_skip_aggregate_main_item       (main item)
proc_ext_skip_aggregate_bom_model       (bom model)
proc_ext_skip_aggregate_bom_revision    (bom revision)
proc_ext_skip_aggregate_bom_position    (bom position)
|* Variations in context
proc_ext_skip_aggregate_supplied_by_subcon (supplied by subcontractor)
proc_ext_skip_aggregate_customer_furnished (customer furnished)
proc_ext_skip_aggregate_contains_customer_furnished ( contains customer furnished)
|* Properties of the line
proc_ext_skip_aggregate_material_item (material item)
proc_ext_skip_aggregate_operation_number (operation number)
proc_ext_skip_aggregate_bom_level (bom level of material line)
proc_ext_skip_aggregate_lot_selection (lot selection property)
proc_ext_skip_aggregate_backflushing_method (backflushing method)
proc_ext_skip_aggregate_material_control_method(material control method)
proc_ext_skip_aggregate_warehouse (warehouse)
proc_ext_skip_aggregate_qms_standard_test_procedure (QMS Standard Test procedure)
proc_ext_skip_aggregate_engineering_item_revision (Engineering Item Revision)
Pseudocode:
Below you can find an example.
Hook: Declarations
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on proc_ext_skip_aggregate_material_item > then
return(true)
endif
return (false)
}
```
