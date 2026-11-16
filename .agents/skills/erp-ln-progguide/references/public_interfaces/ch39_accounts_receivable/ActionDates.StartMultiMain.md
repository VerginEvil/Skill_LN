# ActionDates.StartMultiMain

> Chapter: Chapter 39 Public Interfaces for Accounts Receivable
>
> Group: Public Interfaces for ActionDates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1823-1824

```baan
DLL:   tfextacrapi
This function is available from 2023.12 (KB2301434).
Syntax: long ActionDates.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tfgld.ttyp       iTransactionType,
domain  tfgld.docn       iDocument,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts MMT session Action Dates by Invoice
(tfacr5600m100).
Pre:    na
Post:   na
Input:  iStartMode              - Start Mode
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
Possible values are:""
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
No Session Index available for tfacr5600m100.
iQueryExtend
A specific query to be used when zooming to this session.
iInvoiceToBusinessPartner
- Invoice To Business Partner
iTransactionType        - Transaction Type
iDocument               - Invoice number
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - succes
<> 0                      otherwise
```
