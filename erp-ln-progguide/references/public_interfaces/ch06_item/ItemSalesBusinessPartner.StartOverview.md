# ItemSalesBusinessPartner.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemSalesBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 208-209

```baan
DLL:   tdextisaapi
This function is available from     2023.08 (KB2300144  ).
Syntax: long ItemSalesBusinessPartner.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tcefex.date      iEffectiveDate,
ref     domain  tccitg           oItemGroup,
ref     domain  tcitem           oItem,
ref     domain  tccom.bpid       oSoldToBusinessPartner,
ref     domain  tccom.bpid       oShipToBusinessPartner,
ref     domain  tcefex.date      oEffectiveDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Items - Sales Business Partner
Overview (tdisa0510m000).
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS        Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Start Filter, not used.
iSessionIndex           The table index that will be used
(Optional).
Supported values:
1: sort by Item Group, Item
2: sort by Sold                                              -to Business Partner,
Ship                                                 -to Business Partner
3: sort by Item, Item Group
iQueryExtend            A specific query to be used when zooming
to this session (Optional).
iItemGroup              Item Group (Optional).
iItem                   Item (Optional).
iSoldToBusinessPartner  Sold                      -to Business Partner (Optional)
iShipToBusinessPartner  Ship                      -to Business Partner (Optional).
iEffectiveDate          Effective date (Optional).
Output:
Variables below contain the values of the selected record,
they are only filled if iStartMode is MODAL and 1 record has
been selected:
oItemGroup              Item Group
oItem                   Item
oSoldToBusinessPartner  Sold                      -to Business Partner
oShipToBusinessPartner  Ship                      -to Business Partner
oEffectiveDate          Effective Date
Variables for API error handling:
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

## Public Interfaces for ItemSalesByOffice

The following functions are available: ItemSalesByOffice.StartOverview
