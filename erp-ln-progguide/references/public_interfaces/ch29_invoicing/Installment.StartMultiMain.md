# Installment.StartMultiMain

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for Installment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1601-1603

```baan
DLL:   ciextsliapi
This function is available from     2026.06 (KB3674854  ).
Syntax: long Installment.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcncmp           iSourceCompany,
domain  tcsli.srtp       iSourceType,
domain  tcorno           iOrderNumber,
domain  tcsli.oref       iOrderReference,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl: This function starts session Installments (cisli8620m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"" (Session has no start filter)
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
Primary Key Fields:
iSourceCompany                                - Source Company
iSourceType                                   - Source Type
iOrderNumber                                  - Order Number
iOrderReference                               - Order Reference
Output:
oExceptionMessage                             - The last message if the return
value is not equal to 0.
If more than one  message is
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to all error
information. Use the functions in
Exception to get all relevant
information.
Return  0                                     - Session started
DALHOOKERROR                                  - Otherwise.
```
