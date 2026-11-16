# OutboundOrderLine.StatusOverviewStartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1242-1243

```baan
DLL:   whextinhapi
This function is available from 2025.08 (KB3606158).
Syntax: long OutboundOrderLine.StatusOverviewStartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcwset           iOrderSet,
domain  tcitem           iItem,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcorno           oOrderNumber,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Outbound Line
Status Overview (whinh2129m000).
Input:  iStartMode
Specifies the start mode for the session. (Mandatory)
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
view fields: None
"byOrderSet":
data is displayed by Order Set
session will be started on index 6
view fields: Order Origin
Order Number
Order Set
"byItem":
data is displayed by Item
session will be started on index 4
view fields: Item
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
Using the query extend may lead to a "data not found,
session not started" situation. (Optional)
iOrderOrigin
The Order Origin to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 6 (or iStartFilter = "byOrderSet")
iOrderNumber
The Order Number to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 6 (or iStartFilter = "byOrderSet")
iOrderLine
The Order Line to be started. (Optional)
iOrderSequence
The Order Sequence to be started. (Optional)
iOrderSet
The Order Set to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 6 (or iStartFilter = "byOrderSet")
iItem
The Item to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 4 (or iStartFilter = "byItem")
Output:
Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected:
oOrderOrigin    - Order Origin of selected record
oOrderNumber    - Order Number of selected record
oOrderLine      - Order Line of selected record
oOrderSequence  - Order Sequence of selected record
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
