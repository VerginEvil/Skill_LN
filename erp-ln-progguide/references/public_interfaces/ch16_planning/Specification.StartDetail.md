# Specification.StartDetail

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for Specification
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 599-599

```baan
DLL:   cpextrrpapi
This function is available from 2026.01 (KB3606127).
Syntax: long Specification.StartDetail(
long             iStartMode,
domain  tcguid           iSpecificationID,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Specification
(cprrp0101s000).
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session. Mandatory.
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS
Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dialog.
iSpecificationID        Specification Identifier. Specification
must be part of the Specification(cprrp001)
Output: oExceptionMessage       The last message, if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started successfully.
<> 0                    Otherwise.
```
