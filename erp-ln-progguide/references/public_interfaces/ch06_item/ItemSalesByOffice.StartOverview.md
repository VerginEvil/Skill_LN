# ItemSalesByOffice.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemSalesByOffice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 209-211

```baan
DLL:   tdextisaapi
This function is available from     2024.12 (KB3538855  ).
Syntax: long ItemSalesByOffice.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tccwoc           iSalesOffice,
ref     domain  tcitem           oItem,
ref     domain  tccwoc           oSalesOffice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Items - Sales by Office
(tdisa0181m000) in Overview mode.
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
1: sort by Item, Sales Office
2: sort by Sales Office, Item
iQueryExtend            A specific query to be used when zooming
to this session (Optional).
iItem                   Item (Mandatory if iSessionIndex equals 1
and iStartMode equals MODELESS).
iSalesOffice            Sales Office (Optional)
Output:
Variables below contain the values of the selected record,
they are only filled if iStartMode is MODAL and 1 record has
been selected:
oItem                   Item
oSalesOffice            Sales Office
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

## Public Interfaces for ItemPlanning

The following functions are available: ItemPlanning.StartDetail ItemPlanning.StartOverview
