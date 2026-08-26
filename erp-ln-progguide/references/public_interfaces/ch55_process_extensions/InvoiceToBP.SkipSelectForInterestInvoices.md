# InvoiceToBP.SkipSelectForInterestInvoices

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InvoiceToBP
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2072-2073

Skips Business Partner selection for Interest Invoice. This process extension is available from 2023.09 ( KB2300368 ). Technical information for this process extension:

```baan
Usage:        InvoiceToBP.SkipSelectForInterestInvoices can be used to skip an
Invoice              -to Business Partner for Interest Invoice selection.
A message may be filled, to present information about the skip
decision on the report. This message can have max 70 characters.
Session where this Process Extension can be implemented:
-               Select Inv.-to BP Receipts for Interest Invoices (tfacr5210m000)
Fields that are available to be used in this Process Extension:
-               Primary key fields of tccom112:       tccom112.itbp (Invoice-to Business
Partner)
tccom112.cofc (Department)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttccom112       |* Invoice              -to Business Partners
Hook: ext.skip
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
read data (binded!!) using tccom112.itbp, tccom112.cofc
if <condition on tccom112 = true> then
o.reason = "Invoice                                      -to BP skipped because ..."
return(true)
endif
return (false)
}
```

## Process Extensions for ItemMasterPlan

The following process extension(s) is/are available: ItemMasterPlan.SkipCopyToScenario ItemMasterPlan.SkipCopyToScenarioForPeriod
