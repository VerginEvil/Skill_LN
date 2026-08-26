# InboundAdvice.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1073-1073

```baan
DLL:   whextinhapi
This function is available from     2025.04 (KB3566675  ).
Syntax: long InboundAdvice.StartDetail(
long             iStartMode,
domain  tcorno           iAdvice,
domain  tcpono           iAdviceLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Inbound Advice
(whinh3125s000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, in case of a
multi                                              -occurrence the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Following input variable form the primary key, these fields
are mandatory, if the primary key cannot be found an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iAdvice
iAdviceLine                                   - The primary key fields must refer to
an existing Inbound Advice
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```
