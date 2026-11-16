# Invoice.StartMultiMain

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1614-1615

```baan
DLL:   ciextsliapi
This function is available from 2020.07 (KB2124250).
Syntax: long Invoice.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcncmp           iFinancialCompany,
domain  tctran           iTransactionType,
domain  tcgld.docn       iInvoiceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts session 'Invoice'(cisli3605m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"" (Session has no start filter)
iSessionIndex
iSessionIndex is not used (yet) because session has
only 1 index
iQueryExtend
Optional
A specific query to be used when zooming to this session.
Primary Key Fields:
iFinancialCompany
iTransactionType
iInvoiceNumber
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
