# ProductVariant.SkipRefreshCPQ

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2174-2175

```baan
Skips Refresh CPQ Rules Set.
This process extension is available from 2026.06 (KB3617511).
To implement this process extension, you can use the information below:
Usage:                Process Extension ProductVariant.SkipRefreshCPQ can be used
to skip certain Product Variants to Skip the CPQ Rules Set.
Where this Process Extension can be implemented:
Sales Orders /Sales Quotations BOD
Fields that are available to be used in this Process Extension:
Extern Variables used in this process extension
proc_ext_skip_refreshcpq_item
proc_ext_skip_refreshcpq_original_product_variant
proc_ext_skip_refreshcpq_new_product_variant
proc_ext_skip_refreshcpq_in_crm_scenario
Pseudocode:
Below you can find an example.
Hook: Declarations
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on proc_ext_skip_refreshcpq_original_product_variant
> then
return(true)
endif
return (false)
}
```
