# PurchaseConsumption.SkipGenerateSelfBillingInvoice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseConsumption
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2166-2167

Skip purchase consumption when generating self - billing purchase invoices. This process extension is available from 2025.04 ( KB3568308 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PurchaseConsumption.SkipGenerateSelfBillingInvoice
can be used to skip purchase consumption when generating self              -billing
purchase invoices.
Sessions where this Process Extension can be implemented:
-                       Generate Self-Billing Purchase Invoices (tfacp2290m000)
Fields that are available to be used in this Process Extension:
-                       Purchase Consumptions (tfacp249)
-                       Order Data for Approval (tfacp240)
Pseudocode: In the code below,
if the extender defined expression evaluates to true
then the purchase consumption from tfacp249 is skipped
when generating self                          -billing purchase invoices.
Hook: Declarations
table   tfacp249
table   tfacp240
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tfacp249 = true> then
return(true)
endif
return(false)
}
```

## Process Extensions for PurchaseInvoice

The following process extension(s) is/are available: PurchaseInvoice.SkipMatchApproveByRange
