# Invoice.SkipPrintInvoice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2080-2081

```baan
Skips Printing Invoice.
This process extension is available from 2021.03 (KB2176978).
To implement this process extension, you can use the information below:
Usage:        Process Extension Invoice.SkipPrintInvoice can be used
to skip invoices when printing the invoices in Central Invoicing.
Sessions where this Process Extension can be implemented:
- Print Invoices (cisli2400m000, cisli2405m000 )
Fields that are available to be used in this Process Extension:
- Key fields of cisli305        - cisli305.sfcp (Financial Company)
- cisli305.tran (Transaction Type)
- cisli305.idoc (Invoice Number)
Those fields can be used to read table cisli305 (binded)
- proc_ext_print_option         Indicates if a draft or original invoice
is printed or a reprint is done.
possible values are:
- cisli.prno.draft
- cisli.prno.original
- cisli.prno.reprint
Note: tables must also be declared in the Process Extension.
Pseudocode:
In de code below reprinting of an invoice with InvoiceTo Business Partner
"TDCUS0014" is skipped.
Hook: Declarations
table tcisli305
extern  domain  cisli.prno      proc_ext_print_option
domain  tccom.bpid      invoice.to.bp
Hook: ext.skip
function extern boolean ext.skip()
{
invoice.to.bp = ""
on case proc_ext_print_option
case    cisli.prno.draft:
case    cisli.prno.original:
break
case    cisli.prno.reprint:
select  cisli305.itbp:invoice.to.bp
from    cisli305
where   cisli305._index1 = {    :cisli305.sfcp,
:cisli305.tran,
:cisli305.idoc}
as set with 1 rows
selectdo
if invoice.to.bp = "TDCUS0014" then
return(true)
endif
endselect
break
default:
break
endcase
return (false)
}
```
