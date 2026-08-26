# Installment.Transfer

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Installment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1603-1604

```baan
DLL:   ciextsliapi
This function is available from     2022.12 (KB2269017  ).
Syntax: long Installment.Transfer(
domain  tcncmp           iSourceCompany,
domain  tcsli.srtp       iSourceType,
domain  tcorno           iOrderNumber,
domain  tcsli.oref       iOrderReference,
domain  tcnins           iInstallmentLine,
domain  tcsli.tinv       iTypeOfInvoice,
domain  tcpitp           iProFormaInvoicingType,
domain  tcguid           iDraftGuid,
domain  tcmcs.str14      iPrintDevice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to Transfer Approved Installment
Line to Invoicing.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  i.calling.api
Input:  iSourceCompany
Source Company of the Installment Line.
This is a Mandatory field.
iSourceType
Source Type of the Installment Line.
This is a Mandatory field.
iOrderNumber
Order Number of the Installment Line.
This is a Mandatory field.
iOrderReference
Order Reference of the Installment Line.
iInstallmentLine
The Installment Line number.
This is a Mandatory field.
iTypeOfInvoice
The Type of Invoice.
This is a Mandatory field.
Possible values : Standard      tcsli.tinv.standard
: Pro Forma     tcsli.tinv.pro.forma
: Customs       tcsli.tinv.customs
: Consignment   tcsli.tinv.consignment
iProFormaInvoicingType
The Pro Forma Invoicing Type specified in the
Pro Forma Invoicing Types (tcmcs0167m000) session.
This field is Mandatory only when Type of Invoice is
other than Standard.
iDraftGuid
Draft Guid if filled will be passed to the created
Billable line.
iPrintDevice
Print Device to print the Pro forma invoice
This field is only relevant when Type of Invoice is
other than Standard.
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
