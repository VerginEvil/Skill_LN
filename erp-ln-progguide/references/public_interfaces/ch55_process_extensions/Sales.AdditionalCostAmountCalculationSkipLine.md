# Sales.AdditionalCostAmountCalculationSkipLine

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2229-2232

```baan
Skips lines when calculating total amounts and quantities during Additional Costs Line
determination.
This process extension is available from 2026.09 (KB3688067).
To implement this process extension, you can use the information below:
Usage:        Process extension Sales.AdditionalCostAmountCalculationSkipLine can be
used to exclude specific lines from total amount and total quantity
calculations. After these totals have been calculated, they determine
which Additional Cost Set Lines, if any, are applied.
Processes where this Process Extension can be implemented:
- Approve Sales Order
- Save Price Calculation
- (Re)calculate Additional Costs
- Simulation (e.g. from REST-api)
External variables that are available to be used in this Process
Extension:
- td_proc_ext_option_set_for_sales_add_cost_amount_skip_line [ type: long
]
This external variable is filled by LN whenever this
process extension is called. It contains a reference
to a Processing Option Set.
This Option Set can be used to obtain the context of the
call (e.g. sales order or price calculation)
Read it using ProcessingOptionSet.Read()
in DLL tcextextapi.
Supported Processing Options and their type:
NAME                            TYPE
SalesOrder                      domain  tcorno
PriceCalculation                domain  tcorno
Line                            domain  tcpono
Sequence                        domain  tcpono
SoldToBP                        domain  tccom.bpid
HeaderInvoiceToBP               domain  tccom.bpid
OrderCurrency                   domain  tcccur
HeaderDiscount                  domain  tcdisc
OrderType                       domain  tccotp
SalesOffice                     domain  tccwoc
BPForPricing                    domain  tccom.bpid
PriceList                       domain  tccplt
DirectDeliveryPriceList         domain  tccplt
Area                            domain  tccreg
PaymentMethod                   domain  tcpaym
SalesOrderOrigin                domain  tdsls.corg
FinancialDepartment             domain  tccwoc
FinancialCompany                domain  tcncmp
ShipToBP                        domain  tccom.bpid
Item                            domain  tcitem
Site                            domain  tcsite
ComponentHandling               domain  tdcphl
EffectivityUnit                 domain  tcuef.effn
ProductVariant                  domain  tccpva
DeliveryType                    domain  tdsls.dltp
Payment                         domain  tcpmnt
Channel                         domain  tcmcs.chan
DeliveryTerms                   domain  tccdec
Contract                        domain  tccono
ContractLine                    domain  tcpono
ContractOffice                  domain  tccwoc
OrderedQuantity                 domain  tcqsl1
OrderedQuantityInInventoryUnit  domain  tcqrd1
OrderDate                       domain  tcdate
PlannedDeliveryDate             domain  tcdate
OrderLineAmount                 domain  tcamnt
HazardousMaterial                       boolean
Explanation for some of the supported Processing Options:
SalesOrder
- The Sales Order. If filled, then this
refers to a Sales Order context.
Note that most of the other attributes
will be empty in that case.
PriceCalculation
- The Price Calculation If filled, then this
refers to a Price Calculation context.
Note that most of the other attributes
will be empty in that case.
Line
- The meaning depends on the context
in which the additional cost set is
retrieved:
* Sales Order context:
Line refers to the sales order line.
* Price Calculation context:
Line refers to the price calculation
line.
See also Sequence.
Sequence
- Belongs to the same context as Line.
Note that if both the SalesOrder and the
PriceCalculation are empty, then this refers to
a simulation context. Most of the other
attributes will have a non-empty value in that
case.
Note: External variables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
extern          long
td_proc_ext_option_set_for_sales_add_cost_amount_skip_line
Hook: ext.skip
function extern boolean ext.skip()
{
|* Read the context
ret = ProcessingOptionSet.Read(
td_proc_ext_option_set_for_sales_add_cost_amount_skip_line,
exception.message1,
exception.id1,
|* option name                  option-variable                 option
default
"SalesOrder",                   sales.order,                    "",
"PriceCalculation",             price.calculation,              "",
"Line",                         line,                           0,
"Sequence",                     sequence,                       0,
"SoldToBP",                     sold.to.bp,                     "",
"HeaderInvoiceToBP",            header.invoice.to.bp,           "",
"OrderCurrency",                header.order.currency,          "",
"HeaderDiscount",               header.discount,                0,
"OrderType",                    header.order.type,              "",
"SalesOffice",                  header.sales.office,            "",
"BPForPricing",                 header.bp.prices.discounts,     "",
"PriceList",                    header.price.list,              "",
"DirectDeliveryPriceList",      header.direct.delivery.price.list,
"",
"Area",                         header.area,                    "",
"PaymentMethod",                header.payment.method,          "",
"SalesOrderOrigin",             sales.order.origin,             empty,
"FinancialDepartment",          header.financial.department,    "",
"FinancialCompany",             financial.company,              0,
"ShipToBP",                     ship.to.bp,                     "",
"Item",                         item,                           "",
"Site",                         site,                           "",
"ComponentHandling",            component.handling,             empty,
"EffectivityUnit",              effectivity.unit,               0,
"ProductVariant",               product.variant,                0,
"DeliveryType",                 delivery.type,                  empty,
"Payment",                      payment,                        empty,
"Channel",                      channel,                        "",
"DeliveryTerms",                delivery.terms,                 "",
"Contract",                     contract.number,                "",
"ContractLine",                 contract.position,              0,
"ContractOffice",               contract.office,                "",
"OrderedQuantity",              ordered.quantity,               0.0,
"OrderedQuantityInInventoryUnit",       quantity.in.inv.unit,   0.0,
"OrderDate",                    order.date,                     0,
"PlannedDeliveryDate",          planned.delivery.date,          0,
"OrderLineAmount",              order.line.amount,              0.0,
"HazardousMaterial",            hazardous.material,             false)
if <some.condition> then
|* Skip
return(true)
endif
return(false)
}
```
