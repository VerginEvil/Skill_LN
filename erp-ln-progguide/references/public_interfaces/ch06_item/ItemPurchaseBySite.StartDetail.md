# ItemPurchaseBySite.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPurchaseBySite
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 200-201

```baan
DLL:   tdextipuapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long ItemPurchaseBySite.StartDetail(
long             iStartMode,
domain  tcitem           iItem,
domain  tcitem           iSite,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Items - Purchase
(tdipu0101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Following input variables form the primary key, these fields
are mandatory. If the primary key cannot be found an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iItem           Item
iSite           Site
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

## Public Interfaces for ItemPurchaseBusinessPartner

The following functions are available: ItemPurchaseBusinessPartner.CalculateLeadTimes ItemPurchaseBusinessPartner.GetSafetyTime ItemPurchaseBusinessPartner.StartDetail ItemPurchaseBusinessPartner.StartOverview
