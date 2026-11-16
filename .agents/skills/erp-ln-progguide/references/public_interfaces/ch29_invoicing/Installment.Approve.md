# Installment.Approve

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Installment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1617-1618

```baan
DLL:   ciextsliapi
This function is available from 2026.10 (KB3696744).
Syntax: long Installment.Approve(
domain  tcncmp           iSourceCompany,
domain  tcsli.srtp       iSourceType,
domain  tcorno           iOrderNumber,
domain  tcsli.oref       iOrderReference,
domain  tcnins           iInstallmentLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to Approve an Installment Line.
Pre:    Caller must set retry-point.
Post:   Caller must commit/abort transaction.
Input:  iSourceCompany
Source Company of the Installment Line.
This is a Mandatory field.
iSourceType
Source Type of the Installment Line.
This is a Mandatory field.
iOrderNumber
Order Number of the Installment Line.
This is a Mandatory field.
iOrderReference
Order Reference of the Installment Line.
iInstallmentLine
The Installment Line number.
This is a Mandatory field.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Installment Approved.
<> 0                    - Error
```
