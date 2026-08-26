# SerializedItem.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 244-246

```baan
DLL:   tcextibdapi
This function is available from     2026.04 (KB3617513  ).
Syntax: long SerializedItem.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcclot           iLotCode,
ref     domain  tcitem           oItem,
ref     domain  tcibd.sern       oSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Serialized Items
(tcibd4501m000) in overview mode. This session displays the
serialized items that are tracked within the system. These are
items for which serial numbers have been assigned either
automatically or manually.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used
iSessionIndex           Specifies the table                      -index that is to be
used. Default index is 1.
Standard supported values:
1: Sort by Item, Serial Number
2: Sort by Serial Number, Item
3: Sort by Item, Lot, Serial Number
iQueryExtend            A specific query to be used when zooming
to this session.
iItem                   Item
iSerialNumber           Serial Number
iLotCode                Lot Code
Output: for iStartMode MODAL:
oItem                   Item of the selected row
oSerialNumber           Serial Number of the selected row
oExceptionMessage       The last message, if any message is
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

## Public Interfaces for

## ReceivedProductionBillOfMaterial

The following functions are available: ReceivedProductionBillOfMaterial.Process
