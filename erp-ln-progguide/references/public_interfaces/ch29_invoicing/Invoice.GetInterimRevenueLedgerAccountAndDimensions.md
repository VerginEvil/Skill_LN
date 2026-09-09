# Invoice.GetInterimRevenueLedgerAccountAndDimensions

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1608-1609

```baan
DLL:   ciextsliapi
This function is available from 2024.07 (KB2331941).
Syntax: long Invoice.GetInterimRevenueLedgerAccountAndDimensions(
domain  tcncmp           iFinancialCompany,
domain  tctran           iTransactionType,
domain  tcgld.docn       iInvoiceNumber,
domain  tciseq           iInvoiceLine,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tccom.cadr       iInvoiceToAddress,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.cadr       iSoldToAddress,
domain  tcccty           iTaxCountry,
domain  tccvat           iTaxCode,
domain  tcccty           iBpTaxCountry,
domain  tcyesno          iAssetDisposal,
ref     domain  tfgld.leac       oLedgerAccount,
ref     domain  tfgld.dimx       oDimensions() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves ledger account and dimensions from the
mapping scheme for a manual sales invoice with a fixed asset.
Pre:    Not applicable
Post:   Not applicable
Input:  iFinancialCompany       - Financial Company: Mandatory
iTransactionType        - Invoice Transaction Type: Optional
iInvoiceNumber          - Invoice Number: Optional
iInvoiceLine            - Invoice Line: Optional
iInvoiceToBusinessPartner
- Invoice-to Business Partner: Optional
iInvoiceToAddress       - Address Invoice-to Business Partner:
Optional
iSoldToBusinessPartner  - Sold-to Business Partner: Optional
iSoldToAddress          - Address Sold-to Business Partner:
Optional
iTaxCountry             - Tax Country: Optional
iTaxCode                - Tax Code: Optional
iBpTaxCountry           - Business Partner Tax Country: Optional
iAssetDisposal          - Asset Disposal: Mandatory
Output: oLedgerAccount          - Ledger Account
oDimensions             - Array with Dimensions
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
