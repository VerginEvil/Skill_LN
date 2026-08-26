# TargetPrices.SkipCalculateOrderLines

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TargetPrices
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2258-2260

Skips Purchase Order Lines when Calculating Target Prices. This process extension is available from 2024.12 ( KB3540096 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension TargetPrices.SkipCalculateOrderLines can be used to
skip Purchase Order Lines when Calculating Target Prices.
Sessions where this Process Extension can be implemented:
-               Calculate Target Prices (tdpcg0233m100)
External variables that are available to be used in this Process
Extension:
-               proc_ext_skip_calc_po_lines_is_history_line [ type: boolean ]
Supported values are:
-                       true          Current record is an order line from
table Purchase Order Line History (tdpur451)
-                       false         Current record is a normal order line from
table Purchase Order Lines (tdpur401)
-               proc_ext_skip_calc_po_lines_search_criterion [ type: domain tdpcg.tpsp ]
Supported values are:
-                       tdpcg.tpsp.order.lowest       Purchase Order Price (Lowest)
-                       tdpcg.tpsp.order.most.rec     Purchase Order Price (Most Recent)
-                       tdpcg.tpsp.order.average      Purchase Order Price (Average)
Fields that are available to be used in this Process Extension:
-               When variable proc_ext_skip_calc_po_lines_is_history_line = false:
The primary key fields of table tdpur401 (Purchase Order Lines):
-                       tdpur401.orno                 Purchase Order
-                       tdpur401.pono                 Line
-                       tdpur401.sqnb                 Sequence
-               When variable proc_ext_skip_calc_po_lines_is_history_line = true:
The primary key fields of table tdpur451 (Purchase Order Line History):
-                       tdpur451.orno                 Purchase Order
-                       tdpur451.pono                 Line
-                       tdpur451.sqnb                 Sequence
-                       tdpur451.trdt                 Transaction Date
-                       tdpur451.ckor                 Record Type
-                       tdpur451.sern                 Sequence Number
Note: tables and external variables must also be declared in the
Process Extension.
The Calculate Target Prices logic processes Purchase Order Lines for
a range of Items and Order Dates when one or more of the Search Options
"Purchase Order Price (Lowest)", "Purchase Order Price (Most Recent)"
and "Purchase Order Price (Average)" are selected in session 'Calculate
Target Prices' (tdpcg0233m100).
With this Process Extension it is possible to skip Purchase Order Lines
or all lines of a Purchase Order for each of these Search Options. When
the option "Include History" is checked, the Purchase Order Line History
is also processed.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdpur400       |* Purchase Orders
table   ttdpur401       |* Purchase Order Lines
table   ttdpur450       |* Purchase Order History
table   ttdpur451       |* Purchase Order Line History
extern          boolean
proc_ext_skip_calc_po_lines_is_history_line
extern  domain  tdpcg.tpsp
proc_ext_skip_calc_po_lines_search_criterion
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_skip_calc_po_lines_search_criterion
case tdpcg.tpsp.order.lowest:
|* Skip Order line based on Order header data
|*                                       - Read Purchase Order (tdpur400) if
|*   proc_ext_skip_calc_po_lines_is_history_line = false
|*   using tdpur401.orno
|*                                       - Read Purchase Order History (tdpur450) if
|*   proc_ext_skip_calc_po_lines_is_history_line = true
|*   using tdpur451.orno
Read order data (tdpur400/tdpur450)
if <condition on tdpur400/tdpur450 = true> then
return(true)
endif
AND / OR
|* Skip order line based on Order Line data
|*                                       - Read Purchase Order Lines (tdpur401) if
|*   proc_ext_skip_calc_po_lines_is_history_line = false
|*   using tdpur401.orno
|*         tdpur401.pono
|*         tdpur401.sqnb
|*                                       - Read Purchase Order Line History (tdpur451) if
|*   proc_ext_skip_calc_po_lines_is_history_line = true
|*   using tdpur451.orno
|*         tdpur451.pono
|*         tdpur451.sqnb
|*         tdpur451.trdt
|*         tdpur451.ckor
|*         tdpur451.sern
Read order line (history) data (tdpur401/tdpur451)
if <condition on tdpur401/tdpur451 = true> then
return(true)
endif
break
case tdpcg.tpsp.order.most.rec:
Specify another condition or use the same as above
break
case tdpcg.tpsp.order.average:
Specify another condition or use the same as above
break
default:
break
endcase
return(false)
}
```

## Process Extensions for Tax

The following process extension(s) is/are available: Tax.ExternalTaxProviderHandling Tax.FlexibleFieldsVertex
