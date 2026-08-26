# PurchaseRequisition.SkipConvert

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseRequisition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2189-2191

Skips Purchase Requisition when Converting. This process extension is available from 2026.05 ( KB3660439 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PurchaseRequisition.SkipConvert can be used
to skip Purchase Requisition (Line)s when Converting to Purchase
Orders or Requests for Quotation.
Session where this Process Extension can be implemented:
-               Convert Purchase Requisitions (tdpur2201m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Purchase Requisitions (tdpur200)
-               All fields of table Purchase Requisition Lines (tdpur201)
External variable that is available to be used in this Process Extension:
-               proc_ext_skip_convert_requisition_for_commingle [ type: boolean ].
Supported values are:
-                       true (commingle)
-                       false (non-commingle)
Note: Tables and external variable must also be declared in the Process Extension.
Skip conditions can be built on current tdpur200 and tdpur201 data as
instructed below.
Pseudocode:
Below you can find an example how to handle the conditions for purchase
requisition
(line)s.
Hook: Declarations
table   tdpur200        |* Purchase Requisitions
table   tdpur201        |* Purchase Requisition Lines
extern          boolean proc_ext_skip_convert_requisition_for_commingle
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_skip_convert_requisition_for_commingle
case true:
|* If Commingle is checked.
if <condition on tdpur200 and/or tdpur201 = true> then
return(true)
endif
break
case false:
|* If Commingle is unchecked.
if <condition on tdpur200 and/or tdpur201 = true> then
return(true)
endif
break
endcase
return (false)
}
```

## Process Extensions for PurchaseSelfBilledInvoice

The following process extension(s) is/are available: PurchaseSelfBilledInvoice.CustomCompose
