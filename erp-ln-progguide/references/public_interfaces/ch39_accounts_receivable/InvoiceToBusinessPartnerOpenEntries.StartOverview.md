# InvoiceToBusinessPartnerOpenEntries.StartOverview

> Chapter: Chapter 39 Public Interfaces for Accounts Receivable
>
> Group: Public Interfaces for InvoiceToBusinessPartnerOpenEntries
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1804-1806

```baan
DLL:   tfextacrapi
This function is available from     2024.10 (KB3532922  ).
Syntax: long InvoiceToBusinessPartnerOpenEntries.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcncmp           iFinancialCompany,
domain  tfgld.ttyp       iTransactionType,
domain  tfgld.docn       iDocument,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tfgld.date       iDocumentDate,
domain  tccom.bpid       iPayByBusinessPartner,
ref     domain  tcncmp           oFinancialCompany,
ref     domain  tfgld.ttyp       oTransactionType,
ref     domain  tfgld.docn       oDocument,
ref     domain  tfgld.lino       oLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Invoice To BP Open Entries
(tfacr2520m000).
Pre:    na
Post:   na
Input:  iStartMode                            - Start Mode (mandatory)
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
Possible values are: ""
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
Possible values are 1,2,3 or 4
iQueryExtend
A specific query to be used when zooming to this session.
iFinancialCompany
Financial company
iTransactionType
Transaction type
iDocument
Document
iInvoiceToBusinessPartner
Invoice to Business Partner  fill when session.index=2
iDocumentDate
Document Date                fill when session.index=3
iPayByBusinessPartner
Pay By Business Partner      fill when session.index=4
Output:
oFinancialCompany                             - selected Financial Company
oTransactionType                              - selected Transaction Type
oDocument                                     - selected Document
oLine                                         - selected Line
The 4 output variables mentioned above are only filled when
iStartMode = MODAL and 1 record is selected.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - succes
<> 0                      otherwise
```

## Public Interfaces for OpenEntry

The following functions are available: OpenEntry.StartMultiMain
