# ItemsByManufacturerPartNumber.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemsByManufacturerPartNumber
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 207-208

```baan
DLL:   tdextipuapi
This function is available from 2025.02 (KB3556200).
Syntax: long ItemsByManufacturerPartNumber.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcmpnr           iManufacturerPartNumber,
domain  tcmcs.cmnf       iManufacturer,
domain  tcitem           iItem,
ref     domain  tcmpnr           oManufacturerPartNumber,
ref     domain  tcmcs.cmnf       oManufacturer,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Items by MPN (tdipu0149m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used
iSessionIndex
Specifies the session-index that is to be used.
Supported values:
1: sort by Manufacturer Part Number, Manufacturer, Item (default)
2: sort by Item, Manufacturer Part Number, Manufacturer
iQueryExtend
A specific query to be used when zooming to this session.
iManufacturerPartNumber
Manufacturer Part Number
Mandatory if iStartMode = MODELESS and session-index 1 is used.
iManufacturer
Manufacturer
Mandatory if iStartMode = MODELESS and session-index 1 is used.
iItem
Item
Mandatory if iStartMode = MODELESS and session-index 2 is used.
Output: for iStartMode MODAL:
oManufacturerPartNumber
The selected Manufacturer Part Number
oManufacturer   The selected Manufacturer
oItem           The selected Item
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
