# SalesOrderInvoiceLine.SkipReleaseToInvoicing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderInvoiceLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2233-2234

Skips Sales Order Invoice Line when Releasing to Invoicing. This process extension is available from 2025.07 ( KB3570312 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesOrderInvoiceLine.SkipReleaseToInvoicing can be used
to skip specific Sales Order Invoice Lines when Releasing to Invoicing.
Sessions where this Process Extension can be implemented:
-               Release Sales Orders/Schedules to Invoicing (tdsls4247m000) for option 'Release
Order'
-               Print Sales Draft Invoices (tdsls4447m000) for option 'Print Order'
-               All sessions and processes that trigger the release of sales order invoice lines
(like automatic processing logic).
Fields that are available to be used in this Process Extension:
-               All fields of table Sales Order Actual Delivery Lines (tdsls406)
-               All fields of table Linked Ord. Line Data for Invoicing (tdsls408)
Note: Tables must also be declared in the Process Extension.
So skip conditions can be built on current tdsls406 and tdsls408 data
as instructed below.
Table tdsls408 is used for invoicing sales order lines within a set.
If a sales order line that is part of a set is skipped for invoicing,
all other sales order lines within that set are also skipped.
Pseudocode:
Here you can find an example how to handle the conditions for sales
order lines.
Hook: Declarations
table   ttdsls406       |* Sales Order Actual Delivery Lines
table   ttdsls408       |* Linked Ord. Line Data for Invoicing
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls406 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for SalesOrderLine

The following process extension(s) is/are available: SalesOrderLine.AllowDisplaySelectedContract SalesOrderLine.AllowSaveInCaseOfInsufficientATP SalesOrderLine.SkipGenerateProjectStructure SalesOrderLine.SkipPrint SalesOrderLine.SkipPrintAcknowledgement
