# Invoice.ReprintV2

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1611-1612

```baan
DLL:   ciextsliapi
This function is available from 2026.10 (KB3699767).
Syntax: long Invoice.ReprintV2(
domain  tcncmp           iSalesInvoiceCompany,
domain  tcsli.tinv       iTypeOfInvoice,
domain  tcncmp           iFinancialCompany,
domain  tfgld.ttyp       iInvoiceTransactionType,
domain  tfgld.docn       iInvoiceDocumentNumber,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tcdate           iInvoiceDateFrom,
domain  tcdate           iInvoiceDateTo,
domain  cisli.ipro       iInvoicePrintOutput,
domain  cisli.psco       iPrintingSequence,
domain  tcyesno          iPrintInEuro,
domain  tcyesno          iPrintOriginalInvoiceCreditNote,
domain  tcyesno          iPrintCanceledInvoice,
domain  tcyesno          iPrintInvoiceDeliveryMethod,
domain  tcyesno          iPrintInvoicesToOneSpooler,
domain  cisli.lang       iPrintInvoiceLanguageOption,
domain  cisli.xml.lang   iPrintXMLLanguageOption,
domain  cisli.devc       iInvoicePrintDevice,
domain  cisli.devc       iExceptionPrintDevice,
domain  tcmcs.s250m      iReasonForReprint mb,
ref     domain  tcmcs.long       oNumberOfInvoicesPrinted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to reprint the invoice for the given
invoice number or range of invoice for the given Invoice-To
Business Partner and Invoice date range.
To reprint the invoice, either the Invoice Number in combination
with Invoice-to Business Partner is given as an input or only
the Invoice Number is given or only Invoice-to Business Partner
is given as an input.
In case where 'iInvoiceTransactionType' is empty but
Invoice-to Business Partner is entered then the
'iInvoiceDateFrom' becomes a mandatory input.
If 'iInvoiceDateTo' is not passed then the current date is
taken.
Pre:    Not applicable
Post:   Not applicable
Input:  iSalesInvoiceCompany    - Sales Invoice Company
(This is a Mandatory field)
iTypeOfInvoice          - Type of Invoice
(This is a Mandatory field)
Possible values : Standard      tcsli.tinv.standard
: Pro Forma     tcsli.tinv.pro.forma
: Customs       tcsli.tinv.customs
: Consignment   tcsli.tinv.consignment
iFinancialCompany       - Financial Company
iInvoiceTransactionType - Invoice Transaction Type
iInvoiceDocumentNumber  - Invoice Document Number
iInvoiceToBusinessPartner
- Invoice-to Business Partner
iInvoiceDateFrom        - Invoice Date From
iInvoiceDateTo          - Invoice Date To
(If Invoice Date to is not given then
Current date will be taken)
iInvoicePrintOutput     - Invoice Print Output
Possible Values :
: Printed Document
: Printed Document and XML Document
: XML Document
: Not Applicable
iPrintingSequence       - Printing Sequence of the Invoices
iPrintInEuro            - Print in Euro
(Amounts in EMU currencies are printed
in euros.
This input is only applicable when the
currency system for the given Sales
Invoice company is other than
'Standard')
iPrintOriginalInvoiceCreditNote
- Print the linked Original Invoice for
the given Credit note invoice
iPrintCanceledInvoice   - Print Canceled Invoice
iPrintInvoiceDeliveryMethod
- Print Invoices sorted by invoice
delivery method
iPrintInvoicesToOneSpooler
- Print invoice in one single file
iPrintInvoiceLanguageOption
- Print Invoice in below languages
(This is a Mandatory field)
Possible Values : Own Tax Country Language
: Business Partner Tax Country Language
: Both
iPrintXMLLanguageOption - Print XML  Invoice Language options
(This is a Mandatory field)
Possible Values : User Language
: Printed Invoice Language
: Own Tax Country Language
: Business Partner Tax Country Language
iInvoicePrintDevice     - Print Device for the Invoice report
iExceptionPrintDevice   - Print Device for the Exception report
iReasonForReprint       - Reason for Reprint
Output: oNumberOfInvoicesPrinted- Number of Invoices printed
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information
Return: 0/DALHOOKERROR
```
