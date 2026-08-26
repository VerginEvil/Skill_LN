# Invoice.CreditInvoiceLine

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1591-1592

```baan
DLL:   ciextsliapi
This function is available from     2024.09 (KB3513949  ).
Syntax: long Invoice.CreditInvoiceLine(
domain  tcncmp           iFinancialCompany,
domain  tctran           iTransactionType,
domain  tcgld.docn       iInvoiceNumber,
domain  tciseq           iInvoiceLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to create Credit Note for the
given Invoice Line.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iFinancialCompany                     - Financial Company of the Invoice.
(This is a Mandatory field)
iTransactionType                              - Transaction Type of the Invoice.
(This is a Mandatory field)
iInvoiceNumber                                - Invoice Number.
(This is a Mandatory field)
iInvoiceLine                                  - Invoice Line.
(This is a Mandatory field)
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Credit Note created successfully.
<> 0                                          - Error
```
