# ItemPurchase.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPurchase
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 199-200

```baan
DLL:   tdextipuapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long ItemPurchase.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tcseak           iSearchKey mb,
domain  tcemno           iBuyer,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Items - Purchase
in overview mode (tdipu0101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The index that will be used.
Supported values:
1: sort by Item
2: sort by Search Key/Item
3: sort by Buyer/Item
iQueryExtend            A specific query to be used when zooming
to this session.
iItem                   Item
iSearchKey              Search Key
iBuyer                  Buyer
Output: for iStartMode MODAL:
oItem           Selected Item
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

## Public Interfaces for ItemPurchaseBySite

The following functions are available: ItemPurchaseBySite.StartDetail
