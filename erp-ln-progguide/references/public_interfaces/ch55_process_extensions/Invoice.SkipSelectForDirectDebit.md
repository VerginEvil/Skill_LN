# Invoice.SkipSelectForDirectDebit

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2063-2064

Skips the invoice during selection for direct debit. This process extension is available from 2026.08 ( KB3677300 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension Invoice.SkipSelectForDirectDebit can be used to skip an
invoice during selection for direct debit.
Sessions where this Process Extension can be implemented:
-                       Select Invoices for Direct Debit (tfcmg4220m000)
Fields that are available to be used in this Process Extension:
-               proc_ext_acp_or_acr     - "acp" for Purchase Invoice or Credit Note.
"acr" for Sales Invoice or Credit Note.
-               proc_ext_schedule       - "true" if selection is done on Schedule level.
"false" if selection is done on Invoice level.
-               proc_ext_inv_comp       - The Invoice Company of the Purchase Invoice/
Sales Invoice/Credit Note.
-               proc_ext_inv_ttyp       - The Transaction Type.
-               proc_ext_inv_docn       - The Document Number.
-               proc_ext_inv_line       - The Invoice Line Number.
-               proc_ext_inv_sch_line   - The Invoice Schedule Line Number.
(Only available if proc_ext_schedule = true)
-               proc_ext_inv_dued       - The Due Date of the Invoice or Schedule Line.
-               proc_ext_inv_bpid       - The Business Partner.
(Either Invoice                                          -from or Invoice-to)
Pseudocode: In the code below,
if the extender defined expression evaluates to true
then the invoice from tfacr500 is skipped
during selection for direct debit.
Hook: Declarations
table   tfacr500
extern          string          proc_ext_acp_or_acr(3)
extern          boolean         proc_ext_schedule
extern  domain  tcncmp          proc_ext_inv_comp
extern  domain  tfgld.ttyp      proc_ext_inv_ttyp
extern  domain  tfgld.docn      proc_ext_inv_docn
extern  domain  tfgld.lino      proc_ext_inv_line
extern  domain  tfgld.schn      proc_ext_inv_sch_line
extern  domain  tfgld.date      proc_ext_inv_dued
extern  domain  tccom.bpid      proc_ext_inv_bpid
Hook: ext.skip
function extern boolean ext.skip()
{
if proc_ext_acp_or_acr = "acr" then
<
read tfacr500 based on the variables:
proc_ext_inv_comp, proc_ext_inv_ttyp,
proc_ext_inv_docn, proc_ext_inv_line
>
if <condition on Process Extension Field = true> then
return(true)
endif
endif
return(false)
}
```
