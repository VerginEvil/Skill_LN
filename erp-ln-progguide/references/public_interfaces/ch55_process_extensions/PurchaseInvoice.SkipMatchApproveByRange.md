# PurchaseInvoice.SkipMatchApproveByRange

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2167-2169

Skips Purchase Invoice for Matching or Approval. This process extension is available from 2026.04 ( KB3665487 ). Technical information for this process extension:

```baan
Usage:        PurchaseInvoice.SkipMatchApproveByRange can be used to skip a Purchase
Invoice for matching or approval during Matching/Approving Purchase
Invoices by Range.
A message may be filled, to present information about the skip
decision on the report. This message can have max 70 characters.
Session where this Process Extension can be implemented:
-                Match/Approve Purchase Invoices by Range (tfacp2280m000)
Fields that are available to be used in this Process Extension:
-               proc_ext_action               - Indicates the current action
-                                               which is performed.
-                                               Possible Values:
"match": match a Purchase Invoice
"submit": submit a Purchase Invoice for Workflow
"approve": approve a Purchase Invoice
-               Primary key fields of tfacp500        -       tfacp500.fcom
-                                                            tfacp500.ttyp
-                                                            tfacp500.ninv
-                                                            tfacp500.line
Note: filled if proc_ext_action
= "match"
-               Primary key fields of tfacp200        -       tfacp200.ttyp
-                                                            tfacp200.ninv
-                                                            tfacp200.line
-                                                            tfacp200.tdoc
-                                                            tfacp200.docn
-                                                            tfacp200.lino
Note: filled if proc_ext_action
= "submit" or "approve".
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfacp200       |* Open Items (Purchase Invoices and Payments)
table   ttfacp500       |* Open Items A/P
extern  domain  tcmcs.str10m    proc_ext_action
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if proc_ext_action = "match" then
|* During selecting Purchase Invoice in tfacp500
read tfacp500 (binded!)
if <condition on tfacp500 = true> then
o.reason = "Skipped Purchase Invoice because....."
return(true)
endif
endif
if proc_ext_action <> "match" then
|* During selecting Purchase Invoice in tfacp200
read tfacp200 (binded!)
if <condition on tfacp200 = true> then
o.reason = "Skipped Purchase Invoice because....."
return(true)
endif
endif
return (false)
}
```

## Process Extensions for PurchaseOrder

The following process extension(s) is/are available: PurchaseOrder.HandleAdditionalActionsAfterPrint PurchaseOrder.SkipApprove PurchaseOrder.SkipPrint PurchaseOrder.SkipPrintPurchaseInvoice PurchaseOrder.SkipPrintPurchaseOrder PurchaseOrder.SkipPrintReceivableInvoice PurchaseOrder.SkipReleaseToWarehousing
