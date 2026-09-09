# SalesOrder.SkipReleaseToWarehousing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2250-2251

```baan
Skips Sales Order Lines and Sales Order Line Components when Releasing to Warehousing.
This process extension is available from 2019.08 (KB2070268).
To implement this process extension, you can use the information below:
Usage:        Process Extension SalesOrder.SkipReleaseToWarehousing can be used
to skip Sales Order Lines and Sales Order Line Components when
Releasing to Warehousing.
Note: Sales Order Line Components are used when 'Advanced Kitting'
is implemented and Component Handling of the sales order line is
set to 'Component Lines'.
Sessions where this Process Extension can be implemented:
- Release Sales Orders to Warehousing (tdsls4246m000)
- All sessions and processes that trigger the release of lines to
Warehousing (like automatic processing logic).
Fields that are available to be used in this Process Extension:
- All fields of table Sales Order Lines (tdsls401) when releasing
order lines or component lines.
- All fields of table Sales Order Line Components (tdsls463) when
releasing component lines.
External variables that are available to be used in this Process
Extension:
- proc_ext_skip_rtw_so_line_type [ type: string(20) ].
Supported values are:
- order_line
- component_line
Note: tables and external variables must also be declared in the
Process Extension.
The sales order release to warehousing process releases sales order
lines. In case of component handling (tdsls401.cphl =
tdcphl.component.lines), sales order line is selected first and then
the component lines are released.
The sales order line table is tdsls401.
The sales order line components table is tdsls463.
So in case of component lines, skip conditions can be built both on
current tdsls401 data and tdsls463 data as instructed below.
The process extension must be applied to these two tables.
Pseudocode:
Below you can find an example how to handle the conditions for sales
order lines and component lines.
Hook: Declarations
table   ttdsls401       |* Sales Order Lines
table   ttdsls463       |* Sales Order Line Components
extern          string  proc_ext_skip_rtw_so_line_type(20)
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_skip_rtw_so_line_type
case "order_line":
if <condition on tdsls401 = true> then
return(true)
endif
So in case of order_line, component handling
sales order lines can also be skipped based on
tdsls401 data.
break
case "component_line":
if <condition on tdsls463 = true> then
return(true)
endif
AND / OR
if <condition on tdsls401 = true> then
return(true)
endif
So in case of component_line, component lines
can also be skipped based on tdsls401 data.
break
default:
break
endcase
return (false)
}
```
