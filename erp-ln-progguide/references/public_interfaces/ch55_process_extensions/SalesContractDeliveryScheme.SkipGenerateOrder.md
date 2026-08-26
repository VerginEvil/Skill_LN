# SalesContractDeliveryScheme.SkipGenerateOrder

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesContractDeliveryScheme
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2219-2220

Skips Sales Contract Delivery Scheme Lines when Generating Sales Order. This process extension is available from 2023.04 ( KB2286306 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesContractDeliveryScheme.SkipGenerateOrder can be
used to skip Sales Contract Delivery Scheme Lines when Generating Sales
Order.
Sessions where this Process Extension can be implemented:
-               Generate Sales Orders from Delivery Schemes (tdsls3204m000)
-               Sales Contract Delivery Lines (tdsls3104m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Sales Contracts (tdsls300)
-               All fields of table Sales Contract Lines (tdsls301)
-               All fields of table Sales Contract Delivery Lines (tdsls304)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttdsls304       |* Sales Contract Delivery Lines
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls304 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for SalesOrder

The following process extension(s) is/are available: SalesOrder.DetermineSupplier SalesOrder.SkipAdditionalCostSet SalesOrder.SkipApprove SalesOrder.SkipPrint SalesOrder.SkipPrintAcknowledgement SalesOrder.SkipReleaseToWarehousing
