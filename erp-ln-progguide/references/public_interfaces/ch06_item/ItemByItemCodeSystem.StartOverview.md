# ItemByItemCodeSystem.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemByItemCodeSystem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 196-197

```baan
DLL:   tcextibdapi
This function is available from     2025.08 (KB3611238  ).
Syntax: long ItemByItemCodeSystem.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccitt           iItemCodeSystem,
domain  tccom.bpid       iBusinessPartner,
domain  tcitem           iItem,
domain  tcaitm           iBusinessPartnerItem mb,
ref     domain  tccitt           oItemCodeSystem,
ref     domain  tccom.bpid       oBusinessPartner,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Item Code System - Items (tcibd0104m000) in
overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used.
iSessionIndex
Value:  1:  Code System, Business Partner, Item
2:  Code System, Business Partner,
Business Partner Item
Determines the sort order in the session.
E.g. if iSessionIndex = 1, then Items are sorted by
Item Code System, Business Partner and Item Code.
iQueryExtend
A specific query to be used when zooming to the session.
Using the query extend may lead to a "data not found,
session not started" situation. (Optional)
iItemCodeSystem
Optional
iBusinessPartner
Optional
iItem
Optional
iBusinessPartnerItem
Optional
Output: When Start Mode is MODAL, and one row is selected on exit:
oItemCodeSystem                               - Item code system of the selected row
oBusinessPartner                              - Business partner of the selected row
oItem                                         - Item of the selected row
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

## Public Interfaces for ItemPurchase

The following functions are available: ItemPurchase.StartDetail ItemPurchase.StartMultiMain ItemPurchase.StartOverview
