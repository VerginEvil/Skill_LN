# BillableLine.CreateInvoice

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for BillableLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1627-1628

```baan
DLL:   ciextsliapi
This function is available from 2023.12 (KB2306144).
Syntax: long BillableLine.CreateInvoice(
domain  tcncmp           iSalesInvoiceCompany,
domain  tcsli.tinv       iTypeOfInvoice,
domain  tcmcs.long       iBillableLineKeyCollection,
ref     domain  tcmcs.long       oNumberOfInvoicingBatchesPosted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to create an invoice for the
given key collection of billable lines.
If no invoicing batch is linked to a billable line, a new
invoicing batch will be created automatically and will be
processed to create an invoice.
If an invoicing batch is already linked to the billable line,
an invoice will be created for the invoicing batch.
The billable lines linked to the invoicing batch will be
composed, printed and posted.
Number of invoicing batches posted will be returned as an
output.
During this process, the transaction handling is being done in
this function. Retry point, commit transaction and abort
transaction will be handled in this function.
----------------------------------------------------------------
Start of Example of Implementation
Requirement -   Create Invoice for a Manual Sales Invoice.
Solution    -   Read all the confirmed billable lines created
for the manual sales invoice id and create a
billable line key collection.
Pseudocode  -
table   tcisli810       |* Billable Lines
long            collection.key.fields
long            keyfields.object
long            ret
collection.key.fields =
create.keyfields.collection()
select  cisli810.*
from    cisli810
where   cisli810._index1 = {
:i.financial.company,
tcsli.srtp.manual.sales,
:i.manual.sales }
selectdo
keyfields.object =
create.keyfields.object(
"cisli810",
collection.key.fields)
keyfields.to.object(keyfields.object)
endselect
ret = BillableLine.CreateInvoice(
iSalesInvoiceCompany,
iTypeOfInvoice,
collection.key.fields,
oNumberOfInvoicingBatchPosted)
delete.keyfields.collection(collection.key.fields)
End of Example of Implementation
----------------------------------------------------------------
Pre:    No open database transaction.
Post:   Billable line key collection 'iBillableLineKeyCollection'
should be deleted after the public interface has been called.
Use 'delete.keyfields.collection(iBillableLineKeyCollection)'
Input:  iSalesInvoiceCompany    -
Sales Invoice Company.
This is a Mandatory field.
iTypeOfInvoice          -
The Type of Invoice.
This is a Mandatory field.
Possible values : Standard      tcsli.tinv.standard
: Pro Forma     tcsli.tinv.pro.forma
: Customs       tcsli.tinv.customs
: Consignment   tcsli.tinv.consignment
iBillableLineKeyCollection -
Billable line Key Collection
This is a Mandatory field.
Output:
oNumberOfInvoicingBatchesPosted -
Number of Invoicing Batches posted.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Invoice Created.
<> 0                    - Error
```
