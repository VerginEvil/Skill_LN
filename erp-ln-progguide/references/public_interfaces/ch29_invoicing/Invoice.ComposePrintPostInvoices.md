# Invoice.ComposePrintPostInvoices

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1589-1591

```baan
DLL:   ciextsliapi
This function is available from     2024.12 (KB3529255  ).
Syntax: long Invoice.ComposePrintPostInvoices(
domain  tcncmp           iSalesInvoiceCompany,
domain  cisli.rbrs       iRecurringInvoicingBatch,
domain  tcdate           iCutoffDate,
domain  tcsli.tinv       iTypeOfInvoice,
domain  tcorno           iInvoicingBatchFrom,
domain  tcorno           iInvoicingBatchTo,
boolean          iUseNextOpenPeriod,
long             iProcessingOptionSet,
ref             long             oNumberOfInvoicingBatchesComposed,
ref             long             oNumberOfInvoicingBatchesDecomposed,
ref             long             oNumberOfInvoicingBatchesSubmitted,
ref             long
oNumberOfInvoicingBatchesSubmittedToExternalSystem,
ref             long             oNumberOfInvoicingBatchesPrinted,
ref             long             oNumberOfInvoicingBatchesPosted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to execute compose/print/post
process for the given invoicing batches.
Pre:    No open database transaction.
Post:   Not Applicable
Input:  iSalesInvoiceCompany                  - Company of the Sales Invoice
This is a Mandatory field.
iRecurringInvoicingBatch                      - Recurring Invoicing Batch
iCutoffDate                                   - Cut-off Date
iTypeOfInvoice                                - Type of Invoice
This is a Mandatory field.
Possible values : Standard      tcsli.tinv.standard
: Pro Forma     tcsli.tinv.pro.forma
: Customs       tcsli.tinv.customs
: Consignment   tcsli.tinv.consignment
iInvoicingBatchFrom                           - Invoicing Batch From
iInvoicingBatchTo                             - Invoicing Batch To
iUseNextOpenPeriod                            - Use Next Open Periods.
This is only applicable for Invoice
Date and Post Transaction Entry Date.
Possible Values : True                               - If the period is closed for the
given Invoice Date or Post
Transaction Entry Date then
the next open period will be
assigned.
false                                                 - If the period is closed for the
given Invoice Date or Post
Transaction Entry Date then
the process will stop and
error message will be given.
iProcessingOptionSet                          - Processing Option Set
This is a Mandatory field.
A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form
fields on session Compose/Print/Post Invoices (cisli2200m000)
and are not explained in further detail here. Please refer to
the session help for additional information.
Processing Options which are set while on session cisli2200m000
the option is not applicable are ignored.
NAME                                    TYPE                    DEFAULT
|* Actions
invoiceCompose                          domain tcyesno          tcyesno.no
invoiceDate                             domain tcdate           utc.num()
invoiceUndoCompose                      domain tcyesno          tcyesno.no
invoiceDelete                           domain tcyesno          tcyesno.no
invoiceSubmit                           domain tcyesno          tcyesno.no
invoiceSubmitToExternalSystem           domain tcyesno          tcyesno.no
invoicePrint                            domain tcyesno          tcyesno.no
invoicePost                             domain tcyesno          tcyesno.no
invoicePrintTransactionEntryDate        domain tcdate           0
invoicePostTransactionEntryDate         domain tcdate           0
|* Print
invoicePrintOption                      domain cisli.prno       cisli.prno.not.appl
invoicePrintinEuro                      domain  tcyesno         tcyesno.no
invoicePrintDeliveryMethod              domain tcyesno          tcyesno.no
invoicePrintToSingleFile                domain tcyesno          tcyesno.no
invoicePrintOriginalCreditNote          domain tcyesno          tcyesno.no
invoicePrintSequence                    domain cisli.psco       ""
|* Output Devices
invoicePrintDevice                      domain cisli.devc       ""
invoicePostingDevice                    domain cisli.devc       ""
invoiceExceptionsDevice                 domain cisli.devc       ""
Output: oNumberOfInvoicingBatchesComposed               -
Number of invoicing batch composed.
oNumberOfInvoicingBatchesDecomposed                       -
Number of invoicing batch decomposed.
oNumberOfInvoicingBatchesSubmitted                       -
Number of invoicing batch submitted.
oNumberOfInvoicingBatchesSubmittedToExternalSystem                       -
Number of invoicing batch submitted to
external system.
oNumberOfInvoicingBatchesPrinted                       -
Number of invoicing batch printed.
oNumberOfInvoicingBatchesPosted                       -
Number of invoicing batch posted
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     -
<> 0                                          - Error
```
