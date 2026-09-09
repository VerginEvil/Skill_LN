# ProjectContract.SkipProcessProFormaInvoices

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProjectContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2176-2179

```baan
Skip Project Contract Transactions to Process Pro Forma Invoices.
This process extension is available from 2023.12 (KB2301699).
To implement this process extension, you can use the information below:
Usage:        Process Extension ProjectContract.SkipProcessProFormaInvoices
can be used to skip processing of pro forma invoices in
Project Contract for invoice types
- Advance Payments,
- Installments,
- Cost Transactions,
- Element Physical Progress,
- Activity Physical Progress,
- Progress Payment Requests,
- Fees and Penalties,
- Extensions,
- Holdback and
- Deliverables.
Session where this Process Extension can be implemented:
- Process Pro Forma Invoices (tppin4200m100)
Fields that are available to be used in this Process Extension:
- All fields of table: Advance Payments (tppin010)
- All fields of table: Installments (tppin020)
- All fields of table: Cost Transactions (tpppc200)
- All fields of table: Element Physical Progress (tpppc150)
- All fields of table: Activity Physical Progress (tpppc160)
- All fields of table: Progress Payment Requests (tppin070)
- All fields of table: Fees and Penalties (tppin080)
- All fields of table: Extensions (tpptc050)
- All fields of table: Holdback (tppin040)
- All fields of table: Deliverables (tppdm700)
External variables that are available to be used in this Process
Extension:
- proc_ext_invoice_type [ type: string(20) ]
Note: tables and external variables must also be declared in the
Process Extension.
Pseudocode
The session Process Pro Forma Invoices can process pro form invoice
transactions for 9 different invoice types. Each invoice
type has its own table, so the process extension must be applied
on these tables. Available table fields and external variables
(proc_ext_invoice_type) value per invoice type:
Advance Payments        - tppin010 (Advance Payments)
variable proc_ext_invoice_type = "advance.payments"
Installments            - tppin020 (Installments)
variable proc_ext_invoice_type = "installments"
Cost-Plus               - tpppc200 (Cost Transactions)
variable proc_ext_invoice_type = "cost.plus"
Unit Rates              - tpppc150 (Element Physical Progress)
- tpppc160 (Activity Physical Progress)
variable proc_ext_invoice_type = "unit.rates"
Progress Payments       - tppin070 (Progress Payment Requests)
variable proc_ext_invoice_type = "progress.payments"
Fees and Penalties      - tppin080 (Fees and Penalties)
variable proc_ext_invoice_type = "fees.and.penalties"
Extensions              - tpptc050 (Extensions)
variable proc_ext_invoice_type = "extensions"
Holdback                - tppin040 (Holdback)
variable proc_ext_invoice_type = "holdback"
Deliverables            - tppdm700 (Deliverables)
variable proc_ext_invoice_type = "deliverables"
Below you can find an example how to handle the conditions per invoice
type.
Hook: Declarations
table   ttppin010       |* Advance Payments
table   ttppin020       |* Installments
table   ttpppc200       |* Cost Transactions
table   ttpppc150       |* Element Physical Progress
table   ttpppc160       |* Activity Physical Progress
table   ttppin070       |* Progress Payment Requests
table   ttppin080       |* Fees and Penalties
table   ttpptc050       |* Extensions
table   ttppin040       |* Holdback
table   ttppdm700       |* Deliverables
extern          string          proc_ext_invoice_type(20)
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_invoice_type
case "advance.payments":
if <condition on tppin010 = true> then
return(true)
endif
break
case "installments":
if <condition on tppin020 = true> then
return(true)
endif
break
case "cost.plus":
if <condition on tpppc200 = true> then
return(true)
endif
break
case "unit.rates":
if <condition on tpppc150 = true> or
<condition on tpppc160 = true> then
return(true)
endif
break
case "progress.payments":
if <condition on tppin070 = true> then
return(true)
endif
break
case "fees.and.penalties":
if <condition on tppin080 = true> then
return(true)
endif
break
case "extensions":
if <condition on tpptc050 = true> then
return(true)
endif
break
case "holdback":
if <condition on tppin040 = true> then
return(true)
endif
break
case "deliverables":
if <condition on tppdm700 = true> then
return(true)
endif
break
default:
break
endcase
return (false)
}
```
