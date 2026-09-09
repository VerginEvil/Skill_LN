# GeneralLedger.CheckDocumentIsBalanced

> Chapter: Chapter 40 Public Interfaces for General Ledger
>
> Group: Public Interfaces for GeneralLedger
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1831-1831

```baan
DLL:   tfextgldapi
This function is available from 2023.05 (KB2285516).
Syntax: long GeneralLedger.CheckDocumentIsBalanced(
domain  tcncmp           iFinancialCompany,
domain  tfgld.ttyp       iTransactionType,
domain  tfgld.docn       iDocument,
ref             boolean          oDocumentIsBalanced,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function checks if the given input document is balanced.
Pre:    NA
Post:   NA
Input:  iFinancialCompany       - Financial Company - mandatory
iTransactionType        - Transaction Type  - mandatory
iDocument               - Document
Output: oDocumentIsBalanced     - Document is balanced indicator
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
