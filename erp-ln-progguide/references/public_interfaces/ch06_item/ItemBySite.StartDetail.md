# ItemBySite.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemBySite
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 191-192

```baan
DLL:   tcextibdapi
This function is available from     2020.06 (KB2127551  ).
Syntax: long ItemBySite.StartDetail(
long             iStartMode,
domain  tcsite           iSite,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Items by Site  General (tcibd1550m000)
in detail mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSite   Mandatory
iItem   Mandatory
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```
