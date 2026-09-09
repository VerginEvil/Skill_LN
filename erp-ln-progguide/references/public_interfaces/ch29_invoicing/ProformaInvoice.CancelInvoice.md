# ProformaInvoice.CancelInvoice

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for ProformaInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1615-1615

```baan
DLL:   ciextsliapi
This function is available from 2024.11 (KB3533175).
Syntax: long ProformaInvoice.CancelInvoice(
domain  tcncmp           iFinancialCompany,
domain  tctran           iTransactionType,
domain  tcgld.docn       iInvoiceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to cancel a printed Proforma
Invoice.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iFinancialCompany       - Financial Company of the Invoice.
(This is a Mandatory field)
iTransactionType        - Transaction Type of the Invoice.
(This is a Mandatory field)
iInvoiceNumber          - Invoice Number.
(This is a Mandatory field)
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Printed Pro Forma Invoice is Canceled
successfully.
<> 0                    - Error
```
