# BRA.BrazilianInvoice.CopyInvoice

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for BRA.BrazilianInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1923-1925

```baan
DLL:   btextsliapi
This function is available from 2026.04 (KB3665487).
Syntax: long BRA.BrazilianInvoice.CopyInvoice(
domain  btncmp           iSalesInvoiceCompany,
domain  btorno           iSourceFiscalReference,
domain  btmcs.fdtc       iTargetFiscalDocTypeCode,
domain  btorno           iTargetFiscalReferenceSeries,
long             iProcessingOptionSet,
ref     domain  btorno           oTargetFiscalReference,
ref             long             oNumberOfInvoiceLinesCopied,
ref             boolean          oRecordProcessed,
ref             boolean          oProcessStopped,
ref     domain  btmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface performs a copy of the source invoice to
the target invoice with options.
During this process, the transaction handling is being done in
this function. Retry point, commit transaction and abort
transaction will be handled in this function.
Pre:    No open database transaction.
Post:   The copy results will aways be a manual invoice and the line
type (in case any line is copied) will always be 'Standard'.
Input:  iSalesInvoiceCompany            - Company of the Sales Invoice.
This is a mandatory field.
iSourceFiscalReference          - Source fiscal reference to be
copied. This is a mandatory
field.
iTargetFiscalDocTypeCode        - Target fiscal document type
code. This is a mandatory
field.
iTargetFiscalReferenceSeries    - Target fiscal reference
series. This is a mandatory
field.
The fiscal reference number
group is the default which is
set in the 'Invoicing
Parameters' session,
btsli0100m000.
iProcessingOptionSet            - Processing option have a
direct relationship with the
form fields on session
Copy Invoices (btsli2200m300).
This is a mandatory field.
A processing option set can
be created via a call to
ProcessingOptionSet.Create().
Optinonal arguments:
copyOnlyHeader                  - Indicates if only the invoice
header should be copied.
copyPaymentModeData             - Indicates if the invoice
payment mode data should be
copied
copyRelatedInvoiceData          - Indicates if the invoice
related data should be copied
copyImportationData             - Indicates if the invoice
importation data should be
copied
copyExportationData             - Indicates if the invoice
exportation data should be
copied
copyPackagesData                - Indicates if the invoice
package data should be
copied
copyEinvoiceAuthData            - Indicates if the invoice
NFe authorization data should
be copied
copyHeaderTexts                 - Indicates if the invoice
header texts should be copied
copyLineTaxes                   - Indicates if the invoice
line taxes data should be
copied
copyLinesExportationData        - Indicates if the invoice
lines exportation data should
be copied
copyConstructionWorkData        - Indicates if the invoice
line construction work data
should be copied
copyLineTexts                   - Indicates if the invoice
line texts should be copied
NAME                            TYPE                    DEFAULT
|* Actions
copyOnlyHeader                  domain  btyesno         btyesno.no
copyPaymentModeData             domain  btyesno         btyesno.yes
copyRelatedInvoiceData          domain  btyesno         btyesno.yes
copyImportationData             domain  btyesno         btyesno.yes
copyExportationData             domain  btyesno         btyesno.yes
copyPackagesData                domain  btyesno         btyesno.yes
copyEinvoiceAuthData            domain  btyesno         btyesno.yes
copyHeaderTexts                 domain  btyesno         btyesno.yes
copyLineTaxes                   domain  btyesno         btyesno.yes
copyLinesExportationData        domain  btyesno         btyesno.yes
copyConstructionWorkData        domain  btyesno         btyesno.yes
copyLineTexts                   domain  btyesno         btyesno.yes
Output: oTargetFiscalReference          - Target fiscal reference,
result of the copy process.
oNumberOfInvoiceLinesCopied     - Number of invoice lines
copied.
oRecordProcessed                - Indicates that the record is
processed.
oProcessStopped                 - Indicates that the process is
stopped.
oExceptionMessage               - The last message if any
message is found. If more than
one message is given, these
are present in the
oExceptionID.
oExceptionID                    - An ID that refers to the
exception information. Use the
functions in Exception to get
all relevant information.
Return: 0/DALHOOKERROR
```
