# ItemPurchase.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPurchase
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 198-199

```baan
DLL:   tdextipuapi
This function is available from 2020.03 (KB2111387).
Syntax: long ItemPurchase.StartDetail(
long             iStartMode,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Items - Purchase
(tdipu0101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iItem                   Item (Mandatory; given item must exist)
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
