# AlternativeItem.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for AlternativeItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 231-232

```baan
DLL:   tcextibdapi
This function is available from 2024.07 (KB2303602).
Syntax: long AlternativeItem.StartDetail(
long             iStartMode,
domain  tcitem           iItem,
domain  tcitem           iAlternativeItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Alternative Items (tcibd0505m000) in detail mode.
This function can only be used when the sites concept is NOT
active.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iItem
Mandatory
iAlternativeItem
Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
