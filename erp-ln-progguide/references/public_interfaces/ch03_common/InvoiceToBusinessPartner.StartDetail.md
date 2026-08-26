# InvoiceToBusinessPartner.StartDetail

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for InvoiceToBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 136-137

```baan
DLL:   tcextcomapi
This function is available from     2024.11 (KB3524683  ).
Syntax: long InvoiceToBusinessPartner.StartDetail(
long             iStartMode,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tccwoc           iDepartment,
boolean          iReadOnly,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Detail session Invoice-to Business Partner-
(tccom4112s000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                                 -       The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                              -       Parent and child are parallel
sessions that can be manipulated
simultaneously.
iInvoiceToBusinessPartner
-                                             Invoice-to Business Partner (Mandatory)
iDepartment                           -       Department              (Not Mandatory)
iReadOnly                             -       Session is started in readonly-mode when
iReadOnly is True       (Optional)
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
<> 0                                          - Otherwise.
```
