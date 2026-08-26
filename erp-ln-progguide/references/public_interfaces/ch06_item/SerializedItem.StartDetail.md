# SerializedItem.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 244-244

```baan
DLL:   tcextibdapi
This function is available from     2026.04 (KB3617513  ).
Syntax: long SerializedItem.StartDetail(
long             iStartMode,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Serialized Items
(tcibd4101s000) in detail mode. This section displays the
serialized item that are tracked within the system. Using
Serialized Item can create new serials.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iItem                   Item
iSerialNumber           Serial Number
Output: oExceptionMessage       The last message, if any message is
found. If more than one message is
given these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
