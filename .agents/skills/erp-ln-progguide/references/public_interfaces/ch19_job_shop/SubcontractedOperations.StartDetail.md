# SubcontractedOperations.StartDetail

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for SubcontractedOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 813-814

```baan
DLL:   tiextsfcapi
This function is available from 2024.04 (KB2323105).
Syntax: long SubcontractedOperations.StartDetail(
long             iStartMode,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Subcontracted Operations
(tisfc2110m000) in detail mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Primary Key Fields:
iProductionOrder        Production Order - Mandatory.
iOperation              Operation - Mandatory.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
