# ItemBySite.StartCreate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemBySite
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 190-191

```baan
DLL:   tcextibdapi
This function is available from     2026.08 (KB3685058  ).
Syntax: long ItemBySite.StartCreate(
long             iStartMode,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Create Item by Sites
(tcibd1552m100).
The session creates Item by Site records (tcibd152) for the
given Item. The Item Type and Item Group are derived from the
given Item internally by the session.
Input:
iStartMode
Specifies the start mode for the session (Mandatory).
Possible values are:
MODAL                                         - The parent session is blocked until the
child session exits.
MODELESS                                      - Parent and child are parallel
sessions that can be manipulated
simultaneously.
iItem                                         - Item (Mandatory).
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started.
<> 0                                          - Otherwise.
```
