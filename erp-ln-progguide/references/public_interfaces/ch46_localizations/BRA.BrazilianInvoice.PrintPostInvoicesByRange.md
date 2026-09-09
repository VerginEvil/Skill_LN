# BRA.BrazilianInvoice.PrintPostInvoicesByRange

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for BRA.BrazilianInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1927-1929

```baan
DLL:   btextsliapi
This function is available from 2025.04 (KB3568308).
Syntax: long BRA.BrazilianInvoice.PrintPostInvoicesByRange(
domain  btncmp           iSalesInvoiceCompany,
domain  btorno           iFiscalReferenceFrom,
domain  btorno           iFiscalReferenceTo,
long             iProcessingOptionSet,
ref             long             oNumberOfInvoicesPrinted,
ref             long             oNumberOfInvoicesPosted,
ref             boolean          oRecordProcessed,
ref             boolean          oProcessStopped,
ref     domain  btmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface print/post a Brazilian invoice for the
given range of fiscal references.
This function can either print (send the XML of the e-invoice
to the Brazilian tax authority) or post the invoices according
to the options.
During this process, the transaction handling is being done in
this function. Retry point, commit transaction and abort
transaction will be handled in this function.
Pre:    No open database transaction.
Post:   n.a.
Input:  iSalesInvoiceCompany    - Company of the Sales Invoice. This is
a mandatory field.
iFiscalReferenceFrom    - Fiscal reference from
iFiscalReferenceTo      - Fiscal reference to
iProcessingOptionSet    - Processing Option have a direct
relationship with the form fields on
session Print/Post Invoices
(btsli2200m100).
This is a mandatory field.
A processing option set can  be
created via a call to
ProcessingOptionSet.Create().
Optinonal arguments:
fiscalDocSeriesFrom     - Fiscal document series from
fiscalDocSeriesTo       - Fiscal document series to
documentTypeFrom        - Document type from
documentTypeTo          - Document type to
fiscalDocTypeCodeFrom   - Fiscal document type code from
fiscalDocTypeCodeTo     - Fiscal document type code to
invFiscalDocTypeFrom    - Invoicing fiscal document type from
invFiscalDocTypeTo      - Invoicing fiscal document type to
creationDateFrom        - Fiscal document creation date from,
used for the invoice print.
creationDateTo          - Fiscal document creation date to,
used for the invoice print.
printingDateFrom        - Fiscal document printing date from,
used for the invoice post.
printingDateTo          - Fiscal document printing date to,
used for the invoice post.
mainSession             - Session which started the process
(for logging purposes).
invoicePrint            - Determine if the invoice should be
printed. This means to send the
e-invoice XML to the Brazilian Tax
Authority (SEFAZ).
invoicePost             - Determine if the invoice should be
posted. The invoice can only be
posted after it is approved by SEFAZ.
printOption             - Print options:
* Draft         - btsli.prno.draft
* Original      - btsli.prno.original
* Reprint       - btsli.prno.reprint
skipErrorCheck          - Skip error check, only allowed for
draft print.
printErrorReport        - Print error report. Always enabled,
except when the option skipErrorCheck
is enabled.
setGoodsMovementDate    - Determine if the e-invoice XML tag
"dhSaiEnt" should be created or not.
progressBar             - Indicates if a progress bar should
be enabled.
successDevice           - Device for printing the report when
the operation is successful.
errorDevice             - Device for printing the report when
the operation is retrieved an error.
NAME                            TYPE                    DEFAULT
|* Selection Range
fiscalDocSeriesFrom             domain  btseri          ""
fiscalDocSeriesTo               domain  btseri          maximum field value
documentTypeFrom                domain  btdoty          minimum field value
documentTypeTo                  domain  btdoty          maximum field value
fiscalDocTypeCodeFrom           domain  btmcs.fdtc      ""
fiscalDocTypeCodeTo             domain  btmcs.fdtc      maximum field value
invFiscalDocTypeFrom            domain  btsli.tdff      minimum field value
invFiscalDocTypeTo              domain  btsli.tdff      maximum field value
creationDateFrom                domain  btdate          0
creationDateTo                  domain  btdate          maximum field value
printingDateFrom                domain  btdate          0
printingDateTo                  domain  btdate          maximum field value
|* Log
mainSession                     domain  btsess          "API"
|* Actions
invoicePrint                    domain  btyesno         btyesno.no
invoicePost                     domain  btyesno         btyesno.no
|* Print
printOption                     domain  btsli.prno      btsli.prno.original
skipErrorCheck                  domain  btyesno         btyesno.no
printErrorReport                domain  btyesno         btyesno.yes
setGoodsMovementDate            domain  btyesno         btyesno.yes
|* Progress bar
progressBar                     domain  btyesno         btyesno.yes
|* Report Devices
successDevice                   domain  btmcs.str14     ""
errorDevice                     domain  btmcs.str14     ""
Output: oNumberOfInvoicesPrinted- Number of invoice printed.
oNumberOfInvoicesPosted - Number of invoice posted.
oRecordProcessed        - Indicates that the range is processed.
oProcessStopped         - Indicates that the process is stopped.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```
