# HandlingUnit.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1054-1054

```baan
DLL:   whextwmdapi
This function is available from     2025.07 (KB3572724  ).
Syntax: long HandlingUnit.StartDetail(
long             iStartMode,
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Handling Units in Detail mode
(whwmd5130m000).
Pre:    oHandlingUnitArray must be declared as based array.
Post:   NA
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iHandlingUnit                         - Mandatory
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0     Session started
<> 0: Error
```
