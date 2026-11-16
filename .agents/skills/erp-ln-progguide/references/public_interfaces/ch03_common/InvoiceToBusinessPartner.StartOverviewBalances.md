# InvoiceToBusinessPartner.StartOverviewBalances

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for InvoiceToBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 138-138

```baan
DLL:   tcextcomapi
This function is available from 2026.06 (KB3673849).
Syntax: long InvoiceToBusinessPartner.StartOverviewBalances(
long             iStartMode,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tcncmp           iCompany,
domain  tccwoc           iDepartment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Overview session
Invoice-to Business Partner Balances tccom4513m000 (Overview).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL   -       The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS-       Parent and child are parallel sessions
that can be manipulated simultaneously.
iSessionIndex           - The index that will be used.
Supported value:
1: sort by BP, Company, Department.
iQueryExtend            - A specific query to be used when
zooming to this session.
iInvoiceToBusinessPartner       - Invoice-to Business Partner (Mandatory)
iCompany                        - Company
iDepartment                     - Department
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
<> 0                    - Otherwise.
```
