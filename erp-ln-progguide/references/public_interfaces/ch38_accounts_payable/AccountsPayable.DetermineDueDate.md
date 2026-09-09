# AccountsPayable.DetermineDueDate

> Chapter: Chapter 38 Public Interfaces for Accounts Payable
>
> Group: Public Interfaces for AccountsPayable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1817-1818

```baan
DLL:   tfextacpapi
This function is available from 2023.04 (KB2286742).
Syntax: long AccountsPayable.DetermineDueDate(
domain  tcncmp           iFinancialCompany,
const   domain  tccom.bpid       iPayToBusinessPartner,
const   domain  tccpay           iPaymentTerms,
domain  tfgld.date       iDocumentDate,
ref     domain  tfgld.date       oDueDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines a due date based on the given input
parameters.
Pre:    NA
Post:   NA
Input:  iFinancialCompany       - Financial Company       - mandatory
iPayToBusinessPartner   - Pay-to Business Partner
iPaymentTerms           - Payment Terms
iDocumentDate           - Document Date
eg. Invoice date or
Invoice Receipt date
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
