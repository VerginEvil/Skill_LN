# Installment.ApproveCorrections

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Installment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1618-1619

```baan
DLL:   ciextsliapi
This function is available from 2024.07 (KB3507558).
Syntax: long Installment.ApproveCorrections(
domain  tcncmp           iSourceCompany,
domain  tcsli.srtp       iSourceType,
domain  tcorno           iOrderNumber,
domain  tcsli.oref       iOrderReference,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to approve the corrections in
billable installment lines for the given order.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSourceCompany          - Source Company of the Order.
(This is a Mandatory field)
iSourceType             - Source Type of the Order.
(This is a Mandatory field)
Possible values :
Sales Order     - tcsli.srtp.sales.order
Service Order   - tcsli.srtp.service.order
Maintenance Sales Order
- tcsli.srtp.maint.sales.ord
iOrderNumber            - Order Number.
(This is a Mandatory field)
iOrderReference         - Order Reference of the Order.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Corrections approved.
<> 0                    - Error
```
