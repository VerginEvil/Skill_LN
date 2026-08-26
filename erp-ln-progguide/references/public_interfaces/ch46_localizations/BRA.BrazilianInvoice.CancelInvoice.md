# BRA.BrazilianInvoice.CancelInvoice

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for BRA.BrazilianInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1904-1905

```baan
DLL:   btextsliapi
This function is available from     2026.04 (KB3665487  ).
Syntax: long BRA.BrazilianInvoice.CancelInvoice(
domain  btncmp           iSalesInvoiceCompany,
domain  btorno           iFiscalReference,
ref     domain  btmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the cancelation of a Brazilian invoice.
During this process, the transaction handling is being done in
this function. Retry point, commit transaction and abort
transaction will be handled in this function.
Pre:    No open database transaction.
Post:   n.a.
Input:  iSalesInvoiceCompany                  - Company of the Sales Invoice.
This is a mandatory field.
iFiscalReference                              - Fiscal reference of the invoice which
will be canceled. This is a mandatory
field.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```
