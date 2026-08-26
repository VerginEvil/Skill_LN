# AsBuilt.StartOverview

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for AsBuilt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 632-634

```baan
DLL:   tiextmfcapi
This function is available from     2024.01 (KB2304915  ).
Syntax: long AsBuilt.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  timfc.ord        iOrderType,
domain  tcpdno           iOrderNumber,
domain  tcponl           iSchedulePosition,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref     domain  timfc.ord        oOrderType,
ref     domain  tcpdno           oOrderNumber,
ref     domain  tcponl           oSchedulePosition,
ref     domain  tcitem           oItem,
ref     domain  tcibd.sern       oSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Serial End Item - As-Built
Headers (timfc0110m000) in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used.
iSessionIndex           Optional. The index that will be used.
Supported values:
1: sort by Order Type, Order, Schedule
Line, End Item, Serial Number.
2: sort by Order Type, Order, Schedule
Line, Eff Unit, Status, Serial, End
Item.
3: sort by End Item, Serial, Order
Type, Order, Schedule Line.
iQueryExtend            A specific query to be used when zooming
to this session. Optional.
iOrderType              Order Type                       - Optional
iOrderNumber            Order Number can be either Production
Order or Assembly Order                                               - Optional
iSchedulePosition       Schedule Position                       - Optional
iItem                   Item                       - Optional
iSerialNumber           Serial Number                       - Optional
Output: Variables below contain the values of the selected record.
They are only filled if i.start.mode is MODAL and 1 record has
been selected.
oOrderType             Order Type
oOrderNumber           Order Number can be either Production
Order or Assembly Order
oSchedulePosition      Schedule Position
oItem                  Item
oSerialNumber          Serial Number
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```

## Chapter 19 Public Interfaces for Job Shop

## Public Interfaces for BillOfMaterialLines

The following functions are available: BillOfMaterialLines.StartOverview
