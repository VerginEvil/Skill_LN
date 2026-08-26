# InvoicingBatch.CreateInvoice

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for InvoicingBatch
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1605-1606

```baan
DLL:   ciextsliapi
This function is available from     2023.12 (KB2306144  ).
Syntax: long InvoicingBatch.CreateInvoice(
domain  tcncmp           iSalesInvoiceCompany,
domain  tcsli.tinv       iTypeOfInvoice,
domain  tcorno           iInvoicingBatchFrom,
domain  tcorno           iInvoicingBatchTo,
ref     domain  tcmcs.long       oNumberOfInvoicingBatchesPosted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to create an invoice for the
given range of Invoicing Batches.
The billable lines linked to the invoicing batch will be
composed, printed and posted. Number of invoicing batches
posted will be returned as an output.
During this process, the transaction handling is being done in
this function. Retry point, commit transaction and abort
transaction will be handled in this function.
Pre:    No open database transaction.
Post:   NA
Input:  iSalesInvoiceCompany                  -
Sales Invoice Company.
This is a Mandatory field.
iTypeOfInvoice                                -
The Type of Invoice.
This is a Mandatory field.
Possible values : Standard      tcsli.tinv.standard
: Pro Forma     tcsli.tinv.pro.forma
: Customs       tcsli.tinv.customs
: Consignment   tcsli.tinv.consignment
iInvoicingBatchFrom                           -
Invoicing Batch from
iInvoicingBatchTo                             -
Invoicing Batch to
This is a Mandatory field.
Output:
oNumberOfInvoicingBatchesPosted                       -
Number of Invoicing Batches posted.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Invoice Created.
<> 0                                          - Error
```

## Public Interfaces for BillableLine

The following functions are available: BillableLine.Compose BillableLine.CreateInvoice BillableLine.UpdateStatus
