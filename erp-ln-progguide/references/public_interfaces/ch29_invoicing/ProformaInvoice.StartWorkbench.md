# ProformaInvoice.StartWorkbench

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for ProformaInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1597-1599

```baan
DLL:   ciextsliapi
This function is available from     2022.10 (KB2262990  ).
Syntax: long ProformaInvoice.StartWorkbench(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tcncmp           iSourceCompany,
domain  tcsli.srtp       iSourceType,
domain  tcorno           iOrder,
domain  tcsli.oref       iSourceDocumentLine,
domain  tcinvt           iInvoiceLineType,
domain  tcsli.tinv       iTypeOfInvoice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts session 'Proforma Invoicing Workbench'
(cisli3640m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
iStartFilter is not used (yet)
iSessionIndex
iSessionIndex is not used (yet) because session has
only 1 index
iQueryExtend
iQueryExtend is not used (yet)
iInvoiceToBusinessPartner
In the satellites the data for this Invoice to Business
Partner will be shown.
iSourceCompany
In the satellites the data for this Source Company
will be shown.
iSourceType
In the satellites the data for this Source Type
will be shown.
iOrder
In the satellites the data for this Ordernumber will be
shown.
iSourceDocumentLine
In the satellites the data for this Source Document Line
will be shown.
iInvoiceLineType
In the satellites the data for this Invoice Line Type
will be shown.
The value of the 'source type' determines which Invoice
Line types are possible.
iTypeOfInvoice
In the satellites the data for this Invoice Type
will be shown.
Possible values : Pro Forma     tcsli.tinv.pro.forma
: Customs       tcsli.tinv.customs
: Consignment   tcsli.tinv.consignment
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for Installment

The following functions are available: Installment.ApproveCorrections Installment.Close Installment.CreateCorrections Installment.StartMultiMain Installment.Transfer Installment.TransferCorrections
