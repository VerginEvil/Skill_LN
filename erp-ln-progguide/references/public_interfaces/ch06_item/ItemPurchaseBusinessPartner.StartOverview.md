# ItemPurchaseBusinessPartner.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPurchaseBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 204-206

```baan
DLL:   tdextipuapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long ItemPurchaseBusinessPartner.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcefex.date      iEffectiveDate,
ref     domain  tccitg           oItemGroup,
ref     domain  tcitem           oItem,
ref     domain  tccom.bpid       oBuyFromBusinessPartner,
ref     domain  tccom.bpid       oShipFromBusinessPartner,
ref     domain  tcefex.date      oEffectiveDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Items - Purchase Business Partner
in overview mode (tdipu0110m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used
iSessionIndex           The index that will be used.
Supported values:
1: sort by Item Group/Item
2: sort by Buy                                                -from Business Partner/
Ship                                                           -from Business Partner
3: sort by Approved Supplier List
iQueryExtend            A specific query to be used when zooming
to this session.
iItemGroup              Item Group
iItem                   Item
iBuyFromBusinessPartner
Buy                                              -from Business Partner (Mandatory if
iStartMode = MODELESS and iSessionIndex = 2)
iShipFromBusinessPartner
Ship                                              -from Business Partner
iEffectiveDate          Effective Date
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oItemGroup      Item Group
oItem           Item
oBuyFromBusinessPartner
Buy                                              -from Business Partner
oShipFromBusinessPartner
Ship                                              -from Business Partner
oEffectiveDate  Effective Date
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

## Public Interfaces for

## ItemsByManufacturerPartNumber

The following functions are available: ItemsByManufacturerPartNumber.StartOverview
