# BRA.BrazilianReceipt.MatchReceiptLinesToFiscalDocByWarehouseReceiptArray

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for BRA.BrazilianReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1902-1904

```baan
DLL:   btextrecapi
This function is available from     2025.11 (KB3634230  ).
Syntax: long BRA.BrazilianReceipt.MatchReceiptLinesToFiscalDocByWarehouseReceiptArray(
domain  btncmp           iLogisticCompany,
domain  btlogn           iLogin,
boolean          iMarkToLink,
const   domain  btinh.shpm       iMarkReceiptArray() fixed,
const   domain  btpono           iMarkReceiptLineArray(),
long             iMarkReceiptArrayLength,
boolean          iLinkToFiscalDocument,
domain  btftb.fity       iLinkFiscalIdentificationType,
domain  btfovn           iLinkFiscalIdentificationCode,
domain  btfovn           iLinkNewFiscalIdentificationCode,
domain  btcom.bpid       iLinkBusinessPartner,
domain  btyesno          iLinkElectronicFiscalReference,
domain  btorno           iLinkElectronicFiscalReferenceCode,
domain  btmcs.str50      iLinkNfeLocalizer,
domain  btdocn           iLinkDocumentNumber,
domain  btseri           iLinkSerie,
domain  btdate           iLinkIssueDate,
domain  btdoty           iLinkDocumentType,
domain  btratc           iLinkCurrencyRate,
domain  btyesno          iLinkRelativeReferences,
ref     domain  btmcs.str215     oErrorMessage,
ref     domain  btorno           oFiscalReference,
ref     domain  btmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function Matches Receipt Lines for a given warehouse
receipts array to a Fiscal Document.
It is possible to Mark to Link and Link to Fiscal Document in
the same process.
During this process, the transaction handling is being done in
this function. Retry point, commit transaction and abort
transaction will be handled in this function.
Pre:    No open database transaction.
Do not use NORETIFNOK or dal.set.messages.off() command to get
the correct error message on o.error.message.
Post:   n.a.
Input:  iLogisticCompany                      - Logistic Company
iLogin                                        - Login Name
iMarkToLink                                   - Mark to Link Process [True/False]
iMarkReceiptArray                             - Warehouse Receipt Number Array
iMarkReceiptLineArray                         - Warehouse Receipt Line Array
iMarkReceiptArrayLength                       - Receipt Array Length
iLinkToFiscalDocument                         - Link to Fiscal Document Process
[True/False]
iLinkFiscalIdentificationType
-                                               Fiscal Identification Type
iLinkFiscalIdentificationCode
-                                               Fiscal Identification Code
iLinkNewFiscalIdentificationCode
-                                               New Fiscal Identification Code
iLinkBusinessPartner                          - Business Partner
iLinkElectronicFiscalReference
-                                               Electronic Fiscal Reference
iLinkElectronicFiscalReferenceCode
-                                               Electronic Fiscal Reference Code
iLinkNfeLocalizer                             - NFe Localizer
iLinkDocumentNumber                           - Document Number
(Optional when
iLinkElectronicFiscalReferenceCode is
informed)
iLinkSerie                                    - Serie
(Optional when
iLinkElectronicFiscalReferenceCode is
informed)
iLinkIssueDate                                - Issue Date
(Optional when
iLinkElectronicFiscalReferenceCode is
informed)
iLinkDocumentType                             - Document Type
iLinkCurrencyRate                             - Currency Rate
iLinkRelativeReferences                       - Relative References
Output: oErrorMessage                         - Error message
oFiscalRreference                             - Fiscal reference (when no errors found)
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```

## Public Interfaces for BRA.BrazilianInvoice

The following functions are available: BRA.BrazilianInvoice.CancelInvoice BRA.BrazilianInvoice.CopyInvoice BRA.BrazilianInvoice.PrintPostInvoicesByArray BRA.BrazilianInvoice.PrintPostInvoicesByRange
