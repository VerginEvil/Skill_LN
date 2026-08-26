# ReceiptDetails.StartOverview

> Chapter: Chapter 39 Public Interfaces for Accounts Receivable
>
> Group: Public Interfaces for ReceiptDetails
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1807-1810

```baan
DLL:   tfextacrapi
This function is available from     2026.04 (KB3665487  ).
Syntax: long ReceiptDetails.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tfcmg.cheq       iBusinessPartnerPaymentNumber,
domain  tfgld.ttyp       iReceiptTransactionType,
domain  tfgld.docn       iReceiptDocument,
domain  tfgld.lino       iReceiptLine,
domain  tfgld.ttyp       iInvoiceTransactionType,
domain  tfgld.docn       iInvoiceDocument,
domain  tfgld.lino       iInvoiceLine,
ref     domain  tfgld.ttyp       oReceiptTransactionType,
ref     domain  tfgld.docn       oReceiptDocument,
ref     domain  tfgld.lino       oReceiptLine,
ref     domain  tfgld.ttyp       oInvoiceTransactionType,
ref     domain  tfgld.docn       oInvoiceDocument,
ref     domain  tfgld.lino       oInvoiceLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Overview session Receipt Details -
(tfacr2538m000).
Pre:    Not Applicable
Post:   Not Applicable
Input:  iStartMode                            - Start Mode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:""
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
No Session Index available for tfacr2538m000
iQueryExtend
A specific query to be used when zooming to this session.
iInvoiceToBusinessPartner
-                                               Invoice To Business Partner
iBusinessPartnerPaymentNumber
-                                               Business Partner Payment Number
iReceiptTransactionType                       - Receipt Transaction Type
iReceiptDocument                              - Receipt Document
iReceiptLine                                  - Receipt Line
iInvoiceTransactionType                       - Invoice Transaction Type
iInvoiceDocument                              - Invoice Document Number
iInvoiceLine                                  - Invoice Line Number
Output: oReceiptTransactionType               - Selected Receipt Transaction Type
oReceiptDocument                              - Selected Receipt Document
oReceiptLine                                  - Selected Receipt Line
oInvoiceTransactionType                       - Selected Invoice Transaction Type
oInvoiceDocument                              - Selected Invoice Document
oInvoiceLine                                  - Selected Invoice Line
The 6 output variables mentioned above are only filled when
iStartMode = MODAL and 1 record is selected.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```

## Chapter 40 Public Interfaces for General Ledger

## Public Interfaces for GeneralLedger

The following functions are available: GeneralLedger.CheckBatchLineIsBalanced GeneralLedger.CheckDocumentIsBalanced
