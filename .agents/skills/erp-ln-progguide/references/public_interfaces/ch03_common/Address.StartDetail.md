# Address.StartDetail

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Address
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 89-89

```baan
DLL:   tcextcomapi
This function is available from 2024.08 (KB3502076).
Syntax: long Address.StartDetail(
long             iStartMode,
domain  tccom.cadr       iAddress,
boolean          iReadOnly,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Addresses (tccom4130s000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iAddress: Mandatory
iReadOnly:
Optional: Session is started in readonly-mode when
iReadOnly is True
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
