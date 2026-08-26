# SalesCheckInventory.SkipShortageLine

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesCheckInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2216-2218

Skips Sales Order Inventory Shortage Lines during Sales Check Inventory. This process extension is available from 2021.04 ( KB2181351 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesCheckInventory.SkipShortageLine can be used
to skip Sales Order Inventory Shortage Lines during Sales Check
Inventory.
Note: Shortage lines can be present for Sales Order Lines and Sales
Order Line Components. Sales Order Line Components are used when
'Advanced Kitting' is implemented and Component Handling of the
sales order line is set to 'Component Lines'.
Shortage Lines for Sales Quotes are not supported/handled in this flow.
Session where this Process Extension can be implemented:
-               Check Inventory Sales Orders (tdsls4217m000)
Fields that are available to be used in this Process Extension:
-               Only the primary key fields of the Sales Order Inventory Shortage
Lines (tdsls417) are current. These fields are:
-                       tdsls417.orno
-                       tdsls417.pono
-                       tdsls417.sqnb
-                       tdsls417.csqn
-                       tdsls417.koor - Applicable values in this process are
'Sales Order Line' and
'Sales Order Line Component'
The Check Inventory Sales Orders process checks and rechecks
(if applicable) the inventory for sales order lines and sales order
component lines, based on shortage lines in table tdsls417. The primary
key fields of this table are current and can e.g., be used to read data
from the sales order (line) and also sales order component line in case
of component handling to build skip conditions.
External variables that are available to be used in this Process
Extension:
-               proc_ext_skip_shortage_line_rechecking [ type: boolean ].
Supported values are:
-                       True  - The process is rechecking inventory for (promised)
lines.
-                       False - The process is checking the inventory for lines.
Note: tables and external variables must also be declared in the
Process Extension.
Pseudocode:
Below you can find an example how to handle the conditions for sales
order lines and component lines.
Hook: Declarations
table   ttdsls417       |* Sales Order Inventory Shortage Lines
table   ttdsls401       |* Sales Order Lines
table   ttdsls463       |* Sales Order Line Components
extern  boolean         proc_ext_skip_shortage_line_rechecking
Hook: ext.skip
function extern boolean ext.skip()
{
on case tdsls417.koor
case tdsls.koor.sls.line:       |* Sales Order Line
read data using tdsls417.orno, tdsls417.pono,
tdsls417.sqnb
if <condition on the data read = true> then
return(true)
endif
break
case tdsls.koor.sls.line.comp:   |* Sales Order Line Component
read data using tdsls417.orno, tdsls417.pono,
tdsls417.sqnb, tdsls417.csqn
if <condition on the data read = true> then
return(true)
endif
So in case of a component line, component lines
can also be skipped based on tdsls401 data
if the data is read.
break
default:
break
endcase
return (false)
}
```

## Process Extensions for SalesContract

The following process extension(s) is/are available: SalesContract.SkipPrintSalesContract
