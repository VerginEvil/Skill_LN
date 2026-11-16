# ProductionOrderAdvice.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProductionOrderAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1307-1308

```baan
DLL:   whextinaapi
This function is available from 2023.08 (KB2297822).
Syntax: long ProductionOrderAdvice.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcpdno           iOrderNumber,
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
ref     domain  tcpdno           oOrderNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Production Order
Advice (whina3100m000).
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
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byOrder":
data is displayed by Order
session will be started on index 1
view field: None
"byItem":
data is displayed by Item
session will be started on index 2
view field: Item
"byWarehouse":
data is displayed by Warehouse
session will be started on index 3
view field: Warehouse
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iOrderNumber
The Production Order Advice to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byOrder")
iItem
The Item to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 2 (or iStartFilter = "byItem")
iWarehouse
The Warehouse to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 3 (or iStartFilter = "byWarehouse")
Output: for iStartMode MODAL:
oOrderNumber    - Production Order Advice of selected
record
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
