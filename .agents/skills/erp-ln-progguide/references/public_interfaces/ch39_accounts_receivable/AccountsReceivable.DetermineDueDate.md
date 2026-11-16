# AccountsReceivable.DetermineDueDate

> Chapter: Chapter 39 Public Interfaces for Accounts Receivable
>
> Group: Public Interfaces for AccountsReceivable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1821-1822

```baan
DLL:   tfextacrapi
This function is available from 2023.10 (KB2308375).
Syntax: long AccountsReceivable.DetermineDueDate(
domain  tcncmp           iFinancialCompany,
const   domain  tccom.bpid       iPayByBusinessPartner,
const   domain  tccpay           iPaymentTerms,
domain  tfgld.amnt       iInvoiceAmount,
domain  tfgld.date       iDocumentDate,
ref     domain  tfgld.date       oDueDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines a due date based on the given input
parameters. Here the document date and due date are non-UTC
dates.
Pre:    NA
Post:   NA
Input:  iFinancialCompany       - Financial Company       - mandatory
iPayByBusinessPartner   - Pay-by Business Partner
iPaymentTerms           - Payment Terms
iInvoiceAmount          - Invoice Amount - (Not used yet)
iDocumentDate           - Document Date
eg. Invoice date
Output: oDueDate                - Determined Due Date
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK
<> 0                    - on errors
```
