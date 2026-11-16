# SalesOrder.SkipAdditionalCostSet

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2245-2247

```baan
Skips Additional Cost Sets when retrieving Additional Cost Set.
This process extension is available from 2025.10 (KB3629872).
To implement this process extension, you can use the information below:
Usage:        Process Extension SalesOrder.SkipAdditionalCostSet can
be used to skip (exclude) particular Additional Cost Sets
when retrieving (determining) an Additional Cost Set for a Sales
Order, Shipment or Price Calculation. Both on header and line level.
Processes where this Process Extension can be implemented:
- Approve Sales Order
- Confirm Shipment
- Save Price Calculation
- (Re)calculate Additional Costs
Fields that are available to be used in this Process Extension
are the underneath fields of table Sales Additional Cost Set
Scenarios (tdsls027):
- Sold-to Business Partner (tdsls027.ofbp)
- Ship-to Business Partner (tdsls027.stbp)
- Item                     (tdsls027.item)
- Cost Set                 (tdsls027.ccos)
- Interactive Adding of Additional Costs (tdsls027.inta)
External variables that are available to be used in this Process
Extension:
- proc_ext_skip_add_cost_set [ type: string(20) ]
Supported values are:
- tdsls400
- tdsls401
- whinh430
- whinh431
- tdpcg200
- tdpcg201
This external variable indicates the context from which the function
is being called.
Additionally, the primary key fields of the relevant object and its
line (if applicable) are populated using the corresponding input
arguments.
Note: tables and external variables must also be declared in the
Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdsls027       |* Sales Additional Cost Set Scenarios
extern          string  proc_ext_skip_add_cost_set(20)
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_skip_add_cost_set
case "tdsls400":
if <condition on tdsls027 = true> then
return(true)
endif
Retrieval (determining) of Additional Cost
Set is called for Sales Order header.
break
case "tdsls401":
if <condition on tdsls027 = true> then
return(true)
endif
Retrieval (determining) of Additional Cost
Set is called for Sales Order Line.
break
case "whinh430":
if <condition on tdsls027 = true> then
return(true)
endif
Retrieval (determining) of Additional Cost
Set is called for Shipment header.
break
case "whinh431":
if <condition on tdsls027 = true> then
return(true)
endif
Retrieval (determining) of Additional Cost
Set is called for Shipment Line.
break
case "tdpcg200":
if <condition on tdsls027 = true> then
return(true)
endif
Retrieval (determining) of Additional Cost
Set is called for Price Calculation header.
break
case "tdpcg201":
if <condition on tdsls027 = true> then
return(true)
endif
Retrieval (determining) of Additional Cost
Set is called for Price Calculation Line.
break
default:
break
endcase
return (false)
}
```
